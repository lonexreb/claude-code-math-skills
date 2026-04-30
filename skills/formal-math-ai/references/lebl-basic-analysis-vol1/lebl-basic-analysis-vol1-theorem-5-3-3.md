Theorem 5.3.3

**Theorem 5.3.3.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a Riemann integrable function. Define_

**==> picture [74 x 30] intentionally omitted <==**

_First, 𝐹 is continuous on_ [ _𝑎, 𝑏_ ] _. Second, if 𝑓 is continuous at 𝑐_ ∈[ _𝑎, 𝑏_ ] _, then 𝐹 is differentiable at 𝑐 and 𝐹_[′] ( _𝑐_ ) = _𝑓_ ( _𝑐_ ) _._

_Proof._ As _𝑓_ is bounded, there is an _𝑀 >_ 0 such that �� _𝑓_ ( _𝑥_ )�� ≤ _𝑀_ for all _𝑥_ ∈[ _𝑎, 𝑏_ ]. Suppose _𝑥, 𝑦_ ∈[ _𝑎, 𝑏_ ] with _𝑥 > 𝑦_ . Then

**==> picture [278 x 39] intentionally omitted <==**

By symmetry, the same also holds if _𝑥 < 𝑦_ . So _𝐹_ is Lipschitz continuous and hence continuous.

Now suppose _𝑓_ is continuous at _𝑐_ . Let _𝜖>_ 0 be given. Let _𝛿>_ 0 be such that for _𝑥_ ∈[ _𝑎, 𝑏_ ], | _𝑥_ − _𝑐_ | _< 𝛿_ implies �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ )�� _< 𝜖_ . In particular, for such _𝑥_ , we have

**==> picture [137 x 14] intentionally omitted <==**

Thus if _𝑥 > 𝑐_ , then

**==> picture [234 x 30] intentionally omitted <==**

When _𝑐 > 𝑥_ , then the inequalities are reversed. Therefore, assuming _𝑥_ ≠ _𝑐_ , we get

**==> picture [144 x 32] intentionally omitted <==**

As

**==> picture [326 x 114] intentionally omitted <==**

we have

The result follows. It is left to the reader to see why is it OK that we just have a non-strict inequality. □

_5.3. FUNDAMENTAL THEOREM OF CALCULUS_

203

Of course, if _𝑓_ is continuous on [ _𝑎, 𝑏_ ], then it is automatically Riemann integrable, _𝐹_ is differentiable on all of [ _𝑎, 𝑏_ ] and _𝐹_[′] ( _𝑥_ ) = _𝑓_ ( _𝑥_ ) for all _𝑥_ ∈[ _𝑎, 𝑏_ ].

_Remark_ 5.3.4 _._ The second form of the fundamental theorem of calculus still holds if we let _𝑑_ ∈[ _𝑎, 𝑏_ ] and define

**==> picture [74 x 30] intentionally omitted <==**

That is, we can use any point of [ _𝑎, 𝑏_ ] as our base point. The proof is left as an exercise.

Let us look at what a simple discontinuity can do. Take _𝑓_ ( _𝑥_ ) � −1 if _𝑥 <_ 0, and _𝑥 𝑓_ ( _𝑥_ ) � 1 if _𝑥_ ≥ 0. Let _𝐹_ ( _𝑥_ ) � ∫0 _[𝑓]_[.][It is not difficult to see that] _[ 𝐹]_[(] _[𝑥]_[)][ =][ |] _[𝑥]_[|][.][Notice that] _[𝑓]_[is] discontinuous at 0 and _𝐹_ is not differentiable at 0. However, the converse in the theorem _𝑥_ does not hold. Let _𝑔_ ( _𝑥_ ) � 0 if _𝑥_ ≠ 0, and _𝑔_ (0) � 1. Letting _𝐺_ ( _𝑥_ ) � ∫0 _[𝑔]_[,][we find that] _𝐺_ ( _𝑥_ ) = 0 for all _𝑥_ . So _𝑔_ is discontinuous at 0, but _𝐺_[′] (0) exists and is equal to 0. A common misunderstanding of the integral for calculus students is to think of integrals This is not the case. whose solution cannot be given in closed-form as somehow deficient. Most integrals we write down are not computable in closed-form. Even some integrals that we consider in closed-form are not really such. We define the natural logarithm as the antiderivative of[1] / _𝑥_ such that ln 1 = 0:

