Proposition 3.2.2

**Proposition 3.2.2.** _Consider a function 𝑓_ : _𝑆_ → ℝ _defined on a set 𝑆_ ⊂ ℝ _and let 𝑐_ ∈ _𝑆. Then:_

- _(i) If 𝑐 is not a cluster point of 𝑆, then 𝑓 is continuous at 𝑐._

- _(ii) If 𝑐 is a cluster point of 𝑆, then 𝑓 is continuous at 𝑐 if and only if the limit of 𝑓_ ( _𝑥_ ) _as 𝑥_ → _𝑐 exists and_

   - lim _[𝑓]_[(] _[𝑐]_[)] _[.] 𝑥_ → _𝑐[𝑓]_[(] _[𝑥]_[)][ =]

- _(iii) The function 𝑓 is continuous at 𝑐 if and only if for every sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[where][𝑥][𝑛]_[∈] _[𝑆]_ ∞

- _and 𝑛_ lim→∞ _[𝑥][𝑛]_[=] _[𝑐][, the sequence]_ � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1 _[converges to][𝑓]_[(] _[𝑐]_[)] _[.]_

123

## _3.2. CONTINUOUS FUNCTIONS_

_Proof._ We start with . Suppose _𝑐_ is not a cluster point of _𝑆_ . Then there exists a _𝛿>_ 0 such that _𝑆_ ∩( _𝑐_ − _𝛿, 𝑐_ + _𝛿_ ) = { _𝑐_ }. For any _𝜖>_ 0, simply pick this given _𝛿_ . The only _𝑥_ ∈ _𝑆_ such that | _𝑥_ − _𝑐_ | _< 𝛿_ is _𝑥_ = _𝑐_ . Then �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ )�� = �� _𝑓_ ( _𝑐_ ) − _𝑓_ ( _𝑐_ )�� = 0 _< 𝜖_ . Let us move to . Suppose _𝑐_ is a cluster point of _𝑆_ . Let us first suppose that lim _𝑥_ → _𝑐 𝑓_ ( _𝑥_ ) = _𝑓_ ( _𝑐_ ). Then for every _𝜖>_ 0, there is a _𝛿>_ 0 such that if _𝑥_ ∈ _𝑆_ \ { _𝑐_ } and | _𝑥_ − _𝑐_ | _< 𝛿_ , then �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ )�� _< 𝜖_ . Also �� _𝑓_ ( _𝑐_ ) − _𝑓_ ( _𝑐_ )�� = 0 _< 𝜖_ , so the definition of continuity at _𝑐_ is satisfied. On the other hand, suppose _𝑓_ is continuous at _𝑐_ . For every _𝜖>_ 0, there exists a _𝛿>_ 0 such that for _𝑥_ ∈ _𝑆_ where | _𝑥_ − _𝑐_ | _< 𝛿_ , we have �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ )�� _< 𝜖_ . Then the statement is, of course, still true if _𝑥_ ∈ _𝑆_ \ { _𝑐_ } ⊂ _𝑆_ . Therefore, lim _𝑥_ → _𝑐 𝑓_ ( _𝑥_ ) = _𝑓_ ( _𝑐_ ). For , first suppose _𝑓_ is continuous at _𝑐_ . Let { _𝑥𝑛_ }[∞] _𝑛_ =1[be a sequence such that] _[ 𝑥][𝑛]_[∈] _[𝑆]_ and lim _𝑛_ →∞ _𝑥𝑛_ = _𝑐_ . Let _𝜖>_ 0 be given. Find a _𝛿>_ 0 such that �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ )�� _< 𝜖_ for all _𝑥_ ∈ _𝑆_ where | _𝑥_ − _𝑐_ | _< 𝛿_ . Find an _𝑀_ ∈ ℕ such that for _𝑛_ ≥ _𝑀_ , we have | _𝑥𝑛_ − _𝑐_ | _< 𝛿_ . Then ∞ for _𝑛_ ≥ _𝑀_ , we have that �� _𝑓_ ( _𝑥𝑛_ ) − _𝑓_ ( _𝑐_ )�� _< 𝜖_ , so � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1[converges to] _[𝑓]_[(] _[𝑐]_[)][.] We prove the other direction of by contrapositive. Suppose _𝑓_ is not continuous at _𝑐_ . Then there exists an _𝜖>_ 0 such that for every _𝛿>_ 0, there exists an _𝑥_ ∈ _𝑆_ such that | _𝑥_ − _𝑐_ | _< 𝛿_ and �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ )�� ≥ _𝜖_ . Define a sequence { _𝑥𝑛_ }∞ _𝑛_ =1[as][follows.][Let] _[𝑥][𝑛]_[∈] _[𝑆]_[be] such that | _𝑥𝑛_ − _𝑐_ | _<_[1] / _𝑛_ and �� _𝑓_ ( _𝑥𝑛_ ) − _𝑓_ ( _𝑐_ )�� ≥ _𝜖_ . Now { _𝑥𝑛_ }∞ _𝑛_ =1[is a sequence in] _[ 𝑆]_[such that] ∞ lim _𝑛_ →∞ _𝑥𝑛_ = _𝑐_ and such that �� _𝑓_ ( _𝑥𝑛_ ) − _𝑓_ ( _𝑐_ )�� ≥ _𝜖_ for all _𝑛_ ∈ ℕ. Thus � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1[does not] converge to _𝑓_ ( _𝑐_ ). It may or may not converge, but it definitely does not converge to _𝑓_ ( _𝑐_ ). □

The last item in the proposition is particularly powerful. It allows us to quickly apply what we know about limits of sequences to continuous functions and even to prove that certain functions are continuous. It can also be strengthened, see .