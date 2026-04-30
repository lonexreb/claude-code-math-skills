---
id: putnam-2023-a1
domain: combinatorics
difficulty: 4
source: Putnam 2023, Problem A1
formalize: false
---

# Putnam 2023 A1

## Problem

For a positive integer `n`, let `f(n)` be the number of permutations `σ` of `{1, 2, …, n}` such that

```
σ(1) + σ(2) + … + σ(k)   is divisible by k   for every k = 1, 2, …, n.
```

Determine, with proof, all `n` for which `f(n) ≥ 2023`.

## Reference solution sketch

The condition says `σ(1) + … + σ(k) ≡ 0 (mod k)` for every `k`. Since `σ(1) + … + σ(n) = n(n+1)/2`, the `k = n` divisibility is automatic for odd `n` (n divides n(n+1)/2 iff n is odd or n is 1 mod something — careful here). Work out:

- `f(1) = 1`, `f(2) = 1`, `f(3) = 3`, `f(4) = 9`, …
- One slick approach: induction with a careful counting of how `σ(k)` is determined by the prefix.

Determine the asymptotic growth and find the threshold `n*` where `f(n*) ≥ 2023`.

## Notes

- This is a **discovery + proof** problem. The strategist should propose: brute-force small `n` to see the pattern, then prove by induction.
- **Counterexample hunter** is useful here only insofar as small-n computation tells you what the right answer is.
- **Numeric verifier** can compute `f(n)` for small `n` directly:
  ```python
  from itertools import permutations
  def f(n):
      return sum(
          all(sum(p[:k+1]) % (k+1) == 0 for k in range(n))
          for p in permutations(range(1, n+1))
      )
  ```
- Watch out: this problem is solvable in pieces. The harness should benefit from `math-symbol-runner` (or just direct Bash) for the small-n computation.
