Theorem 7.4.11

**Theorem 7.4.11.** _Let_ ( _𝑋, 𝑑_ ) _be a metric space. Then 𝐾_ ⊂ _𝑋 is compact if and only if every 𝐾 𝐾. sequence in has a subsequence converging to a point in_

> ‗Named after the French mathematician (1875–1941). The number _𝛿_ is sometimes called the Lebesgue number of the cover.

₇.4. COMPLETENESS AND COMPACTNESS_

283

**==> picture [231 x 114] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐵 ( 𝑦, [1] / 𝑛 )<br>𝑦<br>𝑥<br>𝜖 𝜖 /2 𝐵 ( 𝑦, [𝜖] /2)<br>𝑈𝜆<br>𝐵 ( 𝑥, 𝜖 ) 𝐵 ( 𝑥, [𝜖] /2)<br>**----- End of picture text -----**<br>


**Figure 7.12:** Proof of Lebesgue covering lemma. Note that _𝐵_ ( _𝑦,[𝜖]_ /2) ⊂ _𝐵_ ( _𝑥, 𝜖_ ) by triangle inequality.

_Proof._ Claim: _Let 𝐾_ ⊂ _𝑋 be a subset of 𝑋 and_ { _𝑥𝑛_ }[∞] _𝑛_ =1 _[a sequence in][ 𝐾][.][Suppose that for each] 𝑥_ ∈ _𝐾, there is a ball 𝐵_ ( _𝑥, 𝛼𝑥_ ) _for some 𝛼𝑥 >_ 0 _such that 𝑥𝑛_ ∈ _𝐵_ ( _𝑥, 𝛼𝑥_ ) _for only finitely many 𝑛_ ∈ ℕ _. Then 𝐾 is not compact._

Proof of the claim: Notice

**==> picture [88 x 29] intentionally omitted <==**

Any finite collection of these balls contains at most finitely many elements of { _𝑥𝑛_ }[∞] _𝑛_ =1[, and] so there must be an _𝑥𝑛_ ∈ _𝐾_ not in their union. Hence, _𝐾_ is not compact and the claim is proved.

So suppose that _𝐾_ is compact and { _𝑥𝑛_ }[∞] _𝑛_ =1[is][a][sequence][in] _[𝐾]_[.][Then][there][exists][an] _𝑥_ ∈ _𝐾_ such that for all _𝛿>_ 0, _𝐵_ ( _𝑥, 𝛿_ ) contains _𝑥𝑛_ for infinitely many _𝑛_ ∈ ℕ. We define the subsequence inductively. The ball _𝐵_ ( _𝑥,_ 1) contains some _𝑥𝑘_ , so let _𝑛_ 1 � _𝑘_ . Suppose _𝑛𝑗_ −1 is defined. There must exist a _𝑘 > 𝑛𝑗_ −1 such that _𝑥𝑘_ ∈ _𝐵_ ( _𝑥,_[1] / _𝑗_ ). Define _𝑛𝑗_ � _𝑘_ . We now posses a subsequence { _𝑥𝑛𝑗_ }[∞] _𝑗_ =1[.][Since] _[ 𝑑]_[(] _[𝑥, 𝑥][𝑛][𝑗]_[)] _[ <]_[1][/] _[𝑗]_[,] says lim _𝑗_ →∞ _𝑥𝑛𝑗_ = _𝑥_ .

For the other direction, suppose every sequence in _𝐾_ has a subsequence converging in _𝐾_ . Take an open cover { _𝑈𝜆_ } _𝜆_ ∈ _𝐼_ of _𝐾_ . Using the Lebesgue covering lemma above, find a _𝛿>_ 0 such that for every _𝑥_ ∈ _𝐾_ , there is a _𝜆_ ∈ _𝐼_ with _𝐵_ ( _𝑥, 𝛿_ ) ⊂ _𝑈𝜆_ .

Pick _𝑥_ 1 ∈ _𝐾_ and find _𝜆_ 1 ∈ _𝐼_ such that _𝐵_ ( _𝑥_ 1 _, 𝛿_ ) ⊂ _𝑈𝜆_ 1. If _𝐾_ ⊂ _𝑈𝜆_ 1, we stop as we have found a finite subcover. Otherwise, there must be a point _𝑥_ 2 ∈ _𝐾_ \ _𝑈𝜆_ 1. Note that _𝑑_ ( _𝑥_ 2 _, 𝑥_ 1) ≥ _𝛿_ . There must exist some _𝜆_ 2 ∈ _𝐼_ such that _𝐵_ ( _𝑥_ 2 _, 𝛿_ ) ⊂ _𝑈𝜆_ 2. We work inductively. Suppose _𝜆𝑛_ −1 is defined. Either _𝑈𝜆_ 1 ∪ _𝑈𝜆_ 2 ∪· · · ∪ _𝑈𝜆𝑛_ −1 is a finite cover of _𝐾_ , in which case we stop, or there must be a point _𝑥𝑛_ ∈ _𝐾_$$�] _𝑈𝜆_ 1 ∪ _𝑈𝜆_ 2 ∪· · · ∪ _𝑈𝜆𝑛_ −1�. Note that _𝑑_ ( _𝑥𝑛 , 𝑥 𝑗_ ) ≥ _𝛿_ for all _𝑗_ = 1 _,_ 2 _, . . . , 𝑛_ − 1. Next, there must be some _𝜆𝑛_ ∈ _𝐼_ such that _𝐵_ ( _𝑥𝑛 , 𝛿_ ) ⊂ _𝑈𝜆𝑛_ . See .

_𝐾_ Either at some point we obtain a finite subcover of , or we obtain an infinite sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[as][above.][For][contradiction,][suppose][that][there][is][no][finite][subcover][and][we] have the sequence { _𝑥𝑛_ }[∞] _𝑛_ =1[.] For all _𝑛_ and _𝑘_ , _𝑛_ ≠ _𝑘_ , we have _𝑑_ ( _𝑥𝑛 , 𝑥𝑘_ ) ≥ _𝛿_ . So no subsequence of { _𝑥𝑛_ }[∞] _𝑛_ =1[is Cauchy.][Hence, no subsequence of][ {] _[𝑥][𝑛]_[}][∞] _𝑛_ =1[is convergent, which] is a contradiction. □

_CHAPTER 7. METRIC SPACES_

284

**==> picture [283 x 118] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑈𝜆 3<br>𝛿 𝑥 2 𝑥 4<br>𝑥 3 𝐾<br>𝑈𝜆 1 𝑥 1<br>𝑈𝜆 2<br>**----- End of picture text -----**<br>


**Figure 7.13:** Covering _𝐾_ by _𝑈𝜆_ . The points _𝑥_ 1 _, 𝑥_ 2 _, 𝑥_ 3 _, 𝑥_ 4, the three sets _𝑈𝜆_ 1, _𝑈𝜆_ 2, _𝑈𝜆_ 2, and the first three balls of radius _𝛿_ are drawn.