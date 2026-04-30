Proposition 2.1.15

**Proposition 2.1.15.** _Let_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[be a sequence.][Then the following statements are equivalent:]_

_(i) The sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[converges.]_

_(ii) The 𝐾-tail_ { _𝑥𝑛_ + _𝐾_ }[∞] _𝑛_ =1 _[converges for all][ 𝐾]_[∈][ℕ] _[.] (iii) The 𝐾-tail_ { _𝑥𝑛_ + _𝐾_ }[∞] _𝑛_ =1 _[converges for some][ 𝐾]_[∈][ℕ] _[.]_

_Furthermore, if any (and hence all) of the limits exist, then for all 𝐾_ ∈ ℕ

**==> picture [106 x 18] intentionally omitted <==**

_Proof._ It is clear that implies . We will therefore show first that implies , and then we will show that implies . That is,

**==> picture [107 x 39] intentionally omitted <==**

In the process we will also show that the limits are equal.

We start with implies . Suppose { _𝑥𝑛_ }[∞] _𝑛_ =1[converges to some] _[ 𝑥]_[∈][ℝ][.][Let] _[ 𝐾]_[∈][ℕ][be] arbitrary, and define _𝑦𝑛_ � _𝑥𝑛_ + _𝐾_ . We wish to show that { _𝑦𝑛_ }[∞] _𝑛_ =1[converges to] _[ 𝑥]_[.][Given an] _𝜖>_ 0, there exists an _𝑀_ ∈ ℕ such that | _𝑥_ − _𝑥𝑛_ | _< 𝜖_ for all _𝑛_ ≥ _𝑀_ . Note that _𝑛_ ≥ _𝑀_ implies _𝑛_ + _𝐾_ ≥ _𝑀_ . Therefore, for all _𝑛_ ≥ _𝑀_ , we have

**==> picture [131 x 17] intentionally omitted <==**

Consequently, { _𝑦𝑛_ }[∞] _𝑛_ =1[converges to] _[ 𝑥]_[.]

Let us move to implies . Let _𝐾_ ∈ ℕ be given, define _𝑦𝑛_ � _𝑥𝑛_ + _𝐾_ , and suppose that { _𝑦𝑛_ }[∞] _𝑛_ =1[converges to] _[ 𝑥]_[∈][ℝ][.][That is, given an] _[ 𝜖>]_[ 0][, there exists an] _[ 𝑀]_[′][ ∈][ℕ][such that] �� _𝑥_ − _𝑦𝑛_ �� _< 𝜖_ for all _𝑛_ ≥ _𝑀_ ′. Let _𝑀_ � _𝑀_ ′ + _𝐾_ . Then _𝑛_ ≥ _𝑀_ implies _𝑛_ − _𝐾_ ≥ _𝑀_ ′. Thus, whenever _𝑛_ ≥ _𝑀_ , we have | _𝑥_ − _𝑥𝑛_ | = �� _𝑥_ − _𝑦𝑛_ − _𝐾_ �� _< 𝜖._

**==> picture [469 x 15] intentionally omitted <==**

At the end of the day, the limit does not care about how the sequence begins, it only cares about the tail of the sequence. The beginning of the sequence may be arbitrary.

_CHAPTER 2. SEQUENCES AND SERIES_

58

For example, the sequence defined by _𝑥𝑛_ � _𝑛_[2] + _𝑛_ 16[is decreasing if we start at] _[ 𝑛]_[=][ 4][ (it is] increasing before). That is: { _𝑥𝑛_ }[∞] _𝑛_ =1[=][1][/][17] _[,]_[ 1][/][10] _[,]_[ 3][/][25] _[,]_[ 1][/][8] _[,]_[ 5][/][41] _[,]_[ 3][/][26] _[,]_[ 7][/][65] _[,]_[ 1][/][10] _[,]_[ 9][/][97] _[,]_[ 5][/][58] _[, . . .]_[, and]

**==> picture [337 x 12] intentionally omitted <==**

If we throw away the first 3 terms and look at the 3-tail, it is decreasing. The proof is left as an exercise. Since the 3-tail is monotone and bounded below by zero, it is convergent, and therefore the sequence is convergent.

## **2.1.3 Subsequences**

It is useful to sometimes consider only some terms of a sequence. A subsequence of { _𝑥𝑛_ }[∞] _𝑛_ =1 is a sequence that contains only some of the numbers from { _𝑥𝑛_ }[∞] _𝑛_ =1[in the same order.]