# Hilbert Spaces and Banach Spaces

## Table of Contents
1. [Normed Spaces and Banach Spaces](#normed-spaces-and-banach-spaces)
2. [Inner Product Spaces and Hilbert Spaces](#inner-product-spaces-and-hilbert-spaces)
3. [Lp Spaces](#lp-spaces)
4. [Orthogonality and Projections](#orthogonality-and-projections)
5. [Orthonormal Bases](#orthonormal-bases)
6. [Classical Banach Spaces](#classical-banach-spaces)

---

## Normed Spaces and Banach Spaces

### Normed Space
A vector space X (over ℝ or ℂ) with a function ‖·‖ : X → [0, ∞) satisfying:
1. ‖x‖ = 0 ⟺ x = 0  (positive definiteness)
2. ‖αx‖ = |α| · ‖x‖  (homogeneity)
3. ‖x + y‖ ≤ ‖x‖ + ‖y‖  (triangle inequality)

Every normed space is a metric space via d(x, y) = ‖x - y‖.

### Banach Space
A complete normed space (every Cauchy sequence converges).

**Standard technique to show completeness:**
1. Take an arbitrary Cauchy sequence (xₙ)
2. Find a candidate limit x (often by completeness of ℝ or ℂ, applied coordinate-wise or pointwise)
3. Show x is in the space
4. Show ‖xₙ - x‖ → 0

**Useful criterion:** A normed space X is Banach ⟺ every absolutely convergent series converges (i.e., Σ ‖xₙ‖ < ∞ ⟹ Σ xₙ converges in X).

### Equivalent Norms
Two norms ‖·‖₁ and ‖·‖₂ on X are equivalent if ∃ c, C > 0:
c · ‖x‖₁ ≤ ‖x‖₂ ≤ C · ‖x‖₁ for all x ∈ X.

**Theorem:** On a finite-dimensional vector space, ALL norms are equivalent.

**Consequence:** Every finite-dimensional normed space is a Banach space, and every finite-dimensional subspace is closed.

**WARNING:** This fails in infinite dimensions. Different norms can give different topologies and different completions.

### Schauder Basis
A sequence (eₙ) in a Banach space X such that every x ∈ X has a unique representation x = Σ αₙ eₙ (convergent in norm).

**Not every separable Banach space has a Schauder basis** (Enflo's counterexample, 1973).

---

## Inner Product Spaces and Hilbert Spaces

### Inner Product
A function ⟨·,·⟩ : X × X → 𝔽 (ℝ or ℂ) satisfying:
1. ⟨x, x⟩ ≥ 0, with equality ⟺ x = 0
2. ⟨x + y, z⟩ = ⟨x, z⟩ + ⟨y, z⟩
3. ⟨αx, y⟩ = α⟨x, y⟩
4. ⟨x, y⟩ = conjugate(⟨y, x⟩)

**Convention warning:** Physicists use linearity in the second argument. Mathematicians typically use linearity in the first argument. Be explicit about which convention you're using.

Every inner product induces a norm: ‖x‖ = √⟨x, x⟩.

### Hilbert Space
A complete inner product space (equivalently, a Banach space whose norm comes from an inner product).

### Parallelogram Law
‖x + y‖² + ‖x - y‖² = 2(‖x‖² + ‖y‖²)

**This characterizes inner product spaces:** A norm satisfies the parallelogram law ⟺ it comes from an inner product (via the polarization identity).

### Polarization Identity
- Real case: ⟨x, y⟩ = ¼(‖x+y‖² - ‖x-y‖²)
- Complex case: ⟨x, y⟩ = ¼(‖x+y‖² - ‖x-y‖² + i‖x+iy‖² - i‖x-iy‖²)

### Cauchy-Schwarz Inequality
|⟨x, y⟩| ≤ ‖x‖ · ‖y‖

Equality holds ⟺ x and y are linearly dependent.

---

## Lp Spaces

### Definition
For a measure space (X, 𝒮, μ) and 1 ≤ p < ∞:
Lp(μ) = { measurable f : ∫ |f|ᵖ dμ < ∞ } / (a.e. equality)

with norm ‖f‖_p = (∫ |f|ᵖ dμ)^{1/p}.

For p = ∞:
L∞(μ) = { measurable f : ess sup |f| < ∞ } / (a.e. equality)

with norm ‖f‖_∞ = ess sup |f| = inf { M : |f(x)| ≤ M a.e. }.

### Key Inequalities

**Hölder's Inequality:**
If 1/p + 1/q = 1 (conjugate exponents), then:
∫ |fg| dμ ≤ ‖f‖_p · ‖g‖_q

Special case p = q = 2: this is Cauchy-Schwarz.

**Minkowski's Inequality:**
‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p

This is the triangle inequality for Lp, establishing that ‖·‖_p is indeed a norm.

### Completeness (Riesz-Fischer Theorem)
Lp(μ) is a Banach space for 1 ≤ p ≤ ∞.

**Proof strategy for 1 ≤ p < ∞:**
1. Take a Cauchy sequence (fₙ) in Lp
2. Extract a subsequence (fₙₖ) with ‖fₙₖ₊₁ - fₙₖ‖_p < 2⁻ᵏ
3. Define g = Σ |fₙₖ₊₁ - fₙₖ|, show g ∈ Lp using Minkowski
4. The telescoping series converges a.e. to some f
5. Verify f ∈ Lp and ‖fₙ - f‖_p → 0

### L² is a Hilbert Space
With inner product ⟨f, g⟩ = ∫ f · ḡ dμ.

This is the ONLY Lp space that is a Hilbert space (for p ≠ 2, the norm doesn't satisfy the parallelogram law).

### Duality of Lp Spaces
For 1 ≤ p < ∞ with conjugate exponent q (1/p + 1/q = 1):
(Lp)* ≅ Lq  (isometric isomorphism)

Every bounded linear functional on Lp has the form f ↦ ∫ fg dμ for a unique g ∈ Lq.

**Exception:** (L∞)* is NOT L¹ in general. It is strictly larger (contains singular functionals).

### Sequence Spaces (ℓp)
ℓp = Lp(ℕ, counting measure) = { sequences (xₙ) : Σ |xₙ|ᵖ < ∞ }

These are important concrete examples:
- ℓ¹: absolutely summable sequences
- ℓ²: square-summable sequences (Hilbert space)
- ℓ∞: bounded sequences
- c₀: sequences converging to 0 (closed subspace of ℓ∞)

**Inclusions:** ℓ¹ ⊂ ℓ² ⊂ ℓp ⊂ ℓq ⊂ c₀ ⊂ ℓ∞  for 1 ≤ p ≤ q

---

## Orthogonality and Projections

### Orthogonal Complement
For a subset S of a Hilbert space H:
S⊥ = { y ∈ H : ⟨x, y⟩ = 0 for all x ∈ S }

**Properties:**
- S⊥ is always a closed subspace
- (S⊥)⊥ = span(S) (the closed linear span)
- H = M ⊕ M⊥ for every closed subspace M (orthogonal decomposition)

### Projection Theorem
Let M be a closed subspace of a Hilbert space H. For every x ∈ H, there exists a UNIQUE y ∈ M (the orthogonal projection) minimizing ‖x - y‖.

Moreover: x - y ∈ M⊥, i.e., x = y + (x - y) is the orthogonal decomposition.

**WARNING:** This requires M to be CLOSED. And it requires a Hilbert space (or at least a uniformly convex Banach space). In a general Banach space, closest points to a subspace may not exist or may not be unique.

### Riesz Representation Theorem (Hilbert spaces)
Every bounded linear functional φ on a Hilbert space H has the form φ(x) = ⟨x, y⟩ for a unique y ∈ H.
Moreover, ‖φ‖ = ‖y‖.

**This means:** H* ≅ H (isometric anti-isomorphism). Hilbert spaces are self-dual.

---

## Orthonormal Bases

### Orthonormal System
A set {eα} in H is orthonormal if:
- ⟨eα, eβ⟩ = 0 for α ≠ β
- ‖eα‖ = 1 for all α

### Bessel's Inequality
For any orthonormal system {eα} and any x ∈ H:
Σ |⟨x, eα⟩|² ≤ ‖x‖²

### Parseval's Identity
An orthonormal system {eₙ} is a basis ⟺ for all x ∈ H:
‖x‖² = Σ |⟨x, eₙ⟩|²

Equivalently: x = Σ ⟨x, eₙ⟩ eₙ for all x ∈ H.

### Existence of Orthonormal Bases
Every Hilbert space has an orthonormal basis (by Zorn's lemma in the uncountable case).

A Hilbert space is separable ⟺ it has a countable orthonormal basis.

**All separable infinite-dimensional Hilbert spaces are isomorphic to ℓ².**

### Gram-Schmidt Orthogonalization
Given a linearly independent sequence (xₙ), produce orthonormal (eₙ) with:
span{e₁, ..., eₙ} = span{x₁, ..., xₙ} for each n.

---

## Classical Banach Spaces

### Summary Table

| Space | Elements | Norm | Banach? | Hilbert? | Separable? | Dual |
|-------|----------|------|---------|----------|------------|------|
| ℓp (1≤p<∞) | Sequences, Σ\|xₙ\|ᵖ < ∞ | (Σ\|xₙ\|ᵖ)^{1/p} | Yes | Only p=2 | Yes | ℓq |
| ℓ∞ | Bounded sequences | sup\|xₙ\| | Yes | No | No | ≠ ℓ¹ |
| c₀ | Sequences → 0 | sup\|xₙ\| | Yes | No | Yes | ℓ¹ |
| c | Convergent sequences | sup\|xₙ\| | Yes | No | Yes | ℓ¹ |
| Lp[0,1] (1≤p<∞) | Functions, ∫\|f\|ᵖ < ∞ | (∫\|f\|ᵖ)^{1/p} | Yes | Only p=2 | Yes | Lq |
| L∞[0,1] | Ess. bounded functions | ess sup\|f\| | Yes | No | No | ≠ L¹ |
| C[0,1] | Continuous functions | sup\|f(x)\| | Yes | No | Yes | Radon measures |
| C₀(ℝ) | Continuous, vanishing at ∞ | sup\|f\| | Yes | No | Yes | Radon measures |

### Key Distinctions
- ℓ¹ is NOT reflexive ((ℓ¹)** ≅ (ℓ∞)* ≠ ℓ¹)
- C[0,1] is NOT reflexive
- Lp for 1 < p < ∞ IS reflexive
- L¹ is NOT reflexive
- Every reflexive Banach space has the Radon-Nikodym property
