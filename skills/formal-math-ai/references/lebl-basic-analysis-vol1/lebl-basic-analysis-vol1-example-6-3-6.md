Example 6.3.6

**Example 6.3.6:** Consider _𝑦_[′] = _𝜑_ ( _𝑥_ ) where _𝜑_ ( _𝑥_ ) � 0 if _𝑥_ ∈ ℚ and _𝜑_ ( _𝑥_ ) � 1 if _𝑥_ ∉ ℚ. In other words, the _𝐹_ ( _𝑥, 𝑦_ ) = _𝜑_ ( _𝑥_ ) is discontinuous. The equation has no solution regardless of the initial conditions. A solution would have derivative _𝜑_ , but _𝜑_ does not have the . intermediate value property at any point (why?). No solution exists by

The examples show that without the Lipschitz condition, a solution might exist but not be unique, and without continuity of _𝐹_ , we may not have a solution at all. It is in fact a theorem, the Peano existence theorem, that if _𝐹_ is continuous a solution exists (but may not be unique).

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

252

” _Remark_ 6.3.7 _._ It is possible to weaken what we mean by “solution to _𝑦_[′] = _𝐹_ ( _𝑥, 𝑦_ ) by _𝑥_ focusing on the integral equation _𝑓_ ( _𝑥_ ) = _𝑦_ 0 + ∫ _𝑥_ 0 _[𝐹]_[�] _𝑡, 𝑓_ ( _𝑡_ )[�] _𝑑𝑡_ . For example, let _𝐻_ be the Heaviside function , that is _𝐻_ ( _𝑥_ ) � 0 for _𝑥 <_ 0 and _𝐻_ ( _𝑥_ ) � 1 for _𝑥_ ≥ 0. Then _𝑦_[′] = _𝐻_ ( _𝑥_ ), _𝑦_ (0) = 0, is a common equation. The “solution” is the ramp function _𝑓_ ( _𝑥_ ) � 0 if _𝑥 <_ 0 _𝑥_ and _𝑓_ ( _𝑥_ ) � _𝑥_ if _𝑥_ ≥ 0, since this function satisfies _𝑓_ ( _𝑥_ ) = ∫0 _[𝐻]_[(] _[𝑡]_[)] _[ 𝑑𝑡]_[.][Notice, however, that] _𝑓_[′] (0) does not exist, so _𝑓_ is only a so-called _weak solution_ to the differential equation.

## **6.3.4 Exercises**

_**Exercise**_ **6.3.1** _**:** Let 𝐼, 𝐽_ ⊂ ℝ _be intervals. Let 𝐹_ : _𝐼_ × _𝐽_ → ℝ _be a continuous function of two variables and suppose 𝑓_ : _𝐼_ → _𝐽 be a continuous function. Show that 𝐹_[�] _𝑥, 𝑓_ ( _𝑥_ )[�] _is a continuous function on 𝐼._

_**Exercise**_ **6.3.2** _**:** Let 𝐼, 𝐽_ ⊂ ℝ _be closed bounded intervals. Show that if 𝐹_ : _𝐼_ × _𝐽_ → ℝ _is continuous, then 𝐹 is bounded._

_**Exercise**_ **6.3.3** _**:** We proved Picard’s theorem under the assumption that 𝑥_ 0 = 0 _. Prove the full statement of Picard’s theorem for an arbitrary 𝑥_ 0 _._

_**Exercise**_ **6.3.4** _**:** Let 𝑓_[′] ( _𝑥_ ) = _𝑥𝑓_ ( _𝑥_ ) _be our equation. Start with the initial condition 𝑓_ (0) = 2 _and find the Picard iterates 𝑓_ 0 _, 𝑓_ 1 _, 𝑓_ 2 _, 𝑓_ 3 _, 𝑓_ 4 _._

