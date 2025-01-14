(differential-geometry:intro)=
# Introduction to Differential Geometry

## Differential geometry in $E^3$

### Curves

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

### Surfaces

$$\vec{r}(q^1, q^2)$$

$$d \vec{r} =
  \frac{\partial \vec{r}}{\partial q^1} \, d q^1 + \frac{\partial \vec{r}}{\partial q^2} \, d q^2 =
  \vec{b}_1 \, d q^1 + \vec{b}_2 \, d q^2
$$

A third vector $\vec{b}_3 := \hat{n}$ can be defined so that $|\hat{n}| = 1$ and $\hat{n} \cdot \vec{b}_{i} = 0$, $i=1:2$. For $i=1:2$, $k=1:2$

$$\frac{\partial \vec{b}_i}{\partial q^j} = \Gamma_{ij}^k \vec{b}_k = \Gamma_{ij}^1 \vec{b}_1 + \Gamma_{ij}^2 \vec{b}_2 + \Gamma_{ij}^3 \vec{b}_3$$

so that

$$\Gamma_{ij}^{k} = \vec{b}^k \cdot \frac{\partial \vec{b}_i}{\partial q^j}$$

**Normal vector.** 

$$\vec{n}(q^1, q^2) = \frac{\partial \vec{r}}{\partial q^1}(q^1, q^2) \times \frac{\partial \vec{r}}{\partial q^2}(q^1, q^2) = \vec{b}_1(q^1, q^2) \times \vec{b}_2(q^1, q^2)$$

**Tangent plane.** 

$$(\vec{r} - \vec{r}(q^1, q^2)) \cdot \vec{n}(q^1, q^2) = 0$$

**Length of elementary segment.**

$$\begin{aligned}
|d \vec{r}|^2 
  & = d \vec{r} \cdot d \vec{r} = \\
  & = \left( \vec{b}_1 \, d q^1 + \vec{b}_2 \, d q^2 \right) \cdot \left( \vec{b}_1 \, d q^1 + \vec{b}_2 \, d q^2 \right) = \\
  & = g_{11} \, dq^1 \, dq^1 + g_{12} \, dq^1 \, dq^2 + g_{21} \, dq^2 \, dq^1 + g_{22} \, dq^2 \, d q^2 = g_{ij} \, dq^i \, dq^j 
\end{aligned}$$

**Second order approximation.**

$$\begin{aligned}
  \vec{r}(q^1 + d q^1, q^2 + d q^2) 
  & = \vec{r}(q_1, q_2) + \frac{\partial \vec{r}}{\partial q^i} \, dq^i + \frac{\partial^2 \vec{r}}{\partial q^i \partial q^j} \, dq^i \, dq^j = \\
  & = \vec{r}(q_1, q_2) + \vec{b}_{i} \, dq^i + \vec{b}_k \Gamma^{k}_{ij} \, dq^i \, dq^j +  \hat{n} \, \Gamma^{3}_{ij} \, dq^i \, dq^j 
\end{aligned}$$

so that

$$\begin{aligned}
\left[ \vec{r}(q^1 + d q^1, q^2 + d q^2) - \vec{r}(q^1, q^2) \right] \cdot \hat{n} 
 & = \Gamma^3_{ij} \, d q^i \, dq^j = \\
 & = \hat{n} \cdot \frac{\partial^2 \vec{r}}{\partial q^i \partial q^j} \, d q^i \, dq^j = \\
 & = \hat{n} \cdot \frac{\partial^2 \vec{r}}{\partial q^i \partial q^j} \, \vec{b}^i \cdot \vec{b}_k d q^k \, \vec{b}^j \cdot \vec{b}_l dq^l = \\
 & = \underbrace{d q^k \vec{b}_k}_{d \vec{r}} \cdot \left[ \hat{n} \cdot \frac{\partial^2 \vec{r}}{\partial q^i \partial q^j}  \vec{b}^i \otimes \vec{b}^j \right] \cdot \underbrace{d q^l \vec{b}_l}_{d\vec{r}}
\end{aligned}$$

**Curvature tensor.**
