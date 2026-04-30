Proposition 1.4.1

**Proposition 1.4.1.** _A set 𝐼_ ⊂ ℝ _is an interval if and only if 𝐼 contains at least 2 points and for all 𝑎, 𝑐_ ∈ _𝐼 and 𝑏_ ∈ ℝ _such that 𝑎 < 𝑏 < 𝑐, we have 𝑏_ ∈ _𝐼._

We have already seen that every open interval ( _𝑎, 𝑏_ ) (where _𝑎 < 𝑏_ of course) must be nonempty. For example, it contains the number _[𝑎]_[+] 2 _[𝑏]_[.][An unexpected fact is that from a] set-theoretic perspective, all intervals have the same “size,” that is, they all have the same cardinality. For instance, the map _𝑓_ ( _𝑥_ ) � 2 _𝑥_ takes the interval [0 _,_ 1] bĳectively to the interval [0 _,_ 2].

Maybe more interestingly, the function _𝑓_ ( _𝑥_ ) � tan( _𝑥_ ) is a bĳective map from (− _[𝜋]_ /2 _,[𝜋]_ /2) to ℝ. Hence the bounded interval (− _[𝜋]_ /2 _,[𝜋]_ /2) has the same cardinality as ℝ. It is not completely straightforward to construct a bĳective map from [0 _,_ 1] to (0 _,_ 1), but it is possible.

And do not there does exist a to measure the “size” of subsets of real worry, way numbers that “sees” the difference between [0 _,_ 1] and [0 _,_ 2]. However, its proper definition requires much more machinery than we have right now.

‗Sometimes single point sets and the empty set are also called intervals, but in this book, intervals have at least 2 points. That is, we only defined the bounded intervals if _𝑎 < 𝑏_ .

_CHAPTER 1. REAL NUMBERS_

42

ℝ. Let us say more about the cardinality of intervals and hence about the cardinality of We have seen that there exist irrational numbers, that is ℝ \ ℚ, is nonempty. The question is: How many irrational numbers are there? It turns out there are a lot more irrational numbers than rational numbers. We have seen that ℚ is countable, and we will show that ℝ is uncountable. In fact, the cardinality of ℝ is the same as the cardinality of _P_ (ℕ), although we will not prove this claim here.

**Theorem 1.4.2** (Cantor) **.** ℝ _is uncountable._

We give a version of Cantor’s original proof from 1874 as this proof requires the least setup. Normally this proof is stated as a contradiction, but a proof by contrapositive is easier to understand.

> _Proof._ Let _𝑋_ ⊂ ℝ be a countably infinite subset such that for every pair of real numbers _𝑎 < 𝑏_ , there is an _𝑥_ ∈ _𝑋_ such that _𝑎 < 𝑥 < 𝑏_ . Were ℝ countable, we could take _𝑋_ = ℝ. We will show that _𝑋_ is necessarily a proper subset, and so _𝑋_ cannot equal ℝ, and ℝ must be uncountable.

As _𝑋_ is countably infinite, there is a bĳection from ℕ to _𝑋_ . We write _𝑋_ as a sequence of real numbers _𝑥_ 1 _, 𝑥_ 2 _, 𝑥_ 3 _, . . ._ , such that each number in _𝑋_ is given by _𝑥𝑛_ for some _𝑛_ ∈ ℕ.

