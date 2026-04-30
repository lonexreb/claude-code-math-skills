Definition 0.3.33

**Definition 0.3.33.** The _power set_ of a set _𝐴_ , denoted by _P_ ( _𝐴_ ), is the set of all subsets of _𝐴_ .

For example, if _𝐴_ � {1 _,_ 2}, then _P_ ( _𝐴_ ) = �∅ _,_ {1} _,_ {2} _,_ {1 _,_ 2}�. In particular, | _𝐴_ | = 2 and | _P_ ( _𝐴_ )| = 4 = 2[2] . In general, for a finite set _𝐴_ of cardinality _𝑛_ , the cardinality of _P_ ( _𝐴_ ) is 2 _[𝑛]_ . This fact is left as an exercise. Hence, for a finite set _𝐴_ , the cardinality of _P_ ( _𝐴_ ) is _𝐴_ . strictly larger than the cardinality of What is an unexpected and striking fact is that this statement is also true for infinite sets.

**Theorem 0.3.34** (Cantor ) **.** _Let 𝐴 be a set. Then_ | _𝐴_ | _<_ | _P_ ( _𝐴_ )| _. In particular, there exists no surjection from 𝐴 onto P_ ( _𝐴_ ) _._

_Proof._ An injection _𝑓_ : _𝐴_ → _P_ ( _𝐴_ ) exists: For _𝑥_ ∈ _𝐴_ , let _𝑓_ ( _𝑥_ ) � { _𝑥_ }. Thus, | _𝐴_ | ≤| _P_ ( _𝐴_ )|.

To finish the proof, we must show that no function _𝑔_ : _𝐴_ → _P_ ( _𝐴_ ) is a surjection. Suppose _𝑔_ : _𝐴_ → _P_ ( _𝐴_ ) is a function. So for _𝑥_ ∈ _𝐴_ , _𝑔_ ( _𝑥_ ) is a subset of _𝐴_ . Define the set

**==> picture [124 x 16] intentionally omitted <==**

We claim that _𝐵_ is not in the range of _𝑔_ and hence _𝑔_ is not a surjection. Suppose for contradiction that there exists an _𝑥_ 0 such that _𝑔_ ( _𝑥_ 0) = _𝐵_ . Either _𝑥_ 0 ∈ _𝐵_ or _𝑥_ 0 ∉ _𝐵_ . If _𝑥_ 0 ∈ _𝐵_ , then _𝑥_ 0 ∉ _𝑔_ ( _𝑥_ 0) = _𝐵_ , which is a contradiction. If _𝑥_ 0 ∉ _𝐵_ , then _𝑥_ 0 ∈ _𝑔_ ( _𝑥_ 0) = _𝐵_ , which is again a contradiction. Thus such an _𝑥_ 0 does not exist. Therefore, _𝐵_ is not in the range of _𝑔_ , and _𝑔_ is not a surjection. As _𝑔_ was an arbitrary function, no surjection exists. □

One particular consequence of this theorem is that there do exist uncountable sets, as _P_ (ℕ) must be uncountable. A related fact is that the set of real numbers (which we study in the next chapter) is uncountable. The existence of uncountable sets may seem unintuitive, and the theorem caused quite a controversy at the time it was announced. The theorem not only says that uncountable sets exist, but that there, in fact, exist progressively larger and larger infinite sets ℕ, _P_ (ℕ), _P_ ( _P_ (ℕ)), _P_ ( _P_ ( _P_ (ℕ))), etc.

> ‗Named after the German mathematician (1845–1918).

_INTRODUCTION_

20

## **0.3.6 Exercises**

_**Exercise**_ **0.3.1** _**:** Show 𝐴_ \ ( _𝐵_ ∩ _𝐶_ ) = ( _𝐴_ \ _𝐵_ ) ∪( _𝐴_ \ _𝐶_ ) _._

_**Exercise**_ **0.3.2** _**:** Prove that the principle of strong induction is equivalent to the standard induction._

_**Exercise**_ **0.3.3** _**:** Finish the proof of ._

## _**Exercise**_ **0.3.4** _**:**_

- _a) Prove ._

