Definition 7.1.1

**Definition 7.1.1.** Let _𝑋_ be a set, and let _𝑑_ : _𝑋_ × _𝑋_ → ℝ be a function such that for all _𝑥, 𝑦, 𝑧_ ∈ _𝑋_

(i) _𝑑_ ( _𝑥, 𝑦_ ) ≥ 0. ( _nonnegativity_ ) (ii) _𝑑_ ( _𝑥, 𝑦_ ) = 0 if and only if _𝑥_ = _𝑦_ . ( _identity of indiscernibles_ ) (iii) _𝑑_ ( _𝑥, 𝑦_ ) = _𝑑_ ( _𝑦, 𝑥_ ). ( _symmetry_ ) (iv) _𝑑_ ( _𝑥, 𝑧_ ) ≤ _𝑑_ ( _𝑥, 𝑦_ ) + _𝑑_ ( _𝑦, 𝑧_ ). ( _triangle inequality_ )

The pair ( _𝑋, 𝑑_ ) is called a _metric space_ . The function _𝑑_ is called the _metric_ or the _distance function_ . Sometimes we write just _𝑋_ as the metric space instead of ( _𝑋, 𝑑_ ) if the metric is clear from context.

The geometric idea is that _𝑑_ is the distance between two points. Items – have obvious geometric interpretation: Distance is always nonnegative, the only point that is

_CHAPTER 7. METRIC SPACES_

256

distance 0 away from _𝑥_ is _𝑥_ itself, and finally that the distance from _𝑥_ to _𝑦_ is the same as the distance from _𝑦_ to _𝑥_ . The triangle inequality has the interpretation given in .

**==> picture [184 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑧<br>𝑑 ( 𝑥, 𝑧 ) 𝑑 ( 𝑦, 𝑧 )<br>shorter<br>longer<br>𝑦<br>𝑥 𝑑 ( 𝑥, 𝑦 )<br>**----- End of picture text -----**<br>


**Figure 7.1:** Diagram of the triangle inequality in metric spaces.

For the purposes of drawing, it is convenient to draw figures and diagrams in the plane with the metric being the euclidean distance. However, that is only one particular metric space. Just because a certain fact seems to be clear from drawing a picture does not mean it is true in every metric space. You might be getting sidetracked by intuition from euclidean geometry, whereas the concept of a metric space is a lot more general.

Let us give some examples of metric spaces.