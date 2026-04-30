# Benchmarks

Each `problems/<id>.md` is a self-contained benchmark for the harness. The orchestrator (`/math-bench`) reads the `## Problem` section, runs the full pipeline, and writes a reproducible report under `runs/<id>__<timestamp>/`.

## Problem file schema

```markdown
---
id: <slug>
domain: <real-analysis | combinatorics | number-theory | …>
difficulty: <1–5>
source: <where the problem comes from>
formalize: <true|false>            # whether /math-bench should also emit Lean
---

# <Title>

## Problem
<the problem statement, formal or informal>

## Reference solution (optional)
<a sketch — used only for human review, not fed to the harness>

## Notes (optional)
<known gotchas / common wrong proofs / what makes this benchmark interesting>
```

## Running

```
/math-bench <id>          # one problem
/math-bench all           # everything in problems/
```

Reports land under `runs/<id>__<UTC ts>/`:

- `meta.json` — machine-readable run metadata
- `report.md` — human-readable solution + verdict
- `proof.md` — the final approved proof, separate for diffing across runs

A summary index at `runs/_index.md` is appended on every run.

## Seed benchmarks

Designed to exercise different agents and surface different failure modes.

| id | domain | difficulty | exercises |
|---|---|---|---|
| `lebl-3-1-7-cauchy-converges` | real-analysis | 2 | reading from `lebl-basic-analysis-vol1/`, citing existence theorems |
| `epsilon-delta-continuity` | real-analysis | 1 | quantifier discipline, ε-δ template |
| `dominated-convergence-application` | measure-theory | 4 | hypothesis verification at the citation point |
| `putnam-2023-a1` | combinatorics | 4 | pattern recognition + clean argument |
| `imo-2023-p1` | number-theory | 5 | prime / factorial reasoning |
| `intermediate-value-bisection` | real-analysis | 2 | tightness check, completeness invocation |
| `cauchy-schwarz-inner-product` | linear-algebra | 2 | algebraic identity, equality case |
