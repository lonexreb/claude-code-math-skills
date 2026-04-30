Lemma 4.4.1

**Lemma 4.4.1.** _Let 𝐼, 𝐽_ ⊂ ℝ _be intervals. If 𝑓_ : _𝐼_ → _𝐽 is strictly monotone (hence one-to-one), onto ( 𝑓_ ( _𝐼_ ) = _𝐽), differentiable at 𝑥_ 0 ∈ _𝐼, and 𝑓_[′] ( _𝑥_ 0) ≠ 0 _, then the inverse 𝑓_[−][1] _is differentiable at 𝑦_ 0 = _𝑓_ ( _𝑥_ 0) _and_

**==> picture [176 x 30] intentionally omitted <==**

_If 𝑓 is continuously differentiable and 𝑓_[′] _is never zero, then 𝑓_[−][1] _is continuously differentiable._

> _Proof._ By , _𝑓_ has a continuous inverse. For convenience, call the inverse _𝑔_ : _𝐽_ → _𝐼_ . Let _𝑥_ 0 _, 𝑦_ 0 be as in the statement. For _𝑥_ ∈ _𝐼_ , write _𝑦_ � _𝑓_ ( _𝑥_ ). If _𝑥_ ≠ _𝑥_ 0, and so _𝑦_ ≠ _𝑦_ 0, we find

**==> picture [264 x 32] intentionally omitted <==**

See for the geometric idea.

