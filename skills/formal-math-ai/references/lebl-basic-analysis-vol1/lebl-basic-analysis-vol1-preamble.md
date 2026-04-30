## **Basic Analysis I**

_Introduction to Real Analysis, Volume I_

## **by Jiří Lebl**

May 23, 2025 (version 6.2)

2

Typeset in L[A] TEX.

Copyright ©2009–2025 Jiří Lebl

**==> picture [214 x 35] intentionally omitted <==**

This work is dual licensed under the Creative Commons Attribution-Noncommercial-Share Alike 4.0 International License and the Creative Commons Attribution-Share Alike 4.0 International License. To view a copy of these licenses, visit or or send a letter to Creative Commons PO Box 1866, Mountain View, CA 94042, USA.

You can use, print, duplicate, and share this book as much as you want. You can base your own notes on it and reuse parts if you keep the license the same. You can assume the license is either CC-BY-NC-SA or CC-BY-SA, whichever is compatible with what you wish to do. Your derivative work must use at least one of the licenses. Derivative works must be prominently marked as such.

During the writing of this book, the author was in part supported by NSF grants DMS0900885 and DMS-1362337.

The major version / edition number is raised only if there have been substantial changes. From 6th edition onwards, both volumes share the same version number. Edition number started at 4, that is, version 4.0, as it was not kept track of before.

See for more information (including contact information, possible updates, and errata).

The L[A] TEX source for the book is available for possible modification and customization at github:

## **Contents**

|**Introduction**|**Introduction**|**Introduction**|||||||||**5**|
|---|---|---|---|---|---|---|---|---|---|---|---|
||0.1|About this book<br>. . .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|5|
||0.2|About analysis<br>. . . .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|7|
||0.3|Basic set theory<br>. . .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|8|
|**1**|**Real Numbers**||||||||||**23**|
||1.1|Basic properties<br>. . .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|23|
||1.2|The set of real numbers|||.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|29|
||1.3|Absolute value and|bounded functions<br>.||||||. . . . . . .|. . . . . . . . . . . . .|36|
||1.4|Intervals and the size||ofℝ<br>. .|||. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|41|
||1.5|Decimal representation|||of the reals|||. . . .|. . . . . . .|. . . . . . . . . . . . .|44|
|**2**|**Sequences and Series**||||||||||**51**|
||2.1|Sequences and limits||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|51|
||2.2|Facts about limits of sequences|||||. .|. . . .|. . . . . . .|. . . . . . . . . . . . .|61|
||2.3|Limit superior, limit inferior, and Bolzano–Weierstrass||||||||. . . . . . . . . . . . .|73|
||2.4|Cauchy sequences<br>. .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|84|
||2.5|Series<br>. . . . . . . . .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|87|
||2.6|More on series<br>. . . .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|100|
|**3**|**Continuous Functions**||||||||||**113**|
||3.1|Limits of functions|.|.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|113|
||3.2|Continuous functions||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|122|
||3.3|Extreme and intermediate value theorems|||||||. . . . . . .|. . . . . . . . . . . . .|130|
||3.4<br> 3.5|Uniform continuity<br>. <br>Limits at infnity<br>. . .||. <br> .|. <br> .|. . . <br> . . .|. . . <br> . . .|. . . . <br> . . . .|. . . . . . . <br> . . . . . . .|. . . . . . . . . . . . . <br> . . . . . . . . . . . . .|138<br> 145|
||3.6|Monotone functions and continuity||||||. . . .|. . . . . . .|. . . . . . . . . . . . .|149|
|**4**|**The Derivative**||||||||||**155**|
||4.1|The derivative<br>. . . .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|155|
||4.2|Mean value theorem||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|162|
||4.3|Taylor’s theorem<br>. . .||.|.|. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|171|
||4.4|Inverse function theorem||||. . .|. . .|. . . .|. . . . . . .|. . . . . . . . . . . . .|176|


_CONTENTS_

4