We inductively construct two sequences of real numbers _𝑎_ 1 _, 𝑎_ 2 _, 𝑎_ 3 _, . . ._ and _𝑏_ 1 _, 𝑏_ 2 _, 𝑏_ 3 _, . . ._ . Let _𝑎_ 1 � _𝑥_ 1 and _𝑏_ 1 � _𝑥_ 1 + 1. Note that _𝑎_ 1 _< 𝑏_ 1 and _𝑥_ 1 ∉ ( _𝑎_ 1 _, 𝑏_ 1). For some _𝑘 >_ 1, suppose _𝑎_ 1 _, 𝑎_ 2 _, . . . , 𝑎𝑘_ −1 and _𝑏_ 1 _, 𝑏_ 2 _, . . . , 𝑏𝑘_ −1 have been defined, suppose _𝑎_ 1 _< 𝑎_ 2 _<_ · · · _< 𝑎𝑘_ −1 _< 𝑏𝑘_ −1 _<_ · · · _< 𝑏_ 2 _< 𝑏_ 1, and suppose for each _𝑗_ = 1 _,_ 2 _, . . . , 𝑘_ − 1, we have _𝑥ℓ_ ∉ ( _𝑎 𝑗 , 𝑏 𝑗_ ) for _ℓ_ = 1 _,_ 2 _, . . . , 𝑗_ .

- (i) Define _𝑎𝑘_ � _𝑥𝑛_ , where _𝑛_ is the smallest _𝑛_ ∈ ℕ such that _𝑥𝑛_ ∈( _𝑎𝑘_ −1 _, 𝑏𝑘_ −1). Such an _𝑥𝑛_ exists by our assumption on _𝑋_ , and _𝑛_ ≥ _𝑘_ by the assumption on ( _𝑎𝑘_ −1 _, 𝑏𝑘_ −1).

- (ii) Next, define _𝑏𝑘_ to be some real number in ( _𝑎𝑘 , 𝑏𝑘_ −1).

Notice that _𝑎𝑘_ −1 _< 𝑎𝑘 < 𝑏𝑘 < 𝑏𝑘_ −1. Also notice that ( _𝑎𝑘 , 𝑏𝑘_ ) does not contain _𝑥𝑘_ and hence

- does not contain _𝑥 𝑗_ for _𝑗_ = 1 _,_ 2 _, . . . , 𝑘_ . The two sequences are now defined. Claim: _𝑎𝑛 < 𝑏𝑚 for all 𝑛 and 𝑚 in_ ℕ _._ Proof: Let us first assume _𝑛 < 𝑚_ . Then

- _𝑎𝑛 < 𝑎𝑛_ +1 _<_ · · · _< 𝑎𝑚_ −1 _< 𝑎𝑚 < 𝑏𝑚_ . Similarly for _𝑛 > 𝑚_ . The claim follows. Let _𝐴_ � { _𝑎𝑛_ : _𝑛_ ∈ ℕ} and _𝐵_ � { _𝑏𝑛_ : _𝑛_ ∈ ℕ}. By and the claim above,

## sup _𝐴_ ≤ inf _𝐵._

Define _𝑦_ � sup _𝐴_ . The number _𝑦_ cannot be a member of _𝐴_ : If _𝑦_ = _𝑎𝑛_ for some _𝑛_ , then _𝑦 < 𝑎𝑛_ +1, which is impossible. Similarly, _𝑦_ cannot be a member of _𝐵_ . Therefore, _𝑎𝑛 < 𝑦_ for all _𝑛_ ∈ ℕ and _𝑦 < 𝑏𝑛_ for all _𝑛_ ∈ ℕ. In other words, for every _𝑛_ ∈ ℕ, we have _𝑦_ ∈( _𝑎𝑛 , 𝑏𝑛_ ). By the construction of the sequence, _𝑥𝑛_ ∉ ( _𝑎𝑛 , 𝑏𝑛_ ), and so _𝑦_ ≠ _𝑥𝑛_ . As this was true for all _𝑛_ ∈ ℕ, we have that _𝑦_ ∉ _𝑋_ .

- We have constructed a real number _𝑦_ that is not in _𝑋_ , and thus _𝑋_ is a proper subset of

- ℝ. The sequence _𝑥_ 1 _, 𝑥_ 2 _, . . ._ cannot contain all elements of ℝ and thus ℝ is uncountable. □

43

## _1.4. INTERVALS AND THE SIZE OF_ ℝ

## **1.4.1 Exercises**

