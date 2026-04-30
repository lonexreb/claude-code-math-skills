Example 7.4.15

**Example 7.4.15:** The discrete metric provides interesting counterexamples again. Let ( _𝑋, 𝑑_ ) be a metric space with the discrete metric, that is, _𝑑_ ( _𝑥, 𝑦_ ) = 1 if _𝑥_ ≠ _𝑦_ . Suppose _𝑋_ is an Then infinite set.

- (i) ( _𝑋, 𝑑_ ) is a complete metric space.

- (ii) Any subset _𝐾_ ⊂ _𝑋_ is closed and bounded.

- (iii) A subset _𝐾_ ⊂ _𝑋_ is compact if and only if it is a finite set.

- (iv) The conclusion of the Lebesgue covering lemma is always satisfied, e.g. with _𝛿_ =[1] /2, _𝐾_ ⊂ _𝑋_ .

- even for noncompact

The proofs of the statements above are either trivial or are relegated to the exercises below.

_Remark_ 7.4.16 _._ A subtle issue with Cauchy sequences, completeness, compactness, and convergence is that compactness and convergence only depend on the topology, that is, on which sets are the open sets. On the other hand, Cauchy sequences and completeness depend on the actual metric. See .

## **7.4.3 Exercises**

_**Exercise**_ **7.4.1** _**:** Let_ ( _𝑋, 𝑑_ ) _be a metric space and 𝐴 a finite subset of 𝑋. Show that 𝐴 is compact._

_**Exercise**_ **7.4.2** _**:** Let 𝐴_ � {[1] / _𝑛_ : _𝑛_ ∈ ℕ} ⊂ ℝ _._

_a) Show that 𝐴 is not compact directly using the definition._

- _b) Show that 𝐴_ ∪{0} _is compact directly using the definition._

_**Exercise**_ **7.4.3** _**:** Let_ ( _𝑋, 𝑑_ ) _be a metric space with the discrete metric._

_a) Prove that 𝑋 is complete._

- _b) Prove that 𝑋 is compact if and only if 𝑋 is a finite set._

_**Exercise**_ **7.4.4** _**:**_

- _a) Show that the union of finitely many compact sets is a compact set._

- _b) Find an example where the union of infinitely many compact sets is not compact._

_**Exercise**_ **7.4.5** _**:** Prove for arbitrary dimension. Hint: The trick is to use the correct notation._

_CHAPTER 7. METRIC SPACES_

286

_**Exercise**_ **7.4.6** _**:** Show that a compact set 𝐾 (in any metric space) is itself a complete metric space (using the subspace metric)._

_**Exercise**_ **7.4.7** _**:** Let 𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] _be the metric space as in . Show that 𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] _is a complete metric space._

_**Exercise**_ **7.4.8** (Challenging) _**:** Let 𝐶_[�] [0 _,_ 1] _,_ ℝ[�] _be the metric space of . Let_ 0 _denote the zero function. Then show that the closed ball 𝐶_ (0 _,_ 1) _is not compact (even though it is closed and bounded). Hints: Construct a sequence of distinct continuous functions_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[such that][ 𝑑]_[(] _[𝑓][𝑛][,]_[ 0][)][ =][ 1] _[ and][ 𝑑]_[(] _[𝑓][𝑛][,][𝑓][𝑘]_[)][ =][ 1] _[ for] all 𝑛_ ≠ _𝑘. Show that the set_ { _𝑓𝑛_ : _𝑛_ ∈ ℕ} ⊂ _𝐶_ (0 _,_ 1) _is closed but not compact. See for inspiration._ _**Exercise**_ **7.4.9** (Challenging) _**:** Show that there exists a metric on_ ℝ _that makes_ ℝ _into a compact set._ _**Exercise**_ **7.4.10** _**:** Suppose_ ( _𝑋, 𝑑_ ) _is complete and suppose we have a countably infinite collection of nonempty compact sets 𝐸_ 1 ⊃ _𝐸_ 2 ⊃ _𝐸_ 3 ⊃· · · _. Prove_[�][∞] _𝑗_ =1 _[𝐸][𝑗]_[≠][∅] _[.]_

_**Exercise**_ **7.4.11** (Challenging) _**:** Let 𝐶_[�] [0 _,_ 1] _,_ ℝ[�] _be the metric space of . Let 𝐾 be the set of 𝑓_ ∈ _𝐶_[�] [0 _,_ 1] _,_ ℝ[�] _such that 𝑓 is equal to a quadratic polynomial, i.e. 𝑓_ ( _𝑥_ ) = _𝑎_ + _𝑏𝑥_ + _𝑐𝑥_[2] _, and such that_ �� _𝑓_ ( _𝑥_ )�� ≤ 1 _for all 𝑥_ ∈[0 _,_ 1] _, that is 𝑓_ ∈ _𝐶_ (0 _,_ 1) _. Show that 𝐾 is compact._

