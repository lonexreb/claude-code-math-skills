# Agentic Formal Verification

## Table of Contents
1. [AI-Assisted Theorem Proving](#ai-assisted-theorem-proving)
2. [Neural Network Verification](#neural-network-verification)
3. [Autoformalization](#autoformalization)
4. [LLM + Formal Methods Integration](#llm--formal-methods-integration)
5. [Tools and Frameworks](#tools-and-frameworks)
6. [Key Results and Benchmarks](#key-results-and-benchmarks)

---

## AI-Assisted Theorem Proving

### The Problem
Formal theorem proving is powerful but labor-intensive:
- Average mathlib theorem: 10-50 lines of tactic proof
- Formalizing a textbook chapter: weeks to months
- Proof search space is enormous: which tactic? which arguments?

### Approaches

**1. Tactic Prediction (Next-Step)**
Given proof state, predict the next tactic:
- Input: Goal type, hypotheses, context
- Output: Tactic string (e.g., "apply Nat.add_comm")
- Train on (proof_state, tactic) pairs from mathlib

**2. Whole-Proof Generation**
Generate complete proof from theorem statement:
- Input: Theorem statement in natural language or formal syntax
- Output: Full proof (checked by proof assistant kernel)
- Used by: DeepSeek-Prover, Goedel-Prover

**3. Premise Selection**
Choose which lemmas are likely useful:
- Given: current goal
- Retrieve: relevant theorems from library (mathlib has 150k+)
- Approach: embedding-based retrieval (like RAG for proofs)

**4. Proof Search with Tree Exploration**
Combine tactic prediction with tree search:
- BFS/DFS/MCTS over proof states
- Each node: apply predicted tactic, get new proof state(s)
- Success: reach "no goals" state (proof complete)
- Failure: max depth/time exceeded

---

## Neural Network Verification

### Problem Statement
Given neural network f and input region X, verify property:
∀x ∈ X: f(x) ∈ Y (output in desired range)

Example: "For any image within ε-perturbation of x₀, the classifier still predicts the correct class."

### Approaches

**1. Bound Propagation**
Compute bounds on each layer's output:
- **Interval Bound Propagation (IBP):** Cheapest, loosest bounds
- **CROWN / DeepPoly:** Linear relaxation of nonlinear activations. Tighter.
- **α-CROWN:** Optimizable linear bounds (α parameters learnable)
- **β-CROWN:** Add branch-and-bound for tightest bounds + completeness

**2. SMT-Based**
Encode network + property as SMT formula:
- Marabou: ReLU networks → linear programming + case splits
- Sound and complete (in principle), but slow for large networks

**3. Abstract Interpretation**
Over-approximate network behavior using abstract domains:
- DeepZ: Zonotope domain
- DeepPoly: Combination of zonotope + polyhedral
- PRIMA: Multi-neuron relaxations (tighter than per-neuron)

### Certified Robustness
**Certified radius:** Largest ε such that no adversarial example exists within ε-ball.
- Randomized smoothing: Statistical certification. Works for any classifier.
- Deterministic certification: Bound propagation (α,β-CROWN). Exact for small networks.

### Scalability
| Method | Network Size | Complete? | Speed |
|--------|-------------|-----------|-------|
| IBP | Very large | No | Very fast |
| CROWN | Large | No | Fast |
| α,β-CROWN | Medium-large | Yes (with BaB) | Medium |
| Marabou (SMT) | Small-medium | Yes | Slow |
| ERAN (AI) | Medium | No | Medium |

---

## Autoformalization

### Natural Language → Formal Specification
Translate informal math into formal proof assistant code:
- "For all ε > 0, there exists N such that for all n ≥ N, |aₙ - L| < ε"
- → `∀ ε > 0, ∃ N, ∀ n ≥ N, |a n - L| < ε` (Lean 4)

### Challenges
- Ambiguity in natural language
- Implicit assumptions (e.g., "let f be a function" — what's the domain?)
- Notation varies across textbooks
- Mathematical idiom doesn't map 1:1 to formal syntax

### Current Systems
- **LLMs (GPT-4, Claude) for autoformalization:** Translate NL theorem → Lean/Coq
- **ProofNet:** Benchmark for autoformalization (undergraduate competition math)
- **MMA:** Multilingual Mathematical Autoformalization benchmark
- **Herald:** Autoformalize high-school competition problems

### Informal-to-Formal Pipeline
1. Parse natural language theorem statement
2. LLM generates candidate Lean 4 statement
3. Type-check in Lean (catches most errors)
4. LLM generates candidate proof
5. Lean kernel verifies proof (complete trust)
6. If proof fails → feedback to LLM → retry

---

## LLM + Formal Methods Integration

### Direction 1: LLMs Enhance Formal Methods
- **Tactic prediction:** LLM suggests next proof step
- **Premise selection:** LLM retrieves relevant lemmas
- **Loop invariant synthesis:** LLM proposes invariants, SMT solver checks
- **Specification generation:** LLM writes TLA+ / Hoare logic specs from NL requirements
- **Counterexample explanation:** LLM explains model checker counterexamples in natural language

### Direction 2: Formal Methods Verify LLMs
- **Certified robustness:** Prove adversarial robustness of NN classifiers
- **Runtime monitoring:** Check LLM agent actions against formal safety specs
- **Output verification:** Use formal checkers to validate LLM-generated code/proofs
- **Guaranteed safe AI:** Use world models + formal safety specs to bound agent behavior

### The Hybrid Architecture
```
User (natural language)
    ↓
LLM (informal reasoning, hypothesis generation)
    ↓
Formal System (Lean/Coq/Z3 — rigorous verification)
    ↓
Feedback loop (errors → LLM → revised attempt)
    ↓
Verified result (machine-checked proof / verified property)
```

**Key insight:** LLMs are creative but unreliable. Formal systems are rigid but trustworthy.
The combination gets the best of both: creative proof search with machine-verified correctness.

---

## Tools and Frameworks

### LeanDojo Ecosystem
- **LeanDojo:** Extract data from Lean repos. 122,517 theorems + proofs from mathlib4.
- **ReProver:** Retrieval-augmented prover. Embeds proof states, retrieves relevant premises.
- **LeanCopilot:** Interactive tactic suggestions in VS Code. 74.2% automation rate.
- **LeanAgent:** Lifelong learning — improves by proving theorems across repos.
- License: MIT. GitHub: https://github.com/lean-dojo

### DeepSeek-Prover V2
- Decomposes hard problems into subgoals
- 88.9% on MiniF2F-test
- Uses reinforcement learning (GRPO) on formal proof success
- Open-source: weights + code

### Goedel-Prover V2 (2025)
- 90.4% on MiniF2F (SOTA)
- 86 PutnamBench problems
- Scaffolded data synthesis: generate training proofs via decomposition
- Self-correction: learn from failed proof attempts
- 32B parameter model (80× smaller than alternatives)

### AlphaProof (Google DeepMind)
- IMO 2024: solved 4/6 problems (silver medal level)
- Gemini + AlphaZero-style search in Lean
- Not open-source, but published in Nature (2025)

### COPRA (UT Austin)
- In-context learning agent for Lean/Coq
- No fine-tuning: uses GPT-4 with carefully designed prompts
- Stateful interaction: sends proof state, receives tactic, sends result
- Beats ReProver without any training on proof data

### Neural Network Verification Tools
| Tool | Approach | License | URL |
|------|----------|---------|-----|
| α,β-CROWN | Bound propagation + BaB | BSD 3-Clause | https://github.com/Verified-Intelligence/alpha-beta-CROWN |
| Marabou | SMT-based | BSD-style | https://github.com/NeuralNetworkVerification/Marabou |
| ERAN | Abstract interpretation | Apache 2.0 | https://github.com/eth-sri/eran |
| NNV | MATLAB-based, hybrid | BSD | https://github.com/verivital/nnv |
| nnenum | Exact analysis via star sets | BSD | https://github.com/stanleybak/nnenum |

---

## Key Results and Benchmarks

### MiniF2F Benchmark
244 competition-level math problems formalized in Lean/Isabelle.
| System | MiniF2F-test Score | Year |
|--------|-------------------|------|
| GPT-4 (naive) | ~30% | 2023 |
| ReProver | 53.0% | 2023 |
| DeepSeek-Prover-V1.5 | 63.5% | 2024 |
| InternLM2-Math | 69.6% | 2024 |
| DeepSeek-Prover-V2 | 88.9% | 2025 |
| Goedel-Prover-V2 | 90.4% | 2025 |

### VNN-COMP (Neural Network Verification Competition)
α,β-CROWN has won 5 consecutive years (2021-2025).
Tests: ACAS Xu (collision avoidance), CIFAR/MNIST robustness, RL policies.

### Key Papers
- "LeanDojo: Theorem Proving with Retrieval-Augmented Language Models" — NeurIPS 2023
- "DeepSeek-Prover-V2" — arXiv 2025
- "Goedel-Prover-V2" — arXiv 2025, Princeton/NVIDIA
- "AlphaProof" — Nature 2025, Google DeepMind
- "Towards Guaranteed Safe AI" — arXiv 2024, Bengio/Russell/Tegmark/Seshia et al.
- "Trustworthy AI Agents Require LLMs + Formal Methods" — ICML 2025

### Open Problems
1. Scaling to research-level mathematics (beyond competition problems)
2. Handling creative / non-standard proof strategies
3. Formalizing entire textbooks automatically
4. Real-time verification of LLM agent behavior
5. Combining symbolic reasoning with neural creativity efficiently
6. Verifying properties of transformer architectures themselves
