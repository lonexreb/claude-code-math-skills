Example 2.6.13

**Example 2.6.13:** Let us expand 1+2 _𝑥𝑥_ + _𝑥_[2][as a power series around the origin (] _[𝑥]_[0][=][0][) and] find the radius of convergence.

Write 1 + 2 _𝑥_ + _𝑥_[2] = (1 + _𝑥_ )[2] =[�] 1 −(− _𝑥_ )[�][2] , and suppose | _𝑥_ | _<_ 1. Compute

**==> picture [160 x 160] intentionally omitted <==**

_CHAPTER 2. SEQUENCES AND SERIES_

110

Using the formula for the product of series, we obtain _𝑐_ 0 = 1, _𝑐_ 1 = −1 − 1 = −2, _𝑐_ 2 = 1 + 1 + 1 = 3, etc. Hence, for | _𝑥_ | _<_ 1,

**==> picture [155 x 36] intentionally omitted <==**

The radius of convergence is at least 1. We leave it to the reader to verify that the radius of convergence is exactly equal to 1.

You can use the method of partial fractions you know from calculus. For example, to find the power series for _[𝑥] 𝑥_[3][2][+] − _[𝑥]_ 1[at 0, write]

**==> picture [283 x 35] intentionally omitted <==**

## **2.6.6 Exercises**

_**Exercise**_ **2.6.1** _**:** Decide the convergence or divergence of the following series._

**==> picture [345 x 32] intentionally omitted <==**

_**Exercise**_ **2.6.2** _**:** Suppose both_[�][∞] _𝑛_ =0 _[𝑎][𝑛][and]_[�][∞] _𝑛_ =0 _[𝑏][𝑛][converge][absolutely.][Show][that][the][product][series,]_ ∞ � _𝑛_ =0 _[𝑐][𝑛][where][ 𝑐][𝑛]_[=] _[𝑎]_[0] _[𝑏][𝑛]_[+] _[ 𝑎]_[1] _[𝑏][𝑛]_[−][1][ + · · · +] _[ 𝑎][𝑛][𝑏]_[0] _[, also converges absolutely.]_

_**Exercise**_ **2.6.3** (Challenging) _**:** Let_[�][∞] _𝑛_ =1 _[𝑎][𝑛][be][conditionally][convergent.][Show][that][given][an][arbitrary] 𝑥_ ∈ ℝ _there exists a rearrangement of_[�][∞] _𝑛_ =1 _[𝑎][𝑛][such that the rearranged series converges to][𝑥][.][Hint:][See] ._

## _**Exercise**_ **2.6.4** _**:**_

- (−1) _[𝑛]_[+][1]

- _a) Show that the alternating harmonic series_[�][∞] _𝑛_ =1 _𝑛 has a rearrangement such that for every interval_ ( _𝑥, 𝑦_ ) _, there exists a partial sum 𝑠𝑛 of the rearranged series such that 𝑠𝑛_ ∈( _𝑥, 𝑦_ ) _._

- _b) Show that the rearrangement you found does not converge. See ._

- _c) Show that for every 𝑥_ ∈ ℝ _, there exists a subsequence of partial sums_ { _𝑠𝑛𝑘_ }[∞] _𝑘_ =1 _[of your rearrangement] such that_ lim _[𝑥][.] 𝑘_ →∞ _[𝑠][𝑛][𝑘]_[=]

_**Exercise**_ **2.6.5** _**:** For the following power series, find if they are convergent or not, and if so find their radius of convergence._

**==> picture [464 x 33] intentionally omitted <==**

_**Exercise**_ **2.6.6** _**:** Suppose_[�][∞] _𝑛_ =0 _[𝑎][𝑛][𝑥][𝑛][converges for][ 𝑥]_[=][ 1] _[.]_

_a) What can you say about the radius of convergence?_

- _b) If you further know that at 𝑥_ = 1 _the convergence is not absolute, what can you say?_

_2.6. MORE ON SERIES_

111

_𝑥_ _**Exercise**_ **2.6.7** _**:** Expand[as a power series around][ 𝑥]_[0][=][ 0] _[, and compute its radius of convergence.]_ 4 − _𝑥_[2]

## _**Exercise**_ **2.6.8** _**:**_

- _a) Find an example where the radii of convergence of_[�][∞] _𝑛_ =0 _[𝑎][𝑛][𝑥][𝑛][and]_[ �][∞] _𝑛_ =0 _[𝑏][𝑛][𝑥][𝑛][are both 1, but the radius] of convergence of the sum of the two series is infinite._

- _b) (Trickier) Find an example where the radii of convergence of_[�][∞] _𝑛_ =0 _[𝑎][𝑛][𝑥][𝑛][and]_[ �][∞] _𝑛_ =0 _[𝑏][𝑛][𝑥][𝑛][are both 1, but] the radius of convergence of the product of the two series is infinite._

_**Exercise**_ **2.6.9** _**:** Figure out how to compute the radius of convergence using the ratio test. That is, suppose_ ∞ | _𝑎𝑛_ +1| � _𝑛_ =0 _[𝑎][𝑛][𝑥][𝑛][is a power series and][ 𝑅]_[�][lim] _[𝑛]_[→∞] | _𝑎𝑛_ | _[exists or is]_[ ∞] _[.][Find the radius of convergence and prove] your claim._

## _**Exercise**_ **2.6.10** _**:**_

