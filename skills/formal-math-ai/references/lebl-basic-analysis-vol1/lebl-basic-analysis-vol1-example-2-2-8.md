Example 2.2.8

**Example 2.2.8:** Let { _𝑥𝑛_ }[∞] _𝑛_ =1[be defined by] _[ 𝑥]_[1][�][2 and]

**==> picture [106 x 30] intentionally omitted <==**

We must first find out if this sequence is well-defined; we must show we never divide by zero. Then we must find out if the sequence converges. Only then can we attempt to find the limit.

_2.2. FACTS ABOUT LIMITS OF SEQUENCES_

67

So let us prove that for all _𝑛𝑥𝑛_ exists and _𝑥𝑛 >_ 0 (so the sequence is well-defined and bounded below). Let us show this by . We know that _𝑥_ 1 = 2 _>_ 0. For the induction step, suppose _𝑥𝑛_ exists and _𝑥𝑛 >_ 0. Then

**==> picture [232 x 31] intentionally omitted <==**

_𝑛_[+][2] It is always true that _𝑥𝑛_[2][+][ 2] _[ >]_[0, and as] _[ 𝑥][𝑛][>]_[ 0, then] _[ 𝑥][𝑛]_[+][1][=] _[𝑥]_ 2[2] _𝑥𝑛[>]_[ 0.] Next let us show that the sequence is monotone decreasing. If we show that _𝑥𝑛_[2][−][2][ ≥][0] for all _𝑛_ , then _𝑥𝑛_ +1 ≤ _𝑥𝑛_ for all _𝑛_ . Obviously _𝑥_ 1[2][−][2][ =][ 4][ −][2][ =][ 2] _[ >]_[ 0][.][For an arbitrary] _[ 𝑛]_[, we] have

**==> picture [388 x 36] intentionally omitted <==**

Since are _𝑥_[2][≥][0][for][all] _[𝑛]_[.][Therefore,][{] _[𝑥][𝑛]_[}][∞][monotone] squares nonnegative, _𝑛_ +1[−][2] _𝑛_ =1[is] decreasing and bounded ( _𝑥𝑛 >_ 0 for all _𝑛_ ), and so the limit exists. It remains to find the limit.

Write

**==> picture [92 x 15] intentionally omitted <==**

Since { _𝑥𝑛_ +1}[∞] _𝑛_ =1[is][the][1-tail][of][{] _[𝑥][𝑛]_[}][∞] _𝑛_ =1[,][it][converges][to][the][same][limit.][Let][us][define] _𝑥_ � lim _𝑛_ →∞ _𝑥𝑛_ . Take the limit of both sides to obtain

**==> picture [68 x 14] intentionally omitted <==**

**==> picture [339 x 16] intentionally omitted <==**

You may have seen the sequence above before. It is _Newton’s method_ for finding the square root of 2. This method comes up often in practice and converges very rapidly. We used the fact that _𝑥_[2][0][, although it was not strictly needed to show convergence by] 1[−][2] _[ >]_ considering a tail of the sequence. The sequence converges as long as _𝑥_ 1 ≠ 0, although with a negative _𝑥_ 1 we would arrive at _𝑥_ = −√2. By replacing the 2 in the numerator we obtain the square root of any positive number. These statements are left as an exercise.

You should, however, be careful. Before taking any limits, you must make sure the sequence converges. Let us see an example.