Example 3.4.10

**Example 3.4.10:** The function _𝑓_ : [1 _,_ ∞) → ℝ defined by _𝑓_ ( _𝑥_ ) �[√] _𝑥_ is Lipschitz continuous. Proof:

**==> picture [186 x 39] intentionally omitted <==**

As _𝑥_ ≥ 1 and _𝑦_ ≥ 1, we see that ~~√~~ _𝑥_ +1 ~~[√]~~ ~~_𝑦_~~[≤] 2[1][.][Therefore,]

**==> picture [184 x 40] intentionally omitted <==**

On the other hand, _𝑔_ : [0 _,_ ∞) → ℝ defined by _𝑔_ ( _𝑥_ ) �[√] _𝑥_ is not Lipschitz continuous. Proof: Suppose for all _𝑥, 𝑦_ ∈[0 _,_ ∞),

**==> picture [116 x 16] intentionally omitted <==**

for some _𝐾_ . Set _𝑦_ = 0 to obtain ~~[√]~~ _𝑥_ ≤ _𝐾𝑥_ . If _𝐾 >_ 0, then for _𝑥 >_ 0 we get[1] / _𝐾_ ≤[√] _𝑥_ or 1/ _𝐾_[2] ≤ _𝑥_ . This cannot possibly be true for all _𝑥 >_ 0. Thus no such _𝐾 >_ 0 exists and _𝑔_ is not Lipschitz continuous. See and note how secant lines would be more and more vertical as we get closer to _𝑥_ = 0.

**==> picture [220 x 112] intentionally omitted <==**

**Figure 3.10:** Graph of[√] _𝑥_ and some secant lines through (0 _,_ 0) and ( _𝑥,_ ~~[√]~~ _𝑥_ ).

The last example _𝑔_ is a function that is uniformly continuous but not Lipschitz continuous. To see that[√] _𝑥_ is uniformly continuous as a function on [0 _,_ ∞), note that it is uniformly continuous when restricted to [0 _,_ 1] by . It is also Lipschitz (and so uniformly continuous) when restricted to [1 _,_ ∞). It is not hard (exercise) to show that this means that[√] _𝑥_ is a uniformly continuous function on [0 _,_ ∞).

_3.4. UNIFORM CONTINUITY_

143

## **3.4.4 Exercises**

_**Exercise**_ **3.4.1** _**:** Let 𝑓_ : _𝑆_ → ℝ _be uniformly continuous. Let 𝐴_ ⊂ _𝑆. Then the restriction 𝑓_ | _𝐴 is uniformly continuous._

_**Exercise**_ **3.4.2** _**:** Let 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _be a uniformly continuous function. Finish the proof of by showing that the limit_ lim _𝑥_ → _𝑏[𝑓]_[(] _[𝑥]_[)] _[ exists.]_

_**Exercise**_ **3.4.3** _**:** Show that 𝑓_ : ( _𝑐,_ ∞) → ℝ _for some 𝑐 >_ 0 _and defined by 𝑓_ ( _𝑥_ ) �[1] / _𝑥 is Lipschitz continuous._

_**Exercise**_ **3.4.4** _**:** Show that 𝑓_ : (0 _,_ ∞) → ℝ _defined by 𝑓_ ( _𝑥_ ) �[1] / _𝑥 is not Lipschitz continuous._

_**Exercise**_ **3.4.5** _**:** Let 𝐴, 𝐵 be intervals. Let 𝑓_ : _𝐴_ → ℝ _and 𝑔_ : _𝐵_ → ℝ _be uniformly continuous functions such that 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) _for 𝑥_ ∈ _𝐴_ ∩ _𝐵. Define the function ℎ_ : _𝐴_ ∪ _𝐵_ → ℝ _by ℎ_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) _if 𝑥_ ∈ _𝐴 and ℎ_ ( _𝑥_ ) � _𝑔_ ( _𝑥_ ) _if 𝑥_ ∈ _𝐵_ \ _𝐴._

- _a) Prove that if 𝐴_ ∩ _𝐵_ ≠ ∅ _, then ℎ is uniformly continuous._

- _b) Find an example where 𝐴_ ∩ _𝐵_ = ∅ _and ℎ is not even continuous._

_**Exercise**_ **3.4.6** (Challenging) _**:** Let 𝑓_ : ℝ → ℝ _be a polynomial of degree 𝑑_ ≥ 2 _. Show that 𝑓 is not Lipschitz continuous._

_**Exercise**_ **3.4.7** _**:** Let 𝑓_ : (0 _,_ 1) → ℝ _be a bounded continuous function. Show that the function 𝑔_ ( _𝑥_ ) � _𝑥_ (1 − _𝑥_ ) _𝑓_ ( _𝑥_ ) _is uniformly continuous._

_**Exercise**_ **3.4.8** _**:** Show that 𝑓_ : (0 _,_ ∞) → ℝ _defined by 𝑓_ ( _𝑥_ ) � sin([1] / _𝑥_ ) _is not uniformly continuous._

_**Exercise**_ **3.4.9** (Challenging) _**:** Let 𝑓_ : ℚ → ℝ _be a uniformly continuous function. Show that there exists a uniformly continuous function_[�] _𝑓_ : ℝ → ℝ _such that 𝑓_ ( _𝑥_ ) =[�] _𝑓_ ( _𝑥_ ) _for all 𝑥_ ∈ ℚ _._

## _**Exercise**_ **3.4.10** _**:**_

- _a) Find a continuous 𝑓_ : (0 _,_ 1) → ℝ _and a sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[in]_[(][0] _[,]_[ 1][)] _[that][is][Cauchy,][but][such][that]_ ∞

- � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1 _[is not Cauchy.]_

