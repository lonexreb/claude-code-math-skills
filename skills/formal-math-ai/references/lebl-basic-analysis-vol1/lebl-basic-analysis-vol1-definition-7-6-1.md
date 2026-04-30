Definition 7.6.1

**Definition 7.6.1.** Let ( _𝑋, 𝑑𝑋_ ) and ( _𝑌, 𝑑𝑌_ ) be metric spaces. A map _𝜑_ : _𝑋_ → _𝑌_ is a _contraction_ (or a contractive map) if it is a _𝑘_ -Lipschitz map for some _𝑘 <_ 1, i.e. if there exists a _𝑘 <_ 1 such that

**==> picture [246 x 15] intentionally omitted <==**

Given a map _𝜑_ : _𝑋_ → _𝑋_ , a point _𝑥_ ∈ _𝑋_ is called a _fixed point_ if _𝜑_ ( _𝑥_ ) = _𝑥_ .

**Theorem 7.6.2** (Contraction mapping principle or Banach fixed point theorem ) **.** _Let_ ( _𝑋, 𝑑_ ) _be a nonempty complete metric space and 𝜑_ : _𝑋_ → _𝑋 a contraction. Then 𝜑 has a unique fixed point._

The words _complete_ and _contraction_ are necessary. See .

_Proof._ Pick _𝑥_ 0 ∈ _𝑋_ . Define a sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[by] _[ 𝑥][𝑛]_[+][1][�] _[𝜑]_[(] _[𝑥][𝑛]_[)][.][Then]

**==> picture [244 x 15] intentionally omitted <==**

Repeating _𝑛_ times, we get _𝑑_ ( _𝑥𝑛_ +1 _, 𝑥𝑛_ ) ≤ _𝑘[𝑛] 𝑑_ ( _𝑥_ 1 _, 𝑥_ 0). For _𝑚 > 𝑛_ ,

**==> picture [254 x 164] intentionally omitted <==**

In particular, the sequence is Cauchy (why?). Since _𝑋_ is complete, we let _𝑥_ � lim _𝑛_ →∞ _𝑥𝑛_ , and we claim that _𝑥_ is our unique fixed point.

> ‗Named after the Polish mathematician (1892–1945) who first stated the theorem in 1922.

_7.6. FIXED POINT THEOREM AND PICARD’S THEOREM AGAIN_

297

Fixed point? The function _𝜑_ is a contraction, so it is Lipschitz continuous:

**==> picture [254 x 24] intentionally omitted <==**

Unique? Let _𝑥_ and _𝑦_ be fixed points.

**==> picture [182 x 15] intentionally omitted <==**

As _𝑘 <_ 1, the inequality means that _𝑑_ ( _𝑥, 𝑦_ ) = 0, and hence _𝑥_ = _𝑦_ . The theorem is proved. □

The proof is constructive. Not only do we know a unique fixed point exists, we know how to find it. Start with any point _𝑥_ 0 ∈ _𝑋_ , then iterate _𝜑_ ( _𝑥_ 0), _𝜑_ ( _𝜑_ ( _𝑥_ 0)), _𝜑_ ( _𝜑_ ( _𝜑_ ( _𝑥_ 0))), etc. to find better and better approximations. We can even find how far away from the fixed point we are, see the exercises. The idea of the proof is therefore useful in real-world applications.

## **7.6.2 Picard’s theorem**

We start with the metric space where we will apply the fixed point theorem: the space _𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] of , the space of continuous functions _𝑓_ : [ _𝑎, 𝑏_ ] → ℝ with the metric

**==> picture [228 x 26] intentionally omitted <==**

Convergence in this metric is convergence in uniform norm, or in other words, uniform convergence. Therefore, _𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] is a complete metric space, see . Consider now the ordinary differential equation

**==> picture [69 x 27] intentionally omitted <==**

Given some _𝑥_ 0 _, 𝑦_ 0, we desire a function _𝑦_ = _𝑓_ ( _𝑥_ ) such that _𝑓_ ( _𝑥_ 0) = _𝑦_ 0 and such that

**==> picture [95 x 15] intentionally omitted <==**

To avoid having to come up with many names, we often simply write _𝑦_[′] = _𝐹_ ( _𝑥, 𝑦_ ) for the equation and _𝑦_ ( _𝑥_ ) for the solution.

