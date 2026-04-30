Corollary 5.2.3

**Corollary 5.2.3.** _If 𝑓_ ∈ _R_[�] [ _𝑎, 𝑏_ ][�] _and_ [ _𝑐, 𝑑_ ] ⊂[ _𝑎, 𝑏_ ] _, then the restriction 𝑓_ |[ _𝑐,𝑑_ ] _is in R_[�] [ _𝑐, 𝑑_ ][�] _._

_5.2. PROPERTIES OF THE INTEGRAL_

193

## **5.2.2 Linearity and monotonicity**

A sum is a linear function of the summands. So is the integral.

**Proposition 5.2.4** (Linearity) **.** _Let 𝑓 and 𝑔 be in R_[�] [ _𝑎, 𝑏_ ][�] _and 𝛼_ ∈ ℝ _._

_(i) 𝛼 𝑓 is in R_[�] [ _𝑎, 𝑏_ ][�] _and_

**==> picture [156 x 32] intentionally omitted <==**

_(ii) 𝑓_ + _𝑔 is in R_[�] [ _𝑎, 𝑏_ ][�] _and_

**==> picture [255 x 32] intentionally omitted <==**

_Proof._ Let us prove the first item for _𝛼_ ≥ 0. Let _𝑃_ be a partition of [ _𝑎, 𝑏_ ], and _𝑚𝑖_ � inf� _𝑓_ ( _𝑥_ ) : _𝑥_ ∈[ _𝑥𝑖_ −1 _, 𝑥𝑖_ ]� as usual. As _𝛼_ ≥ 0, the multiplication by _𝛼_ moves past the infimum,

**==> picture [322 x 16] intentionally omitted <==**

Therefore,

**==> picture [254 x 36] intentionally omitted <==**

Similarly,

**==> picture [113 x 14] intentionally omitted <==**

Again, as _𝛼_ ≥ 0, we may move multiplication by _𝛼_ past the supremum. Hence,

**==> picture [281 x 110] intentionally omitted <==**

Similarly, we show

**==> picture [150 x 32] intentionally omitted <==**

The conclusion now follows for _𝛼_ ≥ 0.

To finish the proof of the first item (for _𝛼<_ 0), we need to show that − _𝑓_ is Riemann _𝑏 𝑏_[The proof of this fact is left as] . integrable and ∫ _𝑎_[−] _[𝑓]_[(] _[𝑥]_[)] _[ 𝑑𝑥]_[=][ −] ∫ _𝑎[𝑓]_[(] _[𝑥]_[)] _[ 𝑑𝑥]_[.] . The proof of the second item is left as It is not difficult, but it is not as □ trivial as it may appear at first glance.

_CHAPTER 5. THE RIEMANN INTEGRAL_

194

The second item in the proposition does not hold with equality for the Darboux integrals, but we do obtain inequalities. The proof of the following proposition is . It follows for upper and lower sums on a fixed partition by , that is, supremum of a sum is less than or equal to the sum of suprema and similarly for infima.