Example 6.2.1

**Example 6.2.1:** Define _𝑓𝑛_ : [0 _,_ 1] → ℝ as

**==> picture [147 x 39] intentionally omitted <==**

See .

Each function _𝑓𝑛_ is continuous. Fix an _𝑥_ ∈(0 _,_ 1]. If _𝑛_ ≥[1] / _𝑥_ , then _𝑥_ ≥[1] / _𝑛_ . Therefore for _𝑛_ ≥[1] / _𝑥_ , we have _𝑓𝑛_ ( _𝑥_ ) = 0, and so

**==> picture [76 x 18] intentionally omitted <==**

On the other hand, if _𝑥_ = 0, then

**==> picture [120 x 18] intentionally omitted <==**

Thus the pointwise limit of _𝑓𝑛_ is the function _𝑓_ : [0 _,_ 1] → ℝ defined by

**==> picture [107 x 39] intentionally omitted <==**

The function _𝑓_ is not continuous at 0.

_6.2. INTERCHANGE OF LIMITS_

235

**==> picture [217 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>1/ 푛<br>**----- End of picture text -----**<br>


**Figure 6.4:** Graph of _𝑓𝑛_ ( _𝑥_ ).

If we, however, require the convergence to be uniform, the limits can be interchanged. **Theorem 6.2.2.** _Suppose 𝑆_ ⊂ ℝ _. Let_ { _𝑓𝑛_ }[∞] _𝑛_ =1 _[be a sequence of continuous functions][𝑓][𝑛]_[:] _[𝑆]_[→][ℝ] _converging uniformly to 𝑓_ : _𝑆_ → ℝ _. Then 𝑓 is continuous._

_Proof._ Let _𝑥_ ∈ _𝑆_ be fixed. Let { _𝑥𝑛_ }[∞] _𝑛_ =1[be a sequence in] _[ 𝑆]_[converging to] _[ 𝑥]_[.] Let _𝜖>_ 0 be given. As { _𝑓𝑘_ }[∞] _𝑘_ =1[converges uniformly to] _[𝑓]_[, we find a] _[ 𝑘]_[∈][ℕ][such that]

**==> picture [96 x 17] intentionally omitted <==**

for all _𝑦_ ∈ _𝑆_ . As _𝑓𝑘_ is continuous at _𝑥_ , we find an _𝑁_ ∈ ℕ such that for all _𝑚_ ≥ _𝑁_ ,

**==> picture [110 x 17] intentionally omitted <==**

Thus for all _𝑚_ ≥ _𝑁_ ,

**==> picture [344 x 52] intentionally omitted <==**

Therefore, � _𝑓_ ( _𝑥𝑚_ )�∞ _𝑚_ =1[converges to] _[𝑓]_[(] _[𝑥]_[)][, and consequently] _[𝑓]_[is continuous at] _[ 𝑥]_[.][As] _[ 𝑥]_[was] arbitrary, _𝑓_ is continuous everywhere. □

## **6.2.2 Integral of the limit**

Again, if we simply require pointwise convergence, then the integral of a limit of a sequence of functions need not be equal to the limit of the integrals.

_CHAPTER 6. SEQUENCES OF FUNCTIONS_

236