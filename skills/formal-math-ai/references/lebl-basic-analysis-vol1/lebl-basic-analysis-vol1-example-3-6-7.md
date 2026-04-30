Example 3.6.7

**Example 3.6.7:** The proposition does not require _𝑓_ itself to be continuous. Let _𝑓_ : ℝ → ℝ be defined by

**==> picture [128 x 39] intentionally omitted <==**

The function _𝑓_ is not continuous at 0. The image of _𝐼_ = ℝ is the set (−∞ _,_ 0) ∪[1 _,_ ∞), not an interval. Then _𝑓_[−][1] : (−∞ _,_ 0) ∪[1 _,_ ∞) → ℝ can be written as

**==> picture [136 x 38] intentionally omitted <==**

It is not difficult to see that _𝑓_[−][1] is a continuous function. See for the graphs.

Notice what happens with the proposition if _𝑓_ ( _𝐼_ ) is an interval. In that case, we could simply apply to both _𝑓_ and _𝑓_[−][1] . That is, if _𝑓_ : _𝐼_ → _𝐽_ is an onto strictly monotone function and _𝐼_ and _𝐽_ are intervals, then both _𝑓_ and _𝑓_[−][1] are continuous. Furthermore, _𝑓_ ( _𝐼_ ) is an interval precisely when _𝑓_ is continuous.

_3.6. MONOTONE FUNCTIONS AND CONTINUITY_

153

**==> picture [133 x 132] intentionally omitted <==**

**==> picture [133 x 132] intentionally omitted <==**

**Figure 3.13:** Graph of _𝑓_ on the left and _𝑓_[−][1] on the right.

## **3.6.3 Exercises**

_**Exercise**_ **3.6.1** _**:** Suppose 𝑓_ : [0 _,_ 1] → ℝ _is monotone. Prove 𝑓 is bounded._

_**Exercise**_ **3.6.2** _**:** Finish the proof of . Hint: You can halve your work by noticing that if 𝑔 is_ − _decreasing, then 𝑔 is increasing._

_**Exercise**_ **3.6.3** _**:** Finish the proof of ._

_**Exercise**_ **3.6.4** _**:** Prove the claims in ._

_**Exercise**_ **3.6.5** _**:** Finish the proof of ._

_**Exercise**_ **3.6.6** _**:** Suppose 𝑆_ ⊂ ℝ _, and 𝑓_ : _𝑆_ → ℝ _is an increasing function. Prove:_

_a) If 𝑐 is a cluster point of 𝑆_ ∩( _𝑐,_ ∞) _, then 𝑥_ lim→ _𝑐_[+] _[𝑓]_[(] _[𝑥]_[)] _[ <]_[∞] _[.]_

_b) If 𝑐 is a cluster point of 𝑆_ ∩(−∞ _, 𝑐_ ) _and_ lim _𝑥_ → _𝑐_[−] _[𝑓]_[(] _[𝑥]_[)][ =][ ∞] _[, then][ 𝑆]_[⊂(−∞] _[, 𝑐]_[)] _[.]_

_**Exercise**_ **3.6.7** _**:** Let 𝐼_ ⊂ ℝ _be an interval and 𝑓_ : _𝐼_ → ℝ _a function. Suppose that for each 𝑐_ ∈ _𝐼, there exist 𝑎, 𝑏_ ∈ ℝ _with 𝑎 >_ 0 _such that 𝑓_ ( _𝑥_ ) ≥ _𝑎𝑥_ + _𝑏 for all 𝑥_ ∈ _𝐼 and 𝑓_ ( _𝑐_ ) = _𝑎𝑐_ + _𝑏. Show that 𝑓 is strictly increasing._

_**Exercise**_ **3.6.8** _**:** Suppose 𝐼 and 𝐽 are intervals and 𝑓_ : _𝐼_ → _𝐽 is a continuous, bĳective (one-to-one and onto) function. Show that 𝑓 is strictly monotone._

