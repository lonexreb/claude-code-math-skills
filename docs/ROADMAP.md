# Roadmap

## v0.1 — current

- 7-agent roster (strategist, prover, counterexample-hunter, numeric-verifier, critic, formalizer, symbol-runner)
- 6 slash commands (`/math-solve`, `/math-prove`, `/math-disprove`, `/math-check`, `/math-formalize`, `/math-bench`)
- Knowledge skill with 334-chunk Lebl corpus + 16 hand-written digests
- Python harness: SymPy CLI, Lean skeleton emitter, benchmark scaffolding
- 7 seed benchmark problems

## v0.2 — short term

- **Self-consistency voting**: run prover N times in parallel with different strategies, vote/merge in critic.
- **Wire `convert_chunked()` provenance bug** flagged in skill memory — chunked conversions don't currently log to `SOURCES.md`.
- **Ingest Lebl Vol II** (Lebesgue / multivariable) into `references/lebl-basic-analysis-vol2/`.
- **Mathlib lemma lookup tool** for `math-formalizer` — local cache of mathlib4 with grep.
- **Hook: auto-run `math-critic`** when a `proofs/*.md` file is written outside `/math-solve`.

## v0.3 — medium term

- **MCP integration**: SymPy MCP server, Lean LSP MCP server. Frees agents from Bash subprocess for repeated symbolic / typecheck calls.
- **Z3 integration** for SMT-decidable subgoals in formalizer.
- **Counterexample auto-construction**: when hunter fails to find one, hand a candidate hypothesis to a SAT/SMT-style search.
- **Citation linter**: post-prover hook that verifies every "(textbook §X)" citation actually resolves to a real chunk.

## v0.4+ — long term

- **Tree search at the prover**: maintain candidate proofs in a beam; critic prunes; reorder by score.
- **AlphaProof-style integration with Lean**: closed-loop training/distillation against benchmark suite.
- **CV / GPU / GenAI sub-harnesses**: the same Generator–Critic shape applied to CUDA kernel correctness or attention math.
- **Multi-agent debate**: two prover agents argue opposite claims; critic adjudicates.

## Tracking

Open questions and design notes go in `docs/NOTES.md` (created lazily). Major decisions get an ADR in `docs/adr/`.
