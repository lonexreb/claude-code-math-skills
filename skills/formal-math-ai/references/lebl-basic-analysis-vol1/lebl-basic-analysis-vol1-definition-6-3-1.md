Definition 6.3.1

**Definition 6.3.1.** Let _𝑈_ ⊂ ℝ[2] be a set, _𝐹_ : _𝑈_ → ℝ a function, and ( _𝑥, 𝑦_ ) ∈ _𝑈_ a point. The ∞ function _𝐹_ is _continuous at_ ( _𝑥, 𝑦_ ) if for every sequence �( _𝑥𝑛 , 𝑦𝑛_ )� _𝑛_ =1[of points in] _[ 𝑈]_[such that] lim _𝑛_ →∞ _𝑥𝑛_ = _𝑥_ and lim _𝑛_ →∞ _𝑦𝑛_ = _𝑦_ , we have

**==> picture [126 x 18] intentionally omitted <==**

We say _𝐹_ is _continuous_ if it is continuous at all points in _𝑈_ .

**Theorem 6.3.2** (Picard’s theorem on existence and uniqueness) **.** _Let 𝐼, 𝐽_ ⊂ ℝ _be closed bounded intervals, let 𝐼_[◦] _and 𝐽_[◦] _be their interiors , and let_ ( _𝑥_ 0 _, 𝑦_ 0) ∈ _𝐼_[◦] × _𝐽_[◦] _. Suppose 𝐹_ : _𝐼_ × _𝐽_ → ℝ _is continuous and Lipschitz in the second variable, that is, there exists an 𝐿_ ∈ ℝ _such that_

**==> picture [276 x 16] intentionally omitted <==**

_Then there exists an ℎ >_ 0 _such that_ [ _𝑥_ 0 − _ℎ, 𝑥_ 0 + _ℎ_ ] ⊂ _𝐼 and a unique differentiable function 𝑓_ : [ _𝑥_ 0 − _ℎ, 𝑥_ 0 + _ℎ_ ] → _𝐽_ ⊂ ℝ _such that_

**==> picture [342 x 15] intentionally omitted <==**

. _Proof._ Suppose we could find a solution _𝑓_ Using the fundamental theorem of calculus we integrate the equation _𝑓_[′] ( _𝑥_ ) = _𝐹_[�] _𝑥, 𝑓_ ( _𝑥_ )[�] , _𝑓_ ( _𝑥_ 0) = _𝑦_ 0, and write ( ) as the integral equation

**==> picture [309 x 31] intentionally omitted <==**

The idea of our proof is that we try to plug in approximations to a solution to the right-hand side of ( ) to get better approximations on the left-hand side of ( ). We hope that in the end the sequence converges and solves ( ) and hence ( ). The technique below is called _Picard iteration_ , and the individual functions _𝑓𝑘_ are called the _Picard iterates_ .

Without loss of generality, suppose _𝑥_ 0 = 0 (exercise below). Another exercise tells us that _𝐹_ is bounded as it is continuous. Therefore pick some _𝑀 >_ 0 so that �� _𝐹_ ( _𝑥, 𝑦_ )�� ≤ _𝑀_ for all ( _𝑥, 𝑦_ ) ∈ _𝐼_ × _𝐽_ . Pick _𝛼>_ 0 such that [− _𝛼, 𝛼_ ] ⊂ _𝐼_ and [ _𝑦_ 0 − _𝛼, 𝑦_ 0 + _𝛼_ ] ⊂ _𝐽_ . Define

**==> picture [122 x 24] intentionally omitted <==**

Observe [− _ℎ, ℎ_ ] ⊂ _𝐼_ .

Set _𝑓_ 0( _𝑥_ ) � _𝑦_ 0. We define _𝑓𝑘_ inductively. Assuming _𝑓𝑘_ −1([− _ℎ, ℎ_ ]) ⊂[ _𝑦_ 0 − _𝛼, 𝑦_ 0 + _𝛼_ ], we see _𝐹_[�] _𝑡, 𝑓𝑘_ −1( _𝑡_ )[�] is a well-defined function of _𝑡_ for _𝑡_ ∈[− _ℎ, ℎ_ ]. Further if _𝑓𝑘_ −1 is continuous

‗ By interior of [ _𝑎, 𝑏_ ], we mean ( _𝑎, 𝑏_ ).

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

248

on [− _ℎ, ℎ_ ], then _𝐹_[�] _𝑡, 𝑓𝑘_ −1( _𝑡_ )[�] is continuous as a function of _𝑡_ on [− _ℎ, ℎ_ ] (left as an exercise). Define

**==> picture [168 x 30] intentionally omitted <==**

