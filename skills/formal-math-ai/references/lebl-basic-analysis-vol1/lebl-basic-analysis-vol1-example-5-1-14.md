Example 5.1.14

**Example 5.1.14:** Let us show 1+1 _𝑥_[is integrable on][ [][0] _[, 𝑏]_[]][ for all] _[ 𝑏][>]_[ 0][.][We will see later that] continuous functions are integrable, but let us demonstrate how we do it directly.

Let _𝜖>_ 0 be given. Take _𝑛_ ∈ ℕ and let _𝑥𝑖_ � _[𝑖𝑏]_ / _𝑛_ form the partition _𝑃_ � { _𝑥_ 0 _, 𝑥_ 1 _, . . . , 𝑥𝑛_ } of [0 _, 𝑏_ ]. Then Δ _𝑥𝑖_ = _[𝑏]_ / _𝑛_ for all _𝑖_ . As _𝑓_ is decreasing, for every subinterval [ _𝑥𝑖_ −1 _, 𝑥𝑖_ ],

**==> picture [454 x 31] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

188

Then

**==> picture [449 x 72] intentionally omitted <==**

The sum telescopes, the terms successively cancel each other, something we have seen _𝑏_[2] before. Picking _𝑛_ to be such that _𝑛_ ( _𝑏_ +1) _[<][𝜖]_[, the proposition is satisfied, and the function is] integrable.

_Remark_ 5.1.15 _._ A way of thinking of the integral is that it adds up (integrates) lots of local information—it sums _𝑓_ ( _𝑥_ ) _𝑑𝑥_ over all _𝑥_ . The integral sign was chosen by Leibniz to be the long S to mean summation. Unlike derivatives, which are “local,” integrals show up in applications when one wants a “global” answer: total distance travelled, average temperature, total charge, etc.

## **5.1.3 More notation**

When _𝑓_ : _𝑆_ → ℝ is defined on a larger set _𝑆_ and [ _𝑎, 𝑏_ ] ⊂ _𝑆_ , we say _𝑓_ is Riemann integrable on [ _𝑎, 𝑏_ ] if the restriction of _𝑓_ to [ _𝑎, 𝑏_ ] is Riemann integrable. In this case, we say _𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] , _𝑏_ and we write ∫ _𝑎[𝑓]_[to mean the Riemann integral of the restriction of] _[𝑓]_[to][ [] _[𝑎, 𝑏]_[]][.] _𝑏_ It is useful to define the integral ∫ _𝑎[𝑓]_[even if] _[ 𝑎]_[≮] _[𝑏]_[.][Suppose] _[ 𝑏][<][𝑎]_[and] _[𝑓]_[∈] _[R]_[�] [ _𝑏, 𝑎_ ][�] , then define

**==> picture [91 x 32] intentionally omitted <==**

For any function _𝑓_ , define

**==> picture [58 x 30] intentionally omitted <==**

At times, the variable _𝑥_ may already have some other meaning. When we need to write down the variable of integration, we may simply use a different letter. For example,

**==> picture [140 x 33] intentionally omitted <==**

## **5.1.4 Exercises**

_**Exercise**_ **5.1.1** _**:** Define 𝑓_ : [0 _,_ 1] → ℝ _by 𝑓_ ( _𝑥_ ) � _𝑥_[3] _and let 𝑃_ � {0 _,_ 0 _._ 1 _,_ 0 _._ 4 _,_ 1} _. Compute 𝐿_ ( _𝑃, 𝑓_ ) _and 𝑈_ ( _𝑃, 𝑓_ ) _._

1 _**Exercise**_ **5.1.2** _**:** Let 𝑓_ : [0 _,_ 1] → ℝ _be defined by 𝑓_ ( _𝑥_ ) � _𝑥. Show that 𝑓_ ∈ _R_[�] [0 _,_ 1][�] _and compute_ ∫0 _[𝑓] using the definition of the integral (but feel free to use the propositions of this section)._

_5.1. THE RIEMANN INTEGRAL_

189

_**Exercise**_ **5.1.3** _**:** Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a bounded function. Suppose there exists a sequence of partitions_ { _𝑃𝑘_ }[∞] _𝑘_ =1 _[of]_[ [] _[𝑎, 𝑏]_[]] _[ such that]_

**==> picture [141 x 18] intentionally omitted <==**

_Show that 𝑓 is Riemann integrable and that_

**==> picture [178 x 29] intentionally omitted <==**

_**Exercise**_ **5.1.4** _**:** Finish the proof of ._

_**Exercise**_ **5.1.5** _**:** Suppose 𝑓_ : [−1 _,_ 1] → ℝ _is defined as_

**==> picture [98 x 36] intentionally omitted <==**

1 _Prove that 𝑓_ ∈ _R_[�] [−1 _,_ 1][�] _and compute_ ∫−1 _[𝑓][using the definition of the integral (but feel free to use the] propositions of this section)._

_**Exercise**_ **5.1.6** _**:** Let 𝑐_ ∈( _𝑎, 𝑏_ ) _and let 𝑑_ ∈ ℝ _. Define 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _as_

**==> picture [98 x 36] intentionally omitted <==**

_𝑏 Prove that 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _and compute_ ∫ _𝑎[𝑓][using][the][definition][of][the][integral][(but][feel][free][to][use][the] propositions of this section)._

