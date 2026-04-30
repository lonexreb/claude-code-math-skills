Proposition 7.4.9

**Proposition 7.4.9.** _Let_ ( _𝑋, 𝑑_ ) _be a metric space. If 𝐾_ ⊂ _𝑋 is compact, then 𝐾 is closed and bounded._

₇.4. COMPLETENESS AND COMPACTNESS_

281

Fix ∈ _𝑋_ . _Proof._ First, we prove that a compact set is bounded. _𝑝_ We have the open cover

**==> picture [106 x 36] intentionally omitted <==**

If _𝐾_ is compact, then there exists some set of indices _𝑛_ 1 _< 𝑛_ 2 _< . . . < 𝑛𝑚_ such that

**==> picture [144 x 38] intentionally omitted <==**

As _𝐾_ is contained in a ball, _𝐾_ is bounded. See the left-hand side of .

Next, we show a set that is not closed is not compact. Suppose _𝐾_ ≠ _𝐾_ , that is, there is a point _𝑥_ ∈ _𝐾_ \ _𝐾_ . If _𝑦_ ≠ _𝑥_ , then _𝑦_ ∉ _𝐶_ ( _𝑥,_[1] / _𝑛_ ) for _𝑛_ ∈ ℕ such that[1] / _𝑛 < 𝑑_ ( _𝑥, 𝑦_ ). Furthermore, _𝑥_ ∉ _𝐾_ , so

**==> picture [94 x 35] intentionally omitted <==**

A closed ball is closed, so its complement _𝐶_ ( _𝑥,_[1] / _𝑛_ ) _[𝑐]_ is open, and we have an open cover. If we take any finite collection of indices _𝑛_ 1 _< 𝑛_ 2 _< . . . < 𝑛𝑚_ , then

**==> picture [137 x 37] intentionally omitted <==**

As _𝑥_ is in the closure of _𝐾_ , then _𝐶_ ( _𝑥,_[1] / _𝑛𝑚_ ) ∩ _𝐾_ ≠ ∅. So there is no finite subcover and _𝐾_ is . □ not compact. See the right-hand side of

**==> picture [377 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐾 𝐶 ( 𝑥, [1] /4)<br>𝐾<br>2<br>1<br>3 𝐶 ( 𝑥, [1] /3)<br>𝑝 𝑥<br>𝐵 ( 𝑝,  2) 𝐶 ( 𝑥, [1] /2)<br>𝐶 ( 𝑥,  1)<br>𝐵 ( 𝑝,  3) 𝐵 ( 𝑝,  1)<br>**----- End of picture text -----**<br>


**Figure 7.11:** Proving compact set is bounded (left) and closed (right).

We prove below that in a finite-dimensional euclidean space, every closed bounded set is compact. So closed bounded sets of ℝ _[𝑛]_ are examples of compact sets. It is not true that in every metric space, closed and bounded is equivalent to compact. A simple example is an incomplete metric space such as (0 _,_ 1) with the subspace metric from ℝ. There are

_CHAPTER 7. METRIC SPACES_

282

many complete and very useful metric spaces where closed and bounded is not enough to give compactness: _𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] is a complete metric space, but the closed unit ball _𝐶_ (0 _,_ 1) is not compact, see . However, see also .

Not worrying about the boundedness for a moment, note further the difference between being closed and being compact. Being closed depends on the ambient metric space: The set (0 _,_ 1] is not closed in ℝ, but it is closed in the subspace (0 _,_ ∞). However, a set _𝐾_ is compact in some metric space ( _𝑋, 𝑑_ ) if and only if it is compact in the subspace metric on _𝐾_ . So for a compact set, we do not have to ask what metric space it lives in. On the other hand, every set is always closed in the subspace metric as a subset of itself. See also .

A useful property of compact sets in a metric space is that every sequence in the set has a convergent subsequence converging to a point in the set. Such sets are called _sequentially_ . _compact_ We will prove that in the context of metric spaces, a set is compact if and only if it is sequentially compact. First we prove a lemma.

**Lemma 7.4.10** (Lebesgue covering lemma ) **.** _Let_ ( _𝑋, 𝑑_ ) _be a metric space and 𝐾_ ⊂ _𝑋. Suppose every sequence in 𝐾 has a subsequence convergent in 𝐾. Given an open cover_ { _𝑈𝜆_ } _𝜆_ ∈ _𝐼 of 𝐾, there exists a 𝛿>_ 0 _such that for every 𝑥_ ∈ _𝐾, there exists a 𝜆_ ∈ _𝐼 with 𝐵_ ( _𝑥, 𝛿_ ) ⊂ _𝑈𝜆._

> _Proof._ We prove the lemma by contrapositive. If the conclusion is not true, then there is an open cover { _𝑈𝜆_ } _𝜆_ ∈ _𝐼_ of _𝐾_ with the following property. For every _𝑛_ ∈ ℕ, there exists an _𝑥𝑛_ ∈ _𝐾_ such that _𝐵_ ( _𝑥𝑛 ,_[1] / _𝑛_ ) is not a subset of any _𝑈𝜆_ . Take any _𝑥_ ∈ _𝐾_ . There is a _𝜆_ ∈ _𝐼_ such that _𝑥_ ∈ _𝑈𝜆_ . As _𝑈𝜆_ is open, there is an _𝜖>_ 0 such that _𝐵_ ( _𝑥, 𝜖_ ) ⊂ _𝑈𝜆_ . Take _𝑀_ such that 1/ _𝑀 < 𝜖_ /2. If _𝑦_ ∈ _𝐵_ ( _𝑥, 𝜖_ /2) and _𝑛_ ≥ _𝑀_ , then

**==> picture [246 x 14] intentionally omitted <==**

where _𝐵_ ( _𝑦,[𝜖]_ /2) ⊂ _𝐵_ ( _𝑥, 𝜖_ ) follows by triangle inequality. See . Thus _𝑦_ ≠ _𝑥𝑛_ . In other words, for all _𝑛_ ≥ _𝑀_ , _𝑥𝑛_ ∉ _𝐵_ ( _𝑥,[𝜖]_ /2). The sequence cannot have a subsequence converging to _𝑥_ . As _𝑥_ ∈ _𝐾_ was arbitrary we are done. □

It is important to recognize what the lemma says. It says that if _𝐾_ is sequentially compact, then given any cover there is a single _𝛿>_ 0. The _𝛿_ depends on the cover, but, of course, it does not depend on _𝑥_ .

For example, let _𝐾_ � [−10 _,_ 10] and let _𝑈𝑛_ � ( _𝑛, 𝑛_ + 2) for _𝑛_ ∈ ℤ give an open cover. Consider _𝑥_ ∈ _𝐾_ . There is an _𝑛_ ∈ ℤ, such that _𝑛_ ≤ _𝑥 < 𝑛_ + 1. If _𝑛_ ≤ _𝑥 < 𝑛_ +[1] /2, then _𝐵_[�] _𝑥,_[1] /2[�] ⊂ _𝑈𝑛_ −1. If _𝑛_ +[1] /2 ≤ _𝑥 < 𝑛_ + 1, then _𝐵_[�] _𝑥,_[1] /2[�] ⊂ _𝑈𝑛_ . So _𝛿_ =[1] /2 will do. The sets _𝑈𝑛_[′][�][�] _[𝑛]_ 2 _[,][𝑛]_[+] 2[2] �, again give an open cover, but now the largest _𝛿_ that works is[1] /4. On the other hand, ℕ ⊂ ℝ is not sequentially compact. It is an exercise to find a cover for which no _𝛿>_ 0 works.