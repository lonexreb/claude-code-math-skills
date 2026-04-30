Example 4.2.12

**Example 4.2.12:** Let _𝑓_ : ℝ → ℝ be the function defined by

**==> picture [162 x 39] intentionally omitted <==**

We claim that _𝑓_ is differentiable everywhere, but _𝑓_[′] : ℝ → ℝ is not continuous at the origin. Furthermore, _𝑓_ has a minimum at 0, but the derivative changes sign infinitely often near the origin. See .

**==> picture [219 x 148] intentionally omitted <==**

**==> picture [219 x 147] intentionally omitted <==**

**Figure 4.7:** A function with a discontinuous derivative. The function _𝑓_ is on the left and _𝑓_[′] is on the right. Notice that _𝑓_ ( _𝑥_ ) ≤ _𝑥_[2] on the left graph.

Proof: It is immediate from the definition that _𝑓_ has an absolute minimum at 0; we know _𝑓_ ( _𝑥_ ) ≥ 0 for all _𝑥_ and _𝑓_ (0) = 0.

For _𝑥_ ≠ 0, _𝑓_ is differentiable and the derivative is 2 sin([1] / _𝑥_ )[�] _𝑥_ sin([1] / _𝑥_ ) − cos([1] / _𝑥_ )[�] . As an 4 4 exercise, show that for _𝑥𝑛_ = (8 _𝑛_ +1) _𝜋_[, we have][ lim] _[𝑛]_[→∞] _[𝑓]_[′][(] _[𝑥][𝑛]_[)][ =][ −][1][, and for] _[𝑦][𝑛]_[=] (8 _𝑛_ +3) _𝜋_[, we] have lim _𝑛_ →∞ _𝑓_[′] ( _𝑦𝑛_ ) = 1. So _𝑓_[′] cannot be continuous at 0 no matter what _𝑓_[′] (0) is.

Let us show that _𝑓_ is differentiable at 0 and _𝑓_[′] (0) = 0. For _𝑥_ ≠ 0,

**==> picture [270 x 32] intentionally omitted <==**

_4.2. MEAN VALUE THEOREM_

169

And, of course, as _𝑥_ tends to zero, | _𝑥_ | tends to zero, and hence _𝑓_ ( _𝑥𝑥_ )−−0 _𝑓_ (0) − 0 goes to zero. ��� ��� Therefore, _𝑓_ is differentiable at 0 and the derivative at 0 is 0. A key point in the calculation 2 above is that �� _𝑓_ ( _𝑥_ )�� ≤ _𝑥_ , see also Exercises and .

It is sometimes useful to assume the derivative of a differentiable function is continuous. If _𝑓_ : _𝐼_ → ℝ is differentiable and the derivative _𝑓_[′] is continuous on _𝐼_ , then we say _𝑓_ is _continuously differentiable_ . It is common to write _𝐶_[1] ( _𝐼_ ) for the set of continuously _𝐼_ . differentiable functions on

## **4.2.6 Exercises**

_**Exercise**_ **4.2.1** _**:** Finish the proof of ._

_**Exercise**_ **4.2.2** _**:** Finish the proof of ._

_**Exercise**_ **4.2.3** _**:** Suppose 𝑓_ : ℝ → ℝ _is a differentiable function such that 𝑓_[′] _is a bounded function. Prove that 𝑓 is a Lipschitz continuous function._

_**Exercise**_ **4.2.4** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is differentiable and 𝑐_ ∈[ _𝑎, 𝑏_ ] _. Show there exists a sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _converging to 𝑐, 𝑥𝑛_ ≠ _𝑐 for all 𝑛, such that_

**==> picture [90 x 17] intentionally omitted <==**

_Do note this does_ not _imply that 𝑓_[′] _is continuous (why?)._

2 _**Exercise**_ **4.2.5** _**:** Suppose 𝑓_ : ℝ → ℝ _is a function such that_ �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� ≤ �� _𝑥_ − _𝑦_ �� _for all 𝑥 and 𝑦. Show that 𝑓_ ( _𝑥_ ) = _𝐶 for some constant 𝐶. Hint: Show that 𝑓 is differentiable at all points and compute the derivative._

_**Exercise**_ **4.2.6** _**:** Finish the proof of . That is, suppose 𝐼 is an interval and 𝑓_ : _𝐼_ → ℝ _is a differentiable function such that 𝑓_[′] ( _𝑥_ ) _>_ 0 _for all 𝑥_ ∈ _𝐼. Show that 𝑓 is strictly increasing._

_**Exercise**_ **4.2.7** _**:** Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _is a differentiable function such that 𝑓_[′] ( _𝑥_ ) ≠ 0 _for all 𝑥_ ∈( _𝑎, 𝑏_ ) _. Suppose there exists a point 𝑐_ ∈( _𝑎, 𝑏_ ) _such that 𝑓_[′] ( _𝑐_ ) _>_ 0 _. Prove 𝑓_[′] ( _𝑥_ ) _>_ 0 _for all 𝑥_ ∈( _𝑎, 𝑏_ ) _._

_**Exercise**_ **4.2.8** _**:** Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _and 𝑔_ : ( _𝑎, 𝑏_ ) → ℝ _are differentiable functions such that 𝑓_[′] ( _𝑥_ ) = _𝑔_[′] ( _𝑥_ ) _for all 𝑥_ ∈( _𝑎, 𝑏_ ) _, then show that there exists a constant 𝐶 such that 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) + _𝐶._

