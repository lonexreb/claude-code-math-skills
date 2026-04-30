Proposition 6.1.13

**Proposition 6.1.13.** _Let 𝑓𝑛_ : _𝑆_ → ℝ _be bounded functions. Then_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[is Cauchy in the uniform] norm if and only if there exists an 𝑓_ : _𝑆_ → ℝ _and_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges uniformly to][𝑓][.]_

_Proof._ First suppose { _𝑓𝑛_ }[∞] _𝑛_ =1[is Cauchy in the uniform norm.][Let us define] _[𝑓]_[.][Fix] _[ 𝑥]_[.][The] ∞ sequence � _𝑓𝑛_ ( _𝑥_ )� _𝑛_ =1[is Cauchy because]

**==> picture [148 x 18] intentionally omitted <==**

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

232

**==> picture [365 x 20] intentionally omitted <==**

**==> picture [94 x 18] intentionally omitted <==**

The sequence { _𝑓𝑛_ }[∞] _𝑛_ =1[converges pointwise to] _[𝑓]_[.][To show that the convergence is uniform,] let _𝜖>_ 0 be given. Find an _𝑁_ such that for all _𝑚, 𝑘_ ≥ _𝑁_ , we have �� _𝑓𝑚_ − _𝑓𝑘_ �� _𝑆[<][𝜖]_[/][2][.][In other] words, for all _𝑥_ , we have �� _𝑓𝑚_ ( _𝑥_ ) − _𝑓𝑘_ ( _𝑥_ )�� _< 𝜖_ /2. For any fixed _𝑥_ , take the limit as _𝑘_ goes to infinity. Then �� _𝑓𝑚_ ( _𝑥_ ) − _𝑓𝑘_ ( _𝑥_ )�� goes to �� _𝑓𝑚_ ( _𝑥_ ) − _𝑓_ ( _𝑥_ )��. Consequently for all _𝑥_ ,

**==> picture [124 x 17] intentionally omitted <==**

Hence, { _𝑓𝑛_ }[∞] _𝑛_ =1[converges uniformly.] Next, we prove the other direction. Suppose { _𝑓𝑛_ }[∞] _𝑛_ =1[converges uniformly to] _[𝑓]_[.][Given] _𝜖>_ 0, find _𝑁_ such that for all _𝑛_ ≥ _𝑁_ , we have �� _𝑓𝑛_ ( _𝑥_ ) − _𝑓_ ( _𝑥_ )�� _< 𝜖_ /4 for all _𝑥_ ∈ _𝑆_ . Therefore, for all _𝑚, 𝑘_ ≥ _𝑁_ and all _𝑥_ ,

**==> picture [447 x 36] intentionally omitted <==**

Take the supremum over all _𝑥_ to obtain

**==> picture [288 x 17] intentionally omitted <==**

## **6.1.4 Exercises**

_**Exercise**_ **6.1.1** _**:** Let 𝑓 and 𝑔 be bounded functions on_ [ _𝑎, 𝑏_ ] _. Prove_

**==> picture [152 x 18] intentionally omitted <==**

_**Exercise**_ **6.1.2** _**:**_

_a) Find the pointwise limit[𝑒][𝑥]_[/] _[𝑛] for 𝑥_ ∈ ℝ _. 𝑛_

_b) Is the limit uniform on_ ℝ _?_

_c) Is the limit uniform on_ [0 _,_ 1] _?_

_**Exercise**_ **6.1.3** _**:** Suppose 𝑓𝑛_ : _𝑆_ → ℝ _are functions that converge uniformly to 𝑓_ : _𝑆_ → ℝ _. Suppose 𝐴_ ⊂ _𝑆. Show that the sequence of restrictions_ { _𝑓𝑛_ | _𝐴_ }[∞] _𝑛_ =1 _[converges uniformly to][𝑓]_[|] _[𝐴][.]_

_**Exercise**_ **6.1.4** _**:** Suppose_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[and]_[{] _[𝑔][𝑛]_[}][∞] _𝑛_ =1 _[defined][on][some][set][𝐴][converge][to][𝑓][and][𝑔][respectively] pointwise. Show that_ { _𝑓𝑛_ + _𝑔𝑛_ }[∞] _𝑛_ =1 _[converges pointwise to][𝑓]_[+] _[ 𝑔][.]_

