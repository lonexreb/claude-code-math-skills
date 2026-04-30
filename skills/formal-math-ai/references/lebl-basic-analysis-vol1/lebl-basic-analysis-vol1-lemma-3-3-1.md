Lemma 3.3.1

**Lemma 3.3.1.** _A continuous function 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _is bounded._

_Proof._ We prove the claim by contrapositive. Suppose _𝑓_ is not bounded. Then for each _𝑛_ ∈ ℕ, there is an _𝑥𝑛_ ∈[ _𝑎, 𝑏_ ], such that

**==> picture [61 x 16] intentionally omitted <==**

The sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[is bounded as] _[𝑎]_[≤] _[𝑥][𝑛]_[≤] _[𝑏]_[.][By the] , there is a convergent subsequence { _𝑥𝑛𝑖_ }[∞] _𝑖_ =1[.][Let] _[ 𝑥]_[�][lim] _[𝑖]_[→∞] _[𝑥][𝑛][𝑖]_[.][Since] _[ 𝑎]_[≤] _[𝑥][𝑛][𝑖]_[≤] _[𝑏]_[for all] _[ 𝑖]_[,] ∞ then _𝑎_ ≤ _𝑥_ ≤ _𝑏_ . The sequence � _𝑓_ ( _𝑥𝑛𝑖_ )� _𝑖_ =1[is not bounded as] �� _𝑓_ ( _𝑥𝑛𝑖_ )�� ≥ _𝑛𝑖_ ≥ _𝑖_ . Thus _𝑓_ is not continuous at _𝑥_ as

**==> picture [383 x 24] intentionally omitted <==**

Notice a key point of the proof. Boundedness of [ _𝑎, 𝑏_ ] allows us to use Bolzano– Weierstrass, while the fact that it is closed gives us that the limit is back in [ _𝑎, 𝑏_ ]. The technique is a common one: Find a sequence with a certain property, then use Bolzano– Weierstrass to make such a sequence that also converges.

Recall from calculus that _𝑓_ : _𝑆_ → ℝ achieves an _absolute minimum_ at _𝑐_ ∈ _𝑆_ if

**==> picture [148 x 14] intentionally omitted <==**

On the other hand, _𝑓_ achieves an _absolute maximum_ at _𝑐_ ∈ _𝑆_ if

**==> picture [148 x 13] intentionally omitted <==**

If such a _𝑐_ ∈ _𝑆_ exists, then we say _𝑓 achieves an absolute minimum (resp. absolute maximum) on 𝑆_ , and we call _𝑓_ ( _𝑐_ ) the _absolute minimum (resp. absolute maximum)_ .

If _𝑆_ is a closed and bounded interval, then a continuous _𝑓_ is not just bounded, it must achieve an absolute minimum and an absolute maximum on _𝑆_ .

**Theorem 3.3.2** (Minimum-maximum theorem / Extreme value theorem) **.** _A continuous function 𝑓_ : [ _𝑎, 𝑏_ ] → ℝ _achieves both an absolute minimum and an absolute maximum on_ [ _𝑎, 𝑏_ ] _._

Again, we remark that is important that the domain of _𝑓_ is a closed and bounded interval [ _𝑎, 𝑏_ ].

_3.3. EXTREME AND INTERMEDIATE VALUE THEOREMS_

131

**==> picture [292 x 76] intentionally omitted <==**

**Figure 3.6:** _𝑓_ : [ _𝑎, 𝑏_ ] → ℝ achieves an absolute maximum _𝑓_ ( _𝑐_ ) at _𝑐_ , and an absolute minimum _𝑓_ ( _𝑑_ ) at _𝑑_ .

_Proof._ The lemma says that _𝑓_ is bounded, so the set _𝑓_[�] [ _𝑎, 𝑏_ ][�] = � _𝑓_ ( _𝑥_ ) : _𝑥_ ∈[ _𝑎, 𝑏_ ]� has a supremum and an infimum. There exist sequences in the set _𝑓_[�] [ _𝑎, 𝑏_ ][�] that approach ∞ ∞ its supremum and its infimum. That is, there are sequences � _𝑓_ ( _𝑥𝑛_ )� _𝑛_ =1[and] � _𝑓_ ( _𝑦𝑛_ )� _𝑛_ =1[,] where _𝑥𝑛_ and _𝑦𝑛_ are in [ _𝑎, 𝑏_ ], such that

**==> picture [336 x 19] intentionally omitted <==**

We are not done yet; we need to find where the minima and the maxima are. The problem is that the sequences { _𝑥𝑛_ }[∞] _𝑛_ =1[and][{] _[𝑦][𝑛]_[}][∞] _𝑛_ =1[need][not][converge.][We][know][{] _[𝑥][𝑛]_[}][∞] _𝑛_ =1[and] { _𝑦𝑛_ }[∞] _𝑛_ =1[are][bounded][(their][elements][belong][to][a][bounded][interval][[] _[𝑎, 𝑏]_[]][).][Apply][the] to find convergent subsequences { _𝑥𝑛𝑖_ }[∞] _𝑖_ =1[and][ {] _[𝑦][𝑚][𝑖]_[}][∞] _𝑖_ =1[.][Let]

**==> picture [200 x 18] intentionally omitted <==**

As _𝑎_ ≤ _𝑥𝑛𝑖_ ≤ _𝑏_ for all _𝑖_ , we have _𝑎_ ≤ _𝑥_ ≤ _𝑏_ . Similarly, _𝑎_ ≤ _𝑦_ ≤ _𝑏_ . So _𝑥_ and _𝑦_ are in [ _𝑎, 𝑏_ ]. A limit of a subsequence is the same as the limit of the sequence, and we can take a limit past the continuous function _𝑓_ :

**==> picture [308 x 24] intentionally omitted <==**

Similarly,

**==> picture [393 x 43] intentionally omitted <==**

Hence, _𝑓_ achieves an absolute minimum at _𝑥_ and an absolute maximum at _𝑦_ .