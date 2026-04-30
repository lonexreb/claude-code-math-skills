Theorem 2.4.5

**Theorem 2.4.5.** _A sequence of real numbers is Cauchy if and only if it converges._

_Proof._ Suppose { _𝑥𝑛_ }[∞] _𝑛_ =1[converges to] _[ 𝑥]_[, and let] _[ 𝜖>]_[ 0][ be given.][Then there exists an] _[ 𝑀]_[such] that for _𝑛_ ≥ _𝑀_ ,

**==> picture [68 x 23] intentionally omitted <==**

Hence for _𝑛_ ≥ _𝑀_ and _𝑘_ ≥ _𝑀_ ,

**==> picture [324 x 23] intentionally omitted <==**

Alright, that direction was easy. Now suppose { _𝑥𝑛_ }[∞] _𝑛_ =1[is Cauchy.][We have shown that] { _𝑥𝑛_ }[∞] _𝑛_ =1[is bounded.][For a bounded sequence, liminf and limsup exist, and this is where] we use the . If we show that

**==> picture [122 x 21] intentionally omitted <==**

then { _𝑥𝑛_ }[∞] _𝑛_ =1[must be convergent by] . Define _𝑎_ � lim sup _𝑛_ →∞ _𝑥𝑛_ and _𝑏_ � lim inf _𝑛_ →∞ _𝑥𝑛_ . By , there exist subsequences { _𝑥𝑛𝑖_ }[∞] _𝑖_ =1[and][ {] _[𝑥][𝑚][𝑖]_[}][∞] _𝑖_ =1[, such that]

**==> picture [194 x 18] intentionally omitted <==**

**==> picture [468 x 132] intentionally omitted <==**

As | _𝑎_ − _𝑏_ | _< 𝜖_ for all _𝜖>_ 0, then _𝑎_ = _𝑏_ and the sequence converges.

_Remark_ 2.4.6 _._ The statement of this theorem is sometimes used to define the completeness property of the real numbers. We say a set is _Cauchy-complete_ (or sometimes just _complete_ ) if every Cauchy sequence converges to something in the set. Above, we proved that as ℝ has the , ℝ is Cauchy-complete. One can construct ℝ via “completing” ℚ by “throwing in” just enough points to make all Cauchy sequences converge (we omit the details). The resulting field has the least-upper-bound property. The advantage of defining completeness via Cauchy sequences is that it generalizes to more . abstract settings such as metric spaces, see

The Cauchy criterion is stronger than | _𝑥𝑛_ +1 − _𝑥𝑛_ | (or �� _𝑥𝑛_ + _𝑗_ − _𝑥𝑛_ �� for a fixed _𝑗_ ) going to zero as _𝑛_ goes to infinity. When we get to the partial sums of the harmonic series (see in the next section), we will have a sequence such that _𝑥𝑛_ +1 − _𝑥𝑛_ =[1] / _𝑛_ , yet { _𝑥𝑛_ }[∞] _𝑛_ =1[is divergent.][In fact, for that sequence,][ lim] _[𝑛]_[→∞] �� _𝑥𝑛_ + _𝑗_ − _𝑥𝑛_ �� = 0 for every _𝑗_ ∈ ℕ (compare ). The key point in the definition of Cauchy is that _𝑛_ and _𝑘_ vary independently and can be arbitrarily far apart.

_CHAPTER 2. SEQUENCES AND SERIES_

86

## **2.4.1 Exercises**

_**Exercise**_ **2.4.1** _**:** Prove that 𝑛_ 2−1 ∞ � _𝑛_[2] � _𝑛_ =1 _[is Cauchy using directly the definition of Cauchy sequences.]_ _**Exercise**_ **2.4.2** _**:** Let_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[be a sequence such that there exists a positive][ 𝐶][<]_[1] _[ and for all][ 𝑛][,]_

**==> picture [132 x 11] intentionally omitted <==**

_Prove that_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is Cauchy.][Hint:][You can freely use the formula (for][ 𝐶]_[≠][1] _[)]_

**==> picture [161 x 25] intentionally omitted <==**

_**Exercise**_ **2.4.3** (Challenging) _**:** Suppose 𝐹 is an ordered field that contains the rational numbers_ ℚ _, such that_ ℚ _is dense, that is: Whenever 𝑥, 𝑦_ ∈ _𝐹 are such that 𝑥 < 𝑦, then there exists a 𝑞_ ∈ ℚ _such that 𝑥 < 𝑞 < 𝑦. Say a sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[of rational numbers is Cauchy if given every][ 𝜖]_[∈][ℚ] _[with][ 𝜖>]_[0] _[, there exists an][ 𝑀] such that for all 𝑛, 𝑘_ ≥ _𝑀, we have_ | _𝑥𝑛_ − _𝑥𝑘_ | _< 𝜖. Suppose every Cauchy sequence of rational numbers has a limit in 𝐹. Prove that 𝐹 has the ._

_**Exercise**_ **2.4.4** _**:** Let_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[and]_[ {] _[𝑦][𝑛]_[}][∞] _𝑛_ =1 _[be sequences such that]_[ lim] _[𝑛]_[→∞] _[𝑦][𝑛]_[=][ 0] _[.][Suppose that for all][ 𝑘]_[∈][ℕ] _and for all 𝑚_ ≥ _𝑘, we have_

**==> picture [72 x 12] intentionally omitted <==**

_Show that_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is Cauchy.]_

_**Exercise**_ **2.4.5** _**:** Suppose a Cauchy sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is such that for every][𝑀]_[∈][ℕ] _[, there exists a][𝑘]_[≥] _[𝑀] and an 𝑛_ ≥ _𝑀 such that 𝑥𝑘 <_ 0 _and 𝑥𝑛 >_ 0 _. Using simply the definition of a Cauchy sequence and of a convergent sequence, show that the sequence converges to_ 0 _._

_**Exercise**_ **2.4.6** _**:** Suppose_ | _𝑥𝑛_ − _𝑥𝑘_ | ≤ _[𝑛]_ / _𝑘_[2] _for all 𝑛 and 𝑘. Show that_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is Cauchy.]_

_**Exercise**_ **2.4.7** _**:** Suppose_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is a Cauchy sequence such that for infinitely many][ 𝑛][,][ 𝑥][𝑛]_[=] _[𝑐][.][Using only] the definition of Cauchy sequence prove that_ lim _[𝑐][.] 𝑛_ →∞ _[𝑥][𝑛]_[=]

_**Exercise**_ **2.4.8** _**:** True or false, prove or find a counterexample: If_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is a Cauchy sequence, then there] exists an 𝑀 such that for all 𝑛_ ≥ _𝑀, we have_ | _𝑥𝑛_ +1 − _𝑥𝑛_ | ≤| _𝑥𝑛_ − _𝑥𝑛_ −1| _._

_2.5. SERIES_

87

## **2.5 Series**

_Note: 2 lectures_

A fundamental object in mathematics is that of a series. In fact, when the foundations of analysis were being developed, the motivation was to understand series. Understanding series is important in applications of analysis. For example, solutions to differential equations are often given as series, and differential equations are the basis for understanding almost all of modern science.

## **2.5.1 Definition**