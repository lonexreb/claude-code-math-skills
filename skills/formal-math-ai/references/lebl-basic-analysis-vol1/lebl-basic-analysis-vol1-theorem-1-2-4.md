Theorem 1.2.4

**Theorem 1.2.4.**

_(i) (Archimedean property) If 𝑥, 𝑦_ ∈ ℝ _and 𝑥 >_ 0 _, then there exists an 𝑛_ ∈ ℕ _such that_

**==> picture [41 x 11] intentionally omitted <==**

_(ii) (_ ℚ _is dense in_ ℝ _) If 𝑥, 𝑦_ ∈ ℝ _and 𝑥 < 𝑦, then there exists an 𝑟_ ∈ ℚ _such that 𝑥 < 𝑟 < 𝑦._

_Proof._ Let us prove . Divide through by _𝑥_ . Then says that for every real number _𝑡_ � _[𝑦]_ / _𝑥_ , we can find _𝑛_ ∈ ℕ such that _𝑛 > 𝑡_ . In other words, says that ℕ ⊂ ℝ is not bounded above. Suppose for contradiction that ℕ is bounded above. Let _𝑏_ � sup ℕ. The number _𝑏_ − 1 cannot possibly be an upper bound for ℕ as it is strictly less than _𝑏_ (the least upper bound). Thus there exists an _𝑚_ ∈ ℕ such that _𝑚 > 𝑏_ − 1. Add one to obtain _𝑚_ + 1 _> 𝑏_ , contradicting _𝑏_ being an upper bound.

**==> picture [219 x 64] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑚 −1 𝑚 𝑚 +1<br>𝑛 𝑛 𝑛<br>1<br>𝑛<br>𝑥 𝑦<br>**----- End of picture text -----**<br>


**Figure 1.2:** Idea of the proof of the density of ℚ: Find _𝑛_ such that _𝑦_ − _𝑥 >_[1] / _𝑛_ , then take the least _𝑚_ such that _[𝑚]_ / _𝑛 > 𝑥_ .

Let us tackle . See for a picture of the idea behind the proof. First assume _𝑥_ ≥ 0. Note that _𝑦_ − _𝑥 >_ 0. By , there exists an _𝑛_ ∈ ℕ such that

**==> picture [184 x 14] intentionally omitted <==**

Again by the set _𝐴_ � { _𝑘_ ∈ ℕ : _𝑘 > 𝑛𝑥_ } is nonempty. By the of ℕ, _𝐴_ has a least element _𝑚_ , and as _𝑚_ ∈ _𝐴_ , then _𝑚 > 𝑛𝑥_ . Divide through by _𝑛_ to get _𝑥 <[𝑚]_ / _𝑛_ . As _𝑚_ is the least element of _𝐴_ , _𝑚_ − 1 ∉ _𝐴_ . If _𝑚 >_ 1, then _𝑚_ − 1 ∈ ℕ, but _𝑚_ − 1 ∉ _𝐴_ and so _𝑚_ − 1 ≤ _𝑛𝑥_ . If _𝑚_ = 1, then _𝑚_ − 1 = 0, and _𝑚_ − 1 ≤ _𝑛𝑥_ still holds as _𝑥_ ≥ 0. In other words,

**==> picture [182 x 10] intentionally omitted <==**

On the other hand, from _𝑛_ ( _𝑦_ − _𝑥_ ) _>_ 1 we obtain _𝑛𝑦 >_ 1 + _𝑛𝑥_ . Hence _𝑛𝑦 >_ 1 + _𝑛𝑥_ ≥ _𝑚_ , and therefore _𝑦 >[𝑚]_ / _𝑛_ . Putting everything together, we obtain _𝑥 <[𝑚]_ / _𝑛 < 𝑦_ . So take _𝑟_ = _[𝑚]_ / _𝑛_ .

> ‗Named after the Ancient Greek mathematician (c. 287 BC – c. 212 BC). This property is Axiom V from Archimedes’ “On the Sphere and Cylinder” 225 BC.

_CHAPTER 1. REAL NUMBERS_

32

Now assume _𝑥 <_ 0. If _𝑦 >_ 0, then just take _𝑟_ = 0. If _𝑦_ ≤ 0, then 0 ≤− _𝑦 <_ − _𝑥_ , and we find a rational _𝑞_ such that − _𝑦 < 𝑞 <_ − _𝑥_ . Then take _𝑟_ = − _𝑞_ . □

. Let us state and prove a simple but useful corollary of the **Corollary 1.2.5.** inf{[1] / _𝑛_ : _𝑛_ ∈ ℕ} = 0 _. See ._

_Proof._ Let _𝐴_ � {[1] / _𝑛_ : _𝑛_ ∈ ℕ}. Obviously, _𝐴_ is not empty. Furthermore,[1] / _𝑛 >_ 0 for all _𝑛_ ∈ ℕ, so 0 is a lower bound and _𝑏_ � inf _𝐴_ exists. As 0 is a lower bound, then _𝑏_ ≥ 0. Take an arbitrary _𝑎 >_ 0. By the , there exists an _𝑛_ such that _𝑛𝑎 >_ 1, that is, _𝑎 >_[1] / _𝑛_ ∈ _𝐴_ . Therefore, _𝑎_ cannot be a lower bound for _𝐴_ . Hence _𝑏_ = 0. □

**==> picture [244 x 23] intentionally omitted <==**

**----- Start of picture text -----**<br>
0 · · · 18 17 16 15 14 13 12 1<br>**----- End of picture text -----**<br>


**Figure 1.3:** The set {[1] / _𝑛_ : _𝑛_ ∈ ℕ} and its infimum 0.

## **1.2.3 Using supremum and infimum**

For a set _𝐴_ ⊂ ℝ and _𝑥_ ∈ ℝ Suprema and infima are compatible with algebraic operations. define

**==> picture [154 x 32] intentionally omitted <==**

For example, if _𝐴_ = {1 _,_ 2 _,_ 3}, then 5 + _𝐴_ = {6 _,_ 7 _,_ 8} and 3 _𝐴_ = {3 _,_ 6 _,_ 9}.