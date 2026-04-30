Definition 1.2.9

**Definition 1.2.9.** Let _𝐴_ ⊂ ℝ be a set.

(i) If _𝐴_ is empty, then sup _𝐴_ � −∞.

(ii) If _𝐴_ is not bounded above, then sup _𝐴_ � ∞.

(iii) If _𝐴_ is empty, then inf _𝐴_ � ∞.

(iv) If _𝐴_ is not bounded below, then inf _𝐴_ � −∞.

For convenience, ∞ and −∞ are sometimes treated as if they were numbers, except we do not allow arbitrary arithmetic with them. We make ℝ[∗] � ℝ ∪{−∞ _,_ ∞} into an ordered set by letting

**==> picture [292 x 10] intentionally omitted <==**

_CHAPTER 1. REAL NUMBERS_

34

The set ℝ[∗] is called the set of _extended real numbers_ . It is possible to define some arithmetic on ℝ[∗] . Most operations are extended in an obvious way, but we must leave ∞−∞, 0 · (±∞), and[±∞][We][refrain][from][using][this][arithmetic,][it][leads][to][easy][mistakes][as] ±∞[undefined.] ℝ[∗] is not a field. Now we can take suprema and infima without fear of emptiness or unboundedness. In this book, we mostly avoid using ℝ[∗] outside of exercises and leave such generalizations to the interested reader.

## **1.2.4 Maxima and minima**

By , a finite set of numbers always has a supremum and an infimum and they are both contained in the set itself. In this case, we usually do not use the words supremum or infimum. When a set _𝐴_ of real numbers is bounded above and sup _𝐴_ ∈ _𝐴_ , we can use the word _maximum_ and the notation max _𝐴_ to denote the supremum. Similarly for infimum: When _𝐴_ is bounded below and inf _𝐴_ ∈ _𝐴_ , we can use the word _minimum_ and the notation min _𝐴_ . For example,

**==> picture [135 x 30] intentionally omitted <==**

While writing sup and inf may be technically correct in this situation, max and min are generally used to emphasize that the supremum or infimum is in the set itself, especially when the set is finite.

## **1.2.5 Exercises**

_**Exercise**_ **1.2.1** _**:** Prove that if 𝑡 >_ 0 _(𝑡_ ∈ ℝ _), then there exists an 𝑛_ ∈ ℕ _such that_[1] _[<][𝑡][.] 𝑛_[2]

_**Exercise**_ **1.2.2** _**:** Prove that if 𝑡_ ≥ 0 _(𝑡_ ∈ ℝ _), then there exists an 𝑛_ ∈ ℕ _such that 𝑛_ − 1 ≤ _𝑡 < 𝑛._

_**Exercise**_ **1.2.3** _**:** Finish the proof of ._

_**Exercise**_ **1.2.4** _**:** Let 𝑥, 𝑦_ ∈ ℝ _. Suppose 𝑥_[2] + _𝑦_[2] = 0 _. Prove that 𝑥_ = 0 _and 𝑦_ = 0 _._

_**Exercise**_ **1.2.5** _**:** Show that_ ~~√~~ 3 _is irrational._

_**Exercise**_ **1.2.6** _**:** Let 𝑛_ ∈ ℕ _. Show that_[√] _𝑛 is either an integer or it is irrational._

_**Exercise**_ **1.2.7** _**:** Prove the_ arithmetic-geometric mean inequality _. For two positive real numbers 𝑥, 𝑦,_

**==> picture [66 x 23] intentionally omitted <==**

_Furthermore, equality occurs if and only if 𝑥_ = _𝑦._

_**Exercise**_ **1.2.8** _**:** Show that for every pair of real numbers 𝑥 and 𝑦 such that 𝑥 < 𝑦, there exists an irrational number 𝑠 such that 𝑥 < 𝑠 < 𝑦. Hint: Apply the density of_ ℚ _to[𝑥] and[𝑦] ._ ~~√~~ 2 ~~√~~ 2

_1.2. THE SET OF REAL NUMBERS_

35

_**Exercise**_ **1.2.9** _**:** Let 𝐴 and 𝐵 be two nonempty bounded sets of real numbers. Let 𝐶_ � { _𝑎_ + _𝑏_ : _𝑎_ ∈ _𝐴, 𝑏_ ∈ _𝐵_ } _. Show that 𝐶 is a bounded set and that_

**==> picture [278 x 13] intentionally omitted <==**

_**Exercise**_ **1.2.10** _**:** Let 𝐴 and 𝐵 be two nonempty bounded sets of nonnegative real numbers. Define the set 𝐶_ � { _𝑎𝑏_ : _𝑎_ ∈ _𝐴, 𝑏_ ∈ _𝐵_ } _. Show that 𝐶 is a bounded set and that_

**==> picture [284 x 12] intentionally omitted <==**

_**Exercise**_ **1.2.11** (Hard) _**:** Given 𝑥 >_ 0 _and 𝑛_ ∈ ℕ _, show that there exists a unique positive real number 𝑟 such that 𝑥_ = _𝑟[𝑛] . Usually, 𝑟 is denoted by 𝑥_[1][/] _[𝑛] ._

