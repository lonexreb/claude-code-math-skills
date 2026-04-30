Example 3.2.13

**Example 3.2.13:** Define _𝑔_ : ℝ → ℝ by _𝑔_ ( _𝑥_ ) � 0 if _𝑥_ ≠ 0 and _𝑔_ (0) � 1. Then _𝑔_ is not continuous at zero, but continuous everywhere else (why?). The point _𝑥_ = 0 is called a . _removable discontinuity_ That is because if we would change the definition of _𝑔_ , by insisting that _𝑔_ (0) be 0, we would obtain a continuous function. On the other hand, let _𝑓_ be the function of . Then _𝑓_ does not have a removable discontinuity at 0. No matter how we would define _𝑓_ (0) the function would still fail to be continuous. The difference is that lim _𝑥_ →0 _𝑔_ ( _𝑥_ ) exists while lim _𝑥_ →0 _𝑓_ ( _𝑥_ ) does not.

We stay with this example to show another phenomenon. Let _𝐴_ � {0}, then _𝑔_ | _𝐴_ is continuous (why?), while _𝑔_ is not continuous on _𝐴_ . Similarly, if _𝐵_ � ℝ \ {0}, then _𝑔_ | _𝐵_ is also continuous, and _𝑔_ is in fact continuous on _𝐵_ .

## **3.2.4 Exercises**

_**Exercise**_ **3.2.1** _**:** Using the definition of continuity directly prove that 𝑓_ : ℝ → ℝ _defined by 𝑓_ ( _𝑥_ ) � _𝑥_[2] _is continuous._

_**Exercise**_ **3.2.2** _**:** Using the definition of continuity directly prove that 𝑓_ : (0 _,_ ∞) → ℝ _defined by 𝑓_ ( _𝑥_ ) �[1] / _𝑥 is continuous._

_**Exercise**_ **3.2.3** _**:** Define 𝑓_ : ℝ → ℝ _by_

**==> picture [138 x 36] intentionally omitted <==**

_Using the definition of continuity directly prove that 𝑓 is continuous at_ 1 _and discontinuous at_ 2 _._

_CHAPTER 3. CONTINUOUS FUNCTIONS_

128

_**Exercise**_ **3.2.4** _**:** Define 𝑓_ : ℝ → ℝ _by_

**==> picture [126 x 36] intentionally omitted <==**

_Is 𝑓 continuous? Prove your assertion._

_**Exercise**_ **3.2.5** _**:** Define 𝑓_ : ℝ → ℝ _by_

**==> picture [134 x 36] intentionally omitted <==**

_Is 𝑓 continuous? Prove your assertion._

_**Exercise**_ **3.2.6** _**:** Prove ._

_**Exercise**_ **3.2.7** _**:** Let 𝑆_ ⊂ ℝ _and 𝐴_ ⊂ _𝑆. Let 𝑓_ : _𝑆_ → ℝ _be a continuous function. Prove that the restriction 𝑓_ | _𝐴 is continuous._

_**Exercise**_ **3.2.8** _**:** Suppose 𝑆_ ⊂ ℝ _, such that_ ( _𝑐_ − _𝛼, 𝑐_ + _𝛼_ ) ⊂ _𝑆 for some 𝑐_ ∈ ℝ _and 𝛼>_ 0 _. Let 𝑓_ : _𝑆_ → ℝ _be a function and 𝐴_ � ( _𝑐_ − _𝛼, 𝑐_ + _𝛼_ ) _. Prove that if 𝑓_ | _𝐴 is continuous at 𝑐, then 𝑓 is continuous at 𝑐._

_**Exercise**_ **3.2.9** _**:** Give an example of functions 𝑓_ : ℝ → ℝ _and 𝑔_ : ℝ → ℝ _such that the function ℎ, defined by ℎ_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) + _𝑔_ ( _𝑥_ ) _, is continuous, but 𝑓 and 𝑔 are not continuous. Can you find 𝑓 and 𝑔 that are nowhere continuous, but ℎ is a continuous function?_

_**Exercise**_ **3.2.10** _**:** Let 𝑓_ : ℝ → ℝ _and 𝑔_ : ℝ → ℝ _be continuous functions. Suppose that 𝑓_ ( _𝑟_ ) = _𝑔_ ( _𝑟_ ) _for all 𝑟_ ∈ ℚ _. Show that 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) _for all 𝑥_ ∈ ℝ _._

_**Exercise**_ **3.2.11** _**:** Let 𝑓_ : ℝ → ℝ _be continuous. Suppose 𝑓_ ( _𝑐_ ) _>_ 0 _. Show that there exists an 𝛼>_ 0 _such that for all 𝑥_ ∈( _𝑐_ − _𝛼, 𝑐_ + _𝛼_ ) _, we have 𝑓_ ( _𝑥_ ) _>_ 0 _._

_**Exercise**_ **3.2.12** _**:** Let 𝑓_ : ℤ → ℝ _be a function. Show that 𝑓 is continuous._

_**Exercise**_ **3.2.13** _**:** Let 𝑓_ : _𝑆_ → ℝ _be a function and 𝑐_ ∈ _𝑆, such that for every sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[in][ 𝑆][with]_ ∞ lim _𝑛_ →∞ _𝑥𝑛_ = _𝑐, the sequence_ � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1 _[converges.][Show that][𝑓][is continuous at][ 𝑐][.]_

