---
description: Run the harness on a benchmark problem and produce a reproducible run report (JSON + markdown) under benchmarks/runs/.
argument-hint: <benchmark id, e.g. putnam-2023-a1, or "all">
allowed-tools: Read, Write, Bash, Glob, Agent
---

# /math-bench

## Target

$ARGUMENTS

## Resolution

If `$ARGUMENTS` is a single id (e.g. `putnam-2023-a1`), resolve it to `benchmarks/problems/<id>.md`. Read the file. Use the `## Problem` section as input to `/math-solve`.

If `$ARGUMENTS` is `all`, run sequentially over every `.md` in `benchmarks/problems/`.

## Procedure for each problem

1. Note the start time (UTC ISO).
2. Run the same pipeline as `/math-solve`.
3. After the critic approves (or after max rounds), record the run:
   - Output dir: `benchmarks/runs/<id>__<timestamp>/`
   - Files written:
     - `report.md` — final solution + verdict.
     - `meta.json` — `{id, started_at, finished_at, critic_rounds, critic_final_verdict, used_counterexample_hunter, used_numeric_verifier, used_symbol_runner, used_formalizer, total_agent_calls}`.
     - `proof.md` — final approved proof (separate file for diffing across runs).
4. Append one row to `benchmarks/runs/_index.md`:
   `| timestamp | id | verdict | critic rounds | proof path |`

## Final response

A short markdown table summarizing the run(s):

```markdown
| id | verdict | critic rounds | duration |
|---|---|---|---|
| putnam-2023-a1 | APPROVE | 2 | 4m12s |
```

Plus a link to the run dir(s).

## Why this exists

The harness is supposed to *get better*. Without a reproducible bench, we can't tell if a change to a subagent's prompt makes us worse on classical problems. Run `/math-bench all` after meaningful agent edits.
