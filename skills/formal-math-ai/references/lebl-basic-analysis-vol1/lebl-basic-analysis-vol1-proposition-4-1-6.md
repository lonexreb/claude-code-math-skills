Proposition 4.1.6

**Proposition 4.1.6.** _Let 𝑓_ : _𝐼_ → ℝ _be differentiable at 𝑐_ ∈ _𝐼, then it is continuous at 𝑐. Proof._ We know the limits

**==> picture [264 x 28] intentionally omitted <==**

exist. Furthermore,

**==> picture [182 x 32] intentionally omitted <==**

Therefore, the limit of _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ ) exists and

**==> picture [470 x 123] intentionally omitted <==**

**Proposition 4.1.7** (Linearity) **.** _Let 𝐼 be an interval, let 𝑓_ : _𝐼_ → ℝ _and 𝑔_ : _𝐼_ → ℝ _be differentiable at 𝑐_ ∈ _𝐼, and let 𝛼_ ∈ ℝ _._

- _(i) Define ℎ_ : _𝐼_ → ℝ _by ℎ_ ( _𝑥_ ) � _𝛼 𝑓_ ( _𝑥_ ) _. Then ℎ is differentiable at 𝑐 and ℎ_[′] ( _𝑐_ ) = _𝛼 𝑓_[′] ( _𝑐_ ) _._

- _(ii) Define ℎ_ : _𝐼_ → ℝ _by ℎ_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) + _𝑔_ ( _𝑥_ ) _. Then ℎ is differentiable at 𝑐 and ℎ_[′] ( _𝑐_ ) = _𝑓_[′] ( _𝑐_ ) + _𝑔_[′] ( _𝑐_ ) _._

_Proof._ First, let _ℎ_ ( _𝑥_ ) � _𝛼 𝑓_ ( _𝑥_ ). For _𝑥_ ∈ _𝐼_ , _𝑥_ ≠ _𝑐_ ,

**==> picture [235 x 28] intentionally omitted <==**

The limit as _𝑥_ goes to _𝑐_ exists on the right-hand side by . We get

**==> picture [190 x 27] intentionally omitted <==**

_CHAPTER 4. THE DERIVATIVE_

158

Therefore, _ℎ_ is differentiable at _𝑐_ , and the derivative is computed as given. Next, define _ℎ_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) + _𝑔_ ( _𝑥_ ). For _𝑥_ ∈ _𝐼_ , _𝑥_ ≠ _𝑐_ , we have

**==> picture [375 x 30] intentionally omitted <==**

The limit as _𝑥_ goes to _𝑐_ exists on the right-hand side by . We get

**==> picture [274 x 28] intentionally omitted <==**

Therefore, _ℎ_ is differentiable at _𝑐_ , and the derivative is computed as given.

**==> picture [9 x 7] intentionally omitted <==**

It is not true that the derivative of a product of two functions is the product of the derivatives. Instead we get the so-called _product rule_ or the _Leibniz rule_ .

**Proposition 4.1.8** (Product rule) **.** _Let 𝐼 be an interval, let 𝑓_ : _𝐼_ → ℝ _and 𝑔_ : _𝐼_ → ℝ _be functions 𝑐. ℎ_ : _𝐼_ → ℝ _differentiable at If is defined by_

**==> picture [89 x 14] intentionally omitted <==**

_then ℎ is differentiable at 𝑐 and_

**==> picture [148 x 13] intentionally omitted <==**

The proof of the product rule is left as an exercise. The key to the proof is the identity _𝑓_ ( _𝑥_ ) _𝑔_ ( _𝑥_ )− _𝑓_ ( _𝑐_ ) _𝑔_ ( _𝑐_ ) = _𝑓_ ( _𝑥_ )[�] _𝑔_ ( _𝑥_ )− _𝑔_ ( _𝑐_ )[�] +[�] _𝑓_ ( _𝑥_ )− _𝑓_ ( _𝑐_ )[�] _𝑔_ ( _𝑐_ ), which is illustrated in .

