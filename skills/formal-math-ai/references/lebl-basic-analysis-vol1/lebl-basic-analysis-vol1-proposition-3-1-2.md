Proposition 3.1.2

**Proposition 3.1.2.** _Let 𝑆_ ⊂ ℝ _. Then 𝑥_ ∈ ℝ _is a cluster point of 𝑆 if and only if there exists a convergent sequence of numbers_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[such that][ 𝑥][𝑛]_[≠] _[𝑥][and][ 𝑥][𝑛]_[∈] _[𝑆][for all][ 𝑛][, and] 𝑛_[lim] →∞ _[𝑥][𝑛]_[=] _[𝑥][.]_

_CHAPTER 3. CONTINUOUS FUNCTIONS_

114

_Proof._ First suppose _𝑥_ is a cluster point of _𝑆_ . For every _𝑛_ ∈ ℕ, pick _𝑥𝑛_ to be an arbitrary point of ( _𝑥_ −[1] / _𝑛, 𝑥_ +[1] / _𝑛_ ) ∩ _𝑆_ \ { _𝑥_ }, which is nonempty because _𝑥_ is a cluster point of _𝑆_ . Then _𝑥𝑛_ is within[1] / _𝑛_ of _𝑥_ , that is,

**==> picture [73 x 13] intentionally omitted <==**

As {[1] / _𝑛_ }[∞] _𝑛_ =1[converges to zero,][ {] _[𝑥][𝑛]_[}][∞] _𝑛_ =1[converges to] _[ 𝑥]_[.] On the other hand, if we start with a sequence of numbers { _𝑥𝑛_ }[∞] _𝑛_ =1[in] _[𝑆]_[converging] to _𝑥_ such that _𝑥𝑛_ ≠ _𝑥_ for all _𝑛_ , then for every _𝜖>_ 0 there is an _𝑀_ such that, in particular, | _𝑥𝑀_ − _𝑥_ | _< 𝜖_ . That is, _𝑥𝑀_ ∈( _𝑥_ − _𝜖, 𝑥_ + _𝜖_ ) ∩ _𝑆_ \ { _𝑥_ }. □

## **3.1.2 Limits of functions**

If a function _𝑓_ is defined on a set _𝑆_ and _𝑐_ is a cluster point of _𝑆_ , then we define the limit of _𝑓_ ( _𝑥_ ) as _𝑥_ approaches _𝑐_ . It is irrelevant for the definition whether _𝑓_ is defined at _𝑐_ or not. Even if the function is defined at _𝑐_ , the limit of the function as _𝑥_ goes to _𝑐_ can very well be different from _𝑓_ ( _𝑐_ ).