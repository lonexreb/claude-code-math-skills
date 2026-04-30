Proposition 2.6.10

**Proposition 2.6.10.** _Let_[�][∞] _𝑛_ =0 _[𝑎][𝑛]_[(] _[𝑥]_[−] _[𝑥]_[0][)] _[𝑛][be][a][power][series.][If][the][series][is][convergent,][then] either it converges absolutely at all 𝑥_ ∈ ℝ _, or there exists a number 𝜌, such that the series converges absolutely on the interval_ ( _𝑥_ 0 − _𝜌, 𝑥_ 0 + _𝜌_ ) _and diverges when 𝑥 < 𝑥_ 0 − _𝜌 or 𝑥 > 𝑥_ 0 + _𝜌._

The number _𝜌_ is called the _radius of convergence_ of the power series. We write _𝜌_ = ∞ if the series converges for all _𝑥_ , and we write _𝜌_ = 0 if the series is divergent. At the endpoints, that is, if _𝑥_ = _𝑥_ 0 + _𝜌_ or _𝑥_ = _𝑥_ 0 − _𝜌_ , the proposition says nothing, and the series might or might not converge. See . In , the radius of convergence is _𝜌_ = 1, in , the radius of convergence is _𝜌_ = ∞, and in , the radius of convergence is _𝜌_ = 0.

|diverges|?|?|?|converges absolutely|converges absolutely|converges absolutely|?|?|?|diverges|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||_𝑥_0|−_𝜌_||_𝑥_0|||_𝑥_0|+_𝜌_|||


**Figure 2.10:** Convergence of a power series.

_Proof._ Write

_𝑅_ � lim sup | _𝑎𝑛_ |[1][/] _[𝑛] . 𝑛_ →∞

_CHAPTER 2. SEQUENCES AND SERIES_

108

We apply the root test,

**==> picture [340 x 26] intentionally omitted <==**

If _𝑅_ = ∞, then _𝐿_ = ∞ for every _𝑥_ ≠ _𝑥_ 0, and the series diverges by the root test. On the other hand, if _𝑅_ = 0, then _𝐿_ = 0 for every _𝑥_ , and the series converges absolutely for all _𝑥_ . Suppose 0 _< 𝑅 <_ ∞. The series converges absolutely if 1 _> 𝐿_ = _𝑅_ | _𝑥_ − _𝑥_ 0|, that is,

**==> picture [72 x 12] intentionally omitted <==**

The series diverges when 1 _< 𝐿_ = _𝑅_ | _𝑥_ − _𝑥_ 0|, or

**==> picture [72 x 12] intentionally omitted <==**

Letting _𝜌_ �[1] / _𝑅_ completes the proof.

**==> picture [9 x 8] intentionally omitted <==**

It may be useful to restate what we have learned in the proof as a separate proposition. **Proposition 2.6.11.** _Let_[�][∞] _𝑛_ =0 _[𝑎][𝑛]_[(] _[𝑥]_[−] _[𝑥]_[0][)] _[𝑛][be a power series, and let]_

**==> picture [106 x 24] intentionally omitted <==**

_If 𝑅_ = ∞ _, the power series is divergent. If 𝑅_ = 0 _, then the power series converges everywhere. Otherwise, the radius of convergence 𝜌_ =[1] / _𝑅._

Often, the radius of convergence is written as _𝜌_ =[1] / _𝑅_ in all three cases, with the understanding of what _𝜌_ should be if _𝑅_ = 0 or _𝑅_ = ∞.

series can be added and and Convergent power multiplied together, multiplied by constants. The proposition has a straightforward proof using what we know about series in general, and power series in particular. We leave the proof to the reader.