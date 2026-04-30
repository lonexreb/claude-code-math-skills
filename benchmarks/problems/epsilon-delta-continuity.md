---
id: epsilon-delta-continuity
domain: real-analysis
difficulty: 1
source: standard textbook (Lebl §3.2)
formalize: false
---

# ε-δ continuity of x²

## Problem

Show that the function `f : ℝ → ℝ` defined by `f(x) = x²` is continuous at every point `c ∈ ℝ`. Specifically: for every `c ∈ ℝ` and every `ε > 0`, exhibit a `δ > 0` such that

> for every `x ∈ ℝ` with `|x − c| < δ`, we have `|f(x) − f(c)| < ε`.

The δ is allowed to depend on both `c` and `ε`.

## Reference solution

`|x² − c²| = |x − c|·|x + c|`. If `|x − c| < 1`, then `|x + c| ≤ |x − c| + 2|c| ≤ 1 + 2|c|`. So choosing `δ = min(1, ε / (1 + 2|c|))` works.

## Notes

- **Common bug:** picking `δ = ε / (2|c|)` without the `min` — fails at `c = 0` and ignores the bound on `|x + c|`.
- **Pitfall:** picking `δ = √ε` works at `c = 0` only. Must adapt to `c`.
- The δ explicitly depends on `c` — this is **pointwise**, not uniform, continuity. A critic should not let a uniform-continuity argument slip in.
