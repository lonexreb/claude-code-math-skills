Proposition 2.6.3

**Proposition 2.6.3.** _Let_[�][∞] _𝑛_ =1 _[𝑥][𝑛][be an absolutely convergent series converging to a number][ 𝑥][.][Let] 𝜎_ : ℕ → ℕ _be a bĳection. Then_[�][∞] _𝑛_ =1 _[𝑥][𝜎]_[(] _[𝑛]_[)] _[ is absolutely convergent and converges to][ 𝑥][.]_

In other words, a rearrangement of an absolutely convergent series converges (absolutely) to the same number.

_Proof._ Let _𝜖>_ 0 be given. As[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[is absolutely convergent, take] _[ 𝑀]_[such that]

**==> picture [244 x 39] intentionally omitted <==**

As _𝜎_ is a bĳection, there exists a number _𝐾_ such that for each _𝑛_ ≤ _𝑀_ , there exists _𝑘_ ≤ _𝐾_ such that _𝜎_ ( _𝑘_ ) = _𝑛_ . In other words {1 _,_ 2 _, . . . , 𝑀_ } ⊂ _𝜎_[�] {1 _,_ 2 _, . . . , 𝐾_ }[�] .

_2.6. MORE ON SERIES_

103

For _𝑁_ ≥ _𝐾_ , let _𝑄_ � max _𝜎_[�] {1 _,_ 2 _, . . . , 𝑁_ }[�] . Compute

**==> picture [244 x 175] intentionally omitted <==**

So[�][∞] _𝑛_ =1 _[𝑥][𝜎]_[(] _[𝑛]_[)][ converges to] _[ 𝑥]_[.][To see that the convergence is absolute, we apply the argument] above to[�][∞] _𝑛_ =1[|] _[𝑥][𝑛]_[|][ to show that][ �][∞] _𝑛_ =1 �� _𝑥𝜎_ ( _𝑛_ )�� converges. □

(−1) _[𝑛]_[+][1] **Example 2.6.4:** Let us show that the alternating harmonic series[�][∞] _𝑛_ =1 _𝑛_ , which does not converge absolutely, can be rearranged to converge to anything. The odd terms and the even terms diverge to plus infinity and minus infinity respectively (prove this!):

**==> picture [234 x 35] intentionally omitted <==**

Let _𝑎𝑛_ �[(][−][1] _𝑛_[)] _[𝑛]_[+][1] for simplicity, let an arbitrary number _𝐿_ ∈ ℝ be given, and set _𝜎_ (1) � 1. Suppose we have defined _𝜎_ ( _𝑛_ ) for all _𝑛_ ≤ _𝑁_ . If

**==> picture [69 x 38] intentionally omitted <==**

then let _𝜎_ ( _𝑁_ + 1) � _𝑘_ be the smallest odd _𝑘_ ∈ ℕ that we have not used yet, that is, _𝜎_ ( _𝑛_ ) ≠ _𝑘_ for all _𝑛_ ≤ _𝑁_ . Otherwise, let _𝜎_ ( _𝑁_ + 1) � _𝑘_ be the smallest even _𝑘_ that we have not yet used.

By construction, _𝜎_ : ℕ → ℕ is one-to-one. It is also onto, because if we keep adding either odd (resp. even) terms, eventually we pass _𝐿_ and switch to the evens (resp. odds). So we switch infinitely many times.

Finally, let _𝑁_ be the _𝑁_ where we just pass _𝐿_ and switch. For example, suppose we have just switched from odd to even (so we start subtracting), and let _𝑁_[′] _> 𝑁_ be where we first switch back from even to odd. Then

**==> picture [240 x 37] intentionally omitted <==**

_CHAPTER 2. SEQUENCES AND SERIES_

104

Similarly for switching in the other direction. Therefore, the sum up to _𝑁_[′] − 1 is within min{ _𝜎_ ( _𝑁_ 1) _,𝜎_ ( _𝑁_[′] )}[of] _[ 𝐿]_[.][As we switch infinitely many times,] _[ 𝜎]_[(] _[𝑁]_[) →∞][and] _[ 𝜎]_[(] _[𝑁]_[′][) →∞][.][Hence]

**==> picture [154 x 37] intentionally omitted <==**

Here is an example to illustrate the proof. Suppose _𝐿_ = 1 _._ 2, then the order is

**==> picture [400 x 13] intentionally omitted <==**

At this point we are no more than[1] /8 from the limit. See .

**==> picture [216 x 144] intentionally omitted <==**

**Figure 2.9:** The first 14 partial sums of the rearrangement converging to 1 _._ 2.

## **2.6.4 Multiplication of series**

As we have already mentioned, multiplication of series is somewhat harder than addition. If at least one of the series converges absolutely, then we can use the following theorem. For this result, it is convenient to start the series at 0, rather than at 1.

**Theorem 2.6.5** (Mertens’ theorem ) **.** _Suppose_[�][∞] _𝑛_ =0 _[𝑎][𝑛][and]_[ �][∞] _𝑛_ =0 _[𝑏][𝑛][are two convergent series,] converging to 𝐴 and 𝐵 respectively. Suppose at least one of the series converges absolutely. Define_

**==> picture [230 x 35] intentionally omitted <==**

_Then the series_[�][∞] _𝑛_ =0 _[𝑐][𝑛][converges to][ 𝐴𝐵][.]_

The series[�][∞] _𝑛_ =0 _[𝑐][𝑛]_[is called the] _[ Cauchy product]_[ of][ �][∞] _𝑛_ =0 _[𝑎][𝑛]_[and][ �][∞] _𝑛_ =0 _[𝑏][𝑛]_[.]

> ‗Proved by the German mathematician (1840–1927).

_2.6. MORE ON SERIES_

105

_Proof._ Suppose[�][∞] _𝑛_ =0 _[𝑎][𝑛]_[converges absolutely, and let] _[ 𝜖>]_[0][ be given.][In this proof instead] of picking complicated estimates just to make the final estimate come out as less than _𝜖_ , let us simply obtain an estimate that depends on _𝜖_ and can be made arbitrarily small. Write

**==> picture [278 x 225] intentionally omitted <==**

We rearrange the _𝑚_ th partial sum of[�][∞] _𝑛_ =0 _[𝑐][𝑛]_[:]

We can surely make the second term on the right-hand side small. The trick is to handle the first term. Pick _𝐾_ such that for all _𝑚_ ≥ _𝐾_ , we have | _𝐴𝑚_ − _𝐴_ | _< 𝜖_ and also | _𝐵𝑚_ − _𝐵_ | _< 𝜖_ . As[�][∞] _𝑛_ =0 _[𝑎][𝑛]_[converges absolutely, make sure that] _[ 𝐾]_[is large enough such that for all] _[ 𝑚]_[≥] _[𝐾]_[,]

**==> picture [64 x 36] intentionally omitted <==**

As[�][∞] _𝑛_ =0 _[𝑏][𝑛]_[converges, then] _[ 𝐵]_[max][�][sup] �| _𝐵𝑛_ − _𝐵_ | : _𝑛_ = 0 _,_ 1 _,_ 2 _, . . ._ � is finite. Take _𝑚_ ≥ 2 _𝐾_ . In particular _𝑚_ − _𝐾_ + 1 _> 𝐾_ . So

**==> picture [363 x 124] intentionally omitted <==**

Therefore, for _𝑚_ ≥ 2 _𝐾_ , we have

**==> picture [390 x 81] intentionally omitted <==**

_CHAPTER 2. SEQUENCES AND SERIES_

106

The expression in the parenthesis on the right-hand side is a fixed number. Hence, we can make the right-hand side arbitrarily small by picking a small enough _𝜖>_ 0. So[�][∞] _𝑛_ =0 _[𝑐][𝑛] 𝐴𝐵_ . □ converges to