Example 3.6.5

**Example 3.6.5:** By ⌊ _𝑥_ ⌋ denote the largest integer less than or equal to _𝑥_ . Define _𝑓_ : [0 _,_ 1] → ℝ by

**==> picture [121 x 38] intentionally omitted <==**

for _𝑥 <_ 1 and _𝑓_ (1) � 3. It is an exercise to show that _𝑓_ is strictly increasing, bounded, and has a discontinuity at all points 1 −[1] / _𝑘_ for _𝑘_ ∈ ℕ. In particular, there are countably many See discontinuities, but the function is bounded and defined on a closed bounded interval. .

**==> picture [168 x 88] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>2.5<br>2<br>1.5<br>0 1<br>**----- End of picture text -----**<br>


**Figure 3.12:** Strictly increasing function on [0 _,_ 1] with countably many discontinuities.

Similarly, one can find an example of a monotone function discontinuous on a dense set such as the rational numbers. See the exercises.

_CHAPTER 3. CONTINUOUS FUNCTIONS_

152

## **3.6.2 Continuity of inverse functions**

A strictly monotone function _𝑓_ is one-to-one (injective). To see this fact, notice that if _𝑥_ ≠ _𝑦_ , then we can assume _𝑥 < 𝑦_ . Either _𝑓_ ( _𝑥_ ) _< 𝑓_ ( _𝑦_ ) if _𝑓_ is strictly increasing or _𝑓_ ( _𝑥_ ) _> 𝑓_ ( _𝑦_ ) if _𝑓_ is strictly decreasing, so _𝑓_ ( _𝑥_ ) ≠ _𝑓_ ( _𝑦_ ). Hence, _𝑓_ must have an inverse _𝑓_[−][1] defined on its range. **Proposition 3.6.6.** _If 𝐼_ ⊂ ℝ _is an interval and 𝑓_ : _𝐼_ → ℝ _is strictly monotone, then the inverse 𝑓_[−][1] : _𝑓_ ( _𝐼_ ) → _𝐼 is continuous._

_Proof._ Suppose _𝑓_ is strictly increasing. The proof is almost identical for a strictly decreasing function. Since _𝑓_ is strictly increasing, so is _𝑓_[−][1] . That is, if _𝑓_ ( _𝑥_ ) _< 𝑓_ ( _𝑦_ ), then we must have _𝑥 < 𝑦_ and therefore _𝑓_[−][1][�] _𝑓_ ( _𝑥_ )[�] _< 𝑓_[−][1][�] _𝑓_ ( _𝑦_ )[�] .

Take _𝑐_ ∈ _𝑓_ ( _𝐼_ ). If _𝑐_ is not a cluster point of _𝑓_ ( _𝐼_ ), then _𝑓_[−][1] is continuous at _𝑐_ automatically. So let _𝑐_ be a cluster point of _𝑓_ ( _𝐼_ ). Suppose both of the following one-sided limits exist:

**==> picture [384 x 49] intentionally omitted <==**

We have _𝑥_ 0 ≤ _𝑥_ 1 as _𝑓_[−][1] is increasing. For all _𝑥_ ∈ _𝐼_ where _𝑥 > 𝑥_ 0, we have _𝑓_ ( _𝑥_ ) ≥ _𝑐_ . As _𝑓_ is strictly increasing, we must have _𝑓_ ( _𝑥_ ) _> 𝑐_ for all _𝑥_ ∈ _𝐼_ where _𝑥 > 𝑥_ 0. Therefore,

**==> picture [192 x 16] intentionally omitted <==**

The infimum of the left-hand set is _𝑥_ 0, and the infimum of the right-hand set is _𝑥_ 1, so we obtain _𝑥_ 0 ≥ _𝑥_ 1. So _𝑥_ 1 = _𝑥_ 0, and _𝑓_[−][1] is continuous at _𝑐_ .

If one of the one-sided limits does not exist, the argument is similar and is left as an exercise. □