and _𝑓𝑘_ is continuous on [− _ℎ, ℎ_ ] by the fundamental theorem of calculus. To see that _𝑓𝑘_ maps [− _ℎ, ℎ_ ] to [ _𝑦_ 0 − _𝛼, 𝑦_ 0 + _𝛼_ ], we compute for _𝑥_ ∈[− _ℎ, ℎ_ ]

**==> picture [351 x 32] intentionally omitted <==**

We next define _𝑓𝑘_ +1 using _𝑓𝑘_ and so on. Thus we have inductively defined a sequence { _𝑓𝑘_ }[∞] _𝑘_ =1[of][functions.][We][need][to][show][that][it][converges][to][a][function] _[𝑓]_[that][solves][the] equation ( ) and therefore ( ).

We wish to show that the sequence { _𝑓𝑘_ }[∞] _𝑘_ =1[converges uniformly to some function on] [− _ℎ, ℎ_ ]. First, for _𝑡_ ∈[− _ℎ, ℎ_ ], we have the following useful bound

**==> picture [316 x 18] intentionally omitted <==**

where �� _𝑓𝑛_ − _𝑓𝑘_ ��[− _ℎ,ℎ_ ][is][the][uniform][norm,][that][is][the][supremum][of] �� _𝑓𝑛_ ( _𝑡_ ) − _𝑓𝑘_ ( _𝑡_ )�� for _𝑡_ ∈[− _ℎ, ℎ_ ]. Now note that | _𝑥_ | ≤ _ℎ_ ≤ _𝑀_ + _𝛼𝐿𝛼_[.][Therefore]

**==> picture [300 x 116] intentionally omitted <==**

Let _𝐶_ � _𝐿𝛼_[Taking supremum on the left-hand side we get] _𝑀_ + _𝐿𝛼_[and note that] _[ 𝐶][<]_[ 1.]

**==> picture [196 x 19] intentionally omitted <==**

Without loss of generality, suppose _𝑛_ ≥ _𝑘_ . Then by we can show

**==> picture [192 x 19] intentionally omitted <==**

For _𝑥_ ∈[− _ℎ, ℎ_ ], we have

**==> picture [191 x 17] intentionally omitted <==**

Therefore,

**==> picture [226 x 19] intentionally omitted <==**

As _𝐶 <_ 1, { _𝑓𝑛_ }[∞] _𝑛_ =1[is uniformly Cauchy and by] we obtain that { _𝑓𝑛_ }[∞] _𝑛_ =1 converges uniformly on [− _ℎ, ℎ_ ] to some function _𝑓_ : [− _ℎ, ℎ_ ] → ℝ. The function _𝑓_ is the

_6.3. PICARD’S THEOREM_

249

uniform limit of continuous functions and therefore continuous. Furthermore, since _𝑓𝑛_ �[− _ℎ, ℎ_ ][�] ⊂[ _𝑦_ 0 − _𝛼, 𝑦_ 0 + _𝛼_ ] for all _𝑛_ , then _𝑓_[�] [− _ℎ, ℎ_ ][�] ⊂[ _𝑦_ 0 − _𝛼, 𝑦_ 0 + _𝛼_ ] (why?). We now need to show that _𝑓_ solves ( ). First, as before we notice

**==> picture [306 x 19] intentionally omitted <==**

As �� _𝑓𝑛_ − _𝑓_ ��[− _ℎ,ℎ_ ][converges][to][0,][then] _[𝐹]_[�] _𝑡, 𝑓𝑛_ ( _𝑡_ )[�] converges uniformly to _𝐹_[�] _𝑡, 𝑓_ ( _𝑡_ )[�] for _𝑡_ ∈[− _ℎ, ℎ_ ]. Hence, for _𝑥_ ∈[− _ℎ, ℎ_ ] the convergence is uniform for _𝑡_ ∈[0 _, 𝑥_ ] (or [ _𝑥,_ 0] if _𝑥 <_ 0). Therefore,

**==> picture [427 x 120] intentionally omitted <==**

We apply the fundamental theorem of calculus ( ) to show that _𝑓_ is differentiable and its derivative is _𝐹_[�] _𝑥, 𝑓_ ( _𝑥_ )[�] . It is obvious that _𝑓_ (0) = _𝑦_ 0. Finally, what is left to do is to show uniqueness. Suppose _𝑔_ : [− _ℎ, ℎ_ ] → _𝐽_ ⊂ ℝ is another solution. As before we use the fact that �� _𝐹_ � _𝑡, 𝑓_ ( _𝑡_ )[�] − _𝐹_[�] _𝑡, 𝑔_ ( _𝑡_ )[���] ≤ _𝐿_ �� _𝑓_ − _𝑔_ ��[− _ℎ,ℎ_ ][.][Then]

