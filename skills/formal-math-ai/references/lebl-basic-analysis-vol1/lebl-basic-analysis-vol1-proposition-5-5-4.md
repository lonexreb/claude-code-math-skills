Proposition 5.5.4

**Proposition 5.5.4.** _Suppose 𝑓_ : [ _𝑎,_ ∞) → ℝ _is nonnegative ( 𝑓_ ( _𝑥_ ) ≥ 0 _for all 𝑥) and 𝑓 is Riemann integrable on_ [ _𝑎, 𝑏_ ] _for all 𝑏 > 𝑎._

_(i)_

**==> picture [156 x 32] intentionally omitted <==**

∞ _(ii) Suppose_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is a sequence with]_[ lim] _[𝑛]_[→∞] _[𝑥][𝑛]_[=][∞] _[.][Then]_ ∫ _𝑎 𝑓 converges if and only if_ lim _𝑛_ →∞ ∫ _𝑎𝑥𝑛 𝑓 exists, in which case_

**==> picture [110 x 30] intentionally omitted <==**

∞ In the first item we allow for the value of in the supremum indicating that the integral diverges to infinity.

_𝑥 Proof._ We start with the first item. As _𝑓_ is nonnegative, ∫ _𝑎[𝑓]_[is increasing as a function of] _𝑁 𝑥_ . If the supremum is infinite, then for every _𝑀_ ∈ ℝ we find _𝑁_ such that ∫ _𝑎 𝑓_ ≥ _𝑀_ . As _𝑥 𝑥_ ∞ ∫ _𝑎[𝑓]_[is increasing,] ∫ _𝑎[𝑓]_[≥] _[𝑀]_[for all] _[ 𝑥]_[≥] _[𝑁]_[.][So] ∫ _𝑎 𝑓_ diverges to infinity.

_CHAPTER 5. THE RIEMANN INTEGRAL_

216

_𝑥_ Next suppose the supremum is finite, say _𝐴_ � sup �∫ _𝑎[𝑓]_[:] _[𝑥]_[≥] _[𝑎]_ �. For every _𝜖>_ 0, we _𝑁 𝑥 𝑥_ find an _𝑁_ such that _𝐴_ − ∫ _𝑎 𝑓 < 𝜖_ . As ∫ _𝑎[𝑓]_[is increasing, then] _[ 𝐴]_[−] ∫ _𝑎[𝑓][<][𝜖]_[for all] _[ 𝑥]_[≥] _[𝑁]_ ∞ and hence ∫ _𝑎 𝑓_ converges to _𝐴_ .

∞ Let us look at the second item. If ∫ _𝑎 𝑓_ converges, then every sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[going] to infinity works. The trick is proving the other direction. Suppose { _𝑥𝑛_ }[∞] _𝑛_ =1[is such that] lim _𝑛_ →∞ _𝑥𝑛_ = ∞ and

**==> picture [84 x 30] intentionally omitted <==**

_𝑥𝑛_ converges. Given _𝜖>_ 0, pick _𝑁_ such that for all _𝑛_ ≥ _𝑁_ , we have _𝐴_ − _𝜖<_ ∫ _𝑎 𝑓 < 𝐴_ + _𝜖_ . _𝑥_ Because ∫ _𝑎[𝑓]_[is increasing as a function of] _[ 𝑥]_[, we have that for all] _[ 𝑥]_[≥] _[𝑥][𝑁]_

**==> picture [128 x 30] intentionally omitted <==**

As { _𝑥𝑛_ }[∞] _𝑛_ =1[goes to][ ∞][, then for any given] _[𝑥]_[, there is an] _[𝑥][𝑚]_[such that] _[ 𝑚]_[≥] _[𝑁]_[and] _[𝑥]_[≤] _[𝑥][𝑚]_[.] Then

**==> picture [469 x 59] intentionally omitted <==**

**Proposition 5.5.5** (Comparison test for improper integrals) **.** _Let 𝑓_ : [ _𝑎,_ ∞) → ℝ _and 𝑔_ : [ _𝑎,_ ∞) → ℝ _be functions that are Riemann integrable on_ [ _𝑎, 𝑏_ ] _for all 𝑏 > 𝑎. Suppose that for all 𝑥_ ≥ _𝑎,_

**==> picture [376 x 68] intentionally omitted <==**

_Proof._ We start with the first item. For every _𝑏_ and _𝑐_ , such that _𝑎_ ≤ _𝑏_ ≤ _𝑐_ , we have − _𝑔_ ( _𝑥_ ) ≤ _𝑓_ ( _𝑥_ ) ≤ _𝑔_ ( _𝑥_ ), and so

**==> picture [130 x 115] intentionally omitted <==**

_𝑐 𝑐_ In other words, ���∫ _𝑏[𝑓]_ ��� ≤ ∫ _𝑏[𝑔]_[.] Let _𝜖>_ 0 be given. Because of ,

_𝑏_ ∞ ∞ As ∫ _𝑎[𝑔]_[goes to] ∫ _𝑎 𝑔_ as _𝑏_ goes to infinity, ∫ _𝑏 𝑔_ goes to 0 as _𝑏_ goes to infinity. Choose _𝐵_ such that

**==> picture [58 x 30] intentionally omitted <==**

_5.5. IMPROPER INTEGRALS_

217

_𝑐_ As _𝑔_ is nonnegative, if _𝐵_ ≤ _𝑏 < 𝑐_ , then ∫ _𝑏[𝑔][<][𝜖]_[as well.][Let][ {] _[𝑥][𝑛]_[}][∞] _𝑛_ =1[be a sequence going] to infinity. Let _𝑀_ be such that _𝑥𝑛_ ≥ _𝐵_ for all _𝑛_ ≥ _𝑀_ . Take _𝑛, 𝑚_ ≥ _𝑀_ , with _𝑥𝑛_ ≤ _𝑥𝑚_ ,

**==> picture [222 x 32] intentionally omitted <==**

Therefore, the sequence �∫ _𝑎𝑥𝑛 𝑓_ �∞ _𝑛_ =1[is Cauchy and hence converges.] We need to show that the limit is unique. Suppose { _𝑥𝑛_ }[∞] _𝑛_ =1[is a sequence converging] to infinity such that �∫ _𝑎𝑥𝑛 𝑓_ �∞ _𝑛_ =1[converges][to] _[𝐿]_[1][,][and][{] _[𝑦][𝑛]_[}][∞] _𝑛_ =1[is][a][sequence][converging] _𝑦𝑛_ ∞ to infinity such that �∫ _𝑎 𝑓_ � _𝑛_ =1[converges][to] _[𝐿]_[2][.][Then][there][must][be][some] _[𝑛]_[such][that] ��∫ _𝑎𝑥𝑛 𝑓_ − _𝐿_ 1�� _< 𝜖_ and ��∫ _𝑎𝑦𝑛 𝑓_ − _𝐿_ 2�� _< 𝜖_ . We can also suppose _𝑥𝑛_ ≥ _𝐵_ and _𝑦𝑛_ ≥ _𝐵_ . Then

**==> picture [430 x 32] intentionally omitted <==**

∞ As _𝜖>_ 0 was arbitrary, _𝐿_ 1 = _𝐿_ 2, and hence ∫ _𝑎 𝑓_ converges. Above we have shown that _𝑐 𝑐_ ≤ _[𝑎]_[.][By taking the limit] _[ 𝑐]_[→∞][, the first item is proved.] ���∫ _𝑎[𝑓]_ ��� ∫ _𝑎[𝑔]_[for all] _[ 𝑐][>]_ □ The second item is simply a contrapositive of the first item.