_**Exercise**_ **7.4.12** (Challenging) _**:** Let_ ( _𝑋, 𝑑_ ) _be a complete metric space. Show that 𝐾_ ⊂ _𝑋 is compact if and only if 𝐾 is closed and such that for every 𝜖>_ 0 _there exists a finite set of points 𝑥_ 1 _, 𝑥_ 2 _, . . . , 𝑥𝑛 with 𝐾_ ⊂[�] _[𝑛] 𝑗_ =1 _[𝐵]_[(] _[𝑥][𝑗][,][ 𝜖]_[)] _[.][Note:][Such a set][ 𝐾][is said to be]_[ totally bounded] _[, so in a complete metric space a set is] compact if and only if it is closed and totally bounded._

_**Exercise**_ **7.4.13** _**:** Take_ ℕ ⊂ ℝ _using the standard metric. Find an open cover of_ ℕ _such that the conclusion of the Lebesgue covering lemma does not hold._

_**Exercise**_ **7.4.14** _**:** Prove the general Bolzano–Weierstrass theorem: Any bounded sequence_ { _𝑥𝑘_ }[∞] _𝑘_ =1 _[in]_[ ℝ] _[𝑛][has] a convergent subsequence._

_**Exercise**_ **7.4.15** _**:** Let 𝑋 be a metric space and 𝐶_ ⊂ _P_ ( _𝑋_ ) _the set of nonempty compact subsets of 𝑋. Using the Hausdorff metric from , show that_ ( _𝐶, 𝑑𝐻_ ) _is a metric space. That is, show that if 𝐿 and 𝐾 are nonempty compact subsets, then 𝑑𝐻_ ( _𝐿, 𝐾_ ) = 0 _if and only if 𝐿_ = _𝐾._

_**Exercise**_ **7.4.16** _**:** Prove . That is, let_ ( _𝑋, 𝑑_ ) _be a complete metric space and 𝐸_ ⊂ _𝑋 a closed set. Show that 𝐸 with the subspace metric is a complete metric space._

_**Exercise**_ **7.4.17** _**:** Let_ ( _𝑋, 𝑑_ ) _be an incomplete metric space. Show that there exists a closed and bounded set 𝐸_ ⊂ _𝑋 that is not compact._

_**Exercise**_ **7.4.18** _**:** Let_ ( _𝑋, 𝑑_ ) _be a metric space and 𝐾_ ⊂ _𝑋. Prove that 𝐾 is compact as a subset of_ ( _𝑋, 𝑑_ ) _if and only if 𝐾 is compact as a subset of itself with the subspace metric._

_**Exercise**_ **7.4.19** _**:** Consider two metrics on_ ℝ _. Let 𝑑_ ( _𝑥, 𝑦_ ) � �� _𝑥_ − _𝑦_ �� _be the standard metric, and let 𝑥 𝑦 𝑑_[′] ( _𝑥, 𝑦_ ) � �� 1+| _𝑥_ |[−] 1+| _𝑦_ | �� _._

_a) Show that_ (ℝ _, 𝑑_[′] ) _is a metric space (if you have done , the computation is the same)._

- _b) Show that the topology is the same, that is, a set is open in_ (ℝ _, 𝑑_ ) _if and only if it is open in_ (ℝ _, 𝑑_[′] ) _._

- _c) Show that a set is compact in_ (ℝ _, 𝑑_ ) _if and only if it is compact in_ (ℝ _, 𝑑_[′] ) _._

- _d) Show that a sequence converges in_ (ℝ _, 𝑑_ ) _if and only if it converges in_ (ℝ _, 𝑑_[′] ) _._

- _e) Find a sequence of real numbers that is Cauchy in_ (ℝ _, 𝑑_[′] ) _but not Cauchy in_ (ℝ _, 𝑑_ ) _._

- _f) While_ (ℝ _, 𝑑_ ) _is complete, show that_ (ℝ _, 𝑑_[′] ) _is not complete._

287

## _7.4. COMPLETENESS AND COMPACTNESS_

_**Exercise**_ **7.4.20** _**:** Let_ ( _𝑋, 𝑑_ ) _be a complete metric space. We say a set 𝑆_ ⊂ _𝑋 is_ relatively compact _if the closure 𝑆 is compact. Prove that 𝑆_ ⊂ _𝑋 is relatively compact if and only if given any sequence_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[in][ 𝑆][,] there exists a subsequence_ { _𝑥𝑛𝑘_ }[∞] _𝑘_ =1 _[that converges (in][ 𝑋][).]_

_CHAPTER 7. METRIC SPACES_

288

## **7.5 Continuous functions**

_Note: 1.5–2 lectures_

## **7.5.1 Continuity**