The simplest example is the equation _𝑦_[′] = _𝑦_ , _𝑦_ (0) = 1. The solution is the exponential _𝑦_ ( _𝑥_ ) = _𝑒[𝑥]_ . A somewhat more complicated example is _𝑦_[′] = −2 _𝑥𝑦_ , _𝑦_ (0) = 1, whose solution is the Gaussian _𝑦_ ( _𝑥_ ) = _𝑒_[−] _[𝑥]_[2] .

A subtle issue is how long does the solution exist. Consider the equation _𝑦_[′] = _𝑦_[2] , 1 _𝑦_ (0) = 1. Then _𝑦_ ( _𝑥_ ) = 1− _𝑥_[is a solution.][While] _[𝐹]_[is a reasonably “nice” function and in] particular it exists for all _𝑥_ and _𝑦_ , the solution “blows up” at _𝑥_ = 1. For more examples related to Picard’s theorem, see .

_CHAPTER 7. METRIC SPACES_

298

We will look for the solution in _𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] , which may feel strange at first as we are searching for a differentiable function. The explanation is that we consider the corresponding integral equation

**==> picture [148 x 31] intentionally omitted <==**

To solve this integral equation, we only need a continuous function, so in some sense our task should be easier—we have more candidate functions to try. This way of thinking is quite typical when solving differential equations.

**Theorem 7.6.3** (Picard’s theorem on existence and uniqueness) **.** _Let 𝐼, 𝐽_ ⊂ ℝ _be closed and bounded intervals, let 𝐼_[◦] _and 𝐽_[◦] _be their interiors, and let_ ( _𝑥_ 0 _, 𝑦_ 0) ∈ _𝐼_[◦] × _𝐽_[◦] _. Suppose 𝐹_ : _𝐼_ × _𝐽_ → ℝ _is continuous and Lipschitz in the second variable, that is, there exists an 𝐿_ ∈ ℝ _such that_

**==> picture [276 x 16] intentionally omitted <==**

_Then there exists an ℎ >_ 0 _such that_ [ _𝑥_ 0 − _ℎ, 𝑥_ 0 + _ℎ_ ] ⊂ _𝐼 and a unique differentiable function 𝑓_ : [ _𝑥_ 0 − _ℎ, 𝑥_ 0 + _ℎ_ ] → _𝐽_ ⊂ ℝ _such that_

**==> picture [214 x 15] intentionally omitted <==**

_Proof._ Without loss of generality, assume _𝑥_ 0 = 0 (exercise). As _𝐼_ × _𝐽_ is compact and _𝐹_ is continuous, _𝐹_ is bounded. So find an _𝑀 >_ 0 such that �� _𝐹_ ( _𝑥, 𝑦_ )�� ≤ _𝑀_ for all ( _𝑥, 𝑦_ ) ∈ _𝐼_ × _𝐽_ . Pick _𝛼>_ 0 such that [− _𝛼, 𝛼_ ] ⊂ _𝐼_ and [ _𝑦_ 0 − _𝛼, 𝑦_ 0 + _𝛼_ ] ⊂ _𝐽_ . Let

**==> picture [122 x 24] intentionally omitted <==**

Note [− _ℎ, ℎ_ ] ⊂ _𝐼_ . Let

**==> picture [219 x 16] intentionally omitted <==**

That is, _𝑌_ is the set of continuous functions on [− _ℎ, ℎ_ ] with values in _𝐽_ , in other words, exactly those functions where _𝐹_[�] _𝑥, 𝑓_ ( _𝑥_ )[�] makes sense. It is left as an exercise to show that _𝑌_ is a closed subset of _𝐶_[�] [− _ℎ, ℎ_ ] _,_ ℝ[�] (because _𝐽_ is closed). The space _𝐶_[�] [− _ℎ, ℎ_ ] _,_ ℝ[�] is complete, and a closed subset of a complete metric space is a complete metric space with the subspace metric, see . So _𝑌_ with the subspace metric is a complete metric space. We will write _𝑑_ ( _𝑓, 𝑔_ ) = ∥ _𝑓_ − _𝑔_ ∥[− _ℎ,ℎ_ ] for this metric. Define a mapping _𝑇_ : _𝑌_ → _𝐶_[�] [− _ℎ, ℎ_ ] _,_ ℝ[�] by

**==> picture [170 x 30] intentionally omitted <==**

It is an exercise to check that _𝑇_ is well-defined, and that for _𝑓_ ∈ _𝑌_ , _𝑇_ ( _𝑓_ ) really is in _𝐶_[�] [− _ℎ, ℎ_ ] _,_ ℝ[�] . Let _𝑓_ ∈ _𝑌_ and | _𝑥_ | ≤ _ℎ_ . As _𝐹_ is bounded by _𝑀_ , we have

