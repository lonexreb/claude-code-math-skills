Example 2.2.2

**Example 2.2.2:** One application of the is to compute limits of sequences using limits that we already know. For example, consider the sequence � _𝑛_ ~~[√]~~ 1 _𝑛_ �∞ _𝑛_ =1[.][Since] √ _𝑛_ ≥ 1 for all _𝑛_ ∈ ℕ, we have

**==> picture [73 x 30] intentionally omitted <==**

for all _𝑛_ ∈ ℕ. We already know lim _𝑛_ →∞[1] / _𝑛_ = 0. Hence, using the constant sequence {0}[∞] _𝑛_ =1 and the sequence {[1] / _𝑛_ }[∞] _𝑛_ =1[in the squeeze lemma, we conclude]

**==> picture [76 x 30] intentionally omitted <==**

Limits, when they exist, preserve non-strict inequalities.

**==> picture [339 x 36] intentionally omitted <==**

_Then_

**==> picture [94 x 17] intentionally omitted <==**

_Proof._ Let _𝑥_ � lim _𝑛_ →∞ _𝑥𝑛_ and _𝑦_ � lim _𝑛_ →∞ _𝑦𝑛_ . Let _𝜖>_ 0 be given. Find an _𝑀_ 1 such that for all _𝑛_ ≥ _𝑀_ 1, we have | _𝑥𝑛_ − _𝑥_ | _<[𝜖]_ /2. Find an _𝑀_ 2 such that for all _𝑛_ ≥ _𝑀_ 2, we have �� _𝑦𝑛_ − _𝑦_ �� _< 𝜖_ /2. In particular, for some _𝑛_ ≥ max{ _𝑀_ 1 _, 𝑀_ 2}, we have _𝑥_ − _𝑥𝑛 < 𝜖_ /2 and _𝑦𝑛_ − _𝑦 <[𝜖]_ /2. We add these inequalities to obtain

**==> picture [270 x 11] intentionally omitted <==**

Since _𝑥𝑛_ ≤ _𝑦𝑛_ , we have 0 ≤ _𝑦𝑛_ − _𝑥𝑛_ and hence 0 _< 𝑦_ − _𝑥_ + _𝜖_ . In other words,

**==> picture [52 x 10] intentionally omitted <==**

Because _𝜖>_ 0 was arbitrary, we obtain _𝑥_ − _𝑦_ ≤ 0. Therefore, _𝑥_ ≤ _𝑦_ . □

. The next corollary follows by using constant sequences in The proof is left as an exercise.

## **Corollary 2.2.4.**

_(i) If_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is a convergent sequence such that][ 𝑥][𝑛]_[≥][0] _[ for all][ 𝑛]_[∈][ℕ] _[, then]_

**==> picture [63 x 17] intentionally omitted <==**

**==> picture [330 x 14] intentionally omitted <==**

**==> picture [133 x 13] intentionally omitted <==**

_Then_

**==> picture [85 x 17] intentionally omitted <==**

In and we cannot simply replace all the non-strict inequalities with strict inequalities. For example, let _𝑥𝑛_ �[−][1] / _𝑛_ and _𝑦𝑛_ �[1] / _𝑛_ . Then _𝑥𝑛 < 𝑦𝑛_ , _𝑥𝑛 <_ 0,

_2.2. FACTS ABOUT LIMITS OF SEQUENCES_

63

and _𝑦𝑛 >_ 0 for all _𝑛_ . However, these inequalities are not preserved by the limit operation as lim _𝑛_ →∞ _𝑥𝑛_ = lim _𝑛_ →∞ _𝑦𝑛_ = 0. The moral of this example is that strict inequalities may become non-strict inequalities when limits are applied; if we know _𝑥𝑛 < 𝑦𝑛_ for all _𝑛_ , we may only conclude

**==> picture [94 x 17] intentionally omitted <==**

This issue is a common source of errors.

## **2.2.2 Continuity of algebraic operations**

Limits interact nicely with algebraic operations.