Example 5.5.14

**Example 5.5.14:** The integral test can be used not only to show that a series converges, but to estimate its sum to arbitrary precision. Let us show[�][∞] _𝑛_ =1 _𝑛_ 1[2][exists and estimate its sum] to within 0.01. As this series is the _𝑝_ -series for _𝑝_ = 2, we already proved it converges (let us pretend we do not know that), but we only roughly estimated its sum.

The fundamental theorem of calculus says that for all _𝑘_ ∈ ℕ,

**==> picture [82 x 29] intentionally omitted <==**

In particular, the series must converge. But we also have

**==> picture [278 x 35] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

224

Adding the partial sum up to _𝑘_ − 1 we get

**==> picture [206 x 38] intentionally omitted <==**

In other words,[1] / _𝑘_ +[�] _𝑛[𝑘]_[−] =[1] 1[1][/] _[𝑛]_[2][is an estimate for the sum to within][1][/] _[𝑘]_[2][.][Therefore, if we] wish to find the sum to within 0.01, we note[1] /10[2] = 0 _._ 01. We obtain

**==> picture [354 x 38] intentionally omitted <==**

The actual sum is _[𝜋]_[2] /6 ≈ 1 _._ 6449 _. . ._ .

## **5.5.2 Exercises**

_**Exercise**_ **5.5.1** _**:** Finish the proof of ._

_**Exercise**_ **5.5.2** _**:** Find out for which 𝑎_ ∈ ℝ _does_[�][∞] _𝑛_ =1 _[𝑒][𝑎𝑛][converge.][When the series converges, find an upper] bound for the sum._

_**Exercise**_ **5.5.3** _**:**_

_a) Estimate_[�][∞] _𝑛_ =1 _𝑛_ ( _𝑛_ 1+1) _[correct to within 0.01 using the integral test.]_

_b) Compute the limit of the series exactly and compare. Hint: The sum telescopes._

_**Exercise**_ **5.5.4** _**:** Prove_

**==> picture [105 x 27] intentionally omitted <==**

_Hint: Again, it is enough to show this on just one side._

_**Exercise**_ **5.5.5** _**:** Can you interpret_

**==> picture [58 x 33] intentionally omitted <==**

_as an improper integral? If so, compute its value._

_**Exercise**_ **5.5.6** _**:** Take 𝑓_ : [0 _,_ ∞) → ℝ _, Riemann integrable on every interval_ [0 _, 𝑏_ ] _, and such that there exist 𝑀, 𝑎, and 𝑇, such that_ �� _𝑓_ ( _𝑡_ )�� ≤ _𝑀𝑒 𝑎𝑡 for all 𝑡_ ≥ _𝑇. Show that the_ Laplace transform _of 𝑓 exists. That is, for every 𝑠 > 𝑎 the following integral converges:_

**==> picture [112 x 27] intentionally omitted <==**

_**Exercise**_ **5.5.7** _**:** Let 𝑓_ : ℝ → ℝ _be a Riemann integrable function on every interval_ [ _𝑎, 𝑏_ ] _, and such that_ ∞ ∫−∞ �� _𝑓_ ( _𝑥_ )�� _𝑑𝑥 <_ ∞ _. Show that the_ Fourier sine and cosine transforms _exist. That is, for every 𝜔_ ≥ 0 _the following integrals converge_

**==> picture [322 x 27] intentionally omitted <==**

_Furthermore, show that 𝐹[𝑠] and 𝐹[𝑐] are bounded functions._

_5.5. IMPROPER INTEGRALS_

225

∞ _**Exercise**_ **5.5.8** _**:** Suppose 𝑓_ : [0 _,_ ∞) → ℝ _is Riemann integrable on every interval_ [0 _, 𝑏_ ] _. Show that_ ∫0 _𝑓 𝑏 converges if and only if for every 𝜖>_ 0 _there exists an 𝑀 such that if 𝑀_ ≤ _𝑎 < 𝑏, then_ ��∫ _𝑎[𝑓]_ �� _< 𝜖._ _**Exercise**_ **5.5.9** _**:** Suppose 𝑓_ : [0 _,_ ∞) → ℝ _is nonnegative and_ decreasing _. Prove:_

∞ _a) If_ ∫0 _𝑓 <_ ∞ _, then 𝑥_ lim→∞ _[𝑓]_[(] _[𝑥]_[)][ =][ 0] _[.]_

_b) The converse does not hold._

_**Exercise**_ **5.5.10** _**:** Find an example of an_ unbounded _continuous function 𝑓_ : [0 _,_ ∞) → ℝ _that is nonnegative_ ∞ _and such that_ ∫0 _𝑓 <_ ∞ _. Note that_ lim _𝑥_ →∞ _𝑓_ ( _𝑥_ ) _will not exist; compare previous exercise. Hint: On each interval_ [ _𝑘, 𝑘_ + 1] _, 𝑘_ ∈ ℕ _, define a function whose integral over this interval is less than say_ 2[−] _[𝑘] ._

