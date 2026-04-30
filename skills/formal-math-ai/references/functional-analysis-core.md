# Functional Analysis Core

## Table of Contents
1. [Bounded Linear Operators](#bounded-linear-operators)
2. [The Hahn-Banach Theorem](#the-hahn-banach-theorem)
3. [The Uniform Boundedness Principle](#the-uniform-boundedness-principle)
4. [The Open Mapping Theorem](#the-open-mapping-theorem)
5. [The Closed Graph Theorem](#the-closed-graph-theorem)
6. [Weak Topologies](#weak-topologies)
7. [Reflexivity and Duality](#reflexivity-and-duality)

---

## Bounded Linear Operators

### Definition
T: X → Y (between normed spaces) is a bounded linear operator if:
- T is linear: T(αx + βy) = αT(x) + βT(y)
- T is bounded: ‖T‖ := sup_{‖x‖≤1} ‖Tx‖ < ∞

### Equivalences
For a linear operator T: X → Y, TFAE:
1. T is bounded
2. T is continuous
3. T is continuous at 0
4. T is Lipschitz continuous
5. T maps bounded sets to bounded sets

**Key point:** For LINEAR operators, continuity and boundedness are equivalent. This is specific to linear operators — it fails for general maps.

### Operator Norm
‖T‖ = sup_{‖x‖≤1} ‖Tx‖ = sup_{‖x‖=1} ‖Tx‖ = sup_{x≠0} ‖Tx‖/‖x‖ = inf{ M : ‖Tx‖ ≤ M‖x‖ for all x }

### Space of Bounded Operators
B(X, Y) = { bounded linear T: X → Y } with operator norm.

**Theorem:** If Y is Banach, then B(X, Y) is Banach. In particular, X* = B(X, 𝔽) is always Banach.

### Dual Space
X* = B(X, 𝔽) = { bounded linear functionals on X }

The dual space is always a Banach space, even when X is not complete.

---

## The Hahn-Banach Theorem

### Analytic Form (Real)
Let X be a real vector space, p: X → ℝ a sublinear functional (p(x+y) ≤ p(x)+p(y), p(αx) = αp(x) for α ≥ 0).
If f is a linear functional on a subspace M ⊂ X with f(x) ≤ p(x) on M, then
there exists a linear functional F on all of X with F = f on M and F(x) ≤ p(x) on X.

### Extension Form (Normed Spaces)
If f is a bounded linear functional on a subspace M of a normed space X with ‖f‖ = C, then
there exists F ∈ X* with F = f on M and ‖F‖ = C.

**The extension preserves the norm exactly.**

### Consequences

**Separation of points:** For every x ≠ 0 in X, there exists f ∈ X* with f(x) = ‖x‖ and ‖f‖ = 1.

**The dual space is rich:** X* separates points of X. This means: if f(x) = f(y) for all f ∈ X*, then x = y.

**Separation of convex sets (geometric form):** If A, B are disjoint convex sets with A open, there exists f ∈ X* and α ∈ ℝ such that Re f(a) < α ≤ Re f(b) for all a ∈ A, b ∈ B.

**Supporting hyperplanes:** At every boundary point of a closed convex set, there exists a supporting hyperplane.

**Canonical embedding:** The map J: X → X** defined by J(x)(f) = f(x) is a linear isometry (not always surjective).

### Common Errors with Hahn-Banach
- Assuming the extension is unique (it's generally NOT — only the norm is preserved)
- Forgetting it requires the real/complex distinction (use the real version + complexification trick for complex spaces)
- Assuming it works for arbitrary functionals without a sublinear majorant

---

## The Uniform Boundedness Principle

### Statement (Banach-Steinhaus Theorem)
Let X be a Banach space, Y a normed space, and {Tα} ⊂ B(X, Y) a family of bounded linear operators.
If sup_α ‖Tα(x)‖ < ∞ for each x ∈ X (pointwise bounded),
then sup_α ‖Tα‖ < ∞ (uniformly bounded).

**Contrapositive:** If sup_α ‖Tα‖ = ∞, then there is a DENSE Gδ set of points x where sup_α ‖Tα(x)‖ = ∞.

### Key Hypothesis
**X must be complete** (Banach). This is essential — the theorem fails for incomplete normed spaces.

The proof uses the Baire Category Theorem.

### Applications

**Convergence of operators:** If Tₙ ∈ B(X,Y) with X Banach and Tₙx → Tx for all x, then:
- sup_n ‖Tₙ‖ < ∞
- T is bounded
- ‖T‖ ≤ lim inf ‖Tₙ‖

**Divergence of Fourier series:** There exist continuous functions whose Fourier series diverges at a point (use UBP with partial sum operators).

**Condensation of singularities:** If a sequence of operators is unbounded, the set of points where pointwise divergence occurs is comeager (residual).

---

## The Open Mapping Theorem

### Statement
If X, Y are Banach spaces and T ∈ B(X, Y) is surjective, then T is an open map (maps open sets to open sets).

### Consequence: Bounded Inverse Theorem
If T: X → Y is a bounded bijective linear operator between Banach spaces, then T⁻¹ is also bounded.

**In other words:** A continuous linear bijection between Banach spaces is automatically a homeomorphism.

### Key Hypotheses
- Both X AND Y must be Banach (complete)
- T must be surjective (onto)
- T must be bounded (continuous)

**What fails without completeness:** Consider the identity map from (X, ‖·‖₁) to (X, ‖·‖₂) where ‖·‖₁ is strictly stronger. This is continuous and bijective but the inverse is not continuous.

### Proof Idea
Uses the Baire Category Theorem: Y = ∪ T(B̄(0,n)), so some T(B̄(0,n)) has nonempty interior, which forces T to be open.

---

## The Closed Graph Theorem

### Statement
Let X, Y be Banach spaces and T: X → Y be linear. If the graph of T,
G(T) = { (x, Tx) : x ∈ X }, is closed in X × Y, then T is bounded.

### When to Use It
The Closed Graph Theorem is often the easiest way to prove an operator is bounded when:
- Direct estimation of ‖Tx‖ is hard
- You can show: if xₙ → x and Txₙ → y, then Tx = y

### Equivalence with Open Mapping Theorem
- Closed Graph ⟹ Open Mapping (and vice versa)
- They are different perspectives on the same underlying fact

### Key Hypothesis
**Both spaces must be complete.** The theorem fails for incomplete normed spaces.

### Closed Range Theorem
For T ∈ B(X, Y) with X, Y Banach:
Range(T) is closed ⟺ Range(T*) is closed ⟺ Range(T) = (ker T*)⊥ ⟺ Range(T*) = (ker T)⊥

(Here T* is the adjoint and the orthogonal complements are in the duality sense.)

---

## Weak Topologies

### Weak Topology on X
The weakest topology making all f ∈ X* continuous.

A net xα →^w x ⟺ f(xα) → f(x) for all f ∈ X*.

**Properties:**
- Weaker than the norm topology (fewer open sets)
- A convex set is weakly closed ⟺ it is norm-closed (Mazur's theorem)
- The closed unit ball is weakly compact ⟺ X is reflexive (Eberlein-Šmulian)

### Weak* Topology on X*
The weakest topology making all evaluation maps J(x): X* → 𝔽 continuous.

A net fα →^{w*} f ⟺ fα(x) → f(x) for all x ∈ X.

**Properties:**
- Weaker than the weak topology on X*
- **Banach-Alaoglu Theorem:** The closed unit ball of X* is weak*-compact
- Weak* is generally NOT metrizable (unless X is separable, in which case the unit ball of X* is weak*-metrizable)

### Banach-Alaoglu Theorem
The closed unit ball B* = { f ∈ X* : ‖f‖ ≤ 1 } is compact in the weak* topology.

**Proof idea:** Embed B* into a product of compact intervals via the map f ↦ (f(x))_{x∈X}, then use Tychonoff's theorem.

**This is one of the most important compactness results in functional analysis.** It replaces Heine-Borel (which fails in infinite dimensions) with a useful substitute.

### Goldstine's Theorem
The closed unit ball of X is weak*-dense in the closed unit ball of X**.

---

## Reflexivity and Duality

### Canonical Embedding
J: X → X** defined by J(x)(f) = f(x) for f ∈ X*.

J is always a linear isometry (Hahn-Banach ensures this).

### Reflexive Space
X is reflexive if J is surjective, i.e., X** = J(X).

**Reflexive spaces:** ℓp for 1 < p < ∞, Lp for 1 < p < ∞, all Hilbert spaces, finite-dimensional spaces.

**Non-reflexive spaces:** ℓ¹, ℓ∞, c₀, L¹, L∞, C[0,1].

### James' Theorem
A Banach space is reflexive ⟺ every bounded linear functional attains its norm on the unit ball.

### Eberlein-Šmulian Theorem
In a Banach space, the following are equivalent for a subset A:
1. A is weakly compact
2. A is weakly sequentially compact
3. A is weakly countably compact

**This is extremely useful** because it lets you work with sequences instead of nets when checking weak compactness.

### Milman-Pettis Theorem
Every uniformly convex Banach space is reflexive.

**Consequence:** Lp for 1 < p < ∞ is reflexive (since Lp is uniformly convex for these p).
