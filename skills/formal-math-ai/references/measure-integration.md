# Measure Theory and Integration

## Table of Contents
1. [Outer Measure and Lebesgue Measure](#outer-measure-and-lebesgue-measure)
2. [Measurable Sets and Sigma-Algebras](#measurable-sets-and-sigma-algebras)
3. [Measurable Functions](#measurable-functions)
4. [Lebesgue Integration](#lebesgue-integration)
5. [Convergence Theorems](#convergence-theorems)
6. [Product Measures and Fubini's Theorem](#product-measures-and-fubinis-theorem)
7. [Differentiation and Integration](#differentiation-and-integration)
8. [Signed Measures and Radon-Nikodym](#signed-measures-and-radon-nikodym)

---

## Outer Measure and Lebesgue Measure

### Outer Measure on ℝ
For A ⊂ ℝ, define:
|A|* = inf { Σ ℓ(Iₖ) : A ⊂ ∪ Iₖ, each Iₖ an open interval }
where ℓ(I) is the length of interval I.

**Properties of outer measure:**
- |∅|* = 0
- A ⊂ B ⟹ |A|* ≤ |B|*  (monotonicity)
- |∪ Aₖ|* ≤ Σ |Aₖ|*  (countable subadditivity)
- Outer measure is NOT additive in general (this motivates restricting to measurable sets)

### Carathéodory's Criterion
A set E ⊂ ℝ is Lebesgue measurable if for every A ⊂ ℝ:
|A|* = |A ∩ E|* + |A ∩ Eᶜ|*

**Intuition:** E "splits" every set cleanly with respect to outer measure.

### Properties of Lebesgue Measure
- Every open set and every closed set is measurable
- Countable sets have measure zero
- The Cantor set has measure zero but is uncountable
- Lebesgue measure is translation-invariant
- There exist non-measurable sets (Vitali sets, requires Axiom of Choice)
- Lebesgue measure is the completion of Borel measure

---

## Measurable Sets and Sigma-Algebras

### Sigma-Algebra
A collection 𝒮 of subsets of X is a σ-algebra if:
1. ∅ ∈ 𝒮
2. E ∈ 𝒮 ⟹ Eᶜ ∈ 𝒮  (closed under complement)
3. E₁, E₂, ... ∈ 𝒮 ⟹ ∪ Eₙ ∈ 𝒮  (closed under countable union)

**Consequences:** Also closed under countable intersection, set difference, symmetric difference.

### Borel σ-algebra
The smallest σ-algebra containing all open sets of a topological space. Denoted 𝓑 or 𝓑(ℝ).

**Generated equivalently by:** open sets, closed sets, open intervals, half-open intervals, compact sets, Gδ sets, Fσ sets.

### Abstract Measure
A measure μ on (X, 𝒮) is a function μ: 𝒮 → [0, ∞] such that:
1. μ(∅) = 0
2. Countable additivity: μ(∪ Eₙ) = Σ μ(Eₙ) for disjoint Eₙ ∈ 𝒮

### Important Measure Types
- **Finite measure:** μ(X) < ∞
- **σ-finite:** X = ∪ Eₙ with μ(Eₙ) < ∞ for each n
- **Probability measure:** μ(X) = 1
- **Counting measure:** μ(E) = |E| (cardinality)
- **Complete measure:** If μ(E) = 0 and F ⊂ E, then F is measurable

---

## Measurable Functions

### Definition
f: X → ℝ̄ is measurable (with respect to σ-algebra 𝒮) if:
f⁻¹((a, ∞]) = {x : f(x) > a} ∈ 𝒮 for every a ∈ ℝ.

**Equivalent conditions:** Can replace (a, ∞] with [a, ∞], (-∞, a), (-∞, a], or any Borel set.

### Closure Properties
- Sums, products, max, min of measurable functions are measurable
- Pointwise limits of measurable functions are measurable
- lim sup, lim inf of measurable functions are measurable
- Composition: if f is measurable and g is Borel measurable (or continuous), then g ∘ f is measurable

### Simple Functions
A simple function takes finitely many values: φ = Σ aᵢ χ_{Eᵢ} where Eᵢ are measurable sets.

**Approximation theorem:** Every nonneg measurable function is the pointwise limit of an increasing sequence of nonneg simple functions. If f is bounded, the convergence is uniform.

---

## Lebesgue Integration

### Construction (three stages)

**Stage 1 — Simple functions:**
∫ φ dμ = Σ aᵢ · μ(Eᵢ)  for φ = Σ aᵢ χ_{Eᵢ}

**Stage 2 — Nonnegative measurable functions:**
∫ f dμ = sup { ∫ φ dμ : 0 ≤ φ ≤ f, φ simple }

**Stage 3 — General measurable functions:**
Write f = f⁺ - f⁻ where f⁺ = max(f, 0), f⁻ = max(-f, 0).
f is integrable if both ∫ f⁺ dμ and ∫ f⁻ dμ are finite.
Then ∫ f dμ = ∫ f⁺ dμ - ∫ f⁻ dμ.

**Equivalently:** f is integrable ⟺ ∫ |f| dμ < ∞.

### Comparison with Riemann Integral
- Every Riemann integrable function on [a,b] is Lebesgue integrable, with the same value
- Lebesgue integral handles more functions (e.g., indicator of ℚ ∩ [0,1])
- Lebesgue integral has far better convergence theorems

---

## Convergence Theorems

### Monotone Convergence Theorem (MCT)
If 0 ≤ f₁ ≤ f₂ ≤ ... are measurable and fₙ → f pointwise, then:
∫ f dμ = lim ∫ fₙ dμ

**Hypotheses to check:**
- Functions must be nonneg (or bounded below)
- Sequence must be increasing
- No domination condition needed

### Fatou's Lemma
If fₙ ≥ 0 are measurable, then:
∫ lim inf fₙ dμ ≤ lim inf ∫ fₙ dμ

**Warning:** Equality can fail. The inequality can be strict.
**Classic counterexample:** fₙ = n · χ_{[0, 1/n]} on [0,1]. Then fₙ → 0 a.e. but ∫ fₙ = 1 for all n.

### Dominated Convergence Theorem (DCT)
If fₙ → f pointwise (or a.e.), and |fₙ| ≤ g for some integrable g, then:
∫ f dμ = lim ∫ fₙ dμ

**Hypotheses to check (common errors):**
1. Pointwise (or a.e.) convergence — NOT just convergence in measure
2. Dominating function g must be INTEGRABLE (∫ g dμ < ∞)
3. The bound |fₙ(x)| ≤ g(x) must hold for ALL n (not just large n — though this is easily fixed)

### Generalized DCT
Replace |fₙ| ≤ g with |fₙ| ≤ gₙ where gₙ → g pointwise and ∫ gₙ → ∫ g < ∞.

### Vitali Convergence Theorem
On a finite measure space: fₙ → f in measure + {fₙ} uniformly integrable ⟹ ∫ fₙ → ∫ f.

---

## Product Measures and Fubini's Theorem

### Product σ-algebra
Given (X, 𝒜) and (Y, 𝓑), the product σ-algebra 𝒜 ⊗ 𝓑 is generated by rectangles A × B with A ∈ 𝒜, B ∈ 𝓑.

### Tonelli's Theorem (Nonnegative functions)
If f: X × Y → [0, ∞] is 𝒜 ⊗ 𝓑-measurable and μ, ν are σ-finite, then:
∫∫ f d(μ × ν) = ∫_X (∫_Y f(x,y) dν(y)) dμ(x) = ∫_Y (∫_X f(x,y) dμ(x)) dν(y)

**Key:** No integrability assumption needed — works for nonneg functions (may be ∞).

### Fubini's Theorem (Integrable functions)
If f is integrable with respect to the product measure μ × ν (σ-finite), then:
- For a.e. x, the function y ↦ f(x,y) is integrable
- The iterated integrals exist and equal the double integral

**Strategy:** Use Tonelli first on |f| to check integrability, then apply Fubini to f.

---

## Differentiation and Integration

### Lebesgue Differentiation Theorem
If f is locally integrable on ℝⁿ, then for a.e. x:
lim_{r→0} (1/|B(x,r)|) ∫_{B(x,r)} f(y) dy = f(x)

### Hardy-Littlewood Maximal Function
Mf(x) = sup_{r>0} (1/|B(x,r)|) ∫_{B(x,r)} |f(y)| dy

**Maximal inequality:** μ({x : Mf(x) > λ}) ≤ C/λ · ∫ |f| dμ  (weak type (1,1))

### Functions of Bounded Variation
f is BV on [a,b] if: V(f) = sup_{P} Σ |f(xⱼ) - f(xⱼ₋₁)| < ∞

**Jordan Decomposition:** BV functions = difference of two increasing functions.

### Absolutely Continuous Functions
f is absolutely continuous on [a,b] if: ∀ε > 0, ∃δ > 0 such that for any finite collection of disjoint intervals (aₖ, bₖ) in [a,b] with Σ(bₖ - aₖ) < δ, we have Σ|f(bₖ) - f(aₖ)| < ε.

**Fundamental Theorem of Calculus for Lebesgue integral:**
f is absolutely continuous ⟺ f' exists a.e., f' is integrable, and f(x) - f(a) = ∫ₐˣ f'(t) dt.

---

## Signed Measures and Radon-Nikodym

### Signed Measures
A signed measure ν on (X, 𝒮) takes values in [-∞, ∞] (but not both -∞ and +∞), with ν(∅) = 0 and countable additivity.

### Hahn Decomposition
For any signed measure ν, there exist measurable sets P, N with:
- X = P ∪ N, P ∩ N = ∅
- ν(E) ≥ 0 for all measurable E ⊂ P
- ν(E) ≤ 0 for all measurable E ⊂ N

### Jordan Decomposition
ν = ν⁺ - ν⁻ where ν⁺(E) = ν(E ∩ P), ν⁻(E) = -ν(E ∩ N).
|ν| = ν⁺ + ν⁻ is the total variation measure.

### Absolute Continuity
ν ≪ μ means: μ(E) = 0 ⟹ ν(E) = 0.

### Radon-Nikodym Theorem
If μ is σ-finite and ν ≪ μ, then there exists a measurable function f ≥ 0 (the Radon-Nikodym derivative dν/dμ) such that:
ν(E) = ∫_E f dμ for all measurable E.

**The function f is unique up to μ-a.e. equality.**

### Lebesgue Decomposition
Any σ-finite measure ν can be uniquely written as ν = νₐ + νₛ where νₐ ≪ μ and νₛ ⊥ μ.