- _a) Prove that_ lim _𝑛_ →∞ _𝑛_[1][/] _[𝑛]_ = 1 _using the following procedure: Write 𝑛_[1][/] _[𝑛]_ = 1 + _𝑏𝑛 and note 𝑏𝑛 >_ 0 _. Then show that_ (1 + _𝑏𝑛_ ) _[𝑛]_ ≥ _[𝑛]_[(] _[𝑛]_ 2[−][1][)] _𝑏𝑛_[2] _[and use this to show that] 𝑛_[lim] →∞ _[𝑏][𝑛]_[=][ 0] _[.]_

- _b) Use the result of part a) to show that if_[�][∞] _𝑛_ =0 _[𝑎][𝑛][𝑥][𝑛][is a convergent power series with radius of convergence] 𝑅, then_[�][∞] _𝑛_ =0 _[𝑛𝑎][𝑛][𝑥][𝑛][is also convergent with the same radius of convergence.]_

There are different notions of summability (convergence) of a series than just the one we have seen. A common one is _Cesàro summability_ . Let[�][∞] _𝑛_ =1 _[𝑎][𝑛]_[be a series and let] _[𝑠][𝑛]_[be the] _[ 𝑛]_[th partial] sum. The series is said to be Cesàro summable to _𝑎_ if

**==> picture [126 x 22] intentionally omitted <==**

## _**Exercise**_ **2.6.11** (Challenging) _**:**_

- _a) If_[�][∞] _𝑛_ =1 _[𝑎][𝑛][is convergent to][ 𝑎][(in the usual sense), show that]_[ �][∞] _𝑛_ =1 _[𝑎][𝑛][is Cesàro summable (see above) to][ 𝑎][.] b) Show that in the sense of Cesàro_[�][∞] _𝑛_ =1[(−][1][)] _[𝑛][is summable to]_[1][/][2] _[.]_

- _c) Let 𝑎𝑛_ � _𝑘 when 𝑛_ = _𝑘_[3] _for some 𝑘_ ∈ ℕ _, 𝑎𝑛_ � − _𝑘 when 𝑛_ = _𝑘_[3] + 1 _for some 𝑘_ ∈ ℕ _, otherwise let 𝑎𝑛_ � 0 _. Show that_[�][∞] _𝑛_ =1 _[𝑎][𝑛][diverges in the usual sense (in fact, both the sequence of terms and the partial] sums are unbounded), but it is Cesàro summable to 0 (seems a little paradoxical at first sight)._

_**Exercise**_ **2.6.12** (Challenging) _**:** Show that the monotonicity in the alternating series test is necessary. That is, find a sequence of positive real numbers_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[with]_[lim] _[𝑛]_[→∞] _[𝑥][𝑛]_[=][0] _[but][such][that]_[�][∞] _𝑛_ =1[(−][1][)] _[𝑛][𝑥][𝑛] diverges._

_**Exercise**_ **2.6.13** _**:** Find a series_[�][∞] _𝑛_ =1 _[𝑥][𝑛][that converges, but]_[ �][∞] _𝑛_ =1 _[𝑥] 𝑛_[2] _[diverges.][Hint:][Compare] ._

_**Exercise**_ **2.6.14** _**:** Suppose_ { _𝑐𝑛_ }[∞] _𝑛_ =1 _[is][a][sequence.][Prove][that][for][every][𝑟]_[∈(][0] _[,]_[ 1][)] _[,][there][exists][a][strictly] increasing sequence_ { _𝑛𝑘_ }[∞] _𝑘_ =1 _[of natural numbers (][𝑛][𝑘]_[+][1] _[>][𝑛][𝑘][) such that]_

**==> picture [42 x 33] intentionally omitted <==**

_converges absolutely for all 𝑥_ ∈[− _𝑟, 𝑟_ ] _._

- ‗Named for the Italian mathematician (1859–1906).

_CHAPTER 2. SEQUENCES AND SERIES_

112

_**Exercise**_ **2.6.15** (Tonelli/Fubini for sums, challenging) _**:** Suppose let_ { _𝑥𝑘,ℓ_ }[∞] _𝑘_ =1 _,ℓ_ =1 _[denote a doubly indexed] sequence and let 𝜎_ : ℕ → ℕ[2] _be a bĳection. Consider the series_

**==> picture [265 x 36] intentionally omitted <==**

_The expressions ii) and iii) are series of series and so we say they converge if the inner series always converges and the outer series then also converges._

- _a) (Tonelli) Suppose 𝑥𝑘,ℓ_ ≥ 0 _for all 𝑘, ℓ . Show that the three series i), ii), iii) either all diverge (to_ ∞ _) or they all converge to the same number. In the case of divergence, some of the “inner” series might be infinity in which case we consider the entire sum to diverge._

- _b) (Fubini) Suppose i) converges absolutely. Show that ii) and iii) converge and they both converge to the same number as i)._

## **Chapter 3**

## **Continuous Functions**

## **3.1 Limits of functions**

_Note: 2–3 lectures_

Before we define continuity of functions, we visit a somewhat more general notion of a limit than that of a sequence. Given a function _𝑓_ : _𝑆_ → ℝ, we want to see how _𝑓_ ( _𝑥_ ) behaves as _𝑥_ tends to a certain point.

## **3.1.1 Cluster points**

First, we return to a concept we have seen previously in an exercise. When moving within the set _𝑆_ , we can only approach points that have elements of _𝑆_ arbitrarily near.