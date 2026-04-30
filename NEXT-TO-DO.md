# NEXT-TO-DO

Concrete next moves for the harness, in roughly the order they unblock the most impact. Tick items as they ship; promote bigger themes into `docs/ROADMAP.md`.

## High-leverage

- [ ] **SymPy MCP server**
  Wrap `harness/sympy_check.py` into an MCP server so `math-symbol-runner` and `math-numeric-verifier` can keep symbolic state across calls instead of paying subprocess startup per query. Wire via `.claude/settings.json`. Add `mcp__sympy__*` tools to those agents' allowlists. Acceptance: a 5-call calculation chain (define symbols → simplify → integrate → verify → format) runs in one round-trip.

- [ ] **Lean LSP MCP for `math-formalizer`**
  Bring the formalizer from "emit `sorry`-bearing skeletons" to "emit + typecheck incrementally". Needs an `elan`/`lake`-managed mathlib4 next to the repo and an LSP bridge. Acceptance: `/math-formalize` reports a typecheck verdict ("compiles modulo N sorrys") instead of just "not typechecked — no toolchain detected".

- [ ] **Ingest Axler MIRA** (Measure, Integration & Real Analysis, CC BY-NC 4.0)
  Adds measure theory at theorem-level granularity, parallel to the existing Lebl Vol I corpus. Use `setup/convert_pdfs.py --chunk --chunk-strategy theorem --provenance ...`. Add Domain Router rows pointing to the new chunk dir. Update `dominated-convergence-application` benchmark to cite by chunk. **Note:** opendataloader-pdf v2 needs JRE (see project memory); fall through to pymupdf4llm if it isn't installed.

- [ ] **Ingest Lebl Vol II** (Lebesgue / multivariable extension)
  Pairs with Vol I; closes a gap on multivariable / Lebesgue topics. Same pipeline.

- [ ] **Mathlib lemma lookup for the formalizer**
  Local cache of the mathlib4 source under `harness/mathlib_cache/` (gitignored). Add `harness/mathlib_search.py` that grep-searches by lemma signature ("compact + bounded"). The formalizer agent shells out to it when it would otherwise leave a `TODO: locate lemma` comment.

## Agent prompt hardening

- [ ] **Define agent-level failure-mode tests**
  Each of the 7 agents should have ≥ 1 named regression test in `tests/agent_regressions/<agent>.md` describing a known failure mode and a benchmark whose run output should *not* exhibit it. Today the only proxy is `/math-bench all`, which conflates orchestrator and agent issues.

- [ ] **`math-strategist` over-confidence on Putnam/IMO**
  The strategist tends to commit to a single strategy when 3 candidates would give the deep-mode pipeline more lift. Add a "minimum 3 candidates for difficulty ≥ 4" rule and a benchmark guard.

- [ ] **`math-prover` should always cite by chunk id when available**
  Currently the prover sometimes writes "by Bolzano-Weierstrass" without `(Lebl Vol I, Thm 2.3.7)`. Make explicit in the prompt: when the result lives in `references/`, the citation is mandatory; cross-reference `harness/citation_resolve.py`.

- [ ] **`math-counterexample-hunter` numeric vs symbolic**
  The hunter occasionally reports a "numeric counterexample" that's just rounding error. Make explicit: any numeric witness must also pass a symbolic check via `harness.sympy_check`.

- [ ] **`math-critic` over-rejection on stylistic differences**
  Tighten Step 0: linter signals are *triage*, never automatic findings. Add an explicit example of a flagged-but-defensible "trivially" or "similarly".

## Coverage / benchmarks

- [ ] **5 more benchmarks**, picked to stress areas not yet covered:
  - Open Mapping Theorem (functional, difficulty 4)
  - Spectral theorem for compact self-adjoint operators (operator theory, 5)
  - Combinatorial Nullstellensatz application (combinatorics, 4)
  - Picard–Lindelöf existence/uniqueness (ODE, 4)
  - A clean USAMO problem (number-theory or combinatorics, 5)

- [ ] **Reference proofs for the existing 7 benchmarks without one**
  Write canonical solutions for `intermediate-value-bisection` ✅, `cauchy-schwarz-inner-product` ✅, `epsilon-delta-continuity` ✅, `lebl-3-1-7-cauchy-converges` ✅ (already done) — and add the other 7 as time allows. Each must pass `proof_lint` with zero CRITICAL/HIGH.

## Tooling

- [ ] **Z3 / SMT for decidable subgoals**
  When the formalizer hits an arithmetic / propositional-logic subgoal, dispatch via `z3 -smt2 -in` and bake the result into a `decide`-style Lean tactic. Avoids `sorry` for the trivial cases.

- [ ] **Citation linter as a hook**
  PostToolUse hook on `Write|Edit` to `proofs/*.md` runs `harness.proof_lint` and `harness.citation_resolve list`; fails the write if either reports CRITICAL/HIGH or unresolved citations against the local references.

- [ ] **Prover-critic exchange schema**
  Today the contract is informal. Define a JSON schema for prover↔critic exchanges so future automation can run the loop programmatically without an LLM orchestrator.

## Open-source polish

- [ ] **CHANGELOG.md** — start tracking shipped features per commit-cluster.
- [ ] **Demo recording** — short asciicast of `/math-solve` end-to-end on `epsilon-delta-continuity` for the README.
- [ ] **Citation linter exit code policy** — currently `harness.citation_resolve list` exits 1 on any UNRESOLVED. Reconsider: many real textbook citations resolve to chunks that simply weren't extracted. May want to gate only on hallucinated *authors*, not missing chunks.

## Already done this session

For provenance:

- ✅ Self-consistency multi-prover orchestrator (`/math-solve-deep`)
- ✅ No-harness Q&A command (`/math-explain`)
- ✅ Structural proof linter (`harness/proof_lint.py`)
- ✅ Citation resolver (`harness/citation_resolve.py`)
- ✅ 5 canonical proof templates under `templates/proofs/`
- ✅ 4 hand-written reference proofs under `proofs/` with CI gate
- ✅ 4 additional benchmarks (Bolzano–Weierstrass, √2 irrational, infinitude of primes, Banach fixed-point) — 11 total
- ✅ Pytest suite (38 tests), CI on Python 3.10/3.11/3.12
- ✅ `docs/EXTENDING.md` contributor guide
- ✅ GitHub issue + PR templates
- ✅ Fixed: `convert_chunked()` provenance gap
- ✅ Fixed: `datetime.UTC` Python 3.10 incompat in `run_bench.py`
