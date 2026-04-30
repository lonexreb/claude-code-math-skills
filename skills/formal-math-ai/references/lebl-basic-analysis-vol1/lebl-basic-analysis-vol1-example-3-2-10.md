Example 3.2.10

**Example 3.2.10:** The function _𝑓_ : ℝ → ℝ defined by

**==> picture [116 x 39] intentionally omitted <==**

is not continuous at 0.

Proof: Consider {[−][1] / _𝑛_ }[∞] _𝑛_ =1[, which converges to 0.][Then] _[𝑓]_[(][−][1][/] _[𝑛]_[)][ =][ −][1][ for every] _[ 𝑛]_[, and so] lim _𝑛_ →∞ _𝑓_ ([−][1] / _𝑛_ ) = −1, but _𝑓_ (0) = 1. Thus the function is not continuous at 0. See . ∞ Notice that _𝑓_ ([1] / _𝑛_ ) = 1 for all _𝑛_ ∈ ℕ. Hence, lim _𝑛_ →∞ _𝑓_ ([1] / _𝑛_ ) = _𝑓_ (0) = 1. So � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1 may converge to _𝑓_ (0) for some specific sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[going to 0, despite the function] being discontinuous at 0.

Finally, consider _𝑓_ (− _𝑛_ 1) _[𝑛]_ = (−1) _[𝑛]_ . This sequence diverges. � �

_CHAPTER 3. CONTINUOUS FUNCTIONS_

126

**==> picture [109 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1 −21 −31 −41 · · ·<br>**----- End of picture text -----**<br>


**Figure 3.4:** Jump discontinuity. The values of _𝑓_ ([−][1] / _𝑛_ ) and _𝑓_ (0) are marked as black dots.

. **Example 3.2.11:** For an extreme example, take the so-called _Dirichlet function_

**==> picture [150 x 39] intentionally omitted <==**

The function _𝑓_ is discontinuous at all _𝑐_ ∈ ℝ.

Proof: If _𝑐_ is rational, take a sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[of][irrational][numbers][such][that] lim _𝑛_ →∞ _𝑥𝑛_ = _𝑐_ (why can we?). Then _𝑓_ ( _𝑥𝑛_ ) = 0 and so lim _𝑛_ →∞ _𝑓_ ( _𝑥𝑛_ ) = 0, but _𝑓_ ( _𝑐_ ) = 1. If _𝑐_ is irrational, take a sequence of rational numbers { _𝑥𝑛_ }[∞] _𝑛_ =1[that converges to] _[ 𝑐]_[(why can] we?). Then lim _𝑛_ →∞ _𝑓_ ( _𝑥𝑛_ ) = 1, but _𝑓_ ( _𝑐_ ) = 0.

Let us test the limits of our intuition. Can there exist a function continuous at all irrational numbers, but discontinuous at all rational numbers? There are rational numbers arbitrarily close to any irrational number. Perhaps strangely, the answer is yes, such a function exists. The following example is called the _Thomae function_ or the _popcorn function_ .