Example 6.2.15

**Example 6.2.15:** The series

**==> picture [39 x 35] intentionally omitted <==**

_𝑥_ converges to (1− _𝑥_ )[2][on][ (−][1] _[,]_[ 1][)][.] Proof: On (−1 _,_ 1),[�][∞] _𝑛_ =0 _[𝑥][𝑛]_[converges to] 1−1 _𝑥_[.][The derivative][ �][∞] _𝑛_ =1 _[𝑛𝑥][𝑛]_[−][1][ then converges] on the same interval to 1[Multiplying by] _[ 𝑥]_[obtains the result.] (1− _𝑥_ )[2][.]

_6.2. INTERCHANGE OF LIMITS_

243

## **6.2.5 Exercises**

_**Exercise**_ **6.2.1** _**:** Find an explicit example of a sequence of differentiable functions on_ [−1 _,_ 1] _that converge uniformly to a function 𝑓 such that 𝑓 is not differentiable. Hint: There are many possibilities, simplest is perhaps to combine_ | _𝑥_ | _and[𝑛]_ 2 _[𝑥]_[2][ +] 2[1] _𝑛[, another is to consider]_ � _𝑥_[2] + ([1] / _𝑛_ )[2] _. Show that these functions are differentiable, converge uniformly, and then show that the limit is not differentiable._

_**Exercise**_ **6.2.2** _**:** Let 𝑓𝑛_ ( _𝑥_ ) � _[𝑥] 𝑛[𝑛][.][Show that]_[ {] _[ 𝑓][𝑛]_[}][∞] _𝑛_ =1 _[converges uniformly to a differentiable function][𝑓][on]_ [0 _,_ 1] _(find 𝑓 ). However, show that 𝑓_[′] (1) ≠ lim _𝑛_[(][1][)] _[.] 𝑛_ →∞ _[𝑓]_[′]

**==> picture [441 x 29] intentionally omitted <==**

**==> picture [431 x 30] intentionally omitted <==**

_**Exercise**_ **6.2.5** _**:** Find an example of a sequence of continuous functions on_ (0 _,_ 1) _that converges pointwise to a continuous function on_ (0 _,_ 1) _, but the convergence is not uniform._

Note: In the previous exercise, (0 _,_ 1) was picked for simplicity. For a more challenging exercise, replace (0 _,_ 1) with [0 _,_ 1].

_**Exercise**_ **6.2.6** _**:** True/False; prove or find a counterexample to the following statement: If_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[is a sequence] of everywhere discontinuous functions on_ [0 _,_ 1] _that converge uniformly to a function 𝑓 , then 𝑓 is everywhere discontinuous._

_**Exercise**_ **6.2.7** _**:** For a continuously differentiable function 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _, define_

**==> picture [132 x 18] intentionally omitted <==**

_Suppose_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[is a sequence of continuously differentiable functions such that for every][ 𝜖>]_[0] _[, there exists] an 𝑀 such that for all 𝑛, 𝑘_ ≥ _𝑀, we have_

**==> picture [76 x 16] intentionally omitted <==**

_Show that_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges uniformly to some continuously differentiable function][𝑓]_[:][[] _[𝑎, 𝑏]_[] →][ℝ] _[.]_

Suppose _𝑓_ : [0 _,_ 1] → ℝ is Riemann integrable. For the following two exercises define the number

**==> picture [108 x 29] intentionally omitted <==**

It is true that �� _𝑓_ �� is integrable whenever _𝑓_ is, see . The number is called the _𝐿_[1] _-norm_ and defines another very common type of convergence called the _𝐿_[1] _-convergence_ . It is, however, a bit more subtle.

_**Exercise**_ **6.2.8** _**:** Suppose_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[is a sequence of Riemann integrable functions on]_[ [][0] _[,]_[ 1][]] _[ that converges] uniformly to_ 0 _. Show that_

**==> picture [74 x 18] intentionally omitted <==**

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

244

_**Exercise**_ **6.2.9** _**:** Find a sequence_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[of Riemann integrable functions on]_[ [][0] _[,]_[ 1][]] _[ converging pointwise] to_ 0 _, but such that_

**==> picture [148 x 18] intentionally omitted <==**

_**Exercise**_ **6.2.10** (Hard) _**:** Prove_ Dini’s theorem _: Let 𝑓𝑛_ : [ _𝑎, 𝑏_ ] → ℝ _be a sequence of continuous functions such that_

