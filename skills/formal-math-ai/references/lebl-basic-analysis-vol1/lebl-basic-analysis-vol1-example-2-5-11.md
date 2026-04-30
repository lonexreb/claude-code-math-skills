Example 2.5.11

**Example 2.5.11:** The series[�][∞] _𝑛_ =1[1][/] _[𝑛]_[diverges (despite the fact that][ lim] _[𝑛]_[→∞][1][/] _[𝑛]_[=][ 0][).][This is] the famous _harmonic series_ .

Proof: We will show that the sequence of partial sums is unbounded, and hence cannot converge. Write the partial sums _𝑠𝑛_ for _𝑛_ = 2 _[𝑘]_ as:

**==> picture [236 x 189] intentionally omitted <==**

Notice[1] /3 +[1] /4 ≥[1] /4 +[1] /4 =[1] /2 and[1] /5 +[1] /6 +[1] /7 +[1] /8 ≥[1] /8 +[1] /8 +[1] /8 +[1] /8 =[1] /2. More generally

**==> picture [210 x 41] intentionally omitted <==**

‗The divergence of the harmonic series was known long before the theory of series was made rigorous. The proof we give is the earliest proof and was given by (1323?–1382).

_2.5. SERIES_

91

Therefore,

**==> picture [240 x 45] intentionally omitted <==**

As { _[𝑘]_ /2}[∞] _𝑘_ =1[is unbounded by the] , that means that { _𝑠_ 2 _𝑘_ }[∞] _𝑘_ =1[is un-] bounded, and therefore { _𝑠𝑛_ }[∞] _𝑛_ =1[is unbounded.][Hence][ {] _[𝑠][𝑛]_[}][∞] _𝑛_ =1[diverges, and consequently] �∞ _𝑛_ =1[1][/] _[𝑛]_[diverges.]

Like finite sums, convergent series behave linearly. That is, we can multiply them by constants and add them and these operations are done term by term.

**Proposition 2.5.12** (Linearity of series) **.** _Let 𝛼_ ∈ ℝ _and_[�][∞] _𝑛_ =1 _[𝑥][𝑛][and]_[ �][∞] _𝑛_ =1 _[𝑦][𝑛][be convergent] series. Then_

- _(i)_[�][∞] _𝑛_ =1 _[𝛼][𝑥][𝑛][is a convergent series and]_

**==> picture [99 x 35] intentionally omitted <==**

- _(ii)_[�][∞] _𝑛_ =1[(] _[𝑥][𝑛]_[+] _[ 𝑦][𝑛]_[)] _[ is a convergent series and]_

**==> picture [185 x 38] intentionally omitted <==**

_Proof._ For the first item, we simply write the _𝑘_ th partial sum

**==> picture [114 x 39] intentionally omitted <==**

We look at the right-hand side and note that the constant multiple of a convergent sequence is convergent. Hence, we take the limit of both sides to obtain the result.

For the second item we also look at the _𝑘_ th partial sum

**==> picture [184 x 39] intentionally omitted <==**

We look at the right-hand side and note that the sum of convergent sequences is convergent. Hence, we take the limit of both sides to obtain the proposition. □

An example of a useful application of the first item is the following formula. If | _𝑟_ | _<_ 1 and _𝑖_ ∈ ℕ, then

**==> picture [76 x 35] intentionally omitted <==**

_CHAPTER 2. SEQUENCES AND SERIES_

92

The formula follows by using the geometric series and multiplying by _𝑟[𝑖]_ :

**==> picture [144 x 35] intentionally omitted <==**

Multiplying series is not as simple as adding, see the next section. It is not true, of course, that we multiply term by term. That strategy does not work even for finite sums: ( _𝑎_ + _𝑏_ )( _𝑐_ + _𝑑_ ) ≠ _𝑎𝑐_ + _𝑏𝑑_ .

## **2.5.4 Absolute convergence**

As monotone sequences are easier to work with than arbitrary sequences, it is usually easier to work with series[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[, where] _[ 𝑥][𝑛]_[≥][0][ for all] _[ 𝑛]_[.][The sequence of partial sums] is then monotone increasing and converges if it is bounded above. Let us formalize this statement as a proposition.