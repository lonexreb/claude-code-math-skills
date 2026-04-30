Proposition 4.2.9

**Proposition 4.2.9.** _Let 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _be continuous. Let 𝑐_ ∈( _𝑎, 𝑏_ ) _and suppose 𝑓 is differentiable on_ ( _𝑎, 𝑐_ ) _and_ ( _𝑐, 𝑏_ ) _._

- _(i) If 𝑓_[′] ( _𝑥_ ) ≤ 0 _whenever 𝑥_ ∈( _𝑎, 𝑐_ ) _and 𝑓_[′] ( _𝑥_ ) ≥ 0 _whenever 𝑥_ ∈( _𝑐, 𝑏_ ) _, then 𝑓 has an absolute minimum at 𝑐._

- _(ii) If 𝑓_[′] ( _𝑥_ ) ≥ 0 _whenever 𝑥_ ∈( _𝑎, 𝑐_ ) _and 𝑓_[′] ( _𝑥_ ) ≤ 0 _whenever 𝑥_ ∈( _𝑐, 𝑏_ ) _, then 𝑓 has an absolute maximum at 𝑐._

> _Proof._ We prove the first item and leave the second to the reader. Take _𝑥_ ∈( _𝑎, 𝑐_ ) and a sequence { _𝑦𝑛_ }[∞] _𝑛_ =1[such][that] _[𝑥][<][𝑦][𝑛][<][𝑐]_[for][all] _[𝑛]_[and][lim] _[𝑛]_[→∞] _[𝑦][𝑛]_[=] _[𝑐]_[.][By][the][preceding] proposition, _𝑓_ is decreasing on ( _𝑎, 𝑐_ ) so _𝑓_ ( _𝑥_ ) ≥ _𝑓_ ( _𝑦𝑛_ ) for all _𝑛_ . As _𝑓_ is continuous at _𝑐_ , we take the limit to get _𝑓_ ( _𝑥_ ) ≥ _𝑓_ ( _𝑐_ ).

Similarly, take _𝑥_ ∈( _𝑐, 𝑏_ ) and { _𝑦𝑛_ }[∞] _𝑛_ =1[a sequence such that] _[ 𝑐][<][𝑦][𝑛][<][𝑥]_[and][ lim] _[𝑛]_[→∞] _[𝑦][𝑛]_[=] _[𝑐]_[.] The function is increasing on ( _𝑐, 𝑏_ ) so _𝑓_ ( _𝑥_ ) ≥ _𝑓_ ( _𝑦𝑛_ ) for all _𝑛_ . By continuity of _𝑓_ , we get _𝑓_ ( _𝑥_ ) ≥ _𝑓_ ( _𝑐_ ). Thus _𝑓_ ( _𝑥_ ) ≥ _𝑓_ ( _𝑐_ ) for all _𝑥_ ∈( _𝑎, 𝑏_ ). □

The converse of the proposition does not hold. See below.

Another often used application of the mean value theorem you have possibly seen in The calculus is the following result on differentiability at the end points of an interval. . proof is

_4.2. MEAN VALUE THEOREM_

167

## **Proposition 4.2.10.**

- _(i) Suppose 𝑓_ : [ _𝑎, 𝑏_ ) → ℝ _is continuous, differentiable in_ ( _𝑎, 𝑏_ ) _, and_ lim _𝑥_ → _𝑎 𝑓_[′] ( _𝑥_ ) = _𝐿. Then 𝑓 is differentiable at 𝑎 and 𝑓_[′] ( _𝑎_ ) = _𝐿._

- _(ii) Suppose 𝑓_ : ( _𝑎, 𝑏_ ] → ℝ _is continuous, differentiable in_ ( _𝑎, 𝑏_ ) _, and_ lim _𝑥_ → _𝑏 𝑓_[′] ( _𝑥_ ) = _𝐿. Then 𝑓 is differentiable at 𝑏 and 𝑓_[′] ( _𝑏_ ) = _𝐿._