**==> picture [234 x 61] intentionally omitted <==**

_7.6. FIXED POINT THEOREM AND PICARD’S THEOREM AGAIN_

299

So _𝑇_ ( _𝑓_ )[�] [− _ℎ, ℎ_ ][�] ⊂[ _𝑦_ 0 − _𝛼, 𝑦_ 0 + _𝛼_ ] ⊂ _𝐽_ , and _𝑇_ ( _𝑓_ ) ∈ _𝑌_ . In other words, _𝑇_ ( _𝑌_ ) ⊂ _𝑌_ . From now on, we consider _𝑇_ as a mapping of _𝑌_ to _𝑌_ .

We claim _𝑇_ : _𝑌_ → _𝑌_ is a contraction. First, for _𝑥_ ∈[− _ℎ, ℎ_ ] and _𝑓, 𝑔_ ∈ _𝑌_ , we have

**==> picture [276 x 16] intentionally omitted <==**

Therefore,

**==> picture [338 x 60] intentionally omitted <==**

We chose _𝑀 >_ 0 and so _𝐿𝛼_[1][.][Take supremum over] _[ 𝑥]_[∈[−] _[ℎ, ℎ]_[]][ of the left-hand side] _𝑀_ + _𝐿𝛼[<]_ above to obtain _𝑑_[�] _𝑇_ ( _𝑓_ ) _, 𝑇_ ( _𝑔_ )[�] ≤ _𝑀𝐿_ + _𝛼𝐿𝛼[𝑑]_[(] _[𝑓, 𝑔]_[)][, that is,] _[ 𝑇]_[is a contraction.]

The fixed point theorem ( ) gives a unique _𝑓_ ∈ _𝑌_ such that _𝑇_ ( _𝑓_ ) = _𝑓_ . In other words,

**==> picture [148 x 30] intentionally omitted <==**

Clearly, _𝑓_ (0) = _𝑦_ 0. By the fundamental theorem of calculus ( ), _𝑓_ is differentiable and its derivative is _𝐹_[�] _𝑥, 𝑓_ ( _𝑥_ )[�] . Differentiable functions are continuous, so _𝑓_ is the unique differentiable _𝑓_ : [− _ℎ, ℎ_ ] → _𝐽_ such that _𝑓_[′] ( _𝑥_ ) = _𝐹_[�] _𝑥, 𝑓_ ( _𝑥_ )[�] and _𝑓_ (0) = _𝑦_ 0. □

## **7.6.3 Exercises**

For more exercises related to Picard’s theorem see .

_**Exercise**_ **7.6.1** _**:** Let 𝐽 be a closed and bounded interval and 𝑌_ � � _𝑓_ ∈ _𝐶_[�] [− _ℎ, ℎ_ ] _,_ ℝ[�] : _𝑓_[�] [− _ℎ, ℎ_ ][�] ⊂ _𝐽_ � _. Show that 𝑌_ ⊂ _𝐶_[�] [− _ℎ, ℎ_ ] _,_ ℝ[�] _is closed. Hint: 𝐽 is closed._

_**Exercise**_ **7.6.2** _**:** In the proof of Picard’s theorem, show that if 𝑓_ : [− _ℎ, ℎ_ ] → _𝐽 is continuous, then 𝐹_[�] _𝑡, 𝑓_ ( _𝑡_ )[�] _is continuous on_ [− _ℎ, ℎ_ ] _as a function of 𝑡. Use this to show that_

**==> picture [151 x 28] intentionally omitted <==**

_is well-defined and that 𝑇_ ( _𝑓_ ) ∈ _𝐶_[�] [− _ℎ, ℎ_ ] _,_ ℝ[�] _._

_**Exercise**_ **7.6.3** _**:** Prove that in the proof of Picard’s theorem, the statement “Without loss of generality assume 𝑥_ 0 = 0 _” is justified. That is, prove that if we know the theorem with 𝑥_ 0 = 0 _, the theorem is true as stated._

_**Exercise**_ **7.6.4** _**:** Let 𝐹_ : ℝ → ℝ _be defined by 𝐹_ ( _𝑥_ ) � _𝑘𝑥_ + _𝑏 where_ 0 _< 𝑘 <_ 1 _, 𝑏_ ∈ ℝ _._

_a) Show that 𝐹 is a contraction._

_b) Find the fixed point and show directly that it is unique._

_CHAPTER 7. METRIC SPACES_

300