_**Exercise**_ **1.2.12** (Easy) _**:** Prove ._

_**Exercise**_ **1.2.13** _**:** Prove the so-called_ Bernoulli’s inequality _: If_ 1 + _𝑥 >_ 0 _, then for all 𝑛_ ∈ ℕ _, we have_ (1 + _𝑥_ ) _[𝑛]_ ≥ 1 + _𝑛𝑥._

_**Exercise**_ **1.2.14** _**:** Prove_ sup{ _𝑥_ ∈ ℚ : _𝑥_[2] _<_ 2} = sup{ _𝑥_ ∈ ℝ : _𝑥_[2] _<_ 2} _._

_**Exercise**_ **1.2.15** _**:**_

- _a) Prove that given 𝑦_ ∈ ℝ _, we have_ sup{ _𝑥_ ∈ ℚ : _𝑥 < 𝑦_ } = _𝑦._

- _b) Let 𝐴_ ⊂ ℚ _be a set that is bounded above such that whenever 𝑥_ ∈ _𝐴 and 𝑡_ ∈ ℚ _with 𝑡 < 𝑥, then 𝑡_ ∈ _𝐴. Further suppose_ sup _𝐴_ ∉ _𝐴. Show that there exists a 𝑦_ ∈ ℝ _such that 𝐴_ = { _𝑥_ ∈ ℚ : _𝑥 < 𝑦_ } _. A set such as 𝐴 is called a_ Dedekind cut _._

- _c) Show that there is a bĳection between_ ℝ _and Dedekind cuts._

_Note: Dedekind used sets as in part b) in his construction of the real numbers._

_**Exercise**_ **1.2.16** _**:** Prove that if 𝐴_ ⊂ ℤ _is a nonempty subset bounded below, then there exists a least element in 𝐴. Now describe why this statement would simplify the proof of part so that you do not have to assume 𝑥_ ≥ 0 _._

_**Exercise**_ **1.2.17** _**:** Let us suppose we know 𝑥_[1][/] _[𝑛] exists for every 𝑥 >_ 0 _and every 𝑛_ ∈ ℕ _(see 𝑝 above). For integers 𝑝 and 𝑞 >_ 0 _where[𝑝]_ / _𝑞 is in lowest terms, define 𝑥[𝑝]_[/] _[𝑞]_ � ( _𝑥_[1][/] _[𝑞]_ ) _._

- _a) Show that the power is well-defined even if the fraction is not in lowest terms: If[𝑝]_ / _𝑞_ = _[𝑚]_ / _𝑘 where 𝑚 and 𝑘 >_ 0 _are integers, then_ ( _𝑥_[1][/] _[𝑞]_ ) _𝑝_ = ( _𝑥_ 1/ _𝑘_ ) _𝑚._

- _b) Let 𝑥 and 𝑦 be two positive numbers and 𝑟 a rational number. Assuming 𝑟 >_ 0 _, show 𝑥 < 𝑦 if and only if 𝑥[𝑟] < 𝑦[𝑟] . Then suppose 𝑟 <_ 0 _and show: 𝑥 < 𝑦 if and only if 𝑥[𝑟] > 𝑦[𝑟] ._

- _c) Suppose 𝑥 >_ 1 _and 𝑟, 𝑠 are rational where 𝑟 < 𝑠. Show 𝑥[𝑟] < 𝑥[𝑠] . If_ 0 _< 𝑥 <_ 1 _and 𝑟 < 𝑠, show that 𝑥[𝑟] > 𝑥[𝑠] . Hint: Write 𝑟 and 𝑠 with the same denominator._

- _d) (Challenging) For an irrational 𝑧_ ∈ ℝ \ ℚ _and 𝑥 >_ 1 _define 𝑥[𝑧]_ � sup{ _𝑥[𝑟]_ : _𝑟_ ≤ _𝑧, 𝑟_ ∈ ℚ} _, for 𝑥_ = 1 _define_ 1 _[𝑧]_ = 1 _, and for_ 0 _< 𝑥 <_ 1 _define 𝑥[𝑧]_ � inf{ _𝑥[𝑟]_ : _𝑟_ ≤ _𝑧, 𝑟_ ∈ ℚ} _. Prove the two assertions of part b) for all real 𝑧._

> ‗Named after the Swiss mathematician (1655–1705). † In we will define the exponential and the logarithm and define _𝑥[𝑧]_ � exp( _𝑧_ ln _𝑥_ ). We will then have sufficient machinery to make proofs of these assertions far easier. At this point, however, we do not yet have these tools.

_CHAPTER 1. REAL NUMBERS_

36

## **1.3 Absolute value and bounded functions**

_Note: 0.5–1 lecture_

A concept we will encounter over and over is the concept of _absolute value_ . You want to think of the absolute value as the “size” of a real number. Here is the formal definition:

**==> picture [110 x 39] intentionally omitted <==**