**==> picture [213 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑔 ( 𝑥 )<br>𝑓 ( 𝑥 ) [�] 𝑔 ( 𝑥 ) − 𝑔 ( 𝑐 ) [�]<br>𝑔 ( 𝑐 )<br>𝑓 ( 𝑐 ) 𝑔 ( 𝑐 )<br>0<br>0 𝑓 ( 𝑐 ) 𝑓 ( 𝑥 )<br>�<br>𝑓<br>(<br>𝑥<br>) −<br>𝑓<br>(<br>𝑐<br>)<br>�<br>𝑔<br>(<br>𝑐<br>)<br>**----- End of picture text -----**<br>


**Figure 4.2:** The idea of product rule. The area of the entire rectangle _𝑓_ ( _𝑥_ ) _𝑔_ ( _𝑥_ ) differs from the area of the white rectangle _𝑓_ ( _𝑐_ ) _𝑔_ ( _𝑐_ ) by the area of the lightly shaded rectangle _𝑓_ ( _𝑥_ )[�] _𝑔_ ( _𝑥_ ) − _𝑔_ ( _𝑐_ )[�] plus the darker rectangle[�] _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ )[�] _𝑔_ ( _𝑐_ ). In other words, Δ( _𝑓_ · _𝑔_ ) = _𝑓_ · Δ _𝑔_ + Δ _𝑓_ · _𝑔_ .

> ‗Named for the German mathematician (1646–1716).

_4.1. THE DERIVATIVE_

159

**Proposition 4.1.9** (Quotient rule) **.** _Let 𝐼 be an interval, let 𝑓_ : _𝐼_ → ℝ _and 𝑔_ : _𝐼_ → ℝ _be differentiable at 𝑐 and 𝑔_ ( _𝑥_ ) ≠ 0 _for all 𝑥_ ∈ _𝐼. If ℎ_ : _𝐼_ → ℝ _is defined by_

**==> picture [69 x 30] intentionally omitted <==**

_then ℎ is differentiable at 𝑐 and_

**==> picture [151 x 35] intentionally omitted <==**

Again, the proof is left as an exercise.

## **4.1.2 Chain rule**

More complicated functions are often obtained by composition, which is differentiated via the chain rule. The rule also tells us how a derivative changes if we change variables.

**Proposition 4.1.10** (Chain rule) **.** _Let 𝐼_ 1 _, 𝐼_ 2 _be intervals, let 𝑔_ : _𝐼_ 1 → _𝐼_ 2 _be differentiable at 𝑐_ ∈ _𝐼_ 1 _, and 𝑓_ : _𝐼_ 2 → ℝ _be differentiable at 𝑔_ ( _𝑐_ ) _. If ℎ_ : _𝐼_ 1 → ℝ _is defined by_

**==> picture [148 x 15] intentionally omitted <==**

_then ℎ is differentiable at 𝑐 and_

**==> picture [109 x 15] intentionally omitted <==**

_Proof._ Let _𝑑_ � _𝑔_ ( _𝑐_ ). Define _𝑢_ : _𝐼_ 2 → ℝ and _𝑣_ : _𝐼_ 1 → ℝ by

**==> picture [314 x 39] intentionally omitted <==**

Because _𝑓_ is differentiable at _𝑑_ = _𝑔_ ( _𝑐_ ), we find that _𝑢_ is continuous at _𝑑_ . Similarly, _𝑣_ is continuous at _𝑐_ . For any _𝑥_ and _𝑦_ ,

**==> picture [330 x 13] intentionally omitted <==**

Plug in to obtain

**==> picture [410 x 15] intentionally omitted <==**

Therefore, if _𝑥_ ≠ _𝑐_ ,

**==> picture [305 x 27] intentionally omitted <==**

By continuity of _𝑢_ and _𝑣_ at _𝑑_ and _𝑐_ respectively, we find lim _𝑦_ → _𝑑 𝑢_ ( _𝑦_ ) = _𝑓_[′] ( _𝑑_ ) = _𝑓_[′][�] _𝑔_ ( _𝑐_ )[�] and lim _𝑥_ → _𝑐 𝑣_ ( _𝑥_ ) = _𝑔_[′] ( _𝑐_ ). The function _𝑔_ is continuous at _𝑐_ , and so lim _𝑥_ → _𝑐 𝑔_ ( _𝑥_ ) = _𝑔_ ( _𝑐_ ). Hence the limit of the right-hand side of ( ) as _𝑥_ goes to _𝑐_ exists and is equal to _𝑓_[′][�] _𝑔_ ( _𝑐_ )[�] _𝑔_[′] ( _𝑐_ ). Thus _ℎ_ is differentiable at _𝑐_ and _ℎ_[′] ( _𝑐_ ) = _𝑓_[′][�] _𝑔_ ( _𝑐_ )[�] _𝑔_[′] ( _𝑐_ ). □

_CHAPTER 4. THE DERIVATIVE_

160

## **4.1.3 Exercises**

