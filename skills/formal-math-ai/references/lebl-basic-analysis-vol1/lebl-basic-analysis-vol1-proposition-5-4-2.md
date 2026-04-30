Proposition 5.4.2

**Proposition 5.4.2.** _There exists a unique function 𝐸_ : ℝ →(0 _,_ ∞) _such that_

- _(i) 𝐸_ (0) = 1 _._

- _(ii) 𝐸 is differentiable and 𝐸_[′] ( _𝑥_ ) = _𝐸_ ( _𝑥_ ) _._

- _(iii) 𝐸 is strictly increasing, bĳective, and_

**==> picture [223 x 17] intentionally omitted <==**

- _(iv) 𝐸_ ( _𝑥_ + _𝑦_ ) = _𝐸_ ( _𝑥_ ) _𝐸_ ( _𝑦_ ) _for all 𝑥, 𝑦_ ∈ ℝ _._

- _(v) If 𝑞_ ∈ ℚ _, then 𝐸_ ( _𝑞𝑥_ ) = _𝐸_ ( _𝑥_ ) _[𝑞] ._

_Proof._ Again, we prove existence of such a function by defining a candidate and proving that it satisfies all the properties. The _𝐿_ = ln defined above is invertible. Let _𝐸_ be the inverse function of _𝐿_ . Property is immediate.

: Property follows via the inverse function theorem, in particular via _𝐿_ satisfies all the hypotheses of the lemma, and hence

**==> picture [128 x 31] intentionally omitted <==**

Let us look at property . The function _𝐸_ is strictly increasing since _𝐸_[′] ( _𝑥_ ) = _𝐸_ ( _𝑥_ ) _>_ 0. As _𝐸_ is the inverse of _𝐿_ , it must also be bĳective. To find the limits, we use that _𝐸_ is strictly increasing and onto (0 _,_ ∞). For every _𝑀 >_ 0, there is an _𝑥_ 0 such that _𝐸_ ( _𝑥_ 0) = _𝑀_ and _𝐸_ ( _𝑥_ ) ≥ _𝑀_ for all _𝑥_ ≥ _𝑥_ 0. Similarly, for every _𝜖>_ 0, there is an _𝑥_ 0 such that _𝐸_ ( _𝑥_ 0) = _𝜖_ and _𝐸_ ( _𝑥_ ) _< 𝜖_ for all _𝑥 < 𝑥_ 0. Therefore,

**==> picture [226 x 17] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

210

To prove property , we use the corresponding property for the logarithm. Take _𝑥, 𝑦_ ∈ ℝ. As _𝐿_ is bĳective, find _𝑎_ and _𝑏_ such that _𝑥_ = _𝐿_ ( _𝑎_ ) and _𝑦_ = _𝐿_ ( _𝑏_ ). Then

**==> picture [284 x 15] intentionally omitted <==**

Property also follows from the corresponding property of _𝐿_ . Given _𝑥_ ∈ ℝ, let _𝑎_ be such that _𝑥_ = _𝐿_ ( _𝑎_ ) and

**==> picture [222 x 15] intentionally omitted <==**

Uniqueness follows from and . Let _𝐸_ and _𝐹_ be two functions satisfying and .

**==> picture [381 x 26] intentionally omitted <==**

Therefore, by , _𝐹_ ( _𝑥_ ) _𝐸_ (− _𝑥_ ) = _𝐹_ (0) _𝐸_ (−0) = 1 for all _𝑥_ ∈ ℝ. Next, 1 = _𝐸_ (0) = _𝐸_ ( _𝑥_ − _𝑥_ ) = _𝐸_ ( _𝑥_ ) _𝐸_ (− _𝑥_ ). Then

0 = 1 − 1 = _𝐹_ ( _𝑥_ ) _𝐸_ (− _𝑥_ ) − _𝐸_ ( _𝑥_ ) _𝐸_ (− _𝑥_ ) =[�] _𝐹_ ( _𝑥_ ) − _𝐸_ ( _𝑥_ )[�] _𝐸_ (− _𝑥_ ) _._ Finally, _𝐸_ (− _𝑥_ ) ≠ 0 for all _𝑥_ ∈ ℝ. So _𝐹_ ( _𝑥_ ) − _𝐸_ ( _𝑥_ ) = 0 for all _𝑥_ , and we are done. Having proved _𝐸_ is unique, we define the _exponential_ function (see ) as

**==> picture [9 x 7] intentionally omitted <==**

**==> picture [80 x 13] intentionally omitted <==**

**==> picture [218 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>3<br>2<br>1<br>−1 0 1<br>**----- End of picture text -----**<br>


**Figure 5.7:** Plot of _𝑒[𝑥]_ , together with a slope field giving slope _𝑦_ at every point ( _𝑥, 𝑦_ ). The equation _𝑑𝑥[𝑑][𝑒][𝑥]_[=] _[𝑒][𝑥]_[means that] _[𝑦]_[=] _[𝑒][𝑥]_[follows these slopes.]

> ‗ _𝐸_ is a function into (0 _,_ ∞) after all. However, _𝐸_ (− _𝑥_ ) ≠ 0 also follows from _𝐸_ ( _𝑥_ ) _𝐸_ (− _𝑥_ ) = 1. Therefore, we can prove uniqueness of _𝐸_ given and , even for functions _𝐸_ : ℝ → ℝ.

_5.4. THE LOGARITHM AND THE EXPONENTIAL_

211

If _𝑦_ ∈ ℚ and _𝑥 >_ 0, then

**==> picture [170 x 15] intentionally omitted <==**

We can now make sense of exponentiation _𝑥[𝑦]_ for arbitrary _𝑦_ ∈ ℝ; if _𝑥 >_ 0 and _𝑦_ is irrational, define

**==> picture [98 x 15] intentionally omitted <==**

As exp is continuous, then _𝑥[𝑦]_ is a continuous function of _𝑦_ . Therefore, we would obtain the same result had we taken a sequence of rational numbers { _𝑦𝑛_ }[∞] _𝑛_ =1[approaching] _[ 𝑦]_[and] defined _𝑥[𝑦]_ = lim _𝑛_ →∞ _𝑥[𝑦][𝑛]_ .

Define the number _𝑒_ , called _Euler’s number_ or the _base of the natural logarithm_ , as

**==> picture [61 x 13] intentionally omitted <==**

Let us justify the notation _𝑒[𝑥]_ for exp( _𝑥_ ):

**==> picture [142 x 15] intentionally omitted <==**

The properties of the logarithm and the exponential extend to irrational powers. The proof is immediate.