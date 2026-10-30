(differential-geometry:lines)=
# Lines

A line $\gamma$ is a geometric entity that has a 1-parameter parametric representation. Its points in 3-dimensional (Euclidean) space $E^3$ can be represented with the function

$$\gamma: \ \mathbf{r}(q) \ , \quad q \in [q_0, q_1] \ .$$

A parametrization is regular if the parameter $q$ is monotonic along the curve.

(differential-geometry:lines:differential)=
## Differential

The differential $d \mathbf{r}$ represents the elementary vector on the line. From the very definition of the differential of a function, it follows

$$d \mathbf{r}(q) = \mathbf{r}'(q) \, d q \ .$$

```{prf:definition} Arc-length parameter
:label: def-arc-length

The arc-length parameter $s$ is defined by the condition $d s = |d \mathbf{r}(s)|$, or by the equivalent conditions

$$|d \mathbf{r}(s)| = |\mathbf{r}'(s)| \, |d s| \qquad \rightarrow \qquad |\mathbf{r}'(s)| = 1 \qquad \rightarrow \qquad \mathbf{r}'(s) = \hat{\mathbf{t}}(s) \ .$$

```

(differential-geometry:lines:frenet-basis)=
## Frenet basis

Using **arc-length parameter** {prf:ref}`def-arc-length`, Frenet basis is naturally defined as the set $\{ \hat{\mathbf{t}}, \hat{\mathbf{n}}, \hat{\mathbf{b}} \}$:
- tangent unit vector, $\hat{\mathbf{t}}(s) = \mathbf{r}'(s)$,
- normal unit vector, $\hat{\mathbf{n}}$, so that $\hat{\mathbf{r}}''(s) = \hat{\mathbf{t}}'(s) =: \kappa(s) \, \hat{\mathbf{n}}(s) $, with $\kappa(s)$ local curvature
- binormal unit vector, $\hat{\mathbf{b}}(s) = \hat{\mathbf{t}}(s) \times \hat{\mathbf{n}}(s)$

Using a general parameter, $t$, with some abuse of notation $\mathbf{r}(t) = \mathbf{r}(s(t))$ and indicating $\dot{( \_ )} = \frac{d \_}{dt}$,
- $\dot{\mathbf{r}} = \frac{d s}{d t} \frac{d \mathbf{r}}{d s} = \dot{s} \hat{\mathbf{t}}$
- $\ddot{\mathbf{r}} = \dfrac{d}{dt} \dot{\mathbf{r}} = \dfrac{d}{dt} \left( \dot{s} \hat{\mathbf{t}} \right) = \ddot{s} \hat{\mathbf{t}} + \dfrac{ds}{dt} \dfrac{d}{ds} \hat{\mathbf{t}} = \ddot{s} \hat{\mathbf{t}} + \dot{s}^2 \kappa \, \hat{\mathbf{n}}$

```{prf:definition} Osculator circle
:label: def-osculator-circle

The osculator circle relative to a point $P$ of a curve $\gamma$, its the circle that:
* is tangent to the curve $\gamma$ in $P$
* has the same curvature of the curve $\gamma$ in $P$ 

```

```{dropdown} Osculator circle - Details
:open:

Circle with $R(s) = \frac{1}{\kappa(s)}$, in plane orthogonal to $\hat{\mathbf{b}}(s)$, passing through $\mathbf{r}(s)$, and thus center in $\mathbf{r}_C(s) = \mathbf{r}(s) + \hat{\mathbf{n}} R(s)$. Its parametric representation using its arc-length parameter $p$, with $\mathbf{r}(p=0) = \mathbf{r}(s)$ reads 

$$\mathbf{r}(p) = \mathbf{r}_C(s) + R(s) \left[ - \cos \left(\frac{p}{R(s)} \right) \hat{\mathbf{n}}(s) + \sin \left(\frac{p}{R(s)}  \right)\hat{\mathbf{t}}(s) \right] \ .$$

Its first and second order derivatives w.r.t. the arc-length $p$ evaluated in $p=0$, i.e. $\mathbf{r} = \mathbf{r}(s)$ read:

- first derivative in $p=0$,

  $$\left.\hat{\mathbf{t}}(p)\right|_{p=0} = \left.\mathbf{r}'(p)\right|_{p=0} = \left.  \left[ \sin \left(\frac{p}{R(s)} \right) \hat{\mathbf{n}}(s) + \cos \left(\frac{p}{R(s)}  \right)\hat{\mathbf{t}}(s) \right] \right|_{p=0} = \hat{\mathbf{t}}(s) \ ,$$

  i.e. the osculator circle has the same tangent as the curve in the point.

- second derivative in $p=0$,

  $$\left. \kappa(p) \hat{\mathbf{n}}(p)\right|_{p=0} = \left.\mathbf{r}''(p)\right|_{p=0} = \frac{1}{R(s)} \left.  \left[ \cos \left(\frac{p}{R(s)} \right) \hat{\mathbf{n}}(s) - \sin \left(\frac{p}{R(s)}  \right)\hat{\mathbf{t}}(s) \right] \right|_{p=0} = \frac{1}{R(s)}\hat{\mathbf{n}}(s) = \kappa(s) \hat{\mathbf{n}}(s) \ ,$$

  i.e. the osculator circle has the same normal vector and curvature as the curve in the point.

```

