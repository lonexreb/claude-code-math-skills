Lemma 5.2.7

**Lemma 5.2.7.** _If 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is a continuous function, then 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _._

_Proof._ As _𝑓_ is continuous on a closed bounded interval, it is bounded and uniformly continuous. Given _𝜖>_ 0, find a _𝛿>_ 0 such that �� _𝑥_ − _𝑦_ �� _< 𝛿_ implies �� _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑦_ )�� _< 𝑏_ − _𝜖 𝑎_[.] Let _𝑃_ = { _𝑥_ 0 _, 𝑥_ 1 _, . . . , 𝑥𝑛_ } be a partition of [ _𝑎, 𝑏_ ] such that Δ _𝑥𝑖 < 𝛿_ for all _𝑖_ = 1 _,_ 2 _, . . . , 𝑛_ . For example, take _𝑛_ such that _[𝑏]_[−] _𝑛[𝑎] < 𝛿_ , and let _𝑥𝑖_ � _𝑛[𝑖]_[(] _[𝑏]_[−] _[𝑎]_[)+] _[ 𝑎]_[.][Then for all] _[ 𝑥, 𝑦]_[∈[] _[𝑥][𝑖]_[−][1] _[, 𝑥][𝑖]_[]][,] we have �� _𝑥_ − _𝑦_ �� ≤ Δ _𝑥𝑖 < 𝛿_ , and so

**==> picture [184 x 24] intentionally omitted <==**

As _𝑓_ is continuous on [ _𝑥𝑖_ −1 _, 𝑥𝑖_ ], it attains a maximum and a minimum on this interval. Let _𝑥_ be a point where _𝑓_ attains the maximum and _𝑦_ be a point where _𝑓_ attains the minimum. Then _𝑓_ ( _𝑥_ ) = _𝑀𝑖_ and _𝑓_ ( _𝑦_ ) = _𝑚𝑖_ in the notation from the definition of the integral. Therefore,

**==> picture [162 x 23] intentionally omitted <==**

And so

**==> picture [223 x 186] intentionally omitted <==**

As _𝜖>_ 0 was arbitrary,

**==> picture [271 x 51] intentionally omitted <==**

and _𝑓_ is Riemann integrable on [ _𝑎, 𝑏_ ].

The second lemma says that we need the function to only be “Riemann integrable inside the interval,” as long as it is bounded. It also tells us how to compute the integral.