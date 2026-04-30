Definition 7.1.12

**Definition 7.1.12.** Let ( _𝑋, 𝑑_ ) be a metric space. A subset _𝑆_ ⊂ _𝑋_ is said to be _bounded_ if there exists a _𝑝_ ∈ _𝑋_ and a _𝐵_ ∈ ℝ such that

**==> picture [136 x 13] intentionally omitted <==**

We say ( _𝑋, 𝑑_ ) is bounded if _𝑋_ itself is a bounded subset.

For example, the set of real numbers with the standard metric is not a bounded metric It is not hard to see that a subset of the real numbers is bounded in the sense of space. if and only if it is bounded as a subset of the metric space of real numbers with the standard metric.

On the other hand, if we take the real numbers with the discrete metric, then we obtain a bounded metric space. In fact, any set with the discrete metric is bounded.

There are other equivalent ways we could generalize boundedness, and are left as exercises. Suppose _𝑋_ is nonempty to avoid a technicality. Then _𝑆_ ⊂ _𝑋_ being bounded is equivalent to either

(i) For every _𝑝_ ∈ _𝑋_ , there exists a _𝐵 >_ 0 such that _𝑑_ ( _𝑝, 𝑥_ ) ≤ _𝐵_ for all _𝑥_ ∈ _𝑆_ .

(ii) diam( _𝑆_ ) � sup� _𝑑_ ( _𝑥, 𝑦_ ) : _𝑥, 𝑦_ ∈ _𝑆_ � _<_ ∞.

The quantity diam( _𝑆_ ) is called the _diameter_ of a set and is usually only defined for a nonempty set.

## **7.1.1 Exercises**

_**Exercise**_ **7.1.1** _**:** Show that for every set 𝑋, the discrete metric (𝑑_ ( _𝑥, 𝑦_ ) = 1 _if 𝑥_ ≠ _𝑦 and 𝑑_ ( _𝑥, 𝑥_ ) = 0 _) does give a metric space_ ( _𝑋, 𝑑_ ) _._

_**Exercise**_ **7.1.2** _**:** Let 𝑋_ � {0} _be a set. Can you make it into a metric space?_

_**Exercise**_ **7.1.3** _**:** Let 𝑋_ � { _𝑎, 𝑏_ } _be a set. Can you make it into two distinct metric spaces? (define two distinct metrics on it)_

_CHAPTER 7. METRIC SPACES_

262

_**Exercise**_ **7.1.4** _**:** Let the set 𝑋_ � { _𝐴, 𝐵, 𝐶_ } _represent 3 buildings on campus. Suppose we wish our distance to be the time it takes to walk from one building to the other. It takes 5 minutes either way between buildings 𝐴 and 𝐵. However, building 𝐶 is on a hill and it takes 10 minutes from 𝐴 and 15 minutes from 𝐵 to get to 𝐶. On the other hand it takes 5 minutes to go from 𝐶 to 𝐴 and 7 minutes to go from 𝐶 to 𝐵, as we are going downhill. Do these distances define a metric? If so, prove it, if not, say why not._

_**Exercise**_ **7.1.5** _**:** Suppose_ ( _𝑋, 𝑑_ ) _is a metric space and 𝜑_ : [0 _,_ ∞) → ℝ _is an increasing function such that 𝜑_ ( _𝑡_ ) ≥ 0 _for all 𝑡 and 𝜑_ ( _𝑡_ ) = 0 _if and only if 𝑡_ = 0 _. Also suppose 𝜑 is_ subadditive _, that is, 𝜑_ ( _𝑠_ + _𝑡_ ) ≤ _𝜑_ ( _𝑠_ ) + _𝜑_ ( _𝑡_ ) _. Show that with 𝑑_[′] ( _𝑥, 𝑦_ ) � _𝜑_[�] _𝑑_ ( _𝑥, 𝑦_ )[�] _, we obtain a new metric space_ ( _𝑋, 𝑑_[′] ) _._

_**Exercise**_ **7.1.6** _**:** Let_ ( _𝑋, 𝑑𝑋_ ) _and_ ( _𝑌, 𝑑𝑌_ ) _be metric spaces._

_a) Show that_ ( _𝑋_ × _𝑌, 𝑑_ ) _with 𝑑_[�] ( _𝑥_ 1 _, 𝑦_ 1) _,_ ( _𝑥_ 2 _, 𝑦_ 2)[�] � _𝑑𝑋_ ( _𝑥_ 1 _, 𝑥_ 2) + _𝑑𝑌_ ( _𝑦_ 1 _, 𝑦_ 2) _is a metric space. b) Show that_ ( _𝑋_ × _𝑌, 𝑑_ ) _with 𝑑_[�] ( _𝑥_ 1 _, 𝑦_ 1) _,_ ( _𝑥_ 2 _, 𝑦_ 2)[�] � max� _𝑑𝑋_ ( _𝑥_ 1 _, 𝑥_ 2) _, 𝑑𝑌_ ( _𝑦_ 1 _, 𝑦_ 2)� _is a metric space._

_**Exercise**_ **7.1.7** _**:** Let 𝑋 be the set of continuous functions on_ [0 _,_ 1] _. Let 𝜑_ : [0 _,_ 1] →(0 _,_ ∞) _be continuous. Define_

**==> picture [168 x 30] intentionally omitted <==**

_Show that_ ( _𝑋, 𝑑_ ) _is a metric space._

