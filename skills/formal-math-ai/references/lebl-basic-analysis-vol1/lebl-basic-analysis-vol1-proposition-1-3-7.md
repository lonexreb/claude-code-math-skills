Proposition 1.3.7

**Proposition 1.3.7.** _If 𝑓_ : _𝐷_ → ℝ _and 𝑔_ : _𝐷_ → ℝ _(𝐷 nonempty) are bounded functions and_

_𝑓_ ( _𝑥_ ) ≤ _𝑔_ ( _𝑥_ ) _for all 𝑥_ ∈ _𝐷,_

_then_

**==> picture [374 x 22] intentionally omitted <==**

Be careful with the variables. The _𝑥_ on the left side of the inequality in ( ) is different from the _𝑥_ on the right. You should really think of, say, the first inequality as

**==> picture [108 x 24] intentionally omitted <==**

Let us prove this inequality. If _𝑏_ is an upper bound for _𝑔_ ( _𝐷_ ), then _𝑓_ ( _𝑥_ ) ≤ _𝑔_ ( _𝑥_ ) ≤ _𝑏_ for all _𝑥_ ∈ _𝐷_ , and hence _𝑏_ is also an upper bound for _𝑓_ ( _𝐷_ ), or _𝑓_ ( _𝑥_ ) ≤ _𝑏_ for all _𝑥_ ∈ _𝐷_ . Take the least upper bound of _𝑔_ ( _𝐷_ ) to get that for all _𝑥_ ∈ _𝐷_

**==> picture [85 x 24] intentionally omitted <==**

> ‗The boundedness hypothesis is for simplicity, it can be dropped if we allow for the extended real numbers.

_1.3. ABSOLUTE VALUE AND BOUNDED FUNCTIONS_

39

Therefore, sup _𝑦_ ∈ _𝐷 𝑔_ ( _𝑦_ ) is an upper bound for _𝑓_ ( _𝐷_ ) and thus greater than or equal to the least upper bound of _𝑓_ ( _𝐷_ ).

**==> picture [108 x 24] intentionally omitted <==**

The second inequality (the statement about the inf) is left as an exercise ( ). A common mistake is to conclude

**==> picture [289 x 22] intentionally omitted <==**

The inequality ( ) is not true given the hypothesis of the proposition above. For this stronger inequality we need the stronger hypothesis

**==> picture [209 x 13] intentionally omitted <==**

The proof as well as a counterexample is left as an exercise ( ).

## **1.3.1 Exercises**

_**Exercise**_ **1.3.1** _**:** Show that_ �� _𝑥_ − _𝑦_ �� _< 𝜖 if and only if 𝑥_ − _𝜖< 𝑦 < 𝑥_ + _𝜖._

**==> picture [383 x 19] intentionally omitted <==**

_**Exercise**_ **1.3.3** _**:** Find a number 𝑀 such that_ | _𝑥_[3] − _𝑥_[2] + 8 _𝑥_ | ≤ _𝑀 for all_ −2 ≤ _𝑥_ ≤ 10 _._

_**Exercise**_ **1.3.4** _**:** Finish the proof of . That is, prove that given a set 𝐷, and two bounded functions 𝑓_ : _𝐷_ → ℝ _and 𝑔_ : _𝐷_ → ℝ _such that 𝑓_ ( _𝑥_ ) ≤ _𝑔_ ( _𝑥_ ) _for all 𝑥_ ∈ _𝐷, then_

**==> picture [94 x 17] intentionally omitted <==**

_**Exercise**_ **1.3.5** _**:** Let 𝑓_ : _𝐷_ → ℝ _and 𝑔_ : _𝐷_ → ℝ _be functions (𝐷 nonempty)._

_a) Suppose 𝑓_ ( _𝑥_ ) ≤ _𝑔_ ( _𝑦_ ) _for all 𝑥_ ∈ _𝐷 and 𝑦_ ∈ _𝐷. Show that_

