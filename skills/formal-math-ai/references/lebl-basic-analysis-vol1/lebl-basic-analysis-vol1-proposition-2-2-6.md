Proposition 2.2.6

**Proposition 2.2.6.** _Let_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[be a convergent sequence such that][ 𝑥][𝑛]_[≥][0] _[ for all][ 𝑛]_[∈][ℕ] _[.][Then]_

**==> picture [112 x 24] intentionally omitted <==**

Of course, to even make this statement, we need to apply to show that lim _𝑛_ →∞ _𝑥𝑛_ ≥ 0, so that we can take the square root without worry.

_Proof._ Let { _𝑥𝑛_ }[∞] _𝑛_ =1[be a convergent sequence and let] _[ 𝑥]_[�][lim] _[𝑛]_[→∞] _[𝑥][𝑛]_[.][As we just mentioned,] _𝑥_ ≥ 0.

First suppose _𝑥_ = 0. Let _𝜖>_ 0 be given. Then there is an _𝑀_ such that for all _𝑛_ ≥ _𝑀_ , we have _𝑥𝑛_ = | _𝑥𝑛_ | _< 𝜖_[2] , or in other words,[√] _𝑥𝑛 < 𝜖_ . Hence,

**==> picture [118 x 17] intentionally omitted <==**

Now suppose _𝑥 >_ 0 (and hence[√] _𝑥 >_ 0).

**==> picture [317 x 116] intentionally omitted <==**

We leave the rest of the proof to the reader.

_CHAPTER 2. SEQUENCES AND SERIES_

66

A similar proof works for the _𝑘_ th root. That is, we also obtain lim _𝑛_ →∞ _𝑥𝑛_[1][/] _[𝑘]_ = (lim _𝑛_ →∞ _𝑥𝑛_ )[1][/] _[𝑘]_ . We leave this to the reader as a challenging exercise.

We may also want to take the limit past the absolute value sign. The converse of this proposition is not true, see part b). **Proposition 2.2.7.** _If_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is a convergent sequence, then]_[ {|] _[𝑥][𝑛]_[|}][∞] _𝑛_ =1 _[is convergent and]_

**==> picture [108 x 24] intentionally omitted <==**

_Proof._ We simply note the reverse triangle inequality

**==> picture [118 x 16] intentionally omitted <==**

Hence if | _𝑥𝑛_ − _𝑥_ | can be made arbitrarily small, so can �� | _𝑥𝑛_ | −| _𝑥_ | ��. Details are left to the reader. □

Let us see an example putting the propositions above together. Since lim _𝑛_ →∞[1] / _𝑛_ = 0, then

**==> picture [370 x 39] intentionally omitted <==**

That is, the limit on the left-hand side exists because the right-hand side exists. You really should read the equality above from right to left.

On the other hand you must apply the propositions carefully. For example, by rewriting the expression with common denominator first we find

**==> picture [461 x 66] intentionally omitted <==**

## **2.2.3 Recursively defined sequences**

Now that we know we can interchange limits and algebraic operations, we can compute the limits of many sequences. One such class are recursively defined sequences, that is, sequences where the next number in the sequence is computed using a formula from a fixed number of preceding elements in the sequence.