0 ≤ _𝑓𝑛_ +1( _𝑥_ ) ≤ _𝑓𝑛_ ( _𝑥_ ) ≤· · · ≤ _𝑓_ 1( _𝑥_ ) _for all 𝑛_ ∈ ℕ _._

_Suppose_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges pointwise to]_[ 0] _[.][Show that]_[ {] _[ 𝑓][𝑛]_[}][∞] _𝑛_ =1 _[converges to zero uniformly.]_

_**Exercise**_ **6.2.11** _**:** Suppose 𝑓𝑛_ : [ _𝑎, 𝑏_ ] → ℝ _is a sequence of continuous functions that converges pointwise to a_ ∞ _continuous 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _. Suppose that for every 𝑥_ ∈[ _𝑎, 𝑏_ ] _, the sequence_ ��� _𝑓𝑛_ ( _𝑥_ ) − _𝑓_ ( _𝑥_ )��� _𝑛_ =1 _[is monotone.] Show that the sequence_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges uniformly.]_

_**Exercise**_ **6.2.12** _**:** Find sequences of Riemann integrable functions 𝑓𝑛_ : [0 _,_ 1] → ℝ _such that_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges] to zero pointwise, and such that_

1 ∞ _a)_ �∫0 _[𝑓][𝑛]_ � _𝑛_ =1 _[increases without bound,]_

1 ∞ _b)_ �∫0 _[𝑓][𝑛]_ � _𝑛_ =1 _[is the sequence]_[ −][1] _[,]_[ 1] _[,]_[ −][1] _[,]_[ 1] _[,]_[ −][1] _[,]_[ 1] _[, . . .][.]_

It is possible to define a _joint limit_ of a double sequence { _𝑥𝑛,𝑚_ }[∞] _𝑛,𝑚_ =1[of real numbers (that is a] function from ℕ × ℕ to ℝ). We say _𝐿_ is the joint limit of { _𝑥𝑛,𝑚_ }[∞] _𝑛,𝑚_ =1[and write]

**==> picture [208 x 21] intentionally omitted <==**

if for every _𝜖>_ 0, there exists an _𝑀_ such that if _𝑛_ ≥ _𝑀_ and _𝑚_ ≥ _𝑀_ , then | _𝑥𝑛,𝑚_ − _𝐿_ | _< 𝜖_ .

_**Exercise**_ **6.2.13** _**:** Suppose the joint limit (see above) of_ { _𝑥𝑛,𝑚_ }[∞] _𝑛,𝑚_ =1 _[is][ 𝐿][, and suppose that for all][ 𝑛][,] 𝑚_[lim] →∞ _[𝑥][𝑛,𝑚] exists, and for all 𝑚,_ lim _[Then show]_[lim][lim] _𝑛_ →∞ _[𝑥][𝑛,𝑚][exists.] 𝑛_ →∞ _𝑚_[lim] →∞ _[𝑥][𝑛,𝑚]_[=] _𝑚_ →∞ _𝑛_[lim] →∞ _[𝑥][𝑛,𝑚]_[=] _[ 𝐿][.]_

(−1) _[𝑛]_[+] _[𝑚]_ _**Exercise**_ **6.2.14** _**:** A joint limit (see above) does not mean the iterated limits exist. Consider 𝑥𝑛,𝑚_ � min{ _𝑛,𝑚_ } _[.] a) Show that for no 𝑛 does_ lim[lim] _[So neither]_[lim] _𝑚_ →∞ _[𝑥][𝑛,𝑚][exist, and for no][ 𝑚][does] 𝑛_ →∞ _[𝑥][𝑛,𝑚][exist.] 𝑛_ →∞ _𝑚_[lim] →∞ _[𝑥][𝑛,𝑚] nor_ lim _𝑚_ →∞ _𝑛_[lim] →∞ _[𝑥][𝑛,𝑚][makes any sense at all.]_

- _b) Show that the joint limit of_ { _𝑥𝑛,𝑚_ }[∞] _𝑛,𝑚_ =1 _[exists and equals 0.]_

_**Exercise**_ **6.2.15** _**:** We say that a sequence of functions 𝑓𝑛_ : ℝ → ℝ converges uniformly on compact subsets _if for every 𝑘_ ∈ ℕ _, the sequence_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges uniformly on]_[ [−] _[𝑘, 𝑘]_[]] _[.]_

