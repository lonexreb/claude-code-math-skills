Proposition 5.2.10

**Proposition 5.2.10.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be Riemann integrable. Let 𝑔_ : [ _𝑎, 𝑏_ ] → ℝ _be such that 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) _for all 𝑥_ ∈[ _𝑎, 𝑏_ ] \ _𝑆, where 𝑆 is a finite set. Then 𝑔 is Riemann integrable and_

**==> picture [78 x 32] intentionally omitted <==**

_Sketch of proof._ Using additivity of the integral, split the interval [ _𝑎, 𝑏_ ] into smaller intervals such that _𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) holds for all _𝑥_ except at the endpoints (details are left to the reader). Therefore, without loss of generality suppose _𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) for all _𝑥_ ∈( _𝑎, 𝑏_ ). The proof follows by , and is left as . □

Finally, monotone (increasing or decreasing) functions are always Riemann integrable. . The proof is left to the reader as part of **Proposition 5.2.11.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a monotone function. Then 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _._

## **5.2.5 Exercises**

_**Exercise**_ **5.2.1** _**:** Finish the proof of the first part of . Let 𝑓 be in R_[�] [ _𝑎, 𝑏_ ][�] _. Prove that_ − _𝑓 is in R_[�] [ _𝑎, 𝑏_ ][�] _and_

**==> picture [142 x 30] intentionally omitted <==**

_**Exercise**_ **5.2.2** _**:** Prove the second part of . Let 𝑓 and 𝑔 be in R_[�] [ _𝑎, 𝑏_ ][�] _. Prove, without using , that 𝑓_ + _𝑔 is in R_[�] [ _𝑎, 𝑏_ ][�] _and_

**==> picture [233 x 30] intentionally omitted <==**

_Hint: One way to do it is to use to find a single partition 𝑃 such that 𝑈_ ( _𝑃, 𝑓_ )− _𝐿_ ( _𝑃, 𝑓_ ) _<[𝜖]_ /2 _and 𝑈_ ( _𝑃, 𝑔_ ) − _𝐿_ ( _𝑃, 𝑔_ ) _<[𝜖]_ /2 _._

_**Exercise**_ **5.2.3** _**:** Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be Riemann integrable, and 𝑔_ : [ _𝑎, 𝑏_ ] → ℝ _be such that 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) _for all 𝑥_ ∈( _𝑎, 𝑏_ ) _. Prove that 𝑔 is Riemann integrable and that_

**==> picture [70 x 29] intentionally omitted <==**

_**Exercise**_ **5.2.4** _**:** Prove the_ mean value theorem for integrals _: If 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is continuous, then there 𝑏 exists a 𝑐_ ∈[ _𝑎, 𝑏_ ] _such that_ ∫ _𝑎[𝑓]_[=] _[𝑓]_[(] _[𝑐]_[)(] _[𝑏]_[−] _[𝑎]_[)] _[.]_

_**Exercise**_ **5.2.5** _**:** Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function such that 𝑓_ ( _𝑥_ ) ≥ 0 _for all 𝑥_ ∈[ _𝑎, 𝑏_ ] _and 𝑏[Prove that][𝑓]_[(] _[𝑥]_[)][ =][ 0] _[ for all][ 𝑥][.]_ ∫ _𝑎[𝑓]_[=][ 0] _[.]_

_CHAPTER 5. THE RIEMANN INTEGRAL_

198

_𝑏_ _**Exercise**_ **5.2.6** _**:** Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function and_ ∫ _𝑎[𝑓]_[=][0] _[.][Prove][that][there][exists][a] 𝑐_ ∈[ _𝑎, 𝑏_ ] _such that 𝑓_ ( _𝑐_ ) = 0 _. (Compare with the previous exercise.)_

_𝑏 𝑏_ _**Exercise**_ **5.2.7** _**:** Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _and 𝑔_ : [ _𝑎, 𝑏_ ] → ℝ _be continuous functions such that_ ∫ _𝑎[𝑓]_[=] ∫ _𝑎[𝑔][.] Show that there exists a 𝑐_ ∈[ _𝑎, 𝑏_ ] _such that 𝑓_ ( _𝑐_ ) = _𝑔_ ( _𝑐_ ) _._

_**Exercise**_ **5.2.8** _**:** Let 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _. Let 𝛼, 𝛽, 𝛾 be arbitrary numbers in_ [ _𝑎, 𝑏_ ] _(not necessarily ordered in any way). Prove_

**==> picture [112 x 32] intentionally omitted <==**