- _b) Find an example for which the equality of sets in 𝑓_ ( _𝐶_ ∩ _𝐷_ ) ⊂ _𝑓_ ( _𝐶_ ) ∩ _𝑓_ ( _𝐷_ ) _fails. That is, find an 𝑓 , 𝐴, 𝐵, 𝐶, and 𝐷 such that 𝑓_ ( _𝐶_ ∩ _𝐷_ ) _is a proper subset of 𝑓_ ( _𝐶_ ) ∩ _𝑓_ ( _𝐷_ ) _._

_**Exercise**_ **0.3.5** (Tricky) _**:** Prove that if 𝐴 is nonempty and finite, then there exists a unique 𝑛_ ∈ ℕ _such that there exists a bĳection between 𝐴 and_ {1 _,_ 2 _,_ 3 _, . . . , 𝑛_ } _. In other words, the notation_ | _𝐴_ | � _𝑛 is justified. Hint: Show that if 𝑛 > 𝑚, then there is no injection from_ {1 _,_ 2 _,_ 3 _, . . . , 𝑛_ } _to_ {1 _,_ 2 _,_ 3 _, . . . , 𝑚_ } _._

## _**Exercise**_ **0.3.6** _**:** Prove:_

- _a) 𝐴_ ∩( _𝐵_ ∪ _𝐶_ ) = ( _𝐴_ ∩ _𝐵_ ) ∪( _𝐴_ ∩ _𝐶_ ) _._

- _b) 𝐴_ ∪( _𝐵_ ∩ _𝐶_ ) = ( _𝐴_ ∪ _𝐵_ ) ∩( _𝐴_ ∪ _𝐶_ ) _._

_**Exercise**_ **0.3.7** _**:** Let 𝐴_ Δ _𝐵 denote the_ symmetric difference _, that is, the set of all elements that belong to either 𝐴 or 𝐵, but not to both 𝐴 and 𝐵._

- _a) Draw a Venn diagram for 𝐴_ Δ _𝐵._

- _b) Show 𝐴_ Δ _𝐵_ = ( _𝐴_ \ _𝐵_ ) ∪( _𝐵_ \ _𝐴_ ) _._

- _c) Show 𝐴_ Δ _𝐵_ = ( _𝐴_ ∪ _𝐵_ ) \ ( _𝐴_ ∩ _𝐵_ ) _._

_**Exercise**_ **0.3.8** _**:** For each 𝑛_ ∈ ℕ _, let 𝐴𝑛_ � {( _𝑛_ + 1) _𝑘_ : _𝑘_ ∈ ℕ} _._

- _a) Find 𝐴_ 1 ∩ _𝐴_ 2 _._

- _b) Find_[�][∞] _𝑛_ =1 _[𝐴][𝑛][.]_

- _c) Find_[�][∞] _𝑛_ =1 _[𝐴][𝑛][.]_

_**Exercise**_ **0.3.9** _**:** Determine P_ ( _𝑆_ ) _(the power set) for each of the following:_

_a) 𝑆_ = ∅ _,_

- _b) 𝑆_ = {1} _,_

- _c) 𝑆_ = {1 _,_ 2} _,_

- _d) 𝑆_ = {1 _,_ 2 _,_ 3 _,_ 4} _._

_**Exercise**_ **0.3.10** _**:** Let 𝑓_ : _𝐴_ → _𝐵 and 𝑔_ : _𝐵_ → _𝐶 be functions._

- _a) Prove that if 𝑔_ ◦ _𝑓 is injective, then 𝑓 is injective._

- _b) Prove that if 𝑔_ ◦ _𝑓 is surjective, then 𝑔 is surjective._

- _c) Find an explicit example where 𝑔_ ◦ _𝑓 is bĳective, but neither 𝑓 nor 𝑔 is bĳective._

_0.3. BASIC SET THEORY_

21

_**Exercise**_ **0.3.11** _**:** Prove by induction that 𝑛 <_ 2 _[𝑛] for all 𝑛_ ∈ ℕ _._

_**Exercise**_ **0.3.12** _**:** Show that for a finite set 𝐴 of cardinality 𝑛, the cardinality of P_ ( _𝐴_ ) _is_ 2 _[𝑛] ._

_**Exercise**_ **0.3.13** _**:** Prove_ 11·2[+] 21·3[+ · · · +] _𝑛_ ( _𝑛_ 1+1)[=] _𝑛𝑛_ +1 _[for all][ 𝑛]_[∈][ℕ] _[.]_ 2 _**Exercise**_ **0.3.14** _**:** Prove_ 1[3] + 2[3] + · · · + _𝑛_[3] = _𝑛_ ( _𝑛_ 2+1) _for all 𝑛_ ∈ ℕ _._ � �

