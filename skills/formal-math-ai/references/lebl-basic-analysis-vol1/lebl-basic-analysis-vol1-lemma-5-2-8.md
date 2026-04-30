Lemma 5.2.8

**Lemma 5.2.8.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a bounded function,_ { _𝑎𝑛_ }[∞] _𝑛_ =1 _[and]_[{] _[𝑏][𝑛]_[}][∞] _𝑛_ =1 _[be][sequences] such that 𝑎 < 𝑎𝑛 < 𝑏𝑛 < 𝑏 for all 𝑛, with_ lim _𝑛_ →∞ _𝑎𝑛_ = _𝑎 and_ lim _𝑛_ →∞ _𝑏𝑛_ = _𝑏. Suppose 𝑓_ ∈ _R_[�] [ _𝑎𝑛 , 𝑏𝑛_ ][�] _for all 𝑛. Then 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _and_

**==> picture [106 x 34] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

196

**==> picture [414 x 56] intentionally omitted <==**

Therefore, the sequence of numbers �∫ _𝑎𝑏𝑛𝑛[𝑓]_ �∞ _𝑛_ =1[is bounded and by] has a convergent subsequence indexed by _𝑛𝑘_ . Let us call _𝐿_ the limit of the subsequence _𝑏_ ∞ �∫ _𝑎𝑛𝑘𝑛𝑘 𝑓_ � _𝑘_ =1[.] says that the lower and upper integral are additive and the hypothesis says that _𝑓_ is integrable on [ _𝑎𝑛𝑘 , 𝑏𝑛𝑘_ ]. Therefore

**==> picture [375 x 36] intentionally omitted <==**

We take the limit as _𝑘_ goes to ∞ on the right-hand side,

**==> picture [367 x 100] intentionally omitted <==**

Next we use additivity of the upper integral,

_𝑏_ We take the same subsequence {∫ _𝑎𝑛𝑘𝑛𝑘 𝑓_ }[∞] _𝑘_ =1[and take the limit to obtain]

**==> picture [156 x 32] intentionally omitted <==**

_𝑏 𝑏 𝑏_ Thus ∫ _𝑎[𝑓]_[=] ∫ _𝑎 𝑓_ = _𝐿_ and hence _𝑓_ is Riemann integrable and ∫ _𝑎[𝑓]_[=] _[𝐿]_[.][In particular, no] matter what subsequence we chose, the _𝐿_ is the same number.

. We have shown that To prove the final statement of the lemma we use _𝑏_ ∞ _𝑏_ every convergent subsequence �∫ _𝑎𝑛𝑘𝑛𝑘 𝑓_ � _𝑘_ =1[converges to] _[ 𝐿]_[=] ∫ _𝑎[𝑓]_[.][Therefore, the sequence] _𝑏𝑛_ ∞ _𝑏_ □ �∫ _𝑎𝑛[𝑓]_ � _𝑛_ =1[is convergent and converges to] ∫ _𝑎[𝑓]_[.]

We say a function _𝑓_ : [ _𝑎, 𝑏_ ] → ℝ has _finitely many discontinuities_ if there exists a finite set _𝑆_ = { _𝑥_ 1 _, 𝑥_ 2 _, . . . , 𝑥𝑛_ } ⊂[ _𝑎, 𝑏_ ], and _𝑓_ is continuous at all points of [ _𝑎, 𝑏_ ] \ _𝑆_ .