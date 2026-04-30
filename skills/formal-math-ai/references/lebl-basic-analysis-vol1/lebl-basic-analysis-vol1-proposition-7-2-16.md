Proposition 7.2.16

**Proposition 7.2.16.** _A nonempty set 𝑆_ ⊂ ℝ _is connected if and only if 𝑆 is an interval or a single point._

_Proof._ Suppose _𝑆_ is connected. If _𝑆_ is a single point, then we are done. So suppose _𝑥 < 𝑦_ and _𝑥, 𝑦_ ∈ _𝑆_ . If _𝑧_ ∈ ℝ is such that _𝑥 < 𝑧 < 𝑦_ , then (−∞ _, 𝑧_ ) ∩ _𝑆_ is nonempty and ( _𝑧,_ ∞) ∩ _𝑆_ is nonempty. The two sets are disjoint. As _𝑆_ is connected, we must have they their union is not _𝑆_ , so _𝑧_ ∈ _𝑆_ . By , _𝑆_ is an interval.

If _𝑆_ is a single point, it is connected. Therefore, suppose _𝑆_ is an interval. Consider open subsets _𝑈_ 1 and _𝑈_ 2 of ℝ such that _𝑈_ 1 ∩ _𝑆_ and _𝑈_ 2 ∩ _𝑆_ are nonempty, and _𝑆_ =[�] _𝑈_ 1 ∩ _𝑆_[�] ∪[�] _𝑈_ 2 ∩ _𝑆_[�] . We will show that _𝑈_ 1 ∩ _𝑆_ and _𝑈_ 2 ∩ _𝑆_ contain a common point, so they are not disjoint, proving that _𝑆_ is connected. Suppose _𝑥_ ∈ _𝑈_ 1 ∩ _𝑆_ and _𝑦_ ∈ _𝑈_ 2 ∩ _𝑆_ . Without loss of generality, assume _𝑥 < 𝑦_ . As _𝑆_ is an interval, [ _𝑥, 𝑦_ ] ⊂ _𝑆_ . Note that _𝑈_ 2 ∩[ _𝑥, 𝑦_ ] ≠ ∅, and let _𝑧_ � inf( _𝑈_ 2 ∩[ _𝑥, 𝑦_ ]). We wish to show that _𝑧_ ∈ _𝑈_ 1. If _𝑧_ = _𝑥_ , then _𝑧_ ∈ _𝑈_ 1. If _𝑧 > 𝑥_ , then for every _𝜖>_ 0, the ball _𝐵_ ( _𝑧, 𝜖_ ) = ( _𝑧_ − _𝜖, 𝑧_ + _𝜖_ ) contains points of [ _𝑥, 𝑦_ ] not in _𝑈_ 2, as _𝑧_ is the infimum of _𝑈_ 2 ∩[ _𝑥, 𝑦_ ]. So _𝑧_ ∉ _𝑈_ 2 as _𝑈_ 2 is open. Therefore, _𝑧_ ∈ _𝑈_ 1 as every point of [ _𝑥, 𝑦_ ] is in _𝑈_ 1 or _𝑈_ 2. As _𝑈_ 1 is open, _𝐵_ ( _𝑧, 𝛿_ ) ⊂ _𝑈_ 1 for a small enough _𝛿>_ 0. As _𝑧_ is the infimum of the nonempty set _𝑈_ 2 ∩[ _𝑥, 𝑦_ ], there must exist some _𝑤_ ∈ _𝑈_ 2 ∩[ _𝑥, 𝑦_ ] such that _𝑤_ ∈[ _𝑧, 𝑧_ + _𝛿_ ) ⊂ _𝐵_ ( _𝑧, 𝛿_ ) ⊂ _𝑈_ 1. Therefore, _𝑤_ ∈ _𝑈_ 1 ∩ _𝑈_ 2 ∩[ _𝑥, 𝑦_ ]. So _𝑈_ 1 ∩ _𝑆_ and _𝑈_ 2 ∩ _𝑆_ are not disjoint, and _𝑆_ is connected. See . □

**==> picture [246 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑈 1 𝑈 2<br>𝑧 𝑤<br>𝑥 𝑦<br>( 𝑧 − 𝛿, 𝑧 +  𝛿 )<br>**----- End of picture text -----**<br>


**Figure 7.8:** Proof that an interval is connected.