_**Exercise**_ **4.1.1** _**:** Prove the product rule. Hint: Prove and use 𝑓_ ( _𝑥_ ) _𝑔_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ ) _𝑔_ ( _𝑐_ ) = _𝑓_ ( _𝑥_ )[�] _𝑔_ ( _𝑥_ ) − _𝑔_ ( _𝑐_ )[�] + � _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ )[�] _𝑔_ ( _𝑐_ ) _._

_**Exercise**_ **4.1.2** _**:** Prove the quotient rule. Hint: You can do this directly, but it may be easier to find the derivative of_[1] / _𝑥 and then use the chain rule and the product rule._

_**Exercise**_ **4.1.3** _**:** For 𝑛_ ∈ ℤ _, prove that 𝑥[𝑛] is differentiable and find the derivative, unless, of course, 𝑛 <_ 0 _and 𝑥_ = 0 _. Hint: Use the product rule._

_**Exercise**_ **4.1.4** _**:** Prove that a polynomial is differentiable, and find the derivative. Hint: Use the previous exercise._

_**Exercise**_ **4.1.5** _**:** Define 𝑓_ : ℝ → ℝ _by_

**==> picture [110 x 35] intentionally omitted <==**

_Prove that 𝑓 is differentiable at_ 0 _, but discontinuous at all points except_ 0 _._

_**Exercise**_ **4.1.6** _**:** Assume the inequality_ | _𝑥_ − sin( _𝑥_ )| ≤ _𝑥_[2] _. Prove that_ sin _is differentiable at_ 0 _, and find the derivative at_ 0 _._

_**Exercise**_ **4.1.7** _**:** Using the previous exercise, prove that_ sin _is differentiable at all 𝑥 and that the derivative is_ cos( _𝑥_ ) _. Hint: Use the sum-to-product trigonometric identity as we did before._

_**Exercise**_ **4.1.8** _**:** Let 𝑓_ : _𝐼_ → ℝ _be differentiable. For 𝑛_ ∈ ℤ _, let 𝑓[𝑛] be the function defined by 𝑓[𝑛]_ ( _𝑥_ ) �[�] _𝑓_ ( _𝑥_ )[�] _[𝑛] . If 𝑛 <_ 0 _, assume 𝑓_ ( _𝑥_ ) ≠ 0 _for all 𝑥_ ∈ _𝐼. Prove that_ ( _𝑓[𝑛]_ )[′] ( _𝑥_ ) = _𝑛_[�] _𝑓_ ( _𝑥_ )[�] _[𝑛]_[−][1] _𝑓_[′] ( _𝑥_ ) _._

_**Exercise**_ **4.1.9** _**:** Suppose 𝑓_ : ℝ → ℝ _is a differentiable Lipschitz continuous function. Prove that 𝑓_[′] _is a bounded function._

_**Exercise**_ **4.1.10** _**:** Let 𝐼_ 1 _, 𝐼_ 2 _be intervals. Let 𝑓_ : _𝐼_ 1 → _𝐼_ 2 _be a bĳective function and 𝑔_ : _𝐼_ 2 → _𝐼_ 1 _be the inverse. Suppose that both 𝑓 is differentiable at 𝑐_ ∈ _𝐼_ 1 _and 𝑓_[′] ( _𝑐_ ) ≠ 0 _and 𝑔 is differentiable at 𝑓_ ( _𝑐_ ) _. Use the chain rule to find a formula for 𝑔_[′][�] _𝑓_ ( _𝑐_ )[�] _(in terms of 𝑓_[′] ( _𝑐_ ) _)._

_**Exercise**_ **4.1.11** _**:** Suppose 𝑓_ : _𝐼_ → ℝ _is bounded, 𝑔_ : _𝐼_ → ℝ _is differentiable at 𝑐_ ∈ _𝐼, and 𝑔_ ( _𝑐_ ) = _𝑔_[′] ( _𝑐_ ) = 0 _. Show that ℎ_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) _𝑔_ ( _𝑥_ ) _is differentiable at 𝑐. Hint: You cannot apply the product rule._

_**Exercise**_ **4.1.12** _**:** Suppose 𝑓_ : _𝐼_ → ℝ _, 𝑔_ : _𝐼_ → ℝ _, and ℎ_ : _𝐼_ → ℝ _, are functions. Suppose 𝑐_ ∈ _𝐼 is such that 𝑓_ ( _𝑐_ ) = _𝑔_ ( _𝑐_ ) = _ℎ_ ( _𝑐_ ) _, 𝑔 and ℎ are differentiable at 𝑐, and 𝑔_[′] ( _𝑐_ ) = _ℎ_[′] ( _𝑐_ ) _. Furthermore, suppose ℎ_ ( _𝑥_ ) ≤ _𝑓_ ( _𝑥_ ) ≤ _𝑔_ ( _𝑥_ ) _for all 𝑥_ ∈ _𝐼. Prove 𝑓 is differentiable at 𝑐 and 𝑓_[′] ( _𝑐_ ) = _𝑔_[′] ( _𝑐_ ) = _ℎ_[′] ( _𝑐_ ) _._