_**Exercise**_ **7.6.5** _**:** Let 𝑓_ : [0 _,_[1] /4] →[0 _,_[1] /4] _be defined by 𝑓_ ( _𝑥_ ) � _𝑥_[2] _._

_a) Show that 𝑓 is a contraction, and find the best (smallest) 𝑘 from the definition that works._

- _b) Find the fixed point and show directly that it is unique._

## _**Exercise**_ **7.6.6** _**:**_

- _a) Find an example of a contraction 𝑓_ : _𝑋_ → _𝑋 of a non-complete metric space 𝑋 with no fixed point._

- _b) Find a 1-Lipschitz map 𝑓_ : _𝑋_ → _𝑋 of a complete metric space 𝑋 with no fixed point._

_**Exercise**_ **7.6.7** _**:** Consider 𝑦_[′] = _𝑦_[2] _, 𝑦_ (0) = 1 _. Use the iteration scheme from the proof of the contraction mapping principle. Start with 𝑓_ 0( _𝑥_ ) = 1 _. Find a few iterates (at least up to 𝑓_ 2 _). Prove that the pointwise limit of 𝑓𝑛 is_ 1−1 _𝑥[, that is, for every][ 𝑥][with]_[ |] _[𝑥]_[|] _[ <][ℎ][for some][ℎ][>]_[ 0] _[, prove that] 𝑛_[lim] →∞ _[𝑓][𝑛]_[(] _[𝑥]_[)][ =] 1−1 _𝑥[.]_

_**Exercise**_ **7.6.8** _**:** Suppose 𝑓_ : _𝑋_ → _𝑋 is a contraction for 𝑘 <_ 1 _. Suppose you use the iteration procedure with 𝑥𝑛_ +1 � _𝑓_ ( _𝑥𝑛_ ) _as in the proof of the fixed point theorem. Suppose 𝑥 is the fixed point of 𝑓 ._

_a) Show that 𝑑_ ( _𝑥, 𝑥𝑛_ ) ≤ _𝑘[𝑛] 𝑑_ ( _𝑥_ 1 _, 𝑥_ 0) 1−[1] _𝑘[for all][ 𝑛]_[∈][ℕ] _[.]_

- _b) Suppose 𝑑_ ( _𝑦_ 1 _, 𝑦_ 2) ≤ 16 _for all 𝑦_ 1 _, 𝑦_ 2 ∈ _𝑋, and 𝑘_ =[1] /2 _. Find an 𝑁 such that starting at any given point 𝑥_ 0 ∈ _𝑋, 𝑑_ ( _𝑥, 𝑥𝑛_ ) ≤ 2[−][16] _for all 𝑛_ ≥ _𝑁._

_**Exercise**_ **7.6.9** _**:** Let 𝑓_ ( _𝑥_ ) � _𝑥_ − _[𝑥]_ 2[2][−] _𝑥_[2] _(you may recognize Newton’s method for_ √2 _)._

- _a) Prove 𝑓_[�] [1 _,_ ∞)[�] ⊂[1 _,_ ∞) _._

- _b) Prove that 𝑓_ : [1 _,_ ∞) →[1 _,_ ∞) _is a contraction._

- _c) Show that the fixed point theorem applies, find the unique 𝑥_ ≥ 1 _such that 𝑓_ ( _𝑥_ ) = _𝑥, and show that 𝑥_ = √2 _. Note: In particular, the technique from the proof of the theorem can be used to approximate_ √2 _._

_**Exercise**_ **7.6.10** _**:** Suppose 𝑓_ : _𝑋_ → _𝑋 is a contraction, and_ ( _𝑋, 𝑑_ ) _is a metric space with the discrete metric, that is, 𝑑_ ( _𝑥, 𝑦_ ) = 1 _whenever 𝑥_ ≠ _𝑦. Show that 𝑓 is constant, that is, there exists a 𝑐_ ∈ _𝑋 such that 𝑓_ ( _𝑥_ ) = _𝑐 for all 𝑥_ ∈ _𝑋._

_**Exercise**_ **7.6.11** _**:** Suppose_ ( _𝑋, 𝑑_ ) _is a nonempty complete metric space, 𝑓_ : _𝑋_ → _𝑋 is a mapping, and denote by 𝑓[𝑛] the 𝑛th iterate of 𝑓 . Suppose for every 𝑛 there exists a 𝑘𝑛 >_ 0 _such that 𝑑_[�] _𝑓[𝑛]_ ( _𝑥_ ) _, 𝑓[𝑛]_ ( _𝑦_ )[�] ≤ _𝑘𝑛 𝑑_ ( _𝑥, 𝑦_ ) _for all 𝑥, 𝑦_ ∈ _𝑋, where_[�][∞] _𝑛_ =1 _[𝑘][𝑛][<]_[∞] _[.][Prove that][𝑓][has a unique fixed point in][ 𝑋][.]_

