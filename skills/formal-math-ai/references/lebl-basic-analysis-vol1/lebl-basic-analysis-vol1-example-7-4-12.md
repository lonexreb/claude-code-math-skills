Example 7.4.12

**Example 7.4.12:** , the Bolzano–Weierstrass theorem for sequences of real numbers, says that every bounded sequence in ℝ has a convergent subsequence. Therefore, every sequence in a closed interval [ _𝑎, 𝑏_ ] ⊂ ℝ has a convergent subsequence. The limit is also in [ _𝑎, 𝑏_ ] as limits preserve non-strict inequalities. Hence a closed bounded interval [ _𝑎, 𝑏_ ] ⊂ ℝ is (sequentially) compact. **Proposition 7.4.13.** _Let_ ( _𝑋, 𝑑_ ) _be a metric space and let 𝐾_ ⊂ _𝑋 be compact. If 𝐸_ ⊂ _𝐾 is a closed set, then 𝐸 is compact._

Because _𝐾_ is closed, _𝐸_ is closed in _𝐾_ if and only if it is closed in _𝑋_ . See .

_Proof._ Let { _𝑥𝑛_ }[∞] _𝑛_ =1[be][a][sequence][in] _[𝐸]_[.][It][is][also][a][sequence][in] _[𝐾]_[.][Therefore,][it][has][a] convergent subsequence { _𝑥𝑛𝑗_ }[∞] _𝑗_ =1[that converges to some] _[ 𝑥]_[∈] _[𝐾]_[.][As] _[ 𝐸]_[is closed the limit of] a sequence in _𝐸_ is also in _𝐸_ and so _𝑥_ ∈ _𝐸_ . Thus _𝐸_ must be compact. □

**Theorem 7.4.14** (Heine–Borel ) **.** _A closed bounded subset 𝐾_ ⊂ ℝ _[𝑛] is compact._

So subsets of ℝ _[𝑛]_ are compact if and only if they are closed and bounded, a condition that is much easier to check. Let us reiterate that the Heine–Borel theorem only holds for ℝ _[𝑛]_ and not for metric spaces in general. The theorem does not hold even for subspaces of ℝ _[𝑛]_ , just in ℝ _[𝑛]_ itself. In general, compact implies closed and bounded, but not vice versa.

_Proof._ For ℝ = ℝ[1] , suppose _𝐾_ ⊂ ℝ is closed and bounded. Then _𝐾_ ⊂[ _𝑎, 𝑏_ ] for some closed and bounded interval, which is compact by . As _𝐾_ is a closed subset of a . compact set, it is compact by

We carry out the proof for _𝑛_ = 2 and leave arbitrary _𝑛_ as an exercise. As _𝐾_ ⊂ ℝ[2] is bounded, there exists a set _𝐵_ = [ _𝑎, 𝑏_ ] × [ _𝑐, 𝑑_ ] ⊂ ℝ[2] such that _𝐾_ ⊂ _𝐵_ . We will show that _𝐵_ is compact. Then _𝐾_ , being a closed subset of a compact _𝐵_ , is also compact. ∞ Let �( _𝑥𝑘 , 𝑦𝑘_ )� _𝑘_ =1[be a sequence in] _[𝐵]_[.][That is,] _[𝑎]_[≤] _[𝑥][𝑘]_[≤] _[𝑏]_[and] _[𝑐]_[≤] _[𝑦][𝑘]_[≤] _[𝑑]_[for all] _[𝑘]_[.][A] bounded sequence of real numbers has a convergent subsequence so there is a subsequence

> ‗Named after the German mathematician (1821–1881), and the French mathematician (1871–1956).

_7.4. COMPLETENESS AND COMPACTNESS_

285

{ _𝑥𝑘 𝑗_ }[∞] _𝑗_ =1[that is convergent.][The subsequence][ {] _[𝑦][𝑘][𝑗]_[}][∞] _𝑗_ =1[is also a bounded sequence so there] exists a subsequence { _𝑦𝑘 𝑗𝑖_ }[∞] _𝑖_ =1[that is convergent.][A subsequence of a convergent sequence] is still convergent, so { _𝑥𝑘 𝑗𝑖_ }[∞] _𝑖_ =1[is convergent.][Let]

**==> picture [202 x 18] intentionally omitted <==**

By , �( _𝑥𝑘 𝑗𝑖 , 𝑦𝑘 𝑗𝑖_ )�∞ _𝑖_ =1[converges to][ (] _[𝑥, 𝑦]_[)][.][Furthermore, as] _[𝑎]_[≤] _[𝑥][𝑘]_[≤] _[𝑏]_[and] _𝑐_ ≤ _𝑦𝑘_ ≤ _𝑑_ for all _𝑘_ , we know that ( _𝑥, 𝑦_ ) ∈ _𝐵_ . □