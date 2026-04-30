# Claude Code Math Skills

This repo is a **harness** for solving rigorous math problems with Claude Code. It bundles:

- A knowledge skill (`skills/formal-math-ai/`) covering real & functional analysis, measure theory, operator theory, plus adjacent terrain (CV / GPU / GenAI / formal verification). Includes a 334-chunk Lebl Vol I corpus.
- A roster of seven specialized math subagents under `.claude/agents/`.
- Eight slash commands under `.claude/commands/` that orchestrate those agents into a Generator–Critic loop.
- Python helpers under `harness/`: SymPy smoke tests, Lean 4 skeleton emission, structural proof linting, citation resolution, and benchmark scaffolding.
- Five canonical proof templates under `templates/proofs/` (ε–δ, induction, contradiction, bisection, discriminant).
- Four hand-written reference proofs under `proofs/` that establish the rigor bar (CI fails if any accumulates a CRITICAL/HIGH `proof_lint` finding).
- Eleven benchmark problems under `benchmarks/problems/` (textbook + Putnam + IMO) used to dogfood the harness.

## How to use this repo

When the user poses a math problem (proof request, claim verification, "show that...", "is it true that..."), do **not** answer from memory alone. Route through the harness:

| User intent | Slash command |
|---|---|
| Solve / prove a problem end-to-end | `/math-solve` |
| Hard problem; spend more tokens on N parallel branches | `/math-solve-deep` |
| Prove a specific claim | `/math-prove` |
| Disprove / find a counterexample | `/math-disprove` |
| Audit an existing proof | `/math-check` |
| Translate a proof to Lean 4 | `/math-formalize` |
| Run the harness on a benchmark id | `/math-bench` |
| Just look up / explain a result (no harness) | `/math-explain` |

The orchestrator commands invoke the subagents in `.claude/agents/`. Each agent has a narrow, well-defined job. Do not bypass the orchestrator unless the user explicitly opts out.

## Hard rules

1. **Cite theorems by name.** Never write "by a standard result". The skill's reference digests in `skills/formal-math-ai/references/` are the canonical source of truth — read the relevant file before quoting a theorem. Use canonical citation form `(Author Vol X, Thm A.B.C)` so `harness.citation_resolve` can map to the chunk file.
2. **State all hypotheses precisely** with explicit quantifiers (∀, ∃) before proving.
3. **Always run a critic pass** (`math-critic` agent) before declaring a proof done. The critic runs `harness.proof_lint` as Step 0 and `harness.citation_resolve` on any flagged citation. Fix CRITICAL/HIGH findings — do not handwave.
4. **For existence claims, exhibit a witness or invoke a named existence theorem.**
5. **For "always" claims, run the counterexample hunter first.** Cheap insurance.
6. **Numerical verification is suggestive, not a proof.** `math-numeric-verifier` is a sanity check — never the last word.
7. **When the proof depends on a non-trivial lemma, prove the lemma or cite it precisely** (textbook + theorem number, e.g. "Lebl, *Basic Analysis I* §3.4 Theorem 3.4.5").
8. **The reference proofs under `proofs/` are the rigor bar.** Output should match or exceed their cleanliness: zero CRITICAL/HIGH `proof_lint` findings, every load-bearing citation in canonical form, an explicit "where each hypothesis is used" coda, and a tightness check.

## When formal-math-ai skill loads

Read the **Domain Router** in `skills/formal-math-ai/SKILL.md` first. For each domain row that touches the user's problem, read the linked reference file before responding. If the problem touches real analysis, also consult the deep Lebl chunks under `skills/formal-math-ai/references/lebl-basic-analysis-vol1/`.

## When working on the harness itself

- Agents live in `.claude/agents/*.md` with frontmatter (`name`, `description`, `tools`, optional `model`).
- Slash commands live in `.claude/commands/*.md`. They may call agents via the `Agent` tool and run scripts via `Bash`.
- Hooks live in `.claude/settings.json`.
- Python utilities live in `harness/`. They must run on a vanilla `python3 ≥ 3.10` install plus `requirements.txt` — no implicit dependencies. CI matrix is 3.10 / 3.11 / 3.12, so avoid version-only features (e.g. `datetime.UTC` is 3.11+ — use `datetime.timezone.utc`).
- Tests under `tests/` use pytest. Add `tests/test_<module>.py` for any new harness CLI. The full suite runs in under a second; keep it that way.
- The `templates/proofs/*.md` skeletons are scaffolding for the prover's reasoning, not output shape — the prover does **not** mention which template was used.
- See `docs/EXTENDING.md` for the concrete "how to add an agent / command / benchmark / reference / utility" walkthrough.
- `NEXT-TO-DO.md` tracks the active shortlist; bigger initiatives live in `docs/ROADMAP.md`.

Keep everything in this repo runnable on a fresh clone with `python3 -m venv .venv && pip install -r requirements.txt`.
