# Reference proof: Cauchy–Schwarz on a real inner-product space

Benchmark id: `cauchy-schwarz-inner-product`. Domain: linear-algebra. Difficulty: 2.

## Claim

Let `(V, ⟨·,·⟩)` be a real inner-product space with associated norm `‖x‖ := √⟨x, x⟩`. For all `u, v ∈ V`:

    |⟨u, v⟩| ≤ ‖u‖ · ‖v‖.

Equality holds if and only if `u` and `v` are linearly dependent.

## Strategy

The discriminant trick: build a real-valued non-negative quadratic in a parameter `t`, read off the discriminant condition, translate it back to the original inequality. Handle the degenerate case `v = 0` separately.

## Proof

### Edge case: v = 0

If `v = 0`, then `⟨u, v⟩ = ⟨u, 0⟩ = 0` (linearity in the second argument) and `‖v‖ = 0`, so both sides of the inequality equal `0` and the inequality is an equality. The relation `v = 0 · v` exhibits a non-trivial linear combination `0 · u + 1 · v = 0`, so `{u, v}` is linearly dependent by definition.

### Main case: v ≠ 0

Suppose `v ≠ 0`, so `‖v‖² = ⟨v, v⟩ > 0` (positive-definiteness).

For every `t ∈ ℝ`, the vector `u − t v` satisfies
    ⟨u − t v, u − t v⟩ ≥ 0    (positive semi-definiteness of ⟨·,·⟩).
Expanding using bilinearity and the symmetry `⟨v, u⟩ = ⟨u, v⟩` of a real inner product,
    ⟨u − t v, u − t v⟩ = ‖u‖² − 2 t ⟨u, v⟩ + t² ‖v‖².
Hence
    φ(t) := ‖u‖² − 2 t ⟨u, v⟩ + t² ‖v‖² ≥ 0    for every t ∈ ℝ.    (*)

This is a quadratic in `t` with leading coefficient `‖v‖² > 0`. By the standard sign-of-quadratic criterion (a quadratic `A t² + B t + C` with `A > 0` is non-negative on all of ℝ if and only if its discriminant `B² − 4 A C ≤ 0`), inequality (*) gives
    (−2 ⟨u, v⟩)² − 4 ‖u‖² ‖v‖² ≤ 0,
i.e. `4 ⟨u, v⟩² ≤ 4 ‖u‖² ‖v‖²`, hence
    ⟨u, v⟩² ≤ ‖u‖² ‖v‖².

Taking square roots (both sides non-negative) and recalling `√(x²) = |x|`,
    |⟨u, v⟩| ≤ ‖u‖ · ‖v‖.

### Equality case

Suppose `v ≠ 0` (the `v = 0` case was handled above). Equality in the Cauchy–Schwarz inequality is equivalent to equality in the discriminant inequality, i.e. `⟨u, v⟩² = ‖u‖² ‖v‖²`, which is equivalent to the discriminant being zero. A non-negative quadratic with zero discriminant has a unique real root: there exists `t₀ ∈ ℝ` with `φ(t₀) = 0`, i.e.
    ⟨u − t₀ v, u − t₀ v⟩ = 0.
By positive-definiteness, this forces `u − t₀ v = 0`, i.e. `u = t₀ v`. Hence `u` and `v` are linearly dependent.

Conversely, if `u = t₀ v` for some `t₀ ∈ ℝ` (or `v = 0`), direct substitution gives `|⟨u, v⟩| = |t₀| · ‖v‖² = ‖u‖ · ‖v‖`. ∎

## Where each hypothesis is used

- **Positive semi-definiteness of `⟨·,·⟩`**: gives the inequality `⟨u − t v, u − t v⟩ ≥ 0` that drives the whole argument.
- **Positive-definiteness** (the strict version, `⟨x, x⟩ > 0` for `x ≠ 0`): used to conclude `‖v‖² > 0` in the main case, and to deduce `u − t₀ v = 0` from `⟨u − t₀ v, u − t₀ v⟩ = 0` in the equality case.
- **Bilinearity / symmetry**: used to expand `⟨u − t v, u − t v⟩` into a quadratic in `t` with computable coefficients.
- **The scalar field is ℝ**: the symmetry `⟨v, u⟩ = ⟨u, v⟩` (rather than the conjugate `⟨u, v⟩` of the complex case) keeps the discriminant real and the analysis self-contained.

## Tightness

- Drop positive-definiteness (keeping only positive semi-definiteness): the inequality still holds, but the equality case characterization weakens — `u − t₀ v` could be a non-zero null vector. This is the situation in indefinite inner-product spaces (e.g. Minkowski space), where Cauchy–Schwarz must be reformulated.
- Drop bilinearity in `t`: without a quadratic structure, the discriminant trick is unavailable.
- The complex case (`F = ℂ`) requires substituting `t e^{iθ}` and choosing `θ` to align phases; the proof shape is the same but with `Re` and `|⟨u, v⟩|` swapped at the right step.

## References consulted

- `skills/formal-math-ai/references/hilbert-banach-spaces.md` (inner-product space definitions, Cauchy–Schwarz statement)
- `skills/formal-math-ai/references/functional-analysis-core.md` (Cauchy–Schwarz role in Hilbert-space theory)
