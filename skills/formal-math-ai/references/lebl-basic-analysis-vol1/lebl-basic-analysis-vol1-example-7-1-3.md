Example 7.1.3

**Example 7.1.3:** We can also put a different metric on the set of real numbers. For example, take the set of real numbers ℝ together with the metric

**==> picture [112 x 37] intentionally omitted <==**

Items – are again easy to verify. The triangle inequality is a little bit more difficult. Note that _𝑑_ ( _𝑥, 𝑦_ ) = _𝜑_ (�� _𝑥_ − _𝑦_ ��) where _𝜑_ ( _𝑡_ ) = _𝑡_ + _𝑡_ 1[and] _[ 𝜑]_[is an increasing function (positive]

_7.1. METRIC SPACES_

257

derivative, see ). Hence

**==> picture [338 x 153] intentionally omitted <==**

The function _𝑑_ is thus a metric, and gives an example of a nonstandard metric on ℝ. With this metric, _𝑑_ ( _𝑥, 𝑦_ ) _<_ 1 for all _𝑥, 𝑦_ ∈ ℝ. That is, every two points are less than 1 unit apart.

**==> picture [436 x 76] intentionally omitted <==**

**Figure 7.2:** Graph of _𝑡_ + _𝑡_ 1[for positive] _[ 𝑡]_[with an asymptote at 1.]

An important metric space is the _𝑛_ -dimensional _euclidean space_ ℝ _[𝑛]_ = ℝ × ℝ × · · · × ℝ. � We use the following notation for points: _𝑥_ = ( _𝑥_ 1 _, 𝑥_ 2 _, . . . , 𝑥𝑛_ ) ∈ ℝ _[𝑛]_ . We will not write _𝑥_ nor **x** ℝ _[𝑛]_ for a point in as is common in multivariable calculus, we simply give it a name such as _𝑥_ and we will remember that _𝑥_ is an element of ℝ _[𝑛]_ . We also write simply 0 ∈ ℝ _[𝑛]_ to mean the point (0 _,_ 0 _, . . . ,_ 0). Before making ℝ _[𝑛]_ a metric space, we prove an important inequality, the so-called Cauchy–Schwarz inequality.

**Lemma 7.1.4** (Cauchy–Schwarz inequality ) **.** _Suppose 𝑥_ = ( _𝑥_ 1 _, 𝑥_ 2 _, . . . , 𝑥𝑛_ ) ∈ ℝ _[𝑛] , 𝑦_ = ( _𝑦_ 1 _, 𝑦_ 2 _, . . . , 𝑦𝑛_ ) ∈ ℝ _[𝑛] . Then_

**==> picture [163 x 39] intentionally omitted <==**

‗Sometimes it is called the Cauchy–Bunyakovsky–Schwarz inequality. (1843–1921) was a German mathematician and (1804–1889) was a Ukrainian mathematician. What we stated should really be called the Cauchy inequality, as Bunyakovsky and Schwarz provided proofs for infinite-dimensional versions.

_CHAPTER 7. METRIC SPACES_

258

_Proof._ A square of a real number is nonnegative. Hence a sum of squares is nonnegative:

**==> picture [401 x 186] intentionally omitted <==**

We relabel and divide by 2 to obtain precisely what we wanted,