# Triton GPU Programming

## Table of Contents
1. [What is Triton](#what-is-triton)
2. [Programming Model](#programming-model)
3. [Core Operations](#core-operations)
4. [Common Kernel Patterns](#common-kernel-patterns)
5. [Flash Attention in Triton](#flash-attention-in-triton)
6. [Performance Tuning](#performance-tuning)

---

## What is Triton

Triton is a Python-based language for writing GPU kernels. Created by OpenAI (MIT license).

**Key difference from CUDA:** You program at the BLOCK level, not the thread level.
- In CUDA: you think about what one thread does
- In Triton: you think about what one block of data does (tile-based)
- Triton compiler handles: memory coalescing, shared memory, warp scheduling, register allocation

**When to use Triton vs CUDA:**
- Triton: Custom fused kernels, attention variants, activation functions, normalization
- CUDA: Maximum control needed, non-standard memory patterns, low-level hardware features
- cuBLAS/cuDNN: Standard ops (GEMM, conv) — already highly optimized, don't rewrite

---

## Programming Model

### Basic Structure
```python
import triton
import triton.language as tl
import torch

@triton.jit
def add_kernel(
    x_ptr, y_ptr, output_ptr,
    n_elements,
    BLOCK_SIZE: tl.constexpr,  # Compile-time constant
):
    # Each program instance handles one block of data
    pid = tl.program_id(axis=0)  # Which block am I?
    
    # Compute offsets for this block
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)
    
    # Mask out-of-bounds accesses
    mask = offsets < n_elements
    
    # Load data (entire block at once)
    x = tl.load(x_ptr + offsets, mask=mask)
    y = tl.load(y_ptr + offsets, mask=mask)
    
    # Compute
    output = x + y
    
    # Store
    tl.store(output_ptr + offsets, output, mask=mask)


# Launch
def add(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    output = torch.empty_like(x)
    n = x.numel()
    grid = lambda meta: (triton.cdiv(n, meta['BLOCK_SIZE']),)
    add_kernel[grid](x, y, output, n, BLOCK_SIZE=1024)
    return output
```

### Key Concepts
- **program_id:** Which block of work this instance handles (like blockIdx in CUDA)
- **tl.arange:** Create range of offsets within a block
- **tl.constexpr:** Compile-time constant. Triton compiles one kernel per unique value.
- **mask:** Boolean mask for out-of-bounds protection. ALWAYS use with load/store.
- **grid:** Lambda returning number of program instances to launch.

### Pointer Arithmetic
Triton uses explicit pointer arithmetic (like C, unlike PyTorch):
```python
# 1D access
ptr = base_ptr + offsets

# 2D access (row-major)
ptr = base_ptr + row_offsets[:, None] * stride + col_offsets[None, :]

# Strided access
ptr = base_ptr + indices * stride
```

---

## Core Operations

### Load and Store
```python
x = tl.load(ptr, mask=mask, other=0.0)    # Load with default for masked elements
tl.store(ptr, value, mask=mask)            # Store with mask
```

### Reductions
```python
row_sum = tl.sum(x, axis=1)       # Sum along axis
row_max = tl.max(x, axis=1)       # Max along axis
row_min = tl.min(x, axis=1)       # Min along axis
```

### Math Operations
```python
y = tl.exp(x)           # Elementwise exp
y = tl.log(x)           # Elementwise log
y = tl.sqrt(x)          # Elementwise sqrt
y = tl.sigmoid(x)       # 1 / (1 + exp(-x))
y = tl.where(cond, a, b)  # Conditional select
y = tl.dot(a, b)        # Matrix multiply (uses tensor cores!)
```

### Atomic Operations
```python
tl.atomic_add(ptr, val, mask=mask)
tl.atomic_max(ptr, val, mask=mask)
```

---

## Common Kernel Patterns

### Fused Softmax
```python
@triton.jit
def softmax_kernel(
    output_ptr, input_ptr, input_row_stride, output_row_stride,
    n_cols, BLOCK_SIZE: tl.constexpr
):
    row_idx = tl.program_id(0)
    row_start = row_idx * input_row_stride
    col_offsets = tl.arange(0, BLOCK_SIZE)
    mask = col_offsets < n_cols
    
    # Load row
    row = tl.load(input_ptr + row_start + col_offsets, mask=mask, other=-float('inf'))
    
    # Numerically stable softmax
    row_max = tl.max(row, axis=0)
    numerator = tl.exp(row - row_max)
    denominator = tl.sum(numerator, axis=0)
    softmax_output = numerator / denominator
    
    # Store
    out_start = row_idx * output_row_stride
    tl.store(output_ptr + out_start + col_offsets, softmax_output, mask=mask)
```

### Layer Normalization
```python
@triton.jit
def layernorm_kernel(
    x_ptr, weight_ptr, bias_ptr, out_ptr,
    stride, N, eps,
    BLOCK_SIZE: tl.constexpr,
):
    row = tl.program_id(0)
    offs = tl.arange(0, BLOCK_SIZE)
    mask = offs < N
    
    x = tl.load(x_ptr + row * stride + offs, mask=mask, other=0.0)
    
    # Compute stats
    mean = tl.sum(x, axis=0) / N
    var = tl.sum((x - mean) * (x - mean), axis=0) / N
    
    # Normalize
    x_hat = (x - mean) / tl.sqrt(var + eps)
    
    # Scale + shift
    w = tl.load(weight_ptr + offs, mask=mask)
    b = tl.load(bias_ptr + offs, mask=mask)
    out = x_hat * w + b
    
    tl.store(out_ptr + row * stride + offs, out, mask=mask)
```

### Fused Attention (Simplified)
The core idea: compute softmax(QK^T)V without materializing the N×N attention matrix.

```python
@triton.jit
def attention_kernel(
    Q, K, V, Out,
    stride_qz, stride_qh, stride_qm, stride_qk,
    stride_kz, stride_kh, stride_kn, stride_kk,
    stride_vz, stride_vh, stride_vn, stride_vk,
    stride_oz, stride_oh, stride_om, stride_ok,
    N_CTX, BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr,
    BLOCK_DMODEL: tl.constexpr,
):
    # Each program handles one BLOCK_M chunk of queries
    start_m = tl.program_id(0)
    off_hz = tl.program_id(1)
    
    # Initialize accumulator and running max/sum for online softmax
    m_i = tl.zeros([BLOCK_M], dtype=tl.float32) - float("inf")
    l_i = tl.zeros([BLOCK_M], dtype=tl.float32)
    acc = tl.zeros([BLOCK_M, BLOCK_DMODEL], dtype=tl.float32)
    
    # Load Q block (stays in SRAM for the entire loop)
    # ... load Q tile ...
    
    # Loop over K, V blocks
    for start_n in range(0, N_CTX, BLOCK_N):
        # Load K, V blocks
        # Compute QK^T tile
        # Online softmax update (track running max and sum)
        # Accumulate softmax(QK^T) @ V
        pass
    
    # Store output
    # ... store acc ...
```

---

## Flash Attention in Triton

### The Problem
Standard attention: O(N²) memory for the N×N attention matrix.
For N=8192 with FP16: 8192² × 2 bytes = 128 MB per head. Doesn't fit in SRAM.

### Flash Attention Solution
**Tiling + online softmax:** Never materialize the full attention matrix.

**Algorithm:**
1. Divide Q into blocks of BLOCK_M rows
2. For each Q block, loop over all K, V blocks (BLOCK_N columns)
3. Compute local QK^T (BLOCK_M × BLOCK_N, fits in SRAM)
4. Track running max and sum for numerically stable online softmax
5. Accumulate weighted V contributions

**Key formulas (online softmax):**
```
m_new = max(m_old, max(QK^T_local))
l_new = exp(m_old - m_new) * l_old + sum(exp(QK^T_local - m_new))
acc_new = exp(m_old - m_new) * acc_old + exp(QK^T_local - m_new) @ V_block
```

**Result:** O(N) memory, ~2-4× faster than standard attention by reducing HBM accesses.

### Flash Attention Versions
| Version | Key Improvement | Speed (H100) |
|---------|----------------|---------------|
| Flash Attention 1 | Tiling + online softmax | ~2× over PyTorch |
| Flash Attention 2 | Better work partitioning, reduced non-matmul FLOPs | ~2× over FA1 |
| Flash Attention 3 | Hopper warp specialization, FP8, pipelining | 740 TFLOPs/s (75% peak) |

---

## Performance Tuning

### Autotuning
Triton supports automatic kernel tuning over compile-time constants:

```python
@triton.autotune(
    configs=[
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 64}, num_warps=4),
        triton.Config({'BLOCK_M': 64, 'BLOCK_N': 128}, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 128}, num_warps=8),
    ],
    key=['M', 'N', 'K'],  # Re-tune when these change
)
@triton.jit
def matmul_kernel(..., BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr):
    ...
```

### Benchmarking
```python
@triton.testing.perf_report(
    triton.testing.Benchmark(
        x_names=['N'],
        x_vals=[2**i for i in range(10, 16)],
        line_arg='provider',
        line_vals=['triton', 'torch'],
        line_names=['Triton', 'PyTorch'],
        ylabel='GB/s',
        plot_name='softmax-performance',
    )
)
def benchmark(N, provider):
    x = torch.randn(N, N, device='cuda')
    if provider == 'triton':
        return triton.testing.do_bench(lambda: triton_softmax(x))
    else:
        return triton.testing.do_bench(lambda: torch.softmax(x, dim=-1))
```

### Common Optimization Tips
1. **BLOCK_SIZE should be power of 2** (memory alignment, warp efficiency)
2. **Use tl.dot for matmul** — it maps to tensor cores automatically
3. **Minimize global memory loads** — fuse operations to avoid round-trips
4. **Mask everything** — out-of-bounds loads return garbage without masks
5. **num_warps matters** — more warps = more parallelism but more register pressure
6. **Use autotune** — optimal config varies by GPU and problem size
