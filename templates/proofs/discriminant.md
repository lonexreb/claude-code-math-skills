# Discriminant / non-negative quadratic template

Use for: inequalities provable by exhibiting a real-valued quadratic that is `≥ 0` everywhere. The textbook example is the Cauchy–Schwarz inequality.

## Skeleton

```
Goal: P ≤ Q (or |P| ≤ Q with Q ≥ 0).

Proof. Define φ(t) = ⟨linear expression in t involving P and Q⟩², chosen so that:
  (i) φ(t) ≥ 0 for all t ∈ ℝ.
  (ii) φ(t) expanded is a quadratic At² + Bt + C in t with explicit A, B, C
       in terms of the data of the inequality.

Since A ≥ 0 and φ(t) ≥ 0 for all real t, the discriminant satisfies
    B² − 4 A C ≤ 0.
Substituting the explicit A, B, C produces the desired inequality after
algebraic rearrangement.

Edge case A = 0 (degenerate quadratic): handle separately. □
```

## Canonical pitfalls

1. **Forgetting `A ≥ 0`.** The discriminant criterion `B² − 4 A C ≤ 0` for a non-negative quadratic requires `A > 0` (or careful handling of `A = 0`). Without `A > 0`, the quadratic could be a downward parabola that's still `≥ 0` only on an interval, or a linear function.
2. **The `A = 0` edge case.** When the leading coefficient vanishes, the "quadratic" is linear (or constant). The inequality must be checked directly in this case. For Cauchy–Schwarz, `A = 0` corresponds to `‖v‖ = 0`, i.e. `v = 0`.
3. **Equality case.** The discriminant criterion gives equality iff `B² = 4 A C` iff `φ` has a (double) real root. Translate that condition back to the original variables to characterize equality.
4. **Sign conventions.** When taking square roots at the end (e.g. `⟨u, v⟩² ≤ ‖u‖² ‖v‖² ⇒ |⟨u, v⟩| ≤ ‖u‖ ‖v‖`), the absolute value matters.

## Worked micro-example: Cauchy–Schwarz on a real inner-product space

```
Let V be a real inner-product space, u, v ∈ V. We show |⟨u, v⟩| ≤ ‖u‖ · ‖v‖.

If v = 0, both sides are 0; done.    ← edge case A = 0

Otherwise ‖v‖² > 0. Define
    φ(t) := ⟨u − t v, u − t v⟩  =  ‖u‖² − 2 t ⟨u, v⟩ + t² ‖v‖².
By positive semi-definiteness, φ(t) ≥ 0 for every t ∈ ℝ.
This is a quadratic in t with positive leading coefficient ‖v‖² > 0,
so its discriminant is ≤ 0:
    (2⟨u, v⟩)² − 4 ‖u‖² ‖v‖² ≤ 0,
i.e. ⟨u, v⟩² ≤ ‖u‖² ‖v‖².
Take square roots: |⟨u, v⟩| ≤ ‖u‖ · ‖v‖. □

Equality. The discriminant is zero iff φ has a double root t₀, iff
u − t₀ v = 0, iff u, v are linearly dependent.
```

Crisp, with the edge case and equality case both handled.

## Other applications

- **AM–GM via squares**: `(a − b)² ≥ 0 ⇒ a² + b² ≥ 2 a b`.
- **Bunyakovsky / Hölder**-like estimates with the appropriate inner product or integral pairing.
- **Bessel's inequality** in Hilbert spaces.
- **Spectral bounds** via `‖A x‖² ≥ 0` for self-adjoint A.

The shape always: pick a quadratic that's manifestly ≥ 0, expand, read off the discriminant inequality, translate back.
