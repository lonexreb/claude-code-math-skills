Example 0.3.3

**Example 0.3.3:** The following are sets including the standard notations.

- (i) The set of _natural numbers_ , ℕ � {1 _,_ 2 _,_ 3 _, . . ._ }.

- (ii) The set of _integers_ , ℤ � {0 _,_ −1 _,_ 1 _,_ −2 _,_ 2 _, . . ._ }.

- (iii) The set of _rational numbers_ , ℚ � � _𝑚𝑛_[:] _[ 𝑚, 𝑛]_[∈][ℤ][and] _[ 𝑛]_[≠][0] �.

- (iv) The set of even natural numbers, {2 _𝑚_ : _𝑚_ ∈ ℕ}.

- (v) The set of real numbers, ℝ.

Note that ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ.

We create new sets out of old ones by applying some natural operations.

_INTRODUCTION_

10

## **Definition 0.3.4.**

- (i) A _union_ of two sets _𝐴_ and _𝐵_ is defined as

**==> picture [156 x 12] intentionally omitted <==**

- (ii) An _intersection_ of two sets _𝐴_ and _𝐵_ is defined as

**==> picture [165 x 12] intentionally omitted <==**

(iii) A _complement of 𝐵 relative to 𝐴_ (or _set-theoretic difference_ of _𝐴_ and _𝐵_ ) is defined as

_𝐴_ \ _𝐵_ � { _𝑥_ : _𝑥_ ∈ _𝐴_ and _𝑥_ ∉ _𝐵_ } _._

- (iv) We say _complement_ of _𝐵_ and write _𝐵[𝑐]_ instead of _𝐴_ \ _𝐵_ if the set _𝐴_ is either the entire universe or if it is the obvious set containing _𝐵_ , and is understood from context.

- (v) We say sets _𝐴_ and _𝐵_ are _disjoint_ if _𝐴_ ∩ _𝐵_ = ∅.

The notation _𝐵[𝑐]_ may be a little vague at this point. If the set _𝐵_ is a subset of the real numbers ℝ, then _𝐵[𝑐]_ means ℝ \ _𝐵_ . If _𝐵_ is naturally a subset of the natural numbers, then _𝐵[𝑐]_ is ℕ \ _𝐵_ . If ambiguity can arise, we use the set difference notation _𝐴_ \ _𝐵_ .

**==> picture [336 x 262] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐴 𝐴<br>𝐵 𝐵<br>𝐴 ∪ 𝐵 𝐴 ∩ 𝐵<br>𝐴 𝐵<br>𝐵<br>𝐴 \  𝐵 𝐵 [𝑐]<br>**----- End of picture text -----**<br>


**Figure 2:** Venn diagrams of set operations, the result of the operation is shaded.

We illustrate the operations on the _Venn diagrams_ in . Let us now establish one of the most basic theorems about sets and logic.

_0.3. BASIC SET THEORY_

11

**Theorem 0.3.5** (DeMorgan) **.** _Let 𝐴, 𝐵, 𝐶 be sets. Then_

**==> picture [230 x 14] intentionally omitted <==**

_or, more generally,_

**==> picture [354 x 13] intentionally omitted <==**

_Proof._ The first statement is proved by the second statement if we assume the set _𝐴_ is our “universe.”

Let us prove _𝐴_ \ ( _𝐵_ ∪ _𝐶_ ) = ( _𝐴_ \ _𝐵_ ) ∩( _𝐴_ \ _𝐶_ ). Remember the definition of equality of sets. First, we must show that if _𝑥_ ∈ _𝐴_ \ ( _𝐵_ ∪ _𝐶_ ), then _𝑥_ ∈( _𝐴_ \ _𝐵_ ) ∩( _𝐴_ \ _𝐶_ ). Second, we must also show that if _𝑥_ ∈( _𝐴_ \ _𝐵_ ) ∩( _𝐴_ \ _𝐶_ ), then _𝑥_ ∈ _𝐴_ \ ( _𝐵_ ∪ _𝐶_ ). So let us assume _𝑥_ ∈ _𝐴_ \ ( _𝐵_ ∪ _𝐶_ ). Then _𝑥_ is in _𝐴_ , but not in _𝐵_ nor _𝐶_ . Hence _𝑥_ is in _𝐴_ and not in _𝐵_ , that is, _𝑥_ ∈ _𝐴_ \ _𝐵_ . Similarly, _𝑥_ ∈ _𝐴_ \ _𝐶_ . Thus _𝑥_ ∈( _𝐴_ \ _𝐵_ ) ∩( _𝐴_ \ _𝐶_ ). On the other hand, suppose _𝑥_ ∈( _𝐴_ \ _𝐵_ ) ∩( _𝐴_ \ _𝐶_ ). In particular, _𝑥_ ∈( _𝐴_ \ _𝐵_ ), so _𝑥_ ∈ _𝐴_ and _𝑥_ ∉ _𝐵_ . Also, as _𝑥_ ∈( _𝐴_ \ _𝐶_ ), then _𝑥_ ∉ _𝐶_ . Hence _𝑥_ ∈ _𝐴_ \ ( _𝐵_ ∪ _𝐶_ ).

