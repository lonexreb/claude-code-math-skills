Example 0.3.8

**Example 0.3.8:** We claim that for all _𝑐_ ≠ 1,

**==> picture [164 x 28] intentionally omitted <==**

Proof: It is easy to check that the equation holds with _𝑛_ = 1. Suppose it is true for _𝑛_ . Then

**==> picture [297 x 109] intentionally omitted <==**

Sometimes, it is easier to use in the inductive step that _𝑃_ ( _𝑘_ ) is true for all _𝑘_ = 1 _,_ 2 _, . . . , 𝑛_ , _𝑘_ = _𝑛_ . not just for This principle is called _strong induction_ and is equivalent to the normal induction above. The proof of that equivalence is left as an exercise.

**Theorem 0.3.9** (Principle of strong induction) **.** _Let 𝑃_ ( _𝑛_ ) _be a statement depending on a natural number 𝑛. Suppose that_

- _(i) (basis statement) 𝑃_ (1) _is true._

_(ii) (induction step) If 𝑃_ ( _𝑘_ ) _is true for all 𝑘_ = 1 _,_ 2 _, . . . , 𝑛, then 𝑃_ ( _𝑛_ + 1) _is true._

_Then 𝑃_ ( _𝑛_ ) _is true for all 𝑛_ ∈ ℕ _._

## **0.3.3 Functions**

Informally, a _set-theoretic function 𝑓_ taking a set _𝐴_ to a set _𝐵_ is a mapping that to each _𝑥_ ∈ _𝐴_ assigns a unique _𝑦_ ∈ _𝐵_ . We write _𝑓_ : _𝐴_ → _𝐵_ . An example function _𝑓_ : _𝑆_ → _𝑇_ taking

_INTRODUCTION_

14

_𝑆_ � {0 _,_ 1 _,_ 2} to _𝑇_ � {0 _,_ 2} can be defined by assigning _𝑓_ (0) � 2, _𝑓_ (1) � 2, and _𝑓_ (2) � 0. That is, a function _𝑓_ : _𝐴_ → _𝐵_ is a black box, into which we stick an element of _𝐴_ and the _𝐵_ . Sometimes is called a or a function spits out an element of _𝑓 mapping map_ , and we say _𝑓 maps 𝐴 to 𝐵_ .

Often, functions are defined by some sort of formula; however, you should really think of a function as just a very large table of values. The subtle issue here is that a single function can have several formulas, all giving the same function. Also, for many functions, there is no formula that expresses its values.

To define a function rigorously, let us first define the Cartesian product.