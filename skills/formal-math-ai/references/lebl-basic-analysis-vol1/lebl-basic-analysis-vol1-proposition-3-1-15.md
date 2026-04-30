Proposition 3.1.15

**Proposition 3.1.15.** _Let 𝑆_ ⊂ ℝ _, 𝑐_ ∈ ℝ _, and let 𝑓_ : _𝑆_ → ℝ _be a function. Suppose 𝐴_ ⊂ _𝑆 is such that there is some 𝛼>_ 0 _such that_ ( _𝐴_ \ { _𝑐_ }) ∩( _𝑐_ − _𝛼, 𝑐_ + _𝛼_ ) = ( _𝑆_ \ { _𝑐_ }) ∩( _𝑐_ − _𝛼, 𝑐_ + _𝛼_ ) _._

- _(i) The point 𝑐 is a cluster point of 𝐴 if and only if 𝑐 is a cluster point of 𝑆._

- _(ii) Supposing 𝑐 is a cluster point of 𝑆, then 𝑓_ ( _𝑥_ ) → _𝐿 as 𝑥_ → _𝑐 if and only if 𝑓_ | _𝐴_ ( _𝑥_ ) → _𝐿 as 𝑥_ → _𝑐._

_Proof._ First, let _𝑐_ be a cluster point of _𝐴_ . Since _𝐴_ ⊂ _𝑆_ , then if ( _𝐴_ \ { _𝑐_ }) ∩( _𝑐_ − _𝜖, 𝑐_ + _𝜖_ ) is nonempty for every _𝜖>_ 0, then ( _𝑆_ \ { _𝑐_ }) ∩( _𝑐_ − _𝜖, 𝑐_ + _𝜖_ ) is nonempty for every _𝜖>_ 0. Thus _𝑐_ is a cluster point of _𝑆_ . Second, suppose _𝑐_ is a cluster point of _𝑆_ . Then for _𝜖>_ 0 such that _𝜖< 𝛼_ we get that ( _𝐴_ \ { _𝑐_ }) ∩( _𝑐_ − _𝜖, 𝑐_ + _𝜖_ ) = ( _𝑆_ \ { _𝑐_ }) ∩( _𝑐_ − _𝜖, 𝑐_ + _𝜖_ ), which is nonempty. This is true for all _𝜖< 𝛼_ and hence ( _𝐴_ \ { _𝑐_ }) ∩( _𝑐_ − _𝜖, 𝑐_ + _𝜖_ ) must be nonempty for all _𝜖>_ 0. Thus _𝑐_ is a cluster point of _𝐴_ .

Now suppose _𝑐_ is a cluster point of _𝑆_ and _𝑓_ ( _𝑥_ ) → _𝐿_ as _𝑥_ → _𝑐_ . That is, for every _𝜖>_ 0 there is a _𝛿>_ 0 such that if _𝑥_ ∈ _𝑆_ \ { _𝑐_ } and | _𝑥_ − _𝑐_ | _< 𝛿_ , then �� _𝑓_ ( _𝑥_ ) − _𝐿_ �� _< 𝜖_ . Because _𝐴_ ⊂ _𝑆_ , if _𝑥_ ∈ _𝐴_ \ { _𝑐_ }, then _𝑥_ ∈ _𝑆_ \ { _𝑐_ }, and hence _𝑓_ | _𝐴_ ( _𝑥_ ) → _𝐿_ as _𝑥_ → _𝑐_ .

Finally, suppose _𝑓_ | _𝐴_ ( _𝑥_ ) → _𝐿_ as _𝑥_ → _𝑐_ and let _𝜖>_ 0 be given. There is a _𝛿_[′] _>_ 0 such that if _𝑥_ ∈ _𝐴_ \ { _𝑐_ } and | _𝑥_ − _𝑐_ | _< 𝛿_[′] , then �� _𝑓_ | _𝐴_ ( _𝑥_ ) − _𝐿_ �� _< 𝜖_ . Take _𝛿_ � min{ _𝛿_ ′ _, 𝛼_ }. Now suppose _𝑥_ ∈ _𝑆_ \ { _𝑐_ } and | _𝑥_ − _𝑐_ | _< 𝛿_ . As | _𝑥_ − _𝑐_ | _< 𝛼_ , we find _𝑥_ ∈ _𝐴_ \ { _𝑐_ }, and as | _𝑥_ − _𝑐_ | _< 𝛿_[′] , we get �� _𝑓_ ( _𝑥_ ) − _𝐿_ �� = �� _𝑓_ | _𝐴_ ( _𝑥_ ) − _𝐿_ �� _< 𝜖_ . □

The hypothesis on _𝐴_ in the proposition is necessary. For an arbitrary restriction we generally get an implication in only one direction, see . The usual notation for the limit is

**==> picture [120 x 24] intentionally omitted <==**

A common use of restriction with respect to limits, which does not satisfy the hypothesis in the proposition, is the so-called _one-sided limit_