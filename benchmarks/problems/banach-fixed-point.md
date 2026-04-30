---
id: banach-fixed-point
domain: functional-analysis
difficulty: 3
source: classical (Banach 1922; Lebl Vol I §6.5; Folland §0.5)
formalize: false
---

# Banach fixed-point theorem (contraction mapping)

## Problem

Let `(X, d)` be a complete metric space and `T : X → X` a strict contraction: there exists `0 ≤ k < 1` such that

    d(T x, T y) ≤ k · d(x, y)   for every x, y ∈ X.

Show that `T` has a unique fixed point. That is, there exists a unique `x* ∈ X` with `T(x*) = x*`.

## Reference solution

**Existence.** Pick any `x_0 ∈ X` and define `x_{n+1} := T(x_n)`. Show `(x_n)` is Cauchy:

    d(x_{n+1}, x_n) ≤ k · d(x_n, x_{n-1}) ≤ … ≤ kⁿ · d(x_1, x_0).

By the geometric-series tail bound, for `m > n`,

    d(x_m, x_n) ≤ Σ_{j=n}^{m-1} d(x_{j+1}, x_j) ≤ d(x_1, x_0) · Σ_{j=n}^{m-1} kʲ ≤ d(x_1, x_0) · kⁿ / (1 − k).

Since `k < 1`, `kⁿ → 0`, so `(x_n)` is Cauchy. By completeness of `X`, `(x_n)` converges to some `x* ∈ X`. Continuity of `T` (any contraction is in fact `k`-Lipschitz, hence continuous) gives `T(x*) = lim T(x_n) = lim x_{n+1} = x*`.

**Uniqueness.** If `T(y*) = y*` and `T(z*) = z*`, then `d(y*, z*) = d(T y*, T z*) ≤ k · d(y*, z*)`, so `(1 − k) · d(y*, z*) ≤ 0`. Since `1 − k > 0` and `d ≥ 0`, this forces `d(y*, z*) = 0`, hence `y* = z*`.

## Notes

- **Hypothesis verification**: completeness is essential. On a non-complete space (e.g. ℚ), a contraction may iterate to a Cauchy sequence with no limit *in the space*.
- **Strict** contraction (`k < 1`) is essential. The translation `x ↦ x + 1` on ℝ has `k = 1` and no fixed point; rotations on ℝ² are `k = 1` isometries (no fixed point unless the rotation is identity).
- **Common bug**: forgetting that `k = 1` breaks the uniqueness argument. The proof of `(1 − k) · d(y*, z*) ≤ 0 ⇒ d(y*, z*) = 0` requires `1 − k > 0`.
- **Application**: existence and uniqueness theorems for ODEs (Picard–Lindelöf) reduce to this. Newton's method's local convergence is an instance.
- **Counterexample-hunter exercise**: try `k = 1` to see uniqueness collapse; try `X = ℚ` to see existence collapse.
