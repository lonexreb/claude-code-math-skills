Theorem 6.2.10

**Theorem 6.2.10.** _Let 𝐼 be a bounded interval and let 𝑓𝑛_ : _𝐼_ → ℝ _be continuously differentiable functions. Suppose_ { _𝑓𝑛_[′][}][∞] _𝑛_ =1 _[converges][uniformly][to][𝑔]_[:] _[𝐼]_[→][ℝ] _[,][and][suppose]_ � _𝑓𝑛_ ( _𝑐_ )�∞ _𝑛_ =1 _[is] a convergent sequence for some 𝑐_ ∈ _𝐼. Then_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges][uniformly][to][a][continuously] differentiable function 𝑓_ : _𝐼_ → ℝ _, and 𝑓_[′] = _𝑔._

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

240

_Proof._ Define _𝑓_ ( _𝑐_ ) � lim _𝑛_ →∞ _𝑓𝑛_ ( _𝑐_ ). As _𝑓𝑛_[′][are continuous and hence Riemann integrable,] then via the fundamental theorem of calculus, we find that for _𝑥_ ∈ _𝐼_ ,

**==> picture [115 x 31] intentionally omitted <==**

As { _𝑓𝑛_[′][}][∞] _𝑛_ =1[converges uniformly on] _[ 𝐼]_[, it converges uniformly on][ [] _[𝑐, 𝑥]_[]][ (or][ [] _[𝑥, 𝑐]_[]][ if] _[𝑥][<][𝑐]_[).] Thus, the limit as _𝑛_ →∞ on the right-hand side exists. Define _𝑓_ at the remaining points (where _𝑥_ ≠ _𝑐_ ) by this limit:

**==> picture [244 x 30] intentionally omitted <==**

The function _𝑔_ is continuous, being the uniform limit of continuous functions. Hence _𝑓_ is differentiable and _𝑓_[′] ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) for all _𝑥_ ∈ _𝐼_ by the second form of the fundamental theorem.

It remains to prove uniform convergence. Suppose _𝐼_ has a lower bound _𝑎_ and upper bound _𝑏_ . Let _𝜖>_ 0 be given. Take _𝑀_ such that for all _𝑛_ ≥ _𝑀_ , we have �� _𝑓_ ( _𝑐_ ) − _𝑓𝑛_ ( _𝑐_ )�� _< 𝜖_ /2 and �� _𝑔_ ( _𝑥_ ) − _𝑓𝑛_ ′[(] _[𝑥]_[)] �� _<_ 2( _𝑏𝜖_ − _𝑎_ )[for all] _[ 𝑥]_[∈] _[𝐼]_[.][Then]

**==> picture [370 x 129] intentionally omitted <==**

The proof goes through without boundedness of _𝐼_ , except for the uniform convergence of _𝑓𝑛_ to _𝑓_ . As an example suppose _𝐼_ = ℝ and let _𝑓𝑛_ ( _𝑥_ ) � _[𝑥]_ / _𝑛_ . Then _𝑓𝑛_[′][(] _[𝑥]_[)][=][1][/] _[𝑛]_[,][which] converges uniformly to 0. However, { _𝑓𝑛_ }[∞] _𝑛_ =1[converges to 0 only pointwise.]

## **6.2.4 Convergence of power series**

In we saw that a power series converges absolutely inside its radius of convergence, so it converges pointwise. Let us show that it (and all its derivatives) also converges uniformly. This fact allows us to swap several types of limits. Not only is the limit continuous, we can integrate and even differentiate convergent power series term by term.