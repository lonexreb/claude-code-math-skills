Proposition 3.6.2

**Proposition 3.6.2.** _Let 𝑆_ ⊂ ℝ _, 𝑐_ ∈ ℝ _, 𝑓_ : _𝑆_ → ℝ _be increasing, and 𝑔_ : _𝑆_ → ℝ _be decreasing. If 𝑐 is a cluster point of 𝑆_ ∩(−∞ _, 𝑐_ ) _, then_

**==> picture [442 x 18] intentionally omitted <==**

_If 𝑐 is a cluster point of 𝑆_ ∩( _𝑐,_ ∞) _, then_

**==> picture [442 x 18] intentionally omitted <==**

_If_ ∞ _is a cluster point of 𝑆, then_

**==> picture [372 x 17] intentionally omitted <==**

_If_ −∞ _is a cluster point of 𝑆, then_

**==> picture [384 x 18] intentionally omitted <==**

Namely, all the one-sided limits exist whenever they make sense. For monotone functions therefore, when we say the left-hand limit _𝑥_ → _𝑐_[−] exists, we mean that _𝑐_ is a cluster point of _𝑆_ ∩(−∞ _, 𝑐_ ), and same for the right-hand limit.

_Proof._ Let us assume _𝑓_ is increasing, and we will show the first equality. The rest of the proof is very similar and is left as an exercise.

Let _𝑎_ � sup{ _𝑓_ ( _𝑥_ ) : _𝑥 < 𝑐, 𝑥_ ∈ _𝑆_ }. If _𝑎_ = ∞, then given an _𝑀_ ∈ ℝ, there exists an _𝑥𝑀_ ∈ _𝑆_ , _𝑥𝑀 < 𝑐_ , such that _𝑓_ ( _𝑥𝑀_ ) _> 𝑀_ . As _𝑓_ is increasing, _𝑓_ ( _𝑥_ ) ≥ _𝑓_ ( _𝑥𝑀_ ) _> 𝑀_ for all _𝑥_ ∈ _𝑆_ with _𝑥 > 𝑥𝑀_ . Take _𝛿_ � _𝑐_ − _𝑥𝑀 >_ 0 to obtain the definition of the limit going to infinity.

_CHAPTER 3. CONTINUOUS FUNCTIONS_

150

Next suppose _𝑎 <_ ∞. Let _𝜖>_ 0 be given. Because _𝑎_ is the supremum and _𝑆_ ∩(−∞ _, 𝑐_ ) is nonempty, _𝑎_ ∈ ℝ and there exists an _𝑥𝜖_ ∈ _𝑆_ , _𝑥𝜖 < 𝑐_ , such that _𝑓_ ( _𝑥𝜖_ ) _> 𝑎_ − _𝜖_ . As _𝑓_ is increasing, if _𝑥_ ∈ _𝑆_ and _𝑥𝜖 < 𝑥 < 𝑐_ , we have _𝑎_ − _𝜖< 𝑓_ ( _𝑥𝜖_ ) ≤ _𝑓_ ( _𝑥_ ) ≤ _𝑎_ . Let _𝛿_ � _𝑐_ − _𝑥𝜖_ . Then for _𝑥_ ∈ _𝑆_ ∩(−∞ _, 𝑐_ ) with | _𝑥_ − _𝑐_ | _< 𝛿_ , we have �� _𝑓_ ( _𝑥_ ) − _𝑎_ �� _< 𝜖_ . □

Suppose _𝑓_ : _𝑆_ → ℝ is increasing, _𝑐_ ∈ _𝑆_ , and that both one-sided limits exist. Since _𝑓_ ( _𝑥_ ) ≤ _𝑓_ ( _𝑐_ ) ≤ _𝑓_ ( _𝑦_ ) whenever _𝑥 < 𝑐 < 𝑦_ , taking the limits we obtain

**==> picture [152 x 18] intentionally omitted <==**

Then _𝑓_ is continuous at _𝑐_ if and only if both limits are equal to each other (and hence equal to _𝑓_ ( _𝑐_ )). See also . See to get an idea of what a discontinuity looks like.