**==> picture [422 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
slope = [푓] [(] [푥] 푥 [)−] − 푥 [푓] 0 [(] [푥] [0][)] = 푔 ( 푦푦 )−− 푦푔 0( 푦 0) 푥 − 푥 0<br>푓 ( 푥 0) = 푦 0 slope = 푓 ( 푥 )− 푓 ( 푥 0) [=] [푔] [(] [푦] 푦 [)−] − 푦 [푔] 0 [(] [푦] [0][)]<br>푥 0 = 푔 ( 푦 0)<br>푓 ( 푥 ) = 푦<br>푥 = 푔 ( 푦 )<br>푥 = 푔 ( 푦 ) 푥 0 = 푔 ( 푦 0) 푓 ( 푥 ) = 푦푓 ( 푥 0) = 푦 0<br>**----- End of picture text -----**<br>


**Figure 4.10:** Interpretation of the derivative of the inverse function.

_4.4. INVERSE FUNCTION THEOREM_

177

Let

**==> picture [285 x 39] intentionally omitted <==**

As _𝑓_ is differentiable at _𝑥_ 0,

**==> picture [252 x 29] intentionally omitted <==**

that is, _𝑄_ is continuous at _𝑥_ 0. As _𝑔_ ( _𝑦_ ) is continuous at _𝑦_ 0, the composition _𝑄_[�] _𝑔_ ( _𝑦_ )[�] = _𝑔_ ( _𝑦_ )− _𝑔_ ( _𝑦_ 0) _𝑦_ − _𝑦_ 0 is continuous at _𝑦_ 0 by . Therefore,

**==> picture [304 x 32] intentionally omitted <==**

1 So _𝑔_ is differentiable at _𝑦_ 0, and _𝑔_[′] ( _𝑦_ 0) = _𝑓_[′] ( _𝑔_ ( _𝑦_ 0))[.]

If _𝑓_[′] is continuous and nonzero at all _𝑥_ ∈ _𝐼_ , then the lemma applies at all _𝑥_ ∈ _𝐼_ . As _𝑔_ is 1 also continuous (it is differentiable), the derivative _𝑔_[′] ( _𝑦_ ) = □ _𝑓_[′] ( _𝑔_ ( _𝑦_ ))[must be continuous.]

What is usually called the inverse function theorem is the following result.

**Theorem 4.4.2** (Inverse function theorem) **.** _Let 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _be a continuously differentiable function, 𝑥_ 0 ∈( _𝑎, 𝑏_ ) _a point where 𝑓_[′] ( _𝑥_ 0) ≠ 0 _. Then there exists an open interval 𝐼_ ⊂( _𝑎, 𝑏_ ) _with 𝑥_ 0 ∈ _𝐼, the restriction 𝑓_ | _𝐼 is injective with a continuously differentiable inverse 𝑔_ : _𝐽_ → _𝐼 defined on an interval 𝐽_ � _𝑓_ ( _𝐼_ ) _, and_

**==> picture [171 x 30] intentionally omitted <==**

_Proof._ Without loss of generality, suppose _𝑓_[′] ( _𝑥_ 0) _>_ 0. As _𝑓_[′] is continuous, there must exist an open interval _𝐼_ = ( _𝑥_ 0 − _𝛿, 𝑥_ 0 + _𝛿_ ) such that _𝑓_[′] ( _𝑥_ ) _>_ 0 for all _𝑥_ ∈ _𝐼_ . See . By , _𝑓_ is strictly increasing on _𝐼_ , and hence the restriction _𝑓_ | _𝐼_ is bĳective onto _𝐽_ := _𝑓_ ( _𝐼_ ). As _𝑓_ is continuous, (or directly via the ) implies that _𝑓_ ( _𝐼_ ) is an interval. Now apply . □

In , we saw how difficult an endeavor was proving the existence of ~~√~~ 2 without any tools. With the , the the existence of roots is almost trivial, and with the machinery of this section, we will prove far more than mere existence. **Corollary 4.4.3.** _Given 𝑛_ ∈ ℕ _and 𝑥_ ≥ 0 _, there exists a unique number 𝑦_ ≥ 0 _(denoted 𝑥_[1][/] _[𝑛]_ � _𝑦), such that 𝑦[𝑛]_ = _𝑥. Furthermore, the function 𝑔_ : (0 _,_ ∞) →(0 _,_ ∞) _defined by 𝑔_ ( _𝑥_ ) � _𝑥_[1][/] _[𝑛] is continuously differentiable and_

**==> picture [158 x 27] intentionally omitted <==**

_𝑚 using the convention 𝑥[𝑚]_[/] _[𝑛]_ � ( _𝑥_[1][/] _[𝑛]_ ) _._

_CHAPTER 4. THE DERIVATIVE_

178

_Proof._ For _𝑥_ = 0, the existence of a unique root is trivial.

Let _𝑓_ : (0 _,_ ∞) →(0 _,_ ∞) be defined by _𝑓_ ( _𝑦_ ) � _𝑦[𝑛]_ . The function _𝑓_ is continuously differentiable, and _𝑓_[′] ( _𝑦_ ) = _𝑛𝑦[𝑛]_[−][1] , see . For _𝑦 >_ 0, the derivative _𝑓_[′] is strictly positive, and so again by , _𝑓_ is strictly increasing (this can also be proved directly) and hence injective. Suppose _𝑀_ and _𝜖_ are such that _𝑀 >_ 1 and 1 _> 𝜖>_ 0. Then _𝑓_ ( _𝑀_ ) = _𝑀[𝑛]_ ≥ _𝑀_ and _𝑓_ ( _𝜖_ ) = _𝜖[𝑛]_ ≤ _𝜖_ . For every _𝑥_ with _𝜖< 𝑥 < 𝑀_ , we have, by the , that _𝑥_ ∈ _𝑓_[�] [ _𝜖, 𝑀_ ][�] ⊂ _𝑓_[�] (0 _,_ ∞)[�] . As _𝑀_ and _𝜖_ were arbitrary, _𝑓_ is onto (0 _,_ ∞), and hence _𝑓_ is bĳective. Let _𝑔_ be the inverse of _𝑓_ , and we obtain the existence and uniqueness of positive _𝑛_ th roots. says that _𝑔_ has a continuous derivative 1 1 and _𝑔_[′] ( _𝑥_ ) = _𝑓_[′] ( _𝑔_ ( _𝑥_ ))[=] _𝑛_ ( _𝑥_[1][/] _[𝑛]_ ) _[𝑛]_[−][1][.] □