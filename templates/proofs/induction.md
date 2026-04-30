# Induction template

Use for: statements parameterized by `n ∈ ℕ`, recursively defined objects, claims about all positive integers, finite combinatorial identities.

## Skeleton

```
Claim: P(n) holds for every n ≥ n₀.

Proof: by induction on n.

Base case (n = n₀):
  Show P(n₀) directly.    ← do not skip this; n₀ = 0 vs n₀ = 1 matters.

Inductive step:
  Suppose P(k) holds for some k ≥ n₀.    ← weak induction
    -- or --
  Suppose P(j) holds for every n₀ ≤ j ≤ k.   ← strong induction
  We show P(k+1) holds.
  [argument using the hypothesis]
  Therefore P(k+1).

By induction, P(n) holds for every n ≥ n₀. □
```

## When to choose strong induction

If P(k+1) requires P(j) for some j strictly less than k (not just k), use strong induction. Examples: prime factorization (k+1 may factor as a · b with a, b ≤ k), recursive sequences with deep dependence.

## Canonical pitfalls

1. **Wrong base case.** If the claim says `n ≥ 2`, do not start at `n = 1`.
2. **Two-step recurrences need two base cases.** If the inductive step uses both `P(k)` and `P(k−1)`, the base must cover both `n₀` and `n₀ + 1`.
3. **The claim must be strong enough to induct.** Sometimes proving a *stronger* statement is easier because the inductive hypothesis becomes more useful (this is "strengthening the hypothesis" — common in IMO-style problems).
4. **Inducting over the wrong variable.** If the claim has multiple parameters, pick the one that decreases on each recursive step.

## Worked micro-example: 1 + 2 + ... + n = n(n+1)/2

```
Base (n = 1): 1 = 1·2/2 ✓.

Inductive step. Suppose 1 + 2 + ... + k = k(k+1)/2 for some k ≥ 1.
Then
    1 + 2 + ... + (k+1) = k(k+1)/2 + (k+1)
                       = (k+1)(k/2 + 1)
                       = (k+1)(k+2)/2,
which is the claim for n = k+1. By induction, the formula holds for every n ≥ 1. □
```

## Variants

- **Structural induction**: induct on the structure of a recursively defined object (lists, trees, formulas in a formal language).
- **Well-founded induction**: induct on any well-founded relation, not just `<` on ℕ.
- **Infinite descent**: equivalent to strong induction; useful for non-existence proofs (no smallest counterexample).