_**Exercise**_ **1.4.1** _**:** For 𝑎 < 𝑏, construct an explicit bĳection from_ ( _𝑎, 𝑏_ ] _to_ (0 _,_ 1] _._

_**Exercise**_ **1.4.2** _**:** Suppose 𝑓_ : [0 _,_ 1] →(0 _,_ 1) _is a bĳection. Using 𝑓 , construct a bĳection from_ [−1 _,_ 1] _to_ ℝ _._

_**Exercise**_ **1.4.3** _**:** Prove . That is, suppose 𝐼_ ⊂ ℝ _is a subset with at least 2 elements such that if 𝑎 < 𝑏 < 𝑐 and 𝑎, 𝑐_ ∈ _𝐼, then 𝑏_ ∈ _𝐼. Prove that 𝐼 is one of the nine types of intervals explicitly given in this section. Furthermore, prove that the intervals given in this section all satisfy this property._

_**Exercise**_ **1.4.4** (Hard) _**:** Construct an explicit bĳection from_ (0 _,_ 1] _to_ (0 _,_ 1) _. Hint: One approach is as follows: First map_ ([1] /2 _,_ 1] _to_ (0 _,_[1] /2] _, then map_ ([1] /4 _,_[1] /2] _to_ ([1] /2 _,_[3] /4] _, etc. Write down the map explicitly, that is, write down an algorithm that tells you exactly what number goes where. Then prove that the map is a bĳection._

_**Exercise**_ **1.4.5** (Hard) _**:** Construct an explicit bĳection from_ [0 _,_ 1] _to_ (0 _,_ 1) _._

## _**Exercise**_ **1.4.6** _**:**_

- _a) Show that every closed interval_ [ _𝑎, 𝑏_ ] _is the intersection of countably many open intervals._

- _b) Show that every open interval_ ( _𝑎, 𝑏_ ) _is a countable union of closed intervals._

- _c) Show that an intersection of a possibly infinite family of bounded closed intervals,_[�] [ _𝑎𝜆, 𝑏𝜆_ ] _, is either 𝜆_ ∈ _𝐼_

- _empty, a single point, or a bounded closed interval._

_**Exercise**_ **1.4.7** _**:** Suppose 𝑆 is a set of disjoint open intervals in_ ℝ _. That is, if_ ( _𝑎, 𝑏_ ) ∈ _𝑆 and_ ( _𝑐, 𝑑_ ) ∈ _𝑆, then either_ ( _𝑎, 𝑏_ ) = ( _𝑐, 𝑑_ ) _or_ ( _𝑎, 𝑏_ ) ∩( _𝑐, 𝑑_ ) = ∅ _. Prove 𝑆 is a countable set._

_**Exercise**_ **1.4.8** _**:** Prove that the cardinality of_ [0 _,_ 1] _is the same as the cardinality of_ (0 _,_ 1) _by showing that_ |[0 _,_ 1]| ≤|(0 _,_ 1)| _and_ |(0 _,_ 1)| ≤|[0 _,_ 1]| _. See . This proof requires the Cantor–Bernstein– Schröder theorem, which we stated without proof. Note that this proof does not give you an explicit bĳection._

_**Exercise**_ **1.4.9** (Challenging) _**:** A number 𝑥 is_ algebraic _if 𝑥 is a root of a polynomial with integer coefficients, in other words, 𝑎𝑛 𝑥[𝑛]_ + _𝑎𝑛_ −1 _𝑥[𝑛]_[−][1] + · · · + _𝑎_ 1 _𝑥_ + _𝑎_ 0 = 0 _where 𝑎_ 0 _, 𝑎_ 1 _, . . . , 𝑎𝑛_ ∈ ℤ _._

- _a) Show that there are only countably many algebraic numbers._

- _b) Show that there exist non-algebraic (transcendental) numbers (follow in the footsteps of Cantor, use the uncountability of_ ℝ _)._

_Hint: Feel free to use the fact that a polynomial of degree 𝑛 has at most 𝑛 real roots._

