Lemma 7.5.7

**Lemma 7.5.7.** _Let_ ( _𝑋, 𝑑𝑋_ ) _and_ ( _𝑌, 𝑑𝑌_ ) _be metric spaces. A function 𝑓_ : _𝑋_ → _𝑌 is continuous at 𝑐_ ∈ _𝑋 if and only if for every open neighborhood 𝑈 of 𝑓_ ( _𝑐_ ) _in 𝑌, the set 𝑓_[−][1] ( _𝑈_ ) _contains an open neighborhood of 𝑐 in 𝑋. See ._

**==> picture [205 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑓 [−][1] ( 𝑈 )<br>𝑈<br>𝑊 𝑓<br>𝑐 𝑓 ( 𝑐 )<br>**----- End of picture text -----**<br>


**Figure 7.15:** For every neighborhood _𝑈_ of _𝑓_ ( _𝑐_ ), the set _𝑓_[−][1] ( _𝑈_ ) contains an open neighborhood _𝑊_ of _𝑐_ .

_Proof._ First suppose that _𝑓_ is continuous at _𝑐_ . Let _𝑈_ be an open neighborhood of _𝑓_ ( _𝑐_ ) in _𝑌_ , then _𝐵𝑌_ � _𝑓_ ( _𝑐_ ) _, 𝜖_[�] ⊂ _𝑈_ for some _𝜖>_ 0. By continuity of _𝑓_ , there exists a _𝛿>_ 0 such that whenever _𝑥_ is such that _𝑑𝑋_ ( _𝑥, 𝑐_ ) _< 𝛿_ , then _𝑑𝑌_ � _𝑓_ ( _𝑥_ ) _, 𝑓_ ( _𝑐_ )[�] _< 𝜖_ . In other words,

**==> picture [198 x 15] intentionally omitted <==**

and _𝐵𝑋_ ( _𝑐, 𝛿_ ) is an open neighborhood of _𝑐_ .

For the other direction, let _𝜖>_ 0 be given. If _𝑓_[−][1][�] _𝐵𝑌_ � _𝑓_ ( _𝑐_ ) _, 𝜖_[��] contains an open neighborhood _𝑊_ of _𝑐_ , it contains a ball. That is, there is some _𝛿>_ 0 such that

**==> picture [174 x 16] intentionally omitted <==**

That means precisely that if _𝑑𝑋_ ( _𝑥, 𝑐_ ) _< 𝛿_ , then _𝑑𝑌_ � _𝑓_ ( _𝑥_ ) _, 𝑓_ ( _𝑐_ )[�] _< 𝜖_ . So _𝑓_ is continuous at _𝑐_ . □

_7.5. CONTINUOUS FUNCTIONS_

291