_**Exercise**_ **4.2.9** _**:** Prove the following version of L’Hôpital’s rule. Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _and 𝑔_ : ( _𝑎, 𝑏_ ) → ℝ _are differentiable functions and 𝑐_ ∈( _𝑎, 𝑏_ ) _. Suppose that 𝑓_ ( _𝑐_ ) = 0 _, 𝑔_ ( _𝑐_ ) = 0 _, 𝑔_[′] ( _𝑥_ ) ≠ 0 _when 𝑥_ ≠ _𝑐, and that the limit of[𝑓]_[′][(] _[𝑥]_[)] / _𝑔_[′] ( _𝑥_ ) _as 𝑥 goes to 𝑐 exists. Show that_

**==> picture [104 x 29] intentionally omitted <==**

_Compare to . Note: Before you do anything else, prove that 𝑔_ ( _𝑥_ ) ≠ 0 _when 𝑥_ ≠ _𝑐._

_**Exercise**_ **4.2.10** _**:** Let 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _be an unbounded differentiable function. Show 𝑓_[′] : ( _𝑎, 𝑏_ ) → ℝ _is unbounded._

_CHAPTER 4. THE DERIVATIVE_

170

_**Exercise**_ **4.2.11** _**:** Prove the theorem Rolle actually proved in 1691:_ If _𝑓_ is a polynomial, _𝑓_[′] ( _𝑎_ ) = _𝑓_[′] ( _𝑏_ ) = 0 for some _𝑎 < 𝑏_ , and there is no _𝑐_ ∈( _𝑎, 𝑏_ ) such that _𝑓_[′] ( _𝑐_ ) = 0, then there is at most one root of _𝑓_ in ( _𝑎, 𝑏_ ), that is at most one _𝑥_ ∈( _𝑎, 𝑏_ ) such that _𝑓_ ( _𝑥_ ) = 0. _In other words, between any two consecutive roots of 𝑓_[′] _is at most one root of 𝑓 . Hint: Suppose there are two roots and see what happens._

_**Exercise**_ **4.2.12** _**:** Suppose 𝑎, 𝑏_ ∈ ℝ _and 𝑓_ : ℝ → ℝ _is differentiable, 𝑓_[′] ( _𝑥_ ) = _𝑎 for all 𝑥, and 𝑓_ (0) = _𝑏. Find 𝑓 and prove that it is the unique differentiable function with this property._

## _**Exercise**_ **4.2.13** _**:**_

_a) Prove ._

- _b) Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _is continuous, and suppose 𝑓 is differentiable everywhere except at 𝑐_ ∈( _𝑎, 𝑏_ ) _and_ lim _𝑥_ → _𝑐 𝑓_[′] ( _𝑥_ ) = _𝐿. Prove that 𝑓 is differentiable at 𝑐 and 𝑓_[′] ( _𝑐_ ) = _𝐿._

_**Exercise**_ **4.2.14** _**:** Suppose 𝑓_ : (0 _,_ 1) → ℝ _is differentiable and 𝑓_[′] _is bounded._

- _a) Show that there exists a continuous function 𝑔_ : [0 _,_ 1) → ℝ _such that 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) _for all 𝑥_ ≠ 0 _. Hint: and ._

- _b) Find an example where the 𝑔 is not differentiable at 𝑥_ = 0 _._

   - _Hint: Consider something based on_ sin(ln _𝑥_ ) _, and assume you know basic properties of_ sin _and_ ln _from calculus._

- _c) Instead of assuming that 𝑓_[′] _is bounded, assume that_ lim _𝑥_ →0 _𝑓_[′] ( _𝑥_ ) = _𝐿. Prove that not only does 𝑔 exist but it is differentiable at_ 0 _and 𝑔_[′] (0) = _𝐿._

_**Exercise**_ **4.2.15** _**:** Prove ._

_4.3. TAYLOR’S THEOREM_

171

## **4.3 Taylor’s theorem**

_Note: less than a lecture (optional section)_

## **4.3.1 Derivatives of higher orders**

When _𝑓_ : _𝐼_ → ℝ is differentiable, we obtain a function _𝑓_[′] : _𝐼_ → ℝ. The function _𝑓_[′] is called the _first derivative_ of _𝑓_ . If _𝑓_[′] is differentiable, we denote by _𝑓_[′′] : _𝐼_ → ℝ the derivative of _𝑓_[′] . The function _𝑓_[′′] is called the _second derivative_ of _𝑓_ . We similarly obtain _𝑓_[′′′] , _𝑓_[′′′′] , and so on. With a larger number of derivatives the notation would get out of hand; we denote by _𝑓_[(] _[𝑛]_[)] the _𝑛th derivative_ of _𝑓_ . When _𝑓_ possesses _𝑛_ derivatives, we say _𝑓_ is _𝑛 times differentiable_ .

## **4.3.2 Taylor’s theorem**

. Taylor’s theorem is a generalization of the Mean value theorem says that up to a small error _𝑓_ ( _𝑥_ ) for _𝑥_ near _𝑥_ 0 can be approximated by _𝑓_ ( _𝑥_ 0), that is

**==> picture [145 x 13] intentionally omitted <==**

_𝑐_ between _𝑥_ where the “error” is measured in terms of the first derivative at some point and _𝑥_ 0. Taylor’s theorem generalizes this result to higher derivatives. It tells us that up to a small error, any _𝑛_ times differentiable function can be approximated at a point _𝑥_ 0 by a polynomial. The error of this approximation behaves like ( _𝑥_ − _𝑥_ 0) _[𝑛]_ near the point _𝑥_ 0. To see why this is a good approximation, notice that for a big _𝑛_ , ( _𝑥_ − _𝑥_ 0) _[𝑛]_ is very small in a small interval around _𝑥_ 0.