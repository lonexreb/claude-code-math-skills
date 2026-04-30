# Reference proof: every Cauchy sequence in ℝ converges

Benchmark id: `lebl-3-1-7-cauchy-converges`. Domain: real-analysis. Difficulty: 2.

## Claim

Let `(xₙ)_{n≥1}` be a Cauchy sequence in ℝ. Then there exists `x ∈ ℝ` with `xₙ → x`.

## Strategy

Three steps. (i) A Cauchy sequence is bounded. (ii) By Bolzano-Weierstrass on ℝ, the sequence has a convergent subsequence with limit `x`. (iii) The Cauchy property forces the *whole* sequence to converge to `x`.

## Proof

### Step 1: `(xₙ)` is bounded

Let `(xₙ)` be Cauchy. Apply the Cauchy property with ε = 1: choose `N₀ ∈ ℕ` such that for all `m, n ≥ N₀`, `|xₘ − xₙ| < 1`. In particular for every `n ≥ N₀`,
    |xₙ| ≤ |xₙ − x_{N₀}| + |x_{N₀}| < 1 + |x_{N₀}|.
Set
    M := max(|x_1|, |x_2|, …, |x_{N₀-1}|, 1 + |x_{N₀}|).
Then `|xₙ| ≤ M` for every `n ≥ 1`. So `(xₙ)` is bounded.

### Step 2: extract a convergent subsequence

By the Bolzano-Weierstrass theorem on ℝ (Lebl Vol I §2.3 Theorem 2.3.7 — every bounded sequence of real numbers has a convergent subsequence), `(xₙ)` admits a convergent subsequence `(x_{n_k})_{k≥1}` with limit some `x ∈ ℝ`.

### Step 3: the whole sequence converges to `x`

Let `ε > 0` be arbitrary. We find `N ∈ ℕ` such that `n ≥ N ⇒ |xₙ − x| < ε`.

By the Cauchy property, choose `N₁ ∈ ℕ` such that for all `m, n ≥ N₁`, `|xₘ − xₙ| < ε/2`.

By the convergence of the subsequence to `x`, choose `K ∈ ℕ` such that for all `k ≥ K`, `|x_{n_k} − x| < ε/2`. By increasing `K` if necessary, we may also assume `n_K ≥ N₁` (this is possible because `n_k → ∞` strictly; for a strict subsequence, `n_k ≥ k`, so any `K ≥ N₁` already satisfies it).

Set `N := N₁`. For any `n ≥ N`, fix any `k ≥ K`. Then `n_k ≥ N₁`, so
    |xₙ − x| ≤ |xₙ − x_{n_k}| + |x_{n_k} − x|
            < ε/2 + ε/2     (Cauchy on n, n_k ≥ N₁; subsequence convergence at k ≥ K)
            = ε.

Since `ε > 0` was arbitrary, `xₙ → x`. ∎

## Where each hypothesis is used

- **`(xₙ)` is Cauchy** — used twice: in Step 1 (with ε = 1, to bound the sequence) and in Step 3 (with ε/2, to collapse the gap between `xₙ` and the subsequence).
- **The ambient space is ℝ** — used in Step 2 to invoke Bolzano-Weierstrass, which depends on the **completeness** of ℝ. The result fails on ℚ: e.g. the truncations of √2 form a Cauchy sequence in ℚ with no limit in ℚ.

## Tightness

The proof uses Bolzano-Weierstrass, which is itself equivalent to completeness of ℝ. So the conclusion is exactly as strong as completeness: it is **the** completeness of ℝ, packaged as a statement about Cauchy sequences. Drop completeness and the claim immediately fails (see ℚ counterexample above).

## References consulted

- `skills/formal-math-ai/references/real-analysis-foundations.md` (Cauchy sequences, completeness)
- `skills/formal-math-ai/references/lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-theorem-2-3-7.md` (Bolzano-Weierstrass on ℝ)
- `skills/formal-math-ai/references/lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-definition-2-4-3.md` (Cauchy sequence definition, Lebl Vol I)