The proof of the other equality is left as an exercise. □

The result above we called a _Theorem_ , while most results we call a _Proposition_ , and a few we call a _Lemma_ (a result leading to another result) or _Corollary_ (a quick consequence of the preceding result). Do not read too much into the naming. Some of it is traditional, some of it is stylistic choice. It is not necessarily true that a _Theorem_ is always “more important” than a _Proposition_ or a _Lemma_ .

We will also need to intersect or union several sets at once. If there are only finitely many, then we simply apply the union or intersection operation several times. However, suppose we have an infinite collection of sets (a set of sets) { _𝐴_ 1 _, 𝐴_ 2 _, 𝐴_ 3 _, . . ._ }. We define

**==> picture [202 x 76] intentionally omitted <==**

We can also have sets indexed by two natural numbers. For example, we can have the set of sets { _𝐴_ 1 _,_ 1 _, 𝐴_ 1 _,_ 2 _, 𝐴_ 2 _,_ 1 _, 𝐴_ 1 _,_ 3 _, 𝐴_ 2 _,_ 2 _, 𝐴_ 3 _,_ 1 _, . . ._ }. Then we write

**==> picture [158 x 39] intentionally omitted <==**

And similarly with intersections.

It is not hard to see that we can take the unions in any order. However, switching the order of unions and intersections is not generally permitted without proof. For instance,

**==> picture [190 x 35] intentionally omitted <==**

_INTRODUCTION_

12

However,

**==> picture [198 x 35] intentionally omitted <==**

Sometimes, the index set is not the set of natural numbers. In such a case, we require a more general notation. Suppose _𝐼_ is some set and for each _𝜆_ ∈ _𝐼_ , there is a set _𝐴𝜆_ . Then we define

**==> picture [404 x 29] intentionally omitted <==**

## **0.3.2 Induction**

When a statement includes an arbitrary natural number, a common proof method is the principle of induction. We start with the set of natural numbers ℕ = {1 _,_ 2 _,_ 3 _, . . ._ }, and we give them their natural ordering, that is, 1 _<_ 2 _<_ 3 _<_ 4 _<_ · · · . By _𝑆_ ⊂ ℕ having a _least element_ , we mean that there exists an _𝑥_ ∈ _𝑆_ , such that for every _𝑦_ ∈ _𝑆_ , we have _𝑥_ ≤ _𝑦_ .

The natural numbers ℕ ordered in the natural way possess the so-called _well ordering_ . _property_ We take this property as an axiom; we simply assume it is true.

**Well ordering property of** ℕ **.** _Every nonempty subset of_ ℕ _has a least (smallest) element._

The _principle of induction_ is the following theorem, which is in a sense equivalent to the well ordering property of the natural numbers.

**Theorem 0.3.6** (Principle of induction) **.** _Let 𝑃_ ( _𝑛_ ) _be a statement depending on a natural number 𝑛. Suppose that_

- _(i) (basis statement) 𝑃_ (1) _is true._

- _(ii) (induction step) If 𝑃_ ( _𝑛_ ) _is true, then 𝑃_ ( _𝑛_ + 1) _is true._

_Then 𝑃_ ( _𝑛_ ) _is true for all 𝑛_ ∈ ℕ _._

> _Proof._ Let _𝑆_ be the set of natural numbers _𝑛_ for which _𝑃_ ( _𝑛_ ) is not true. Suppose for contradiction that _𝑆_ is nonempty. Then _𝑆_ has a least element by the well ordering property. Call _𝑚_ ∈ _𝑆_ the least element of _𝑆_ . We know 1 ∉ _𝑆_ by hypothesis. So _𝑚 >_ 1, and _𝑚_ − 1 is a natural number as well. Since _𝑚_ is the least element of _𝑆_ , we know that _𝑃_ ( _𝑚_ − 1) is true. But the induction step says that _𝑃_ ( _𝑚_ − 1 + 1) = _𝑃_ ( _𝑚_ ) is true, contradicting the statement that _𝑚_ ∈ _𝑆_ . Therefore, _𝑆_ is empty and _𝑃_ ( _𝑛_ ) is true for all _𝑛_ ∈ ℕ. □

Sometimes it is convenient to start at a different number than 1, all that changes is the labeling. The assumption that _𝑃_ ( _𝑛_ ) is true in “if _𝑃_ ( _𝑛_ ) is true, then _𝑃_ ( _𝑛_ + 1) is true” is . usually called the _induction hypothesis_

> ‗To be completely rigorous, this equivalence is only true if we also assume as an axiom that _𝑛_ − 1 exists for all natural numbers bigger than 1, which we do. In this book, we are assuming all the usual arithmetic holds.

_0.3. BASIC SET THEORY_

13