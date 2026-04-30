Theorem

**Theorem.** Suppose[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[is a series whose sequence of partial sums is bounded,][ {] _[𝜆][𝑛]_[}][∞] _𝑛_ =1[is a] sequence with lim _𝑛_ →∞ _𝜆𝑛_ = 0, and[�][∞] _𝑛_ =1[|] _[𝜆][𝑛]_[+][1][ −] _[𝜆][𝑛]_[|][ is convergent.][Then][ �][∞] _𝑛_ =1 _[𝜆][𝑛][𝑥][𝑛]_[is convergent.]

_CHAPTER 2. SEQUENCES AND SERIES_

100

## **2.6 More on series**

_Note: up to 2–3 lectures (optional, can safely be skipped or covered partially)_

## **2.6.1 Root test**

A test similar to the ratio test is the so-called _root test_ . The proof of this test is similar. Again, the idea is to generalize what happens for the geometric series.

**Proposition 2.6.1** (Root test) **.** _Let_[�][∞] _𝑛_ =1 _[𝑥][𝑛][be a series and let]_

**==> picture [104 x 25] intentionally omitted <==**

**==> picture [235 x 34] intentionally omitted <==**

_Proof._ If _𝐿 >_ 1, then there exists a subsequence { _𝑥𝑛𝑘_ }[∞] _𝑘_ =1[such that] _[𝐿]_[=][lim] _[𝑘]_[→∞][|] _[𝑥][𝑛][𝑘]_[|][1][/] _[𝑛][𝑘]_[.] Let _𝑟_ be such that _𝐿 > 𝑟 >_ 1. There exists an _𝑀_ such that for all _𝑘_ ≥ _𝑀_ , we have | _𝑥𝑛𝑘_ |[1][/] _[𝑛][𝑘] > 𝑟 >_ 1, or in other words | _𝑥𝑛𝑘_ | _> 𝑟[𝑛][𝑘] >_ 1. The subsequence {| _𝑥𝑛𝑘_ |}[∞] _𝑘_ =1[,][and] therefore also {| _𝑥𝑛_ |}[∞] _𝑛_ =1[, cannot possibly converge to zero, and so the series diverges.]

Now suppose _𝐿 <_ 1. Pick _𝑟_ such that _𝐿 < 𝑟 <_ 1. By definition of limit supremum, there is an _𝑀_ such that for all _𝑛_ ≥ _𝑀_ ,

**==> picture [129 x 17] intentionally omitted <==**

Therefore, for all _𝑛_ ≥ _𝑀_ ,

**==> picture [252 x 15] intentionally omitted <==**

Let _𝑘 > 𝑀_ , and estimate the _𝑘_ th partial sum:

**==> picture [322 x 39] intentionally omitted <==**

As 0 _< 𝑟 <_ 1, the geometric series[�][∞] _𝑛_ = _𝑀_ +1 _[𝑟][𝑛]_[converges to] _[𝑟]_ 1 _[𝑀]_ −[+] _𝑟_[1][.][As everything is positive,]

**==> picture [150 x 39] intentionally omitted <==**

Thus the sequence of partial sums of[�][∞] _𝑛_ =1[|] _[𝑥][𝑛]_[|][is][bounded,][and][the][series][converges.] Therefore,[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[converges absolutely.] □

> ‗In case _𝐿_ = ∞, see . Alternatively, note that if _𝐿_ = ∞, then �| _𝑥𝑛_ |[1][/] _[𝑛]_[�][∞] _𝑛_ =1[is unbounded, and] thus so is { _𝑥𝑛_ }[∞] _𝑛_ =1[.]

_2.6. MORE ON SERIES_

101

## **2.6.2 Alternating series test**

The tests we have seen so far only addressed absolute convergence. The following test gives a large supply of conditionally convergent series.

**Proposition 2.6.2** (Alternating series) **.** _Let_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[be][a][monotone][decreasing][sequence][of] positive real numbers such that_ lim _[Then] 𝑛_ →∞ _[𝑥][𝑛]_[=][ 0] _[.]_

**==> picture [134 x 35] intentionally omitted <==**

_Proof._ Let _𝑠𝑚_ �[�] _[𝑚] 𝑘_ =1[(−][1][)] _[𝑛][𝑥][𝑛]_[be the] _[ 𝑚]_[th partial sum.][Then]

**==> picture [376 x 38] intentionally omitted <==**

The sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[is decreasing, so][ (−] _[𝑥]_[2] _[ℓ]_[−][1][ +] _[ 𝑥]_[2] _[ℓ]_[) ≤][0 for all] _[ ℓ]_[.][Thus, the subsequence] { _𝑠_ 2 _𝑘_ }[∞] _𝑘_ =1[of partial sums is a decreasing sequence.][Similarly,][ (] _[𝑥]_[2] _[ℓ]_[−] _[𝑥]_[2] _[ℓ]_[+][1][) ≥][0, and so]

**==> picture [291 x 13] intentionally omitted <==**

The intuition behind the bound 0 ≥ _𝑠_ 2 _𝑘_ ≥− _𝑥_ 1 is illustrated in .

**==> picture [287 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
푥 2<br>푥 4<br>푥 6<br>푥 8<br>−−−− 푥푥푥푥 7531 + + + +  푥 푥 푥 푥 8642 − 푥 1 − 푥 2 − 푥 3 − 푥 4 − 푥 5 − 푥 6 − 푥 7 − 푥 8<br>**----- End of picture text -----**<br>


**Figure 2.8:** Showing that 0 ≥ _𝑠_ 2 _𝑘_ ≥− _𝑥_ 1 where _𝑘_ = 4 for an alternating series.

As { _𝑠_ 2 _𝑘_ }[∞] _𝑘_ =1[is decreasing and bounded below, it converges.][Let] _[𝑎]_[�][lim] _[𝑘]_[→∞] _[𝑠]_[2] _[𝑘]_[.][We] wish to show that lim _𝑚_ →∞ _𝑠𝑚_ = _𝑎_ (and not just for the subsequence). Given _𝜖>_ 0, pick _𝑀_ such that | _𝑠_ 2 _𝑘_ − _𝑎_ | _<[𝜖]_ /2 whenever _𝑘_ ≥ _𝑀_ . Since lim _𝑛_ →∞ _𝑥𝑛_ = 0, we also make _𝑀_ possibly larger to obtain _𝑥_ 2 _𝑘_ +1 _<[𝜖]_ /2 whenever _𝑘_ ≥ _𝑀_ . Suppose _𝑚_ ≥ 2 _𝑀_ + 1. If _𝑚_ = 2 _𝑘_ , then _𝑘_ ≥ _𝑀_ +[1] /2 ≥ _𝑀_ and | _𝑠𝑚_ − _𝑎_ | = | _𝑠_ 2 _𝑘_ − _𝑎_ | _<[𝜖]_ /2 _< 𝜖_ . If _𝑚_ = 2 _𝑘_ + 1, then also _𝑘_ ≥ _𝑀_ . Notice _𝑠_ 2 _𝑘_ +1 = _𝑠_ 2 _𝑘_ − _𝑥_ 2 _𝑘_ +1. Thus

**==> picture [424 x 12] intentionally omitted <==**

_CHAPTER 2. SEQUENCES AND SERIES_

102

Notably, there exist conditionally convergent series where the absolute values of the terms go to zero arbitrarily slowly. The series

**==> picture [49 x 35] intentionally omitted <==**

converges for arbitrarily small _𝑝 >_ 0, but it does not converge absolutely when _𝑝_ ≤ 1.

## **2.6.3 Rearrangements**

Absolutely convergent series behave as we imagine they should. For example, absolutely convergent series can be summed in any order whatsoever. Nothing of the sort holds for conditionally convergent series (see and ).

Consider a series

**==> picture [36 x 35] intentionally omitted <==**

_𝜎_ : ℕ → ℕ Given a bĳective function , the corresponding rearrangement is the series:

**==> picture [46 x 35] intentionally omitted <==**

We simply sum the series in a different order.