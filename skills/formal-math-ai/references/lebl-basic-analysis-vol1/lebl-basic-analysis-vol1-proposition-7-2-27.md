Proposition 7.2.27

**Proposition 7.2.27.** _Let_ ( _𝑋, 𝑑_ ) _be a metric space and 𝐴_ ⊂ _𝑋. Then 𝑥_ ∈ _𝜕𝐴 if and only if for every 𝛿>_ 0 _, 𝐵_ ( _𝑥, 𝛿_ ) ∩ _𝐴 and 𝐵_ ( _𝑥, 𝛿_ ) ∩ _𝐴[𝑐] are both nonempty._

**==> picture [211 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐴 [𝑐]<br>𝛿<br>𝜕𝐴<br>𝑥<br>𝐵 ( 𝑥, 𝛿 )<br>𝐴<br>**----- End of picture text -----**<br>


**Figure 7.9:** Boundary is the set where every ball contains points in the set and also its complement.

_Proof._ Suppose _𝑥_ ∈ _𝜕𝐴_ = _𝐴_ \ _𝐴_[◦] and let _𝛿>_ 0 be arbitrary. By , _𝐵_ ( _𝑥, 𝛿_ ) contains a point of _𝐴_ . If _𝐵_ ( _𝑥, 𝛿_ ) contained no points of _𝐴[𝑐]_ , then _𝑥_ would be in _𝐴_[◦] . Hence _𝐵_ ( _𝑥, 𝛿_ ) contains a point of _𝐴[𝑐]_ as well.

Let us prove the other direction by contrapositive. Suppose _𝑥_ ∉ _𝜕𝐴_ , so _𝑥_ ∉ _𝐴_ or _𝑥_ ∈ _𝐴_[◦] . _𝑐_ If _𝑥_ ∉ _𝐴_ , then _𝐵_ ( _𝑥, 𝛿_ ) ⊂ _𝐴_ for some _𝛿>_ 0 as _𝐴_ is closed. So _𝐵_ ( _𝑥, 𝛿_ ) ∩ _𝐴_ is empty, because _𝑐 𝐴_ ⊂ _𝐴𝑐_ . If _𝑥_ ∈ _𝐴_ ◦, then _𝐵_ ( _𝑥, 𝛿_ ) ⊂ _𝐴_ for some _𝛿>_ 0, so _𝐵_ ( _𝑥, 𝛿_ ) ∩ _𝐴𝑐_ is empty. □

We obtain the following immediate corollary about closures of _𝐴_ and _𝐴[𝑐]_ . We simply . apply