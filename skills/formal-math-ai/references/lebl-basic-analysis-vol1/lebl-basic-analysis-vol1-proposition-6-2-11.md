Proposition 6.2.11

**Proposition 6.2.11.** _Let_[�][∞] _𝑛_ =0 _[𝑐][𝑛]_[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛][be a convergent power series with a radius of convergence] 𝜌, where_ 0 _< 𝜌_ ≤∞ _. Then the series converges uniformly in_ [ _𝑎_ − _𝑟, 𝑎_ + _𝑟_ ] _whenever_ 0 _< 𝑟 < 𝜌._

_In particular, the series converges (pointwise) to a continuous function on_ ( _𝑎_ − _𝜌, 𝑎_ + _𝜌_ ) _if 𝜌<_ ∞ _, or on_ ℝ _if 𝜌_ = ∞ _._

_6.2. INTERCHANGE OF LIMITS_

241

_Proof._ Let _𝐼_ � ( _𝑎_ − _𝜌, 𝑎_ + _𝜌_ ) if _𝜌<_ ∞, or let _𝐼_ � ℝ if _𝜌_ = ∞. Take 0 _< 𝑟 < 𝜌_ . The series converges absolutely for every _𝑥_ ∈ _𝐼_ , in particular if _𝑥_ = _𝑎_ + _𝑟_ . So[�][∞] _𝑛_ =0[|] _[𝑐][𝑛]_[|] _[ 𝑟][𝑛]_[converges.] Given _𝜖>_ 0, find _𝑀_ such that for all _𝑘_ ≥ _𝑀_ ,

**==> picture [86 x 35] intentionally omitted <==**

For all _𝑥_ ∈[ _𝑎_ − _𝑟, 𝑎_ + _𝑟_ ] and all _𝑚 > 𝑘_ ,

**==> picture [447 x 80] intentionally omitted <==**

The partial sums are therefore uniformly Cauchy on [ _𝑎_ − _𝑟, 𝑎_ + _𝑟_ ] and hence converge uniformly on that set.

Moreover, the partial sums are polynomials, which are continuous, and so their uniform limit on [ _𝑎_ − _𝑟, 𝑎_ + _𝑟_ ] is a continuous function. As _𝑟 < 𝜌_ was arbitrary, the limit function is continuous on all of _𝐼_ . □

As we said, we will show that power series can be differentiated and integrated term by term. The differentiated or integrated series is again a power series, and we will show it has the same radius of convergence. Therefore, any power series defines an infinitely differentiable function.

We first prove that we can antidifferentiate, as integration only needs uniform limits. **Corollary 6.2.12.** _Let_[�][∞] _𝑛_ =0 _[𝑐][𝑛]_[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛][be a convergent power series with a radius of convergence]_ 0 _< 𝜌_ ≤∞ _. Let 𝐼_ � ( _𝑎_ − _𝜌, 𝑎_ + _𝜌_ ) _if 𝜌<_ ∞ _or 𝐼_ � ℝ _if 𝜌_ = ∞ _. Let 𝑓_ : _𝐼_ → ℝ _be the limit. Then_

**==> picture [132 x 36] intentionally omitted <==**

_. where the radius of convergence of this series is at least 𝜌_

_Proof._ Take 0 _< 𝑟 < 𝜌_ . The partial sums[�] _𝑛[𝑘]_ =0 _[𝑐][𝑛]_[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛]_[converge uniformly on][ [] _[𝑎]_[−] _[𝑟, 𝑎]_[+] _[𝑟]_[]][.] For every fixed _𝑥_ ∈[ _𝑎_ − _𝑟, 𝑎_ + _𝑟_ ], the convergence is also uniform on [ _𝑎, 𝑥_ ] (or [ _𝑥, 𝑎_ ] if _𝑥 < 𝑎_ ). Hence,

**==> picture [462 x 38] intentionally omitted <==**

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

242