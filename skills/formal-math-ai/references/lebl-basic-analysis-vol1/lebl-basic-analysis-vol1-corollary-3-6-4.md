Corollary 3.6.4

**Corollary 3.6.4.** _Let 𝐼_ ⊂ ℝ _be an interval and 𝑓_ : _𝐼_ → ℝ _be monotone. Then 𝑓 has at most countably many discontinuities._

_Proof._ Let _𝐸_ ⊂ _𝐼_ be the set of all discontinuities that are not endpoints of _𝐼_ . As there are only two endpoints, it is enough to show that _𝐸_ is countable. Without loss of generality, suppose _𝑓_ is increasing. We will define an injection _ℎ_ : _𝐸_ → ℚ. For each _𝑐_ ∈ _𝐸_ , both one-sided limits of _𝑓_ exist as _𝑐_ is not an endpoint. Let

**==> picture [450 x 20] intentionally omitted <==**

_3.6. MONOTONE FUNCTIONS AND CONTINUITY_

151

**==> picture [255 x 168] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑓 ( 𝑥 2) 𝑓 ( 𝐼 ) 𝑦 = 𝑓 ( 𝑥 )<br>𝑥 lim→ 𝑐 [+] [𝑓] [(] [𝑥] [)][ =] [ 𝑏]<br>𝑓 ( 𝑐 )<br>lim [𝑎]<br>𝑥 → 𝑐 [−] [𝑓] [(] [𝑥] [)][ =]<br>𝑓 ( 𝑥 1)<br>𝐼<br>𝑥 1 𝑐 𝑥 2<br>**----- End of picture text -----**<br>


**Figure 3.11:** Increasing function _𝑓_ : _𝐼_ → ℝ discontinuity at _𝑐_ .

As _𝑐_ is a discontinuity, _𝑎 < 𝑏_ . There exists a rational number _𝑞_ ∈( _𝑎, 𝑏_ ), so let _ℎ_ ( _𝑐_ ) � _𝑞_ . Suppose _𝑑_ ∈ _𝐸_ is another discontinuity. If _𝑑 > 𝑐_ , there exist an _𝑥_ ∈ _𝐼_ with _𝑐 < 𝑥 < 𝑑_ , and so lim _𝑥_ → _𝑑_ − _𝑓_ ( _𝑥_ ) ≥ _𝑏_ . Hence the rational number we choose for _ℎ_ ( _𝑑_ ) is different from _𝑞_ , since _𝑞_ = _ℎ_ ( _𝑐_ ) _< 𝑏_ and _ℎ_ ( _𝑑_ ) _> 𝑏_ . Similarly if _𝑑 < 𝑐_ . After making such a choice for every element of _𝐸_ , we have a one-to-one (injective) function into ℚ. Therefore, _𝐸_ is countable. □