**==> picture [398 x 95] intentionally omitted <==**

As before, _𝐶_ = _𝑀𝐿_ + _𝛼𝐿𝛼[<]_[1][.][By taking supremum over] _[ 𝑥]_[∈[−] _[ℎ, ℎ]_[]][ on the left-hand side we] obtain

**==> picture [469 x 43] intentionally omitted <==**

## **6.3.3 Examples**

Let us look at some examples. The proof of the theorem gives us an explicit way to find an _ℎ_ that works. It does not, however, give us the best _ℎ_ . It is often possible to find a much larger _ℎ_ for which the conclusion of the theorem holds.

The proof also gives us the Picard iterates as approximations to the solution. So the proof actually tells us how to obtain the solution, not just that the solution exists.

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

250

## **Example 6.3.3:** Consider

**==> picture [137 x 13] intentionally omitted <==**

That is, we suppose _𝐹_ ( _𝑥, 𝑦_ ) = _𝑦_ , and we are looking for a function _𝑓_ such that _𝑓_[′] ( _𝑥_ ) = _𝑓_ ( _𝑥_ ). Let us forget for the moment that we solved this equation in . See also for a plot of both the equation, showing the slope _𝐹_ ( _𝑥, 𝑦_ ) = _𝑦_ at each point, and the solution, the exponential, that satisfies _𝑓_ (0) = 1.

We pick any _𝐼_ that contains 0 in the interior. We pick an arbitrary _𝐽_ that contains 1 in its interior. We can use _𝐿_ = 1. The theorem guarantees an _ℎ >_ 0 such that there exists a unique solution _𝑓_ : [− _ℎ, ℎ_ ] → ℝ. This solution is usually denoted by

**==> picture [56 x 14] intentionally omitted <==**

We leave it to the reader to verify that by picking _𝐼_ and _𝐽_ large enough the proof of the _𝛼 ℎ_ theorem guarantees that we are able to pick such that we get any we want as long as _ℎ <_[1] /2. We omit the calculation. Of course, we know this function exists as a function for all _𝑥_ , so an arbitrary _ℎ_ ought to work, but the theorem only provides _ℎ <_[1] /2.

By same reasoning as above, no matter what _𝑥_ 0 and _𝑦_ 0 are, the proof guarantees an arbitrary _ℎ_ as long as _ℎ <_[1] /2. Fix such an _ℎ_ . We get a unique function defined on [ _𝑥_ 0 − _ℎ, 𝑥_ 0 + _ℎ_ ]. After defining the function on [− _ℎ, ℎ_ ] we find a solution on the interval [0 _,_ 2 _ℎ_ ] and notice that the two functions must coincide on [0 _, ℎ_ ] by uniqueness. We thus iteratively construct the exponential for all _𝑥_ ∈ ℝ. Therefore, Picard’s theorem could be used to prove the existence and uniqueness of the exponential.

Let us compute the Picard iterates. We start with the constant function _𝑓_ 0( _𝑥_ ) � 1. Then

**==> picture [354 x 99] intentionally omitted <==**

We recognize the beginning of the Taylor series for the exponential. See . **Example 6.3.4:** Consider the equation

**==> picture [190 x 17] intentionally omitted <==**

From elementary differential equations we know

**==> picture [65 x 26] intentionally omitted <==**

is the solution. The solution is only defined on (−∞ _,_ 1). That is, we are able to use _ℎ <_ 1, but never a larger _ℎ_ . The function that takes _𝑦_ to _𝑦_[2] is not Lipschitz as a function on all

_6.3. PICARD’S THEOREM_

251

**==> picture [218 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>3<br>2<br>1<br>−1 0 1<br>**----- End of picture text -----**<br>


**Figure 6.9:** The exponential (solid line) together with _𝑓_ 0, _𝑓_ 1, _𝑓_ 2, _𝑓_ 3 (dashed).

of ℝ. As we approach _𝑥_ = 1 from the left, the solution becomes larger and larger. The derivative of the solution grows as _𝑦_[2] , and so the _𝐿_ required has to be larger and larger as 1 _𝑦_ 0 grows. If we apply the theorem with _𝑥_ 0 close to 1 and _𝑦_ 0 = 1− _𝑥_ 0[we find that the] _[ℎ]_[that] the proof guarantees is smaller and smaller as _𝑥_ 0 approaches 1.

The _ℎ_ from the roof is not the best _ℎ_ . _𝛼_ p By picking correctly, the proof of the theorem guarantees _ℎ_ = 1 − √3/2 ≈ 0 _._ 134 (we omit the calculation) for _𝑥_ 0 = 0 and _𝑦_ 0 = 1, even though we saw above that any _ℎ <_ 1 should work.