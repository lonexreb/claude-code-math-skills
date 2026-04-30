Example 6.1.8

**Example 6.1.8:** The functions _𝑓𝑛_ ( _𝑥_ ) � _𝑥_[2] _[𝑛]_ do not converge uniformly on [−1 _,_ 1], even though they converge pointwise. To see this, suppose for contradiction that the convergence is uniform. For _𝜖_ �[1] /2, there would have to exist an _𝑁_ such that _𝑥_[2] _[𝑁]_ = �� _𝑥_ 2 _𝑁_ − 0�� _<_ 1/2 for all _𝑥_ ∈(−1 _,_ 1) (as _𝑓𝑛_ ( _𝑥_ ) converges to 0 on (−1 _,_ 1)). But that means that for every sequence { _𝑥𝑘_ }[∞] _𝑘_ =1[in][ (−][1] _[,]_[ 1][)][ such that][ lim] _[𝑘]_[→∞] _[𝑥][𝑘]_[=][ 1][, we have] _[ 𝑥]_[2] _𝑘[𝑁] <_[1] /2 for all _𝑘_ . On the other hand, _𝑥_[2] _[𝑁]_ is a continuous function of _𝑥_ (it is a polynomial). Therefore, we obtain a contradiction

**==> picture [130 x 20] intentionally omitted <==**

However, if we restrict our domain to [− _𝑎, 𝑎_ ] where 0 _< 𝑎 <_ 1, then { _𝑓𝑛_ }[∞] _𝑛_ =1[converges] uniformly to 0 on [− _𝑎, 𝑎_ ]. Note that _𝑎_[2] _[𝑛]_ → 0 as _𝑛_ →∞. Given _𝜖>_ 0, pick _𝑁_ ∈ ℕ such that _𝑎_[2] _[𝑛] < 𝜖_ for all _𝑛_ ≥ _𝑁_ . If _𝑥_ ∈[− _𝑎, 𝑎_ ], then | _𝑥_ | ≤ _𝑎_ . So for all _𝑛_ ≥ _𝑁_ and all _𝑥_ ∈[− _𝑎, 𝑎_ ],

**==> picture [120 x 17] intentionally omitted <==**

## **6.1.3 Convergence in uniform norm**

For bounded functions, there is another more abstract way to think of uniform convergence. To every bounded function we assign a certain nonnegative number that measures the “distance” of the function from the constant function 0. This number allows us to “measure” how far two functions are from each other. We then translate a statement about uniform convergence into a statement about a certain sequence of real numbers converging to zero.