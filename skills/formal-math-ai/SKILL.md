---
name: formal-math-ai
description: >
  Comprehensive skill for rigorous work across mathematics, computer vision, GPU programming,
  generative AI, and formal verification. Use this skill whenever the user asks about:
  MATH — real analysis, functional analysis, measure theory, operator theory, epsilon-delta proofs,
  convergence, compactness, Banach/Hilbert spaces, spectral theory, Lp spaces, or any graduate
  analysis topic. CV — classical computer vision (SIFT, optical flow, stereo, SLAM, epipolar geometry),
  or deep learning CV (CNNs, ViTs, YOLO, DETR, segmentation, NeRF, depth estimation, video understanding).
  GPU — CUDA kernels, Triton programming, GPU architecture (warps, SMs, memory hierarchy, tensor cores),
  mixed precision, FlashAttention, kernel fusion, profiling, occupancy optimization.
  GENAI — transformers, attention, LLMs, GPT architecture, RLHF, DPO, diffusion models (DDPM, DDIM,
  score matching), VAEs, GANs, RAG, agentic AI (ReAct, tool use, multi-agent systems).
  FORMAL — theorem proving (Lean 4, Coq, Isabelle), model checking (TLA+, temporal logic), SAT/SMT (Z3),
  Hoare logic, separation logic, dependent types, program verification.
  AGENTIC-FV — LLM-assisted theorem proving (LeanDojo, ReProver, AlphaProof), neural network verification
  (α,β-CROWN, Marabou, ERAN), autoformalization, verified AI systems.
  Trigger even if the user doesn't name the field explicitly — e.g. "prove this converges",
  "write a CUDA kernel", "explain Flash Attention", "verify this loop invariant".
---

# Formal Math & AI Skill

## How This Skill Works

This skill contains curated reference knowledge across 7 domains, organized as `.md` files.
**Read the relevant reference file(s) BEFORE responding.** Many problems span multiple domains.

## Domain Router

| User's Problem Domain | Reference File(s) to Read |
|----------------------|--------------------------|
| Sequences, continuity, topology of ℝ, Riemann integration | `references/real-analysis-foundations.md` (digest); `references/lebl-basic-analysis-vol1.md` (deep, 334 theorem chunks) |
| Measure theory, Lebesgue integration, convergence theorems | `references/measure-integration.md` |
| Normed/Banach/Hilbert/Lp spaces, orthogonality, ONBs | `references/hilbert-banach-spaces.md` |
| Bounded operators, Hahn-Banach, Open Mapping, weak topologies | `references/functional-analysis-core.md` |
| Compact operators, spectral theory, Fredholm theory | `references/operator-theory.md` |
| Proof strategy, counterexamples, ε-δ templates | `references/proof-techniques.md` |
| Classical CV: features, stereo, optical flow, SLAM, geometry | `references/cv-classical.md` |
| Deep learning CV: CNNs, ViTs, detection, segmentation, 3D | `references/cv-deep-learning.md` |
| CUDA kernels, GPU architecture, memory hierarchy, profiling | `references/gpu-cuda.md` |
| Triton programming, kernel fusion, Flash Attention impl | `references/gpu-triton.md` |
| Transformers, LLMs, RLHF, scaling laws | `references/genai-transformers-llms.md` |
| Diffusion models, VAEs, GANs, generative foundations | `references/genai-diffusion-generative.md` |
| RAG, agentic AI, tool use, multi-agent systems | `references/genai-agents-rag.md` |
| Theorem proving: Lean 4, Coq, Isabelle/HOL | `references/fv-theorem-proving.md` |
| Model checking: TLA+, temporal logic, SAT/SMT, Z3 | `references/fv-model-checking.md` |
| LLM + formal methods: LeanDojo, neural net verification | `references/agentic-formal-verification.md` |

## Response Standards

### For Mathematical Proofs
1. State the claim precisely with all hypotheses
2. Proof strategy in 1-2 sentences
3. Rigorous proof with explicit quantifiers (∀, ∃)
4. Key insight — what makes this work?
5. Where each hypothesis is used
6. Counterexample if a hypothesis is dropped

### For Code (CUDA/Triton/Python)
1. Explain the algorithmic idea first
2. Write commented, production-quality code
3. Note performance characteristics (memory, compute, bandwidth)
4. Flag common pitfalls (race conditions, bank conflicts, etc.)
5. Suggest profiling/benchmarking approach

### For System Design (CV pipelines, agent architectures)
1. Architecture diagram or description
2. Component-by-component breakdown
3. Trade-offs between approaches
4. Concrete implementation path with libraries/tools

### For Formal Verification
1. Identify the right formalism (temporal logic, Hoare logic, dependent types)
2. Write specifications precisely
3. Sketch the proof strategy
4. Note automation opportunities (tactics, solvers)
5. Link to relevant tools (Z3, Lean, TLA+)

## Rigor Checklist (always verify before responding)
- [ ] Every quantifier is explicit and correctly ordered
- [ ] Named theorems are cited, not "by a standard result"
- [ ] Edge cases checked (empty set, zero, trivial, n=1)
- [ ] Completeness/compactness assumptions verified
- [ ] Measurability verified for measure-theoretic claims
- [ ] Memory model correct for GPU code (shared vs global, coalescing)
- [ ] Soundness of verification approach (no circular reasoning)

## Adding New Reference Content

Use the included `setup/convert_pdfs.py` script to convert any PDF textbook to
chunked .md files. The pipeline supports LaTeX-aware post-processing, quality
validation, and academic-structure-aware chunking:

```bash
# Install the PDF converter
pip install opendataloader-pdf --break-system-packages

# Basic conversion (auto-detects math, validates quality)
python setup/convert_pdfs.py -i /path/to/book.pdf -o references/new-topic.md

# Academic math textbook with theorem-aware chunking
python setup/convert_pdfs.py -i /path/to/analysis-book.pdf \
  --output-dir references/ --chunk --chunk-strategy theorem

# Skip LaTeX post-processing (for non-math content like CV or GPU)
python setup/convert_pdfs.py -i /path/to/cv-book.pdf -o references/cv-topic.md \
  --no-math-aware

# Track provenance (appends metadata to SOURCES.md)
python setup/convert_pdfs.py -i /path/to/book.pdf -o references/topic.md \
  --provenance references/SOURCES.md
```

See `setup/README.md` for engine installation, validation, and workflow details.

<!-- To add a new domain entry after conversion:
     1. Convert the PDF using the command above
     2. Add a row to the Domain Router table above
     3. Update references/SOURCES.md with source URL and license -->

## Open-Access Sources

All reference content is informed by CC-licensed or freely available sources.
See `references/SOURCES.md` for the full list with URLs, licenses, and coverage descriptions.
