---
description: Multi-prover self-consistency pipeline. Spawns N independent strategist→prover branches in parallel (different strategies, different framings), then has the critic adjudicate the strongest one. Use when the standard /math-solve is brittle on a hard problem.
argument-hint: <problem statement, or path to a benchmark file> [--branches N]
allowed-tools: Read, Write, Bash, Glob, Grep, Agent
---

# /math-solve-deep

For really hard problems, a single prover often picks one strategy and gets stuck. This command runs **N independent prover branches** in parallel and lets the critic pick the strongest one.

## Problem

$ARGUMENTS

(If `$ARGUMENTS` ends with `--branches N`, parse N. Otherwise default N = 3.)

## Pipeline

### Step 0 — Falsification sweep
Same as `/math-solve` step 2: run `math-counterexample-hunter` and `math-numeric-verifier` in parallel. If either disproves the claim, stop and report.

### Step 1 — Generate N strategies
Invoke `math-strategist` **N times in parallel** with the same problem. Each invocation gets a different framing instruction:

- branch 1: "Prefer direct construction. Avoid contradiction."
- branch 2: "Prefer contradiction or contrapositive."
- branch 3: "Prefer reduction to a known textbook theorem (cite by name)."
- branch 4 (if N=4): "Prefer extremal / pigeonhole / counting arguments."

Each branch returns a strategy memo. Branches that agree on the recommended strategy after framing pressure can be collapsed (keep one representative).

### Step 2 — Generate N proofs
For each surviving branch, invoke `math-prover` in parallel with that branch's strategy memo. Each prover writes an independent proof.

### Step 3 — First-round critic on all
For each branch, invoke `math-critic` independently (parallel). Each critic returns severity-classified findings.

### Step 4 — Branch ranking
Rank branches by:
1. Number of CRITICAL findings (fewer is better).
2. Number of HIGH findings.
3. Total proof length (shorter is better, all else equal).
4. Number of named theorem citations (more is generally better, indicates rigor).

Pick the top branch. If multiple tie, prefer the branch with the cleanest critic verdict.

### Step 5 — Refine the winner
Run the standard prover↔critic loop on the winning branch (max 3 critic rounds). Discard losing branches but keep their findings — they may surface a real issue the winner missed.

### Step 6 — Final report

```markdown
# Solution (deep mode, N=<N>)

## Problem
…

## Strategies considered
| branch | strategy | initial CRITICAL | initial HIGH | length |
|---|---|---|---|---|
| 1 | direct construction via … | 0 | 1 | 18 lines |
| 2 | contradiction via Bolzano–Weierstrass | 1 | 0 | 24 lines |
| 3 | reduction to Lebl Thm 3.4.5 | 0 | 0 | 12 lines |  ← winner

## Proof
… (final approved proof from the winning branch)

## What the losing branches caught
- Branch 2's critic flagged: "the contradiction step assumes completeness without invoking it" — relevant; the winning branch did invoke completeness.

## Verification
- Critic verdict: APPROVE (round N on winning branch)
- Falsification sweep: clean
- Numeric sanity: PASS / N/A
```

## When NOT to use

- The problem is easy (`/math-solve` will be faster and cheaper).
- The user is iterating quickly and wants one-shot answers.
- N=1 — that's just `/math-solve`.

## Cost note

This command spends ~N× the tokens of `/math-solve`. Reserve it for problems where the harness has visibly stalled, or for benchmark runs where you want maximum confidence.
