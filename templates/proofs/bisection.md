# Bisection / nested-intervals template

Use for: existence on a real interval (Intermediate Value Theorem, Bolzano root finding, fixed-point existence on a continuous monotone map).

## Skeleton

```
Claim: f : [a, b] → ℝ continuous, f(a) < 0 < f(b). Then ∃ c ∈ (a, b), f(c) = 0.

Proof. Set a₀ = a, b₀ = b.
Inductively define (aₙ, bₙ) for n ≥ 0:
  Let mₙ = (aₙ + bₙ) / 2.
  If f(mₙ) ≤ 0, set aₙ₊₁ = mₙ and bₙ₊₁ = bₙ.    ← invariant: f(aₙ₊₁) ≤ 0
  Otherwise (f(mₙ) > 0), set aₙ₊₁ = aₙ and bₙ₊₁ = mₙ.   ← invariant: f(bₙ₊₁) ≥ 0
By construction:
  (i)  f(aₙ) ≤ 0, f(bₙ) ≥ 0 for all n,
  (ii) [aₙ₊₁, bₙ₊₁] ⊂ [aₙ, bₙ],
  (iii) bₙ − aₙ = (b − a) / 2ⁿ.

By the nested-intervals property of ℝ (a consequence of completeness),
there exists a unique c ∈ ⋂ₙ [aₙ, bₙ]. Both aₙ → c and bₙ → c.
By continuity of f at c:
    f(c) = lim f(aₙ) ≤ 0,    and    f(c) = lim f(bₙ) ≥ 0.
Hence f(c) = 0. □
```

## Canonical pitfalls

1. **Forgetting completeness.** This proof fails on ℚ. Make sure the proof *invokes* completeness (or LUB / nested intervals / Bolzano-Weierstrass — all equivalent for ℝ) explicitly.
2. **Monotonicity of intervals.** Verify `[aₙ₊₁, bₙ₊₁] ⊆ [aₙ, bₙ]` — without this, the nested-intervals property doesn't apply.
3. **Two-sided continuity argument.** Take BOTH limits: `f(aₙ) → f(c) ≤ 0` AND `f(bₙ) → f(c) ≥ 0`. Either inequality alone is not enough.
4. **Edge case `f(a) = 0`.** Some statements include `f(a) ≤ 0`, in which case `a` itself may be the witness — handle separately.
5. **Strict vs non-strict.** If the hypothesis says `f(a) < 0` and the conclusion is `f(c) = 0`, the proof must explicitly produce `f(c) = 0` rather than `f(c) ≤ 0` and stop.

## Variant: supremum proof of IVT

```
Let S = { x ∈ [a, b] : f(x) ≤ 0 }.
S is non-empty (a ∈ S) and bounded above (by b).
Let c = sup S (exists by LUB completeness).
Argue f(c) = 0 by showing both f(c) ≤ 0 and f(c) ≥ 0
(use continuity at c plus the definition of supremum).
```

This is a "one-shot" alternative; skip the inductive construction.

## When NOT to use bisection

- The interval isn't closed. Bisection on `(0, 1)` requires `(0, 1)` to be complete in the relevant sense — usually fails.
- f is not continuous. The interpolation step relies on the limit identification.
- You need the *least* root, the *greatest* root, or *all* roots — bisection gives you *some* root.