_**Exercise**_ **1.4.10** (Challenging) _**:** Let 𝐹 be the set of all functions 𝑓_ : ℝ → ℝ _. Prove_ |ℝ| _<_ | _𝐹_ | _using Cantor’s ._

> ‗Interestingly, if _𝐶_ is the set of continuous functions, then |ℝ| = | _𝐶_ |.

_CHAPTER 1. REAL NUMBERS_

44

## **1.5 Decimal representation of the reals**

_Note: 1 lecture (optional)_

We often think of real numbers as their _decimal representation_ . By a (decimal) _digit_ , we mean an integer between 0 and 9. For a positive integer _𝑛_ , we find the digits _𝑑𝐾 , 𝑑𝐾_ −1 _, . . . , 𝑑_ 2 _, 𝑑_ 1 _, 𝑑_ 0 for some _𝐾_ (each _𝑑𝑗_ an integer between 0 and 9) such that

**==> picture [254 x 14] intentionally omitted <==**

We often assume _𝑑𝐾_ ≠ 0 (avoiding leading zeros). To represent _𝑛_ , we write the sequence of digits: _𝑛_ = _𝑑𝐾 𝑑𝐾_ −1 · · · _𝑑_ 2 _𝑑_ 1 _𝑑_ 0.

Similarly, we represent some rational numbers. That is, for certain numbers _𝑥_ , we can find a negative integer − _𝑀_ , a positive integer _𝐾_ , and digits _𝑑𝐾 , 𝑑𝐾_ −1 _, . . . , 𝑑_ 1 _, 𝑑_ 0 _, 𝑑_ −1 _, . . . , 𝑑_ − _𝑀_ , such that

**==> picture [450 x 14] intentionally omitted <==**

We write _𝑥_ = _𝑑𝐾 𝑑𝐾_ −1 · · · _𝑑_ 1 _𝑑_ 0 _. 𝑑_ −1 _𝑑_ −2 · · · _𝑑_ − _𝑀_ .

Not every real number has such a representation, even the simple rational number[1] /3 does not. The irrational number √2 does not have such a representation either. To get a representation for all real numbers, we must allow infinitely many digits. Let us consider only real numbers in the interval (0 _,_ 1]. If we find a representation for these, adding integers to them obtains a representation for all real numbers. Take an infinite sequence of decimal digits:

**==> picture [66 x 11] intentionally omitted <==**

That is, we have a digit _𝑑𝑗_ for every _𝑗_ ∈ ℕ. We renumbered the digits to avoid the negative signs. We call the number

**==> picture [178 x 28] intentionally omitted <==**

the truncation of _𝑥_ to _𝑛_ decimal digits. We say this sequence of digits represents a real number _𝑥_ if

**==> picture [252 x 31] intentionally omitted <==**

## **Proposition 1.5.1.**

- _(i) Every infinite sequence of digits_ 0 _.𝑑_ 1 _𝑑_ 2 _𝑑_ 3 _. . . represents a unique real number 𝑥_ ∈[0 _,_ 1] _, and_

**==> picture [192 x 26] intentionally omitted <==**

- _(ii) For every 𝑥_ ∈(0 _,_ 1] _there exists an infinite sequence of digits_ 0 _.𝑑_ 1 _𝑑_ 2 _𝑑_ 3 _. . . that represents 𝑥. There exists a unique representation such that_

**==> picture [191 x 26] intentionally omitted <==**

_1.5. DECIMAL REPRESENTATION OF THE REALS_

45

_Proof._ We start with the first item. Take an arbitrary infinite sequence of digits 0 _.𝑑_ 1 _𝑑_ 2 _𝑑_ 3 _. . ._ . Use the geometric sum formula to write

**==> picture [371 x 91] intentionally omitted <==**

In particular, _𝐷𝑛 <_ 1 for all _𝑛_ . A sum of nonnegative numbers is nonnegative so _𝐷𝑛_ ≥ 0, and hence

