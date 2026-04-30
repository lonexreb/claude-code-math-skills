---
id: infinitude-of-primes
domain: number-theory
difficulty: 1
source: Euclid, Elements Book IX, Proposition 20
formalize: true
---

# Infinitude of primes

## Problem

Show that the set of prime numbers is infinite.

## Reference solution

Euclid's argument. Suppose, for contradiction, that there are only finitely many primes `p_1, p_2, …, p_n`. Consider

    N := p_1 · p_2 · … · p_n + 1.

`N > 1`, so by the fundamental theorem of arithmetic `N` has at least one prime divisor `q`. We claim `q` is *not* among `{p_1, …, p_n}`. Indeed, if `q = p_i` for some `i`, then `q | p_1·…·p_n`, and since `q | N`, we'd have `q | (N − p_1·…·p_n) = 1`, contradicting `q > 1`. Hence `q` is a prime not in the list — contradicting the assumed completeness of the list. ∎

## Notes

- **Strategist hint**: the strategy is "construct an explicit contradiction-witness". The candidate `N = p_1·…·p_n + 1` may not itself be prime, only have *some* prime factor outside the list — students who claim "N is prime" miss the subtlety.
- **Counterexample**: not applicable (claim is provably true).
- **Formalization**: `Nat.exists_infinite_primes` in mathlib4 closes this in a one-liner.
