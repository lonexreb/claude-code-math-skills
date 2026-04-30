---
description: Prove a specific claim. Lighter pipeline than /math-solve — skips counterexample hunting (use /math-disprove for that). Strategist → prover → critic loop.
argument-hint: <claim to prove, formal or informal>
allowed-tools: Read, Write, Bash, Agent
---

# /math-prove

The user is committed to proving the claim. They believe it's true. Don't second-guess them with a counterexample sweep — go straight to construction.

## Claim

$ARGUMENTS

## Pipeline

1. **`math-strategist`** — produce strategy memo.
2. **`math-symbol-runner`** (optional) — only if the claim has algebraic content.
3. **`math-prover`** — write the proof.
4. **`math-critic` loop** (max 3 rounds) — until APPROVE with no CRITICAL/HIGH.
5. Compose the final response.

If the prover returns `BLOCKED: claim may be false`, escalate: tell the user "I tried the proof but kept failing on step X. Should I try /math-disprove instead?" — do not silently flip into a counterexample search.

## Final response shape

```markdown
# Proof

## Claim
…

## Strategy
…

## Proof
…

## Where each hypothesis is used
…

## Critic verdict
APPROVE (round N)
```
