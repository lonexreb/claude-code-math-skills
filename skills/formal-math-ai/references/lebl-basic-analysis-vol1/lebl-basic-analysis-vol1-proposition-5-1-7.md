Proposition 5.1.7

**Proposition 5.1.7.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a bounded function, and let 𝑃 be a partition of_ [ _𝑎, 𝑏_ ] _. Let 𝑃_[�] _be a refinement of 𝑃. Then_

**==> picture [252 x 16] intentionally omitted <==**

� _Proof._ The tricky part of this proof is to get the notation correct. Let _𝑃_[�] = { _𝑥_ 0 _,_ � _𝑥_ 1 _, . . . ,_ � _𝑥ℓ_ } be a refinement of _𝑃_ = { _𝑥_ 0 _, 𝑥_ 1 _, . . . , 𝑥𝑛_ }. Then _𝑥_ 0 = � _𝑥_ 0 and _𝑥𝑛_ = � _𝑥ℓ_ . In fact, there are integers _𝑘_ 0 _< 𝑘_ 1 _<_ · · · _< 𝑘𝑛_ such that _𝑥𝑖_ = � _𝑥𝑘𝑖_ for _𝑖_ = 0 _,_ 1 _,_ 2 _, . . . , 𝑛_ .

� � � Let Δ _𝑥𝑞_ � _𝑥𝑞_ − _𝑥𝑞_ −1 for _𝑞_ = 0 _,_ 1 _,_ 2 _, . . . , ℓ_ . See . We get

**==> picture [320 x 40] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

184

**==> picture [332 x 75] intentionally omitted <==**

� � � **Figure 5.2:** Refinement of a subinterval. Notice Δ _𝑥𝑖_ = Δ _𝑥𝑞_ −2+Δ _𝑥𝑞_ −1+Δ _𝑥𝑞_ , and also _𝑘𝑖_ −1+1 = _𝑞_ −2 and _𝑘𝑖_ = _𝑞_ .

� Let _𝑚𝑖_ be as before and correspond to the partition _𝑃_ . Let _𝑚𝑞_ � inf� _𝑓_ ( _𝑥_ ) : � _𝑥𝑞_ −1 ≤ _𝑥_ ≤ � � _𝑥𝑞_ �. Now, _𝑚𝑖_ ≤ _𝑚𝑞_ for _𝑘𝑖_ −1 _< 𝑞_ ≤ _𝑘𝑖_ . Therefore,

**==> picture [300 x 41] intentionally omitted <==**

So

**==> picture [401 x 60] intentionally omitted <==**

The proof of _𝑈_ ( _𝑃,_[�] _𝑓_ ) ≤ _𝑈_ ( _𝑃, 𝑓_ ) is left as an exercise.

Armed with refinements, we prove the following. The key point of this next proposition is that the lower Darboux integral is less than or equal to the upper Darboux integral.