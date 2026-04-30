---
id: dominated-convergence-application
domain: measure-theory
difficulty: 4
source: classical (Royden / Folland exercise)
formalize: false
---

# Interchange of limit and integral via dominated convergence

## Problem

Let `(fₙ : [0, 1] → ℝ)` be a sequence of measurable functions converging pointwise a.e. to `f`. Suppose there exists a measurable `g : [0, 1] → [0, ∞)` with

- `g ∈ L¹([0, 1])` (Lebesgue integrable),
- `|fₙ(x)| ≤ g(x)` for almost every `x` and every `n`.

Show that `f ∈ L¹([0, 1])` and

```
lim_{n→∞} ∫_{[0,1]} fₙ dλ = ∫_{[0,1]} f dλ.
```

## Reference solution

Direct application of the **Dominated Convergence Theorem** (Folland 2.24 / Royden Ch. 4). Verify the three hypotheses at the citation point:

1. `(fₙ)` converges pointwise a.e. — given.
2. There is a Lebesgue-integrable dominating function `g` — given.
3. Each `fₙ` is measurable — given.

Conclude `f` is measurable (as an a.e. pointwise limit of measurable functions on a complete measure space) and that DCT delivers the equality directly.

The integrability of `f` follows from `|f(x)| ≤ g(x)` a.e. (limit of `|fₙ| ≤ g`) and `g ∈ L¹`.

## Notes

- **Critic check:** make sure the prover *names DCT* and *verifies its three hypotheses* at the point of citation. "By DCT" without verification is exactly the kind of HIGH finding the critic should flag.
- **Counterexample if you drop domination:** `fₙ(x) = n · 1_{[0, 1/n]}` on `[0, 1]`. Pointwise limit is `0`, but `∫fₙ = 1` for all `n` — so `lim ∫ ≠ ∫ lim`. Domination fails (any candidate `g ≥ |fₙ|` would have to be `≥ 1/x` near 0, which is not integrable on `[0, 1]`).
