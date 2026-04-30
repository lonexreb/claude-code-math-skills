Example 5.1.4

**Example 5.1.4:** Take the Dirichlet function _𝑓_ : [0 _,_ 1] → ℝ, where _𝑓_ ( _𝑥_ ) � 1 if _𝑥_ ∈ ℚ and _𝑓_ ( _𝑥_ ) � 0 if _𝑥_ ∉ ℚ. Then

**==> picture [168 x 32] intentionally omitted <==**

The reason is that for any partition _𝑃_ and every _𝑖_ , we have _𝑚𝑖_ = inf� _𝑓_ ( _𝑥_ ) : _𝑥_ ∈[ _𝑥𝑖_ −1 _, 𝑥𝑖_ ]� = 0 and _𝑀𝑖_ = sup� _𝑓_ ( _𝑥_ ) : _𝑥_ ∈[ _𝑥𝑖_ −1 _, 𝑥𝑖_ ]� = 1. Thus

**==> picture [354 x 35] intentionally omitted <==**

_𝑏 𝑏 Remark_ 5.1.5 _._ The same definition of ∫ _𝑎 𝑓_ and ∫ _𝑎[𝑓]_[is used when] _[𝑓]_[is defined on a larger set] _𝑆_ such that [ _𝑎, 𝑏_ ] ⊂ _𝑆_ . In that case, we use the restriction of _𝑓_ to [ _𝑎, 𝑏_ ] and we must ensure that the restriction is bounded on [ _𝑎, 𝑏_ ].

To compute the integral, we often take a partition _𝑃_ and make it finer. That is, we cut intervals in the partition into yet smaller pieces.

� **Definition 5.1.6.** Let _𝑃_ = { _𝑥_ 0 _, 𝑥_ 1 _, . . . , 𝑥𝑛_ } and _𝑃_[�] = { _𝑥_ 0 _,_ � _𝑥_ 1 _, . . . ,_ � _𝑥ℓ_ } be partitions of [ _𝑎, 𝑏_ ]. We say _𝑃_[�] is a _refinement_ of _𝑃_ if as sets _𝑃_ ⊂ _𝑃_[�] .

That is, _𝑃_[�] is a refinement of a partition if it contains all the numbers in _𝑃_ and perhaps some other numbers in between. For example, {0 _,_ 0 _._ 5 _,_ 1 _,_ 2} is a partition of [0 _,_ 2] and {0 _,_ 0 _._ 2 _,_ 0 _._ 5 _,_ 1 _,_ 1 _._ 5 _,_ 1 _._ 75 _,_ 2} is a refinement. The main reason for introducing refinements is the following proposition.