_**Exercise**_ **0.3.15** _**:** Prove that 𝑛_[3] + 5 _𝑛 is divisible by_ 6 _for all 𝑛_ ∈ ℕ _._

_**Exercise**_ **0.3.16** _**:** Find the smallest 𝑛_ ∈ ℕ _such that_ 2( _𝑛_ + 5)[2] _< 𝑛_[3] _and call it 𝑛_ 0 _. Show that_ 2( _𝑛_ + 5)[2] _< 𝑛_[3] _for all 𝑛_ ≥ _𝑛_ 0 _._

_**Exercise**_ **0.3.17** _**:** Find all 𝑛_ ∈ ℕ _such that 𝑛_[2] _<_ 2 _[𝑛] ._

_**Exercise**_ **0.3.18** _**:** Prove the of_ ℕ _using the ._

_**Exercise**_ **0.3.19** _**:** Give an example of a countably infinite collection of finite sets 𝐴_ 1 _, 𝐴_ 2 _, . . ., whose union is not a finite set._

_**Exercise**_ **0.3.20** _**:** Give an example of a countably infinite collection of infinite sets 𝐴_ 1 _, 𝐴_ 2 _, . . ., with 𝐴𝑗_ ∩ _𝐴𝑘 being infinite for all 𝑗 and 𝑘, such that_[�][∞] _𝑗_ =1 _[𝐴][𝑗][is nonempty and finite.]_

_**Exercise**_ **0.3.21** _**:** Suppose 𝐴_ ⊂ _𝐵 and 𝐵 is finite. Prove that 𝐴 is finite. That is, if 𝐴 is nonempty, construct a bĳection of 𝐴 to_ {1 _,_ 2 _, . . . , 𝑛_ } _._

_**Exercise**_ **0.3.22** _**:** Prove . That is, prove that if R is an equivalence relation on a set 𝐴, then every 𝑎_ ∈ _𝐴 is in exactly one equivalence class. Then prove that 𝑎 R 𝑏 if and only if_ [ _𝑎_ ] = [ _𝑏_ ] _._

_**Exercise**_ **0.3.23** _**:** Prove that the relation ‘_ ∼ _’ in is an equivalence relation._

_**Exercise**_ **0.3.24** _**:**_

- _a) Suppose 𝐴_ ⊂ _𝐵 and 𝐵 is countably infinite. By constructing a bĳection, show that 𝐴 is countable (that is, 𝐴 is empty, finite, or countably infinite)._

_b) Use part a) to show that if_ | _𝐴_ | _<_ |ℕ| _, then 𝐴 is finite._

_**Exercise**_ **0.3.25** (Challenging) _**:** Suppose_ |ℕ| ≤| _𝑆_ | _, or in other words, 𝑆 contains a countably infinite subset. Show that there exists a countably infinite subset 𝐴_ ⊂ _𝑆 and a bĳection between 𝑆_ \ _𝐴 and 𝑆._

_**Exercise**_ **0.3.26** _**:** Prove the infinite versions of DeMorgan’s laws. Suppose 𝐴 is a set and 𝐵𝜆 is a collection of sets for 𝜆_ ∈ _𝐼. Prove_

**==> picture [278 x 32] intentionally omitted <==**

_**Exercise**_ **0.3.27** _**:** Suppose 𝑓_ : _𝐴_ → _𝐵 is a function and for 𝜆_ ∈ _𝐼, we have a collection of subsets 𝐶𝜆_ ⊂ _𝐴 and 𝐷𝜆_ ⊂ _𝐵. Prove_

_and_

**==> picture [269 x 78] intentionally omitted <==**

_INTRODUCTION_

22

## **Chapter 1**

## **Real Numbers**

## **1.1 Basic properties**

## _Note: 1.5 lectures_

In analysis, the main object we work with is the set of real numbers. As this set is so fundamental, often much time is spent formally constructing the set of real numbers. However, we take an easier approach, and we will assume that a set with the correct properties exists. The three key properties of the real numbers is that it is an ordered set, it We start is complete with respect to this order, and it is a field compatible with this order. with order.