_**Exercise**_ **7.1.8** _**:** Let_ ( _𝑋, 𝑑_ ) _be a metric space. For nonempty bounded subsets 𝐴 and 𝐵 let_

**==> picture [349 x 15] intentionally omitted <==**

_Now define the_ Hausdorff metric _as_

**==> picture [166 x 15] intentionally omitted <==**

_Note: 𝑑𝐻 can be defined for arbitrary nonempty subsets if we allow the extended reals._

- _a) Let 𝑌_ ⊂ _P_ ( _𝑋_ ) _be the set of bounded nonempty subsets. Prove that_ ( _𝑌, 𝑑𝐻_ ) _is a so-called_ pseudometric space _: 𝑑𝐻 satisfies the metric properties , , , and further 𝑑𝐻_ ( _𝐴, 𝐴_ ) = 0 _for all 𝐴_ ∈ _𝑌._

- _b) Show by example that 𝑑 itself is not symmetric, that is 𝑑_ ( _𝐴, 𝐵_ ) ≠ _𝑑_ ( _𝐵, 𝐴_ ) _._

- _c) Find a metric space 𝑋 and two different nonempty bounded subsets 𝐴 and 𝐵 such that 𝑑𝐻_ ( _𝐴, 𝐵_ ) = 0 _._

_**Exercise**_ **7.1.9** _**:** Let_ ( _𝑋, 𝑑_ ) _be a nonempty metric space and 𝑆_ ⊂ _𝑋 a subset. Prove:_

- _a) 𝑆 is bounded if and only if for every 𝑝_ ∈ _𝑋, there exists a 𝐵 >_ 0 _such that 𝑑_ ( _𝑝, 𝑥_ ) ≤ _𝐵 for all 𝑥_ ∈ _𝑆._

_b) A nonempty 𝑆 is bounded if and only if_ diam( _𝑆_ ) � sup{ _𝑑_ ( _𝑥, 𝑦_ ) : _𝑥, 𝑦_ ∈ _𝑆_ } _<_ ∞ _._

_**Exercise**_ **7.1.10** _**:**_

_a) Working in_ ℝ _, compute_ diam[�] [ _𝑎, 𝑏_ ][�] _._

- _b) Working in_ ℝ _[𝑛] , for every 𝑟 >_ 0 _, let 𝐵𝑟_ � { _𝑥_ 1[2][+] _[ 𝑥]_ 2[2][+ · · · +] _[ 𝑥] 𝑛_[2] _[<][𝑟]_[2][}] _[.][Compute]_[ diam][(] _[𝐵][𝑟]_[)] _[.]_

- _c) Suppose_ ( _𝑋, 𝑑_ ) _is a metric space with at least two points, 𝑑 is the discrete metric, and 𝑝_ ∈ _𝑋. Compute_ diam({ _𝑝_ }) _and_ diam( _𝑋_ ) _, then conclude that_ ( _𝑋, 𝑑_ ) _is bounded._

263

## _7.1. METRIC SPACES_

## _**Exercise**_ **7.1.11** _**:**_

- _a) Find a metric 𝑑 on_ ℕ _such that_ ℕ _is an unbounded set in_ (ℕ _, 𝑑_ ) _._

- _b) Find a metric 𝑑 on_ ℕ _such that_ ℕ _is a bounded set in_ (ℕ _, 𝑑_ ) _._

- _c) Find a metric 𝑑 on_ ℕ _such that for every 𝑛_ ∈ ℕ _and every 𝜖>_ 0 _, there exists an 𝑚_ ∈ ℕ _such that 𝑑_ ( _𝑛, 𝑚_ ) _< 𝜖._

- _**Exercise**_ **7.1.12** _**:** Let 𝐶_[1][�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] _be the set of once continuously differentiable functions on_ [ _𝑎, 𝑏_ ] _. Define_

**==> picture [178 x 13] intentionally omitted <==**

_where_ ∥·∥[ _𝑎,𝑏_ ] _is the uniform norm. Prove that 𝑑 is a metric._

_**Exercise**_ **7.1.13** _**:** Consider ℓ_[2] _the set of sequences_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[of real numbers such that]_[ �][∞] _𝑛_ =1 _[𝑥] 𝑛_[2] _[<]_[∞] _[.]_

- _a) Prove the Cauchy–Schwarz inequality for two sequences_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[and]_[{] _[𝑦][𝑛]_[}][∞] _𝑛_ =1 _[in][ℓ]_[2] _[:][Prove][that]_ �∞ _𝑛_ =1 _[𝑥][𝑛][𝑦][𝑛][converges (absolutely) and]_

**==> picture [151 x 36] intentionally omitted <==**

- ∞

- _b) Prove that ℓ_[2] _is a metric space with the metric 𝑑_ ( _𝑥, 𝑦_ ) � �� _𝑛_ =1[(] _[𝑥][𝑛]_[−] _[𝑦][𝑛]_[)][2] _[.][Hint:][Don’t forget to show] that the series for 𝑑_ ( _𝑥, 𝑦_ ) _always converges to some finite number._

_CHAPTER 7. METRIC SPACES_

264

## **7.2 Open and closed sets**

_Note: 2 lectures_

## **7.2.1 Topology**

. Before we get to convergence, we define the so-called _topology_ That is, we define open and closed sets in a metric space. And before that, we define two special open and closed sets.