## **Further Reading**

- [BS] Robert G. Bartle and Donald R. Sherbert, _Introduction to Real Analysis_ , 3rd ed., John Wiley & Sons Inc., New York, 2000.

- [DW] John P. D’Angelo and Douglas B. West, _Mathematical Thinking: Problem-Solving and Proofs_ , 2nd ed., Prentice Hall, 1999.

- [F] Joseph E. Fields, _A Gentle Introduction to the Art of Mathematics_ . Available at .

- [H] Richard Hammack, _Book of Proof_ . Available at .

- [R1] Maxwell Rosenlicht, _Introduction to Analysis_ , Dover Publications Inc., New York, 1986. Reprint of the 1968 edition.

- [R2] Walter Rudin, _Principles of Mathematical Analysis_ , 3rd ed., McGraw-Hill Book Co., New York, 1976. International Series in Pure and Applied Mathematics.

- [T] William F. Trench, _Introduction to Real Analysis_ , Pearson Education, 2003. .

_FURTHER READING_

302

## **Index**

Abel’s theorem, absolute convergence, absolute maximum, , absolute minimum, , absolute value, achieves absolute maximum, achieves absolute minimum, additive property of the integral, algebraic geometry, algebraic number, analytic function, Archimedean property, arithmetic-geometric mean inequality, axiom, ,

ball, Banach fixed point theorem, base of the natural logarithm, basis statement, , Bernoulli’s inequality, bĳection, bĳective, binary relation, bisection method, Bolzano’s intermediate value theorem,

Bolzano’s theorem, Bolzano–Weierstrass theorem, , boundary, bounded above, sequence, bounded below, sequence,

bounded function, , bounded interval, bounded sequence, , bounded set, , bounded variation,

Cantor diagonalization, Cantor’s theorem, , Cantor–Bernstein–Schröder, cardinality, Cartesian product, Cauchy condensation principle, Cauchy in the uniform norm, Cauchy principal value, Cauchy product, Cauchy sequence, , Cauchy series, Cauchy’s mean value theorem, Cauchy–Bunyakovsky–Schwarz inequality, Cauchy–Schwarz inequality, , Cauchy-complete, , Cesàro summability, chain rule, change of variables theorem, clopen, closed ball, closed interval, closed set, closure, cluster point, , , in a metric space, codomain,

304

_INDEX_

compact, comparison test for improper integrals, comparison test for series, complement, complement relative to, complete, , completeness property, complex conjugate, complex modulus, complex numbers, composition of functions, conditional convergence, connected, constant sequence, continuous at _𝑐_ , , continuous function, in a metric space, continuous function of two variables, continuously differentiable, contraction, contraction mapping principle, convergent improper integral, power series, sequence, sequence in a metric space, series, converges function, , function in a metric space, converges absolutely, converges conditionally, converges in uniform norm, converges pointwise, converges to infinity, converges uniformly, converges uniformly on compact subsets, convex, , convolution, countable,

countably infinite, critical point,

Darboux integral, Darboux sum, Darboux’s theorem, decimal digit, decimal representation, decreasing, , Dedekind completeness property, Dedekind cut, DeMorgan’s theorem, dense, density of rational numbers, derivative, diagonalization, diameter, difference quotient, differentiable, continuously, infinitely, , _𝑛_ times, differential equation, digit, Dini’s theorem, direct image, Dirichlet function, , , , , disconnected, discontinuity, discontinuous, discrete metric, disjoint, distance function, divergent improper integral, power series, sequence, sequence in a metric space, series, diverges, function in a metric space, diverges to infinity, , diverges to minus infinity,

_INDEX_

305

domain,

element, elementary step function, empty set, equal, equivalence class, equivalence relation, euclidean space, Euler’s number, Euler–Mascheroni constant, even function, existence and uniqueness theorem, , exponential, , extended real numbers, extreme value theorem, field, finite, finitely many discontinuities, first derivative, first derivative test, first order ordinary differential equation, fixed point, fixed point theorem, Fourier sine and cosine transforms, Fubini for sums, function, bounded, continuous, , differentiable, Lipschitz, , fundamental theorem of calculus, geometric series, , graph, great circle distance, greatest lower bound,

