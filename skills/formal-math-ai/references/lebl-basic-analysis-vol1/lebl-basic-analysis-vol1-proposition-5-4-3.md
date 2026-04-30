Proposition 5.4.3

**Proposition 5.4.3.** _Let 𝑥, 𝑦_ ∈ ℝ _._

**==> picture [128 x 16] intentionally omitted <==**

**==> picture [174 x 13] intentionally omitted <==**

_Remark_ 5.4.4 _._ There are other equivalent ways to define the exponential and the logarithm. A common way is to define _𝐸_ as the solution to the differential equation _𝐸_[′] ( _𝑥_ ) = _𝐸_ ( _𝑥_ ), _𝐸_ (0) = 1. See , for a sketch of that approach. Yet another approach is to . define the exponential function by power series, see

_Remark_ 5.4.5 _._ We proved the uniqueness of the functions _𝐿_ and _𝐸_ from just the properties _𝐿_ (1) = 0, _𝐿_[′] ( _𝑥_ ) =[1] / _𝑥_ and the equivalent condition for the exponential _𝐸_[′] ( _𝑥_ ) = _𝐸_ ( _𝑥_ ), _𝐸_ (0) = 1. Existence also follows from just these properties. Alternatively, uniqueness also follows from the laws of exponents, see the exercises.

## **5.4.3 Exercises**

_**Exercise**_ **5.4.1** _**:** Given a real number 𝑦 and 𝑏 >_ 0 _, define 𝑓_ : (0 _,_ ∞) → ℝ _and 𝑔_ : ℝ → ℝ _as 𝑓_ ( _𝑥_ ) � _𝑥[𝑦] and 𝑔_ ( _𝑥_ ) � _𝑏[𝑥] . Show that 𝑓 and 𝑔 are differentiable and find their derivative._

_**Exercise**_ **5.4.2** _**:** Let 𝑏 >_ 0 _, 𝑏_ ≠ 1 _be given._

- _a) Show that for every 𝑦 >_ 0 _, there exists a unique number 𝑥 such that 𝑦_ = _𝑏[𝑥] . Define the_ logarithm base _𝑏,_ log _𝑏_ : (0 _,_ ∞) → ℝ _, by_ log _𝑏_ ( _𝑦_ ) � _𝑥._

_b) Show that_ log _𝑏_ ( _𝑥_ ) =[ln] ln[(] ( _[𝑥] 𝑏_ )[)] _[.]_

**==> picture [229 x 20] intentionally omitted <==**

_d) Prove_ log _𝑏_ ( _𝑥𝑦_ ) = log _𝑏_ ( _𝑥_ ) + log _𝑏_ ( _𝑦_ ) _, and_ log _𝑏_ ( _𝑥[𝑦]_ ) = _𝑦_ log _𝑏_ ( _𝑥_ ) _._

_CHAPTER 5. THE RIEMANN INTEGRAL_

212

_**Exercise**_ **5.4.3** (requires ) _**:** Use to study the remainder term and show that for all 𝑥_ ∈ ℝ

**==> picture [58 x 32] intentionally omitted <==**

_Hint: Do not differentiate the series term by term (unless you would prove that it works)._

_**Exercise**_ **5.4.4** _**:** Use the geometric sum formula to show (for 𝑡_ ≠ −1 _)_

**==> picture [226 x 27] intentionally omitted <==**

_Using this fact show_

**==> picture [121 x 32] intentionally omitted <==**

_for all 𝑥_ ∈(−1 _,_ 1] _(note that 𝑥_ = 1 _is included). Finally, find the limit of the alternating harmonic series_

## _**Exercise**_ **5.4.5** _**:** Show_

**==> picture [158 x 77] intentionally omitted <==**

_Hint: Take the logarithm. Note: The expression_[�] 1 + _𝑛[𝑥]_ � _𝑛 arises in compound interest calculations. It is the amount of money in a bank account after 1 year if 1 dollar was deposited initially at interest 𝑥 and the interest was compounded 𝑛 times during the year. The exponential 𝑒[𝑥] is the result of continuous compounding._

## _**Exercise**_ **5.4.6** _**:**_

_a) Prove that for 𝑛_ ∈ ℕ _,_

_b) Prove that the limit_

**==> picture [129 x 90] intentionally omitted <==**

_exists. This constant is known as the_ Euler–Mascheroni constant _. It is not known if this constant is rational or not. It is approximately 𝛾_ ≈ 0 _._ 5772 _._

## _**Exercise**_ **5.4.7** _**:** Show_

**==> picture [70 x 24] intentionally omitted <==**

_**Exercise**_ **5.4.8** _**:** Show that 𝑒[𝑥] is_ convex _, in other words, show that if 𝑎_ ≤ _𝑥_ ≤ _𝑏, then 𝑒[𝑥]_ ≤ _𝑒[𝑎][𝑏] 𝑏_[−] − _[𝑥] 𝑎_[+] _[ 𝑒][𝑏][𝑥] 𝑏_ −[−] _𝑎[𝑎][.]_ ‗Named for the Swiss mathematician (1707–1783) and the Italian mathematician (1750–1800).

_5.4. THE LOGARITHM AND THE EXPONENTIAL_

213

_**Exercise**_ **5.4.9** _**:** Using the logarithm find_

**==> picture [46 x 19] intentionally omitted <==**

_**Exercise**_ **5.4.10** _**:** Show that 𝐸_ ( _𝑥_ ) = _𝑒[𝑥] is the unique continuous function such that 𝐸_ ( _𝑥_ + _𝑦_ ) = _𝐸_ ( _𝑥_ ) _𝐸_ ( _𝑦_ ) _and 𝐸_ (1) = _𝑒. Similarly, prove that 𝐿_ ( _𝑥_ ) = ln( _𝑥_ ) _is the unique continuous function defined on positive 𝑥 such that 𝐿_ ( _𝑥𝑦_ ) = _𝐿_ ( _𝑥_ ) + _𝐿_ ( _𝑦_ ) _and 𝐿_ ( _𝑒_ ) = 1 _._

_**Exercise**_ **5.4.11** (requires ) _**:** Since_ ( _𝑒[𝑥]_ )[′] = _𝑒[𝑥] , it is easy to see that 𝑒[𝑥] is infinitely differentiable (has derivatives of all orders). Define the function 𝑓_ : ℝ → ℝ _._

**==> picture [116 x 36] intentionally omitted <==**

_a) Prove that for every 𝑚_ ∈ ℕ _,_

**==> picture [72 x 26] intentionally omitted <==**

_b) Prove that 𝑓 is infinitely differentiable._

_c) Compute the Taylor series for 𝑓 at the origin, that is,_

**==> picture [64 x 33] intentionally omitted <==**

_Show that it converges, but show that it does not converge to 𝑓_ ( _𝑥_ ) _for any given 𝑥 >_ 0 _._

_CHAPTER 5. THE RIEMANN INTEGRAL_

214

## **5.5 Improper integrals**

_Note: 2–3 lectures (optional section, can safely be skipped, requires the optional )_

Often it is necessary to integrate over the entire real line, or an unbounded interval of the form [ _𝑎,_ ∞) or (−∞ _, 𝑏_ ]. We may also wish to integrate unbounded functions defined on an open bounded interval ( _𝑎, 𝑏_ ). For such intervals or functions, the Riemann integral . is not defined, but we will write down the integral anyway in the spirit of These integrals are called _improper integrals_ and are limits of integrals rather than integrals themselves.