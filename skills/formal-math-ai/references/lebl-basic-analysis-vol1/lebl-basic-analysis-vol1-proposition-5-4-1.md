Proposition 5.4.1

**Proposition 5.4.1.** _There exists a unique function 𝐿_ : (0 _,_ ∞) → ℝ _such that_

- _(i) 𝐿_ (1) = 0 _._

- _(ii) 𝐿 is differentiable and 𝐿_[′] ( _𝑥_ ) =[1] / _𝑥._

- _(iii) 𝐿 is strictly increasing, bĳective, and_

**==> picture [225 x 18] intentionally omitted <==**

- _(iv) 𝐿_ ( _𝑥𝑦_ ) = _𝐿_ ( _𝑥_ ) + _𝐿_ ( _𝑦_ ) _for all 𝑥, 𝑦_ ∈(0 _,_ ∞) _._

- _(v) If 𝑞 is a rational number and 𝑥 >_ 0 _, then 𝐿_ ( _𝑥[𝑞]_ ) = _𝑞𝐿_ ( _𝑥_ ) _._

_Proof._ To prove existence, we define a candidate and show it satisfies all the properties. Let

**==> picture [88 x 30] intentionally omitted <==**

Obviously, holds. Property holds via the second form of the fundamental theorem of calculus ( ).

To prove property , we change variables _𝑢_ = _𝑦𝑡_ to obtain

**==> picture [362 x 33] intentionally omitted <==**

_CHAPTER 5. THE RIEMANN INTEGRAL_

208

Let us prove . Property together with the fact that _𝐿_[′] ( _𝑥_ ) =[1] / _𝑥 >_ 0 for _𝑥 >_ 0, implies that _𝐿_ is strictly increasing and hence one-to-one. Let us show _𝐿_ is onto. As[1] / _𝑡_ ≥[1] /2 when _𝑡_ ∈[1 _,_ 2],

**==> picture [111 x 32] intentionally omitted <==**

By induction, implies that for _𝑛_ ∈ ℕ,

**==> picture [206 x 12] intentionally omitted <==**

Given _𝑦 >_ 0, by the of the real numbers (notice _𝐿_ (2) _>_ 0), there is an _𝑛_ ∈ ℕ such that _𝐿_ (2 _[𝑛]_ ) _> 𝑦_ . The gives an _𝑥_ 1 ∈(1 _,_ 2 _[𝑛]_ ) such that _𝐿_ ( _𝑥_ 1) = _𝑦_ . Thus (0 _,_ ∞) is in the image of _𝐿_ . As _𝐿_ is increasing, _𝐿_ ( _𝑥_ ) _> 𝑦_ for all _𝑥 >_ 2 _[𝑛]_ , and so

**==> picture [76 x 18] intentionally omitted <==**

Next 0 = _𝐿_ ( _[𝑥]_ / _𝑥_ ) = _𝐿_ ( _𝑥_ ) + _𝐿_ ([1] / _𝑥_ ), and so _𝐿_ ( _𝑥_ ) = − _𝐿_ ([1] / _𝑥_ ). Using _𝑥_ = 2[−] _[𝑛]_ , we obtain as above that _𝐿_ achieves all negative numbers. And

**==> picture [222 x 18] intentionally omitted <==**

In the limits, note that only _𝑥 >_ 0 are in the domain of _𝐿_ .

Let us prove . Fix _𝑥 >_ 0. As above, implies _𝐿_ ( _𝑥[𝑛]_ ) = _𝑛𝐿_ ( _𝑥_ ) for all _𝑛_ ∈ ℕ. We already found that _𝐿_ ( _𝑥_ ) = − _𝐿_ ([1] / _𝑥_ ), so _𝐿_ ( _𝑥_[−] _[𝑛]_ ) = − _𝐿_ ( _𝑥[𝑛]_ ) = − _𝑛𝐿_ ( _𝑥_ ). Then for _𝑚_ ∈ ℕ

**==> picture [164 x 24] intentionally omitted <==**

Putting everything together for _𝑛_ ∈ ℤ and _𝑚_ ∈ ℕ, we have _𝐿_ ( _𝑥[𝑛]_[/] _[𝑚]_ ) = _𝑛𝐿_ ( _𝑥_[1][/] _[𝑚]_ ) = ( _[𝑛]_ / _𝑚_ ) _𝐿_ ( _𝑥_ ). Uniqueness follows using properties and . Via the first form of the fundamental theorem of calculus ( ),

**==> picture [275 x 53] intentionally omitted <==**

is the unique function such that _𝐿_ (1) = 0 and _𝐿_[′] ( _𝑥_ ) =[1] / _𝑥_ .

Having proved that there is a unique function with these properties, we simply define the _logarithm_ or sometimes called the _natural logarithm_ :

**==> picture [70 x 12] intentionally omitted <==**

See . Mathematicians usually write log( _𝑥_ ) instead of ln( _𝑥_ ), which is more familiar to calculus students. For all practical purposes, there is only one logarithm: the natural logarithm. See .

_5.4. THE LOGARITHM AND THE EXPONENTIAL_

209

**==> picture [219 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
2<br>푦 = [1] / 푥<br>1<br>shaded area = ln(4)<br>0<br>1 2 3 4 5<br>−1 푦 = ln( 푥 )<br>−2<br>**----- End of picture text -----**<br>


**Figure 5.6:** Plot of ln( _𝑥_ ) together with[1] / _𝑥_ , showing the value ln(4).

## **5.4.2 The exponential**

Just as with the logarithm we define the exponential via a list of properties.