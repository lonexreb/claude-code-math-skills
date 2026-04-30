# Cookbook

Worked examples of the harness in action. Each recipe shows: the user's prompt, the agents the orchestrator invokes, what each one returns, and the final shape of the response.

These are *illustrative*. Actual agent output will vary; the structure shouldn't.

## Recipe 1 — Prove a textbook classic (`/math-solve`)

**User**: `/math-solve Show that f(x) = x² is continuous at every c ∈ ℝ.`

**Step 1 — `math-strategist`** returns:

```markdown
## Domain
- primary: real-analysis (pointwise continuity)

## Load-bearing obligation
∀ε > 0, ∃δ > 0, ∀x ∈ ℝ, |x − c| < δ ⇒ |x² − c²| < ε.

## Recommended
ε–δ direct construction. Use the factoring |x² − c²| = |x − c| · |x + c|, bound |x + c| by 1 + 2|c| under the constraint |x − c| < 1.

## Reference files to read
- skills/formal-math-ai/references/real-analysis-foundations.md
- skills/formal-math-ai/references/lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-definition-3-2-1.md
```

**Step 2 — falsification sweep** (parallel):

- `math-counterexample-hunter`: "Claim is the canonical example of pointwise continuity for a polynomial. No counterexample expected. Verified n = 0, 1, c = 0, ±1 cases — all hold."
- `math-numeric-verifier`: `PASS` (consistent, 200 samples, seed 12345).

**Step 3 — `math-prover`** writes the proof using the `epsilon-delta.md` template skeleton (without mentioning the template).

**Step 4 — `math-critic`** runs `proof_lint` first, surfaces 0 HIGH findings, then reads line-by-line and returns `APPROVE` (round 1).

**Final response**: clean ε–δ proof with the δ derivation explicit, a "where each hypothesis is used" coda, and a note that the proof is *pointwise* not uniform.

---

## Recipe 2 — Disprove a plausible-sounding claim (`/math-disprove`)

**User**: `/math-disprove Every continuous function on ℝ is uniformly continuous.`

**Step 1 — falsification first**, in parallel:

- `math-counterexample-hunter`: "Pathology probe — try f(x) = x². Pointwise continuous (recipe 1). For uniform continuity, need a δ that depends only on ε. But |f(x) − f(c)| = |x − c| · |x + c| grows unboundedly with c, so any fixed δ fails for large c. Witness: ε = 1, candidate δ. Take c = 1/δ, x = c + δ/2. Then |x − c| = δ/2 < δ but |f(x) − f(c)| = δ/2 · (2/δ + δ/2) = 1 + δ²/4 > 1 = ε. ✗"
- `math-numeric-verifier`: numerically confirms the witness.

**Final response**: disproof with witness, plus a brief note that on a *bounded* interval the implication does hold (Heine–Cantor), pointing at `lebl-basic-analysis-vol1/...-theorem-3-3-12.md`.

---

## Recipe 3 — Audit a proof someone else wrote (`/math-check`)

**User**: `/math-check ./my_proof.md`

The critic runs `proof_lint --proof ./my_proof.md --claim ./my_claim.md` first. Linter returns:

```json
{
  "findings": [
    {"severity": "HIGH", "category": "filler",
     "message": "unnamed citation: 'by a standard result' — cite the theorem by name",
     "line": 14},
    {"severity": "HIGH", "category": "quantifier",
     "message": "claim references a universal quantifier (∀ / 'for all') but the proof body contains no introduction of an arbitrary element",
     "line": null}
  ],
  "summary": {"CRITICAL": 0, "HIGH": 2, "MEDIUM": 1, "LOW": 0}
}
```

The critic then reads the proof, confirms both linter findings as real, and adds two more (a quantifier-order swap on line 18, a missing edge case for `n = 0`). Verdict: `REVISE`.

---

## Recipe 4 — Run the deep ensemble on a hard problem (`/math-solve-deep`)

**User**: `/math-solve-deep ./benchmarks/problems/imo-2023-p1.md --branches 3`

Three strategist→prover branches run in parallel:

