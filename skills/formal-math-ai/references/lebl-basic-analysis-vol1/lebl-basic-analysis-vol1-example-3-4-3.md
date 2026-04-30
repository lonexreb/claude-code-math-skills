Example 3.4.3

**Example 3.4.3:** The function _𝑓_ : (0 _,_ 1) → ℝ defined by _𝑓_ ( _𝑥_ ) �[1] / _𝑥_ is not uniformly continuous.

Proof: Given _𝜖>_ 0, then _𝜖>_ |[1] / _𝑥_ −[1] / _𝑦_ | holds if and only if

**==> picture [173 x 37] intentionally omitted <==**

or

�� _𝑥_ − _𝑦_ �� _< 𝑥𝑦𝜖._

Suppose _𝜖<_ 1, and we wish to see if a small _𝛿>_ 0 would work. If _𝑥_ ∈(0 _,_ 1) and _𝑦_ = _𝑥_ + _[𝛿]_ /2 ∈(0 _,_ 1), then �� _𝑥_ − _𝑦_ �� = _𝛿_ /2 _< 𝛿_ . We plug _𝑦_ into the inequality above to get _𝛿_ /2 _< 𝑥_[�] _𝑥_ + _[𝛿]_ /2[�] _𝜖< 𝑥_ . If the definition of uniform continuity is satisfied, then the inequality _𝛿_ /2 _< 𝑥_ holds for all _𝑥 >_ 0. But then _𝛿_ ≤ 0. Therefore, no single _𝛿>_ 0 works for all points.

_3.4. UNIFORM CONTINUITY_

139

The examples show that if _𝑓_ is defined on an interval that is either not closed or not bounded, then _𝑓_ can be continuous, but not uniformly continuous. For a closed and bounded interval [ _𝑎, 𝑏_ ], we can, however, make the following statement.