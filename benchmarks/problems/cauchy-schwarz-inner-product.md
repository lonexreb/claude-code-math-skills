---
id: cauchy-schwarz-inner-product
domain: linear-algebra
difficulty: 2
source: classical
formalize: true
---

# Cauchy–Schwarz inequality on a real inner-product space

## Problem

Let `(V, ⟨·,·⟩)` be a real inner-product space. Show that for all `u, v ∈ V`,

```
|⟨u, v⟩| ≤ ‖u‖ · ‖v‖,
```

where `‖x‖ := √⟨x, x⟩`. Determine the equality case.

## Reference solution

If `v = 0`, both sides are 0. Otherwise let `t ∈ ℝ`. Since the inner product is positive semi-definite,

```
0 ≤ ⟨u − t v, u − t v⟩ = ‖u‖² − 2 t ⟨u, v⟩ + t² ‖v‖².
```

This is a quadratic in `t` that is `≥ 0` for all `t`, so its discriminant is `≤ 0`:

```
(2 ⟨u, v⟩)² − 4 ‖u‖² ‖v‖² ≤ 0  ⇒  ⟨u, v⟩² ≤ ‖u‖² ‖v‖².
```

Take square roots.

**Equality case.** Equality forces the discriminant to be zero, i.e. `u − t v = 0` for some `t` (or `v = 0`). So equality iff `u, v` are linearly dependent.

## Notes

- The result also holds over ℂ, but the substitution is `t = e^{iθ} s` to align phases — slightly different argument. This benchmark uses ℝ.
- **Critic check:** confirm the prover handles the `v = 0` edge case explicitly. Many proofs implicitly assume `‖v‖ > 0`.
- **Tightness check:** the equality case is the part most students drop.