Let us give the main features of the absolute value as a proposition.

## **Proposition 1.3.1.**

_(i)_ | _𝑥_ | ≥ 0 _, moreover,_ | _𝑥_ | = 0 _if and only if 𝑥_ = 0 _._

_(ii)_ |− _𝑥_ | = | _𝑥_ | _for all 𝑥_ ∈ ℝ _._

_(iii)_ �� _𝑥𝑦_ �� = | _𝑥_ | �� _𝑦_ �� _for all 𝑥, 𝑦_ ∈ ℝ _._

_(iv)_ | _𝑥_ |[2] = _𝑥_[2] _for all 𝑥_ ∈ ℝ _._

_(v)_ | _𝑥_ | ≤ _𝑦 if and only if_ − _𝑦_ ≤ _𝑥_ ≤ _𝑦._

_(vi)_ −| _𝑥_ | ≤ _𝑥_ ≤| _𝑥_ | _for all 𝑥_ ∈ ℝ _._

> _Proof._ : First suppose _𝑥_ ≥ 0. Then | _𝑥_ | = _𝑥_ ≥ 0. Also, | _𝑥_ | = _𝑥_ = 0 if and only if _𝑥_ = 0. On the other hand, if _𝑥 <_ 0, then | _𝑥_ | = − _𝑥 >_ 0, and | _𝑥_ | is never zero.

: If _𝑥 >_ 0, then − _𝑥 <_ 0 and so |− _𝑥_ | = −(− _𝑥_ ) = _𝑥_ = | _𝑥_ |. Similarly when _𝑥 <_ 0, or _𝑥_ = 0.

: If _𝑥_ or _𝑦_ is zero, then the result is immediate. When _𝑥_ and _𝑦_ are both positive, then | _𝑥_ | �� _𝑦_ �� = _𝑥𝑦_ . As _𝑥𝑦_ is also positive, _𝑥𝑦_ = �� _𝑥𝑦_ ��. If _𝑥_ and _𝑦_ are both negative, then _𝑥𝑦_ = (− _𝑥_ )(− _𝑦_ ) is still positive and �� _𝑥𝑦_ �� = _𝑥𝑦_ . Also, | _𝑥_ | �� _𝑦_ �� = (− _𝑥_ )(− _𝑦_ ) = _𝑥𝑦_ . If _𝑥 >_ 0 and _𝑦 <_ 0, then | _𝑥_ | �� _𝑦_ �� = _𝑥_ (− _𝑦_ ) = −( _𝑥𝑦_ ). Now _𝑥𝑦_ is negative and �� _𝑥𝑦_ �� = −( _𝑥𝑦_ ). Similarly when _𝑥 <_ 0 and _𝑦 >_ 0.

: Immediate if _𝑥_ ≥ 0. If _𝑥 <_ 0, then | _𝑥_ |[2] = (− _𝑥_ )[2] = _𝑥_[2] .

: Suppose | _𝑥_ | ≤ _𝑦_ . If _𝑥_ ≥ 0, then _𝑥_ ≤ _𝑦_ . It follows that _𝑦_ ≥ 0, leading to − _𝑦_ ≤ 0 ≤ _𝑥_ . So − _𝑦_ ≤ _𝑥_ ≤ _𝑦_ holds. If _𝑥 <_ 0, then | _𝑥_ | ≤ _𝑦_ means − _𝑥_ ≤ _𝑦_ . Negating both sides we get _𝑥_ ≥− _𝑦_ . Again _𝑦_ ≥ 0 and so _𝑦_ ≥ 0 _> 𝑥_ . Hence, − _𝑦_ ≤ _𝑥_ ≤ _𝑦_ .

On the other hand, suppose − _𝑦_ ≤ _𝑥_ ≤ _𝑦_ is true. If _𝑥_ ≥ 0, then _𝑥_ ≤ _𝑦_ is equivalent to | _𝑥_ | ≤ _𝑦_ . If _𝑥 <_ 0, then − _𝑦_ ≤ _𝑥_ implies (− _𝑥_ ) ≤ _𝑦_ , which is equivalent to | _𝑥_ | ≤ _𝑦_ .

: Apply with _𝑦_ = | _𝑥_ |. □

. A property used frequently enough to give it a name is the so-called _triangle inequality_ **Proposition 1.3.2** (Triangle Inequality) **.** | _𝑥_ + _𝑦_ | ≤| _𝑥_ | + | _𝑦_ | _for all 𝑥, 𝑦_ ∈ ℝ _._

_1.3. ABSOLUTE VALUE AND BOUNDED FUNCTIONS_

37

_Proof._ gives −| _𝑥_ | ≤ _𝑥_ ≤| _𝑥_ | and −| _𝑦_ | ≤ _𝑦_ ≤| _𝑦_ |. Add these two inequalities to obtain

**==> picture [162 x 15] intentionally omitted <==**

Apply again to find | _𝑥_ + _𝑦_ | ≤| _𝑥_ | + | _𝑦_ |. □

There are other often applied versions of the triangle inequality.