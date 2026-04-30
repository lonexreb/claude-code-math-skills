Theorem 5.3.1

**Theorem 5.3.1.** _Let 𝐹_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function, differentiable on_ ( _𝑎, 𝑏_ ) _. Let 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _be such that 𝑓_ ( _𝑥_ ) = _𝐹_[′] ( _𝑥_ ) _for 𝑥_ ∈( _𝑎, 𝑏_ ) _. Then_

**==> picture [106 x 32] intentionally omitted <==**

It is not hard to generalize the theorem to allow a finite number of points in [ _𝑎, 𝑏_ ] where _𝐹_ is not differentiable, as long as it is continuous. This generalization is left as an exercise.

_Proof._ Let _𝑃_ = { _𝑥_ 0 _, 𝑥_ 1 _, . . . , 𝑥𝑛_ } be a partition of [ _𝑎, 𝑏_ ]. For each interval [ _𝑥𝑖_ −1 _, 𝑥𝑖_ ], use the to find a _𝑐𝑖_ ∈( _𝑥𝑖_ −1 _, 𝑥𝑖_ ) such that

**==> picture [231 x 14] intentionally omitted <==**

See , and notice that the area of the _𝑖_ th rectangle is _𝐹_ ( _𝑥𝑖_ +1) − _𝐹_ ( _𝑥𝑖_ −2) for all three rectangles. The idea is that by taking smaller and smaller subintervals we prove that this . area is the integral of _𝑓_

**==> picture [431 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
푓 ( 푐푖 −1) 푦 = 푓 ( 푥 ) =  퐹 [′] ( 푥 )<br>area = 푓 ( 푐푖 +1)Δ 푥푖 +1<br>푓 ( 푐푖 ) = 퐹 ( 푥푖 +1) − 퐹 ( 푥푖 )<br>area = 푓 ( 푐푖 −1)Δ 푥푖 −1 area = 푓 ( 푐푖 )Δ 푥푖<br>푓 ( 푐푖 +1) = 퐹 ( 푥푖 −1) − 퐹 ( 푥푖 −2) = 퐹 ( 푥푖 ) − 퐹 ( 푥푖 −1)<br>푥푖 −2 푐푖 −1 푥푖 −1 푐푖 푥푖 푐푖 +1 푥푖 +1<br>Δ 푥푖 −1 Δ 푥푖 Δ 푥푖 +1<br>**----- End of picture text -----**<br>


**Figure 5.5:** Mean value theorem on subintervals of a partition approximating the area under the curve.

_5.3. FUNDAMENTAL THEOREM OF CALCULUS_

201

Using the notation from the definition of the integral, _𝑚𝑖_ ≤ _𝑓_ ( _𝑐𝑖_ ) ≤ _𝑀𝑖_ , and multiplying by Δ _𝑥𝑖_ gets

**==> picture [176 x 12] intentionally omitted <==**

We sum over _𝑖_ = 1 _,_ 2 _, . . . , 𝑛_ to get

**==> picture [240 x 36] intentionally omitted <==**

In the middle sum, all the terms except the first and last cancel and we end up with _𝐹_ ( _𝑥𝑛_ ) − _𝐹_ ( _𝑥_ 0) = _𝐹_ ( _𝑏_ ) − _𝐹_ ( _𝑎_ ). The sums on the left and on the right are the lower and the upper sum respectively. So

**==> picture [168 x 14] intentionally omitted <==**

We take the supremum of _𝐿_ ( _𝑃, 𝑓_ ) over all partitions _𝑃_ and the left inequality yields

**==> picture [104 x 32] intentionally omitted <==**

Similarly, taking the infimum of _𝑈_ ( _𝑃, 𝑓_ ) over all partitions _𝑃_ yields

**==> picture [104 x 32] intentionally omitted <==**

As _𝑓_ is Riemann integrable, we have

**==> picture [234 x 32] intentionally omitted <==**

The inequalities must be equalities and we are done.

**==> picture [10 x 7] intentionally omitted <==**

The theorem is used to compute integrals. Suppose we know that the function _𝑓_ ( _𝑥_ ) is a _𝑏_ derivative of some other function _𝐹_ ( _𝑥_ ), then we can find an explicit expression for ∫ _𝑎[𝑓]_[.]

## **Example 5.3.2:** To compute

**==> picture [53 x 32] intentionally omitted <==**

we notice _𝑥_[2] is the derivative of _[𝑥]_[3][The fundamental theorem says] 3[.]

**==> picture [130 x 33] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

202

## **5.3.2 Second form of the theorem**

The second form of the fundamental theorem gives us a way to solve the differential equation _𝐹_[′] ( _𝑥_ ) = _𝑓_ ( _𝑥_ ), where _𝑓_ is a known function and we are trying to find an _𝐹_ that satisfies the equation.