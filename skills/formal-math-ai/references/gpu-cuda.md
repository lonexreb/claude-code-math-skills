# GPU Architecture and CUDA Programming

## Table of Contents
1. [GPU Architecture](#gpu-architecture)
2. [CUDA Programming Model](#cuda-programming-model)
3. [Memory Hierarchy](#memory-hierarchy)
4. [Execution Model and Warps](#execution-model-and-warps)
5. [Performance Optimization](#performance-optimization)
6. [Synchronization and Atomics](#synchronization-and-atomics)
7. [Advanced Patterns](#advanced-patterns)

---

## GPU Architecture

### Streaming Multiprocessors (SMs)
A GPU consists of many SMs (e.g., A100: 108 SMs, H100: 132 SMs).
Each SM contains:
- CUDA cores (FP32/FP64/INT32 units)
- Tensor cores (matrix multiply units for mixed-precision)
- Register file (65,536 32-bit registers per SM on Ampere)
- Shared memory / L1 cache (configurable, up to 164 KB on A100)
- Warp schedulers (4 per SM on Ampere)
- Load/store units

### Architecture Comparison
| Feature | Ampere (A100) | Hopper (H100) | Blackwell (B200) |
|---------|--------------|---------------|-----------------|
| SMs | 108 | 132 | 192 |
| FP32 TFLOPs | 19.5 | 67 | 144 |
| FP16 Tensor TFLOPs | 312 | 989 | 2250 |
| HBM | 80GB HBM2e | 80GB HBM3 | 192GB HBM3e |
| Memory BW | 2.0 TB/s | 3.35 TB/s | 8.0 TB/s |
| L2 Cache | 40 MB | 50 MB | 98 MB |

### Tensor Cores
Specialized units for matrix multiply-accumulate: D = A × B + C
- Operate on small matrix tiles (e.g., 16×16×16 for FP16)
- FP16/BF16 inputs → FP32 accumulator (mixed precision)
- FP8 support on Hopper/Blackwell for inference
- Used by: cuBLAS, cuDNN, CUTLASS, Flash Attention

---

## CUDA Programming Model

### Thread Hierarchy
```
Grid (of blocks)
  └── Block (of threads)
        └── Thread
```

- **Thread:** Executes kernel code. Has unique threadIdx (within block).
- **Block:** Group of threads. Max 1024 threads. Has unique blockIdx.
- **Grid:** Group of blocks. Can be 1D, 2D, or 3D.

```cuda
__global__ void kernel(float* A, float* B, float* C, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N) {
        C[idx] = A[idx] + B[idx];
    }
}

// Launch: grid_size blocks, block_size threads per block
int block_size = 256;
int grid_size = (N + block_size - 1) / block_size;
kernel<<<grid_size, block_size>>>(A, B, C, N);
```

### Kernel Launch Configuration
- **blockDim:** Threads per block. Multiple of 32 (warp size). 128 or 256 typical.
- **gridDim:** Blocks per grid. ceil(N / blockDim).
- Too few blocks → low occupancy. Too many threads/block → fewer blocks per SM.

### Thread Indexing Patterns
```cuda
// 1D
int i = blockIdx.x * blockDim.x + threadIdx.x;

// 2D
int row = blockIdx.y * blockDim.y + threadIdx.y;
int col = blockIdx.x * blockDim.x + threadIdx.x;

// 2D with stride (grid-stride loop)
for (int i = blockIdx.x * blockDim.x + threadIdx.x;
     i < N;
     i += blockDim.x * gridDim.x) { ... }
```

---

## Memory Hierarchy

### Memory Types (fastest → slowest)
| Memory | Scope | Lifetime | Size | Latency | Bandwidth |
|--------|-------|----------|------|---------|-----------|
| Registers | Thread | Thread | ~255 per thread | 0 cycles | — |
| Shared memory | Block | Block | 48-164 KB/SM | ~5 cycles | ~19 TB/s |
| L1 cache | SM | Automatic | Shared w/ smem | ~30 cycles | ~19 TB/s |
| L2 cache | Device | Automatic | 40-50 MB | ~200 cycles | ~6 TB/s |
| Global memory (HBM) | Device | Application | 40-80 GB | ~400 cycles | 2-3.35 TB/s |
| Constant memory | Device | Application | 64 KB | ~5 cy (cached) | Broadcast |

### Memory Coalescing
Global memory is accessed in 32/128-byte transactions.
**Coalesced access:** Consecutive threads access consecutive addresses.

```cuda
// GOOD — coalesced (thread i reads A[i])
float val = A[threadIdx.x];

// BAD — strided (thread i reads A[i * stride])
float val = A[threadIdx.x * stride];  // Wastes bandwidth

// BAD — random access
float val = A[indices[threadIdx.x]];  // No coalescing
```

### Shared Memory
Fastest programmable memory. Shared within a block.

```cuda
__shared__ float tile[BLOCK_SIZE][BLOCK_SIZE];
tile[threadIdx.y][threadIdx.x] = A[row * N + col];
__syncthreads();  // REQUIRED before reading other threads' data
// Now all threads can read any element of tile
```

**Bank conflicts:** Shared memory has 32 banks. If multiple threads in a warp access
different addresses in the same bank, accesses serialize. Padding can help:
```cuda
__shared__ float tile[32][33];  // Pad to avoid bank conflicts
```

---

## Execution Model and Warps

### Warp
32 threads executing in lockstep (SIMT). The fundamental scheduling unit.
- All threads in a warp execute the same instruction at the same time
- Divergent branches → both paths executed, inactive threads masked
- Warp-level primitives: `__shfl_sync`, `__ballot_sync`, `__reduce_sync`

### Warp Divergence
```cuda
// BAD — half the warp is idle each branch
if (threadIdx.x % 2 == 0) { do_A(); }
else { do_B(); }

// BETTER — divergence at warp boundaries
if (threadIdx.x < 32) { do_A(); }
else { do_B(); }
```

### Occupancy
Occupancy = active warps / maximum warps per SM.

Limited by:
- Registers per thread (more registers → fewer concurrent threads)
- Shared memory per block (more smem → fewer concurrent blocks)
- Block size (max 1024 threads, max 32 blocks per SM on Ampere)

Use: `cudaOccupancyMaxPotentialBlockSize` to find optimal launch config.
Use: NVIDIA Nsight Compute for occupancy analysis.

---

## Performance Optimization

### The APOD Workflow (NVIDIA recommended)
1. **Assess:** Profile to find bottlenecks (Nsight Systems for timeline, Nsight Compute for kernels)
2. **Parallelize:** Identify parallelism. Use CUDA/Triton.
3. **Optimize:** Memory access patterns, occupancy, instruction throughput.
4. **Deploy:** Verify correctness, benchmark, integrate.

### Arithmetic Intensity and Roofline Model
Arithmetic Intensity = FLOPs / Bytes transferred

- **Compute-bound:** AI > machine's ops:byte ratio. Optimize FLOPs.
- **Memory-bound:** AI < machine's ops:byte ratio. Optimize memory access.

A100: ~312 TFLOPS (FP16) / 2.0 TB/s = ~156 ops/byte threshold.
Most operations (elementwise, reduction, softmax) are memory-bound.

### Mixed Precision Training
- Forward: FP16/BF16 (faster, less memory)
- Accumulation: FP32 (prevents loss of precision)
- Loss scaling: Scale loss up before backward → scale gradients down after
- Master weights: Keep FP32 copy for optimizer step

```python
# PyTorch automatic mixed precision
scaler = torch.amp.GradScaler('cuda')
with torch.amp.autocast('cuda', dtype=torch.bfloat16):
    output = model(input)
    loss = criterion(output, target)
scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()
```

### Kernel Fusion
Combine multiple operations into one kernel to avoid memory round-trips.
Example: LayerNorm = mean + variance + normalize + scale + shift → 1 kernel instead of 5.

### Common Anti-Patterns
- Excessive host-device transfers (cudaMemcpy)
- Launching tiny kernels (launch overhead dominates)
- Uncoalesced memory access
- Register spilling (too many local variables)
- Not using async operations (streams, cudaMemcpyAsync)

---

## Synchronization and Atomics

### Synchronization Levels
- **__syncthreads():** Block-level barrier. All threads in block must reach it.
- **__syncwarp():** Warp-level barrier (Volta+). Needed after warp-level communication.
- **cudaDeviceSynchronize():** Host-device barrier. Blocks CPU until all GPU work done.
- **cudaStreamSynchronize():** Wait for specific stream.

### Atomic Operations
```cuda
atomicAdd(&address, value);    // Thread-safe addition
atomicMax(&address, value);    // Thread-safe maximum
atomicCAS(&address, compare, value);  // Compare-and-swap (build any atomic)
```

Atomics are slow when many threads contend on same address. Use hierarchical reduction instead.

### CUDA Streams
```cuda
cudaStream_t s1, s2;
cudaStreamCreate(&s1);
cudaStreamCreate(&s2);
kernel1<<<grid, block, 0, s1>>>(a);  // Runs on stream 1
kernel2<<<grid, block, 0, s2>>>(b);  // Runs concurrently on stream 2
```

---

## Advanced Patterns

### Parallel Reduction
Sum N elements: O(log N) steps using tree reduction.

```cuda
__shared__ float sdata[BLOCK_SIZE];
sdata[tid] = input[global_id];
__syncthreads();

for (int s = blockDim.x / 2; s > 0; s >>= 1) {
    if (tid < s) sdata[tid] += sdata[tid + s];
    __syncthreads();
}
if (tid == 0) output[blockIdx.x] = sdata[0];
```

Warp-level optimization: last 32 threads use `__shfl_down_sync` instead of shared memory.

### Tiled Matrix Multiplication
Load tiles of A and B into shared memory, compute partial products, accumulate.
Reduces global memory accesses from O(N³) to O(N³/TILE_SIZE).

### Prefix Sum (Scan)
Blelloch algorithm: up-sweep + down-sweep on shared memory.
Used in: stream compaction, radix sort, histogram equalization.

### CUB and Thrust
Don't reinvent the wheel:
- **CUB:** Block/device-level primitives (reduce, scan, sort, histogram)
- **Thrust:** High-level algorithms (sort, reduce, transform) with STL-like API
- Both in NVIDIA's CCCL library (Apache 2.0)