half-open interval, harmonic series, Hausdorff metric,

Heine–Borel theorem, identity of indiscernibles, image, improper integrals, increasing, , induction, induction hypothesis, induction step, , infimum, infinite, infinite limit of a function, of a sequence, infinitely differentiable, , infinity norm, initial condition, injection, injective, integers, integral test for series, integration by parts, interior, intermediate value theorem, intersection, interval, inverse function, inverse function theorem, inverse image, irrational, joint limit, L’Hôpital’s rule, , L’Hospital’s rule, , _𝐿_[1] -convergence, _𝐿_[1] -norm, Lagrange form, Laplace transform, least element, least upper bound, least-upper-bound property, Lebesgue covering lemma,

_INDEX_

306

Lebesgue number, Leibniz rule, liminf, , limit infinite, , of a function, of a function at infinity, of a function in a metric space, of a sequence in a metric space, limit comparison test, limit inferior, , limit superior, , limsup, , linear first order differential equations, linearity of series, linearity of the derivative, linearity of the integral, Lipschitz continuous, in a metric space, logarithm, , logarithm base _𝑏_ , lower bound, lower Darboux integral, lower Darboux sum, map, mapping, maximum, absolute, relative, strict relative, maximum-minimum theorem, mean value theorem, mean value theorem for integrals, member, Mertens’ theorem, metric, metric space, minimum, absolute, relative, strict relative,

minimum-maximum theorem, modulus, monic polynomial, , monotone convergence theorem, monotone decreasing sequence, monotone function, monotone increasing sequence, monotone sequence, monotonic sequence, monotonicity of the integral, _𝑛_ times differentiable, naïve set theory, natural logarithm, natural numbers, negative, neighborhood, nondecreasing, nonincreasing, nonnegative, nonnegativity of a metric, nonpositive, _𝑛_ th derivative, _𝑛_ th derivative test, _𝑛_ th order Taylor polynomial, odd function, one-sided limit, one-to-one, onto, open ball, open cover, open interval, open neighborhood, open set, ordered field, ordered set, ordinary differential equation,

_𝑝_ -series, _𝑝_ -test, _𝑝_ -test for integrals, partial sums,

_INDEX_

307

partition, Picard iterate, Picard iteration, Picard’s theorem, , pointwise convergence, polynomial, popcorn function, , positive, power series, power set, principle of induction, principle of strong induction, product rule, proper, proper subset, pseudometric space, quotient rule, radius of convergence, range, range of a sequence, ratio test for sequences, ratio test for series, rational functions, rational numbers, real numbers, rearrangement of a series, refinement of a partition, reflexive relation, relation, relative maximum, relative minimum, relatively compact, remainder term in Taylor’s formula, removable discontinuity, removable singularity, restriction, reverse triangle inequality, Riemann integrable, Riemann integral, Riemann–Lebesgue Lemma, Rolle’s theorem,

root test,

secant line, , second derivative, second derivative test, sequence, , sequentially compact, series, set, set building notation, set theory, set-theoretic difference, set-theoretic function, sinc function, slope field, sphere, squeeze lemma, standard metric on ℝ _[𝑛]_ , standard metric on ℝ, step function, strict relative maximum, strict relative minimum, strictly decreasing, , strictly increasing, , strictly monotone function, strong induction, subadditive, subcover, subsequence, , subset, subspace, subspace metric, subspace topology, sup norm, supremum, surjection, surjective, symmetric difference, symmetric relation, symmetry of a metric, tail of a sequence, tail of a series,

_INDEX_

308

Taylor polynomial, Taylor series, Taylor’s theorem, Thomae function, , Tonelli for sums, topology, totally bounded, totally disconnected, transitive relation, triangle inequality, , trichotomy,

unbounded closed intervals, unbounded interval, unbounded open intervals, uncountable, uniform convergence, uniform convergence on compact subsets,

uniform norm, uniform norm convergence, uniformly Cauchy, uniformly continuous, in a metric space, union, unit sphere, universe, upper bound, upper Darboux integral, upper Darboux sum, Venn diagram, weak solution, well ordering property, zero set,

## **List of Notation**

