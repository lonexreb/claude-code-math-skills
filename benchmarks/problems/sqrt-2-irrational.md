---
id: sqrt-2-irrational
domain: number-theory
difficulty: 1
source: classical (Euclid; appears in nearly every introductory analysis text)
formalize: true
---

# √2 is irrational

## Problem

Show that there is no rational number `q ∈ ℚ` with `q² = 2`.

## Reference solution

Standard proof by contradiction. Assume `q = p/m` with `p, m ∈ ℤ`, `m > 0`, and `gcd(p, m) = 1`. Then `2 m² = p²`, so `p²` is even, hence `p = 2 p'`. Substituting: `2 m² = 4 p'²`, so `m² = 2 p'²`, hence `m` is even. Both `p` and `m` are even — contradicting `gcd(p, m) = 1`.

## Notes

- **Counterexample-hunter exercise**: this is a great regression test for the harness. The numeric verifier should **not** find a counterexample (because no rational squares to 2). The counterexample-hunter should report a clean sweep, not a false positive from numerical fuzz like `(99/70)² ≈ 1.999`.
- **Formalization target**: this proof formalizes cleanly in Lean 4 mathlib via `Nat.Prime.irrational_sqrt`; a `/math-formalize` run should produce a one-liner proof modulo `decide`.
- **Tightness**: the result generalizes — if `n` is not a perfect square, then `√n` is irrational. Bonus: prove the generalization.