**==> picture [86 x 30] intentionally omitted <==**

ln _𝑥_ ? How does a computer find the value of One way to do it is to numerically approximate this integral. Morally, we did not really “simplify” ∫1 _𝑥_ 1 _𝑠[𝑑𝑠]_[by][writing][down][ln] _[ 𝑥]_[.][We] simply gave the integral a name. If we require numerical answers, it is possible we end up doing the calculation by approximating an integral anyway. In the next section, we even define the exponential using the logarithm, which we define in terms of the integral.

Another common function defined by an integral that cannot be evaluated symbolically in terms of elementary functions is the erf function, defined as

**==> picture [130 x 32] intentionally omitted <==**

This function comes up often in applied mathematics. It is simply the antiderivative of ([2] / ~~[√]~~ _𝜋_ ) _𝑒_[−] _[𝑥]_[2] that is zero at zero. The second form of the fundamental theorem tells us that we can write the function as an integral. If we wish to compute any particular value, we numerically approximate the integral.

## **5.3.3 Change of variables**

A theorem often used in calculus to solve integrals is the change of variables theorem, you may have called it _𝑢-substitution_ . Let us prove it now. Recall a function is continuously differentiable if it is differentiable and the derivative is continuous.

_CHAPTER 5. THE RIEMANN INTEGRAL_

204

**Theorem 5.3.5** (Change of variables) **.** _Let 𝑔_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuously differentiable function, let 𝑓_ : [ _𝑐, 𝑑_ ] → ℝ _be continuous, and suppose 𝑔_[�] [ _𝑎, 𝑏_ ][�] ⊂[ _𝑐, 𝑑_ ] _. Then_

**==> picture [192 x 34] intentionally omitted <==**

> _Proof._ As _𝑔_ , _𝑔_[′] , and _𝑓_ are continuous, _𝑓_[�] _𝑔_ ( _𝑥_ )[�] _𝑔_[′] ( _𝑥_ ) is a continuous function of [ _𝑎, 𝑏_ ], therefore it is Riemann integrable. Similarly, _𝑓_ is integrable on every subinterval of [ _𝑐, 𝑑_ ]. Define _𝐹_ : [ _𝑐, 𝑑_ ] → ℝ by

**==> picture [106 x 33] intentionally omitted <==**

By the second form of the fundamental theorem of calculus (see and ), _𝐹_ is a differentiable function and _𝐹_[′] ( _𝑦_ ) = _𝑓_ ( _𝑦_ ). Apply the chain rule, � _𝐹_ ◦ _𝑔_[�][′] ( _𝑥_ ) = _𝐹_[′][�] _𝑔_ ( _𝑥_ )[�] _𝑔_[′] ( _𝑥_ ) = _𝑓_[�] _𝑔_ ( _𝑥_ )[�] _𝑔_[′] ( _𝑥_ ) _._ Note that _𝐹_[�] _𝑔_ ( _𝑎_ )[�] = 0 and use the first form of the fundamental theorem to obtain

**==> picture [424 x 70] intentionally omitted <==**

The change of variables theorem is often used to solve integrals by changing them to integrals that we know or that we can solve using the fundamental theorem of calculus. **Example 5.3.6:** The derivative of sin( _𝑥_ ) is cos( _𝑥_ ). Using _𝑔_ ( _𝑥_ ) � _𝑥_[2] , we solve

**==> picture [386 x 33] intentionally omitted <==**

However, beware that we must satisfy the hypotheses of the theorem. The following example demonstrates why we should not just move symbols around mindlessly. We must be careful that those symbols really make sense.