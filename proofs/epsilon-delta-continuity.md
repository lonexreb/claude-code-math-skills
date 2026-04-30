# Reference proof: ε–δ continuity of f(x) = x²

Benchmark id: `epsilon-delta-continuity`. Domain: real-analysis. Difficulty: 1.

## Claim

Let `f : ℝ → ℝ` be defined by `f(x) = x²`. For every `c ∈ ℝ`, `f` is continuous at `c`. Equivalently:

> ∀ c ∈ ℝ, ∀ ε > 0, ∃ δ > 0, ∀ x ∈ ℝ, |x − c| < δ ⇒ |x² − c²| < ε.

## Strategy

Factor `|x² − c²| = |x − c| · |x + c|`. Bound `|x + c|` by a constant on a neighborhood of `c`, then pick δ to make the product `< ε`.

## Proof

Fix `c ∈ ℝ` and let `ε > 0` be arbitrary. We exhibit `δ > 0` with the required property.

Set
    δ := min(1, ε / (1 + 2|c|)).

Both arguments of `min` are strictly positive: `1 > 0`, and `ε > 0`, `1 + 2|c| ≥ 1 > 0`. Hence `δ > 0`.

Now let `x ∈ ℝ` with `|x − c| < δ`. Since `δ ≤ 1`, we have `|x − c| < 1`, so by the triangle inequality
    |x + c| = |(x − c) + 2c| ≤ |x − c| + 2|c| < 1 + 2|c|.    (*)

Therefore
    |x² − c²| = |x − c| · |x + c|
              < δ · (1 + 2|c|)            by (*) and |x − c| < δ
              ≤ (ε / (1 + 2|c|)) · (1 + 2|c|)  since δ ≤ ε / (1 + 2|c|)
              = ε.

Since `ε > 0` was arbitrary, `f` is continuous at `c`. Since `c ∈ ℝ` was arbitrary, `f` is continuous on ℝ. ∎

## Where each hypothesis is used

- `f(x) = x²`: used to factor `|x² − c²| = |x − c| · |x + c|`. Without this specific form, the bound (*) doesn't translate into `< ε`.
- `c ∈ ℝ` (i.e. `c` is finite): used implicitly in the definition `δ = min(1, ε/(1+2|c|))`. If `c` were `∞`, no finite `δ` would work — confirming continuity at `∞` requires a different formalism.

## Tightness

The choice of δ depends on `c` (through the `1 + 2|c|` factor). This is **pointwise** continuity, not uniform continuity. In fact, `f` is **not uniformly continuous on ℝ**: for any candidate `δ > 0`, take `c = 1/δ`, `x = c + δ/2`; then `|x − c| = δ/2 < δ` but `|x² − c²| = δ/2 · (2c + δ/2) = 1 + δ²/4 > 1`. So the result is sharp — pointwise is the strongest conclusion compatible with `f(x) = x²` on all of ℝ.

`f` *is* uniformly continuous on any bounded interval `[−M, M]` (Heine-Cantor: any continuous function on a compact set is uniformly continuous; cf. Lebl Vol I §3.3 Theorem 3.3.12).

## References consulted

- `skills/formal-math-ai/references/real-analysis-foundations.md` (continuity definition)
- `skills/formal-math-ai/references/lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-definition-3-2-1.md` (ε-δ continuity, Lebl Vol I)
