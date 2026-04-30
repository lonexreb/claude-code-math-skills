Lemma 4.2.2

**Lemma 4.2.2.** _Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _is differentiable at 𝑐_ ∈( _𝑎, 𝑏_ ) _, and 𝑓 has a relative minimum or a relative maximum at 𝑐. Then 𝑓_[′] ( _𝑐_ ) = 0 _._

_Proof._ Suppose _𝑐_ is a relative maximum of _𝑓_ . That is, there is a _𝛿>_ 0 such that for every _𝑥_ ∈( _𝑎, 𝑏_ ) where | _𝑥_ − _𝑐_ | _< 𝛿_ , we have _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑐_ ) ≤ 0. Consider the difference quotient. If _𝑐 < 𝑥 < 𝑐_ + _𝛿_ , then

**==> picture [85 x 28] intentionally omitted <==**

and if _𝑐_ − _𝛿< 𝑦 < 𝑐_ , then

**==> picture [85 x 30] intentionally omitted <==**

See for an illustration.

**==> picture [293 x 123] intentionally omitted <==**

**----- Start of picture text -----**<br>
slope = [푓] [(] [푦] 푦 [)−] − 푐 [푓] [(] [푐] [)] ≥ 0 slope = [푓] [(] [푥] 푥 [)−] − 푐 [푓] [(] [푐] [)] ≤ 0<br>푦 푐 푥<br>**----- End of picture text -----**<br>


**Figure 4.3:** Slopes of secants at a relative maximum.

As _𝑎 < 𝑐 < 𝑏_ , there exist sequences { _𝑥𝑛_ }[∞] _𝑛_ =1[and][ {] _[𝑦][𝑛]_[}][∞] _𝑛_ =1[in][ (] _[𝑎, 𝑏]_[)][ such that] _[ 𝑐][<][𝑥][𝑛][<][𝑐]_[+] _[𝛿]_ and _𝑐_ − _𝛿< 𝑦𝑛 < 𝑐_ for all _𝑛_ ∈ ℕ, and such that lim _𝑛_ →∞ _𝑥𝑛_ = lim _𝑛_ →∞ _𝑦𝑛_ = _𝑐_ . Since _𝑓_ is

_4.2. MEAN VALUE THEOREM_

163

differentiable at _𝑐_ ,

**==> picture [469 x 54] intentionally omitted <==**

For a differentiable function, a point where _𝑓_[′] ( _𝑐_ ) = 0 is called a _critical point_ . When _𝑓_ is not differentiable at some points, it is common to also say that _𝑐_ is a critical point if _𝑓_[′] ( _𝑐_ ) does not exist. The theorem says that a relative minimum or maximum at an interior point of an interval must be a critical point. As you remember from calculus, one finds minima and maxima of a function by finding all the critical points together with the endpoints of the interval and simply checking at which of these points is the function biggest or smallest.

## **4.2.2 Rolle’s theorem**

Suppose a function has the same value at both endpoints of an interval. Intuitively, it ought to attain a minimum or a maximum in the interior of the interval, then at such a minimum or a maximum, the derivative should be zero. See for the geometric idea. This is the content of the so-called Rolle’s theorem .

**==> picture [222 x 147] intentionally omitted <==**

**----- Start of picture text -----**<br>
푏<br>푎 푐<br>**----- End of picture text -----**<br>


**Figure 4.4:** Point where the tangent line is horizontal, that is _𝑓_[′] ( _𝑐_ ) = 0.

**Theorem 4.2.3** (Rolle) **.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function differentiable on_ ( _𝑎, 𝑏_ ) _such that 𝑓_ ( _𝑎_ ) = _𝑓_ ( _𝑏_ ) _. Then there exists a 𝑐_ ∈( _𝑎, 𝑏_ ) _such that 𝑓_[′] ( _𝑐_ ) = 0 _._

_Proof._ As _𝑓_ is continuous on [ _𝑎, 𝑏_ ], it attains an absolute minimum and an absolute maximum in [ _𝑎, 𝑏_ ]. We wish to apply , and so we need to find some _𝑐_ ∈( _𝑎, 𝑏_ ) where _𝑓_ attains a minimum or a maximum. Write _𝐾_ � _𝑓_ ( _𝑎_ ) = _𝑓_ ( _𝑏_ ). If there exists an _𝑥_ such that _𝑓_ ( _𝑥_ ) _> 𝐾_ , then the absolute maximum is larger than _𝐾_ and hence occurs at some _𝑐_ ∈( _𝑎, 𝑏_ ), and therefore _𝑓_[′] ( _𝑐_ ) = 0. On the other hand, if there exists an _𝑥_ such that

> ‗Named after the French mathematician (1652–1719).

_CHAPTER 4. THE DERIVATIVE_

164

_𝑓_ ( _𝑥_ ) _< 𝐾_ , then the absolute minimum occurs at some _𝑐_ ∈( _𝑎, 𝑏_ ), and so _𝑓_[′] ( _𝑐_ ) = 0. If there is no _𝑥_ such that _𝑓_ ( _𝑥_ ) _> 𝐾_ or _𝑓_ ( _𝑥_ ) _< 𝐾_ , then _𝑓_ ( _𝑥_ ) = _𝐾_ for all _𝑥_ and then _𝑓_[′] ( _𝑥_ ) = 0 for all _𝑥_ ∈[ _𝑎, 𝑏_ ], so any _𝑐_ ∈( _𝑎, 𝑏_ ) works. □