_**Exercise**_ **6.1.5** _**:** Suppose_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[and]_[{] _[𝑔][𝑛]_[}][∞] _𝑛_ =1 _[defined][on][some][set][𝐴][converge][to][𝑓][and][𝑔][respectively] uniformly on 𝐴. Show that_ { _𝑓𝑛_ + _𝑔𝑛_ }[∞] _𝑛_ =1 _[converges uniformly to][𝑓]_[+] _[ 𝑔][on][ 𝐴][.]_

_**Exercise**_ **6.1.6** _**:** Find an example of a sequence of functions_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[and]_[ {] _[𝑔][𝑛]_[}][∞] _𝑛_ =1 _[that converge uniformly to] some 𝑓 and 𝑔 on some set 𝐴, but such that_ { _𝑓𝑛 𝑔𝑛_ }[∞] _𝑛_ =1 _[(the multiple) does not converge uniformly to][𝑓𝑔][on][ 𝐴][.] Hint: Let 𝐴_ � ℝ _, let 𝑓_ ( _𝑥_ ) � _𝑔_ ( _𝑥_ ) � _𝑥. You can even pick 𝑓𝑛_ = _𝑔𝑛._

233

## _6.1. POINTWISE AND UNIFORM CONVERGENCE_

_**Exercise**_ **6.1.7** _**:** Suppose there exists a sequence of functions_ { _𝑔𝑛_ }[∞] _𝑛_ =1 _[uniformly converging to]_[ 0] _[ on][ 𝐴][.][Now] suppose we have a sequence of functions_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[and a function][𝑓][on][ 𝐴][such that]_

**==> picture [102 x 15] intentionally omitted <==**

_for all 𝑥_ ∈ _𝐴. Show that_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges uniformly to][𝑓][on][ 𝐴][.]_

_**Exercise**_ **6.1.8** _**:** Let_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[,]_[ {] _[𝑔][𝑛]_[}][∞] _𝑛_ =1 _[and]_[ {] _[ℎ][𝑛]_[}][∞] _𝑛_ =1 _[be sequences of functions on]_[ [] _[𝑎, 𝑏]_[]] _[.][Suppose]_[ {] _[ 𝑓][𝑛]_[}][∞] _𝑛_ =1 _and_ { _ℎ𝑛_ }[∞] _𝑛_ =1 _[converge uniformly to some function][𝑓]_[:][[] _[𝑎, 𝑏]_[] →][ℝ] _[and suppose][𝑓][𝑛]_[(] _[𝑥]_[) ≤] _[𝑔][𝑛]_[(] _[𝑥]_[) ≤] _[ℎ][𝑛]_[(] _[𝑥]_[)] _[ for] all 𝑥_ ∈[ _𝑎, 𝑏_ ] _. Show that_ { _𝑔𝑛_ }[∞] _𝑛_ =1 _[converges uniformly to][𝑓][.]_ _**Exercise**_ **6.1.9** _**:** Let 𝑓𝑛_ : [0 _,_ 1] → ℝ _be a sequence of increasing functions (that is, 𝑓𝑛_ ( _𝑥_ ) ≥ _𝑓𝑛_ ( _𝑦_ ) _whenever 𝑥_ ≥ _𝑦). Suppose 𝑓𝑛_ (0) = 0 _and 𝑛_ lim→∞ _[𝑓][𝑛]_[(][1][)][ =][ 0] _[.][Show that]_[ {] _[ 𝑓][𝑛]_[}][∞] _𝑛_ =1 _[converges uniformly to]_[ 0] _[.]_

_**Exercise**_ **6.1.10** _**:** Consider a sequence of functions 𝑓𝑛_ : [0 _,_ 1] → ℝ _so that there is a sequence of distinct numbers 𝑥𝑛_ ∈[0 _,_ 1] _such that for all 𝑛,_

**==> picture [50 x 12] intentionally omitted <==**

_Prove or disprove the following statements:_

_a) True or false: There exists_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[as above that converges pointwise to]_[ 0] _[.]_

