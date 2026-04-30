---
id: intermediate-value-bisection
domain: real-analysis
difficulty: 2
source: standard textbook (Lebl §3.3 / Trench §2.2)
formalize: false
---

# Intermediate Value Theorem via bisection

## Problem

Let `f : [a, b] → ℝ` be continuous, with `f(a) < 0 < f(b)`. Show that there exists `c ∈ (a, b)` with `f(c) = 0`.

Use only:
- continuity of `f` (ε–δ definition),
- completeness of ℝ (least-upper-bound or nested-intervals).

Do **not** quote the Intermediate Value Theorem itself — that's what we are proving.

## Reference solution

Bisect: build sequences `(aₙ), (bₙ)` with `f(aₙ) ≤ 0`, `f(bₙ) ≥ 0`, `bₙ − aₙ = (b − a)/2ⁿ`. The nested intervals `[aₙ, bₙ]` have a unique common point `c` (by completeness). Continuity at `c` and the sign conditions force `f(c) = 0`.

Alternative: let `S = {x ∈ [a, b] : f(x) ≤ 0}`. `S` is non-empty (`a ∈ S`) and bounded above (`b`). Let `c = sup S`. Continuity at `c` plus the definition of supremum forces `f(c) = 0`.

## Notes

- **Tightness check:** the conclusion fails on `ℚ` — completeness of ℝ is essential. The critic should verify completeness was actually invoked.
- **Common bug:** "by continuity, `f(c) = 0`" without the two-sided argument. Continuity gives `f(c) ≤ 0` from `aₙ → c` and `f(c) ≥ 0` from `bₙ → c` — both inequalities are needed.
- This is the canonical place where the prover must explicitly invoke completeness of ℝ.
