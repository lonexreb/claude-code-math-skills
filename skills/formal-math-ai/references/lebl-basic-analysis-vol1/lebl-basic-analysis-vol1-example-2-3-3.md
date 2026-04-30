Example 2.3.3

**Example 2.3.3:** Let { _𝑥𝑛_ }[∞] _𝑛_ =1[be defined by]

**==> picture [129 x 38] intentionally omitted <==**

Let us compute the lim inf and lim sup of this sequence. See also . First the limit inferior:

**==> picture [244 x 19] intentionally omitted <==**

For the limit superior, we write

**==> picture [187 x 22] intentionally omitted <==**

_2.3. LIMIT SUPERIOR, LIMIT INFERIOR, AND BOLZANO–WEIERSTRASS_

75

It is not hard to see that

**==> picture [195 x 39] intentionally omitted <==**

We leave it to the reader to show that the limit is 1. That is,

**==> picture [78 x 20] intentionally omitted <==**

Do note that the sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[is not a convergent sequence.]

**==> picture [312 x 175] intentionally omitted <==**

**----- Start of picture text -----**<br>
lim sup 푥푛푛<br>푛 →∞<br>lim inf 푥푛 ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄ ⋄<br>푛 →∞<br>**----- End of picture text -----**<br>


**==> picture [55 x 20] intentionally omitted <==**

**----- Start of picture text -----**<br>
lim sup 푥푛푛<br>푛 →∞<br>**----- End of picture text -----**<br>


**Figure 2.6:** First 20 terms of the sequence in . The marking is as in .

We associate certain subsequences with lim sup and lim inf. It is important to notice that { _𝑎𝑛_ }[∞] _𝑛_ =1[and][ {] _[𝑏][𝑛]_[}][∞] _𝑛_ =1[are not subsequences of][ {] _[𝑥][𝑛]_[}][∞] _𝑛_ =1[, nor do they have to even consist] of the same numbers. For example, if the sequence is {[1] / _𝑛_ }[∞] _𝑛_ =1[, then] _[ 𝑏][𝑛]_[=][ 0 for all] _[ 𝑛]_[∈][ℕ][.] **Theorem 2.3.4.** _If_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is a bounded sequence, then there exists a subsequence]_[ {] _[𝑥][𝑛][𝑘]_[}][∞] _𝑘_ =1 _[such] that_

**==> picture [112 x 21] intentionally omitted <==**

_Similarly, there exists a (perhaps different) subsequence_ { _𝑥𝑚𝑘_ }[∞] _𝑘_ =1 _[such that]_

**==> picture [110 x 18] intentionally omitted <==**

> _Proof._ Define _𝑎𝑛_ � sup{ _𝑥𝑘_ : _𝑘_ ≥ _𝑛_ }. Write _𝑥_ � lim sup _𝑛_ →∞ _𝑥𝑛_ = lim _𝑛_ →∞ _𝑎𝑛_ . We define the subsequence inductively. Let _𝑛_ 1 � 1, and suppose _𝑛_ 1 _, 𝑛_ 2 _, . . . , 𝑛𝑘_ −1 are already defined for some _𝑘_ ≥ 2. Pick an _𝑚_ ≥ _𝑛𝑘_ −1 + 1 such that

**==> picture [96 x 26] intentionally omitted <==**

_CHAPTER 2. SEQUENCES AND SERIES_

76

Such an _𝑚_ exists as _𝑎_ ( _𝑛𝑘_ −1+1) is a supremum of the set { _𝑥ℓ_ : _ℓ_ ≥ _𝑛𝑘_ −1 + 1} and hence there are elements of the sequence arbitrarily close (or even possibly equal) to the supremum. Set _𝑛𝑘_ � _𝑚_ . The subsequence { _𝑥𝑛𝑘_ }[∞] _𝑘_ =1[is defined.][Next, we must prove that it converges to] _[ 𝑥]_[.] For all _𝑘_ ≥ 2, we have _𝑎_ ( _𝑛𝑘_ −1+1) ≥ _𝑎𝑛𝑘_ (why?) and _𝑎𝑛𝑘_ ≥ _𝑥𝑛𝑘_ . Therefore, for every _𝑘_ ≥ 2,

**==> picture [137 x 64] intentionally omitted <==**

Let us show that { _𝑥𝑛𝑘_ }[∞] _𝑘_ =1[converges][to] _[𝑥]_[.][Note][that][the][subsequence][need][not][be] monotone. Let _𝜖>_ 0 be given. As { _𝑎𝑛_ }[∞] _𝑛_ =1[converges][to] _[𝑥]_[,][the][subsequence][{] _[𝑎][𝑛][𝑘]_[}][∞] _𝑘_ =1 converges to _𝑥_ . Thus there exists an _𝑀_ 1 ∈ ℕ such that for all _𝑘_ ≥ _𝑀_ 1, we have

**==> picture [70 x 23] intentionally omitted <==**

Find an _𝑀_ 2 ∈ ℕ such that

**==> picture [47 x 27] intentionally omitted <==**

Take _𝑀_ � max{ _𝑀_ 1 _, 𝑀_ 2 _,_ 2}. For all _𝑘_ ≥ _𝑀_ ,

**==> picture [319 x 117] intentionally omitted <==**

We leave the statement for lim inf as an exercise.

## **2.3.2 Using limit inferior and limit superior**

The advantage of lim inf and lim sup is that we can always write them down for any (bounded) sequence. If we could somehow compute them, we could also compute the limit of the sequence if it exists, or show that the sequence diverges. Working with lim inf and lim sup is a little bit like working with limits, although there are subtle differences.