- _a) Prove that if 𝑓𝑛_ : ℝ → ℝ _is a sequence of continuous functions converging uniformly on compact subsets, then the limit is continuous._

- _b) Prove that if 𝑓𝑛_ : ℝ → ℝ _is a sequence of functions Riemann integrable on every closed and bounded interval_ [ _𝑎, 𝑏_ ] _, and converging uniformly on compact subsets to an 𝑓_ : ℝ → ℝ _, then for every interval 𝑏 𝑏_

- [ _𝑎, 𝑏_ ] _, we have 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _, and_ ∫ _𝑎[𝑓]_[=] _𝑛_[lim] →∞ ∫ _𝑎[𝑓][𝑛][.]_

_**Exercise**_ **6.2.16** (Challenging) _**:** Find a sequence of continuous functions 𝑓𝑛_ : [0 _,_ 1] → ℝ _that converge to the popcorn function 𝑓_ : [0 _,_ 1] → ℝ _, that is the function such that 𝑓_ ( _[𝑝]_ / _𝑞_ ) �[1] / _𝑞 (if[𝑝]_ / _𝑞 is in lowest terms) and 𝑓_ ( _𝑥_ ) � 0 _if 𝑥 is not rational (note that 𝑓_ (0) = _𝑓_ (1) = 1 _), see . So a pointwise limit of continuous functions can have a dense set of discontinuities. See also the next exercise._

245

## _6.2. INTERCHANGE OF LIMITS_

_**Exercise**_ **6.2.17** (Challenging) _**:** The Dirichlet function 𝑓_ : [0 _,_ 1] → ℝ _, that is the function such that 𝑓_ ( _𝑥_ ) � 1 _if 𝑥_ ∈ ℚ _and 𝑓_ ( _𝑥_ ) � 0 _if 𝑥_ ∉ ℚ _, is not the pointwise limit of continuous functions, although this is difficult to show. Prove, however, that 𝑓 is a pointwise limit of functions that are themselves pointwise limits of continuous functions themselves._

## _**Exercise**_ **6.2.18** _**:**_

- _a) Find a sequence of Lipschitz continuous functions on_ [0 _,_ 1] _whose uniform limit is_[√] _𝑥, which is a non-Lipschitz function._

- _b) On the other hand, show that if 𝑓𝑛_ : _𝑆_ → ℝ _are Lipschitz with a uniform constant 𝐾 (meaning all of them satisfy the definition with the same constant) and_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges pointwise to][𝑓]_[:] _[𝑆]_[→][ℝ] _[, then the] limit 𝑓 is a Lipschitz continuous function with Lipschitz constant 𝐾._

_**Exercise**_ **6.2.19** (requires ) _**:** If_[�][∞] _𝑛_ =0 _[𝑐][𝑛]_[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛][has radius of convergence][ 𝜌][, show that the term by term] integral_[�][∞] _𝑛_ =1 _𝑐𝑛𝑛_ −1[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛][has radius of convergence][ 𝜌][.][Note that we only proved above that the radius of] convergence was at least 𝜌._

_**Exercise**_ **6.2.20** (requires and ) _**:** Suppose 𝑓_ ( _𝑥_ ) �[�][∞] _𝑛_ =0 _[𝑐][𝑛]_[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛][converges in]_[ (] _[𝑎]_[−] _[𝜌][, 𝑎]_[+] _[ 𝜌]_[)] _[.]_

- _a) Suppose that 𝑓_[(] _[𝑘]_[)] ( _𝑎_ ) = 0 _for all 𝑘_ = 0 _,_ 1 _,_ 2 _,_ 3 _, . . .. Prove that 𝑐𝑛_ = 0 _for all 𝑛, or in other words, 𝑓_ ( _𝑥_ ) = 0 _for all 𝑥_ ∈( _𝑎_ − _𝜌, 𝑎_ + _𝜌_ ) _._

- _b) Using part a) prove a version of the so-called “identity theorem for analytic functions”: If there exists an 𝜖>_ 0 _such that 𝑓_ ( _𝑥_ ) = 0 _for all 𝑥_ ∈( _𝑎_ − _𝜖, 𝑎_ + _𝜖_ ) _, then 𝑓_ ( _𝑥_ ) = 0 _for all 𝑥_ ∈( _𝑎_ − _𝜌, 𝑎_ + _𝜌_ ) _._

