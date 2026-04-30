---
id: lebl-3-1-7-cauchy-converges
domain: real-analysis
difficulty: 2
source: Lebl, Basic Analysis I, §3.1 (textbook classic)
formalize: false
---

# Every Cauchy sequence in ℝ converges

## Problem

Let `(xₙ)` be a Cauchy sequence in ℝ. Show that there exists `x ∈ ℝ` such that `xₙ → x`.

You may assume the **Bolzano–Weierstrass theorem** (every bounded sequence in ℝ has a convergent subsequence) — this is a standard consequence of the least-upper-bound property of ℝ; see `lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-theorem-2-3-7.md`.

## Reference solution

1. Cauchy ⇒ bounded: pick `N` so `|xₘ − xₙ| < 1` for `m, n ≥ N`. Then `|xₙ| ≤ |xₙ − xₙ₀| + |xₙ₀|` is bounded for `n ≥ N`; take a max with `|x₁|, …, |xₙ₋₁|`.
2. By Bolzano–Weierstrass, `(xₙ)` has a convergent subsequence `(xₙₖ) → x`.
3. Show that the *whole* sequence converges to `x`: given `ε > 0`, pick `N₁` so `m,n ≥ N₁ ⇒ |xₘ − xₙ| < ε/2`, and pick `K` so `k ≥ K ⇒ |xₙₖ − x| < ε/2` and `nₖ ≥ N₁`. Then for `n ≥ N₁`, choose any `k ≥ K`: `|xₙ − x| ≤ |xₙ − xₙₖ| + |xₙₖ − x| < ε`.

## Notes

- **Common bug:** invoking Bolzano–Weierstrass without first showing the sequence is bounded.
- **Pitfall:** stopping at "the subsequence converges" — the whole sequence must be shown to converge to the *same* limit. The Cauchy property is what closes that gap.
- This proof is the classic illustration of "Cauchy + completeness → convergent". The completeness of ℝ is what makes Bolzano–Weierstrass true.