|**5**|**The Riemann Integral**|||||||**181**|
|---|---|---|---|---|---|---|---|---|
||5.1<br>The Riemann integral|. .|. .|. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 181|
||5.2<br>Properties of the integral||. .|. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 191|
||5.3<br>Fundamental theorem of||calculus|||.|. . . . . . . .|. . . . . . . . . . . . . . . . 200|
||5.4<br>The logarithm and the exponential||||||. . . . . . . .|. . . . . . . . . . . . . . . . 207|
||5.5<br>Improper integrals<br>.|. .|. .|. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 214|
|**6**|**Sequences of Functions**|||||||**227**|
||6.1<br>Pointwise and uniform convergence||||||. . . . . . .|. . . . . . . . . . . . . . . . 227|
||6.2<br>Interchange of limits|. .|. .|. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 234|
||6.3<br>Picard’s theorem<br>. .|. .|. .|. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 246|
|**7**|**Metric Spaces**|||||||**255**|
||7.1<br>Metric spaces<br>. . . .|. .|. .|. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 255|
||7.2<br>Open and closed sets|. .|. .|. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 264|
||7.3<br>Sequences and convergence|||. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 274|
||7.4<br>Completeness and compactness||||.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 279|
||7.5<br>Continuous functions|. .|. .|. .|.|.|. . . . . . . .|. . . . . . . . . . . . . . . . 288|
||7.6<br>Fixed point theorem and||Picard’s|||theorem again||. . . . . . . . . . . . . . . . 296|
|**Further Reading**||||||||**301**|
|**Index**||||||||**303**|
|**List of Notation**||||||||**309**|


## **Introduction**

## **0.1 About this book**

This first volume is a one semester course in basic analysis. With the second volume, it is a year-long course. The book started its life as my lecture notes for teaching Math 444 at the University of Illinois at Urbana-Champaign (UIUC) in the fall semester of 2009. I added the metric space chapter for Math 521 at the University of Wisconsin–Madison (UW). Volume II was added to teach Math 4143/4153 at Oklahoma State University (OSU). A prerequisite for these courses is usually a basic proof course, using, for example, [ ], [ ], or [ ].

It should be possible to use the book for both a basic course for students who do not necessarily wish to go to graduate school (such as UIUC 444), and also as a more advanced one-semester course that also covers topics such as metric spaces (such as UW 521). Here are suggestions for a semester course. A slower course such as UIUC 444:

§0.3, §1.1–§1.4, §2.1–§2.5, §3.1–§3.4, §4.1–§4.2, §5.1–§5.3, §6.1–§6.3

A more rigorous course covering metric spaces that runs quite a bit faster (e.g., UW 521):

§0.3, §1.1–§1.4, §2.1–§2.5, §3.1–§3.4, §4.1–§4.2, §5.1–§5.3, §6.1–§6.2, §7.1–§7.6

It should also be possible to run a faster course without metric spaces covering all sections of chapters 0 through 6. The approximate number of lectures given in the section notes through Chapter 6 are a very rough estimate and were designed for the slower course. The first few chapters of the book can be used in an introductory proofs course, as is done, for example, at Iowa State University Math 201, where this book is used in conjunction with Hammack’s _Book of Proof_ [ ].

With volume II, one can run a year-long course that covers multivariable topics. In this scenario, it may make sense to cover most of the first volume in the first semester while leaving metric spaces for the beginning of the second semester.

The structure of the beginning of volume I somewhat follows the standard syllabus of UIUC Math 444 and, therefore, has some similarities with Bartle and Sherbert, _Introduction to Real Analysis_ [ ], which is the standard book at UIUC. A major difference is that we The Darboux define the Riemann integral using Darboux sums and not tagged partitions. approach is far more appropriate for a course of this level.

Our approach allows us to fit a course such as UIUC 444 within a semester and still spend some time on the interchange of limits and end with Picard’s theorem on the

_INTRODUCTION_

6

This theorem existence and uniqueness of solutions of ordinary differential equations. is a wonderful example that uses many results proved in the book. For more advanced students, material may be covered faster so that we arrive at metric spaces and prove Picard’s theorem using the fixed point theorem as is usual.

Other excellent books exist. My favorite is Rudin’s excellent _Principles of Mathematical Analysis_ [ ] or, as it is commonly and lovingly called, _baby Rudin_ (to distinguish it from his other great analysis textbook, _big Rudin_ ). I took a lot of inspiration and ideas from Rudin. However, Rudin is a bit more advanced and ambitious than this present course. For those who wish to continue mathematics, Rudin is a fine investment. An inexpensive and somewhat simpler alternative to Rudin is Rosenlicht’s _Introduction to Analysis_ [ ]. There is also the freely downloadable _Introduction to Real Analysis_ by William Trench [ ].

A note about the style of some of the proofs: Many proofs traditionally done by contradiction, I prefer to do by a direct proof or by contrapositive. While the book does include proofs by contradiction, I only do so when the contrapositive statement seemed too awkward or when contradiction follows rather quickly. Contradiction is more likely to get beginning students into trouble, as we are talking about objects that do not exist.

I try to avoid unnecessary formalism where it is unhelpful. Furthermore, the proofs and the language get slightly less formal as we progress through the book, as more and more details are left out to avoid clutter.

As a general rule, I use � instead of = to define an object rather than to simply show equality. I use this symbol rather more liberally than is usual for emphasis. I use it even when the context is “local,” that is, I may simply define a function _𝑓_ ( _𝑥_ ) � _𝑥_[2] for a single exercise or example.