**==> picture [86 x 21] intentionally omitted <==**

Therefore, 0 _.𝑑_ 1 _𝑑_ 2 _𝑑_ 3 _. . ._ represents a unique number _𝑥_ � sup _𝑛_ ∈ℕ _𝐷𝑛_ ∈[0 _,_ 1]. As _𝑥_ is a supremum, then _𝐷𝑛_ ≤ _𝑥_ . Take _𝑚_ ∈ ℕ. If _𝑚 < 𝑛_ , then _𝐷𝑚_ − _𝐷𝑛_ ≤ 0. If _𝑚 > 𝑛_ , then computing as above

**==> picture [390 x 29] intentionally omitted <==**

Take the supremum over _𝑚_ to find

**==> picture [76 x 26] intentionally omitted <==**

We move on to the second item. Take any _𝑥_ ∈(0 _,_ 1]. First let us tackle the existence. For convenience, let _𝐷_ 0 � 0. Then, _𝐷_ 0 _< 𝑥_ ≤ _𝐷_ 0 + 10[−][0] . Suppose we defined the digits _𝑑_ 1 _, 𝑑_ 2 _, . . . , 𝑑𝑛_ , and that _𝐷𝑘 < 𝑥_ ≤ _𝐷𝑘_ + 10[−] _[𝑘]_ , for _𝑘_ = 0 _,_ 1 _,_ 2 _, . . . , 𝑛_ . We need to define _𝑑𝑛_ +1. By the of the real numbers, find an integer _𝑗_ such that _𝑥_ − _𝐷𝑛_ ≤ _𝑗_ 10[−(] _[𝑛]_[+][1][)] . Take the least such _𝑗_ and obtain

**==> picture [330 x 16] intentionally omitted <==**

Let _𝑑𝑛_ +1 � _𝑗_ − 1. As _𝐷𝑛 < 𝑥_ , then _𝑑𝑛_ +1 = _𝑗_ − 1 ≥ 0. On the other hand, since _𝑥_ − _𝐷𝑛_ ≤ 10[−] _[𝑛]_ , we have that _𝑗_ is at most 10, and therefore _𝑑𝑛_ +1 ≤ 9. So _𝑑𝑛_ +1 is a decimal digit. Since _𝐷𝑛_ +1 = _𝐷𝑛_ + _𝑑𝑛_ +110[−(] _[𝑛]_[+][1][)] add _𝐷𝑛_ to the inequality ( ) above:

**==> picture [448 x 36] intentionally omitted <==**

And so _𝐷𝑛_ +1 _< 𝑥_ ≤ _𝐷𝑛_ +1 + 10[−(] _[𝑛]_[+][1][)] holds. We inductively defined an infinite sequence of digits 0 _.𝑑_ 1 _𝑑_ 2 _𝑑_ 3 _. . ._ .

Consider _𝐷𝑛 < 𝑥_ ≤ _𝐷𝑛_ + 10[−] _[𝑛]_ . As _𝐷𝑛 < 𝑥_ for all _𝑛_ , then sup{ _𝐷𝑛_ : _𝑛_ ∈ ℕ} ≤ _𝑥_ . The second inequality for _𝐷𝑛_ implies

**==> picture [206 x 14] intentionally omitted <==**

_CHAPTER 1. REAL NUMBERS_

46

As the inequality holds for all _𝑛_ and 10[−] _[𝑛]_ can be made arbitrarily small (see ), we have _𝑥_ ≤ sup{ _𝐷𝑚_ : _𝑚_ ∈ ℕ}. Therefore, sup{ _𝐷𝑚_ : _𝑚_ ∈ ℕ} = _𝑥_ .