_**Exercise**_ **6.3.5** _**:** Suppose 𝐹_ : _𝐼_ × _𝐽_ → ℝ _is a function that is continuous in the first variable, that is, for every fixed 𝑦 the function that takes 𝑥 to 𝐹_ ( _𝑥, 𝑦_ ) _is continuous. Further, suppose 𝐹 is Lipschitz in the second variable, that is, there exists a number 𝐿 such that_

**==> picture [252 x 15] intentionally omitted <==**

_Show that 𝐹 is continuous as a function of two variables. Therefore, the hypotheses in the theorem could be made even weaker._

_**Exercise**_ **6.3.6** _**:** A common type of equation one encounters are_ linear first order differential equations _, that is equations of the form_

**==> picture [160 x 12] intentionally omitted <==**

_Prove Picard’s theorem for linear equations. Suppose 𝐼 is an interval, 𝑥_ 0 ∈ _𝐼, and 𝑝_ : _𝐼_ → ℝ _and 𝑞_ : _𝐼_ → ℝ _are continuous. Show that there exists a unique differentiable 𝑓_ : _𝐼_ → ℝ _, such that 𝑦_ = _𝑓_ ( _𝑥_ ) _satisfies the equation and the initial condition. Hint: Assume existence of the exponential function and use the integrating factor formula for existence of 𝑓 (prove that it works and then that it is unique):_

**==> picture [216 x 30] intentionally omitted <==**

_**Exercise**_ **6.3.7** _**:** Consider the equation 𝑓_[′] ( _𝑥_ ) = _𝑓_ ( _𝑥_ ) _, from . Show that given any 𝑥_ 0 _, any 𝑦_ 0 _, and any positive ℎ <_[1] /2 _, we can pick 𝛼>_ 0 _large enough that the proof of Picard’s theorem guarantees a solution for the initial condition 𝑓_ ( _𝑥_ 0) = _𝑦_ 0 _in the interval_ [ _𝑥_ 0 − _ℎ, 𝑥_ 0 + _ℎ_ ] _._

> ‗Named for the English engineer, mathematician, and physicist (1850–1825).

253

## _6.3. PICARD’S THEOREM_

- _**Exercise**_ **6.3.8** _**:** Consider the equation 𝑦_[′] = _𝑦_[1][/][3] _𝑥._

- _a) Show that for the initial condition 𝑦_ (1) = 1 _, Picard’s theorem applies. Find an 𝛼>_ 0 _, 𝑀, 𝐿, and ℎ that would work in the proof._

- _b) Show that for the initial condition 𝑦_ (1) = 0 _, Picard’s theorem does not apply._

- _c) Find a solution for 𝑦_ (1) = 0 _anyway._

- _**Exercise**_ **6.3.9** _**:** Consider the equation 𝑥𝑦_[′] = 2 _𝑦._

- _a) Show that 𝑦_ = _𝐶𝑥_[2] _is a solution for every constant 𝐶._

- _b) Show that for every 𝑥_ 0 ≠ 0 _and every 𝑦_ 0 _, Picard’s theorem applies for the initial condition 𝑦_ ( _𝑥_ 0) = _𝑦_ 0 _._

- _c) Show that 𝑦_ (0) = _𝑦_ 0 _is solvable if and only if 𝑦_ 0 = 0 _._

# 254 _CHAPTER 6. SEQUENCES OF FUNCTIONS_

## **Chapter 7**

## **Metric Spaces**

## **7.1 Metric spaces**

## _Note: 1.5 lectures_

As mentioned in the introduction, the main idea in analysis is to take limits. In we learned to take limits of sequences of real numbers. And in we learned to take limits of functions as a real number approached some other real number.

We want to take limits in more complicated contexts. For example, we want to have sequences of points in 3-dimensional space. We wish to define continuous functions of several variables. We even want to define functions on spaces that are a little harder to describe, such as the surface of the earth. We still want to talk about limits there.

. Finally, we have seen the limit of a sequence of functions in We wish to unify all these notions so that we do not have to reprove theorems over and over again in each context. The concept of a metric space is an elementary yet powerful tool in analysis. And while it is not sufficient to describe every type of limit we find in modern analysis, it gets us very far indeed.