Example 2.5.18

**Example 2.5.18:** The series[�][∞] _𝑛_ =1 _𝑛_[2] 1+1[converges.]

Proof: First, _𝑛_[2] 1+1 _[<] 𝑛_ 1[2][for all] _[ 𝑛]_[∈][ℕ][.][The series][ �][∞] _𝑛_ =1 _𝑛_ 1[2][converges by the] _[ 𝑝]_[-series test.] Therefore, by the comparison test,[�][∞] _𝑛_ =1 _𝑛_[2] 1+1[converges.]

> ‗Demonstration of this fact is what made the Swiss mathematician (1707–1783) famous.

_CHAPTER 2. SEQUENCES AND SERIES_

96

## **2.5.6 Ratio test**

Suppose _𝑟 >_ 0. The ratio of two subsequent terms in the geometric series[�][∞] _𝑛_ =0 _[𝑟][𝑛]_[is] _[𝑟] 𝑟[𝑛][𝑛]_[+][1][=] _[ 𝑟]_[,] and the series converges whenever _𝑟 <_ 1. Just as for sequences, this fact can be generalized to more arbitrary series as long as we have such a ratio “in the limit.” We then compare the tail of a series to the geometric series.

**Proposition 2.5.19** (Ratio test) **.** _Let_[�][∞] _𝑛_ =1 _[𝑥][𝑛][be a series,][ 𝑥][𝑛]_[≠][0] _[ for all][ 𝑛][, and such that]_

**==> picture [136 x 29] intentionally omitted <==**

**==> picture [235 x 35] intentionally omitted <==**

Although the test as stated is often sufficient, it can be strengthened a bit, see .

_Proof._ If _𝐿 >_ 1, then says that the sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[diverges.][Since it is a] necessary condition for the convergence of series that the terms go to zero, we know that �∞ _𝑛_ =1 _[𝑥][𝑛]_[must diverge.]

Thus suppose _𝐿 <_ 1. We will argue that[�][∞] _𝑛_ =1[|] _[𝑥][𝑛]_[|][ must converge.][The proof is similar] to that of . Of course _𝐿_ ≥ 0. Pick _𝑟_ such that _𝐿 < 𝑟 <_ 1. As _𝑟_ − _𝐿 >_ 0, there exists an _𝑀_ ∈ ℕ such that for all _𝑛_ ≥ _𝑀_ ,

**==> picture [104 x 32] intentionally omitted <==**

Therefore,

**==> picture [56 x 28] intentionally omitted <==**

For _𝑛 > 𝑀_ (that is for _𝑛_ ≥ _𝑀_ + 1), write

**==> picture [408 x 29] intentionally omitted <==**

For _𝑘 > 𝑀_ , write the partial sum as

**==> picture [238 x 125] intentionally omitted <==**

_2.5. SERIES_

97

As 0 _< 𝑟 <_ 1, the geometric series[�][∞] _𝑛_ =0 _[𝑟][𝑛]_[converges, so][ �][∞] _𝑛_ = _𝑀_ +1 _[𝑟][𝑛]_[converges as well.][We] take the limit as _𝑘_ goes to infinity on the right-hand side above to obtain

**==> picture [238 x 82] intentionally omitted <==**

The right-hand side is a number that does not depend on _𝑘_ . Hence the sequence of partial sums of[�][∞] _𝑛_ =1[|] _[𝑥][𝑛]_[|][is][bounded][and][�][∞] _𝑛_ =1[|] _[𝑥][𝑛]_[|][is][convergent.][Thus][�][∞] _𝑛_ =1 _[𝑥][𝑛]_[is][absolutely] convergent. □