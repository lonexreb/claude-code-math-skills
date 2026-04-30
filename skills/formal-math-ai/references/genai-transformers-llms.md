# Transformers and Large Language Models

## Table of Contents
1. [Attention Mechanism](#attention-mechanism)
2. [Transformer Architecture](#transformer-architecture)
3. [GPT and Decoder-Only Models](#gpt-and-decoder-only-models)
4. [Training LLMs](#training-llms)
5. [Alignment: RLHF, DPO, and Beyond](#alignment-rlhf-dpo-and-beyond)
6. [Scaling Laws](#scaling-laws)
7. [Efficient Inference](#efficient-inference)

---

## Attention Mechanism

### Scaled Dot-Product Attention
Attention(Q, K, V) = softmax(QK^T / √d_k) V

- Q (queries), K (keys), V (values): linear projections of input
- √d_k: scaling factor prevents softmax saturation
- Output: weighted sum of values, where weights = similarity of query to keys

### Multi-Head Attention
Split Q, K, V into h heads, run attention independently, concatenate:
MultiHead(Q,K,V) = Concat(head_1,...,head_h) W^O
where head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)

**Why multiple heads?** Each head can attend to different parts of the sequence.
d_model = 768, h = 12 → d_k = d_v = 64 per head (GPT-2).

### Causal (Masked) Attention
For autoregressive generation, mask future positions:
Replace QK^T entries where j > i with -∞ before softmax.
This ensures position i can only attend to positions ≤ i.

### Positional Encoding
Transformers have no built-in notion of position. Solutions:
- **Sinusoidal (original):** PE(pos,2i) = sin(pos/10000^{2i/d}), PE(pos,2i+1) = cos(...)
- **Learned absolute:** Trainable embedding per position (GPT-2)
- **Rotary (RoPE):** Multiply Q, K by rotation matrices encoding relative position. Used in LLaMA, Qwen.
- **ALiBi:** Add linear bias to attention scores proportional to distance. No position embedding needed.

---

## Transformer Architecture

### Encoder-Decoder (Original "Attention Is All You Need")
- **Encoder:** N layers of [Multi-Head Self-Attention → Add&Norm → FFN → Add&Norm]
- **Decoder:** N layers of [Masked Self-Attention → Cross-Attention → FFN], each with Add&Norm
- Cross-attention: decoder queries attend to encoder key-value pairs
- Used in: T5, BART, machine translation

### Decoder-Only (GPT family)
- N layers of [Masked Multi-Head Self-Attention → Add&Norm → FFN → Add&Norm]
- No encoder, no cross-attention
- Autoregressive: predict next token given all previous tokens
- Used in: GPT-2/3/4, LLaMA, Claude, Gemini, Qwen

### Encoder-Only (BERT family)
- N layers of [Multi-Head Self-Attention → Add&Norm → FFN → Add&Norm]
- Bidirectional attention (no causal mask)
- Pre-trained with masked language modeling (MLM)
- Used in: BERT, RoBERTa, DeBERTa (classification, NER, retrieval)

### Feed-Forward Network (FFN)
FFN(x) = GELU(x W₁ + b₁) W₂ + b₂

Modern variants:
- **SwiGLU (LLaMA):** FFN(x) = (Swish(x W₁) ⊙ (x W₃)) W₂ — gated linear unit
- **Mixture of Experts (MoE):** Route each token to top-k of N experts. Sparse computation.

### Normalization
- **Layer Norm (Pre-LN):** Normalize BEFORE attention/FFN. More stable training. Default in modern LLMs.
- **RMSNorm:** Simplified LayerNorm without mean centering. Used in LLaMA: RMSNorm(x) = x / √(mean(x²) + ε) · γ

---

## GPT and Decoder-Only Models

### Architecture Details (LLaMA-2 7B as reference)
- Layers: 32 transformer blocks
- Hidden dim: 4096, FFN dim: 11008
- Heads: 32 attention heads
- Vocab: 32,000 (BPE tokenizer)
- Context: 4096 tokens
- Total params: 6.7B
- Uses: RoPE, SwiGLU FFN, RMSNorm, Pre-LN, Grouped-Query Attention

### Grouped-Query Attention (GQA)
Instead of separate K, V per head (MHA) or shared K, V (MQA):
GQA uses g groups, each group shares K, V. g = 1 → MQA, g = h → MHA.
LLaMA-2 70B uses g = 8 groups for 64 heads.

**Why:** Reduces KV cache size for inference by factor h/g, with minimal quality loss.

### Tokenization
- **BPE (Byte-Pair Encoding):** Iteratively merge frequent character pairs. GPT family.
- **WordPiece:** Similar to BPE. BERT.
- **SentencePiece:** Language-agnostic, operates on raw bytes. LLaMA, T5.

---

## Training LLMs

### Pre-training
Objective: Next-token prediction (causal language modeling)
Loss: L = -Σ log P(x_t | x_{<t})

Data: Trillions of tokens from web crawl, books, code, etc.
Typical recipe: AdamW optimizer, cosine learning rate schedule, gradient clipping, warmup.

### Fine-tuning
**Supervised Fine-Tuning (SFT):** Train on (instruction, response) pairs.
**Parameter-Efficient Fine-Tuning (PEFT):**
- **LoRA:** Add low-rank matrices ΔW = BA (B: d×r, A: r×k, r << d). Train only A, B.
- **QLoRA:** LoRA on 4-bit quantized base model. Enables fine-tuning 65B models on single GPU.
- **Adapters:** Small bottleneck modules inserted between layers.

### Distributed Training
- **Data Parallelism (DDP):** Replicate model on each GPU, split data, all-reduce gradients.
- **Model Parallelism (Tensor):** Split layers across GPUs (Megatron-LM).
- **Pipeline Parallelism:** Different layers on different GPUs (GPipe).
- **FSDP (Fully Sharded):** Shard parameters, gradients, optimizer states across GPUs.
- **DeepSpeed ZeRO:** Stage 1 (shard optimizer), Stage 2 (+gradients), Stage 3 (+parameters).

---

## Alignment: RLHF, DPO, and Beyond

### RLHF (Reinforcement Learning from Human Feedback)
1. **SFT:** Fine-tune base model on demonstrations
2. **Reward Model:** Train classifier on human preference data (response A > response B)
3. **PPO:** Optimize policy (LLM) to maximize reward while staying close to SFT model

PPO Objective: maximize E[r(x,y)] - β · KL(π_θ || π_ref)

### DPO (Direct Preference Optimization)
Reparameterize the RLHF objective to avoid training a separate reward model:
L_DPO = -E[log σ(β(log π_θ(y_w|x)/π_ref(y_w|x) - log π_θ(y_l|x)/π_ref(y_l|x)))]

where y_w = preferred response, y_l = dispreferred response.
**Simpler than RLHF:** No reward model, no RL loop. Just supervised learning on preferences.

### Other Alignment Methods
- **RLAIF:** AI feedback instead of human feedback
- **Constitutional AI:** Self-critique and revision against principles
- **KTO:** Kahneman-Tversky Optimization — only needs binary (good/bad) labels, not pairs
- **ORPO:** Odds Ratio Preference Optimization — combines SFT + preference in one step
- **GRPO:** Group Relative Policy Optimization (DeepSeek) — no critic model needed

---

## Scaling Laws

### Chinchilla Scaling (Hoffmann et al., 2022)
Optimal compute allocation: tokens ≈ 20 × parameters.
- 10B param model → ~200B training tokens
- This was significantly more data than GPT-3 used

### Power Law Relationships
L(N) ∝ N^{-α_N} (loss vs parameters, α_N ≈ 0.076)
L(D) ∝ D^{-α_D} (loss vs data, α_D ≈ 0.095)
L(C) ∝ C^{-α_C} (loss vs compute)

### Emergent Abilities
Capabilities that appear discontinuously at scale:
- Chain-of-thought reasoning (~100B params)
- In-context learning (few-shot)
- Instruction following

Debate: Are these truly emergent or artifacts of evaluation metrics?

---

## Efficient Inference

### KV Cache
During autoregressive generation, cache K, V from previous positions:
- Without cache: each new token recomputes attention over all previous tokens. O(n²).
- With cache: each new token only computes its own Q, reuses cached K, V. O(n) per step.
- Memory cost: 2 × n_layers × n_heads × d_head × seq_len × dtype_size per sequence.

### Quantization
Reduce model precision for faster inference:
- **INT8:** ~2× speedup, minimal quality loss
- **INT4 (GPTQ, AWQ):** ~4× memory reduction, slight quality loss
- **GGUF (llama.cpp):** CPU-friendly quantization formats (Q4_K_M, Q5_K_M, etc.)

### Speculative Decoding
Use a small "draft" model to generate candidate tokens, then verify in parallel with the large model.
If draft matches, accept multiple tokens per step. ~2-3× speedup.

### Inference Frameworks
- **vLLM:** PagedAttention for efficient KV cache management. Best throughput.
- **TensorRT-LLM:** NVIDIA's optimized inference. FP8/INT4 + kernel fusion.
- **llama.cpp:** CPU/GPU inference with quantization. Runs on consumer hardware.
- **SGLang:** Structured generation + RadixAttention for shared prefix caching.
