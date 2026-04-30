# Operator Theory

## Table of Contents
1. [Compact Operators](#compact-operators)
2. [Spectral Theory Basics](#spectral-theory-basics)
3. [Spectral Theory of Compact Operators](#spectral-theory-of-compact-operators)
4. [Self-Adjoint Operators](#self-adjoint-operators)
5. [Spectral Theorem](#spectral-theorem)
6. [Fredholm Theory](#fredholm-theory)

---

## Compact Operators

### Definition
T: X → Y (between normed spaces) is compact if T maps bounded sets to precompact sets (sets whose closure is compact).

Equivalently: T is compact if for every bounded sequence (xₙ) in X, the sequence (Txₙ) has a convergent subsequence in Y.

### Properties
- Every finite-rank operator is compact
- Compact operators form a closed subspace of B(X, Y) (if Y is Banach)
- If T is compact, then T is bounded (but NOT conversely in infinite dimensions)
- The composition of a bounded operator with a compact operator (in either order) is compact
- T is compact ⟹ T* (adjoint) is compact (Schauder's theorem)

### Examples
- **Integral operators** with continuous or L² kernels: (Tf)(x) = ∫ K(x,y) f(y) dy
- **Diagonal operators** on ℓ² with eigenvalues → 0: T(eₙ) = λₙeₙ with λₙ → 0
- The inclusion ℓ¹ ↪ ℓ² is NOT compact
- The identity on an infinite-dimensional space is NEVER compact

### Compact ≠ Closed Range
A compact operator on an infinite-dimensional space has range that is NOT closed (unless finite-rank).

**Why this matters:** If Tx = y has a solution for a compact T, small perturbations of y may not have solutions. This is the essence of ill-posed problems.

---

## Spectral Theory Basics

### Resolvent and Spectrum
For T ∈ B(X) (X a Banach space over ℂ):
- **Resolvent set** ρ(T) = { λ ∈ ℂ : (T - λI) is bijective with bounded inverse }
- **Spectrum** σ(T) = ℂ \ ρ(T)
- **Resolvent operator** R(λ, T) = (T - λI)⁻¹ for λ ∈ ρ(T)

### Partition of the Spectrum
- **Point spectrum** σ_p(T) = { λ : T - λI is not injective } (eigenvalues)
- **Continuous spectrum** σ_c(T) = { λ : T - λI is injective, has dense but not closed range }
- **Residual spectrum** σ_r(T) = { λ : T - λI is injective, range is not dense }

σ(T) = σ_p(T) ∪ σ_c(T) ∪ σ_r(T) (disjoint union)

### Basic Properties of the Spectrum
- σ(T) is a nonempty compact subset of ℂ (for T ∈ B(X), X Banach over ℂ)
- σ(T) ⊂ { λ : |λ| ≤ ‖T‖ }
- **Spectral radius:** r(T) = sup { |λ| : λ ∈ σ(T) } = lim ‖Tⁿ‖^{1/n}
- The resolvent R(λ, T) is an analytic B(X)-valued function on ρ(T)
- Resolvent identity: R(λ, T) - R(μ, T) = (μ - λ)R(λ, T)R(μ, T)

### Spectrum of Specific Operators
- Finite-dimensional: σ(T) = σ_p(T) = { eigenvalues }
- Right shift on ℓ²: σ_p = ∅, σ(T) = closed unit disk
- Left shift on ℓ²: σ_p = open unit disk, σ(T) = closed unit disk
- Multiplication operator M_φ on L²: σ(M_φ) = essential range of φ

---

## Spectral Theory of Compact Operators

### Riesz-Schauder Theory
For a compact operator T on a Banach space X:

1. **σ(T) is countable** with no accumulation point except possibly 0
2. **Every nonzero λ ∈ σ(T) is an eigenvalue** (no continuous or residual spectrum away from 0)
3. **Each nonzero eigenvalue has finite multiplicity** (finite-dimensional eigenspace)
4. **0 ∈ σ(T)** if X is infinite-dimensional
5. If σ(T) is infinite, the eigenvalues form a sequence converging to 0

### Fredholm Alternative
For a compact operator T on a Banach space and λ ≠ 0:

**Exactly one of the following holds:**
- (T - λI) is bijective (so (T - λI)⁻¹ exists and is bounded)
- λ is an eigenvalue of T

**For equations:** The equation (T - λI)x = y either:
- Has a unique solution for every y, OR
- Has a solution only for y ⊥ ker(T* - λ̄I), and the solution is non-unique (up to adding elements of ker(T - λI))

**Applications:** Integral equations of the second kind: x - λKx = y. Either uniquely solvable for all y, or the homogeneous equation has nontrivial solutions.

---

## Self-Adjoint Operators

### On Hilbert Spaces
T ∈ B(H) is self-adjoint if T = T*, i.e., ⟨Tx, y⟩ = ⟨x, Ty⟩ for all x, y ∈ H.

### Properties of Self-Adjoint Operators
- All eigenvalues are real
- Eigenvectors for distinct eigenvalues are orthogonal
- σ(T) ⊂ ℝ
- σ_r(T) = ∅ (no residual spectrum)
- ‖T‖ = sup { |⟨Tx, x⟩| : ‖x‖ = 1 }
- r(T) = ‖T‖ (spectral radius equals norm)

### Normal Operators
T is normal if TT* = T*T.

Self-adjoint, unitary, and skew-adjoint operators are all normal.

**For normal operators:**
- ‖Tx‖ = ‖T*x‖ for all x
- σ_r(T) = ∅
- Eigenvectors for distinct eigenvalues are orthogonal

### Positive Operators
T ≥ 0 means ⟨Tx, x⟩ ≥ 0 for all x ∈ H.

**Properties:**
- Positive operators are self-adjoint
- σ(T) ⊂ [0, ∞)
- Every positive operator has a unique positive square root

---

## Spectral Theorem

### For Compact Self-Adjoint Operators
If T is a compact self-adjoint operator on a Hilbert space H, then:

1. There exists an orthonormal system {eₙ} of eigenvectors with real eigenvalues λₙ → 0
2. Every x ∈ H can be written as: Tx = Σ λₙ ⟨x, eₙ⟩ eₙ
3. H = ker(T) ⊕ span{eₙ} (orthogonal direct sum)

**This is the infinite-dimensional analogue of diagonalization for symmetric matrices.**

### For Bounded Self-Adjoint Operators
T = ∫_{σ(T)} λ dE(λ)

where E is the spectral measure (projection-valued measure) associated to T.

**The spectral measure E:**
- For each Borel set B ⊂ ℝ, E(B) is an orthogonal projection
- E(σ(T)) = I, E(∅) = 0
- E(B₁ ∩ B₂) = E(B₁)E(B₂)
- E(∪ Bₙ) = Σ E(Bₙ) (strong operator convergence, for disjoint Bₙ)

### Continuous Functional Calculus
For T self-adjoint with spectrum σ(T), there is a unique isometric *-homomorphism
Φ: C(σ(T)) → B(H) with Φ(1) = I and Φ(id) = T.

This lets us define f(T) for any continuous function f on σ(T).

**Extends to:** Borel functional calculus (bounded measurable functions).

### Min-Max Principle (Courant-Fischer)
For a compact self-adjoint operator T with eigenvalues λ₁ ≥ λ₂ ≥ ... → 0:

λₙ = max_{dim V = n} min_{x ∈ V, ‖x‖=1} ⟨Tx, x⟩

This is essential for variational characterization of eigenvalues.

---

## Fredholm Theory

### Fredholm Operators
T ∈ B(X, Y) is Fredholm if:
- dim ker(T) < ∞
- dim coker(T) = dim(Y / Range(T)) < ∞
- Range(T) is closed

### Fredholm Index
ind(T) = dim ker(T) - dim coker(T)

**Properties:**
- ind(T₁T₂) = ind(T₁) + ind(T₂)
- ind(T + K) = ind(T) for any compact K (index is stable under compact perturbation)
- ind is continuous: constant on connected components of Fredholm operators
- ind(T*) = -ind(T)

### Atkinson's Theorem
T ∈ B(X, Y) is Fredholm ⟺ T is invertible modulo compact operators.
That is, ∃ S ∈ B(Y, X) with ST - I and TS - I both compact.

### Essential Spectrum
σ_ess(T) = { λ : T - λI is not Fredholm }

The essential spectrum is invariant under compact perturbations.
