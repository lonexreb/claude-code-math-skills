Proposition 2.2.5

**Proposition 2.2.5.** _Let_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[and]_[ {] _[𝑦][𝑛]_[}][∞] _𝑛_ =1 _[be convergent sequences.]_

_(i) The sequence_ { _𝑧𝑛_ }[∞] _𝑛_ =1 _[, where][ 𝑧][𝑛]_[�] _[𝑥][𝑛]_[+] _[ 𝑦][𝑛][, converges and]_

**==> picture [228 x 17] intentionally omitted <==**

_(ii) The sequence_ { _𝑧𝑛_ }[∞] _𝑛_ =1 _[, where][ 𝑧][𝑛]_[�] _[𝑥][𝑛]_[−] _[𝑦][𝑛][, converges and]_

**==> picture [228 x 17] intentionally omitted <==**

_(iii) The sequence_ { _𝑧𝑛_ }[∞] _𝑛_ =1 _[, where][ 𝑧][𝑛]_[�] _[𝑥][𝑛][𝑦][𝑛][, converges and]_

**==> picture [229 x 24] intentionally omitted <==**

**==> picture [464 x 69] intentionally omitted <==**

_Proof._ We start with . Suppose { _𝑥𝑛_ }[∞] _𝑛_ =1[and][ {] _[𝑦][𝑛]_[}][∞] _𝑛_ =1[are convergent sequences and write] _𝑧𝑛_ � _𝑥𝑛_ + _𝑦𝑛_ . Let _𝑥_ � lim _𝑛_ →∞ _𝑥𝑛_ , _𝑦_ � lim _𝑛_ →∞ _𝑦𝑛_ , and _𝑧_ � _𝑥_ + _𝑦_ .

Let _𝜖>_ 0 be given. Find an _𝑀_ 1 such that for all _𝑛_ ≥ _𝑀_ 1, we have | _𝑥𝑛_ − _𝑥_ | _<[𝜖]_ /2. Find an _𝑀_ 2 such that for all _𝑛_ ≥ _𝑀_ 2, we have �� _𝑦𝑛_ − _𝑦_ �� _< 𝜖_ /2. Take _𝑀_ � max{ _𝑀_ 1 _, 𝑀_ 2}. For all _𝑛_ ≥ _𝑀_ , we have

**==> picture [156 x 82] intentionally omitted <==**

Therefore is proved. Proof of is almost identical and is left as an exercise.

_CHAPTER 2. SEQUENCES AND SERIES_

64

Let us tackle . Suppose again that { _𝑥𝑛_ }[∞] _𝑛_ =1[and][ {] _[𝑦][𝑛]_[}][∞] _𝑛_ =1[are convergent sequences] and write _𝑧𝑛_ � _𝑥𝑛 𝑦𝑛_ . Let _𝑥_ � lim _𝑛_ →∞ _𝑥𝑛_ , _𝑦_ � lim _𝑛_ →∞ _𝑦𝑛_ , and _𝑧_ � _𝑥𝑦_ .

Let _𝜖>_ 0 be given. Let _𝐾_ � max{| _𝑥_ | _,_ �� _𝑦_ �� _, 𝜖_ /3 _,_ 1}. Find an _𝑀_ 1 such that for all _𝑛_ ≥ _𝑀_ 1, we have | _𝑥𝑛_ − _𝑥_ | _<_ 3 _𝜖𝐾_[.][Find an] _[𝑀]_[2][such that for all] _[ 𝑛]_[≥] _[𝑀]_[2][, we have] �� _𝑦𝑛_ − _𝑦_ �� _<_ 3 _𝜖𝐾_[.][Take] _𝑀_ � max{ _𝑀_ 1 _, 𝑀_ 2}. For all _𝑛_ ≥ _𝑀_ , we have

**==> picture [398 x 146] intentionally omitted <==**

. Finally, we examine Instead of proving directly, we prove the following simpler claim:

Claim: _If_ { _𝑦𝑛_ }[∞] _𝑛_ =1 _[is a convergent sequence such that]_[ lim] _[𝑛]_[→∞] _[𝑦][𝑛]_[≠][0] _[ and][ 𝑦][𝑛]_[≠][0] _[ for all][ 𝑛]_[∈][ℕ] _[,] then_ {[1] / _𝑦𝑛_ }[∞] _𝑛_ =1 _[converges and]_

**==> picture [116 x 29] intentionally omitted <==**

Once the claim is proved, we take the sequence {[1] / _𝑦𝑛_ }[∞] _𝑛_ =1[, multiply it by the sequence] { _𝑥𝑛_ }[∞] _𝑛_ =1[and apply item] .

Proof of claim: Let _𝜖>_ 0 be given. Let _𝑦_ � lim _𝑛_ →∞ _𝑦𝑛_ . As �� _𝑦_ �� ≠ 0, then min _𝑦_ ��2 2 _𝜖[,]_[|] 2 _[𝑦]_[|] _>_ ��� � 0. Find an _𝑀_ such that for all _𝑛_ ≥ _𝑀_ , we have

**==> picture [150 x 38] intentionally omitted <==**

For all _𝑛_ ≥ _𝑀_ , we have �� _𝑦_ − _𝑦𝑛_ �� _<_ | _𝑦_ |/2, and so

**==> picture [248 x 31] intentionally omitted <==**

Subtracting[|] _[𝑦]_[|] /2 from both sides we obtain[|] _[𝑦]_[|] /2 _<_ �� _𝑦𝑛_ ��, or in other words,

**==> picture [55 x 32] intentionally omitted <==**

_2.2. FACTS ABOUT LIMITS OF SEQUENCES_

65

We finish the proof of the claim:

And we are done.

**==> picture [299 x 167] intentionally omitted <==**

By plugging in constant sequences, we get several easy corollaries. If _𝑐_ ∈ ℝ and { _𝑥𝑛_ }[∞] _𝑛_ =1 is a convergent sequence, then for example

**==> picture [324 x 24] intentionally omitted <==**

Similarly, we find such equalities for constant subtraction and division.

As we can take limits past multiplication we can show (exercise) that lim _𝑛_ →∞ _𝑥𝑛[𝑘]_[=] (lim _𝑛_ →∞ _𝑥𝑛_ ) _[𝑘]_ for all _𝑘_ ∈ ℕ. That is, we can take limits past powers. Let us see if we can do the same with roots.