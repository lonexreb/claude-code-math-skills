Corollary 6.2.13

**Corollary 6.2.13.** _Let_[�][∞] _𝑛_ =0 _[𝑐][𝑛]_[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛][be a convergent power series with a radius of convergence]_ 0 _< 𝜌_ ≤∞ _. Let 𝐼_ � ( _𝑎_ − _𝜌, 𝑎_ + _𝜌_ ) _if 𝜌<_ ∞ _or 𝐼_ � ℝ _if 𝜌_ = ∞ _. Let 𝑓_ : _𝐼_ → ℝ _be the limit. Then 𝑓 is a differentiable function, and_

**==> picture [157 x 35] intentionally omitted <==**

_. where the radius of convergence of this series is 𝜌_

_Proof._ Take 0 _< 𝑟 < 𝜌_ . The series converges uniformly on [ _𝑎_ − _𝑟, 𝑎_ + _𝑟_ ], but we need uniform convergence of the derivative. Let

**==> picture [106 x 24] intentionally omitted <==**

As the series is convergent _𝑅 <_ ∞, and the radius of convergence is[1] / _𝑅_ (or ∞ if _𝑅_ = 0).

Let _𝜖>_ 0 be given. In , we saw lim _𝑛_ →∞ _𝑛_[1][/] _[𝑛]_ = 1. Hence there exists an _𝑁_ such that for all _𝑛_ ≥ _𝑁_ , we have _𝑛_[1][/] _[𝑛] <_ 1 + _𝜖_ . So

**==> picture [380 x 24] intentionally omitted <==**

As _𝜖_ was arbitrary, lim sup _𝑛_ →∞ | _𝑛𝑐𝑛_ |[1][/] _[𝑛]_ = _𝑅_ . Therefore,[�][∞] _𝑛_ =1 _[𝑛𝑐][𝑛]_[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛]_[has][radius][of] convergence _𝜌_ . By dividing by ( _𝑥_ − _𝑎_ ), we find[�][∞] _𝑛_ =0[(] _[𝑛]_[+][ 1][)] _[𝑐][𝑛]_[+][1][(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛]_[has][radius][of] as well. convergence _𝜌_

Consequently, the partial sums[�] _𝑛[𝑘]_ =0[(] _[𝑛]_[+][ 1][)] _[𝑐][𝑛]_[+][1][(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛]_[, which are derivatives of the] partial sums[�] _𝑛[𝑘]_[+] =[1] 0 _[𝑐][𝑛]_[(] _[𝑥]_[−] _[𝑎]_[)] _[𝑛]_[, converge uniformly on][ [] _[𝑎]_[−] _[𝑟, 𝑎]_[+] _[ 𝑟]_[]][.][Furthermore, the series] clearly converges at _𝑥_ = _𝑎_ . We may thus apply , and we are done as _𝑟 < 𝜌_ was arbitrary. □