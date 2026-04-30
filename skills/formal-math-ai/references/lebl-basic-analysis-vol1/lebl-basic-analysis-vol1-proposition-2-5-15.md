Proposition 2.5.15

**Proposition 2.5.15.** _If the series_[�][∞] _𝑛_ =1 _[𝑥][𝑛][converges absolutely, then it converges.]_

_Proof._ A series is convergent if and only if it is Cauchy. Hence suppose[�][∞] _𝑛_ =1[|] _[𝑥][𝑛]_[|][ is Cauchy.] That is, for every _𝜖>_ 0, there exists an _𝑀_ such that for all _𝑘_ ≥ _𝑀_ and all _𝑛 > 𝑘_ , we have

**==> picture [132 x 39] intentionally omitted <==**

We apply the triangle inequality for a finite sum to obtain

**==> picture [126 x 39] intentionally omitted <==**

Hence[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[is Cauchy, and therefore it converges.]

□

_2.5. SERIES_

93

If[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[converges][absolutely,][the][limits][of][�][∞] _𝑛_ =1 _[𝑥][𝑛]_[and][�][∞] _𝑛_ =1[|] _[𝑥][𝑛]_[|][are][generally] different. Computing one does not help us compute the other. However, the computation above leads to a useful inequality for absolutely convergent series, a series version of the triangle inequality, a proof of which we leave as an exercise:

**==> picture [92 x 39] intentionally omitted <==**

Absolutely convergent series have many wonderful properties. For example, absolutely convergent series can be rearranged arbitrarily, or we can multiply such series together easily. Conditionally convergent series on the other hand often do not behave as one would expect. See the next section.

We leave as an exercise to show that

**==> picture [49 x 35] intentionally omitted <==**

converges, although the reader should finish this section before trying. On the other hand, we proved

**==> picture [29 x 36] intentionally omitted <==**

(−1) _[𝑛]_ diverges. Therefore,[�][∞] _𝑛_ =1 _𝑛_ is a conditionally convergent series.

## **2.5.5 Comparison test and the** _𝑝_ **-series**

We noted above that for a series with positive terms to converge the terms not only have to go to zero, but they have to go to zero “fast enough.” If we know about convergence of a certain series, we can use the following comparison test to see if the terms of another series go to zero “fast enough.”

**Proposition 2.5.16** (Comparison test) **.** _Let_[�][∞] _𝑛_ =1 _[𝑥][𝑛][and]_[ �][∞] _𝑛_ =1 _[𝑦][𝑛][be series such that]_[ 0][ ≤] _[𝑥][𝑛]_[≤] _[𝑦][𝑛] 𝑛_ ∈ ℕ _. for all_

- _(i) If_[�][∞] _𝑛_ =1 _[𝑦][𝑛][converges, then so does]_[ �][∞] _𝑛_ =1 _[𝑥][𝑛][.]_

- _(ii) If_[�][∞] _𝑛_ =1 _[𝑥][𝑛][diverges, then so does]_[ �][∞] _𝑛_ =1 _[𝑦][𝑛][.]_

_Proof._ As the terms of the series are all nonnegative, the sequences of partial sums are both monotone increasing. Since _𝑥𝑛_ ≤ _𝑦𝑛_ for all _𝑛_ , the partial sums satisfy for all _𝑘_

**==> picture [277 x 37] intentionally omitted <==**

_CHAPTER 2. SEQUENCES AND SERIES_

94

If the series[�][∞] _𝑛_ =1 _[𝑦][𝑛]_[converges, the partial sums for the series are bounded.][Therefore, the] right-hand side of ( ) is bounded for all _𝑘_ ; there exists some _𝐵_ ∈ ℝ such that[�] _𝑛[𝑘]_ =1 _[𝑦][𝑛]_[≤] _[𝐵]_ for all _𝑘_ , and so

**==> picture [106 x 38] intentionally omitted <==**

Hence the partial sums for[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[are also bounded.][Since the partial sums are a monotone] increasing sequence they are convergent. The first item is thus proved.

On the other hand if[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[diverges, the sequence of partial sums must be unbounded] since it is monotone increasing. That is, the partial sums for[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[are eventually bigger] than any real number. Putting this together with ( ) we see that for every _𝐵_ ∈ ℝ, there is a _𝑘_ such that

**==> picture [106 x 37] intentionally omitted <==**

Hence the partial sums for[�][∞] _𝑛_ =1 _[𝑦][𝑛]_[are also unbounded, and][ �][∞] _𝑛_ =1 _[𝑦][𝑛]_[also diverges.]

**==> picture [9 x 8] intentionally omitted <==**

A useful series to use with the comparison test is the _𝑝_ -series . **Proposition 2.5.17** ( _𝑝_ -series or the _𝑝_ -test) **.** _For 𝑝_ ∈ ℝ _, the series_

**==> picture [35 x 35] intentionally omitted <==**

_>_ 1 _. converges if and only if 𝑝_

_Proof._ First suppose _𝑝_ ≤ 1. As _𝑛_ ≥ 1, we have _𝑛_[1] ~~_[𝑝]_~~[≥] _𝑛_[1][.][Since][ �][∞] _𝑛_ =1 _𝑛_ 1[diverges,][ �][∞] _𝑛_ =1 _𝑛_ 1 ~~_[𝑝]_~~[must] diverge for all _𝑝_ ≤ 1 by the comparison test.

Now suppose _𝑝 >_ 1. We proceed as we did for the harmonic series, but instead of showing that the sequence of partial sums is unbounded, we show that it is bounded. The terms of the series are positive, so the sequence of partial sums is monotone increasing and converges if it is bounded above. Let _𝑠𝑛_ denote the _𝑛_ th partial sum.

_𝑠_ 1 = 1 _,_

**==> picture [246 x 137] intentionally omitted <==**

> ‗We have not yet defined _𝑥𝑝_ for _𝑥 >_ 0 and an arbitrary _𝑝_ ∈ ℝ. The definition is _𝑥𝑝_ � exp( _𝑝_ ln _𝑥_ ). We will define the logarithm and the exponential in . For now you can just think of rational _𝑝_ where _𝑘 𝑥[𝑘]_[/] _[𝑚]_ = ( _𝑥_[1][/] _[𝑚]_ ) . See also .

_2.5. SERIES_

95

Instead of estimating from below, we estimate from above. As _𝑝_ is positive, then 2 _[𝑝] <_ 3 _[𝑝]_ , and hence[1][1][1][1][Similarly,][1][1][1][1][1][1][1][1][Therefore, for] 2 ~~_[𝑝]_~~[+] 3 ~~_[𝑝]_~~ _[<]_ 2 ~~_[𝑝]_~~[+] 2 ~~_[𝑝]_~~[.] 4 ~~_[𝑝]_~~[+] 5 ~~_[𝑝]_~~[+] 6 ~~_[𝑝]_~~[+] 7 ~~_[𝑝]_~~ _[<]_ 4 ~~_[𝑝]_~~[+] 4 ~~_[𝑝]_~~[+] 4 ~~_[𝑝]_~~[+] 4 ~~_[𝑝]_~~[.] all _𝑘_ ≥ 2,

**==> picture [143 x 178] intentionally omitted <==**

1 As _𝑝 >_ 1, then 2 _[𝑝]_[−][1] _[<]_[1.] says that

**==> picture [59 x 37] intentionally omitted <==**

converges. Thus,

**==> picture [214 x 37] intentionally omitted <==**

For every _𝑛_ there is a _𝑘_ ≥ 2 such that _𝑛_ ≤ 2 _[𝑘]_ − 1, and as { _𝑠𝑛_ }[∞] _𝑛_ =1[is a monotone sequence,] _𝑠𝑛_ ≤ _𝑠_ 2 _𝑘_ −1. So for all _𝑛_ ,

**==> picture [104 x 37] intentionally omitted <==**

Thus the sequence of partial sums is bounded, and the series converges.

**==> picture [9 x 8] intentionally omitted <==**

Neither the _𝑝_ -series test nor the comparison test tell us what the sum converges to. They only tell us that a limit of the partial sums exists. For instance, while we know that ∞ � _𝑛_ =1[1][/] _[𝑛]_[2][ converges, it is far harder to find] that the limit is _[𝜋]_[2] /6. If we treat[�][∞] _𝑛_ =1[1][/] _[𝑛][𝑝]_[as a] function of _𝑝_ , we get the so-called Riemann _𝜁_ (zeta) function. Understanding the behavior of this function contains one of the most famous unsolved problems in mathematics today and has applications in seemingly unrelated areas such as modern cryptography.