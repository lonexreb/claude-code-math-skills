Definition 4.3.1

**Definition 4.3.1.** For an _𝑛_ times differentiable function _𝑓_ defined near a point _𝑥_ 0 ∈ ℝ, define the _𝑛_ th order _Taylor polynomial_ for _𝑓_ at _𝑥_ 0 as

**==> picture [351 x 102] intentionally omitted <==**

See for the odd-degree Taylor polynomials for the sine function at _𝑥_ 0 = 0. The even-degree terms are all zero, as even derivatives of sine are again sines, which are zero at the origin.

Taylor’s theorem says a function behaves like its _𝑛_ th Taylor polynomial. The is really Taylor’s theorem for _𝑛_ = 0.

> ‗Named for the English mathematician (1685–1731). It was first found by the Scottish mathematician (1638–1675). The statement we give was proved by (1736–1813).

_CHAPTER 4. THE DERIVATIVE_

172

**==> picture [290 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
푦 = sin( 푥 ) 푦 =  푃 3 [0][(] [푥] [)] 푦 =  푃 1 [0][(] [푥] [)]<br>푦 =  푃 5 [0][(] [푥] [)] 푦 =  푃 7 [0][(] [푥] [)]<br>**----- End of picture text -----**<br>


**Figure 4.8:** The odd degree Taylor polynomials for the sine function.

**Theorem 4.3.2** (Taylor) **.** _Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is a function with 𝑛 continuous derivatives on_ [ _𝑎, 𝑏_ ] _and such that 𝑓_[(] _[𝑛]_[+][1][)] _exists on_ ( _𝑎, 𝑏_ ) _. Given distinct points 𝑥_ 0 _and 𝑥 in_ [ _𝑎, 𝑏_ ] _, we can find a point 𝑐 between 𝑥_ 0 _and 𝑥 such that_

**==> picture [188 x 32] intentionally omitted <==**

_𝑓_[(] _[𝑛]_[+][1][)] ( _𝑐_ ) The term _𝑅𝑛[𝑥]_[0][(] _[𝑥]_[)][�] ( _𝑛_ +1)![(] _[𝑥]_[−] _[𝑥]_[0][)] _[𝑛]_[+][1][is][called][the] _[remainder][term]_[.][This][form][of][the] remainder term is called the _Lagrange form_ of the remainder. There are other ways to write the remainder term, but we skip those. Note that _𝑐_ depends on both _𝑥_ and _𝑥_ 0.

_Proof._ Find a number _𝑀𝑥,𝑥_ 0 (depending on _𝑥_ and _𝑥_ 0) solving the equation

**==> picture [170 x 16] intentionally omitted <==**

Define a function _𝑔_ ( _𝑠_ ) by

**==> picture [206 x 16] intentionally omitted <==**

We compute the _𝑘_ th derivative at _𝑥_ 0 of the Taylor polynomial ( _𝑃𝑛[𝑥]_[0][)][(] _[𝑘]_[)][(] _[𝑥]_ 0[)][=] _[𝑓]_[(] _[𝑘]_[)][(] _[𝑥]_ 0[)][for] _𝑘_ = 0 _,_ 1 _,_ 2 _, . . . , 𝑛_ (the zeroth derivative of a function is the function itself). Therefore,

**==> picture [227 x 16] intentionally omitted <==**

In particular, _𝑔_ ( _𝑥_ 0) = 0. On the other hand _𝑔_ ( _𝑥_ ) = 0. By the , there exists an _𝑥_ 1 between _𝑥_ 0 and _𝑥_ such that _𝑔_[′] ( _𝑥_ 1) = 0. Applying the to _𝑔_[′] , we obtain that there exists _𝑥_ 2 between _𝑥_ 0 and _𝑥_ 1 (and therefore between _𝑥_ 0 and _𝑥_ ) such that _𝑔_[′′] ( _𝑥_ 2) = 0. We repeat the argument _𝑛_ + 1 times to obtain a number _𝑥𝑛_ +1 between _𝑥_ 0 and _𝑥𝑛_ (and therefore between _𝑥_ 0 and _𝑥_ ) such that _𝑔_[(] _[𝑛]_[+][1][)] ( _𝑥𝑛_ +1) = 0.

_4.3. TAYLOR’S THEOREM_

173

Let _𝑐_ � _𝑥𝑛_ +1. We compute the ( _𝑛_ + 1)th derivative of _𝑔_ to find

**==> picture [188 x 16] intentionally omitted <==**

**==> picture [468 x 23] intentionally omitted <==**

In the proof, we found ( _𝑃𝑛[𝑥]_[0][)][(] _[𝑘]_[)][(] _[𝑥]_ 0[)][ =] _[𝑓]_[(] _[𝑘]_[)][(] _[𝑥]_ 0[)][ for] _[ 𝑘]_[=][ 0] _[,]_[ 1] _[,]_[ 2] _[, . . . , 𝑛]_[.][Therefore, the Taylor] polynomial has the same derivatives as _𝑓_ at _𝑥_ 0 up to the _𝑛_ th derivative. That is why the Taylor polynomial is a good approximation to _𝑓_ . Notice how in the Taylor polynomials are reasonably good approximations to the sine near _𝑥_ = 0. We do not necessarily get good approximations by the Taylor polynomial everywhere. Consider expanding the function _𝑓_ ( _𝑥_ ) � 1− _𝑥𝑥_[around 0,][for] _[𝑥][<]_[1][,][we get the graphs in] . The The dotted lines are the first, second, and third degree approximations. dashed line is the 20th degree polynomial. The approximation does seem to get better as the degree rises for _𝑥 >_ −1. For _𝑥 <_ −1, it in fact gets visibly worse. The polynomials are the partial sums of the geometric series[�][∞] _𝑛_ =1 _[𝑥][𝑛]_[, and the series only converges on][ (−][1] _[,]_[ 1][)][.] . See the discussion of power series

**==> picture [290 x 147] intentionally omitted <==**

**Figure 4.9:** The function 1− _𝑥𝑥_[,][and][the][Taylor][polynomials] _[𝑃]_ 1[0][,] _[𝑃]_ 2[0][,] _[𝑃]_ 3[0][(all][dotted),][and][the] polynomial _𝑃_ 20[0][(dashed).]

If _𝑓_ is _infinitely differentiable_ , that is, if _𝑓_ can be differentiated any number of times, then : we define the _Taylor series_

**==> picture [109 x 36] intentionally omitted <==**

There is no guarantee that this series converges for any _𝑥_ ≠ _𝑥_ 0. Even where it does converge, there is no guarantee that it converges to the function _𝑓_ . Functions _𝑓_ whose Taylor series at every point _𝑥_ 0 converges to _𝑓_ in some open interval containing _𝑥_ 0 are called _analytic functions_ . Many functions one tends to see in practice are analytic. See , for an example of a non-analytic function.

_CHAPTER 4. THE DERIVATIVE_

174

The definition of derivative says that a function is differentiable if it is locally approximated by a line. We mention in passing that there exists a converse to Taylor’s theorem, which we will neither state nor prove, saying that if a function is locally approximated in a certain way by a polynomial of degree _𝑑_ , then it has _𝑑_ derivatives.

Taylor’s theorem gives us a quick proof of a version of the second derivative test. By a _strict relative minimum_ of _𝑓_ at _𝑐_ , we mean that there exists a _𝛿>_ 0 such that _𝑓_ ( _𝑥_ ) _> 𝑓_ ( _𝑐_ ) for all _𝑥_ ∈( _𝑐_ − _𝛿, 𝑐_ + _𝛿_ ) where _𝑥_ ≠ _𝑐_ . A _strict relative maximum_ is defined similarly. Continuity of the second derivative is not needed, but the proof is more difficult and is left as an exercise. The proof also generalizes immediately into the _𝑛_ th derivative test, which is also left as an exercise.

**Proposition 4.3.3** (Second derivative test) **.** _Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _is twice continuously differentiable, 𝑥_ 0 ∈( _𝑎, 𝑏_ ) _, 𝑓_[′] ( _𝑥_ 0) = 0 _and 𝑓_[′′] ( _𝑥_ 0) _>_ 0 _. Then 𝑓 has a strict relative minimum at 𝑥_ 0 _._

_Proof._ As _𝑓_[′′] is continuous, there exists a _𝛿>_ 0 such that _𝑓_[′′] ( _𝑐_ ) _>_ 0 for all _𝑐_ ∈( _𝑥_ 0 − _𝛿, 𝑥_ 0 + _𝛿_ ), see . Take _𝑥_ ∈( _𝑥_ 0 − _𝛿, 𝑥_ 0 + _𝛿_ ), _𝑥_ ≠ _𝑥_ 0. Taylor’s theorem says that for some _𝑐_ between _𝑥_ 0 and _𝑥_ ,

**==> picture [419 x 51] intentionally omitted <==**

**==> picture [279 x 16] intentionally omitted <==**

## **4.3.3 Exercises**

_**Exercise**_ **4.3.1** _**:** Compute the 𝑛th Taylor polynomial at_ 0 _for the exponential function._

_**Exercise**_ **4.3.2** _**:** Suppose 𝑝 is a polynomial of degree 𝑑. Given 𝑥_ 0 ∈ ℝ _, show that the 𝑑th Taylor polynomial for 𝑝 at 𝑥_ 0 _is equal to 𝑝._

_**Exercise**_ **4.3.3** _**:** Let 𝑓_ ( _𝑥_ ) � | _𝑥_ |[3] _. Compute 𝑓_[′] ( _𝑥_ ) _and 𝑓_[′′] ( _𝑥_ ) _for all 𝑥, but show that 𝑓_[(][3][)] (0) _does not exist._

_**Exercise**_ **4.3.4** _**:** Suppose 𝑓_ : ℝ → ℝ _has 𝑛 continuous derivatives. Show that for every 𝑥_ 0 ∈ ℝ _, there exist polynomials 𝑃 and 𝑄 of degree 𝑛 and an 𝜖>_ 0 _such that 𝑃_ ( _𝑥_ ) ≤ _𝑓_ ( _𝑥_ ) ≤ _𝑄_ ( _𝑥_ ) _for all 𝑥_ ∈[ _𝑥_ 0 _, 𝑥_ 0 + _𝜖_ ] _and 𝑄_ ( _𝑥_ ) − _𝑃_ ( _𝑥_ ) = _𝜆_ ( _𝑥_ − _𝑥_ 0) _[𝑛] for some 𝜆_ ≥ 0 _._

_𝑅𝑛𝑥_ 0[(] _[𝑥]_[)] _**Exercise**_ **4.3.5** _**:** If 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _has 𝑛_ + 1 _continuous derivatives and 𝑥_ 0 ∈[ _𝑎, 𝑏_ ] _, prove 𝑥_ lim→ _𝑥_ 0 ( _𝑥_ − _𝑥_ 0) ~~_[𝑛]_~~[=][ 0] _[.]_

_**Exercise**_ **4.3.6** _**:** Suppose 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _has 𝑛_ +1 _continuous derivatives and 𝑥_ 0 ∈( _𝑎, 𝑏_ ) _. Prove: 𝑓_[(] _[𝑘]_[)] ( _𝑥_ 0) = 0 _for all 𝑘_ = 0 _,_ 1 _,_ 2 _, . . . , 𝑛 if and only if 𝑥_ lim→ _𝑥_ 0 ( _𝑥_ − _𝑓𝑥_ (0 _𝑥_ )) _[𝑛]_[+][1] _[exists.]_

_**Exercise**_ **4.3.7** _**:** Suppose 𝑎, 𝑏, 𝑐_ ∈ ℝ _and 𝑓_ : ℝ → ℝ _is differentiable, 𝑓_[′′] ( _𝑥_ ) = _𝑎 for all 𝑥, 𝑓_[′] (0) = _𝑏, and 𝑓_ (0) = _𝑐. Find 𝑓 and prove that it is the unique differentiable function with this property._

_**Exercise**_ **4.3.8** (Challenging) _**:** Show that a simple converse to Taylor’s theorem does not hold. Find a function 𝑓_ : ℝ → ℝ _with no second derivative at 𝑥_ = 0 _such that_ �� _𝑓_ ( _𝑥_ )�� ≤ �� _𝑥_ 3�� _, that is, 𝑓 goes to zero at 0 faster than 𝑥_[2] _, and while 𝑓_[′] (0) _exists, 𝑓_[′′] (0) _does not._

175

## _4.3. TAYLOR’S THEOREM_

- _**Exercise**_ **4.3.9** _**:** Suppose 𝑓_ : (0 _,_ 1) → ℝ _is differentiable and 𝑓_[′′] _is bounded._

- _a) Show that there exists a once differentiable function 𝑔_ : [0 _,_ 1) → ℝ _such that 𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) _for all 𝑥_ ≠ 0 _. Hint: See ._

