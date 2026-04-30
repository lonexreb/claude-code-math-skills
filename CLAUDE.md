# Claude Code Math Skills

This repo is a **harness** for solving rigorous math problems with Claude Code. It bundles:

- A knowledge skill (`skills/formal-math-ai/`) covering real & functional analysis, measure theory, operator theory, plus adjacent terrain (CV / GPU / GenAI / formal verification).
- A roster of specialized math subagents under `.claude/agents/`.
- Slash commands under `.claude/commands/` that orchestrate those agents into a Generator–Critic loop.
- Python helpers under `harness/` for symbolic verification, Lean skeleton emission, and benchmark execution.
- A small benchmark suite under `benchmarks/` (Putnam / IMO / textbook problems) used to dogfood the harness.

## How to use this repo

When the user poses a math problem (proof request, claim verification, "show that...", "is it true that..."), do **not** answer from memory alone. Route through the harness:

| User intent | Slash command |
|---|---|
| Solve / prove a problem end-to-end | `/math-solve` |
| Prove a specific claim | `/math-prove` |
| Disprove / find a counterexample | `/math-disprove` |
| Audit an existing proof | `/math-check` |
| Translate a proof to Lean 4 | `/math-formalize` |
| Run the harness on a benchmark id | `/math-bench` |

The orchestrator commands invoke the subagents in `.claude/agents/`. Each agent has a narrow, well-defined job. Do not bypass the orchestrator unless the user explicitly opts out.

## Hard rules

1. **Cite theorems by name.** Never write "by a standard result". The skill's reference digests in `skills/formal-math-ai/references/` are the canonical source of truth — read the relevant file before quoting a theorem.
2. **State all hypotheses precisely** with explicit quantifiers (∀, ∃) before proving.
3. **Always run a critic pass** (`math-critic` agent) before declaring a proof done. If the critic flags CRITICAL or HIGH issues, fix them, do not handwave.
4. **For existence claims, exhibit a witness or invoke a named existence theorem.**
5. **For "always" claims, run the counterexample hunter first.** Cheap insurance.
6. **Numerical verification is suggestive, not a proof.** `math-numeric-verifier` is a sanity check — never the last word.
7. **When the proof depends on a non-trivial lemma, prove the lemma or cite it precisely** (textbook + theorem number, e.g. "Lebl, *Basic Analysis I* §3.4 Theorem 3.4.5").

## When formal-math-ai skill loads

Read the **Domain Router** in `skills/formal-math-ai/SKILL.md` first. For each domain row that touches the user's problem, read the linked reference file before responding. If the problem touches real analysis, also consult the deep Lebl chunks under `skills/formal-math-ai/references/lebl-basic-analysis-vol1/`.

## When working on the harness itself

- Agents live in `.claude/agents/*.md` with frontmatter (`name`, `description`, `tools`, optional `model`).
- Slash commands live in `.claude/commands/*.md`. They may call agents via the `Agent` tool and run scripts via `Bash`.
- Hooks live in `.claude/settings.json`.
- Python utilities live in `harness/`. They must run on a vanilla `python3` install plus a small `requirements.txt` — no implicit dependencies.

Keep everything in this repo runnable on a fresh clone with `python3 -m venv .venv && pip install -r requirements.txt`.
