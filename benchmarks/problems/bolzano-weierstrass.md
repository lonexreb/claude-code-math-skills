---
id: bolzano-weierstrass
domain: real-analysis
difficulty: 3
source: classical (Lebl Vol I §2.3, Trench §3.3)
formalize: false
---

# Bolzano–Weierstrass on ℝ

## Problem

Show that every bounded sequence `(xₙ) ⊂ ℝ` has a convergent subsequence.

You may assume the **monotone convergence theorem** (every bounded monotone sequence converges).

## Reference solution

The cleanest proof uses the **monotone subsequence lemma** (every real sequence has a monotone subsequence — by a clever "peak point" argument). Then bounded + monotone ⇒ convergent (by hypothesis).

Sketch of the monotone subsequence lemma: call `m ∈ ℕ` a *peak* if `xₘ ≥ xₙ` for every `n ≥ m`. Two cases:

1. There are infinitely many peaks. List them in order `m_1 < m_2 < …`; the subsequence `(x_{m_k})` is **non-increasing**.
2. There are only finitely many peaks. Past the last peak, every index `n` admits some `n' > n` with `x_{n'} > x_n`. Build a strictly increasing subsequence inductively.

Either way we have a monotone subsequence; combined with boundedness, it converges.

## Notes

- **Common bug:** "extract a Cauchy subsequence" without justifying *why*. Bolzano–Weierstrass should be the *first* extraction tool, not "by passing to a subsequence".
- **Pitfall:** the proof depends on completeness of ℝ via the monotone convergence theorem — explicit in this problem because it's stated as an admitted hypothesis. The theorem fails on ℚ.
- **Strategist hint**: this is one of those proofs where naming the right lemma (monotone subsequence) changes the whole shape. Without it, you fight through ε-N estimates; with it, the proof is three sentences.
