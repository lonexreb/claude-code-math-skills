Lemma 3.3.7

**Lemma 3.3.7.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function. Suppose 𝑓_ ( _𝑎_ ) _<_ 0 _and 𝑓_ ( _𝑏_ ) _>_ 0 _. Then there exists a number 𝑐_ ∈( _𝑎, 𝑏_ ) _such that 𝑓_ ( _𝑐_ ) = 0 _._

**==> picture [341 x 18] intentionally omitted <==**

- (i) Let _𝑎_ 1 � _𝑎_ and _𝑏_ 1 � _𝑏_ .

**==> picture [276 x 53] intentionally omitted <==**

See for an example defining the first five steps. If _𝑎𝑛 < 𝑏𝑛_ , then _𝑎𝑛 <[𝑎][𝑛]_[+] 2 _[𝑏][𝑛] < 𝑏𝑛_ . So _𝑎𝑛_ +1 _< 𝑏𝑛_ +1. Thus by _𝑎𝑛 < 𝑏𝑛_ for all _𝑛_ . Furthermore, _𝑎𝑛_ ≤ _𝑎𝑛_ +1 and _𝑏𝑛_ ≥ _𝑏𝑛_ +1 for all _𝑛_ , that is, the sequences are monotone. As _𝑎𝑛 < 𝑏𝑛_ ≤ _𝑏_ 1 = _𝑏_ and _𝑏𝑛 > 𝑎𝑛_ ≥ _𝑎_ 1 = _𝑎_ for all _𝑛_ , the sequences are also bounded. Therefore, the sequences converge. Let _𝑐_ � lim _𝑛_ →∞ _𝑎𝑛_ and _𝑑_ � lim _𝑛_ →∞ _𝑏𝑛_ , where also _𝑎_ ≤ _𝑐_ ≤ _𝑑_ ≤ _𝑏_ . We need to show that _𝑐_ = _𝑑_ . Notice

By ,

**==> picture [164 x 73] intentionally omitted <==**

As 2[1][−] _[𝑛]_ ( _𝑏_ − _𝑎_ ) converges to zero, we take the limit as _𝑛_ goes to infinity to get

**==> picture [230 x 20] intentionally omitted <==**

In other words, _𝑑_ = _𝑐_ .

_3.3. EXTREME AND INTERMEDIATE VALUE THEOREMS_

133

**==> picture [219 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
푐<br>푎 1 푏 1<br>푎 2 푏 2<br>푎 3 푏 3<br>푎 4 푏 4<br>푎 5  푏 5<br>**----- End of picture text -----**<br>


**Figure 3.7:** Finding roots (bisection method).

By construction, for all _𝑛_ ,

**==> picture [168 x 14] intentionally omitted <==**

Since lim _𝑛_ →∞ _𝑎𝑛_ = lim _𝑛_ →∞ _𝑏𝑛_ = _𝑐_ and _𝑓_ is continuous at _𝑐_ , we may take limits in those inequalities:

**==> picture [290 x 17] intentionally omitted <==**

As _𝑓_ ( _𝑐_ ) ≥ 0 and _𝑓_ ( _𝑐_ ) ≤ 0, we conclude _𝑓_ ( _𝑐_ ) = 0. Thus also _𝑐_ ≠ _𝑎_ and _𝑐_ ≠ _𝑏_ , so _𝑎 < 𝑐 < 𝑏_ . □

**Theorem 3.3.8** (Bolzano’s intermediate value theorem) **.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function. Suppose 𝑦_ ∈ ℝ _is such that 𝑓_ ( _𝑎_ ) _< 𝑦 < 𝑓_ ( _𝑏_ ) _or 𝑓_ ( _𝑎_ ) _> 𝑦 > 𝑓_ ( _𝑏_ ) _. Then there exists a 𝑐_ ∈( _𝑎, 𝑏_ ) _such that 𝑓_ ( _𝑐_ ) = _𝑦._

The theorem says that a continuous function on a closed interval achieves all the values between the values at the endpoints.

_Proof._ If _𝑓_ ( _𝑎_ ) _< 𝑦 < 𝑓_ ( _𝑏_ ), then define _𝑔_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) − _𝑦_ . Then _𝑔_ ( _𝑎_ ) _<_ 0 and _𝑔_ ( _𝑏_ ) _>_ 0, and we apply to _𝑔_ to find _𝑐_ . If _𝑔_ ( _𝑐_ ) = 0, then _𝑓_ ( _𝑐_ ) = _𝑦_ . Similarly, if _𝑓_ ( _𝑎_ ) _> 𝑦 > 𝑓_ ( _𝑏_ ), then define _𝑔_ ( _𝑥_ ) � _𝑦_ − _𝑓_ ( _𝑥_ ). Again, _𝑔_ ( _𝑎_ ) _<_ 0 and _𝑔_ ( _𝑏_ ) _>_ 0, and we apply to find _𝑐_ . As before, if _𝑔_ ( _𝑐_ ) = 0, then _𝑓_ ( _𝑐_ ) = _𝑦_ . □

