Proposition 7.2.6

**Proposition 7.2.6.** _Let_ ( _𝑋, 𝑑_ ) _be a metric space._

- _(i)_ ∅ _and 𝑋 are open._

- _(ii) If 𝑉_ 1 _, 𝑉_ 2 _, . . . , 𝑉𝑘 are open subsets of 𝑋, then_

**==> picture [30 x 39] intentionally omitted <==**

_is also open. That is, a finite intersection of open sets is open._

- _(iii) If_ { _𝑉𝜆_ } _𝜆_ ∈ _𝐼 is an arbitrary collection of open subsets of 𝑋, then_

**==> picture [32 x 28] intentionally omitted <==**

_is also open. That is, a union of open sets is open._

The index set _𝐼_ in can be arbitrarily large. By[�] _𝜆_ ∈ _𝐼[𝑉][𝜆]_[, we simply mean the set of] all _𝑥_ such that _𝑥_ ∈ _𝑉𝜆_ for at least one _𝜆_ ∈ _𝐼_ .

_Proof._ The sets ∅ and _𝑋_ are obviously open in _𝑋_ .

Let us prove . If _𝑥_ ∈[�] _[𝑘] 𝑗_ =1 _[𝑉][𝑗]_[,][then] _[𝑥]_[∈] _[𝑉][𝑗]_[for all] _[𝑗]_[.][As] _[ 𝑉][𝑗]_[are all open,][for every] _[𝑗]_ there exists a _𝛿 𝑗 >_ 0 such that _𝐵_ ( _𝑥, 𝛿 𝑗_ ) ⊂ _𝑉𝑗_ . Take _𝛿_ � min{ _𝛿_ 1 _, 𝛿_ 2 _, . . . , 𝛿𝑘_ } and notice _𝛿>_ 0.

_CHAPTER 7. METRIC SPACES_

266

We have _𝐵_ ( _𝑥, 𝛿_ ) ⊂ _𝐵_ ( _𝑥, 𝛿 𝑗_ ) ⊂ _𝑉𝑗_ for every _𝑗_ and so _𝐵_ ( _𝑥, 𝛿_ ) ⊂[�] _[𝑘] 𝑗_ =1 _[𝑉][𝑗]_[.][Consequently the] intersection is open.

Let us prove . If _𝑥_ ∈[�] _𝜆_ ∈ _𝐼[𝑉][𝜆]_[, then] _[ 𝑥]_[∈] _[𝑉][𝜆]_[for some] _[ 𝜆]_[∈] _[𝐼]_[.][As] _[ 𝑉][𝜆]_[is open, there exists] a _𝛿>_ 0 such that _𝐵_ ( _𝑥, 𝛿_ ) ⊂ _𝑉𝜆_ . But then _𝐵_ ( _𝑥, 𝛿_ ) ⊂[�] _𝜆_ ∈ _𝐼[𝑉][𝜆]_[, and so the union is open.] □ **Example 7.2.7:** Notice the difference between items and . Item is not true for an arbitrary intersection. For instance,[�][∞] _𝑛_ =1[(][−][1][/] _[𝑛][,]_[ 1][/] _[𝑛]_[)][ =][ {][0][}][, which is not open.]

The proof of the following analogous proposition for closed sets is left as an exercise. **Proposition 7.2.8.** _Let_ ( _𝑋, 𝑑_ ) _be a metric space._

- _(i)_ ∅ _and 𝑋 are closed._

- _(ii) If_ { _𝐸𝜆_ } _𝜆_ ∈ _𝐼 is an arbitrary collection of closed subsets of 𝑋, then_

**==> picture [32 x 28] intentionally omitted <==**

_is also closed. That is, an intersection of closed sets is closed._

_(iii) If 𝐸_ 1 _, 𝐸_ 2 _, . . . , 𝐸𝑘 are closed subsets of 𝑋, then_

**==> picture [30 x 40] intentionally omitted <==**

_is also closed. That is, a finite union of closed sets is closed._

Despite the naming, we have not yet shown that the open ball is open and the closed ball is closed. Let us show these facts now to justify the terminology.