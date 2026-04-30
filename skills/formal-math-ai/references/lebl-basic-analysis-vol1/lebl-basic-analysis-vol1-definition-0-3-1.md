Definition 0.3.1

**Definition 0.3.1.** A _set_ is a collection of objects called _elements_ or _members_ . A set with no objects is called the _empty set_ and is denoted by ∅ (or sometimes by {}).

Think of a set as a club with a certain membership. For example, the students who play chess are members of the chess club. The same student can be a member of many different clubs. However, do not take the analogy too far. A set is only defined by the members that form the set; two sets that have the same members are the same set.

Most of the time, we will consider sets of numbers. For example, the set

**==> picture [66 x 12] intentionally omitted <==**

is the set containing the three elements 0, 1, and 2. By “�”, we mean we are defining what _𝑆_ is, rather than just showing equality. We write

**==> picture [28 x 10] intentionally omitted <==**

to denote that the number 1 belongs to the set _𝑆_ . That is, 1 is a member of _𝑆_ . At times we want to say that two elements are in a set _𝑆_ , so we write “1 _,_ 2 ∈ _𝑆_ ” as a shorthand for “1 ∈ _𝑆_ and 2 ∈ _𝑆_ .”

Similarly, we write

**==> picture [27 x 11] intentionally omitted <==**

to denote that the number 7 is not in _𝑆_ . That is, 7 is not a member of _𝑆_ .

The elements of all sets under consideration come from some set we call the _universe_ . For simplicity, we often consider the universe to be the set that contains only the elements we are interested in. The universe is generally understood from context and is not explicitly mentioned. In this course, our universe will often be the set of real numbers.

Although the elements of a set are often numbers, other objects, such as other sets, can be elements of a set. A set may also contain some of the same elements as another set. For example,

**==> picture [56 x 12] intentionally omitted <==**

contains the numbers 0 and 2. In this case, all elements of _𝑇_ also belong to _𝑆_ . We write _𝑇_ ⊂ _𝑆_ . See for a diagram.

> ‗The term “modern” refers to the late 19th century up to the present.

_0.3. BASIC SET THEORY_

9

**==> picture [185 x 59] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑆<br>0<br>1<br>7<br>𝑇<br>2<br>**----- End of picture text -----**<br>


**Figure 1:** A diagram of the example sets _𝑆_ and its subset _𝑇_ .

## **Definition 0.3.2.**

- (i) A set _𝐴_ is a _subset_ of a set _𝐵_ if _𝑥_ ∈ _𝐴_ implies _𝑥_ ∈ _𝐵_ , and we write _𝐴_ ⊂ _𝐵_ . That is, all members of _𝐴_ are also members of _𝐵_ . At times we write _𝐵_ ⊃ _𝐴_ to mean the same thing.

- (ii) Two sets _𝐴_ and _𝐵_ are _equal_ if _𝐴_ ⊂ _𝐵_ and _𝐵_ ⊂ _𝐴_ . We write _𝐴_ = _𝐵_ . That is, _𝐴_ and _𝐵_ contain exactly the same elements. If it is not true that _𝐴_ and _𝐵_ are equal, then we write _𝐴_ ≠ _𝐵_ .

- (iii) A set _𝐴_ is a _proper subset_ of _𝐵_ if _𝐴_ ⊂ _𝐵_ and _𝐴_ ≠ _𝐵_ . We write _𝐴_ ⊊ _𝐵_ .

For the example _𝑆_ and _𝑇_ defined above, _𝑇_ ⊂ _𝑆_ , but _𝑇_ ≠ _𝑆_ . So _𝑇_ is a proper subset of _𝑆_ . If _𝐴_ = _𝐵_ , then _𝐴_ and _𝐵_ are simply two names for the same exact set. To define new sets, one often uses the _set building notation_ ,

**==> picture [79 x 16] intentionally omitted <==**

This notation refers to a subset of the set _𝐴_ containing all elements of _𝐴_ that satisfy the property _𝑃_ ( _𝑥_ ). Using _𝑆_ = {0 _,_ 1 _,_ 2} as above, { _𝑥_ ∈ _𝑆_ : _𝑥_ ≠ 2} is the set {0 _,_ 1}. The notation is sometimes abbreviated as � _𝑥_ : _𝑃_ ( _𝑥_ )�, that is, _𝐴_ is not mentioned when understood from context. Furthermore, _𝑥_ ∈ _𝐴_ is sometimes replaced with a formula to make the notation easier to read.