Finally, I would like to acknowledge Jana Maříková, Glen Pugh, Paul Vojta, Frank Beatrous, Sönmez Şahutoğlu, Jim Brandt, Kenji Kozai, Arthur Busch, Anton Petrunin, Mark Meilstrup, Harold P. Boas, Atilla Yılmaz, Thomas Mahoney, Scott Armstrong, and Paul Sacks, Matthias Weber, Manuele Santoprete, Robert Niemeyer, Amanullah Nabavi, for teaching with the book and giving me lots of useful feedback. Frank Beatrous wrote the University of Pittsburgh version extensions, which served as inspiration for many more recent additions. I would also like to thank Dan Stoneham, Jeremy Sutter, Eliya Gwetta, Daniel Pimentel-Alarcón, Steve Hoerning, Yi Zhang, Nicole Caviris, Kristopher Lee, Baoyue Bi, Hannah Lund, Trevor Mannella, Mitchel Meyer, Gregory Beauregard, Chase Meadors, Andreas Giannopoulos, Nick Nelsen, Ru Wang, Trevor Fancher, Brandon Tague, Wang KP, Wai Yan Pong, Sam Merat, Judah Nouriyelian, Arnold Cross, Jesse Wallace, Adnan Hashem Mohamed, Nikita Borisov, Bob Strain, Salven V. DeMartino, Xuechi Wang, an anonymous reader or two, and in general all the students in my classes for suggestions and finding errors and typos.

_0.2. ABOUT ANALYSIS_

7

## **0.2 About analysis**

Analysis is the branch of mathematics that deals with inequalities and limits. The present course deals with the most basic concepts in analysis. The goal of the course is to acquaint the reader with rigorous proofs in analysis and also to set a firm foundation for calculus of one variable (and several variables if volume II is also considered).

Calculus has prepared you, the student, for using mathematics without telling you why what you learned is true. To use, or teach, mathematics effectively, you cannot simply know _what_ is true, you must know _why_ it is true. This course shows you _why_ calculus is true. It is here to give you a good understanding of the concept of a limit, the derivative, and the integral.

Let us use an analogy. An auto mechanic who has learned to change the oil, fix broken headlights, and charge the battery, but who does not understand how the engine works, will only be able to do those simple tasks. He will be unable to work independently to diagnose and fix problems. A high school teacher who does not understand the definition of the Riemann integral or the derivative may not be able to properly answer all the students’ questions. To this day I remember several nonsensical statements I heard from my calculus teacher in high school, who simply did not understand the concept of the limit, although he could “do” the problems in the textbook.

We start with a discussion of the real number system, most importantly its completeness property, which is the basis for all that follows. We then discuss the simplest form of a limit, the limit of a sequence. Afterwards, we study functions of one variable, continuity, and the derivative. Next, we define the Riemann integral and prove the fundamental theorem of calculus. We discuss sequences of functions and the interchange of limits. Finally, we give an introduction to metric spaces.

Let us give the most important difference between analysis and algebra. In algebra, we prove equalities directly; we prove that an object, perhaps a number, is equal to another In we and we those object. analysis, usually prove inequalities, prove inequalities by estimating. To illustrate the point, consider the following statement.

_Let 𝑥 be a real number. If 𝑥 < 𝜖 is true for all real numbers 𝜖>_ 0 _, then 𝑥_ ≤ 0.

This statement is the general idea of what we do in analysis. Suppose we really wish to prove the equality _𝑥_ = 0. In analysis, we prove two inequalities: _𝑥_ ≤ 0 and _𝑥_ ≥ 0. To prove the inequality _𝑥_ ≤ 0, we prove _𝑥 < 𝜖_ for all positive _𝜖_ . To prove the inequality _𝑥_ ≥ 0, we prove _𝑥 >_ − _𝜖_ for all positive _𝜖_ .

The term _real analysis_ is a little bit of a misnomer. I prefer to use simply _analysis_ . The other type of analysis, _complex analysis_ , really builds up on the present material, rather than being distinct. Furthermore, a more advanced course on real analysis would talk about complex numbers often. I suspect the nomenclature is historical baggage.

Let us get on with the show. . .

_INTRODUCTION_

8

## **0.3 Basic set theory**

## _Note: 1–3 lectures (some material can be skipped, covered lightly, or left as reading)_

Modern Before we start talking about analysis, we need to fix some language. analysis uses the language of sets and, therefore, that is where we start. We talk about sets in a rather informal way, using the so-called “naïve set theory.” Do not worry, that is what the majority of mathematicians use, and it is hard to get into trouble. The reader has hopefully seen the very basics of set theory and proof writing before, and this section should be a quick refresher.

## **0.3.1 Sets**