**==> picture [96 x 19] intentionally omitted <==**

_b) Find a specific 𝐷, 𝑓 , and 𝑔, such that 𝑓_ ( _𝑥_ ) ≤ _𝑔_ ( _𝑥_ ) _for all 𝑥_ ∈ _𝐷, but_

**==> picture [96 x 20] intentionally omitted <==**

_**Exercise**_ **1.3.6** _**:** Prove without the assumption that the functions are bounded. Hint: You need to use the extended real numbers._

_**Exercise**_ **1.3.7** _**:** Let 𝐷 be a nonempty set. Suppose 𝑓_ : _𝐷_ → ℝ _and 𝑔_ : _𝐷_ → ℝ _are bounded functions._

_a) Show_

**==> picture [434 x 21] intentionally omitted <==**

_b) Find an example (or examples) where we obtain strict inequalities._

_CHAPTER 1. REAL NUMBERS_

40

- _**Exercise**_ **1.3.8** _**:** Suppose 𝐷 is nonempty, 𝑓_ : _𝐷_ → ℝ _and 𝑔_ : _𝐷_ → ℝ _are bounded functions, and 𝛼_ ∈ ℝ _._

- _a) Show that 𝛼 𝑓_ : _𝐷_ → ℝ _defined by_ ( _𝛼 𝑓_ )( _𝑥_ ) � _𝛼 𝑓_ ( _𝑥_ ) _is a bounded function._

- _b) Show that 𝑓_ + _𝑔_ : _𝐷_ → ℝ _defined by_ ( _𝑓_ + _𝑔_ )( _𝑥_ ) � _𝑓_ ( _𝑥_ ) + _𝑔_ ( _𝑥_ ) _is a bounded function._

- _**Exercise**_ **1.3.9** _**:** Let 𝑓_ : _𝐷_ → ℝ _and 𝑔_ : _𝐷_ → ℝ _be functions with 𝐷 nonempty, 𝛼_ ∈ ℝ _, and recall what 𝑓_ + _𝑔 and 𝛼 𝑓 means from the previous exercise._

- _a) Prove that if 𝑓_ + _𝑔 and 𝑔 are bounded, then 𝑓 is bounded._

- _b) Find an example where 𝑓 and 𝑔 are both unbounded, but 𝑓_ + _𝑔 is bounded._

- _c) Prove that if 𝑓 is bounded but 𝑔 is unbounded, then 𝑓_ + _𝑔 is unbounded._

- _d) Find an example where 𝑓 is unbounded but 𝛼 𝑓 is bounded._

_1.4. INTERVALS AND THE SIZE OF_ ℝ

41

## **1.4 Intervals and the size of** ℝ

_Note: 0.5–1 lecture (proof of uncountability of_ ℝ _can be optional)_

You surely saw the notation for intervals before, but let us give a formal definition here. For _𝑎, 𝑏_ ∈ ℝ such that _𝑎 < 𝑏_ , we define

**==> picture [150 x 67] intentionally omitted <==**

The interval [ _𝑎, 𝑏_ ] is called a _closed interval_ and ( _𝑎, 𝑏_ ) is called an _open interval_ . The intervals of the form ( _𝑎, 𝑏_ ] and [ _𝑎, 𝑏_ ) are called _half-open intervals_ .

The intervals above are _bounded intervals_ , since both _𝑎_ and _𝑏_ are real numbers. We define _unbounded intervals_ ,

**==> picture [141 x 67] intentionally omitted <==**

For completeness, we define (−∞ _,_ ∞) � ℝ. The intervals [ _𝑎,_ ∞), (−∞ _, 𝑏_ ], and ℝ are sometimes called _unbounded closed intervals_ , and ( _𝑎,_ ∞), (−∞ _, 𝑏_ ), and ℝ are sometimes called . _unbounded open intervals_

The proof of the following proposition is left as an exercise. In short, an interval is a set with at least two points that contains all points between any two points.