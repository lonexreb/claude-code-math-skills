# Proof Techniques in Analysis

## Table of Contents
1. [Epsilon-Delta and Epsilon-N Proofs](#epsilon-delta-and-epsilon-n-proofs)
2. [Approximation and Density Arguments](#approximation-and-density-arguments)
3. [Compactness Arguments](#compactness-arguments)
4. [Baire Category Arguments](#baire-category-arguments)
5. [Duality and Separation Arguments](#duality-and-separation-arguments)
6. [Diagonal Arguments](#diagonal-arguments)
7. [Fixed Point Theorems](#fixed-point-theorems)
8. [Counterexample Construction Strategies](#counterexample-construction-strategies)
9. [Common Proof Patterns](#common-proof-patterns)

---

## Epsilon-Delta and Epsilon-N Proofs

### Template for Limit Proofs
**Goal:** Show lim_{n→∞} aₙ = L.

**Structure:**
1. Let ε > 0 be given.
2. [Scratch work: figure out how large N needs to be. Work backwards from |aₙ - L| < ε.]
3. Choose N = [your choice, depending on ε].
4. Suppose n ≥ N. Then: |aₙ - L| = ... ≤ ... < ε.

**Common tricks:**
- Use the Archimedean property: choose N > 1/ε
- Use triangle inequality: |aₙ - L| ≤ |aₙ - bₙ| + |bₙ - L|, then bound each piece
- For products: use |ab - cd| = |a(b-d) + d(a-c)| with bounded factors
- For quotients: first establish a lower bound on the denominator for large n

### Template for Continuity Proofs
**Goal:** Show f is continuous at c.

**Structure:**
1. Let ε > 0 be given.
2. [Scratch work: express |f(x) - f(c)| in terms of |x - c|.]
3. Choose δ = [your choice, depending on ε and possibly c].
4. Suppose |x - c| < δ. Then: |f(x) - f(c)| = ... ≤ ... < ε.

### Template for Uniform Continuity
Same as above, but δ must NOT depend on c. If your δ depends on c, the function may not be uniformly continuous.

**Strategy to show NOT uniformly continuous:** Find sequences (xₙ), (yₙ) with |xₙ - yₙ| → 0 but |f(xₙ) - f(yₙ)| ≥ ε₀ for some fixed ε₀.

---

## Approximation and Density Arguments

### The "Dense Subclass" Strategy
To prove a property P holds for all elements of a space X:
1. Prove P for a dense subspace D ⊂ X (e.g., continuous functions, simple functions, polynomials)
2. Show P is preserved under limits (or the map involved is continuous)
3. Conclude P holds on all of X

**Where this is used constantly:**
- Proving Lp results: first for simple functions, then extend
- Proving operator identities: first on a dense subspace
- Stone-Weierstrass: polynomials are dense in C[a,b]

### ε/3 Argument (Three-Epsilon Trick)
To show ‖f - g‖ < ε:
1. Approximate f by something simple f̃ within ε/3
2. Show the operation preserves approximation: ‖T(f̃) - T(f)‖ < ε/3
3. Bound the remaining piece: ‖T(f̃) - g‖ < ε/3

**Classic use:** Proving the uniform limit of continuous functions is continuous.

### Mollification / Convolution Approximation
For Lp functions on ℝⁿ, convolve with a smooth approximate identity φε to get smooth approximations:
fε = f * φε → f in Lp as ε → 0.

---

## Compactness Arguments

### Sequential Compactness Strategy
**Goal:** Extract a convergent subsequence.
1. Show the sequence is bounded in the relevant norm
2. Apply the appropriate compactness theorem:
   - Bolzano-Weierstrass in ℝⁿ (bounded ⟹ convergent subsequence)
   - Arzelà-Ascoli in C(K) (bounded + equicontinuous ⟹ convergent subsequence)
   - Weak compactness in reflexive spaces (bounded ⟹ weakly convergent subsequence)
   - Banach-Alaoglu in X* (bounded ⟹ weak*-convergent subnet/subsequence)
3. Identify the limit and verify convergence

### Covering Compactness Strategy
**Goal:** Reduce to finitely many cases.
1. Cover the compact set with open sets having a useful property
2. Extract a finite subcover
3. Use the finite subcover to obtain uniform bounds or uniform estimates

**Classic uses:** Proving uniform continuity on compact sets, proving equicontinuity implies uniform equicontinuity on compact sets.

### The Cantor Diagonal Trick for Subsequences
When you need convergence on a countable dense set:
1. List the dense set as {q₁, q₂, ...}
2. Extract a subsequence converging at q₁
3. From that, extract a further subsequence converging at q₂
4. Continue for all qₙ
5. Take the diagonal subsequence — it converges at ALL qₙ
6. Use density + equicontinuity to extend convergence everywhere

**This is the core of the Arzelà-Ascoli proof.**

---

## Baire Category Arguments

### Template
**Goal:** Show a "large" set of objects has a property P (or show a specific object exists).

1. Express the set lacking P as a countable union of sets: Bad = ∪ Fₙ
2. Show each Fₙ is closed (or at least has empty interior)
3. Conclude by Baire's theorem that Bad has empty interior (is meager/first category)
4. Therefore the complement (objects with property P) is a dense Gδ set

### When to Reach for Baire Category
- "There exists a continuous function with property X" — often proved by showing the set of functions WITHOUT property X is meager
- Proving the Uniform Boundedness Principle
- Existence of continuous nowhere-differentiable functions
- Proving the Open Mapping Theorem

---

## Duality and Separation Arguments

### Using Hahn-Banach for Existence
**Goal:** Show that some object x is in a set S (e.g., closure of a subspace).

**Strategy (contrapositive):** If x ∉ S̄, then Hahn-Banach separation gives f ∈ X* with f(x) > sup_{s∈S} f(s). Show this leads to a contradiction.

### Testing Properties via Functionals
**Principle:** x = 0 in a normed space ⟺ f(x) = 0 for all f ∈ X*.

**Useful for:**
- Showing two elements are equal: show f(x) = f(y) for all f ∈ X*
- Showing a set is dense: show that f vanishing on the set implies f = 0
- Showing weak convergence: check against all functionals

### Annihilator Calculations
For M ⊂ X, the annihilator M⊥ = { f ∈ X* : f(x) = 0 ∀x ∈ M }.

**Key identities:**
- (M⊥)⊥ = M̄ (closure in the norm topology)
- (M̄)⊥ = M⊥
- X*/M⊥ ≅ M* (for closed subspaces M)

---

## Diagonal Arguments

### Cantor's Diagonal Argument (Uncountability)
The classic: to show a set is uncountable, assume a listing and construct an element not in the list by differing in the nth position from the nth listed element.

### Applied in Analysis
- Proving ℓ∞ is not separable
- Constructing non-measurable sets
- The diagonal subsequence trick (see Compactness section)
- Proving the Banach-Alaoglu theorem (product topology argument)

---

## Fixed Point Theorems

### Banach Fixed Point Theorem (Contraction Mapping)
If (X, d) is a complete metric space and T: X → X satisfies d(Tx, Ty) ≤ c · d(x, y) for some c < 1, then T has a unique fixed point.

**Applications:** Existence/uniqueness for ODEs (Picard-Lindelöf), implicit function theorem, iterative methods.

### Schauder Fixed Point Theorem
If K is a nonempty convex compact subset of a Banach space and T: K → K is continuous, then T has a fixed point.

**Application:** Existence theorems for PDEs, integral equations.

### Brouwer Fixed Point Theorem
Every continuous map from a closed ball in ℝⁿ to itself has a fixed point.

---

## Counterexample Construction Strategies

### For Sequences and Functions
- **Pointwise but not uniform convergence:** fₙ(x) = xⁿ on [0,1]
- **Continuous but not differentiable:** |x| at 0, Weierstrass function (everywhere)
- **Convergent in Lp but not pointwise:** sliding bumps (moving indicator functions)
- **Pointwise convergent but not in Lp:** fₙ = n · χ_{[0,1/n]}
- **Bounded + closed but not compact (infinite dim):** standard basis in ℓ², unit ball in any infinite-dim space

### For Operators
- **Bounded but not compact:** identity on infinite-dim space
- **Compact with non-closed range:** any compact operator on infinite-dim space
- **Injective but not bounded below:** consider diagonal operators with eigenvalues → 0

### For Spaces
- **Complete but not compact:** ℝ with usual metric
- **Not reflexive:** ℓ¹, c₀, L¹, C[0,1]
- **Separable Banach space without Schauder basis:** Enflo's example
- **Non-metrizable weak topology:** any non-separable Banach space's unit ball in weak topology

### Building Blocks for Counterexamples
- **Indicator functions** χ_E: discontinuous, useful for measure theory
- **Bump functions** with shrinking/moving support: for convergence counterexamples
- **Cantor set and Cantor function:** measure zero but uncountable, continuous but singular
- **Rational/irrational indicators:** Dirichlet function for Riemann vs Lebesgue
- **Enumeration of rationals:** useful for constructing dense/everywhere-discontinuous examples

---

## Common Proof Patterns

### The "2ε" or "ε/2" Trick
Split the problem into two pieces and bound each by ε/2 (or ε/3 for three pieces). Very common when proving limits using triangle inequality.

### The "Choose a Good Subsequence" Strategy
When direct estimation fails, extract a subsequence where things are better behaved:
1. Choose subsequence with ‖xₙₖ₊₁ - xₙₖ‖ < 2⁻ᵏ
2. The telescoping series converges absolutely
3. Completeness gives a limit
4. Show the original sequence converges to the same limit

### The "Bootstrapping" Strategy
Prove a weak result first, then use it to prove a stronger result:
- Show T maps bounded sets to bounded sets (weak compactness)
- Use this to show T is actually compact
- Use compactness to get spectral decomposition

### The "Soft vs. Hard Analysis" Distinction
- **Soft analysis:** Abstract, using general principles (Hahn-Banach, Baire category, compactness). Gives existence without explicit construction.
- **Hard analysis:** Explicit estimates, inequalities, computations. Gives quantitative bounds.

**Often the most elegant proofs combine both:** use soft analysis for structure, hard analysis for estimates.

### Checking Your Work
After writing a proof, verify:
1. Every hypothesis of every cited theorem is satisfied
2. All quantifiers are in the correct order
3. No step requires a stronger hypothesis than given
4. The conclusion matches what was claimed
5. Edge cases are handled (empty sets, zero elements, n=1)
6. If the result feels too strong, try to construct a counterexample — if you can't, your proof is more likely correct
