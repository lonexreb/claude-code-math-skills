Example 7.1.9

**Example 7.1.9:** Another useful example of a metric space is the sphere with a metric usually called the _great circle distance_ . Let _𝑆_[2] be the unit sphere in ℝ[3] , that is _𝑆_[2] � { _𝑥_ ∈ ℝ[3] : _𝑥_[2][1][}][.][Take] _[𝑥]_[and] _[𝑦]_[in] _[𝑆]_[2][,][draw][a][line][through][the][origin][and] _[𝑥]_[,][and] 1[+] _[ 𝑥]_ 2[2][+] _[ 𝑥]_ 3[2][=] another line through the origin and _𝑦_ , and let _𝜃_ be the angle that the two lines make. Then define _𝑑_ ( _𝑥, 𝑦_ ) � _𝜃_ . See . The law of cosines from vector calculus says _𝑑_ ( _𝑥, 𝑦_ ) = arccos( _𝑥_ 1 _𝑦_ 1 + _𝑥_ 2 _𝑦_ 2 + _𝑥_ 3 _𝑦_ 3). It is relatively easy to see that this function satisfies the first three properties of a metric. Triangle inequality is harder to prove, and requires a bit more trigonometry and linear algebra than we wish to indulge in right now, so let us leave it without proof.

**==> picture [103 x 96] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑥<br>𝑆 [2]<br>𝜃<br>𝑦<br>0<br>**----- End of picture text -----**<br>


**Figure 7.4:** The great circle distance on the unit sphere.

This distance is the shortest distance between points on a sphere if we are allowed to travel on the sphere only. It is easy to generalize to arbitrary diameters. If we take a sphere of radius _𝑟_ , we let the distance be _𝑑_ ( _𝑥, 𝑦_ ) � _𝑟𝜃_ . As an example, this is the standard distance you would use if you compute a distance on the surface of the earth, such as computing the distance a plane travels from London to Los Angeles.

_7.1. METRIC SPACES_

261

Oftentimes it is useful to consider a subset of a larger metric space as a metric space itself. We obtain the following proposition, which has a trivial proof.