_**Exercise**_ **5.1.7** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is Riemann integrable. Let 𝜖>_ 0 _be given. Then show that there exists a partition 𝑃_ = { _𝑥_ 0 _, 𝑥_ 1 _, . . . , 𝑥𝑛_ } _such that for every set of numbers_ { _𝑐_ 1 _, 𝑐_ 2 _, . . . , 𝑐𝑛_ } _with 𝑐𝑘_ ∈[ _𝑥𝑘_ −1 _, 𝑥𝑘_ ] _for all 𝑘, we have_

**==> picture [469 x 76] intentionally omitted <==**

_**Exercise**_ **5.1.9** _**:** Suppose 𝑓_ : [0 _,_ 1] → ℝ _and 𝑔_ : [0 _,_ 1] → ℝ _are such that for all 𝑥_ ∈(0 _,_ 1] _, we have_ 1 1 _𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) _. Suppose 𝑓 is Riemann integrable. Prove 𝑔 is Riemann integrable and_ ∫0 _[𝑓]_[=] ∫0 _[𝑔][.]_

_**Exercise**_ **5.1.10** _**:** Let 𝑓_ : [0 _,_ 1] → ℝ _be a bounded function. Let 𝑃𝑛_ = { _𝑥_ 0 _, 𝑥_ 1 _, . . . , 𝑥𝑛_ } _be a uniform partition_ ∞ _of_ [0 _,_ 1] _, that is, 𝑥𝑖_ = _[𝑖]_ / _𝑛. Is_ � _𝐿_ ( _𝑃𝑛 , 𝑓_ )� _𝑛_ =1 _[always monotone?][Yes/No:][Prove or find a counterexample.]_

_**Exercise**_ **5.1.11** (Challenging) _**:** For a bounded function 𝑓_ : [0 _,_ 1] → ℝ _, let 𝑅𝑛_ � ([1] / _𝑛_ )[�] _[𝑛] 𝑖_ =1 _[𝑓]_[(] _[𝑖]_[/] _[𝑛]_[)] _[ (the] uniform right-hand rule)._

1 _a) If 𝑓 is Riemann integrable show_ ∫0 _[𝑓]_[=] _𝑛_[lim] →∞ _[𝑅][𝑛][.]_

_b) Find an 𝑓 that is not Riemann integrable, but_ lim _𝑛_ →∞ _[𝑅][𝑛][exists.]_

_CHAPTER 5. THE RIEMANN INTEGRAL_

190

_**Exercise**_ **5.1.12** (Challenging) _**:** Generalize the previous exercise. Show that 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _if and only if there exists an 𝐼_ ∈ ℝ _, such that for every 𝜖>_ 0 _there exists a 𝛿>_ 0 _such that if 𝑃 is a partition with_ Δ _𝑥𝑖 < 𝛿 𝑏 for all 𝑖, then_ �� _𝐿_ ( _𝑃, 𝑓_ ) − _𝐼_ �� _< 𝜖 and_ �� _𝑈_ ( _𝑃, 𝑓_ ) − _𝐼_ �� _< 𝜖. If 𝑓_ ∈ _R_ �[ _𝑎, 𝑏_ ][�] _, then 𝐼_ = ∫ _𝑎[𝑓][.]_ _**Exercise**_ **5.1.13** _**:** Using and the idea of the proof in , show that Darboux integral is the same as the standard definition of Riemann integral, which you have most likely seen in calculus. That is, show that 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _if and only if there exists an 𝐼_ ∈ ℝ _, such that for every 𝜖>_ 0 _there exists a 𝛿>_ 0 _𝑛 such that if 𝑃_ = { _𝑥_ 0 _, 𝑥_ 1 _, . . . , 𝑥𝑛_ } _is a partition with_ Δ _𝑥𝑖 < 𝛿 for all 𝑖, then_ ��� _𝑖_ =1 _[𝑓]_[(] _[𝑐][𝑖]_[)][Δ] _[𝑥][𝑖]_[−] _[𝐼]_ �� _< 𝜖 for every 𝑏 set_ { _𝑐_ 1 _, 𝑐_ 2 _, . . . , 𝑐𝑛_ } _with 𝑐𝑖_ ∈[ _𝑥𝑖_ −1 _, 𝑥𝑖_ ] _. If 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _, then 𝐼_ = ∫ _𝑎[𝑓][.]_

_**Exercise**_ **5.1.14** (Challenging) _**:** Construct functions 𝑓 and 𝑔, where 𝑓_ : [0 _,_ 1] → ℝ _is Riemann integrable, 𝑔_ : [0 _,_ 1] →[0 _,_ 1] _is one-to-one and onto, and such that the composition 𝑓_ ◦ _𝑔 is not Riemann integrable._

_**Exercise**_ **5.1.15** _**:** Suppose that 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is a bounded function, and 𝑃 is a partition of_ [ _𝑎, 𝑏_ ] _such that 𝐿_ ( _𝑃, 𝑓_ ) = _𝑈_ ( _𝑃, 𝑓_ ) _. Prove that 𝑓 is a constant function._

_5.2. PROPERTIES OF THE INTEGRAL_

191

## **5.2 Properties of the integral**

_Note: 2 lectures, integrability of functions with discontinuities can safely be skipped_

## **5.2.1 Additivity**

Adding a bunch of things in two parts and then adding those two parts should be the same as adding everything all at once. The corresponding property for integrals is called the additive property of the integral. First, we prove the additivity property for the lower and upper Darboux integrals.