Proposition 2.3.7

**Proposition 2.3.7.** _A bounded sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is convergent and converges to][𝑥][if and only if] every convergent subsequence_ { _𝑥𝑛𝑘_ }[∞] _𝑘_ =1 _[converges to][ 𝑥][.]_

_CHAPTER 2. SEQUENCES AND SERIES_

78

## **2.3.3 Bolzano–Weierstrass theorem**

While it is not true that a bounded is the Bolzano–Weierstrass sequence convergent, theorem tells us that we can at least find a convergent subsequence. The version of Bolzano–Weierstrass we present in this section is the Bolzano–Weierstrass for sequences of real numbers.

**Theorem 2.3.8** (Bolzano–Weierstrass) **.** _Suppose a sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[of real numbers is bounded.] Then there exists a convergent subsequence_ { _𝑥𝑛𝑖_ }[∞] _𝑖_ =1 _[.]_

_Proof._ says that there exists a subsequence whose limit is lim sup _𝑛_ →∞ _𝑥𝑛_ . □

The reader might complain right now that is strictly stronger than the Bolzano–Weierstrass theorem as presented above. That is true. However, only applies to the real line, but Bolzano–Weierstrass applies in more general contexts (that is, in ℝ _[𝑛]_ ) with pretty much the exact same statement.

As the theorem is so important to analysis, we present an explicit proof. The idea of the following proof also generalizes to different contexts.

_Alternate proof of Bolzano–Weierstrass._ As the sequence is bounded, there exist two numbers _𝑎_ 1 _< 𝑏_ 1 such that _𝑎_ 1 ≤ _𝑥𝑛_ ≤ _𝑏_ 1 for all _𝑛_ ∈ ℕ. We will define a subsequence { _𝑥𝑛𝑖_ }[∞] _𝑖_ =1[and two] sequences { _𝑎𝑖_ }[∞] _𝑖_ =1[and][ {] _[𝑏][𝑖]_[}][∞] _𝑖_ =1[, such that][ {] _[𝑎][𝑖]_[}][∞] _𝑖_ =1[is monotone increasing,][ {] _[𝑏][𝑖]_[}][∞] _𝑖_ =1[is monotone] decreasing, _𝑎𝑖_ ≤ _𝑥𝑛𝑖_ ≤ _𝑏𝑖_ and such that lim _𝑖_ →∞ _𝑎𝑖_ = lim _𝑖_ →∞ _𝑏𝑖_ . That { _𝑥𝑛𝑖_ }[∞] _𝑖_ =1[converges] . then follows by the

We define the sequences inductively. We will define the sequences so that for all _𝑖_ , we have _𝑎𝑖 < 𝑏𝑖_ , and that _𝑥𝑛_ ∈[ _𝑎𝑖 , 𝑏𝑖_ ] for infinitely many _𝑛_ ∈ ℕ. We have already defined _𝑎_ 1 and _𝑏_ 1. We take _𝑛_ 1 � 1, that is _𝑥𝑛_ 1 = _𝑥_ 1. Suppose that up to some _𝑘_ ∈ ℕ, we have defined the subsequence _𝑥𝑛_ 1 _, 𝑥𝑛_ 2 _, . . . , 𝑥𝑛𝑘_ , and the sequences _𝑎_ 1 _, 𝑎_ 2 _, . . . , 𝑎𝑘_ and _𝑏_ 1 _, 𝑏_ 2 _, . . . , 𝑏𝑘_ . Let _𝑦_ � _[𝑎][𝑘]_[+] 2 _[𝑏][𝑘]_ . Clearly _𝑎𝑘 < 𝑦 < 𝑏𝑘_ . If there exist infinitely many _𝑗_ ∈ ℕ such that _𝑥 𝑗_ ∈[ _𝑎𝑘 , 𝑦_ ], then set _𝑎𝑘_ +1 � _𝑎𝑘_ , _𝑏𝑘_ +1 � _𝑦_ , and pick _𝑛𝑘_ +1 _> 𝑛𝑘_ such that _𝑥𝑛𝑘_ +1 ∈[ _𝑎𝑘 , 𝑦_ ]. If there are not infinitely many _𝑗_ such that _𝑥 𝑗_ ∈[ _𝑎𝑘 , 𝑦_ ], then it must be true that there are infinitely many _𝑗_ ∈ ℕ such that _𝑥 𝑗_ ∈[ _𝑦, 𝑏𝑘_ ]. In this case pick _𝑎𝑘_ +1 � _𝑦_ , _𝑏𝑘_ +1 � _𝑏𝑘_ , and pick _𝑛𝑘_ +1 _> 𝑛𝑘_ such that _𝑥𝑛𝑘_ +1 ∈[ _𝑦, 𝑏𝑘_ ].

We now have the sequences defined. What is left to prove is that lim _𝑖_ →∞ _𝑎𝑖_ = lim _𝑖_ →∞ _𝑏𝑖_ . − The limits exist as the sequences are monotone. In the construction, _𝑏𝑖 𝑎𝑖_ is cut in half in each step. Therefore, _𝑏𝑖_ +1 − _𝑎𝑖_ +1 = _[𝑏][𝑖]_[−] 2 _[𝑎][𝑖]_[.][By] ,

**==> picture [89 x 26] intentionally omitted <==**

Let _𝑥_ � lim _𝑖_ →∞ _𝑎𝑖_ . As { _𝑎𝑖_ }[∞] _𝑖_ =1[is monotone,]

**==> picture [104 x 14] intentionally omitted <==**

Let _𝑦_ � lim _𝑖_ →∞ _𝑏𝑖_ = inf{ _𝑏𝑖_ : _𝑖_ ∈ ℕ}. Since _𝑎𝑖 < 𝑏𝑖_ for all _𝑖_ , then _𝑥_ ≤ _𝑦_ . As the sequences are monotone, then for all _𝑖_ , we have (why?)

**==> picture [131 x 27] intentionally omitted <==**

_2.3. LIMIT SUPERIOR, LIMIT INFERIOR, AND BOLZANO–WEIERSTRASS_

79

Because _[𝑏]_ 2[1][−] _[𝑖]_[−] _[𝑎]_[1][1][is arbitrarily small and] _[ 𝑦]_[−] _[𝑥]_[≥][0][, we have] _[ 𝑦]_[−] _[𝑥]_[=][ 0][.][Finish by the] . □

Yet another proof of the Bolzano–Weierstrass theorem is to show the following claim, which is left as a challenging exercise. _Claim: Every sequence has a monotone subsequence_ .

## **2.3.4 Infinite limits**

Just as for infima and suprema, it is possible to allow certain limits to be infinite. That is, we write lim _𝑛_ →∞ _𝑥𝑛_ = ∞ or lim _𝑛_ →∞ _𝑥𝑛_ = −∞ for certain divergent sequences.