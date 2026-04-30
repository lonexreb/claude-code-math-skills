Example 3.3.12

**Example 3.3.12:** Interestingly, there exist discontinuous functions with the intermediate value property. The function

**==> picture [138 x 39] intentionally omitted <==**

is not continuous at 0; however, _𝑓_ has the intermediate value property: Whenever _𝑎 < 𝑏_ and _𝑦_ is such that _𝑓_ ( _𝑎_ ) _< 𝑦 < 𝑓_ ( _𝑏_ ) or _𝑓_ ( _𝑎_ ) _> 𝑦 > 𝑓_ ( _𝑏_ ), there exists a _𝑐_ ∈( _𝑎, 𝑏_ ) such that _𝑓_ ( _𝑐_ ) = _𝑦_ . See for a graph of sin([1] / _𝑥_ ). Proof is left as .

The intermediate value theorem says that if _𝑓_ : [ _𝑎, 𝑏_ ] → ℝ is continuous, then _𝑓_[�] [ _𝑎, 𝑏_ ][�] contains all the values between _𝑓_ ( _𝑎_ ) and _𝑓_ ( _𝑏_ ). In fact, more is true. Combining all the results of this section one can prove the following useful corollary whose proof is left as an exercise. Hint: See and notice what the endpoints of the image interval are. **Corollary 3.3.13.** _If 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is continuous, then the direct image 𝑓_[�] [ _𝑎, 𝑏_ ][�] _is a closed and bounded interval or a single number._

_CHAPTER 3. CONTINUOUS FUNCTIONS_

136

**==> picture [221 x 104] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑦 = 𝑓 ( 𝑥 )<br>𝑓 [�] [ 𝑎, 𝑏 ] [�]<br>𝑎 𝑏<br>**----- End of picture text -----**<br>


**Figure 3.8:** The image of a continuous _𝑓_ : [ _𝑎, 𝑏_ ] → ℝ.

## **3.3.3 Exercises**

_**Exercise**_ **3.3.1** _**:** Find an example of a discontinuous function 𝑓_ : [0 _,_ 1] → ℝ _where the conclusion of the intermediate value theorem fails._

_**Exercise**_ **3.3.2** _**:** Find an example of a_ bounded _discontinuous function 𝑓_ : [0 _,_ 1] → ℝ _that has neither an absolute minimum nor an absolute maximum._

_**Exercise**_ **3.3.3** _**:** Let 𝑓_ : (0 _,_ 1) → ℝ _be a continuous function such that_ lim[lim] _[Show that] 𝑥_ →0 _[𝑓]_[(] _[𝑥]_[)][ =] _𝑥_ →1 _[𝑓]_[(] _[𝑥]_[)][ =][ 0] _[.] 𝑓 achieves either an absolute minimum or an absolute maximum on_ (0 _,_ 1) _(but perhaps not both)._

_**Exercise**_ **3.3.4** _**:** Let_

**==> picture [126 x 36] intentionally omitted <==**

_Show that 𝑓 has the intermediate value property. That is, whenever 𝑎 < 𝑏, if there exists a 𝑦 such that 𝑓_ ( _𝑎_ ) _< 𝑦 < 𝑓_ ( _𝑏_ ) _or 𝑓_ ( _𝑎_ ) _> 𝑦 > 𝑓_ ( _𝑏_ ) _, then there exists a 𝑐_ ∈( _𝑎, 𝑏_ ) _such that 𝑓_ ( _𝑐_ ) = _𝑦._

_**Exercise**_ **3.3.5** _**:** Suppose 𝑔_ ( _𝑥_ ) _is a monic polynomial of odd degree 𝑑, that is,_

**==> picture [176 x 14] intentionally omitted <==**

_for some real numbers 𝑏_ 0 _, 𝑏_ 1 _, . . . , 𝑏𝑑_ −1 _. Show that there exists a 𝐾_ ∈ ℕ _such that 𝑔_ (− _𝐾_ ) _<_ 0 _. Hint: Make sure to use the fact that 𝑑 is odd. You will have to use that_ (− _𝑛_ ) _[𝑑]_ = −( _𝑛[𝑑]_ ) _._

_**Exercise**_ **3.3.6** _**:** Suppose 𝑔_ ( _𝑥_ ) _is a monic polynomial of positive even degree 𝑑, that is,_

**==> picture [176 x 15] intentionally omitted <==**

