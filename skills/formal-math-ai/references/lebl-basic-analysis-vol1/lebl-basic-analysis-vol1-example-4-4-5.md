Example 4.4.5

**Example 4.4.5:** Another useful example is _𝑓_ ( _𝑥_ ) � _𝑥_[3] . The function _𝑓_ : ℝ → ℝ is one-to-one and onto, so _𝑓_[−][1] ( _𝑦_ ) = _𝑦_[1][/][3] exists on the entire real line, including zero and negative _𝑦_ . The function _𝑓_ has a continuous derivative, but _𝑓_[−][1] has no derivative at the origin. The point is that _𝑓_[′] (0) = 0. See for a graph. Notice the vertical tangent on the cube root at the origin. See also .

**==> picture [70 x 35] intentionally omitted <==**

**----- Start of picture text -----**<br>
= 푥 [3]<br>푦<br>= 푥 [1][/][3]<br>푦<br>**----- End of picture text -----**<br>


**Figure 4.11:** Graphs of _𝑥_[3] and _𝑥_[1][/][3] .

## **4.4.2 Exercises**

_**Exercise**_ **4.4.1** _**:** Suppose 𝑓_ : ℝ → ℝ _is continuously differentiable and 𝑓_[′] ( _𝑥_ ) _>_ 0 _for all 𝑥. Show that 𝑓_ ′ _is invertible on the interval 𝐽_ = _𝑓_ (ℝ) _, the inverse is continuously differentiable, and_ ( _𝑓_[−][1] ) ( _𝑦_ ) _>_ 0 _for all 𝑦_ ∈ _𝑓_ (ℝ) _._

179

## _4.4. INVERSE FUNCTION THEOREM_

_**Exercise**_ **4.4.2** _**:** Suppose 𝐼, 𝐽 are intervals and a monotone onto 𝑓_ : _𝐼_ → _𝐽 has an inverse 𝑔_ : _𝐽_ → _𝐼. Suppose you already know that both 𝑓 and 𝑔 are differentiable everywhere and 𝑓_[′] _is never zero. Using chain rule but_ 1 _not , prove the formula 𝑔_[′] ( _𝑦_ ) = _[Remark:][This exercise is the same as] , 𝑓_[′] ( _𝑔_ ( _𝑦_ )) _[.] no need to do it again if you have solved it already._

_**Exercise**_ **4.4.3** _**:** Let 𝑛_ ∈ ℕ _be even. Prove that every 𝑥 >_ 0 _has a unique negative 𝑛th root. That is, there exists a negative number 𝑦 such that 𝑦[𝑛]_ = _𝑥. Compute the derivative of the function 𝑔_ ( _𝑥_ ) � _𝑦._

_**Exercise**_ **4.4.4** _**:** Let 𝑛_ ∈ ℕ _be odd and 𝑛_ ≥ 3 _. Prove that every 𝑥 has a unique 𝑛th root. That is, there exists a number 𝑦 such that 𝑦[𝑛]_ = _𝑥. Prove that the function defined by 𝑔_ ( _𝑥_ ) � _𝑦 is differentiable except at 𝑥_ = 0 _and compute the derivative. Prove that 𝑔 is not differentiable at 𝑥_ = 0 _._

_**Exercise**_ **4.4.5** (requires ) _**:** Show that if in the inverse function theorem 𝑓 has 𝑘 continuous derivatives, then the inverse function 𝑔 also has 𝑘 continuous derivatives._

_**Exercise**_ **4.4.6** _**:** Let 𝑓_ ( _𝑥_ ) � _𝑥_ + 2 _𝑥_[2] sin([1] / _𝑥_ ) _for 𝑥_ ≠ 0 _and 𝑓_ (0) � 0 _. Show that 𝑓 is differentiable at all 𝑥, that 𝑓_[′] (0) _>_ 0 _, but that 𝑓 is not invertible on any open interval containing the origin._

## _**Exercise**_ **4.4.7** _**:**_

- _a) Let 𝑓_ : ℝ → ℝ _be a continuously differentiable function and 𝑘 >_ 0 _be a number such that 𝑓_[′] ( _𝑥_ ) ≥ _𝑘 for all 𝑥_ ∈ ℝ _. Show 𝑓 is one-to-one and onto, and has a continuously differentiable inverse 𝑓_[−][1] : ℝ → ℝ _._

- _b) Find an example 𝑓_ : ℝ → ℝ _where 𝑓_[′] ( _𝑥_ ) _>_ 0 _for all 𝑥, but 𝑓 is not onto._

- _**Exercise**_ **4.4.8** _**:** Suppose 𝐼, 𝐽 are intervals and a monotone onto 𝑓_ : _𝐼_ → _𝐽 has an inverse 𝑔_ : _𝐽_ → _𝐼. Suppose 𝑥_ ∈ _𝐼 and 𝑦_ � _𝑓_ ( _𝑥_ ) ∈ _𝐽, and that 𝑔 is differentiable at 𝑦. Prove:_

- _a) If 𝑔_[′] ( _𝑦_ ) ≠ 0 _, then 𝑓 is differentiable at 𝑥._

- _b) If 𝑔_[′] ( _𝑦_ ) = 0 _, then 𝑓 is not differentiable at 𝑥._

_CHAPTER 4. THE DERIVATIVE_

180

## **Chapter 5**

## **The Riemann Integral**

## **5.1 The Riemann integral**

## _Note: 1.5 lectures_

An integral is a way to “sum” the values of a function. There is sometimes confusion among students of calculus between the _integral_ and the _antiderivative_ . The integral is (informally) the area under the curve, nothing else. That we can compute an antiderivative using the integral is a nontrivial result we must prove. We will define the _Riemann integral_ using the Darboux integral , an equivalent but technically simpler definition.

## **5.1.1 Partitions and lower and upper integrals**

We want to integrate a bounded function defined on an interval [ _𝑎, 𝑏_ ]. We first define two auxiliary integrals that are defined for all bounded functions. Only then can we talk about the Riemann integral and the functions which it can integrate, the Riemann integrable functions.