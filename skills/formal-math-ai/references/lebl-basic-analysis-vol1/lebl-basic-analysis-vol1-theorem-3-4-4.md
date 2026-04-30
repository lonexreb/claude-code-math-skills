Theorem 3.4.4

**Theorem 3.4.4.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function. Then 𝑓 is uniformly continuous._

_Proof._ We prove the statement by contrapositive. Suppose _𝑓_ is not uniformly continuous. We will prove that there is some _𝑐_ ∈[ _𝑎, 𝑏_ ] where _𝑓_ is not continuous. Let us negate the definition of uniformly continuous. There exists an _𝜖>_ 0 such that for every _𝛿>_ 0, there exist points _𝑥, 𝑦_ in [ _𝑎, 𝑏_ ] with �� _𝑥_ − _𝑦_ �� _< 𝛿_ and �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� ≥ _𝜖_ . So for the _𝜖>_ 0 above, we find sequences { _𝑥𝑛_ }[∞] _𝑛_ =1[and][ {] _[𝑦][𝑛]_[}][∞] _𝑛_ =1[such that] �� _𝑥𝑛_ − _𝑦𝑛_ �� _<_ 1/ _𝑛_ and such that �� _𝑓_ ( _𝑥𝑛_ ) − _𝑓_ ( _𝑦𝑛_ )�� ≥ _𝜖_ . By , there exists a convergent subsequence { _𝑥𝑛𝑘_ }[∞] _𝑘_ =1[.][Let] _[𝑐]_[�][lim] _[𝑘]_[→∞] _[𝑥][𝑛][𝑘]_[.][As] _[𝑎]_[≤] _[𝑥][𝑛][𝑘]_[≤] _[𝑏]_[for all] _[𝑘]_[, we have] _[𝑎]_[≤] _[𝑐]_[≤] _[𝑏]_[.] Estimate

**==> picture [377 x 13] intentionally omitted <==**

As[1] / _𝑛𝑘_ and �� _𝑥𝑛𝑘_ − _𝑐_ �� both go to zero when _𝑘_ goes to infinity, { _𝑦𝑛𝑘_ }∞ _𝑘_ =1[converges and the] limit is _𝑐_ . We now show that _𝑓_ is not continuous at _𝑐_ . Estimate

**==> picture [258 x 55] intentionally omitted <==**

Or in other words,

**==> picture [184 x 16] intentionally omitted <==**

At least one of the sequences � _𝑓_ ( _𝑥𝑛𝑘_ )�∞ _𝑘_ =1[or] � _𝑓_ ( _𝑦𝑛𝑘_ )�∞ _𝑘_ =1[cannot converge to] _[𝑓]_[(] _[𝑐]_[)][, otherwise] the left-hand side of the inequality would go to zero while the right-hand side is positive. Thus _𝑓_ cannot be continuous at _𝑐_ . □

As before, note what is key in the proof: We can apply Bolzano–Weierstrass because the interval [ _𝑎, 𝑏_ ] is bounded, and the limit of the subsequence is back in [ _𝑎, 𝑏_ ] because the interval is closed.

## **3.4.2 Continuous extension**

Uniformly continuous functions on open intervals extend continuously to the endpoints. The key is the following lemma, which also has many other uses. It says that uniformly continuous functions preserve Cauchy sequences. The new issue here is that for a Cauchy sequence, the limit may not end up in the domain of the function.