_**Exercise**_ **3.2.14** _**:** Suppose 𝑓_ : [−1 _,_ 0] → ℝ _and 𝑔_ : [0 _,_ 1] → ℝ _are continuous and 𝑓_ (0) = _𝑔_ (0) _. Define ℎ_ : [−1 _,_ 1] → ℝ _by ℎ_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) _if 𝑥_ ≤ 0 _and ℎ_ ( _𝑥_ ) � _𝑔_ ( _𝑥_ ) _if 𝑥 >_ 0 _. Show that ℎ is continuous._

_**Exercise**_ **3.2.15** _**:** Suppose 𝑔_ : ℝ → ℝ _is a continuous function such that 𝑔_ (0) = 0 _, and suppose 𝑓_ : ℝ → ℝ _is such that_ �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� ≤ _𝑔_ ( _𝑥_ − _𝑦_ ) _for all 𝑥 and 𝑦. Show that 𝑓 is continuous._

_**Exercise**_ **3.2.16** (Challenging) _**:** Suppose 𝑓_ : ℝ → ℝ _is continuous at_ 0 _and such that 𝑓_ ( _𝑥_ + _𝑦_ ) = _𝑓_ ( _𝑥_ )+ _𝑓_ ( _𝑦_ ) _for every 𝑥 and 𝑦. Show that 𝑓_ ( _𝑥_ ) = _𝑎𝑥 for some 𝑎_ ∈ ℝ _. Hint: Show that 𝑓_ ( _𝑛𝑥_ ) = _𝑛𝑓_ ( _𝑥_ ) _, then show 𝑓 is continuous on_ ℝ _. Then show that[𝑓]_[(] _[𝑥]_[)] / _𝑥_ = _𝑓_ (1) _for all rational 𝑥._

_**Exercise**_ **3.2.17** _**:** Suppose 𝑆_ ⊂ ℝ _and let 𝑓_ : _𝑆_ → ℝ _and 𝑔_ : _𝑆_ → ℝ _be continuous functions. Define 𝑝_ : _𝑆_ → ℝ _by 𝑝_ ( _𝑥_ ) � max� _𝑓_ ( _𝑥_ ) _, 𝑔_ ( _𝑥_ )� _and 𝑞_ : _𝑆_ → ℝ _by 𝑞_ ( _𝑥_ ) � min� _𝑓_ ( _𝑥_ ) _, 𝑔_ ( _𝑥_ )� _. Prove that 𝑝 and 𝑞 are continuous._

129

## _3.2. CONTINUOUS FUNCTIONS_

_**Exercise**_ **3.2.18** _**:** Suppose 𝑓_ : [−1 _,_ 1] → ℝ _is a function continuous at all 𝑥_ ∈[−1 _,_ 1] \ {0} _. Show that for every 𝜖 such that_ 0 _< 𝜖<_ 1 _, there exists a function 𝑔_ : [−1 _,_ 1] → ℝ _continuous on all of_ [−1 _,_ 1] _, such that 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) _for all 𝑥_ ∈[−1 _,_ − _𝜖_ ] ∪[ _𝜖,_ 1] _, and_ �� _𝑔_ ( _𝑥_ )�� ≤ �� _𝑓_ ( _𝑥_ )�� _for all 𝑥_ ∈[−1 _,_ 1] _._

_**Exercise**_ **3.2.19** (Challenging) _**:** A function 𝑓_ : _𝐼_ → ℝ _is_ convex _if whenever 𝑎_ ≤ _𝑥_ ≤ _𝑏 for 𝑎, 𝑥, 𝑏 in 𝐼, we have 𝑓_ ( _𝑥_ ) ≤ _𝑓_ ( _𝑎_ ) _[𝑏] 𝑏_[−] − _[𝑥] 𝑎_[+] _[𝑓]_[(] _[𝑏]_[)] _[𝑥] 𝑏_ −[−] _𝑎[𝑎][.][In other words, if the line drawn between]_[�] _𝑎, 𝑓_ ( _𝑎_ )[�] _and_[�] _𝑏, 𝑓_ ( _𝑏_ )[�] _is above the graph of 𝑓 ._

- _a) Prove that if 𝐼_ = ( _𝛼, 𝛽_ ) _an open interval and 𝑓_ : _𝐼_ → ℝ _is convex, then 𝑓 is continuous._

- _b) Find an example of a convex 𝑓_ : [0 _,_ 1] → ℝ _that is not continuous._

_CHAPTER 3. CONTINUOUS FUNCTIONS_

130

## **3.3 Extreme and intermediate value theorems**

_Note: 1.5 lectures_

Continuous functions on closed and bounded intervals are quite well behaved.

## **3.3.1 Min-max or extreme value theorem**

Recall that _𝑓_ : [ _𝑎, 𝑏_ ] → ℝ is _bounded_ if there exists a _𝐵_ ∈ ℝ such that �� _𝑓_ ( _𝑥_ )�� ≤ _𝐵_ for all _𝑥_ ∈[ _𝑎, 𝑏_ ]. For a continuous function on a closed and bounded interval, we have the following lemma.