# Reference proof: Intermediate Value Theorem via bisection

Benchmark id: `intermediate-value-bisection`. Domain: real-analysis. Difficulty: 2.

## Claim

Let `f : [a, b] → ℝ` be continuous, with `f(a) < 0 < f(b)`. Then there exists `c ∈ (a, b)` with `f(c) = 0`.

## Strategy

Construct nested intervals `[a_n, b_n] ⊆ [a, b]` such that `f(a_n) ≤ 0 ≤ f(b_n)` and `b_n − a_n → 0`. Use the nested-intervals theorem (a consequence of the completeness of ℝ) to extract a unique common point `c`. Continuity at `c` plus the sign control on the endpoints forces `f(c) = 0`.

## Proof

Set `a_0 := a` and `b_0 := b`. By hypothesis, `f(a_0) < 0` and `f(b_0) > 0`. We define `(a_n, b_n)` inductively.

**Inductive construction.** Suppose we have constructed `[a_n, b_n] ⊆ [a, b]` with `f(a_n) ≤ 0 ≤ f(b_n)` and `b_n − a_n = (b − a) / 2ⁿ`. Set `m_n := (a_n + b_n) / 2`.

- If `f(m_n) ≤ 0`, set `a_{n+1} := m_n` and `b_{n+1} := b_n`.
- Otherwise (`f(m_n) > 0`), set `a_{n+1} := a_n` and `b_{n+1} := m_n`.

In either case, `[a_{n+1}, b_{n+1}] ⊆ [a_n, b_n]`, the sign invariants `f(a_{n+1}) ≤ 0` and `f(b_{n+1}) ≥ 0` hold, and `b_{n+1} − a_{n+1} = (b_n − a_n)/2 = (b − a)/2^{n+1}`.

**Existence of the common point.** The intervals are nested:
    [a, b] = [a_0, b_0] ⊇ [a_1, b_1] ⊇ [a_2, b_2] ⊇ …,
each closed and bounded, with `b_n − a_n = (b − a)/2ⁿ → 0`. By the nested-intervals theorem on ℝ (Lebl Vol I §1.3 — a direct consequence of the completeness / least-upper-bound property), there is a unique `c ∈ ⋂_{n≥0} [a_n, b_n]`. Since `[a_n, b_n] ⊆ [a, b]`, we have `c ∈ [a, b]`.

**The value of `f(c)`.** Since `b_n − a_n → 0` and both `a_n, b_n ∈ [a_n, b_n] ∋ c`, we have
    a_n → c   and   b_n → c.
By continuity of `f` at `c` (Lebl Vol I §3.2 — sequential characterization of continuity),
    f(a_n) → f(c)   and   f(b_n) → f(c).
By the sign invariants and the order limit theorem (Lebl Vol I §2.2 Theorem 2.2.5), `f(a_n) ≤ 0` for every `n` gives `f(c) = lim f(a_n) ≤ 0`, and `f(b_n) ≥ 0` for every `n` gives `f(c) = lim f(b_n) ≥ 0`. Hence `f(c) = 0`.

**Strict interior.** It remains to show `c ∈ (a, b)`, not merely `c ∈ [a, b]`. Since `f(a) < 0 = f(c)`, we have `f(a) ≠ f(c)`, hence `c ≠ a`. By the analogous comparison with the other endpoint, `f(b) > 0 = f(c)` gives `f(b) ≠ f(c)`, hence `c ≠ b`. Therefore `c ∈ (a, b)`. ∎

## Where each hypothesis is used

- **Continuity of `f` on `[a, b]`** — used in the order-limit step to conclude `f(c) = lim f(a_n)` and `f(c) = lim f(b_n)`.
- **`f(a) < 0`** (strict) — used to conclude `c ≠ a` (strict interior). If only `f(a) ≤ 0`, the witness `c` may equal `a`.
- **`f(b) > 0`** (strict) — used analogously to conclude `c ≠ b`.
- **The codomain is ℝ (and ℝ is complete)** — used in the nested-intervals theorem. The result fails on `ℚ`: e.g. `f(x) = x² − 2` on `[0, 2] ∩ ℚ` is continuous, takes values of opposite sign at the endpoints, but has no rational root in `(0, 2)`.

## Tightness

The proof depends critically on completeness. On any non-complete subfield of ℝ (such as ℚ), the conclusion fails. The hypotheses on `f(a), f(b)` cannot be weakened to `≤` without losing the strict-interior conclusion.

## References consulted

- `skills/formal-math-ai/references/real-analysis-foundations.md` (continuity, sequential criterion, completeness)
- `skills/formal-math-ai/references/lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-theorem-2-2-5.md` (order limit theorem, Lebl Vol I)
- `skills/formal-math-ai/references/lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-theorem-1-3-7.md` (nested-intervals / supremum, Lebl Vol I)