- _b) Find an example where the 𝑔 is not twice differentiable at 𝑥_ = 0 _._

- _**Exercise**_ **4.3.10** _**:** Prove the 𝑛_ th derivative test _. Suppose 𝑛_ ∈ ℕ _, 𝑥_ 0 ∈( _𝑎, 𝑏_ ) _, and 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _is 𝑛 times continuously differentiable, with 𝑓_[(] _[𝑘]_[)] ( _𝑥_ 0) = 0 _for 𝑘_ = 1 _,_ 2 _, . . . , 𝑛_ − 1 _, and 𝑓_[(] _[𝑛]_[)] ( _𝑥_ 0) ≠ 0 _. Prove:_

- _a) If 𝑛 is odd, then 𝑓 has neither a relative minimum, nor a maximum at 𝑥_ 0 _._

- _b) If 𝑛 is even, then 𝑓 has a strict relative minimum at 𝑥_ 0 _if 𝑓_[(] _[𝑛]_[)] ( _𝑥_ 0) _>_ 0 _and a strict relative maximum at 𝑥_ 0 _if 𝑓_[(] _[𝑛]_[)] ( _𝑥_ 0) _<_ 0 _._

_**Exercise**_ **4.3.11** _**:** Prove the more general version of the second derivative test. Suppose 𝑓_ : ( _𝑎, 𝑏_ ) → ℝ _is differentiable and 𝑥_ 0 ∈( _𝑎, 𝑏_ ) _is such that, 𝑓_[′] ( _𝑥_ 0) = 0 _, 𝑓_[′′] ( _𝑥_ 0) _exists, and 𝑓_[′′] ( _𝑥_ 0) _>_ 0 _. Prove that 𝑓 has a strict relative minimum at 𝑥_ 0 _. Hint: Consider the limit definition of 𝑓_[′′] ( _𝑥_ 0) _._

_CHAPTER 4. THE DERIVATIVE_

176

## **4.4 Inverse function theorem**

_Note: less than 1 lecture (optional section, needed for , requires )_

## **4.4.1 Inverse function theorem**

We start with a simple example. Consider the function _𝑓_ ( _𝑥_ ) � _𝑎𝑥_ for a number _𝑎_ ≠ 0. Then _𝑓_ : ℝ → ℝ is bĳective, and the inverse is _𝑓_[−][1] ( _𝑦_ ) =[1] _𝑎[𝑦]_[.][In particular,] _[𝑓]_[′][(] _[𝑥]_[)][=] _[𝑎]_[and] ( _𝑓_[−][1] )[′] ( _𝑦_ ) =[1] _𝑎_[.][As differentiable functions are “infinitesimally like” linear functions, we] The main expect the same sort of behavior from the inverse of a differentiable function. idea of differentiating inverse functions is the following lemma.