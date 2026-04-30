Example 1.2.3

**Example 1.2.3:** Claim: _There exists a unique positive 𝑟_ ∈ ℝ _such that 𝑟_[2] = 2 _. We denote 𝑟 by_ √2 _._

> ‗Uniqueness is up to isomorphism, but we wish to avoid excessive use of algebra. For us, it is simply enough to assume that a set of real numbers exists. See Rudin [ ] for the construction and more details.

_CHAPTER 1. REAL NUMBERS_

30

_Proof._ Take the set _𝐴_ � { _𝑥_ ∈ ℝ : _𝑥_[2] _<_ 2}. We first show that _𝐴_ is bounded above and nonempty. The inequality _𝑥_ ≥ 2 implies _𝑥_[2] ≥ 4 (see ). So if _𝑥_[2] _<_ 2, then _𝑥 <_ 2. So _𝐴_ is bounded above. As 1 ∈ _𝐴_ , the set _𝐴_ is nonempty. The supremum, therefore, exists.

Let _𝑟_ � sup _𝐴_ . We will show that _𝑟_[2] = 2 by showing that _𝑟_[2] ≥ 2 and _𝑟_[2] ≤ 2. This is the way analysts show equality, by showing two inequalities. We already know that _𝑟_ ≥ 1 _>_ 0.

In the following, it may seem we are pulling certain expressions out of a hat. When writing a proof such as this, we would, of course, come up with the expressions only after playing around with what we wish to prove. The order in which we write the proof is not necessarily the order in which we come up with the proof.

Let us first show that _𝑟_[2] ≥ 2. Take a positive number _𝑠_ such that _𝑠_[2] _<_ 2. We wish to find an _ℎ >_ 0 such that ( _𝑠_ + _ℎ_ )[2] _<_ 2. As 2 − _𝑠_[2] _>_ 0, we have 2[2] _𝑠_[−] + _[𝑠]_ 1[2] _[>]_[0][.][Choose an] _[ℎ]_[∈][ℝ][such] that 0 _< ℎ <_[2][−] _[𝑠]_[2][Furthermore, assume] _[ℎ][<]_[ 1.][Estimate,] 2 _𝑠_ +1[.]

**==> picture [235 x 56] intentionally omitted <==**

Therefore, ( _𝑠_ + _ℎ_ )[2] _<_ 2. Hence _𝑠_ + _ℎ_ ∈ _𝐴_ , but as _ℎ >_ 0, we have _𝑠_ + _ℎ > 𝑠_ . So _𝑠 < 𝑟_ = sup _𝐴_ . As _𝑠_ was an arbitrary positive number such that _𝑠_[2] _<_ 2, it follows that _𝑟_[2] ≥ 2.

Now take a positive number _𝑠_ such that _𝑠_[2] _>_ 2. We wish to find an _ℎ >_ 0 such that ( _𝑠_ − _ℎ_ )[2] _>_ 2 and _𝑠_ − _ℎ_ is still positive. As _𝑠_[2] − 2 _>_ 0, we have _[𝑠]_[2] 2[−] _𝑠_[2] _>_ 0. Let _ℎ_ � _[𝑠]_[2] 2[−] _𝑠_[2][, and] check _𝑠_ − _ℎ_ = _𝑠_ − _[𝑠]_[2] 2[−] _𝑠_[2] = 2 _[𝑠]_[+][1] _𝑠[>]_[0.][Estimate,]

**==> picture [262 x 58] intentionally omitted <==**

By subtracting _𝑠_[2] from both sides and multiplying by −1, we find ( _𝑠_ − _ℎ_ )[2] _>_ 2. Therefore, _𝑠_ − _ℎ_ ∉ _𝐴_ .

Moreover, if _𝑥_ ≥ _𝑠_ − _ℎ_ , then _𝑥_[2] ≥( _𝑠_ − _ℎ_ )[2] _>_ 2 (as _𝑥 >_ 0 and _𝑠_ − _ℎ >_ 0) and so _𝑥_ ∉ _𝐴_ . Thus, _𝑠_ − _ℎ_ is an upper bound for _𝐴_ . However, _𝑠_ − _ℎ < 𝑠_ , or in other words, _𝑠 > 𝑟_ = sup _𝐴_ . Hence, _𝑟_[2] ≤ 2.

Together, _𝑟_[2] ≥ 2 and _𝑟_[2] ≤ 2 imply _𝑟_[2] = 2. The existence part is finished. We still need to handle uniqueness. Suppose _𝑠_ ∈ ℝ such that _𝑠_[2] = 2 and _𝑠 >_ 0. Thus, _𝑠_[2] = _𝑟_[2] . However, if 0 _< 𝑠 < 𝑟_ , then _𝑠_[2] _< 𝑟_[2] . Similarly, 0 _< 𝑟 < 𝑠_ implies _𝑟_[2] _< 𝑠_[2] . Hence, _𝑠_ = _𝑟_ . □

The number √2 ∉ ℚ. The set ℝ \ ℚ is called the set of _irrational_ numbers. We just proved that ℝ \ ℚ is nonempty. Not only is it nonempty, as we will see, it is very large indeed.

Using the same technique as above, we can show that a positive real number _𝑥_[1][/] _[𝑛]_ exists for all _𝑛_ ∈ ℕ and all _𝑥 >_ 0. That is, for each _𝑥 >_ 0, there exists a unique positive real number _𝑟_ such that _𝑟[𝑛]_ = _𝑥_ . The proof is left as an exercise.

_1.2. THE SET OF REAL NUMBERS_

31

## **1.2.2 Archimedean property**

As we have seen, there are plenty of real numbers in any interval. But there are also infinitely many rational numbers in any interval. The following is one of the fundamental facts about the real numbers. The two parts of the next theorem are actually equivalent, even though it may not seem like that at first sight.