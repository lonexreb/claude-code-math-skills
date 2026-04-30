Theorem 6.2.4

**Theorem 6.2.4.** _Let_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[be][a][sequence][of][Riemann][integrable][functions][𝑓][𝑛]_[:][[] _[𝑎, 𝑏]_[]][→][ℝ] _converging uniformly to 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _. Then 𝑓 is Riemann integrable, and_

**==> picture [106 x 32] intentionally omitted <==**

> _Proof._ Let _𝜖>_ 0 be given. As _𝑓𝑛_ goes to _𝑓_ uniformly, we find an _𝑀_ ∈ ℕ such that for all _𝑛_ ≥ _𝑀_ , we have �� _𝑓𝑛_ ( _𝑥_ ) − _𝑓_ ( _𝑥_ )�� _<_ 2( _𝑏𝜖_ − _𝑎_ )[for all] _[ 𝑥]_[∈[] _[𝑎, 𝑏]_[]][.][In particular, by reverse triangle] inequality, �� _𝑓_ ( _𝑥_ )�� _<_ 2( _𝑏𝜖_ − _𝑎_ )[+] �� _𝑓𝑛_ ( _𝑥_ )�� for all _𝑥_ . Hence _𝑓_ is bounded, as _𝑓𝑛_ is bounded. Note that _𝑓𝑛_ is integrable and compute

**==> picture [464 x 191] intentionally omitted <==**

. The first inequality is The second inequality follows by and the fact that for all _𝑥_ ∈[ _𝑎, 𝑏_ ], we have 2( _𝑏_ −− _𝜖𝑎_ ) _[<][𝑓]_[(] _[𝑥]_[) −] _[𝑓][𝑛]_[(] _[𝑥]_[)] _[<]_ 2( _𝑏𝜖_ − _𝑎_ )[.][As] _[𝜖>]_[0][was] arbitrary, _𝑓_ is Riemann integrable.

_𝑏_ Finally, we compute ∫ _𝑎[𝑓]_[.][We apply] in the calculation. Again, for all _𝑛_ ≥ _𝑀_ (where _𝑀_ is the same as above),

**==> picture [469 x 120] intentionally omitted <==**

**==> picture [139 x 32] intentionally omitted <==**

It is impossible to compute the integrals for any particular _𝑛_ using calculus as sin( _𝑛𝑥_[2] ) has no closed-form antiderivative. However, we can compute the limit. We have shown before

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

238

that _[𝑛𝑥]_[+][sin] _𝑛_[(] _[𝑛𝑥]_[2][)] converges uniformly on [0 _,_ 1] to _𝑥_ . By , the limit exists and

**==> picture [224 x 32] intentionally omitted <==**