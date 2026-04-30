Corollary 3.6.3

**Corollary 3.6.3.** _If 𝐼_ ⊂ ℝ _is an interval and 𝑓_ : _𝐼_ → ℝ _is monotone and not constant, then 𝑓_ ( _𝐼_ ) _is an interval if and only if 𝑓 is continuous._

Assuming _𝑓_ is not constant is to avoid the technicality that _𝑓_ ( _𝐼_ ) is a single point: _𝑓_ ( _𝐼_ ) is a single point if and only if _𝑓_ is constant. A constant function is continuous.

_Proof._ Without loss of generality, suppose _𝑓_ is increasing.

First suppose _𝑓_ is continuous. Take two points _𝑓_ ( _𝑥_ 1) _, 𝑓_ ( _𝑥_ 2) in _𝑓_ ( _𝐼_ ) and suppose _𝑓_ ( _𝑥_ 1) _< 𝑓_ ( _𝑥_ 2). As _𝑓_ is increasing, then _𝑥_ 1 _< 𝑥_ 2. By the , given _𝑦_ with _𝑓_ ( _𝑥_ 1) _< 𝑦 < 𝑓_ ( _𝑥_ 2), we find a _𝑐_ ∈( _𝑥_ 1 _, 𝑥_ 2) ⊂ _𝐼_ such that _𝑓_ ( _𝑐_ ) = _𝑦_ , so _𝑦_ ∈ _𝑓_ ( _𝐼_ ). Hence, _𝑓_ ( _𝐼_ ) is an interval.

Let us prove the reverse direction by contrapositive. Suppose _𝑓_ is not continuous at _𝑐_ ∈ _𝐼_ , and that _𝑐_ is not an endpoint of _𝐼_ . Let

**==> picture [450 x 20] intentionally omitted <==**

As _𝑐_ is a discontinuity, _𝑎 < 𝑏_ . If _𝑥 < 𝑐_ , then _𝑓_ ( _𝑥_ ) ≤ _𝑎_ , and if _𝑥 > 𝑐_ , then _𝑓_ ( _𝑥_ ) ≥ _𝑏_ . Therefore no point in ( _𝑎, 𝑏_ ) \ � _𝑓_ ( _𝑐_ )� is in _𝑓_ ( _𝐼_ ). There exists _𝑥_ 1 ∈ _𝐼_ with _𝑥_ 1 _< 𝑐_ , so _𝑓_ ( _𝑥_ 1) ≤ _𝑎_ , and there exists _𝑥_ 2 ∈ _𝐼_ with _𝑥_ 2 _> 𝑐_ , so _𝑓_ ( _𝑥_ 2) ≥ _𝑏_ . Both _𝑓_ ( _𝑥_ 1) and _𝑓_ ( _𝑥_ 2) are in _𝑓_ ( _𝐼_ ), but there are points in between them that are not in _𝑓_ ( _𝐼_ ). So _𝑓_ ( _𝐼_ ) is not an interval. See .

When _𝑐_ ∈ _𝐼_ is an endpoint, the proof is similar and is left as an exercise. □

A striking property of monotone functions is that they cannot have too many discontinuities.