_**Exercise**_ **3.6.9** _**:** Consider a monotone function 𝑓_ : _𝐼_ → ℝ _on an interval 𝐼. Prove that there exists a function 𝑔_ : _𝐼_ → ℝ _such that_ lim[=] _[𝑔]_[(] _[𝑐]_[)] _[ for all][𝑐][in][𝐼][except the smaller (left) endpoint of][𝐼][, and such that] 𝑥_ → _𝑐_[−] _[𝑔]_[(] _[𝑥]_[)] _𝑔_ ( _𝑥_ ) = _𝑓_ ( _𝑥_ ) _for all but countably many 𝑥_ ∈ _𝐼._

## _**Exercise**_ **3.6.10** _**:**_

- _a) Let 𝑆_ ⊂ ℝ _be a subset. If 𝑓_ : _𝑆_ → ℝ _is increasing and bounded, then show that there exists an increasing 𝐹_ : ℝ → ℝ _such that 𝑓_ ( _𝑥_ ) = _𝐹_ ( _𝑥_ ) _for all 𝑥_ ∈ _𝑆._

- _b) Find an example of a strictly increasing bounded 𝑓_ : _𝑆_ → ℝ _such that an increasing 𝐹 as above is never strictly increasing._

_CHAPTER 3. CONTINUOUS FUNCTIONS_

154

_**Exercise**_ **3.6.11** (Challenging) _**:** Find an example of an increasing function 𝑓_ : [0 _,_ 1] → ℝ _that has a discontinuity at each rational number. Then show that the image 𝑓_[�] [0 _,_ 1][�] _contains no interval. Hint: Enumerate the rational numbers and define the function with a series._

_**Exercise**_ **3.6.12** _**:** Suppose 𝐼 is an interval and 𝑓_ : _𝐼_ → ℝ _is monotone. Show that_ ℝ \ _𝑓_ ( _𝐼_ ) _is a countable union of disjoint intervals._

_**Exercise**_ **3.6.13** _**:** Suppose 𝑓_ : [0 _,_ 1] →(0 _,_ 1) _is increasing. Show that for every 𝜖>_ 0 _, there exists a strictly increasing 𝑔_ : [0 _,_ 1] →(0 _,_ 1) _such that 𝑔_ (0) = _𝑓_ (0) _, 𝑓_ ( _𝑥_ ) ≤ _𝑔_ ( _𝑥_ ) _for all 𝑥, and 𝑔_ (1) − _𝑓_ (1) _< 𝜖._

_**Exercise**_ **3.6.14** _**:** Prove that the Dirichlet function 𝑓_ : [0 _,_ 1] → ℝ _, defined by 𝑓_ ( _𝑥_ ) � 1 _if 𝑥 is rational and 𝑓_ ( _𝑥_ ) � 0 _otherwise, cannot be written as a difference of two increasing functions. That is, there do not exist increasing 𝑔 and ℎ such that, 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) − _ℎ_ ( _𝑥_ ) _._

_**Exercise**_ **3.6.15** _**:** Suppose 𝑓_ : ( _𝑎, 𝑏_ ) →( _𝑐, 𝑑_ ) _is a strictly increasing onto function. Prove that there exists a 𝑔_ : ( _𝑎, 𝑏_ ) →( _𝑐, 𝑑_ ) _, which is also strictly increasing and onto, and 𝑔_ ( _𝑥_ ) _< 𝑓_ ( _𝑥_ ) _for all 𝑥_ ∈( _𝑎, 𝑏_ ) _._

## **Chapter 4**

## **The Derivative**

## **4.1 The derivative**

## _Note: 1 lecture_

The idea of a derivative is the following. If the graph of a function looks locally like a straight line, then we can talk about the slope of this line. The slope tells us the rate at which the value of the function is changing at that particular point. Of course, we are leaving out any function that has corners or discontinuities. Let us be precise.

## **4.1.1 Definition and basic properties**