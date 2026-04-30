Example 5.5.12

**Example 5.5.12:** An example to keep in mind for improper integrals is the so-called _sinc_ . _function_ This function comes up quite often in both pure and applied mathematics. Define

**==> picture [141 x 39] intentionally omitted <==**

**==> picture [218 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>1<br>2<br>−4 휋 −2 휋 2 휋 4 휋<br>− [1]<br>4<br>**----- End of picture text -----**<br>


**Figure 5.8:** The sinc function.

It is not difficult to show that the sinc function is continuous at zero, but that is not important right now. What is important is that

**==> picture [299 x 29] intentionally omitted <==**

The integral of the sinc function is a continuous analogue of the alternating harmonic series[�][∞] _𝑛_ =1[(−][1][)] _[𝑛]_[/] _[𝑛]_[,][while][the][absolute][value][is][like][the][regular][harmonic][series][ �][∞] _𝑛_ =1[1][/] _[𝑛]_[.] In particular, the fact that the integral converges must be done directly rather than using comparison test.

We will not prove the first statement exactly. Let us simply prove that the integral of the sinc function converges, but we will not worry about the exact limit. Because[sin] −[(][−] _𝑥[𝑥]_[)] =[sin] _𝑥_[(] _[𝑥]_[)] , it is enough to show that

**==> picture [74 x 30] intentionally omitted <==**

We also avoid _𝑥_ = converges. 0 this way to make our life simpler.

For every _𝑛_ ∈ ℕ, we have that for _𝑥_ ∈[ _𝜋_ 2 _𝑛, 𝜋_ (2 _𝑛_ + 1)],

**==> picture [152 x 30] intentionally omitted <==**

> ‗Shortened from Latin: _sinus cardinalis_

_5.5. IMPROPER INTEGRALS_

221

as sin( _𝑥_ ) ≥ 0. For _𝑥_ ∈[ _𝜋_ (2 _𝑛_ + 1) _, 𝜋_ (2 _𝑛_ + 2)],

**==> picture [170 x 29] intentionally omitted <==**

as sin( _𝑥_ ) ≤ 0.

Via the fundamental theorem of calculus,

**==> picture [444 x 90] intentionally omitted <==**

Similarly,

Adding the two together we find

**==> picture [414 x 33] intentionally omitted <==**

See .

**==> picture [363 x 147] intentionally omitted <==**

**----- Start of picture text -----**<br>
sin( 푥 ) sin( 푥 ) sin( 푥 )<br>+ 푥 휋 (2 푛 +1) 휋 (2 푛 +2)<br>휋 (2 푛 + 1) 휋 (2 푛 + 2)<br>휋 2 푛<br>sin( 푥 ) sin( 푥 ) sin( 푥 ) −<br>푥 휋 (2 푛 +1) 휋 2 푛<br>**----- End of picture text -----**<br>


2 _𝜋_ ( _𝑛_ +1) sin( _𝑥_ ) 1 −1 **Figure 5.9:** Bound of ∫2 _𝜋𝑛 𝑥 𝑑𝑥_ using the shaded integral (signed area _𝜋𝑛_[+] _𝜋_ ( _𝑛_ +1)[).]

For _𝑘_ ∈ ℕ,

**==> picture [302 x 37] intentionally omitted <==**

We find the partial sums of a series with positive terms. The series converges as[�][∞] _𝑛_ =1 _𝜋𝑛_ (1 _𝑛_ +1) is a convergent series. Thus as a sequence,

**==> picture [243 x 36] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

222

Let _𝑀 >_ 2 _𝜋_ be arbitrary, and let _𝑘_ ∈ ℕ be the largest integer such that 2 _𝑘𝜋_ ≤ _𝑀_ . For 1 _𝑥_ ∈[2 _𝑘𝜋, 𝑀_ ], we have 2[−] _𝑘_[1] _𝜋_[≤][sin] _𝑥_[(] _[𝑥]_[)] ≤ 2 _𝑘𝜋_[, and so]

**==> picture [173 x 33] intentionally omitted <==**

As _𝑘_ is the largest _𝑘_ such that 2 _𝑘𝜋_ ≤ _𝑀_ , then as _𝑀_ ∈ ℝ goes to infinity, so does _𝑘_ ∈ ℕ. Then

**==> picture [262 x 33] intentionally omitted <==**

As _𝑀_ goes to infinity, the first term on the right-hand side goes to _𝐿_ , and the second term on the right-hand side goes to zero. Hence

**==> picture [100 x 30] intentionally omitted <==**

The double-sided integral of sinc also exists as noted above. We leave the other statement—that the integral of the absolute value of the sinc function diverges—as an exercise.

## **5.5.1 Integral test for series**

The fundamental theorem of calculus can be used in proving a series is summable and to estimate its sum.

**Proposition 5.5.13** (Integral test) **.** _Suppose 𝑓_ : [ _𝑘,_ ∞) → ℝ _is a decreasing nonnegative function where 𝑘_ ∈ ℤ _. Then_

_In this case_

**==> picture [306 x 96] intentionally omitted <==**

See , for an illustration with _𝑘_ = 1. By , _𝑓_ is integrable on every interval [ _𝑘, 𝑏_ ] for all _𝑏 > 𝑘_ , so the statement of the theorem makes sense without additional hypotheses of integrability.

_𝑛_ +1 _Proof._ Let _ℓ, 𝑚_ ∈ ℤ be such that _𝑚 > ℓ_ ≥ _𝑘_ . Because _𝑓_ is decreasing, we have ∫ _𝑛 𝑓_ ≤ _𝑛 𝑓_ ( _𝑛_ ) ≤ ∫ _𝑛_ −1 _[𝑓]_[.][Therefore,]

**==> picture [422 x 37] intentionally omitted <==**

_5.5. IMPROPER INTEGRALS_

223

**==> picture [255 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
· · ·<br>0 1 2 3 4 5 6 7 8 9 10<br>**----- End of picture text -----**<br>


∞ **Figure 5.10:** The area under the curve, ∫1 _𝑓_ , is bounded below by the area of the shaded rectangles, _𝑓_ (2) + _𝑓_ (3) + _𝑓_ (4) + · · · , and bounded above by the area entire rectangles, _𝑓_ (1) + _𝑓_ (2) + _𝑓_ (3) + · · · .

∞ Suppose first that ∫ _𝑘 𝑓_ converges and let _𝜖>_ 0 be given. As before, since _𝑓_ is positive, _𝑚_ then there exists an _𝐿_ ∈ ℕ such that if _ℓ_ ≥ _𝐿_ , then ∫ _ℓ 𝑓 <[𝜖]_ /2 for all _𝑚_ ≥ _ℓ_ . The function _𝑓_ must decrease to zero (why?), so make _𝐿_ large enough so that for _ℓ_ ≥ _𝐿_ , we have _𝑓_ ( _ℓ_ ) _<[𝜖]_ /2. Thus, for _𝑚 > ℓ_ ≥ _𝐿_ , we have via ( ),

**==> picture [202 x 35] intentionally omitted <==**

The series is therefore Cauchy and thus converges. The estimate in the proposition is obtained by letting _𝑚_ go to infinity in ( ) with _ℓ_ = _𝑘_ .

∞ Conversely, suppose ∫ _𝑘 𝑓_ diverges. As _𝑓_ is positive, then by , the _𝑚_ sequence {∫ _𝑘 𝑓_ }[∞] _𝑚_ = _𝑘_[diverges to infinity.][Using (] ) with _ℓ_ = _𝑘_ , we find

**==> picture [94 x 37] intentionally omitted <==**

_𝑚_ →∞ As the left-hand side goes to infinity as , so does the right-hand side.

**==> picture [9 x 7] intentionally omitted <==**