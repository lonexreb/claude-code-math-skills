Example 5.3.7

**Example 5.3.7:** Consider

**==> picture [70 x 32] intentionally omitted <==**

It may be tempting to take _𝑔_ ( _𝑥_ ) � ln | _𝑥_ |. Compute _𝑔_[′] ( _𝑥_ ) =[1] / _𝑥_ and try to write

**==> picture [134 x 35] intentionally omitted <==**

This “solution” is incorrect, and it does not say that we can solve the given integral. First problem is that[ln] _𝑥_[|] _[𝑥]_[|] is not continuous on [−1 _,_ 1]. It is not defined at 0, and cannot be made continuous by defining a value at 0. Second,[ln] _𝑥_[|] _[𝑥]_[|] is not even Riemann integrable on [−1 _,_ 1] (it is unbounded). The integral we wrote down simply does not make sense. Finally, _𝑔_ is not continuous on [−1 _,_ 1], let alone continuously differentiable.

_5.3. FUNDAMENTAL THEOREM OF CALCULUS_

205

## **5.3.4 Exercises**

**==> picture [212 x 68] intentionally omitted <==**

_**Exercise**_ **5.3.3** _**:** Suppose 𝐹_ : [ _𝑎, 𝑏_ ] → ℝ _is continuous and differentiable on_ [ _𝑎, 𝑏_ ] \ _𝑆, where 𝑆 is a finite set. 𝑏 Suppose there exists an 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _such that 𝑓_ ( _𝑥_ ) = _𝐹_[′] ( _𝑥_ ) _for 𝑥_ ∈[ _𝑎, 𝑏_ ]\ _𝑆. Show that_ ∫ _𝑎[𝑓]_[=] _[ 𝐹]_[(] _[𝑏]_[)−] _[𝐹]_[(] _[𝑎]_[)] _[.]_ _**Exercise**_ **5.3.4** _**:** Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function. Let 𝑐_ ∈[ _𝑎, 𝑏_ ] _be arbitrary. Define_

**==> picture [68 x 27] intentionally omitted <==**

_Prove that 𝐹 is differentiable and that 𝐹_[′] ( _𝑥_ ) = _𝑓_ ( _𝑥_ ) _for all 𝑥_ ∈[ _𝑎, 𝑏_ ] _._

_**Exercise**_ **5.3.5** _**:** Prove_ integration by parts _. That is, suppose 𝐹 and 𝐺 are continuously differentiable functions on_ [ _𝑎, 𝑏_ ] _. Then prove_

**==> picture [285 x 30] intentionally omitted <==**

_**Exercise**_ **5.3.6** _**:** Suppose 𝐹 and 𝐺 are continuously differentiable functions defined on_ [ _𝑎, 𝑏_ ] _such that 𝐹_[′] ( _𝑥_ ) = _𝐺_[′] ( _𝑥_ ) _for all 𝑥_ ∈[ _𝑎, 𝑏_ ] _. Using the fundamental theorem of calculus, show that 𝐹 and 𝐺 differ by a constant. That is, show that there exists a 𝐶_ ∈ ℝ _such that 𝐹_ ( _𝑥_ ) − _𝐺_ ( _𝑥_ ) = _𝐶._

The next exercise shows how we can use the integral to “smooth out” a non-differentiable function.

_**Exercise**_ **5.3.7** _**:** Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function. Let 𝜖>_ 0 _be a constant so that 𝑎_ + _𝜖< 𝑏_ − _𝜖. For 𝑥_ ∈[ _𝑎_ + _𝜖, 𝑏_ − _𝜖_ ] _, define_

**==> picture [92 x 28] intentionally omitted <==**

_a) Show that 𝑔 is differentiable and find the derivative._

_b) Let 𝑓 be differentiable and fix 𝑥_ ∈( _𝑎, 𝑏_ ) _(let 𝜖 be small enough). What happens to 𝑔_[′] ( _𝑥_ ) _as 𝜖 gets smaller?_

_c) Find 𝑔 for 𝑓_ ( _𝑥_ ) � | _𝑥_ | _, 𝜖_ = 1 _(you can assume_ [ _𝑎, 𝑏_ ] _is large enough)._