|**Notation**|**Description**|**Page**|
|---|---|---|
|∅|the empty set|8|
|{1_,_2_,_3}|set with the given elements|8|
|_𝐴_�_𝐵_|defne_𝐴_to equal_𝐵_|8|
|_𝑥_∈_𝑆_|_𝑥_is an element of_𝑆_|8|
|_𝑥_∉_𝑆_|_𝑥_is not an element of_𝑆_|8|
|_𝐴_⊂_𝐵_|_𝐴_is a subset of_𝐵_|8|
|_𝐴_=_𝐵_|_𝐴_and_𝐵_are equal|9|
|_𝐴_⊊_𝐵_|_𝐴_is a proper subset of_𝐵_|9|
|{_𝑥_∈_𝑆_:_𝑃_(_𝑥_)}|set building notation|9|
|ℕ|the natural numbers: 1_,_2_,_3_, . . ._|9|
|ℤ|the integers: _. . . ,_−2_,_−1_,_0_,_1_,_2_, . . ._|9|
|ℚ|the rational numbers|9|
|ℝ|the real numbers|9|
|_𝐴_∪_𝐵_|union of_𝐴_and_𝐵_|10|
|_𝐴_∩_𝐵_|intersection of_𝐴_and_𝐵_|10|
|_𝐴_\_𝐵_|set minus, elements of_𝐴_not in_𝐵_|10|
|_𝐵𝑐_|set complement, elements not in_𝐵_|10|
|∞|||
|�<br>_𝑛_=1<br>_𝐴𝑛_|union of all_𝐴𝑛_for all_𝑛_∈ℕ|11|
|∞|||
|�<br>_𝑛_=1<br>_𝐴𝑛_|intersection of all_𝐴𝑛_for all_𝑛_∈ℕ|11|
|�<br>_𝜆_∈_𝐼_<br>_𝐴𝜆_|union of all_𝐴𝜆_for all_𝜆_∈_𝐼_|12|
|�<br>_𝜆_∈_𝐼_<br>_𝐴𝜆_|intersection of all_𝐴𝜆_for all_𝜆_∈_𝐼_|12|


_LIST OF NOTATION_

310

|**Notation**|**Description**|**Page**|**Page**|**Page**|
|---|---|---|---|---|
|_𝑓_: _𝐴_→_𝐵_|function with domain_𝐴_and codomain_𝐵_|13|||
|_𝐴_×_𝐵_|Cartesian product of_𝐴_and_𝐵_|14|||
|_𝑓_(_𝐴_)|direct image of_𝐴_by _𝑓_|14|||
|_𝑓_−1(_𝐴_)<br>_𝑓_−1|inverse image of_𝐴_by _𝑓_<br>inverse function|14<br> 16|||
|_𝑓_◦_𝑔_|composition of functions|16|||
|[_𝑎_]|equivalence class of_𝑎_|17|||
||_𝐴_||cardinality of a set_𝐴_|17|||
|_P_(_𝑃_)|power set of_𝐴_|19|||
|_𝑥_= _𝑦_|_𝑥_is equal to_𝑦_|23|||
|_𝑥< 𝑦_|_𝑥_is less than_𝑦_|23|||
|_𝑥_≤_𝑦_|_𝑥_is less than or equal to_𝑦_|23|||
|_𝑥> 𝑦_|_𝑥_is greater than_𝑦_|23|||
|_𝑥_≥_𝑦_|_𝑥_is greater than or equal to_𝑦_|23|||
|sup _𝐸_|supremum of_𝐸_|24|||
|inf _𝐸_|infmum of_𝐸_|24|||
|ℂ|the complex numbers|27|||
|ℝ∗|the extended real numbers|33|||
|∞|infnity|33|||
|max _𝐸_|maximum of_𝐸_|34|||
|min _𝐸_|minimum of_𝐸_|34|||
||_𝑥_||absolute value|36|||
|sup<br>_𝑓_(_𝑥_)|supremum of _𝑓_(_𝐷_)|38|||
|_𝑥_∈_𝐷_|||||
|inf<br>_𝑥_∈_𝐷𝑓_(_𝑥_)|infmum of _𝑓_(_𝐷_)|38|||
|(_𝑎, 𝑏_)|open bounded interval|41|||
|[_𝑎, 𝑏_]|closed bounded interval|41|||
|(_𝑎, 𝑏_],[_𝑎, 𝑏_)|half-open bounded interval|41|||
|(_𝑎,_∞),(−∞_, 𝑏_)|open unbounded interval|41|||
|[_𝑎,_∞),(−∞_, 𝑏_]|closed unbounded interval|41|||
|{_𝑥𝑛_}∞<br>_𝑛_=1|sequence|51|,|274|


_LIST OF NOTATION_

311

