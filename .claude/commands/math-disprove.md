---
description: Disprove a claim by finding a counterexample. counterexample-hunter + numeric-verifier first; if both come back clean, fall back to proving the negation.
argument-hint: <claim to disprove>
allowed-tools: Read, Write, Bash, Agent
---

# /math-disprove

The user thinks this claim is **false** (or wants you to confirm it isn't). Hunt a counterexample. If you can't find one, the user has reason to believe their intuition was wrong — escalate to a positive proof of the claim itself.

## Claim

$ARGUMENTS

## Pipeline

### Step 1 — Hunt
Run **in parallel**:
- `math-counterexample-hunter` — full sweep.
- `math-numeric-verifier` — random + boundary numeric tests, if applicable.

### Step 2 — Branch

**If hunter or verifier finds a counterexample:**
- Verify the witness explicitly (re-run the predicate; or hand to `math-symbol-runner` to verify symbolically).
- Report:
  ```markdown
  # Disproof
  
  ## Claim
  …
  
  ## Counterexample
  Witness: …
  Verification: … (numerical + symbolic)
  
  ## Why the claim fails
  Identify which intuition the user likely had and why it doesn't hold.
  ```

**If both come back clean (no counterexample found after sweep):**
- Tell the user: "After a counterexample sweep covering [list of cases], no counterexample surfaced. The claim is plausibly true. Want me to try `/math-prove`?"
- Optionally proceed straight into `/math-prove` if the user's intent suggests they want it either way.

## Hard rules

- ❌ Don't declare a claim false on numeric evidence alone — surface a *specific* witness.
- ❌ Don't declare "no counterexample exists" — only "no counterexample found in sweep".