_b) True or false: There exists_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[as above that converges uniformly to]_[ 0] _[.]_

_**Exercise**_ **6.1.11** _**:** Fix a continuous ℎ_ : [ _𝑎, 𝑏_ ] → ℝ _. Let 𝑓_ ( _𝑥_ ) � _ℎ_ ( _𝑥_ ) _for 𝑥_ ∈[ _𝑎, 𝑏_ ] _, 𝑓_ ( _𝑥_ ) � _ℎ_ ( _𝑎_ ) _for 𝑥 < 𝑎 and 𝑓_ ( _𝑥_ ) � _ℎ_ ( _𝑏_ ) _for all 𝑥 > 𝑏. First show that 𝑓_ : ℝ → ℝ _is continuous. Now let 𝑓𝑛 be the function 𝑔 from with 𝜖_ =[1] / _𝑛, defined on the interval_ [ _𝑎, 𝑏_ ] _. That is,_

**==> picture [99 x 31] intentionally omitted <==**

_Show that_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[converges uniformly to][ℎ][on]_[ [] _[𝑎, 𝑏]_[]] _[.]_

_**Exercise**_ **6.1.12** _**:** Prove that if a sequence of functions 𝑓𝑛_ : _𝑆_ → ℝ _converge uniformly to a bounded function 𝑓_ : _𝑆_ → ℝ _, then there exists an 𝑁 such that for all 𝑛_ ≥ _𝑁, the 𝑓𝑛 are bounded._

_**Exercise**_ **6.1.13** _**:** Suppose there is a single constant 𝐵 and a sequence of functions 𝑓𝑛_ : _𝑆_ → ℝ _that are bounded by 𝐵, that is_ �� _𝑓𝑛_ ( _𝑥_ )�� ≤ _𝐵 for all 𝑥_ ∈ _𝑆. Suppose that_ { _𝑓𝑛_ }∞ _𝑛_ =1 _[converges pointwise to][𝑓]_[:] _[𝑆]_[→][ℝ] _[.] Prove that 𝑓 is bounded._

_**Exercise**_ **6.1.14** (requires ) _**:** In we saw_[�][∞] _𝑘_ =0 _[𝑥][𝑘][converges pointwise to]_ 1−1 _𝑥[on]_[ (−][1] _[,]_[ 1][)] _[.] a) Show that whenever_ 0 ≤ _𝑐 <_ 1 _, the series_[�][∞] _𝑘_ =0 _[𝑥][𝑘][converges uniformly on]_[ [−] _[𝑐, 𝑐]_[]] _[.]_

_b) Show that the series_[�][∞] _𝑘_ =0 _[𝑥][𝑘][does not converge uniformly on]_[ (−][1] _[,]_[ 1][)] _[.]_

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

234

## **6.2 Interchange of limits**

_Note: 1–2.5 lectures, subsections on derivatives and power series (which requires ) optional._

Large parts of modern analysis deal mainly with the question of the interchange of two limiting operations. When we have a chain of two limits, we cannot always just swap the limits. For instance,

**==> picture [240 x 31] intentionally omitted <==**

When talking about sequences of functions, interchange of limits comes up quite often. We look at several instances: continuity of the limit, the integral of the limit, the derivative of the limit, and the convergence of power series.

## **6.2.1 Continuity of the limit**

If we have a sequence { _𝑓𝑛_ }[∞] _𝑛_ =1[of continuous functions, is the limit continuous?][Suppose] _𝑓_ is the (pointwise) limit of { _𝑓𝑛_ }[∞] _𝑛_ =1[.][If][ lim] _[𝑘]_[→∞] _[𝑥][𝑘]_[=] _[𝑥]_[, we are interested in the following] interchange of limits, where the equality to prove is marked with a question mark. Equality is not always true, in fact, the limits to the left of the question mark might not even exist.

**==> picture [368 x 24] intentionally omitted <==**

We wish to find conditions on the sequence { _𝑓𝑛_ }[∞] _𝑛_ =1[so that the equation above holds.][If we] only require pointwise convergence, then the limit of a sequence of functions need not be continuous, and the equation above need not hold.