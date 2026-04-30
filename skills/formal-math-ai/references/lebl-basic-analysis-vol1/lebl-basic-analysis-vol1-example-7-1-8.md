Example 7.1.8

**Example 7.1.8:** Let _𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] be the set of continuous real-valued functions on the interval [ _𝑎, 𝑏_ ]. Define the metric on _𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] as

**==> picture [154 x 26] intentionally omitted <==**

Let us check the properties. First, _𝑑_ ( _𝑓, 𝑔_ ) is finite as �� _𝑓_ ( _𝑥_ ) − _𝑔_ ( _𝑥_ )�� is a continuous function on a closed bounded interval [ _𝑎, 𝑏_ ], and so is bounded. It is clear that _𝑑_ ( _𝑓, 𝑔_ ) ≥ 0, it is the

_CHAPTER 7. METRIC SPACES_

260

supremum of nonnegative numbers. If _𝑓_ = _𝑔_ , then �� _𝑓_ ( _𝑥_ ) − _𝑔_ ( _𝑥_ )�� = 0 for all _𝑥_ , and hence _𝑑_ ( _𝑓, 𝑔_ ) = 0. Conversely, if _𝑑_ ( _𝑓, 𝑔_ ) = 0, then for every _𝑥_ , we have �� _𝑓_ ( _𝑥_ ) − _𝑔_ ( _𝑥_ )�� ≤ _𝑑_ ( _𝑓, 𝑔_ ) = 0, and hence _𝑓_ ( _𝑥_ ) = _𝑔_ ( _𝑥_ ) for all _𝑥_ , and so _𝑓_ = _𝑔_ . That _𝑑_ ( _𝑓, 𝑔_ ) = _𝑑_ ( _𝑔, 𝑓_ ) is equally trivial. To show the triangle inequality we use the standard triangle inequality;

**==> picture [356 x 86] intentionally omitted <==**

When treating _𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] as a metric space without mentioning a metric, we mean this particular metric. Notice that _𝑑_ ( _𝑓, 𝑔_ ) = �� _𝑓_ − _𝑔_ ��[ _𝑎,𝑏_ ][, the uniform norm of] . This example may seem esoteric at first, but it turns out that working with spaces such as _𝐶_[�] [ _𝑎, 𝑏_ ] _,_ ℝ[�] is really the meat of a large part of modern analysis. Treating sets of functions as metric spaces allows us to abstract away a lot of the grubby detail and prove powerful results such as with less work.