(differential-geometry:lines)=
# Lines

Parametric representation of curve in 3-dimensional (Euclidean) space $E^3$

$$\vec{r}(q)$$

**Differential, $d \vec{r}$.**

$$d \vec{r}(q) = \vec{r}'(q) \, d q \ .$$

**Arc-length parameter, $s$.** So that $d s = |d \vec{r}(s)|$ and thus

$$|d \vec{r}(s)| = |\vec{r}'(s)| \, |d s| \qquad \rightarrow \qquad |\vec{r}'(s)| = 1 \qquad \rightarrow \qquad \vec{r}'(s) = \hat{t}(s) \ .$$

**Frenet basis.** Using arc-length parameter, Frenet basis is naturally defined as the set $\{ \hat{t}, \hat{n}, \hat{b} \}$:
- tangent unit vector, $\hat{t}(s) = \vec{r}'(s)$,
- normal unit vector, $\hat{r}''(s) = \hat{t}'(s) =: \kappa(s) \, \hat{n}(s) $, with $\kappa(s)$ local curvature
- binormal unit vector, $\hat{b}(s) = \hat{t}(s) \times \hat{n}(s)$

Using a general parameter, $t$, with some abuse of notation $\vec{r}(t) = \vec{r}(s(t))$ and indicating $\dot{()} = \frac{d}{dt}$,
- $\dot{\vec{r}} = \frac{d s}{d t} \frac{d \vec{r}}{d s} = \dot{s} \hat{t}$
- $\ddot{\vec{r}} = \dfrac{d}{dt} \dot{\vec{r}} = \dfrac{d}{dt} \left( \dot{s} \hat{t} \right) = \ddot{s} \hat{t} + \dfrac{ds}{dt} \dfrac{d}{ds} \hat{t} = \ddot{s} \hat{t} + \dot{s}^2 \kappa \, \hat{n}$

**Osculator circle.** Circle with $R(s) = \frac{1}{\kappa(s)}$, in plane orthogonal to $\hat{b}(s)$, passing through $\vec{r}(s)$, and thus center in $\vec{r}_C(s) = \vec{r}(s) + \hat{n} R(s)$. Its parametric representation using its arc-length parameter $p$, with $\vec{r}(p=0) = \vec{r}(s)$ reads 

$$\vec{r}(p) = \vec{r}_C(s) + R(s) \left[ - \cos \left(\frac{p}{R(s)} \right) \hat{n}(s) + \sin \left(\frac{p}{R(s)}  \right)\hat{t}(s) \right] \ .$$

Its first and second order derivatives w.r.t. the arc-length $p$ evaluated in $p=0$, i.e. $\vec{r} = \vec{r}(s)$ read:

- first derivative in $p=0$,

  $$\left.\hat{t}(p)\right|_{p=0} = \left.\vec{r}'(p)\right|_{p=0} = \left.  \left[ \sin \left(\frac{p}{R(s)} \right) \hat{n}(s) + \cos \left(\frac{p}{R(s)}  \right)\hat{t}(s) \right] \right|_{p=0} = \hat{t}(s) \ ,$$

  i.e. the osculator circle has the same tangent as the curve in the point.

- second derivative in $p=0$,

  $$\left. \kappa(p) \hat{n}(p)\right|_{p=0} = \left.\vec{r}''(p)\right|_{p=0} = \frac{1}{R(s)} \left.  \left[ \cos \left(\frac{p}{R(s)} \right) \hat{n}(s) - \sin \left(\frac{p}{R(s)}  \right)\hat{t}(s) \right] \right|_{p=0} = \frac{1}{R(s)}\hat{n}(s) = \kappa(s) \hat{n}(s) \ ,$$

  i.e. the osculator circle has the same normal vector and curvature as the curve in the point.