What is left to show is the uniqueness. Suppose 0 _.𝑒_ 1 _𝑒_ 2 _𝑒_ 3 _. . ._ is another representation of _𝑥_ . Let _𝐸𝑛_ be the _𝑛_ -digit truncation of 0 _.𝑒_ 1 _𝑒_ 2 _𝑒_ 3 _. . ._ , and suppose _𝐸𝑛 < 𝑥_ ≤ _𝐸𝑛_ + 10[−] _[𝑛]_ for all _𝑛_ ∈ ℕ. Suppose for some _𝐾_ ∈ ℕ, _𝑒𝑛_ = _𝑑𝑛_ for all _𝑛 < 𝐾_ , so _𝐷𝐾_ −1 = _𝐸𝐾_ −1. Then

**==> picture [330 x 14] intentionally omitted <==**

Subtracting _𝐷𝐾_ −1 and multiplying by 10 _[𝐾]_ we get

**==> picture [152 x 15] intentionally omitted <==**

Similarly,

**==> picture [154 x 15] intentionally omitted <==**

Hence, both _𝑒𝐾_ and _𝑑𝐾_ are the largest integer _𝑗_ such that _𝑗 <_ ( _𝑥_ − _𝐷𝐾_ −1)10 _[𝐾]_ , and therefore _𝑒𝐾_ = _𝑑𝐾_ . That is, the representation is unique. □

The representation is not unique if we do not require _𝐷𝑛 < 𝑥_ for all _𝑛_ . For example, for the number[1] /2, the method in the proof obtains the representation

**==> picture [62 x 9] intentionally omitted <==**

However,[1] /2 also has the representation 0 _._ 50000 _. . ._ .

The only numbers that have nonunique representations are ones that end in an infinite sequence of 0s or an infinite sequence of 9s, because the only representation for which _𝐷𝑛_ = _𝑥_ is one where all digits past the _𝑛_ th digit are zero. In this case, there are exactly two representations of _𝑥_ (see the exercises).

Let us give another proof of the uncountability of the reals using decimal representations. This is Cantor’s second which is better known. This seem proof, probably proof may shorter, but it is because we already did the hard part above and we are left with a slick trick to prove that ℝ is uncountable. This trick is called _Cantor diagonalization_ and finds use in other proofs as well.

**Theorem 1.5.2** (Cantor) **.** _The set_ (0 _,_ 1] _is uncountable._

_Proof._ Let _𝑋_ � { _𝑥_ 1 _, 𝑥_ 2 _, 𝑥_ 3 _, . . ._ } be any countable subset of real numbers in (0 _,_ 1]. We will construct a real number not in _𝑋_ . Let

**==> picture [92 x 14] intentionally omitted <==**

be the unique representation from the proposition, that is, _𝑑[𝑛][𝑗]_[th digit of the] _[ 𝑛]_[th] _𝑗_[is the] number. Let

**==> picture [103 x 39] intentionally omitted <==**

_1.5. DECIMAL REPRESENTATION OF THE REALS_

47

Let _𝐸𝑛_ be the _𝑛_ -digit truncation of _𝑦_ = 0 _.𝑒_ 1 _𝑒_ 2 _𝑒_ 3 _. . ._ . Because all the digits are nonzero we get _𝐸𝑛 < 𝐸𝑛_ +1 ≤ _𝑦_ . Therefore,

**==> picture [101 x 13] intentionally omitted <==**

for all _𝑛_ , and the representation is the unique one for _𝑦_ from the proposition. For every _𝑛_ , the _𝑛_ th digit of _𝑦_ is different from the _𝑛_ th digit of _𝑥𝑛_ , so _𝑦_ ≠ _𝑥𝑛_ . Therefore _𝑦_ ∉ _𝑋_ , and as _𝑋_ was an arbitrary countable subset, (0 _,_ 1] must be uncountable. See for an example. □

**==> picture [344 x 98] intentionally omitted <==**

**Figure 1.5:** Example of Cantor diagonalization, the diagonal digits _𝑑𝑛[𝑛]_[marked.]

Using decimal digits we can also find lots of numbers that are not rational. The following proposition is true for every rational number, but we give it only for _𝑥_ ∈(0 _,_ 1] for simplicity.