|**Notation**|||||**Description**|**Page**|**Page**|**Page**|
|---|---|---|---|---|---|---|---|---|
|lim<br>_𝑛_→∞_𝑥𝑛_|||||limit of a sequence|52<br>,|274||
|{_𝑥𝑛𝑖_}∞<br>_𝑖_=1|||||subsequence|58<br>,|274||
|lim sup<br>_𝑥𝑛_|||||limit superior|73<br>,|80||
|_𝑛_→∞|||||||||
|lim inf<br>_𝑛_→∞_𝑥𝑛_|||||limit inferior|73<br>,|80||
|∞|||||||||
|�<br>_𝑛_=1<br>_𝑎𝑛_|||||series|87|||
|_𝑘_|||||||||
|�<br>_𝑛_=1<br>_𝑎𝑛_|||||sum_𝑎_1+_𝑎_2+ · · · +_𝑎𝑘_|87|||
|_𝑓_(_𝑥_) →_𝐿_as_𝑥_→_𝑐_|||||_𝑓_(_𝑥_)converges to_𝐿_as_𝑥_goes to_𝑐_|114|||
|lim<br>_𝑥_→_𝑐𝑓_(_𝑥_)|||||limit of a function|114<br>,||293|
|lim<br>_𝑥_→_𝑐_+ _𝑓_(_𝑥_),||lim<br>_𝑥_→_𝑐_−_𝑓_(_𝑥_)|||one-sided limit of a function|119|||
|lim<br>_𝑥_→∞_𝑓_(_𝑥_), <br>_𝑓_′(_𝑥_), _𝑑𝑓_<br>_𝑑𝑥_,|lim<br>_𝑥_→−∞_𝑓_(_𝑥_)<br> _𝑑_<br>_𝑑𝑥_<br>�<br>_𝑓_(_𝑥_)�||||limit of a function at infnity<br>derivative of _𝑓_|145<br> 155|||
|_𝑓_′′, _𝑓_′′′, _𝑓_′′′′|||||second, third, fourth derivative of _𝑓_|171|||
|_𝑓_(_𝑛_)|||||_𝑛_th derivative of _𝑓_|171|||
|_𝐿_(_𝑃, 𝑓_)|||||lower Darboux sum of _𝑓_over partition_𝑃_|181|||
|_𝑈_(_𝑃, 𝑓_)|||||upper Darboux sum of _𝑓_over partition_𝑃_|181|||
|∫<br>_𝑏_<br>_𝑎_<br>_𝑓_|||||lower Darboux integral|182|||
||||||||||
|∫<br>_𝑏_<br>_𝑎_<br>_𝑓_|||||upper Darboux integral|182|||
|_R_�<br>[_𝑎, 𝑏_]�<br>∫<br>_𝑏_<br>_𝑎_<br>_𝑓_,<br>∫<br>_𝑎_|_𝑏_<br>_𝑓_(_𝑥_)_𝑑𝑥_||||Riemann integrable functions on[_𝑎, 𝑏_]<br>Riemann integral of _𝑓_on[_𝑎, 𝑏_]|185<br> 185|||
|ln(_𝑥_), log(_𝑥_)|||||natural logarithm function|208|||
|exp(_𝑥_),_𝑒𝑥_|||||exponential function|210|||
|_𝑥𝑦_|||||exponentiation of_𝑥>_0 and_𝑦_∈ℝ|211|||
|_𝑒_|||||Euler’s number, base of the natural logarithm|211|||


_LIST OF NOTATION_

312

|**Notation**|**Description**|**Page**|**Page**|**Page**|
|---|---|---|---|---|
|��_𝑓_<br>��<br>_𝑆_|uniform norm of _𝑓_over_𝑆_|230|||
|ℝ_𝑛_|the_𝑛_-dimensional euclidean space|257|||
|_𝐶_(_𝑆,_ℝ)|continuous functions _𝑓_: _𝑆_→ℝ|259|||
|diam(_𝑆_)|diameter of_𝑆_|261|||
|_𝐶_1(_𝑆,_ℝ)|continuously diferentiable functions _𝑓_: _𝑆_→ℝ|263|,|295|
|_𝐵_(_𝑝, 𝛿_),_𝐵𝑋_(_𝑝, 𝛿_)|open ball in a metric space|264|||
|_𝐶_(_𝑝, 𝛿_),_𝐶𝑋_(_𝑝, 𝛿_)|closed ball in a metric space|264|||
|_𝐴_|closure of_𝐴_|269|||
|_𝐴_◦|interior of_𝐴_|270|||
|_𝜕𝐴_|boundary of_𝐴_|270|||