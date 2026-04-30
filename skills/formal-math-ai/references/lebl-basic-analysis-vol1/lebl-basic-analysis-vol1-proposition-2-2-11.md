Proposition 2.2.11

**Proposition 2.2.11.** _Let 𝑐 >_ 0 _._

**==> picture [83 x 13] intentionally omitted <==**

**==> picture [61 x 18] intentionally omitted <==**

**==> picture [200 x 14] intentionally omitted <==**

_Proof._ First consider _𝑐 <_ 1. As _𝑐 >_ 0, then _𝑐[𝑛] >_ 0 for all _𝑛_ ∈ ℕ by . As _𝑐 <_ 1, then _𝑐[𝑛]_[+][1] _< 𝑐[𝑛]_ for all _𝑛_ . So { _𝑐[𝑛]_ }[∞] _𝑛_ =1[is a decreasing sequence that is bounded below.][Hence, it is] convergent. Let _𝑥_ � lim _𝑛_ →∞ _𝑐[𝑛]_ . The 1-tail { _𝑐[𝑛]_[+][1] }[∞] _𝑛_ =1[also converges to] _[ 𝑥]_[.][Taking the limit] of both sides of _𝑐[𝑛]_[+][1] = _𝑐_ · _𝑐[𝑛]_ , we obtain _𝑥_ = _𝑐𝑥_ , or (1 − _𝑐_ ) _𝑥_ = 0. It follows that _𝑥_ = 0 as _𝑐_ ≠ 1. Now consider _𝑐 >_ 1. Let _𝐵 >_ 0 be arbitrary. As[1] / _𝑐 <_ 1, then �([1] / _𝑐_ ) _[𝑛]_[�][∞] _𝑛_ =1[converges to][ 0][.] Hence for some large enough _𝑛_ , we get

**==> picture [84 x 32] intentionally omitted <==**

In other words, _𝑐[𝑛] > 𝐵_ , and _𝐵_ is not an upper bound for { _𝑐[𝑛]_ }[∞] _𝑛_ =1[.][As] _[𝐵]_[was][arbitrary,] { _𝑐[𝑛]_ }[∞] _𝑛_ =1[is unbounded.] □

In the proposition above, the ratio of the ( _𝑛_ + 1)th term and the _𝑛_ th term is _𝑐_ . We generalize this simple result to a larger class of sequences. The following lemma will come up again once we get to series.

_2.2. FACTS ABOUT LIMITS OF SEQUENCES_

69

**Lemma 2.2.12** (Ratio test for sequences) **.** _Let_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[be a sequence such that][ 𝑥][𝑛]_[≠][0] _[ for all][ 𝑛] and such that the limit_

**==> picture [293 x 76] intentionally omitted <==**

If _𝐿_ exists, but _𝐿_ = 1, the lemma says nothing. We cannot make any conclusion based on that information alone. For example, the sequence {[1] / _𝑛_ }[∞] _𝑛_ =1[converges to zero, but] _[ 𝐿]_[=][ 1][.] The constant sequence {1}[∞] _𝑛_ =1[converges to 1, not zero, and] _[ 𝐿]_[=][ 1][.][The sequence] �(−1) _[𝑛]_[�][∞] _𝑛_ =1 does not converge at all, and _𝐿_ = 1 as well. Finally, the sequence { _𝑛_ }[∞] _𝑛_ =1[is unbounded, yet] _𝐿_ = 1. again The statement of the lemma may be strengthened somewhat, see exercises and .

_Proof._ Suppose _𝐿 <_ 1. As[|] _[𝑥]_ | _𝑥[𝑛] 𝑛_[+] |[1][|][≥][0][ for all] _[ 𝑛]_[, then] _[ 𝐿]_[≥][0][.][Pick] _[ 𝑟]_[such that] _[ 𝐿][<][𝑟][<]_[1][.][We] wish to compare the sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[to the sequence][ {] _[𝑟][𝑛]_[}][∞] _𝑛_ =1[.][The idea is that while the] ratio[|] _[𝑥]_ | _𝑥[𝑛] 𝑛_[+] |[1][|][is not going to be less than] _[ 𝐿]_[eventually, it will eventually be less than] _[ 𝑟]_[, which] is still less than 1. The intuitive idea of the proof is illustrated in .

**==> picture [154 x 30] intentionally omitted <==**

**Figure 2.4:** The short lines represent the ratios[|] _[𝑥]_ | _𝑥[𝑛] 𝑛_[+] |[1][|][approaching] _[ 𝐿][<]_[1.]

As _𝑟_ − _𝐿 >_ 0, there exists an _𝑀_ ∈ ℕ such that for all _𝑛_ ≥ _𝑀_ , we have

**==> picture [104 x 31] intentionally omitted <==**

Therefore, for _𝑛_ ≥ _𝑀_ ,

**==> picture [209 x 28] intentionally omitted <==**

For _𝑛 > 𝑀_ (that is for _𝑛_ ≥ _𝑀_ + 1) write

**==> picture [408 x 28] intentionally omitted <==**

The sequence { _𝑟[𝑛]_ }[∞] _𝑛_ =1[converges][to][zero][and][hence][|] _[𝑥][𝑀]_[|] _[ 𝑟]_[−] _[𝑀][𝑟][𝑛]_[converges][to][zero.][By] , the _𝑀_ -tail { _𝑥𝑛_ }[∞] _𝑛_ = _𝑀_ +1[converges to zero and therefore][ {] _[𝑥][𝑛]_[}][∞] _𝑛_ =1[converges] to zero.

_CHAPTER 2. SEQUENCES AND SERIES_

70

Now suppose _𝐿 >_ 1. Pick _𝑟_ such that 1 _< 𝑟 < 𝐿_ . As _𝐿_ − _𝑟 >_ 0, there exists an _𝑀_ ∈ ℕ such that for all _𝑛_ ≥ _𝑀_

Therefore,

**==> picture [104 x 80] intentionally omitted <==**

Again for _𝑛 > 𝑀_ , write

**==> picture [408 x 29] intentionally omitted <==**

The sequence { _𝑟[𝑛]_ }[∞] _𝑛_ =1[is unbounded (since] _[ 𝑟][>]_[1][), and so][ {] _[𝑥][𝑛]_[}][∞] _𝑛_ =1[cannot be bounded (if] _𝐵_ | _𝑥𝑛_ | ≤ _𝐵_ for all _𝑛_ , then _𝑟[𝑛] <_ | _𝑥𝑀_ | _[𝑟][𝑀]_[for all] _[𝑛][>][𝑀]_[,][which is impossible).][Consequently,] { _𝑥𝑛_ }[∞] _𝑛_ =1[cannot converge.] □