∞ _b) Prove that if 𝑓_ : ℝ → ℝ _is continuous, and_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[is Cauchy, then]_ � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1 _[is Cauchy.]_

## _**Exercise**_ **3.4.11** _**:** Prove:_

- _a) If 𝑓_ : _𝑆_ → ℝ _and 𝑔_ : _𝑆_ → ℝ _are uniformly continuous, then ℎ_ : _𝑆_ → ℝ _given by ℎ_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) + _𝑔_ ( _𝑥_ ) _is uniformly continuous._

- _b) If 𝑓_ : _𝑆_ → ℝ _is uniformly continuous and 𝑎_ ∈ ℝ _, then ℎ_ : _𝑆_ → ℝ _given by ℎ_ ( _𝑥_ ) � _𝑎𝑓_ ( _𝑥_ ) _is uniformly continuous._

## _**Exercise**_ **3.4.12** _**:** Prove:_

- _a) If 𝑓_ : _𝑆_ → ℝ _and 𝑔_ : _𝑆_ → ℝ _are Lipschitz, then ℎ_ : _𝑆_ → ℝ _given by ℎ_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) + _𝑔_ ( _𝑥_ ) _is Lipschitz._

- _b) If 𝑓_ : _𝑆_ → ℝ _is Lipschitz and 𝑎_ ∈ ℝ _, then ℎ_ : _𝑆_ → ℝ _given by ℎ_ ( _𝑥_ ) � _𝑎𝑓_ ( _𝑥_ ) _is Lipschitz._

_CHAPTER 3. CONTINUOUS FUNCTIONS_

144

## _**Exercise**_ **3.4.13** _**:**_

- _a) If 𝑓_ : [0 _,_ 1] → ℝ _is given by 𝑓_ ( _𝑥_ ) � _𝑥[𝑚] for an integer 𝑚_ ≥ 0 _, show 𝑓 is Lipschitz and find the best (the smallest) Lipschitz constant 𝐾 (depending on 𝑚 of course). Hint:_ ( _𝑥_ − _𝑦_ )( _𝑥[𝑚]_[−][1] + _𝑥[𝑚]_[−][2] _𝑦_ + _𝑥[𝑚]_[−][3] _𝑦_[2] + · · · + _𝑥𝑦[𝑚]_[−][2] + _𝑦[𝑚]_[−][1] ) = _𝑥[𝑚]_ − _𝑦[𝑚] ._

- _b) Using the previous exercise, show that if 𝑓_ : [0 _,_ 1] → ℝ _is a polynomial, that is, 𝑓_ ( _𝑥_ ) � _𝑎𝑚 𝑥[𝑚]_ + _𝑎𝑚_ −1 _𝑥[𝑚]_[−][1] + · · · + _𝑎_ 0 _, then 𝑓 is Lipschitz._

_**Exercise**_ **3.4.14** _**:** Suppose for 𝑓_ : [0 _,_ 1] → ℝ _, we have_ �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� ≤ _𝐾_ �� _𝑥_ − _𝑦_ �� _for all 𝑥, 𝑦 in_ [0 _,_ 1] _, and 𝑓_ (0) = _𝑓_ (1) = 0 _. Prove that_ �� _𝑓_ ( _𝑥_ )�� ≤ _𝐾_ /2 _for all 𝑥_ ∈[0 _,_ 1] _. Further show by example that 𝐾_ /2 _is the best possible, that is, there exists such a continuous function for which_ �� _𝑓_ ( _𝑥_ )�� = _𝐾_ /2 _for some 𝑥_ ∈[0 _,_ 1] _._

_**Exercise**_ **3.4.15** _**:** Suppose 𝑓_ : ℝ → ℝ _is continuous and periodic with period 𝑃 >_ 0 _. That is, 𝑓_ ( _𝑥_ + _𝑃_ ) = _𝑓_ ( _𝑥_ ) _for all 𝑥_ ∈ ℝ _. Show that 𝑓 is uniformly continuous._

_**Exercise**_ **3.4.16** _**:** Suppose 𝑓_ : _𝑆_ → ℝ _and 𝑔_ : [0 _,_ ∞) →[0 _,_ ∞) _are functions, 𝑔 is continuous at_ 0 _, 𝑔_ (0) = 0 _, and whenever 𝑥 and 𝑦 are in 𝑆, we have_ �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� ≤ _𝑔_ ��� _𝑥_ − _𝑦_ ��� _. Prove that 𝑓 is uniformly continuous._

_**Exercise**_ **3.4.17** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is a function such that for every 𝑐_ ∈[ _𝑎, 𝑏_ ] _there is a 𝐾𝑐 >_ 0 _and an 𝜖𝑐 >_ 0 _for which_ �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� ≤ _𝐾𝑐_ �� _𝑥_ − _𝑦_ �� _for all 𝑥 and 𝑦 in_ ( _𝑐_ − _𝜖𝑐 , 𝑐_ + _𝜖𝑐_ ) ∩[ _𝑎, 𝑏_ ] _. In other words, 𝑓 is “locally Lipschitz.”_

- _a) Prove that there exists a single 𝐾 >_ 0 _such that_ �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� ≤ _𝐾_ �� _𝑥_ − _𝑦_ �� _for all 𝑥, 𝑦 in_ [ _𝑎, 𝑏_ ] _._

- _b) Find a counterexample to the above if the interval is open, that is, find an 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _that is locally Lipschitz, but not Lipschitz._

_3.5. LIMITS AT INFINITY_

145

## **3.5 Limits at infinity**

_Note: less than 1 lecture (optional, can safely be omitted unless or is also covered)_

## **3.5.1 Limits at infinity**

As for sequences, a continuous variable can also approach infinity.