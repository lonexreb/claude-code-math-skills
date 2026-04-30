---
description: End-to-end math problem solver. Routes through strategist → counterexample-hunter (if applicable) → numeric-verifier (if applicable) → prover → critic loop → optional formalizer. The flagship command of the harness.
argument-hint: <problem statement, or path to a benchmark file>
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent
---

# /math-solve

The user gave us a math problem. Run the full harness.

## Problem

$ARGUMENTS

(If `$ARGUMENTS` is a path to a `benchmarks/problems/*.md` file, read that file and use its `## Problem` section as the problem statement.)

## Pipeline

Execute these steps **in order**. Use the `Agent` tool to invoke the named subagent. Pass each agent the prior agents' outputs as context.

### Step 1 — Strategy
Invoke `math-strategist` with the problem. Receive a strategy memo.

### Step 2 — Cheap falsification
If the strategy memo says "Counterexample sweep recommended? Yes" **or** the problem is a `∀`-statement we have no strong prior on:
- Invoke `math-counterexample-hunter` in parallel with step 3.
- If a counterexample is returned, **stop** the prove path and report the disproof to the user with the witness.

If the claim has concrete numerical content (closed forms, inequalities, integrals, sums):
- Invoke `math-numeric-verifier` in parallel.
- If `FAIL`, stop and report numerical disproof.

### Step 3 — Symbolic precomputation (optional)
If the problem reduces to an algebraic / calculus computation, invoke `math-symbol-runner` to compute the closed form before the prover writes the proof. Pass its output forward.

### Step 4 — Proof generation
Invoke `math-prover` with:
- The original problem.
- The strategy memo.
- The list of reference files the strategist named.
- Any symbol-runner output.

If the prover returns `BLOCKED`:
- If the block is "missing lemma", invoke a fresh `math-strategist` round with the gap as context.
- If the block is "claim may be false", run `math-counterexample-hunter` deeper.

### Step 5 — Critic loop
Invoke `math-critic` on the proof.
- If verdict is `APPROVE` and there are no CRITICAL or HIGH findings: proceed to step 6.
- Otherwise: pass the critic's findings back to `math-prover` for revision. **Maximum 3 critic rounds.** If the critic still rejects after round 3, surface the open findings to the user and stop — do not ship a proof the critic doesn't approve.

### Step 6 — (Optional) Formalization
If the user asked for Lean output, or the orchestrator detects `formalize: true` in the problem file, invoke `math-formalizer` with the approved proof.

### Step 7 — Final report
Compose a single response to the user:

```markdown
# Solution

## Problem
…

## Strategy
… (1-paragraph distillation of the strategist memo)

## Proof
… (the approved proof verbatim)

## Where each hypothesis is used
… (from the prover's coda)

## Verification
- Critic verdict: APPROVE (round N)
- Numeric sanity check: PASS / N/A
- Counterexample sweep: clean / N/A
- Lean skeleton: <link or omit>

## Remaining open items
- Any MEDIUM critic findings the user may want to address.
- Any sorry'd subgoals in the Lean output.
```

## Loop guards

- Each agent invocation must complete before chaining the next that depends on it. Independent steps (counterexample hunter + numeric verifier) may run in parallel.
- If the same prover↔critic exchange repeats without progress (the critic flags the same finding twice), break out and report the impasse — don't burn the loop.

## When NOT to use

- The user is asking *about* a result, not for a proof of one ("explain Banach-Steinhaus" → just answer using the skill, no harness needed).
- The user wants a quick definition or a worked example from a textbook.
- The user is debugging code, not math.

In those cases, answer directly with the skill's references and skip the harness.