_for some real numbers 𝑏_ 0 _, 𝑏_ 1 _, . . . , 𝑏𝑑_ −1 _. Suppose 𝑔_ (0) _<_ 0 _. Show that 𝑔 has at least two distinct real roots._

_**Exercise**_ **3.3.7** _**:** Prove : Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is a continuous function. Prove that the direct image 𝑓_[�] [ _𝑎, 𝑏_ ][�] _is a closed and bounded interval or a single number._

_**Exercise**_ **3.3.8** _**:** Suppose 𝑓_ : ℝ → ℝ _is continuous and periodic with period 𝑃 >_ 0 _. That is, 𝑓_ ( _𝑥_ + _𝑃_ ) = _𝑓_ ( _𝑥_ ) _for all 𝑥_ ∈ ℝ _. Show that 𝑓 achieves an absolute minimum and an absolute maximum._

_3.3. EXTREME AND INTERMEDIATE VALUE THEOREMS_

137

_**Exercise**_ **3.3.9** (Challenging) _**:** Suppose 𝑓_ ( _𝑥_ ) _is a bounded polynomial, in other words, there is an 𝑀 such that_ �� _𝑓_ ( _𝑥_ )�� ≤ _𝑀 for all 𝑥_ ∈ ℝ _. Prove that 𝑓 must be a constant._

_**Exercise**_ **3.3.10** _**:** Suppose 𝑓_ : [0 _,_ 1] →[0 _,_ 1] _is continuous. Show that 𝑓 has a fixed point, in other words, show that there exists an 𝑥_ ∈[0 _,_ 1] _such that 𝑓_ ( _𝑥_ ) = _𝑥._

_**Exercise**_ **3.3.11** _**:** Find an example of a continuous bounded function 𝑓_ : ℝ → ℝ _that does not achieve an absolute minimum nor an absolute maximum on_ ℝ _._

_**Exercise**_ **3.3.12** _**:** Suppose 𝑓_ : ℝ → ℝ _is continuous such that 𝑥_ ≤ _𝑓_ ( _𝑥_ ) ≤ _𝑥_ + 1 _for all 𝑥_ ∈ ℝ _. Find 𝑓_ (ℝ) _._

_**Exercise**_ **3.3.13** _**:** True/False, prove or find a counterexample. If 𝑓_ : ℝ → ℝ _is a continuous function such that 𝑓_ |ℤ _is bounded, then 𝑓 is bounded._

_**Exercise**_ **3.3.14** _**:** Suppose 𝑓_ : [0 _,_ 1] →(0 _,_ 1) _is a bĳection. Prove that 𝑓 is not continuous._

_**Exercise**_ **3.3.15** _**:** Suppose 𝑓_ : ℝ → ℝ _is continuous._

_a) Prove that if there is a 𝑐 such that 𝑓_ ( _𝑐_ ) _𝑓_ (− _𝑐_ ) _<_ 0 _, then there is a 𝑑_ ∈ ℝ _such that 𝑓_ ( _𝑑_ ) = 0 _._

_b) Find a continuous function 𝑓 such that 𝑓_ (ℝ) = ℝ _, but 𝑓_ ( _𝑥_ ) _𝑓_ (− _𝑥_ ) ≥ 0 _for all 𝑥_ ∈ ℝ _._

_**Exercise**_ **3.3.16** _**:** Suppose 𝑔_ ( _𝑥_ ) _is a monic polynomial of even degree 𝑑, that is,_

**==> picture [176 x 14] intentionally omitted <==**

_for some real numbers 𝑏_ 0 _, 𝑏_ 1 _, . . . , 𝑏𝑑_ −1 _. Show that 𝑔 achieves an absolute minimum on_ ℝ _._

_**Exercise**_ **3.3.17** _**:** Suppose 𝑓_ ( _𝑥_ ) _is a polynomial of degree 𝑑 and 𝑓_ (ℝ) = ℝ _. Show that 𝑑 is odd._

_CHAPTER 3. CONTINUOUS FUNCTIONS_

138

## **3.4 Uniform continuity**

_Note: 1.5–2 lectures (continuous extension can be optional)_

## **3.4.1 Uniform continuity**

We made a fuss of saying that the _𝛿_ in the definition of continuity depended on the point _𝑐_ . There are situations when it is advantageous to be able to pick a _𝛿_ independent of any point, and so we give a name to this concept.