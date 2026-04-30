# Real Analysis Foundations

## Table of Contents
1. [The Real Number System](#the-real-number-system)
2. [Sequences and Limits](#sequences-and-limits)
3. [Topology of R and R^n](#topology-of-r-and-rn)
4. [Continuity](#continuity)
5. [Differentiation](#differentiation)
6. [Riemann Integration](#riemann-integration)
7. [Sequences and Series of Functions](#sequences-and-series-of-functions)

---

## The Real Number System

### Completeness Axiom (Least Upper Bound Property)
Every nonempty subset of ℝ that is bounded above has a least upper bound (supremum) in ℝ.

**Why it matters:** This single axiom is what separates ℝ from ℚ. Nearly every major theorem in real analysis ultimately traces back to completeness.

**Equivalent formulations:**
- Monotone Convergence Property: Every bounded monotone sequence converges
- Nested Intervals Property: Nested closed bounded intervals have nonempty intersection
- Bolzano-Weierstrass Property: Every bounded sequence has a convergent subsequence
- Cauchy Completeness: Every Cauchy sequence converges

### Archimedean Property
For every x ∈ ℝ, there exists n ∈ ℕ with n > x.

**Consequence:** For every ε > 0, there exists n ∈ ℕ with 1/n < ε. This is the workhorse for epsilon-delta proofs.

### Density of ℚ in ℝ
Between any two distinct real numbers there exists a rational number (and also an irrational number).

---

## Sequences and Limits

### Definition of Convergence
A sequence (aₙ) converges to L ∈ ℝ if:
∀ε > 0, ∃N ∈ ℕ such that n ≥ N ⟹ |aₙ - L| < ε.

**Common errors to watch for:**
- N may depend on ε (this is fine and expected)
- The inequality is strict: |aₙ - L| < ε, not ≤ ε (though ≤ also works — they're equivalent)
- "Eventually" means "for all sufficiently large n," not "for infinitely many n"

### Limit Superior and Limit Inferior
- lim sup aₙ = inf_{N≥1} sup_{n≥N} aₙ = lim_{N→∞} sup_{n≥N} aₙ
- lim inf aₙ = sup_{N≥1} inf_{n≥N} aₙ = lim_{N→∞} inf_{n≥N} aₙ

**Key facts:**
- A sequence converges ⟺ lim sup = lim inf (and both are finite)
- lim inf aₙ ≤ lim sup aₙ always
- lim sup aₙ is the largest subsequential limit
- lim inf aₙ is the smallest subsequential limit

### Cauchy Sequences
(aₙ) is Cauchy if: ∀ε > 0, ∃N ∈ ℕ such that m, n ≥ N ⟹ |aₘ - aₙ| < ε.

**Theorem:** In ℝ, a sequence converges ⟺ it is Cauchy.
*This equivalence is precisely the completeness of ℝ. It fails in ℚ.*

### Bolzano-Weierstrass Theorem
Every bounded sequence in ℝⁿ has a convergent subsequence.

**Why it matters:** This is the compactness theorem in disguise for ℝⁿ. It fails in infinite-dimensional spaces — a crucial distinction for functional analysis.

### Key Series Tests
- **Comparison Test:** 0 ≤ aₙ ≤ bₙ and Σbₙ converges ⟹ Σaₙ converges
- **Ratio Test:** If lim |aₙ₊₁/aₙ| = L, then: L < 1 ⟹ converges absolutely; L > 1 ⟹ diverges
- **Root Test:** If lim sup |aₙ|^{1/n} = L, same conclusion as ratio test
- **Alternating Series Test (Leibniz):** aₙ ≥ 0, aₙ decreasing to 0 ⟹ Σ(-1)ⁿaₙ converges
- **Abel's Test / Dirichlet's Test:** For conditionally convergent series and summation by parts

---

## Topology of R and R^n

### Open and Closed Sets
- A set U ⊂ ℝ is **open** if ∀x ∈ U, ∃ε > 0 with (x-ε, x+ε) ⊂ U
- A set F ⊂ ℝ is **closed** if its complement is open, equivalently if it contains all its limit points
- A set can be both open and closed (clopen): only ∅ and ℝ in ℝ
- A set can be neither open nor closed: [0, 1) in ℝ

### Compactness
**Definition (sequential):** K is sequentially compact if every sequence in K has a subsequence converging to a point in K.

**Definition (open cover):** K is compact if every open cover has a finite subcover.

**Heine-Borel Theorem:** In ℝⁿ, compact ⟺ closed and bounded.

**WARNING:** Heine-Borel fails in infinite dimensions. The closed unit ball in an infinite-dimensional normed space is NOT compact. This is a common error.

### Connectedness
- S ⊂ ℝ is connected ⟺ S is an interval
- Intermediate Value Theorem is a consequence of connectedness of intervals

### Baire Category Theorem
A complete metric space is not a countable union of nowhere-dense sets. Equivalently, the intersection of countably many dense open sets is dense.

**Applications:** Existence of continuous nowhere-differentiable functions, existence of transcendental numbers, proof of the Uniform Boundedness Principle.

---

## Continuity

### Equivalent Definitions
For f: D → ℝ, the following are equivalent at a point c ∈ D:
1. **(ε-δ):** ∀ε > 0, ∃δ > 0 such that |x - c| < δ and x ∈ D ⟹ |f(x) - f(c)| < ε
2. **(Sequential):** For every sequence (xₙ) in D with xₙ → c, we have f(xₙ) → f(c)
3. **(Topological):** Preimage of every open set is open (for continuity on all of D)

### Uniform Continuity
f: D → ℝ is uniformly continuous if:
∀ε > 0, ∃δ > 0 such that |x - y| < δ ⟹ |f(x) - f(y)| < ε for ALL x, y ∈ D.

**Key difference from pointwise continuity:** δ depends only on ε, not on the point.

**Theorem:** A continuous function on a compact set is uniformly continuous.

### Extreme Value Theorem
A continuous function on a compact set attains its maximum and minimum.

### Types of Discontinuities
- **Removable:** Both one-sided limits exist and are equal, but ≠ f(c) (or f(c) undefined)
- **Jump:** Both one-sided limits exist but are unequal
- **Essential/Oscillatory:** At least one one-sided limit fails to exist

### Lipschitz Continuity
f is Lipschitz if ∃M > 0: |f(x) - f(y)| ≤ M|x - y| for all x, y.

**Hierarchy:** Contraction ⊂ Lipschitz ⊂ Uniformly Continuous ⊂ Continuous
(All inclusions are strict.)

---

## Differentiation

### Definition
f'(c) = lim_{h→0} [f(c+h) - f(c)] / h, if this limit exists.

**Fact:** Differentiable at c ⟹ continuous at c. Converse is FALSE (e.g., |x| at 0).

### Mean Value Theorem (MVT)
If f is continuous on [a,b] and differentiable on (a,b), then ∃c ∈ (a,b) with
f'(c) = [f(b) - f(a)] / (b - a).

**Applications:** If f' = 0 on an interval, then f is constant. If f' > 0, then f is strictly increasing.

### Taylor's Theorem
f(x) = Σ_{k=0}^{n} f^{(k)}(c)/k! · (x-c)^k + Rₙ(x)

where the remainder Rₙ can be expressed in Lagrange form:
Rₙ(x) = f^{(n+1)}(ξ)/(n+1)! · (x-c)^{n+1} for some ξ between c and x.

### L'Hôpital's Rule
If f(x)/g(x) is 0/0 or ∞/∞ and f'(x)/g'(x) → L, then f(x)/g(x) → L.

**Caution:** The converse is false. f(x)/g(x) may have a limit even when f'(x)/g'(x) does not.

### Weierstrass Approximation Theorem
Every continuous function on [a,b] can be uniformly approximated by polynomials.

---

## Riemann Integration

### Definition via Darboux Sums
For a bounded function f on [a,b] and partition P = {x₀, ..., xₙ}:
- Lower sum: L(f, P) = Σ (inf f on [xⱼ₋₁, xⱼ]) · (xⱼ - xⱼ₋₁)
- Upper sum: U(f, P) = Σ (sup f on [xⱼ₋₁, xⱼ]) · (xⱼ - xⱼ₋₁)

f is Riemann integrable if sup_P L(f, P) = inf_P U(f, P).

### Lebesgue's Criterion for Riemann Integrability
A bounded function on [a,b] is Riemann integrable ⟺ its set of discontinuities has Lebesgue measure zero.

**Classic examples:**
- Thomae's function (rational indicator variant): Riemann integrable (discontinuities = ℚ, measure zero)
- Dirichlet function (indicator of ℚ): NOT Riemann integrable (discontinuous everywhere)

### Fundamental Theorem of Calculus
**Part I:** If f is continuous on [a,b] and F(x) = ∫ₐˣ f(t) dt, then F'(x) = f(x).
**Part II:** If F is an antiderivative of f on [a,b] and f is Riemann integrable, then ∫ₐᵇ f(x) dx = F(b) - F(a).

---

## Sequences and Series of Functions

### Pointwise vs. Uniform Convergence
- **Pointwise:** ∀x, ∀ε > 0, ∃N(x, ε) such that n ≥ N ⟹ |fₙ(x) - f(x)| < ε
- **Uniform:** ∀ε > 0, ∃N(ε) such that ∀x, n ≥ N ⟹ |fₙ(x) - f(x)| < ε

**The difference:** In uniform convergence, N does not depend on x.

### What Uniform Convergence Preserves
- Continuity: uniform limit of continuous functions is continuous
- Integration: if fₙ → f uniformly on [a,b], then ∫fₙ → ∫f
- **NOT** differentiation in general (need extra conditions)

### Weierstrass M-Test
If |fₙ(x)| ≤ Mₙ for all x, and ΣMₙ converges, then Σfₙ converges uniformly and absolutely.

### Arzela-Ascoli Theorem
A sequence of functions in C([a,b]) has a uniformly convergent subsequence ⟺ it is uniformly bounded and equicontinuous.

**Why it matters:** This is the correct compactness criterion for function spaces, replacing Bolzano-Weierstrass.

### Stone-Weierstrass Theorem
A subalgebra of C(K) (K compact Hausdorff) that separates points and contains the constants is dense in C(K) under the sup norm. This generalizes the Weierstrass Approximation Theorem.
