Proposition 7.5.2

**Proposition 7.5.2.** _Let_ ( _𝑋, 𝑑𝑋_ ) _and_ ( _𝑌, 𝑑𝑌_ ) _be metric spaces. Then 𝑓_ : _𝑋_ → _𝑌 is continuous at_ ∞ _𝑐_ ∈ _𝑋 if and only if for every sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[in][𝑋][converging][to][𝑐][,][the][sequence]_ � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1 _converges to 𝑓_ ( _𝑐_ ) _. Proof._ Suppose _𝑓_ is continuous at _𝑐_ . Let { _𝑥𝑛_ }[∞] _𝑛_ =1[be a sequence in] _[ 𝑋]_[converging to] _[ 𝑐]_[.][Given] _𝜖>_ 0, there is a _𝛿>_ 0 such that _𝑑𝑋_ ( _𝑥, 𝑐_ ) _< 𝛿_ implies _𝑑𝑌_ � _𝑓_ ( _𝑥_ ) _, 𝑓_ ( _𝑐_ )[�] _< 𝜖_ . So take _𝑀_ such ∞ that for all _𝑛_ ≥ _𝑀_ , we have _𝑑𝑋_ ( _𝑥𝑛 , 𝑐_ ) _< 𝛿_ , then _𝑑𝑌_ � _𝑓_ ( _𝑥𝑛_ ) _, 𝑓_ ( _𝑐_ )[�] _< 𝜖_ . Hence � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1 converges to _𝑓_ ( _𝑐_ ). On the other hand, suppose _𝑓_ is not continuous at _𝑐_ . Then there exists an _𝜖>_ 0, such that for every _𝑛_ ∈ ℕ there exists an _𝑥𝑛_ ∈ _𝑋_ , with _𝑑𝑋_ ( _𝑥𝑛 , 𝑐_ ) _<_[1] / _𝑛_ such that _𝑑𝑌_ � _𝑓_ ( _𝑥𝑛_ ) _, 𝑓_ ( _𝑐_ )[�] ≥ _𝜖_ . Then { _𝑥𝑛_ }[∞] _𝑛_ =1[converges to] _[ 𝑐]_[, but] � _𝑓_ ( _𝑥𝑛_ )�∞ _𝑛_ =1[does not converge to] _[𝑓]_[(] _[𝑐]_[)][.] □ **Example 7.5.3:** Suppose _𝑓_ : ℝ[2] → ℝ is a polynomial. That is,

**==> picture [447 x 41] intentionally omitted <==**

∞ for some _𝑑_ ∈ ℕ (the degree) and _𝑎 𝑗𝑘_ ∈ ℝ. We claim _𝑓_ is continuous. Let �( _𝑥𝑛 , 𝑦𝑛_ )� _𝑛_ =1[be a] sequence in ℝ[2] that converges to ( _𝑥, 𝑦_ ) ∈ ℝ[2] . We proved that this means lim _𝑛_ →∞ _𝑥𝑛_ = _𝑥_ and lim _𝑛_ →∞ _𝑦𝑛_ = _𝑦_ . By ,

**==> picture [336 x 41] intentionally omitted <==**

So _𝑓_ is continuous at ( _𝑥, 𝑦_ ), and as ( _𝑥, 𝑦_ ) was arbitrary _𝑓_ is continuous everywhere. Similarly, a polynomial in _𝑛_ variables is continuous.

Be careful about taking limits separately. Consider _𝑓_ : ℝ[2] → ℝ defined by _𝑓_ ( _𝑥, 𝑦_ ) � _𝑥_[2] _𝑥_ + _𝑦𝑦_[2][outside][the][origin][and] _[𝑓]_[(][0] _[,]_[ 0][)][�][0][.][See] . In , you are asked to prove that _𝑓_ is not continuous at the origin. However, for every _𝑦_ , the function _𝑔_ ( _𝑥_ ) � _𝑓_ ( _𝑥, 𝑦_ ) is continuous, and for every _𝑥_ , the function _ℎ_ ( _𝑦_ ) � _𝑓_ ( _𝑥, 𝑦_ ) is continuous.

_7.5. CONTINUOUS FUNCTIONS_

289

**==> picture [192 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
푧<br>푦<br>푥<br>**----- End of picture text -----**<br>


_𝑥 𝑦_ **Figure 7.14:** Graph of _𝑥_[2] + _𝑦_[2][.]