In fact, using the extension result , you do not need to assume that _𝑓_ is See . defined at the end point.

## **4.2.5 Continuity of derivatives and the intermediate value theorem**

Derivatives of functions satisfy an intermediate value property.

**Theorem 4.2.11** (Darboux) **.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be differentiable. Suppose 𝑦_ ∈ ℝ _is such that 𝑓_[′] ( _𝑎_ ) _< 𝑦 < 𝑓_[′] ( _𝑏_ ) _or 𝑓_[′] ( _𝑎_ ) _> 𝑦 > 𝑓_[′] ( _𝑏_ ) _. Then there exists a 𝑐_ ∈( _𝑎, 𝑏_ ) _such that 𝑓_[′] ( _𝑐_ ) = _𝑦._

The proof follows by subtracting _𝑓_ and a linear function with derivative _𝑦_ . The new function _𝑔_ reduces the problem to the case _𝑦_ = 0, where _𝑔_[′] ( _𝑎_ ) _>_ 0 _> 𝑔_[′] ( _𝑏_ ). That is, _𝑔_ is increasing at _𝑎_ and decreasing at _𝑏_ , so it must attain a maximum inside ( _𝑎, 𝑏_ ), where the derivative is zero. See .

**==> picture [242 x 102] intentionally omitted <==**

**----- Start of picture text -----**<br>
푔 [′] ( 푐 ) = 0 푔 [′] ( 푏 ) <  0<br>푔 [′] ( 푎 ) >  0<br>푎 푐 푏<br>**----- End of picture text -----**<br>


**Figure 4.6:** Idea of the proof of Darboux theorem.

_Proof._ Suppose _𝑓_[′] ( _𝑎_ ) _< 𝑦 < 𝑓_[′] ( _𝑏_ ). Define

**==> picture [94 x 13] intentionally omitted <==**

The function _𝑔_ is continuous on [ _𝑎, 𝑏_ ], and so _𝑔_ attains a maximum at some _𝑐_ ∈[ _𝑎, 𝑏_ ].

The function _𝑔_ is also differentiable on [ _𝑎, 𝑏_ ]. Compute _𝑔_[′] ( _𝑥_ ) = _𝑦_ − _𝑓_[′] ( _𝑥_ ). Thus _𝑔_[′] ( _𝑎_ ) _>_ 0. As the derivative is the limit of difference quotients and is positive, there must be some difference quotient that is positive. That is, there must exist an _𝑥 > 𝑎_ such that

**==> picture [85 x 28] intentionally omitted <==**

_CHAPTER 4. THE DERIVATIVE_

168

or _𝑔_ ( _𝑥_ ) _> 𝑔_ ( _𝑎_ ). Thus _𝑔_ cannot possibly have a maximum at _𝑎_ . Similarly, as _𝑔_[′] ( _𝑏_ ) _<_ 0, we find an _𝑥 < 𝑏_ (a different _𝑥_ ) such that _[𝑔]_[(] _[𝑥] 𝑥_[)][−] − _𝑏[𝑔]_[(] _[𝑏]_[)] _<_ 0 or that _𝑔_ ( _𝑥_ ) _> 𝑔_ ( _𝑏_ ), thus _𝑔_ cannot possibly have a maximum at _𝑏_ . Therefore, _𝑐_ ∈( _𝑎, 𝑏_ ), and applies: As _𝑔_ attains a maximum at _𝑐_ , we find _𝑔_[′] ( _𝑐_ ) = 0 and so _𝑓_[′] ( _𝑐_ ) = _𝑦_ . Similarly, if _𝑓_[′] ( _𝑎_ ) _> 𝑦 > 𝑓_[′] ( _𝑏_ ), consider _𝑔_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) − _𝑦𝑥_ . □

We have seen already that there exist discontinuous functions that have the intermediate value property. While it is hard to imagine at first, there also exist functions that are differentiable everywhere and the derivative is not continuous.