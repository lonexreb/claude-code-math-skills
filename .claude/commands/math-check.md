---
description: Audit a proof the user has written. Pure critic invocation — surfaces gaps, citation errors, quantifier-order bugs, and missing edge cases.
argument-hint: <proof text or path to .md file>
allowed-tools: Read, Write, Bash, Agent
---

# /math-check

The user has written a proof and wants a rigorous review. Run the critic.

## Proof to audit

$ARGUMENTS

(If `$ARGUMENTS` is a file path, read it.)

## Pipeline

1. **`math-critic`** — full review with severity-classified findings.
2. (Optional) If critic flags "claim may be false", run `math-counterexample-hunter` to confirm.
3. (Optional) If critic flags "computation suspicious", run `math-numeric-verifier` or `math-symbol-runner`.

## Final response shape

```markdown
# Audit

## Verdict
APPROVE / REVISE / REJECT

## Findings
### CRITICAL
…
### HIGH
…
### MEDIUM
…
### LOW
…

## Recommended next action
- (e.g.) "Strengthen step 4 with explicit invocation of completeness."
- (e.g.) "Hypothesis B appears unused — claim may be stronger than stated."
```

If the user wants the gaps actually filled, they should follow up with `/math-prove` on the patched claim.