_**Exercise**_ **4.1.13** _**:** Suppose 𝑓_ : (−1 _,_ 1) → ℝ _is a function such that 𝑓_ ( _𝑥_ ) = _𝑥ℎ_ ( _𝑥_ ) _for a bounded function ℎ. a) Show that 𝑔_ ( _𝑥_ ) �[�] _𝑓_ ( _𝑥_ )[�][2] _is differentiable at the origin and 𝑔_[′] (0) = 0 _._

- _b) Find an example of a continuous function 𝑓_ : (−1 _,_ 1) → ℝ _with 𝑓_ (0) = 0 _, but such that 𝑔_ ( _𝑥_ ) �[�] _𝑓_ ( _𝑥_ )[�][2] _is not differentiable at the origin._

_4.1. THE DERIVATIVE_

161

_**Exercise**_ **4.1.14** _**:** Suppose 𝑓_ : _𝐼_ → ℝ _is differentiable at 𝑐_ ∈ _𝐼. Prove that there exist numbers 𝑎 and 𝑏 with the property that for every 𝜖>_ 0 _, there is a 𝛿>_ 0 _, such that_ �� _𝑎_ + _𝑏_ ( _𝑥_ − _𝑐_ ) − _𝑓_ ( _𝑥_ )�� ≤ _𝜖_ | _𝑥_ − _𝑐_ | _, whenever 𝑥_ ∈ _𝐼 and_ | _𝑥_ − _𝑐_ | _< 𝛿. In other words, show that there exists a function 𝑔_ : _𝐼_ → ℝ _such that_ lim _𝑥_ → _𝑐 𝑔_ ( _𝑥_ ) = 0 _and_ �� _𝑎_ + _𝑏_ ( _𝑥_ − _𝑐_ ) − _𝑓_ ( _𝑥_ )�� = _𝑔_ ( _𝑥_ ) | _𝑥_ − _𝑐_ | _._

_**Exercise**_ **4.1.15** _**:** Prove the following simple version of L’Hôpital’s rule. Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _and 𝑔_ : ( _𝑎, 𝑏_ ) → ℝ _are differentiable functions whose derivatives 𝑓_[′] _and 𝑔_[′] _are continuous functions. Suppose that at 𝑐_ ∈( _𝑎, 𝑏_ ) _, 𝑓_ ( _𝑐_ ) = 0 _, 𝑔_ ( _𝑐_ ) = 0 _, 𝑔_[′] ( _𝑥_ ) ≠ 0 _for all 𝑥_ ∈( _𝑎, 𝑏_ ) _, and 𝑔_ ( _𝑥_ ) ≠ 0 _whenever 𝑥_ ≠ _𝑐. Note that the limit of[𝑓]_[′][(] _[𝑥]_[)] / _𝑔_[′] ( _𝑥_ ) _as 𝑥 goes to 𝑐 exists. Show that_

**==> picture [104 x 28] intentionally omitted <==**

_**Exercise**_ **4.1.16** _**:** Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _is differentiable at 𝑐_ ∈( _𝑎, 𝑏_ ) _, 𝑓_ ( _𝑐_ ) = 0 _, and 𝑓_[′] ( _𝑐_ ) _>_ 0 _. Prove that there is a 𝛿>_ 0 _such that 𝑓_ ( _𝑥_ ) _<_ 0 _whenever 𝑐_ − _𝛿< 𝑥 < 𝑐 and 𝑓_ ( _𝑥_ ) _>_ 0 _whenever 𝑐 < 𝑥 < 𝑐_ + _𝛿._

_CHAPTER 4. THE DERIVATIVE_

162

## **4.2 Mean value theorem**

_Note: 2 lectures (some applications may be skipped)_

## **4.2.1 Relative minima and maxima**

We previously talked about absolute maxima and minima. These are the tallest peaks and the lowest valleys in the entire mountain range. What about peaks of individual mountains and bottoms of individual valleys? The derivative, being a local concept, is like walking around in a fog; it cannot tell you if you are on the highest peak, but it can tell you whether you are at the top of some peak.