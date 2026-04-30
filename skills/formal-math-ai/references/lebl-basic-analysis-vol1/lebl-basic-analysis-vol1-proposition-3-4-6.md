Proposition 3.4.6

**Proposition 3.4.6.** _A function 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _is uniformly continuous if and only if the limits_

**==> picture [214 x 18] intentionally omitted <==**

_exist and the function_[�] _𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _defined by_

**==> picture [143 x 54] intentionally omitted <==**

_is continuous._

_Proof._ One direction is quick. If[�] _𝑓_ is continuous, then it is uniformly continuous by . As _𝑓_ is the restriction of[�] _𝑓_ to ( _𝑎, 𝑏_ ), _𝑓_ is also uniformly continuous (exercise). Now suppose _𝑓_ is uniformly continuous. We must first show that the limits _𝐿𝑎_ and _𝐿𝑏_ exist. Let us concentrate on _𝐿𝑎_ . Take { _𝑥𝑛_ }[∞] _𝑛_ =1[in][ (] _[𝑎, 𝑏]_[)][ such that][ lim] _[𝑛]_[→∞] _[𝑥][𝑛]_[=] _[𝑎]_[.][The] ∞ sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[is Cauchy, so by] the sequence � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1[is Cauchy and] thus convergent. Let _𝐿_ 1 � lim _𝑛_ →∞ _𝑓_ ( _𝑥𝑛_ ). Take another sequence { _𝑦𝑛_ }[∞] _𝑛_ =1[in][ (] _[𝑎, 𝑏]_[)][ such] that lim _𝑛_ →∞ _𝑦𝑛_ = _𝑎_ . By the same reasoning we get _𝐿_ 2 � lim _𝑛_ →∞ _𝑓_ ( _𝑦𝑛_ ). If we show that _𝐿_ 1 = _𝐿_ 2, then the limit _𝐿𝑎_ = lim _𝑥_ → _𝑎 𝑓_ ( _𝑥_ ) exists. Let _𝜖>_ 0 be given. Find _𝛿>_ 0 such that �� _𝑥_ − _𝑦_ �� _< 𝛿_ implies �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� _< 𝜖_ /3. Find _𝑀_ ∈ ℕ such that for _𝑛_ ≥ _𝑀_ , we have | _𝑎_ − _𝑥𝑛_ | _<[𝛿]_ /2, �� _𝑎_ − _𝑦𝑛_ �� _< 𝛿_ /2, �� _𝑓_ ( _𝑥𝑛_ ) − _𝐿_ 1�� _< 𝜖_ /3, and �� _𝑓_ ( _𝑦𝑛_ ) − _𝐿_ 2�� _< 𝜖_ /3. Then for _𝑛_ ≥ _𝑀_ , �� _𝑥𝑛_ − _𝑦𝑛_ �� = �� _𝑥𝑛_ − _𝑎_ + _𝑎_ − _𝑦𝑛_ �� ≤| _𝑥𝑛_ − _𝑎_ | + �� _𝑎_ − _𝑦𝑛_ �� _< 𝛿_ /2 + _𝛿_ /2 = _𝛿._

So

**==> picture [376 x 119] intentionally omitted <==**

Therefore, _𝐿_ 1 = _𝐿_ 2. Thus _𝐿𝑎_ exists. To show that _𝐿𝑏_ exists is left as an exercise. If _𝐿𝑎_ = lim _𝑥_ → _𝑎 𝑓_ ( _𝑥_ ) exists, then lim _𝑥_ → _𝑎_[�] _𝑓_ ( _𝑥_ ) exists and equals _𝐿𝑎_ (see ). Similarly for _𝐿𝑏_ . Hence[�] _𝑓_ is continuous at _𝑎_ and _𝑏_ . And since _𝑓_ is continuous at _𝑐_ ∈( _𝑎, 𝑏_ ), then[�] _𝑓_ is continuous at _𝑐_ ∈( _𝑎, 𝑏_ ) ( again). □

A typical application of this proposition (together with ) is the following. Suppose _𝑓_ : (−1 _,_ 0) ∪(0 _,_ 1) → ℝ is uniformly continuous, then lim _𝑥_ →0 _𝑓_ ( _𝑥_ ) exists and the function has a _removable singularity_ , that is, we can extend the function to a continuous function on (−1 _,_ 1).

_3.4. UNIFORM CONTINUITY_

141

## **3.4.3 Lipschitz continuous functions**