If a function is continuous, then the restriction to a subset is continuous; if _𝑓_ : _𝑆_ → ℝ is continuous and [ _𝑎, 𝑏_ ] ⊂ _𝑆_ , then _𝑓_ |[ _𝑎,𝑏_ ] is also continuous. We generally apply the theorem to a function continuous on some large set _𝑆_ , but we restrict our attention to an interval.

_𝑐_ . The proof of the lemma tells us how to find the root The proof is not only useful for us pure mathematicians, it is a useful idea in applied mathematics, where it is called the _bisection method_ .

_CHAPTER 3. CONTINUOUS FUNCTIONS_

134

**Example 3.3.9** (Bisection method) **:** The polynomial _𝑓_ ( _𝑥_ ) � _𝑥_[3] − 2 _𝑥_[2] + _𝑥_ − 1 has a real root in (1 _,_ 2). We simply notice that _𝑓_ (1) = −1 and _𝑓_ (2) = 1. Hence there must exist a point _𝑐_ ∈(1 _,_ 2) such that _𝑓_ ( _𝑐_ ) = 0. To find a better approximation of the root we follow the proof of . We look at 1.5 and find that _𝑓_ (1 _._ 5) = −0 _._ 625. Therefore, there is a root of the polynomial in (1 _._ 5 _,_ 2). Next we look at 1.75 and note that _𝑓_ (1 _._ 75) ≈−0 _._ 016. Hence there is a root of _𝑓_ in (1 _._ 75 _,_ 2). Next we look at 1.875 and find that _𝑓_ (1 _._ 875) ≈ 0 _._ 44, thus there is a root in (1 _._ 75 _,_ 1 _._ 875). We follow this procedure until we gain sufficient precision. In fact, the root is at _𝑐_ ≈ 1 _._ 7549.

The is the method of roots of a common technique simplest finding polynomials, problem in applied mathematics. In general, finding roots is hard to do quickly, precisely, and automatically. There are other, faster methods of finding roots of polynomials, such as Newton’s method. One advantage of the method above is its simplicity. The moment we find an interval where the intermediate value theorem applies, we are guaranteed to find a root up to a desired precision in finitely many steps. Furthermore, the bisection method finds roots of any continuous function, not just a polynomial.

The theorem guarantees one _𝑐_ such that _𝑓_ ( _𝑐_ ) = _𝑦_ , but there may be other roots of the equation _𝑓_ ( _𝑐_ ) = _𝑦_ . If we follow the procedure of the proof, we are guaranteed to find approximations to one such root. We need to work harder to find any other roots.

Polynomials of even degree may not have any real roots. There is no real number _𝑥_ such that _𝑥_[2] + 1 = 0. Odd polynomials, on the other hand, always have at least one real root. **Proposition 3.3.10.** _Let 𝑓_ ( _𝑥_ ) _be a polynomial of odd degree. Then 𝑓 has a real root._

_Proof._ Suppose _𝑓_ is a polynomial of odd degree _𝑑_ . We write

**==> picture [204 x 16] intentionally omitted <==**

**==> picture [314 x 14] intentionally omitted <==**

**==> picture [197 x 15] intentionally omitted <==**

where _𝑏𝑘_ = _[𝑎][𝑘]_ / _𝑎𝑑_ . Let us show that _𝑔_ ( _𝑛_ ) is positive for some large _𝑛_ ∈ ℕ. We first compare the highest order term with the rest:

**==> picture [347 x 160] intentionally omitted <==**

> ‗The word _monic_ means that the coefficient of _𝑥𝑑_ is 1.

_3.3. EXTREME AND INTERMEDIATE VALUE THEOREMS_

135

Therefore,

**==> picture [180 x 29] intentionally omitted <==**

Thus there exists an _𝑀_ ∈ ℕ such that

**==> picture [172 x 31] intentionally omitted <==**

which implies

**==> picture [191 x 15] intentionally omitted <==**

Therefore, _𝑔_ ( _𝑀_ ) _>_ 0.

Next, consider _𝑔_ (− _𝑛_ ) for _𝑛_ ∈ ℕ. By a similar argument, there exists a _𝐾_ ∈ ℕ such that _𝑏𝑑_ −1(− _𝐾_ ) _[𝑑]_[−][1] + · · · + _𝑏_ 1(− _𝐾_ ) + _𝑏_ 0 _< 𝐾[𝑑]_ and therefore _𝑔_ (− _𝐾_ ) _<_ 0 (see ). In the proof, make sure you use the fact that _𝑑_ is odd. In particular, if _𝑑_ is odd, then (− _𝑛_ ) _[𝑑]_ = −( _𝑛[𝑑]_ ). We appeal to the intermediate value theorem to find a _𝑐_ ∈(− _𝐾, 𝑀_ ), such that _𝑔_ ( _𝑐_ ) = 0. As _𝑔_ ( _𝑥_ ) = _[𝑓] 𝑎_[(] _𝑑[𝑥]_[)][, then] _[𝑓]_[(] _[𝑐]_[)][ =][ 0, and the proof is done.] □