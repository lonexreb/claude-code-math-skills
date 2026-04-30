Example 5.1.11

**Example 5.1.11:** We integrate constant functions using . If _𝑓_ ( _𝑥_ ) � _𝑐_ for some constant _𝑐_ , then we take _𝑚_ = _𝑀_ = _𝑐_ . In inequality ( ) all the inequalities must be _𝑏_ equalities. Thus _𝑓_ is integrable on [ _𝑎, 𝑏_ ] and ∫ _𝑎[𝑓]_[=] _[𝑐]_[(] _[𝑏]_[−] _[𝑎]_[)][.] **Example 5.1.12:** Let _𝑓_ : [0 _,_ 2] → ℝ be defined by

**==> picture [114 x 54] intentionally omitted <==**

2 We claim _𝑓_ is Riemann integrable and ∫0 _[𝑓]_[=][ 1.] Proof: Let 0 _< 𝜖<_ 1 be arbitrary. Let _𝑃_ � {0 _,_ 1 − _𝜖,_ 1 + _𝜖,_ 2} be a partition. We use the Then notation from the definition of the Darboux sums.

**==> picture [426 x 55] intentionally omitted <==**

Furthermore, Δ _𝑥_ 1 = 1 − _𝜖_ , Δ _𝑥_ 2 = 2 _𝜖_ , and Δ _𝑥_ 3 = 1 − _𝜖_ . See . We compute

**==> picture [316 x 80] intentionally omitted <==**

Thus,

**==> picture [298 x 32] intentionally omitted <==**

_5.1. THE RIEMANN INTEGRAL_

187

**==> picture [333 x 138] intentionally omitted <==**

**----- Start of picture text -----**<br>
푀 1 = 푀 2 =  푚 1 = 1<br>푀 3 =  푚 2 =  푚 3 = 0<br>0 1 − 휖 1 +  휖 2<br>Δ 푥 1 = 1 − 휖 Δ 푥 2 = 2 휖 Δ 푥 3 = 1 − 휖<br>**----- End of picture text -----**<br>


**Figure 5.4:** Darboux sums for the step function. _𝐿_ ( _𝑃, 𝑓_ ) is the area of the shaded rectangle, _𝑈_ ( _𝑃, 𝑓_ ) is the area of both rectangles, and _𝑈_ ( _𝑃, 𝑓_ )− _𝐿_ ( _𝑃, 𝑓_ ) is the area of the unshaded rectangle.

2 2 2 2 By , ∫0 _𝑓_ ≤ ∫0 _[𝑓]_[.][As] _[𝜖]_[was][arbitrary,] ∫0 _[𝑓]_[=] ∫0 _𝑓_ . So _𝑓_ is Riemann integrable. Finally,

**==> picture [220 x 32] intentionally omitted <==**

2 2 Hence, ��∫0 _[𝑓]_[−][1] �� ≤ _𝜖_ . As _𝜖_ was arbitrary, we conclude ∫0 _[𝑓]_[=][ 1.] It may be worthwhile to extract part of the technique of the example into a proposition. Note that _𝑈_ ( _𝑃, 𝑓_ ) − _𝐿_ ( _𝑃, 𝑓_ ) is exactly the total area of the white part of the rectangles in .