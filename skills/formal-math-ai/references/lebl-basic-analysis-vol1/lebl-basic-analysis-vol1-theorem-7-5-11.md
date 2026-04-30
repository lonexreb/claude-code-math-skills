Theorem 7.5.11

**Theorem 7.5.11.** _Let_ ( _𝑋, 𝑑𝑋_ ) _and_ ( _𝑌, 𝑑𝑌_ ) _be metric spaces. Suppose 𝑓_ : _𝑋_ → _𝑌 is continuous and 𝑋 is compact. Then 𝑓 is uniformly continuous._

_Proof._ Let _𝜖>_ 0 be given. For each _𝑐_ ∈ _𝑋_ , pick _𝛿𝑐 >_ 0 such that _𝑑𝑌_ � _𝑓_ ( _𝑥_ ) _, 𝑓_ ( _𝑐_ )[�] _<[𝜖]_ /2 whenever _𝑥_ ∈ _𝐵_ ( _𝑐, 𝛿𝑐_ ). The balls _𝐵_ ( _𝑐, 𝛿𝑐_ ) cover _𝑋_ , and the space _𝑋_ is compact. Apply the to obtain a _𝛿>_ 0 such that for every _𝑥_ ∈ _𝑋_ , there is a _𝑐_ ∈ _𝑋_ for which _𝐵_ ( _𝑥, 𝛿_ ) ⊂ _𝐵_ ( _𝑐, 𝛿𝑐_ ).

Suppose _𝑝, 𝑞_ ∈ _𝑋_ where _𝑑𝑋_ ( _𝑝, 𝑞_ ) _< 𝛿_ . Find a _𝑐_ ∈ _𝑋_ such that _𝐵_ ( _𝑝, 𝛿_ ) ⊂ _𝐵_ ( _𝑐, 𝛿𝑐_ ). Then _𝑞_ ∈ _𝐵_ ( _𝑐, 𝛿𝑐_ ). By the triangle inequality and the definition of _𝛿𝑐_ ,

**==> picture [398 x 15] intentionally omitted <==**

As an application of uniform continuity, we prove a useful criterion for continuity of functions defined by integrals. Let _𝑓_ ( _𝑥, 𝑦_ ) be a function of two variables and define

**==> picture [117 x 33] intentionally omitted <==**

Question is, is _𝑔_ is continuous? We are really asking when do two limiting operations commute, which is not always possible, so some extra hypothesis is necessary. A useful sufficient (but not necessary) condition is that _𝑓_ is continuous on a closed rectangle.

_CHAPTER 7. METRIC SPACES_

292