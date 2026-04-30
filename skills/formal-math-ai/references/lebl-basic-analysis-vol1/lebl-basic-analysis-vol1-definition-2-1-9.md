Definition 2.1.9

**Definition 2.1.9.** A sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[is] _[ monotone increasing]_[ if] _[ 𝑥][𝑛]_[≤] _[𝑥][𝑛]_[+][1][for all] _[ 𝑛]_[∈][ℕ][.][A] sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[is] _[ monotone decreasing]_[ if] _[ 𝑥][𝑛]_[≥] _[𝑥][𝑛]_[+][1][for all] _[ 𝑛]_[∈][ℕ][.][If a sequence is either] monotone increasing or monotone decreasing, we can simply say the sequence is _monotone_ .

For example, { _𝑛_ }[∞] _𝑛_ =1[is][monotone][increasing,][{][1][/] _[𝑛]_[}][∞] _𝑛_ =1[is][monotone][decreasing,][the] constant sequence {1}[∞] _𝑛_ =1[is][both][monotone][increasing][and][monotone][decreasing,][and] �(−1) _[𝑛]_[�][∞] _𝑛_ =1[is not monotone.][First few terms of a sample monotone increasing sequence] are shown in .

**==> picture [216 x 129] intentionally omitted <==**

**==> picture [189 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5 6 7 8 9 10<br>**----- End of picture text -----**<br>


**Figure 2.2:** First few terms of a monotone increasing sequence as a graph.

**Theorem 2.1.10** (Monotone convergence theorem) **.** _A monotone sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is bounded] if and only if it is convergent._

_Furthermore, if_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is monotone increasing and bounded, then]_

**==> picture [140 x 17] intentionally omitted <==**

_If_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is monotone decreasing and bounded, then]_

**==> picture [136 x 18] intentionally omitted <==**

_Proof._ Consider a monotone increasing sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[.][Suppose first the sequence is] bounded, that is, the set { _𝑥𝑛_ : _𝑛_ ∈ ℕ} is bounded. Let

**==> picture [112 x 14] intentionally omitted <==**

Let _𝜖>_ 0 be arbitrary. As _𝑥_ is the supremum, there must be at least one _𝑀_ ∈ ℕ such that _𝑥𝑀 > 𝑥_ − _𝜖_ . As { _𝑥𝑛_ }[∞] _𝑛_ =1[is monotone increasing, then it is easy to see (by] ) that _𝑥𝑛_ ≥ _𝑥𝑀_ for all _𝑛_ ≥ _𝑀_ . Hence for all _𝑛_ ≥ _𝑀_ ,

| _𝑥𝑛_ − _𝑥_ | = _𝑥_ − _𝑥𝑛_ ≤ _𝑥_ − _𝑥𝑀 < 𝜖._

> ‗ Some authors use the word _monotonic_ .

_CHAPTER 2. SEQUENCES AND SERIES_

56

So { _𝑥𝑛_ }[∞] _𝑛_ =1[converges to] _[ 𝑥]_[.][Therefore, a bounded monotone increasing sequence converges.] For the other direction, we already proved that a convergent sequence is bounded. The proof for monotone decreasing sequences is left as an exercise. □

A monotone increasing sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[is always bounded from below since] _[𝑥]_[1][≤] _𝑥_ 2 ≤· · · ≤ _𝑥𝑛_ for any _𝑛_ , so _𝑥_ 1 is a lower bound. So to see if a monotone increasing sequence is bounded, it is enough to check if it is bounded above. Similarly, a monotone decreasing sequence is always bounded from above, so it is enough to check whether it is bounded from below.