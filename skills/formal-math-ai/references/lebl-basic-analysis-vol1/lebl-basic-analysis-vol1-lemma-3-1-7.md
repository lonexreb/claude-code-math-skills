Lemma 3.1.7

**Lemma 3.1.7.** _Let 𝑆_ ⊂ ℝ _, let 𝑐 be a cluster point of 𝑆, let 𝑓_ : _𝑆_ → ℝ _be a function, and let 𝐿_ ∈ ℝ _. Then 𝑓_ ( _𝑥_ ) → _𝐿 as 𝑥_ → _𝑐 if and only if for every sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[such that][ 𝑥][𝑛]_[∈] _[𝑆]_[\ {] _[𝑐]_[}] _[ for]_ ∞ _all 𝑛, and such that_ lim _𝑛_ →∞ _𝑥𝑛_ = _𝑐, we have that the sequence_ � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1 _[converges to][ 𝐿][.]_

_Proof._ Suppose _𝑓_ ( _𝑥_ ) → _𝐿_ as _𝑥_ → _𝑐_ , and { _𝑥𝑛_ }[∞] _𝑛_ =1[is a sequence such that] _[ 𝑥][𝑛]_[∈] _[𝑆]_[\ {] _[𝑐]_[}][ and] ∞ lim _𝑛_ →∞ _𝑥𝑛_ = _𝑐_ . We wish to show that � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1[converges to] _[ 𝐿]_[.][Let] _[ 𝜖>]_[ 0][ be given.][Find] a _𝛿>_ 0 such that if _𝑥_ ∈ _𝑆_ \ { _𝑐_ } and | _𝑥_ − _𝑐_ | _< 𝛿_ , then �� _𝑓_ ( _𝑥_ ) − _𝐿_ �� _< 𝜖_ . As { _𝑥𝑛_ }∞ _𝑛_ =1[converges] to _𝑐_ , find an _𝑀_ such that for _𝑛_ ≥ _𝑀_ , we have that | _𝑥𝑛_ − _𝑐_ | _< 𝛿_ . Therefore, for _𝑛_ ≥ _𝑀_ ,

**==> picture [80 x 17] intentionally omitted <==**

∞ Thus � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1[converges to] _[ 𝐿]_[.]

For the other direction, we use proof by contrapositive. Suppose it is not true that _𝑓_ ( _𝑥_ ) → _𝐿_ as _𝑥_ → _𝑐_ . The negation of the definition is that there exists an _𝜖>_ 0 such that for every _𝛿>_ 0 there exists an _𝑥_ ∈ _𝑆_ \ { _𝑐_ }, where | _𝑥_ − _𝑐_ | _< 𝛿_ and �� _𝑓_ ( _𝑥_ ) − _𝐿_ �� ≥ _𝜖_ . Let us use[1] / _𝑛_ for _𝛿_ in the statement above to construct a sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[.][We have] that there exists an _𝜖>_ 0 such that for every _𝑛_ , there exists a point _𝑥𝑛_ ∈ _𝑆_ \ { _𝑐_ }, where | _𝑥𝑛_ − _𝑐_ | _<_[1] / _𝑛_ and �� _𝑓_ ( _𝑥𝑛_ ) − _𝐿_ �� ≥ _𝜖_ . The sequence { _𝑥𝑛_ }∞ _𝑛_ =1[just constructed converges to] _[𝑐]_[,] but the sequence � _𝑓_ ( _𝑥𝑛_ )�∞ _𝑛_ =1[does not converge to] _[ 𝐿]_[.][And we are done.] □

It is possible to strengthen the reverse direction of the lemma by simply stating that “� _𝑓_ ( _𝑥𝑛_ )�∞ _𝑛_ =1[converges,” without requiring a specific limit.][See] .

lim[lim][See] . **Example 3.1.8:** _𝑥_ →0[sin][(][1][/] _[𝑥]_[)][ does not exist, but] _𝑥_ →0 _[𝑥]_[sin][(][1][/] _[𝑥]_[)][ =][ 0.]

**==> picture [219 x 149] intentionally omitted <==**

**==> picture [219 x 147] intentionally omitted <==**

**Figure 3.2:** Graphs of sin([1] / _𝑥_ ) and _𝑥_ sin([1] / _𝑥_ ). Note that the computer cannot properly graph sin([1] / _𝑥_ ) near zero as it oscillates too fast.

_3.1. LIMITS OF FUNCTIONS_

117

1 Proof: We start with sin([1] / _𝑥_ ). Define a sequence by _𝑥𝑛_ � _𝜋𝑛_ + _[𝜋]_ /2[.][It is not hard to see] that lim _𝑛_ →∞ _𝑥𝑛_ = 0. Furthermore,

**==> picture [170 x 13] intentionally omitted <==**

∞ Therefore, �sin([1] / _𝑥𝑛_ )� _𝑛_ =1[does not converge.][By] , _𝑥_ lim→0[sin][(][1][/] _[𝑥]_[)][ does not exist.] Now consider _𝑥_ sin([1] / _𝑥_ ). Let { _𝑥𝑛_ }[∞] _𝑛_ =1[be a sequence such that] _[ 𝑥][𝑛]_[≠][0][ for all] _[ 𝑛]_[, and such] that lim _𝑛_ →∞ _𝑥𝑛_ = 0. Notice that |sin( _𝑡_ )| ≤ 1 for all _𝑡_ ∈ ℝ. Therefore,

**==> picture [208 x 12] intentionally omitted <==**

∞ As _𝑥𝑛_ goes to 0, then | _𝑥𝑛_ | goes to zero, and hence � _𝑥𝑛_ sin([1] / _𝑥𝑛_ )� _𝑛_ =1[converges to zero.][By] , lim _𝑥_ →0 _[𝑥]_[sin][(][1][/] _[𝑥]_[)][ =][ 0.]

Keep in mind the phrase “for every sequence” in the lemma. For example, take sin([1] / _𝑥_ ) ∞ and the sequence given by _𝑥𝑛_ �[1] / _𝜋𝑛_ . Then �sin([1] / _𝑥𝑛_ )� _𝑛_ =1[is the constant zero sequence,] and therefore converges to zero, but the limit of sin([1] / _𝑥_ ) as _𝑥_ → 0 does not exist.

Using , we can start applying everything we know about sequential limits to limits of functions. Let us give a few important examples.