_**Exercise**_ **6.2.21** _**:** Let 𝑓𝑛_ ( _𝑥_ ) � 1+( _𝑥𝑛𝑥_ )[2] _[.][Notice that][𝑓][𝑛][are differentiable functions.]_

- _a) Show that_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges uniformly to 0.]_

- _b) Show that_ | _𝑓𝑛_[′][(] _[𝑥]_[)| ≤][1] _[ for all][ 𝑥][and all][ 𝑛][.]_

- _c) Show that_ { _𝑓𝑛_[′][}][∞] _𝑛_ =1 _[converges pointwise to a function discontinuous at the origin.]_

- _d) Let_ { _𝑎𝑛_ }[∞] _𝑛_ =1 _[be an enumeration of the rational numbers.][Define]_

**==> picture [125 x 33] intentionally omitted <==**

_Show that_ { _𝑔𝑛_ }[∞] _𝑛_ =1 _[converges uniformly to 0.]_

- _e) Show that_ { _𝑔𝑛_[′][}][∞] _𝑛_ =1 _[converges pointwise to a function][ 𝜓][that is discontinuous at every rational number] and continuous at every irrational number. In particular,_ lim _𝑛_[(] _[𝑥]_[)][ ≠][0] _[ for every rational number][ 𝑥][.] 𝑛_ →∞ _[𝑔]_[′]

_**Exercise**_ **6.2.22** (requires ) _**:** Show that uniform convergence is not enough to pass the limit through improper integrals over infinite intervals. That is, find a sequence of functions 𝑓𝑛_ : ℝ → ℝ _Riemann integrable on every bounded interval, converging uniformly to zero, and such that_ ∫−∞∞ _[𝑓][𝑛]_[=][ 1] _[ for every][ 𝑛][.]_

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

246

## **6.3 Picard’s theorem**

## _Note: 1–2 lectures (can be safely skipped)_

A first semester course in analysis should have a _pièce de résistance_ caliber theorem. We pick a theorem whose proof combines everything we have learned. It is more sophisticated than the fundamental theorem of calculus, the first highlight theorem of this course. The theorem we are talking about is Picard’s theorem on existence and uniqueness of a solution to an ordinary differential equation. Both the statement and the proof are beautiful examples of what one can do with the material we mastered so far. It is also a good example of how analysis is applied, as differential equations are indispensable in science of every stripe.

## **6.3.1 First order ordinary differential equation**

Modern science is described in the language of _differential equations_ . That is, equations involving not only the unknown, but also its derivatives. The simplest nontrivial form of a differential equation is the so-called _first order ordinary differential equation_

**==> picture [64 x 13] intentionally omitted <==**

Generally, we also specify an _initial condition 𝑦_ ( _𝑥_ 0) = _𝑦_ 0. The solution of the equation is a function _𝑦_ ( _𝑥_ ) such that _𝑦_ ( _𝑥_ 0) = _𝑦_ 0 and _𝑦_[′] ( _𝑥_ ) = _𝐹_[�] _𝑥, 𝑦_ ( _𝑥_ )[�] . See for a graphical . representation as a so-called _slope field_

**==> picture [35 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
( 푥 0 , 푦 0)<br>**----- End of picture text -----**<br>


**Figure 6.8:** A _slope field_ giving the slope _𝐹_ ( _𝑥, 𝑦_ ) at each point, in this case _𝐹_ ( _𝑥, 𝑦_ ) = _𝑥_ (1 − _𝑦_ ). A solution is drawn going through the point ( _𝑥_ 0 _, 𝑦_ 0) = (1 _,_ 0 _._ 3), notice how it follows the slopes.

When _𝐹_ involves only the _𝑥_ variable, the solution is given by the fundamental theorem of calculus. On the other hand, when _𝐹_ depends on both _𝑥_ and _𝑦_ , we need far more firepower. It is not always true that a solution exists, and if it does, that it is the unique solution. Picard’s theorem gives us certain sufficient conditions for existence and uniqueness. ‗Named for the French mathematician (1856–1941).

_6.3. PICARD’S THEOREM_

247

## **6.3.2 The theorem**

We need a definition of continuity in two variables. A point in the plane ℝ[2] = ℝ × ℝ is denoted by an ordered pair ( _𝑥, 𝑦_ ). For simplicity, we give the following sequential definition of continuity.