_**Exercise**_ **5.5.11** (More challenging) _**:** Find an example of a function 𝑓_ : [0 _,_ ∞) → ℝ _integrable on all 𝑛_ ∞ _intervals such that_ lim _𝑛_ →∞ ∫0 _𝑓 converges as a limit of a sequence (so 𝑛_ ∈ ℕ _), but such that_ ∫0 _𝑓 does not exist. Hint: For all 𝑛_ ∈ ℕ _, divide_ [ _𝑛, 𝑛_ + 1] _into two halves. On one half make the function negative, on the other make the function positive._

_**Exercise**_ **5.5.12** _**:** Suppose 𝑓_ : [1 _,_ ∞) → ℝ _is such that 𝑔_ ( _𝑥_ ) � _𝑥_[2] _𝑓_ ( _𝑥_ ) _is a bounded function. Prove that_ ∫1∞ _𝑓 converges._

It is sometimes desirable to assign a value to integrals that normally cannot be interpreted even 1 as improper integrals, e.g. ∫−1 1/ _𝑥 𝑑𝑥_ . Suppose _𝑓_ : [ _𝑎, 𝑏_ ] → ℝ is a function and _𝑎 < 𝑐 < 𝑏_ , where _𝑓_ is Riemann integrable on the intervals [ _𝑎, 𝑐_ − _𝜖_ ] and [ _𝑐_ + _𝜖, 𝑏_ ] for all _𝜖>_ 0. Define the _Cauchy principal 𝑏 value_ of ∫ _𝑎[𝑓]_[as]

**==> picture [178 x 30] intentionally omitted <==**

if the limit exists.

_**Exercise**_ **5.5.13** _**:**_

1 _a) Compute 𝑝.𝑣._ ∫−1 1/ _𝑥 𝑑𝑥._

− _𝜖_ 1 _b) Compute_ lim _𝜖_ →0[+] (∫−1 1/ _𝑥 𝑑𝑥_ + ∫2 _𝜖_ 1/ _𝑥 𝑑𝑥_ ) _and show it is not equal to the principal value._

_𝑏 𝑏 c) Show that if 𝑓 is integrable on_ [ _𝑎, 𝑏_ ] _, then 𝑝.𝑣._ ∫ _𝑎[𝑓]_[=] ∫ _𝑎[𝑓][(for an arbitrary][ 𝑐]_[∈(] _[𝑎, 𝑏]_[)] _[).]_

- _d) Suppose 𝑓_ : [−1 _,_ 1] → ℝ _is an odd function ( 𝑓_ (− _𝑥_ ) = − _𝑓_ ( _𝑥_ ) _) that is integrable on_ [−1 _,_ − _𝜖_ ] _and_ [ _𝜖,_ 1] 1

- _for all 𝜖>_ 0 _. Prove that 𝑝.𝑣._ ∫−1 _[𝑓]_[=][ 0]

1 _𝑓_ ( _𝑥_ ) _e) Suppose 𝑓_ : [−1 _,_ 1] → ℝ _is continuous and differentiable at 0. Show that 𝑝.𝑣._ ∫−1 _𝑥 𝑑𝑥 exists._

_**Exercise**_ **5.5.14** _**:** Let 𝑓_ : ℝ → ℝ _and 𝑔_ : ℝ → ℝ _be continuous functions, where 𝑔_ ( _𝑥_ ) = 0 _for all 𝑥_ ∉ [ _𝑎, 𝑏_ ] _for some interval_ [ _𝑎, 𝑏_ ] _._

_a) Show that the_ convolution

**==> picture [151 x 27] intentionally omitted <==**

_is well-defined for all 𝑥_ ∈ ℝ _._

∞ _b) Suppose_ ∫−∞ �� _𝑓_ ( _𝑥_ )�� _𝑑𝑥 <_ ∞ _. Prove that_

**==> picture [242 x 16] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

226

## **Chapter 6**

## **Sequences of Functions**

## **6.1 Pointwise and uniform convergence**

_Note: 1–1.5 lecture_

Up till now, when we talked about limits of sequences we talked about sequences of numbers. A very useful concept in analysis is a sequence of functions. For example, a solution to some differential equation might be found by finding only approximate solutions. Then the actual solution is some sort of limit of those approximate solutions.

When talking about sequences of functions, the tricky part is that there are multiple notions of a limit. Let us describe two common notions of a limit of a sequence of functions.

## **6.1.1 Pointwise convergence**