| branch | framing | strategy chosen | initial CRITICAL | initial HIGH |
|---|---|---|---|---|
| 1 | direct construction | "Forward case analysis on smallest two divisors" | 0 | 2 |
| 2 | contradiction | "Assume a non-prime-power n satisfies; derive contradiction with the divisor chain" | 1 | 1 |
| 3 | reduction to textbook theorem | "Classify via the structure of the divisor lattice; cite [textbook]" | 0 | 0 |

Branch 3 wins. Critic loop refines once (round 1 → round 2). Final proof shipped. Branch 2's critic flagged a missing case that branch 3 had handled — confirming branch 3's coverage.

---

## Recipe 5 — Quick lookup, no harness (`/math-explain`)

**User**: `/math-explain Banach–Steinhaus theorem`

The orchestrator skips the agent loop. Reads `skills/formal-math-ai/references/functional-analysis-core.md`, finds the statement, composes a 300-word explanation: statement, hypotheses in plain English, key idea (Baire category), where it shows up (resonance theorem corollary), common confusions (completeness of the *domain* matters; pointwise boundedness ≠ uniform boundedness without it).

Cost: 1 reference read, no LLM-driven proof generation. Right tool for "what does X say" questions.

---

## Recipe 6 — Translate a proof to Lean (`/math-formalize`)

**User**: `/math-formalize ./my_approved_proof.md`

`math-formalizer` produces:

```lean
import Mathlib.Analysis.InnerProductSpace.Basic

/--
Cauchy–Schwarz on a real inner-product space.
-/
theorem cauchy_schwarz_real
    {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V] (u v : V) :
    |⟪u, v⟫_ℝ| ≤ ‖u‖ * ‖v‖ := by
  -- Discriminant trick on ⟨u - tv, u - tv⟩ ≥ 0.
  by_cases hv : v = 0
  · simp [hv]
  · have h_nonneg : ∀ t : ℝ, 0 ≤ ‖u‖^2 - 2 * t * ⟪u, v⟫_ℝ + t^2 * ‖v‖^2 := by
      sorry  -- expand ⟨u - tv, u - tv⟩ ≥ 0
    have h_disc : (2 * ⟪u, v⟫_ℝ)^2 - 4 * ‖u‖^2 * ‖v‖^2 ≤ 0 := by
      sorry  -- non-negative quadratic ⇒ discriminant ≤ 0
    sorry
```

Three labeled `sorry`s, each with a comment describing what closes it. A human (or a future search-augmented agent) can take this scaffold the rest of the way.

---

## Recipe 7 — Reproducible benchmarking (`/math-bench`)

**User**: `/math-bench all`

For each `benchmarks/problems/*.md`:

1. `python3 -m harness.run_bench init <id>` → fresh run dir.
2. Same pipeline as `/math-solve`, executed in sequence.
3. `python3 -m harness.run_bench record <run_dir>` → appends row to `benchmarks/runs/_index.md`.

Final response is a markdown table:

```markdown
| id | verdict | critic rounds | duration |
|---|---|---|---|
| epsilon-delta-continuity | APPROVE | 1 | 38s |
| lebl-3-1-7-cauchy-converges | APPROVE | 2 | 1m07s |
| intermediate-value-bisection | APPROVE | 1 | 41s |
| cauchy-schwarz-inner-product | APPROVE | 1 | 33s |
| dominated-convergence-application | APPROVE | 2 | 1m22s |
| putnam-2023-a1 | REVISE (max rounds) | 3 | 4m18s |  ← worth investigating
| imo-2023-p1 | APPROVE | 2 | 3m41s |
```

Run reports under `benchmarks/runs/<id>__<ts>/`. Diff a future run against this baseline to verify changes to agent prompts didn't regress.

---

## Anti-recipe — when NOT to use the harness

| User intent | Use this | Don't use |
|---|---|---|
| "What's the statement of Banach–Steinhaus?" | `/math-explain` | `/math-solve` |
| "Compute ∫₀¹ x² dx" | direct SymPy via `math-symbol-runner` | full pipeline |
| "Is the following code's complexity O(n log n)?" | nothing in this harness — that's algorithmic analysis, not math proof | `/math-solve` |
| "Help me debug my Lean proof" | mathlib search + manual editing | `/math-formalize` |
| "Write a textbook chapter on measure theory" | the skill references directly | any harness command |

The harness is for **rigorous proof construction with adversarial verification**. For everything else, lean on the skill or write directly.