It is absolutely necessary that the derivative exists for all _𝑥_ ∈( _𝑎, 𝑏_ ). Consider the function _𝑓_ ( _𝑥_ ) � | _𝑥_ | on [−1 _,_ 1]. Clearly _𝑓_ (−1) = _𝑓_ (1), but there is no point _𝑐_ where _𝑓_[′] ( _𝑐_ ) = 0.

## **4.2.3 Mean value theorem**

We extend to functions that attain different values at the endpoints. **Theorem 4.2.4** (Mean value theorem) **.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _be a continuous function differentiable on_ ( _𝑎, 𝑏_ ) _. Then there exists a point 𝑐_ ∈( _𝑎, 𝑏_ ) _such that_

**==> picture [133 x 13] intentionally omitted <==**

For a geometric interpretation of the mean value theorem, see . The idea is that the value _[𝑓]_[(] _[𝑏] 𝑏_[)][−] − _𝑎[𝑓]_[(] _[𝑎]_[)] is the slope of the line between the points[�] _𝑎, 𝑓_ ( _𝑎_ )[�] and[�] _𝑏, 𝑓_ ( _𝑏_ )[�] . Then _𝑐_ is the point such that _𝑓_[′] ( _𝑐_ ) = _[𝑓]_[(] _[𝑏] 𝑏_[)] −[−] _𝑎[𝑓]_[(] _[𝑎]_[)] , that is, the tangent line at the point[�] _𝑐, 𝑓_ ( _𝑐_ )[�] has the same slope as the line between[�] _𝑎, 𝑓_ ( _𝑎_ )[�] and[�] _𝑏, 𝑓_ ( _𝑏_ )[�] . The name comes from the fact that the slope of the secant line is the mean value of the derivative, so the average derivative is achieved in the interior of the interval.

The theorem follows from by subtracting from _𝑓_ the affine linear function with the derivative _[𝑓]_[(] _[𝑏] 𝑏_[)] −[−] _𝑎[𝑓]_[(] _[𝑎]_[)] with the same values at _𝑎_ and _𝑏_ as _𝑓_ . That is, we subtract the function whose graph is the straight line[�] _𝑎, 𝑓_ ( _𝑎_ )[�] and[�] _𝑏, 𝑓_ ( _𝑏_ )[�] . Then we are looking for a point where this new function has derivative zero.

**==> picture [222 x 148] intentionally omitted <==**

**----- Start of picture text -----**<br>
( 푏, 푓 ( 푏 ))<br>푐<br>( 푎, 푓 ( 푎 ))<br>**----- End of picture text -----**<br>


**Figure 4.5:** Graphical interpretation of the mean value theorem.

_Proof._ Define the function _𝑔_ : [ _𝑎, 𝑏_ ] → ℝ by

**==> picture [209 x 28] intentionally omitted <==**

_4.2. MEAN VALUE THEOREM_

165

The function _𝑔_ is differentiable on ( _𝑎, 𝑏_ ), continuous on [ _𝑎, 𝑏_ ], such that _𝑔_ ( _𝑎_ ) = 0 and _𝑔_ ( _𝑏_ ) = 0. Thus there exists a _𝑐_ ∈( _𝑎, 𝑏_ ) such that _𝑔_[′] ( _𝑐_ ) = 0, that is,

**==> picture [162 x 27] intentionally omitted <==**

In other words, _𝑓_ ( _𝑏_ ) − _𝑓_ ( _𝑎_ ) = _𝑓_[′] ( _𝑐_ )( _𝑏_ − _𝑎_ ).

**==> picture [9 x 7] intentionally omitted <==**

The proof generalizes. By considering _𝑔_ ( _𝑥_ ) � _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑏_ ) − _𝜑[𝑓]_[(] ( _[𝑏] 𝑏_[)] )−[−] _𝜑[𝑓]_[(] ( _[𝑎] 𝑎_[)] ) � _𝜑_ ( _𝑥_ ) − _𝜑_ ( _𝑏_ )[�] , one can prove the following version. We leave the proof as an exercise.

**Theorem 4.2.5** (Cauchy’s mean value theorem) **.** _Let 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _and 𝜑_ : [ _𝑎, 𝑏_ ] → ℝ _be continuous functions differentiable on_ ( _𝑎, 𝑏_ ) _. Then there exists a point 𝑐_ ∈( _𝑎, 𝑏_ ) _such that_

**==> picture [206 x 15] intentionally omitted <==**

The mean value theorem has the distinction of being one of the few theorems cited in court. That is, when police measure the speed of cars by aircraft, or via cameras reading license plates, they measure the time the car takes to go between two points. The mean value theorem then says that the car must have somewhere attained the speed you get by dividing the difference in distance by the difference in time.

## **4.2.4 Applications**

Let us look at a few applications of the mean value theorem. The applications show the typical use of the theorem, which is to get rid of a limit by finding the right sort of points where the derivative is not just close to some difference quotient, but actually equal to one. First, we solve our very first differential equation.