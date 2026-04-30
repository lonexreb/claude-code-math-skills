Proposition 1.5.3

**Proposition 1.5.3.** _If 𝑥_ ∈(0 _,_ 1] _is a rational number and 𝑥_ = 0 _.𝑑_ 1 _𝑑_ 2 _𝑑_ 3 _. . ., then the decimal digits eventually start repeating. That is, there are positive integers 𝑁 and 𝑃, such that for all 𝑛_ ≥ _𝑁, 𝑑𝑛_ = _𝑑𝑛_ + _𝑃._

_Proof._ Suppose _𝑥_ = _[𝑝]_ / _𝑞_ for positive integers _𝑝_ and _𝑞_ . Suppose also that _𝑥_ is a number with a unique representation, as otherwise we have seen above that both its representations are repeating, see also . This also means that _𝑥_ ≠ 1 so _𝑝 < 𝑞_ .

To compute the first digit, we take 10 _𝑝_ and divide by _𝑞_ . Let _𝑑_ 1 be the quotient, and the remainder _𝑟_ 1 is some integer between 0 and _𝑞_ − 1. That is, _𝑑_ 1 is the largest integer such that _𝑑_ 1 _𝑞_ ≤ 10 _𝑝_ and then _𝑟_ 1 = 10 _𝑝_ − _𝑑_ 1 _𝑞_ . As _𝑝 < 𝑞_ , then _𝑑_ 1 _<_ 10, so _𝑑_ 1 is a digit. Furthermore,

**==> picture [163 x 30] intentionally omitted <==**

The first inequality is strict since _𝑥_ has a unique representation. That is, _𝑑_ 1 really is the first digit. What is left is _[𝑟]_[1] /(10 _𝑞_ ). This is the same as computing the first digit of _[𝑟]_[1] / _𝑞_ . To compute _𝑑_ 2 divide 10 _𝑟_ 1 by _𝑞_ , and so on. After computing _𝑛_ − 1 digits, we have _[𝑝]_ / _𝑞_ = _𝐷𝑛_ −1 + _[𝑟][𝑛]_[−][1] /(10 _[𝑛]_[−][1] _𝑞_ ). To get the _𝑛_ th digit, divide 10 _𝑟𝑛_ −1 by _𝑞_ to get quotient _𝑑𝑛_ , remainder _𝑟𝑛_ , and the inequalities

**==> picture [179 x 30] intentionally omitted <==**

_CHAPTER 1. REAL NUMBERS_

48

Dividing by 10 _[𝑛]_[−][1] and adding _𝐷𝑛_ −1 we find

**==> picture [471 x 100] intentionally omitted <==**

The converse of the proposition is also true and is left as an exercise.