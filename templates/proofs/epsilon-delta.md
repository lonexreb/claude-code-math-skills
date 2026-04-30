# ε–δ proof template

Use for: pointwise continuity, limit-of-function claims, uniform continuity, sequence convergence (the discrete analogue with `N` instead of `δ`).

## Skeleton

```
Claim: f is continuous at c. (i.e. ∀ ε > 0, ∃ δ > 0, ∀ x, |x − c| < δ ⇒ |f(x) − f(c)| < ε.)

Proof:
  Let ε > 0 be arbitrary.        ← introduces the ∀ε
  [scratch work to identify δ]
  Set δ = <expression depending on ε and c>.   ← supplies the ∃δ
  Verify δ > 0.                  ← non-trivial; omit at your peril
  Now let x ∈ ℝ with |x − c| < δ.  ← introduces the inner ∀x
  We compute:
      |f(x) − f(c)| = ...
                   ≤ ... (bound by inserting the assumed δ-condition)
                   < ε.
  This holds for our arbitrary ε, so f is continuous at c.  □
```

## Canonical pitfalls

1. **Forgetting `δ > 0`.** A `δ = ε / something_that_could_be_zero` is broken. State the positivity check.
2. **δ depending on x.** δ should depend only on ε (and c, for pointwise continuity). If δ depends on x, you have **uniform** continuity confusion — the proof shape has to change.
3. **Bounding by `ε / 2 + ε / 2 = ε`** (canonical). If you split into k terms, each must be `< ε / k`.
4. **Uniform continuity drops the `c`** — δ depends on ε alone. Make sure you don't accidentally use `c` in the chosen δ.
5. **Sequential convergence** is the discrete analogue: replace `δ` with `N`, `|x − c| < δ` with `n ≥ N`. Same skeleton.

## Worked micro-example: f(x) = x² is continuous at c

```
Let ε > 0 be arbitrary.
Set δ = min(1, ε / (1 + 2|c|)). Then δ > 0 since ε > 0 and 1 + 2|c| ≥ 1.
Let x ∈ ℝ with |x − c| < δ.
Then |x − c| ≤ 1, so |x + c| ≤ |x − c| + 2|c| < 1 + 2|c|.
Hence |x² − c²| = |x − c| · |x + c| < δ · (1 + 2|c|) ≤ ε.
```

Three lines, no filler, every step justified.