_𝑥 𝑏_ _**Exercise**_ **5.3.8** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is continuous and_ ∫ _𝑎[𝑓]_[=] ∫ _𝑥[𝑓][for][all][𝑥]_[∈[] _[𝑎, 𝑏]_[]] _[.][Show][that] 𝑓_ ( _𝑥_ ) = 0 _for all 𝑥_ ∈[ _𝑎, 𝑏_ ] _. 𝑥_ _**Exercise**_ **5.3.9** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is continuous and_ ∫ _𝑎[𝑓]_[=][ 0] _[ for all rational][ 𝑥][in]_[ [] _[𝑎, 𝑏]_[]] _[.][Show that] 𝑓_ ( _𝑥_ ) = 0 _for all 𝑥_ ∈[ _𝑎, 𝑏_ ] _._

_**Exercise**_ **5.3.10** _**:** A function 𝑓 is an_ odd function _if 𝑓_ ( _𝑥_ ) = − _𝑓_ (− _𝑥_ ) _, and 𝑓 is an_ even function _if 𝑓_ ( _𝑥_ ) = _𝑓_ (− _𝑥_ ) _. Let 𝑎 >_ 0 _. Assume 𝑓 is continuous. Prove:_

_a) If 𝑓 is odd, then_ ∫− _𝑎𝑎[𝑓]_[=][ 0] _[.]_

_b) If 𝑓 is even, then_ ∫− _𝑎𝑎[𝑓]_[=][ 2] ∫0 _𝑎[𝑓][.]_

> ‗ Compare this hypothesis to .

_CHAPTER 5. THE RIEMANN INTEGRAL_

206

## _**Exercise**_ **5.3.11** _**:**_

- _a) Show that 𝑓_ ( _𝑥_ ) � sin([1] / _𝑥_ ) _is integrable on every interval (you can define 𝑓_ (0) _to be anything)._

- 1

- _b) Compute_ ∫−1[sin][(][1][/] _[𝑥]_[)] _[ 𝑑𝑥][(mind the discontinuity).]_

_**Exercise**_ **5.3.12** (uses ) _**:**_

- _a) Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is increasing, by , 𝑓 is Riemann integrable. Suppose 𝑓 has a 𝑥_

- _discontinuity at 𝑐_ ∈( _𝑎, 𝑏_ ) _, show that 𝐹_ ( _𝑥_ ) � ∫ _𝑎[𝑓][is not differentiable at][ 𝑐][.]_

- _b) In , you constructed an increasing function 𝑓_ : [0 _,_ 1] → ℝ _that is discontinuous at every 𝑥_ ∈[0 _,_ 1] ∩ ℚ _. Use this 𝑓 to construct a function 𝐹_ ( _𝑥_ ) _that is continuous on_ [0 _,_ 1] _, but not differentiable at every 𝑥_ ∈[0 _,_ 1] ∩ ℚ _._

_**Exercise**_ **5.3.13** _**:** For any ℓ_ ∈ ℕ _, show that the following limit exists and find what it is:_

**==> picture [62 x 32] intentionally omitted <==**

_5.4. THE LOGARITHM AND THE EXPONENTIAL_

207

## **5.4 The logarithm and the exponential**

_Note: 1 lecture (optional, requires the optional sections , , )_

We now have the tools required to properly define the exponential and the logarithm that you know from calculus so well. We start with exponentiation. If _𝑛_ is a positive integer, it is obvious to define

**==> picture [97 x 31] intentionally omitted <==**

It makes sense to define _𝑥_[0] � 1. For negative integers, let _𝑥_[−] _[𝑛]_ �[1] / _𝑥[𝑛]_ . If _𝑥 >_ 0, define _𝑥_[1][/] _[𝑛]_ as the unique positive _𝑛_ th root. Finally, for a rational number _[𝑛]_ / _𝑚_ (in lowest terms), define

**==> picture [86 x 17] intentionally omitted <==**

It is not difficult to show we get the same number no matter what representation of _[𝑛]_ / _𝑚_ we use, so we do not need to use lowest terms.

~~√~~ 2 However, what do we mean by √2 ? Or _𝑥 𝑦_ in general? In particular, what is _𝑒 𝑥_ for all _𝑥_ ? And how do we solve _𝑦_ = _𝑒[𝑥]_ for _𝑥_ ? This section answers these questions and more.

## **5.4.1 The logarithm**

It is convenient to define the logarithm first. Let us show that a unique function with the right properties exists, and only then will we call it _the_ logarithm.