_𝑏 Recall what_ ∫ _𝑎[𝑓][means if][ 𝑏]_[≤] _[𝑎][.]_

_**Exercise**_ **5.2.9** _**:** Prove ._

_**Exercise**_ **5.2.10** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is bounded and has finitely many discontinuities. Show that as a function of 𝑥 the expression_ �� _𝑓_ ( _𝑥_ )�� _is bounded with finitely many discontinuities and is thus Riemann integrable. Then show_

**==> picture [140 x 36] intentionally omitted <==**

_**Exercise**_ **5.2.11** (Hard) _**:** Show that the Thomae or popcorn function (see ) is Riemann integrable. Therefore, there exists a function discontinuous at all rational numbers (a dense set) that is Riemann integrable._

_That is, define 𝑓_ : [0 _,_ 1] → ℝ _by_

**==> picture [357 x 35] intentionally omitted <==**

1 _Show_ ∫0 _[𝑓]_[=][ 0] _[.]_

If _𝐼_ ⊂ ℝ is a bounded interval, then the function

**==> picture [117 x 35] intentionally omitted <==**

is called an _elementary step function_ .

_**Exercise**_ **5.2.12** _**:** Let 𝐼 be an arbitrary bounded interval (you should consider all types of intervals: closed, open, half-open) and 𝑎 < 𝑏, then using only the definition of the integral show that the elementary step function 𝜑𝐼 is integrable on_ [ _𝑎, 𝑏_ ] _, and find the integral in terms of 𝑎, 𝑏, and the endpoints of 𝐼._

A function _𝑓_ is called a _step function_ if it can be written as

**==> picture [91 x 33] intentionally omitted <==**

for some real numbers _𝛼_ 1 _, 𝛼_ 2 _, . . . , 𝛼𝑛_ and some bounded intervals _𝐼_ 1 _, 𝐼_ 2 _, . . . , 𝐼𝑛_ .

199

## _5.2. PROPERTIES OF THE INTEGRAL_

_**Exercise**_ **5.2.13** _**:** Using , show that a step function (see above) is integrable on every interval_ [ _𝑎, 𝑏_ ] _. Furthermore, find the integral in terms of 𝑎, 𝑏, the endpoints of 𝐼𝑘 and the 𝛼𝑘._

_**Exercise**_ **5.2.14** _**:** Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a function._

- _a) Show that if 𝑓 is increasing, then it is Riemann integrable. Hint: Use a uniform partition; each subinterval of same length._

- _b) Use part a) to show that if 𝑓 is decreasing, then it is Riemann integrable._

- _c) Suppose ℎ_ = _𝑓_ − _𝑔 where 𝑓 and 𝑔 are increasing functions on_ [ _𝑎, 𝑏_ ] _. Show that ℎ is Riemann integrable._

_**Exercise**_ **5.2.15** (Challenging) _**:** Suppose 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _, then the function that takes 𝑥 to_ �� _𝑓_ ( _𝑥_ )�� _is also Riemann integrable on_ [ _𝑎, 𝑏_ ] _. Then show the same inequality as ._

_**Exercise**_ **5.2.16** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _and 𝑔_ : [ _𝑎, 𝑏_ ] → ℝ _are bounded._

**==> picture [290 x 18] intentionally omitted <==**

_b) Find example 𝑓 and 𝑔 where the inequality is strict. Hint: 𝑓 and 𝑔 should not be Riemann integrable._

_**Exercise**_ **5.2.17** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is continuous and 𝑔_ : ℝ → ℝ _is Lipschitz continuous. Define_

**==> picture [128 x 30] intentionally omitted <==**

_Prove that ℎ is Lipschitz continuous._

_**Exercise**_ **5.2.18** _**:** Prove a version of the so-called_ Riemann–Lebesgue Lemma _(one of several so named): Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is continuous and define the sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[by]_

**==> picture [117 x 29] intentionally omitted <==**

_Prove that_ lim _𝑛_ →∞ _[𝑥][𝑛]_[=][ 0] _[.]_

‗ Such an _ℎ_ is said to be of _bounded variation_ .

_CHAPTER 5. THE RIEMANN INTEGRAL_

200

## **5.3 Fundamental theorem of calculus**

## _Note: 1.5 lectures_

. In this section we discuss and prove the _fundamental theorem of calculus_ The entirety of integral calculus is built upon this theorem, ergo the name. The theorem relates the seemingly unrelated concepts of integral and derivative. It tells us how to compute the antiderivative of a function using the integral and vice versa.

## **5.3.1 First form of the theorem**