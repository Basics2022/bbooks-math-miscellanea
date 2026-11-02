(differential-geometry:curvature)=
# Curvature

This section is devoted to curvature, and its different descriptions:
* [**Extrinsic curvature**](differential-geometry:curvature:extrinsic), i.e. the description of the curvature of a $n$-manifold embedded in a $n+1$-space, as it's usually done in the description of [2-dimensional surfaces in the 3-dimensional Euclidean space](differential-geometry:surfaces).
* [**Intrinsic curvature**](differential-geometry:curvature:intrinsic), i.e. the description of a curvature of a $n$-manifold without the need for an embedding in a higher-dimensional space. This approach exploits the concepts of parallel transport, that - when applied to a vector field on a closed loop, see [Parallel transport around a closed loop and the Riemann tensor](differential-geometry:curvature:intrinsic:riemann-curvature-tensor:riemann-tensor) - provides the definition of Riemann tensor, {prf:ref}`def-differential-geometry-riemann-tensor`.

(differential-geometry:curvature:extrinsic)=
## Extrinsic curvature

Extrinsic curvature of a $n$-dimensional manifold needs the manifold to be embedded in a $n+1$-dimensional space.

From the second order approximation of the $n$-dimensional manifold $\mathbf{r}\left( q^i \right)$ in a $n+1$-dimensional space

$$\begin{aligned}
\mathbf{r}\left( q^i + d q^i \right) - \mathbf{r}\left( q^i \right) 
& = \frac{\partial \mathbf{r}}{\partial q^i} d q^i + 
\frac{1}{2} \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^k} d q^i d q^k + o(|d \mathbf{q}|^2) = \\
& = \mathbf{b}_i \, d q^i + \frac{1}{2} \Gamma_{ik}^{\alpha} \mathbf{b}_{\alpha} \, dq^i dq^k = \\
& = \mathbf{b}_i \, d q^i + \frac{1}{2} \left( \Gamma_{ik}^{l} \mathbf{b}_{l} + \Gamma_{ik}^{n+1} \mathbf{n} \right) \, dq^i dq^k \ ,
\end{aligned}$$

with the Greek indices for sum over the $n+1$ dimensions, and latin indices for the indices in $\{ 1, \dots, n \}$. Here $\mathbf{n} := \mathbf{b}_{n+1}$ s.t. $\mathbf{n} \cdot \mathbf{b}_i = 0$, for $n \in \{ 1, \dots, n \}$.

The extrinsic curvature tensor, already used for [differential geometry of surfaces](differential-geometry:surfaces), is defined as $\mathbb{b} := \Gamma^{n+1}_{ik} \mathbf{b}^i \otimes \mathbf{b}^k$.

````{dropdown} Derivatives of the normal vector - Weingarten formula
:open:

The spatial derivatives of the unit normal vector $\hat{\mathbf{n}}(q^i)$ reads

$$\frac{\partial \hat{\mathbf{n}}}{\partial q^i} = -b_{i}^{\,\,l} \mathbf{b}_l \ .$$ (eq:differential-geometry:curvature:weingarten)

```{dropdown} Proof

Consider an $n$-dimensional hypersurface embedded in an $(n+1)$-dimensional space with normal vector $\hat{\mathbf{n}}$ satisfying $\hat{\mathbf{n}} \cdot \mathbf{b}_i = 0$. The derivative of basis vectors decomposes into tangential and normal components:

$$\frac{\partial \mathbf{b}_i}{\partial q^k} = \Gamma^{\alpha}_{ik} \mathbf{b}_{\alpha} = \Gamma^l_{ik} \mathbf{b}_l + \Gamma^{n+1}_{ik} \hat{\mathbf{n}}$$

Differentiating the normality condition $\hat{\mathbf{n}} \cdot \mathbf{b}_k = 0$ with respect to $q^i$,

$$\begin{aligned}
  0
  & = \frac{\partial \hat{\mathbf{n}}}{\partial q^i} \cdot \mathbf{b}_k + \hat{\mathbf{n}} \cdot \frac{\partial \mathbf{b}_k}{\partial q^i} = \\
  & = \frac{\partial \hat{\mathbf{n}}}{\partial q^i} \cdot \mathbf{b}_k + \hat{\mathbf{n}} \cdot \left( \Gamma^l_{ik} \mathbf{b}_l + \Gamma^{n+1}_{ik} \hat{\mathbf{n}} \right) \ ,
\end{aligned}$$

or

$$\frac{\partial \hat{\mathbf{n}}}{\partial q^i} \cdot \mathbf{b}_k = -\hat{\mathbf{n}} \cdot \left( \Gamma^l_{ik} \mathbf{b}_l + \Gamma^{n+1}_{ik} \hat{\mathbf{n}} \right) = -\Gamma^{n+1}_{ik}$$

From the latter expression, it immediately follows

$$\frac{\partial \hat{\mathbf{n}}}{\partial q^i} = -\Gamma^{n+1}_{ik} \mathbf{b}^k = -g^{kl} \Gamma^{n+1}_{ik} \mathbf{b}_l = -b_{i}^{\,\,l} \mathbf{b}_l \ ,$$ 

where $b_{ik} = \Gamma^{n+1}_{ik}$ is the **second fundamental form**.

<!--

If the normal coordinate is choosen so that the normal vector is unitary, $\mathbf{b}_{n+1} = \hat{\mathbf{n}}$, then

$$0 = \partial_i | \hat{\mathbf{n}} |^2 = 2 \hat{\mathbf{n}} \cdot \partial_i \hat{\mathbf{n}} \ .$$

-->
```

````

(differential-geometry:curvature:intrinsic)=
## Intrinsic curvature

Intrinsic curvature of a $n$-dimensional manifold doesn't need any embedding in a higher dimensional space, but it's built from the metric $g_{\mu \nu}$ and its derivatives. It measures...

<div style="color:red"> <b>todo</b> Relation with parallel transport and geodesic convergence/divergence. Add some illutrative examples/visualizations,...</div>

(differential-geometry:curvature:intrinsic:riemann-curvature-tensor)=
### Riemann curvature tensor

(differential-geometry:curvature:intrinsic:riemann-curvature-tensor:vector-fields)=
#### Vector fields as differential operators, and directional or covariant derivatives

A vector field $X(f)$ acting on a scalar function $f$ defines a directional derivative:

$$X(f) = X^\mu \partial_\mu f \ .$$ (eq:curvature:vector-field-operator)

The definition of the vector field $X$ as a differential operator can be recast as the scalar product of the vector field $\mathbf{X}$ and the gradient of the function $f$,

$$\nabla_{X} f = \mathbf{X} \cdot \nabla f \ .$$

The **directional derivative** of the function $f$ along a curve $\gamma$ with element $d \mathbf{r}$ is $d \mathbf{r} \cdot \nabla f$. So, for a scalar field $f$,

$$\begin{aligned}
      d\mathbf{r} \cdot \nabla f
  & = \left( d q^\nu \mathbf{b}_\nu \right) \cdot \mathbf{b}^\mu \partial_{\mu} f 
    =        d q^\mu \partial_{\mu} f \ . 
\end{aligned}$$

For a vector field $\mathbf{v}$,

$$\begin{aligned}
      d\mathbf{r} \cdot \nabla \mathbf{v} 
  & = \left( d q^\nu \mathbf{b}_\nu \right) \cdot \mathbf{b}^\mu \partial_{\mu} \mathbf{v} = \\ 
  & = d q^\mu \partial_{\mu} \mathbf{v} = \\
  & =  d q^{\mu} \left( \partial_{\mu} v^{\nu} + \Gamma_{\xi \mu}^{\nu} v^{\xi} \right) \mathbf{b}_{\nu} \ .
\end{aligned}$$ (eq:differential-geometry:curvature:directional-derivative:vector)

(differential-geometry:curvature:intrinsic:riemann-curvature-tensor:parallel-transport)=
#### Parallel transport

A vector field $\mathbf{v}$ is parallel transported along a curve $\gamma$ with element $d\mathbf{r}$ if $d \mathbf{r} \cdot \nabla f = \mathbf{0}$. Thus, using the relation {eq}`eq:differential-geometry:curvature:directional-derivative:vector`, parallel transport implies

$$\begin{aligned}
\partial_{\mu} v^{\nu} = - \Gamma_{\xi \mu}^{\nu} v^{\xi} \ .
\end{aligned}$$ (eq:differential-geometry:curvature:parallel-transport:component-increment)

To first order, the transported vector $v^\mu$ from $q^\eta$ to $q^\eta + dq^\eta$ satisfies:

$$v^\nu(q^\eta + d q^\eta) \sim v^\nu(q^\eta) + dq^\mu \partial_{\mu} v^\nu(q^\eta) = v^\nu(q^\eta) - dq^\mu \Gamma_{\mu \chi}^{\nu}(q^\eta) v^\chi(q^\eta)\ .$$


(differential-geometry:curvature:intrinsic:riemann-curvature-tensor:lie-bracket)=
#### Lie bracket

The Lie bracket of two vector fields $X$ and $Y$ measures their non-commutativity, i.e.

$$[X, Y]f = X(Y(f)) - Y(X(f)) \ .$$

In component notation, applying the definition {eq}`eq:curvature:vector-field-operator` of a vector field as differential operator twice,

$$\begin{aligned}
 \left[ X, Y \right] f
 & = X^\mu \partial_\mu (Y^\nu \partial_\nu f) - Y^\nu \partial_\nu (X^\mu \partial_\mu f) = \\
 & = X^\mu \partial_\mu Y^\nu \partial_\nu f + X^{\mu} Y^{\nu} \partial_{\mu \nu}f - Y^\nu \partial_\nu (X^\mu \partial_\mu f) - X^{\mu} Y^{\nu} \partial_{\mu \nu}f= \\
 & = (X^\nu \partial_\nu Y^\mu - Y^\nu \partial_\nu X^\mu) \partial_\mu f \ ,
\end{aligned}$$

so that the components of the vector field $[X, Y]$ in the natural basis are

$$[X, Y]^\mu = X^\nu \partial_\nu Y^\mu - Y^\nu \partial_\nu X^\mu \ .$$

(differential-geometry:curvature:intrinsic:riemann-curvature-tensor:riemann-tensor)=
#### Parallel transport around a closed loop and the Riemann tensor

##### Elementary loop

The elementary loop is build with 2 vector fields $X$, $Y$. In general, the elementary loops need $5$ sides if the vector fields $X$, $Y$ don't commute. Let (**todo** *Add some details, and pay attention to notation, as it can be non-trivial for curved spaces*) 

* point **A** be in $\mathbf{r}_A$
* point **B** be in $\mathbf{r}_B = \mathbf{r}_A + \mathbf{X}(\mathbf{r}_A)$
* point **C** be in $\mathbf{r}_C = \mathbf{r}_B + \mathbf{Y}(\mathbf{r}_B) = \mathbf{r}_A + \mathbf{X}(\mathbf{r}_A) + \mathbf{Y}(\mathbf{r}_A + \mathbf{X}(\mathbf{r}_A))$
* point **D** be in $\mathbf{r}_D = \mathbf{r}_A + \mathbf{Y}(\mathbf{r}_A)$
* point **E** be in $\mathbf{r}_E = \mathbf{r}_D + \mathbf{X}(\mathbf{r}_D) = \mathbf{r}_A + \mathbf{Y}(\mathbf{r}_A) + \mathbf{X}(\mathbf{r}_A + \mathbf{Y}(\mathbf{r}_A))$

The - maybe unexpected fifth side - is required when $\mathbf{r}_E \ne \mathbf{r}_C$, i.e. when

$$\begin{aligned}
  \mathbf{0} \ne \mathbf{r}_E - \mathbf{r}_C
  & = \left\{ \mathbf{r}_A + \mathbf{Y}(\mathbf{r}_A) + \mathbf{X}(\mathbf{r}_A) + \mathbf{Y}(\mathbf{r}_A) \cdot \nabla \mathbf{X}(\mathbf{r}_A) \right\} + \\
  & \quad - \left\{ \mathbf{r}_A + \mathbf{X}(\mathbf{r}_A) + \mathbf{Y}(\mathbf{r}_A) + \mathbf{X}(\mathbf{r}_A) \cdot \nabla \mathbf{Y}(\mathbf{r}_A ) \right\} + o(|\mathbf{X}||\mathbf{Y}|) = \\
  & = \mathbf{Y}(\mathbf{r}_A) \cdot \nabla \mathbf{X}(\mathbf{r}_A) - \mathbf{X}(\mathbf{r}_A) \cdot \nabla \mathbf{Y}(\mathbf{r}_A) \ .
\end{aligned}$$

or, in components

$$\begin{aligned}
  \mathbf{0} \ne \mathbf{r}_E - \mathbf{r}_C
  & = Y^{\nu} \partial_{\nu} \left( X^{\mu} \mathbf{b}_{\mu} \right) - X^{\nu} \partial_{\nu} \left( Y^{\mu} \mathbf{b}_{\mu} \right) = \\
  & = \left[ Y^{\nu} \left( \partial_{\nu} X^{\mu} + \Gamma_{\nu \xi}^{\mu} X^{\xi} \right) - X^{\nu} \left( \partial_{\nu} Y^{\mu} + \Gamma_{\nu \xi}^{\mu} Y^{\xi} \right) \right] \mathbf{b}_{\mu} = \\
  & = - (X^\nu \partial_\nu Y^\mu - Y^\nu \partial_\nu X^\mu) \mathbf{b}_{\mu} = \\
  & = - [ X, Y ]^{\mu} \mathbf{b}_{\mu} = - [ X, Y] \ ,
\end{aligned}$$

i.e. when $X$, $Y$ don't commute, as stated above.

```{prf:example} Coordinates vector fields commute, and thus only 4 sides are required to build the loop

...

$$[ X, Y ] = 0$$

...

```

<!--
Consider transport along an infinitesimal quadrilateral formed by displacements along vector fields $X$ and $Y$:

* **Path A $\rightarrow$ B $\rightarrow$ C:** Parallel transport first along $X$, then along $Y$.
* **Path A $\rightarrow$ D $\rightarrow$ C:** Parallel transport first along $Y$, then along $X$.
-->

The discrepancy (holonomy) after completing the loop gives rise to curvature.

##### Parallel transport along a closed path

**Path A to C: first along $\mathbf{X}(\mathbf{r})$ then along to $\mathbf{Y}(\mathbf{r}+\mathbf{X}(\mathbf{r}))$.**

$$\begin{aligned}
  \left( \mathbf{v}_{||\mathbf{X}} \right)_{||\mathbf{Y}} 
  & = \mathbf{b}_\nu \Big[ v^\nu - X^\mu \Gamma^\nu_{\mu\xi} v^\xi - Y^\mu \Gamma^\nu_{\mu\xi} v^\xi - X^\alpha \left( \partial_\alpha Y^\mu + \Gamma^\mu_{\alpha\phi} Y^\phi \right) \Gamma^\nu_{\mu\xi} v^\xi + \\
  & \qquad - Y^\mu X^\alpha \partial_\alpha \Gamma^\nu_{\mu\xi} v^\xi + Y^\mu X^\alpha \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta + X^\alpha X^\mu (\partial_\alpha Y^\mu + \Gamma^\mu_{\alpha\phi} Y^\phi) \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta \Big] = \\
  & \sim \mathbf{b}_\nu \Big[ v^\nu - X^\mu \Gamma^\nu_{\mu\xi} v^\xi - Y^\mu \Gamma^\nu_{\mu\xi} v^\xi - X^\alpha \left( \partial_\alpha Y^\mu + \Gamma^\mu_{\alpha\phi} Y^\phi \right) \Gamma^\nu_{\mu\xi} v^\xi + \\
  & \qquad - Y^\mu X^\alpha \partial_\alpha \Gamma^\nu_{\mu\xi} v^\xi + Y^\mu X^\alpha \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta \Big]
\end{aligned}$$

```{dropdown} Details

First transport along $\mathbf{X}$, using {eq}`eq:differential-geometry:curvature:parallel-transport:component-increment`,

$$\mathbf{v}_{||\mathbf{X}} = \mathbf{b}_{\nu} \left( v^{\nu} + X^{\mu} \left\{ \partial_{\mu} v^{\nu} \right\}_{\parallel} \right) = \mathbf{b}_{\nu} \left( v^{\nu} - X^{\mu} \Gamma_{\mu \xi}^{\nu} v^{\xi} \right) \ .$$

and then along $\mathbf{Y}(\mathbf{r} + \mathbf{X})$. Expanding $\left( \mathbf{v}_{||\mathbf{X}} \right)_{||\mathbf{Y}}$ to second order in components:

$$\begin{aligned}
  \left( \mathbf{v}_{||\mathbf{X}} \right)_{||\mathbf{Y}} 
  & = \mathbf{b}_\nu \left[ v^\nu - X^\mu \Gamma^\nu_{\mu\xi} v^\xi - \left( Y^\mu + X^\alpha (\partial_\alpha Y^\mu + \Gamma^\mu_{\alpha\phi} Y^\phi) \right) \left( \Gamma^\nu_{\mu\xi} + X^\alpha \partial_\alpha \Gamma^\nu_{\mu\xi} \right) \left( v^\xi - X^\mu \Gamma^\xi_{\mu\eta} v^\eta \right) \right]
\end{aligned}$$

Expanding terms explicitly:

$$\begin{aligned}
  \left( \mathbf{v}_{||\mathbf{X}} \right)_{||\mathbf{Y}} 
  & = \mathbf{b}_\nu \Big[ v^\nu - X^\mu \Gamma^\nu_{\mu\xi} v^\xi - Y^\mu \Gamma^\nu_{\mu\xi} v^\xi - X^\alpha \left( \partial_\alpha Y^\mu + \Gamma^\mu_{\alpha\phi} Y^\phi \right) \Gamma^\nu_{\mu\xi} v^\xi + \\
  & \qquad - Y^\mu X^\alpha \partial_\alpha \Gamma^\nu_{\mu\xi} v^\xi + Y^\mu X^\alpha \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta + X^\alpha X^\mu (\partial_\alpha Y^\mu + \Gamma^\mu_{\alpha\phi} Y^\phi) \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta \Big]
\end{aligned}$$

```

**A to C to E, to second order.**

$$\begin{aligned}
  \left( \left( \mathbf{v}_{||\mathbf{X}} \right)_{||\mathbf{Y}} \right)_{|| [Y,X]}
  & = \mathbf{b}_\nu \Big[  \left\{ \left( \mathbf{v}_{||\mathbf{X}} \right)_{||\mathbf{Y}} \right\}^{\nu} + [ X, Y ]^{\mu} \Gamma^{\nu}_{\mu \xi} \left\{ \left( \mathbf{v}_{||\mathbf{X}} \right)_{||\mathbf{Y}} \right\}^{\xi} \Big] = \\
  & \sim \mathbf{b}_\nu \Big[ v^\nu - X^\mu \Gamma^\nu_{\mu\xi} v^\xi - Y^\mu \Gamma^\nu_{\mu\xi} v^\xi - X^\alpha \left( \partial_\alpha Y^\mu + \Gamma^\mu_{\alpha\eta} Y^\eta \right) \Gamma^\nu_{\mu\xi} v^\xi + \\
  & \qquad - Y^\mu X^\alpha \partial_\alpha \Gamma^\nu_{\mu\xi} v^\xi + Y^\mu X^\alpha \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta + \left(  X^\alpha \partial_\alpha Y^{\mu} - Y^\alpha \partial_\alpha X^{\mu} \right) \Gamma^{\nu}_{\mu \xi} v^\xi \Big]
\end{aligned}$$


**Path A to E: first along $\mathbf{Y}(\mathbf{r})$ then along to $\mathbf{X}(\mathbf{r}+\mathbf{Y}(\mathbf{r}))$.** Just swapping the $X$, $Y$

$$\begin{aligned}
  \left( \mathbf{v}_{||\mathbf{Y}} \right)_{||\mathbf{X}} 
  & = \mathbf{b}_\nu \Big[ v^\nu - Y^\mu \Gamma^\nu_{\mu\xi} v^\xi - X^\mu \Gamma^\nu_{\mu\xi} v^\xi - Y^\alpha \left( \partial_\alpha X^\mu + \Gamma^\mu_{\alpha\eta} X^\eta \right) \Gamma^\nu_{\mu\xi} v^\xi + \\
  & \qquad - X^\mu Y^\alpha \partial_\alpha \Gamma^\nu_{\mu\xi} v^\xi + X^\mu Y^\alpha \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta + Y^\alpha Y^\mu (\partial_\alpha X^\mu + \Gamma^\mu_{\alpha\eta} X^\eta) \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta \Big] = \\
  & \sim \mathbf{b}_\nu \Big[ v^\nu - Y^\mu \Gamma^\nu_{\mu\xi} v^\xi - X^\mu \Gamma^\nu_{\mu\xi} v^\xi - Y^\alpha \left( \partial_\alpha X^\mu + \Gamma^\mu_{\alpha\eta} X^\eta \right) \Gamma^\nu_{\mu\xi} v^\xi + \\
  & \qquad - X^\mu Y^\alpha \partial_\alpha \Gamma^\nu_{\mu\xi} v^\xi + X^\mu Y^\alpha \Gamma^\nu_{\mu\xi} \Gamma^\xi_{\alpha\eta} v^\eta \Big]
\end{aligned}$$


**Difference path $\text{A} \rightarrow \text{B} \rightarrow \text{C} \rightarrow \text{E}$ - path $\text{A} \rightarrow \text{D} \rightarrow \text{E}$ to second order.**

Subtracting Path B from Path A yields, as the travelling direction during the closed path is the opposite,:

$$\begin{aligned}
  (A - B)^\nu
  & = \underbrace{ - X^\alpha \partial_\alpha Y^\mu \Gamma^\nu_{\mu\xi} v^\xi }_{ i_{[X,Y],2} }  - \underbrace{X^\alpha Y^\beta \Gamma^\mu_{\alpha\beta}  \Gamma^\nu_{\mu\xi} v^\xi }_{ 1 } + \underbrace{ Y^\alpha \partial_\alpha X^\mu \Gamma^\nu_{\mu\xi} v^\xi }_{ i_{[X,Y],1} } + \underbrace{ X^\alpha Y^\beta  \Gamma^\mu_{\beta\alpha} \Gamma^\nu_{\mu\xi} v^\xi }_{ 1 } + \\
  & \quad \ + \underbrace{ \left(  X^\alpha \partial_\alpha Y^{\mu} - Y^\alpha \partial_\alpha X^{\mu} \right) \Gamma^{\nu}_{\mu \xi} v^\xi }_{ i_{[X,Y]} } + \\ 
  & \quad \ + X^\alpha Y^\beta \Gamma^\nu_{\beta\eta} \Gamma^\eta_{\alpha\xi} v^\xi - X^\alpha Y^\beta \Gamma^\nu_{\alpha\eta} \Gamma^\eta_{\beta\xi} v^\xi - X^\alpha Y^\beta \partial_\alpha \Gamma^\nu_{\beta \xi} v^\xi + X^\alpha Y^\beta \partial_\beta \Gamma^\nu_{\alpha\xi} v^\xi + \text{higher order terms} = \\ 
  & \sim - \left[ \partial_{\alpha} \Gamma^{\nu}_{\beta \xi} - \partial_{\beta} \Gamma^{\nu}_{\alpha \xi} + \Gamma_{\alpha \eta}^{\nu} \Gamma_{\beta \xi}^{\eta} - \Gamma_{\beta \eta}^{\nu} \Gamma_{\alpha \xi}^{\eta} \right] X^{\alpha} Y^{\beta} v^{\xi} = \\
  & = - R^{\nu}_{\ \ \alpha \beta \xi} X^\alpha Y^\beta v^\xi \ ,
\end{aligned}$$

having introduced the definition of the **Riemann tensor**, $R^{\nu}_{\ \ \alpha \beta \xi}$.

```{prf:definition} Riemann tensor
:label: def-differential-geometry-riemann-tensor

$$R^{\nu}_{\ \ \alpha \beta \xi} := \partial_{\alpha} \Gamma^{\nu}_{\beta \xi} - \partial_{\beta} \Gamma^{\nu}_{\alpha \xi} + \Gamma_{\alpha \eta}^{\nu} \Gamma_{\beta \xi}^{\eta} - \Gamma_{\beta \eta}^{\nu} \Gamma_{\alpha \xi}^{\eta} \ . $$

```

**Remark.** The contribution of the Lie bracket, required to close the loop, annihilates with other two terms.

**Remark.** Exploiting the anti-symmetry of the Riemann tensor, $R^{\nu}_{\ \ \alpha \beta \xi} = - R^{\nu}_{\ \ \beta \alpha \xi}$, it's possible to recast the expression of the parallel transport of the vector field $\mathbf{v}$ along the elementary closed path $\gamma_{X,Y}$ built with the vector fields $X$, $Y$ as

$$\begin{aligned}
  H^\nu = \Delta v^{nu} 
  & := \oint_{\gamma_{X,Y}}d q^{\mu} \left\{  \partial_{\mu} v^{\nu}  \right\}_{||} =  \\
  & := - \oint_{\gamma_{X,Y}} d q^{\mu} \Gamma_{\mu \xi}^{\nu} v^{\xi} =  \\
  &  = - \frac{1}{2} R^{\nu}_{\ \ \alpha \beta \xi} \left( X^{\alpha} Y^{\beta} - X^{\beta} Y^{\alpha} \right) v^\xi + \text{higher order terms} = \\
  &  = - \frac{1}{2} R^{\nu}_{\ \ \alpha \beta \xi} \, A^{\alpha \beta} \, v^\xi + \text{higher order terms} \ ,
\end{aligned}$$

having introduced the **signed areas** $A^{\alpha \beta}$ of the projection of the area enclosed in the elementary loop onto the plane defined by the coordinates $q^{\alpha}$ and $q^{\beta}$.

**todo**

* discuss the projected areas
* discuss the higher-order correction to the area from Lie-bracket cut at the corner
* check the common standard for the order of the indices of the Riemann tensor


<!--
**Re-grouping into Curvature and Lie Bracket Contributions**

The second-order difference head components simplify to two distinct physical terms:

$$\begin{aligned}
  ( A - B )^{\nu} 
  & = - X^\alpha Y^\beta v^\xi \left( -\partial_\beta \Gamma^\nu_{\alpha\xi} + \partial_\alpha \Gamma^\nu_{\beta\xi} - \Gamma^\nu_{\alpha\eta} \Gamma^\eta_{\beta\xi} + \Gamma^\nu_{\beta\eta} \Gamma^\eta_{\alpha\xi} \right) + \\
  & \quad - \left( X^\alpha \partial_\alpha Y^\mu - Y^\alpha \partial_\alpha X^\mu \right) \Gamma^\nu_{\mu\xi} v^\xi
\end{aligned}$$

1. **Riemann Curvature Tensor** contribution, $- X^\alpha Y^\beta v^\xi R^\nu_{\,\,\xi\alpha\beta} \mathbf{b}_\nu$

2. **Lie Bracket** $[X,Y]^\mu$ contribution, required to close the loop, $- [X, Y]^\mu \Gamma^\nu_{\mu\xi} v^\xi \mathbf{b}_\nu$

-->

<!--
   *(Note in page: "contribution w/o parallel transport along the Lie bracket")*
-->

```{dropdown} ...
:open:

**todo** *Link the following sections to what's done so far.*

##### Riemann Curvature Tensor Definition

For arbitrary vector fields $X, Y, Z$:

$$R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$$

If $X, Y$ are coordinate vector fields ($[X, Y] = 0$), this simplifies to:

$$R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z$$

##### Component Expression

Computing $\nabla_i \nabla_j Z - \nabla_j \nabla_i Z$ for $Z = Z^m \mathbf{b}_m$:

$$R^k_{\,m i j} = \partial_i \Gamma^k_{j m} - \partial_j \Gamma^k_{i m} + \Gamma^l_{j m} \Gamma^k_{i l} - \Gamma^l_{i m} \Gamma^k_{j l}$$

```

(differential-geometry:curvature:intrinsic:relation-with-extrinsic-curvature)=
### Relation between Riemann curvature tensor and extrinsic curvature

If the parametrization of the space is regular enough, second-order mixed derivatives have the same value, i.e. $\tfrac{\partial^2 \mathbf{r}}{\partial q^i \partial q^k} = \tfrac{\partial^2 \mathbf{r}}{\partial q^k \partial q^i}$ that implies $\Gamma_{ik}^{\alpha} = \Gamma_{ki}^{\alpha}$. Similar relation holds for the mixed derivatives of vector $\mathbf{b}_i$ of the natural basis, $\tfrac{\partial^2 \mathbf{b}_i}{\partial q^j \partial q^k} = \tfrac{\partial^2 \mathbf{b}_i}{\partial q^k \partial q^j}$. As

$$\begin{aligned}
  \dfrac{\partial^2 \mathbf{b}_i}{\partial q^j \partial q^k} 
  & = \dfrac{\partial}{\partial q^j} \dfrac{\partial \mathbf{b}_i}{\partial q^k} = \\
  & = \dfrac{\partial}{\partial q^j} \left( \Gamma_{ik}^{\alpha} \mathbf{b}_{\alpha} \right) = \\
  & = \dfrac{\partial}{\partial q^j} \left( \Gamma_{ik}^{l} \mathbf{b}_{l} + \Gamma_{ik}^{n+1} \mathbf{n} \right) = \\
  & = \partial_j \Gamma^{l}_{ik} \mathbf{b}_{l} + \Gamma_{ik}^{l} \left( \Gamma_{l j}^{m} \mathbf{b}_{m} + \Gamma_{l j}^{n+1} \mathbf{n} \right) + \partial_j \Gamma_{ik}^{n+1} \mathbf{n} + \Gamma_{ik}^{n+1} \partial_j \mathbf{n} = \\
  & = \left( \partial_j \Gamma_{ik}^l + \Gamma_{ik}^m \Gamma_{mj}^l - \Gamma_{ik}^{n+1} b^l_j \right) \mathbf{b}_l + \left( \partial_j \Gamma_{ik}^{n+1} + \Gamma_{ik}^{l} \Gamma_{lj}^{n+1} \right) \mathbf{n} \ ,
\end{aligned}$$

having used the **Weingarten equation** {eq}`eq:differential-geometry:curvature:weingarten`, $\partial_j \mathbf{n} = - b^{\ \ l}_j \mathbf{b}_l$. Equating every tangential components of $\partial_{jk} \mathbf{b}_i$ and $\partial_{kj} \mathbf{b}_i$, it follows for the component $l$,

$$
\partial_j \Gamma_{ik}^l + \Gamma_{ik}^m \Gamma_{mj}^l - \Gamma_{ik}^{n+1} b^l_j = 
\partial_k \Gamma_{ij}^l + \Gamma_{ij}^m \Gamma_{mk}^l - \Gamma_{ij}^{n+1} b^l_k \ ,
$$

or, rearranging

$$
\underbrace{\partial_j \Gamma_{ik}^l - \partial_k \Gamma_{ij}^l + \Gamma_{ik}^m \Gamma_{mj}^l - \Gamma_{ij}^m \Gamma_{mk}^l}_{ = R^{l}_{\ \ ijk} } = \Gamma_{ik}^{n+1} b^l_j - \Gamma_{ij}^{n+1} b^l_k \ ,
$$

having introduced the definition of **Riemann curvature tensor** $R^{l}_{\ \ ijk}$. Writing $\Gamma^{n+1}_{ij} = b_{ij}$, it follows

$$R^{l}_{\ \ ijk} = b_{ij} b^l_j - b_{ij} b^l_k \ .$$


See also [General Relativity: Differential Geometry: Curvature Tensor](https://basics2022.github.io/bbooks-physics-modern/ch/relativity-general/differential-geometry.html#curvature-tensor)

(differential-geometry:curvature:intrinsic:examples)=
### Examples

````{prf:example} 2-d Euclidean space is flat, independently from the set of coordinates used for the description

While it's trivial to prove that the 2-dimensional Euclidean space is flat using Cartesian coordinates, in this result is also proved using polar coordinates. This should be an expected result, as an intrinsic/tensor relation holds independently from an arbitrary choice of coordinates or vector basis.

**Cartesian coordinates.** Cartesian coordinates have uniform (constant in space) vectors of the natural basis, and thus all the Christoffel symbols equal to zero - being the components of their space derivatives - and the partial derivatives of the Christoffell symbols equal to zero as well. Thus,

$$R^{k}_{\ m i j} = 0 \ .$$


```{dropdown} Polar coordinates

**Polar Coordinates $(r, \theta)$. Let $q^1 = r$, $q^2 = \theta$. Thus, the natural basis and its reciprocal - using the common unit-length orhogonal polar basis - are

$$
\left\{ \begin{aligned} \mathbf{b}_1 & = \partial_1 \mathbf{r} = \hat{r} \\ \mathbf{b}_2 & = \partial_2 \mathbf{r} = r \hat{\boldsymbol\theta} \end{aligned}\right.
\quad , \quad 
\left\{ \begin{aligned} \mathbf{b}^1 & = \hat{r} \\ \mathbf{b}^2 & = \frac{1}{r} \hat{\boldsymbol\theta} \end{aligned}\right.
\ .$$

**Metric tensor, $g_{ij} = \mathbf{b}_i \cdot \mathbf{b}_j$.**

$$g_{ij} = \begin{pmatrix} 1 & 0 \\ 0 & r^2 \end{pmatrix}, \quad g^{ij} = \begin{pmatrix} 1 & 0 \\ 0 & \frac{1}{r^2} \end{pmatrix}$$

**Non-vanishing Christoffel Symbols.**
Using $\Gamma^l_{ik} = \frac{1}{2} g^{lj} \left( \partial_i g_{jk} + \partial_k g_{ji} - \partial_j g_{ik} \right)$:

1. $\Gamma^1_{22} = \frac{1}{2} g^{11} (-\partial_1 g_{22}) = \frac{1}{2}(1)(-2r) = -r$
2. $\Gamma^2_{12} = \Gamma^2_{21} = \frac{1}{2} g^{22} (\partial_1 g_{22}) = \frac{1}{2}\left(\frac{1}{r^2}\right)(2r) = \frac{1}{r}$

All other $\Gamma^k_{ij} = 0$.

**Non-vanishing derivatives of Christoffel Symbols.**
* $\partial_1 \Gamma^2_{12} = \partial_r \left(\frac{1}{r}\right) = -\frac{1}{r^2}$
* $\partial_1 \Gamma^1_{22} = \partial_r (-r) = -1$

**Calculation of Riemann Tensor Components.**
Riemann tensor of a 2-dimensional manifold has 16 components. Not all the components are independent
Exploiting symmetries of the Riemann tensor,  $R^k_{\,m i j} = \partial_i \Gamma^k_{j m} - \partial_j \Gamma^k_{i m} + \Gamma^l_{j m} \Gamma^k_{i l} - \Gamma^l_{i m} \Gamma^k_{j l}$, it's easy to realized that

$$R^{k}_{\ m i j} = - R^{k}_{\ m j i} \ .$$

Thus, all the components with $i = j$ are identically zero. So, only 4 components can be independent, setting as an example $i = 1$, $j = 2$, and evaluating the 4 terms with $(k,m) \in \{ 1 , 2 \}^2$.

* **Component $R^1_{\,212}$:**

  $$\begin{aligned}
    R^1_{\,212} 
    & = \partial_1 \Gamma^1_{22} - \partial_2 \Gamma^1_{12} + \Gamma^l_{22} \Gamma^1_{1l} - \Gamma^l_{12} \Gamma^1_{2l} = \\
    & = (-1) - 0 + (\Gamma^1_{22} \Gamma^1_{11} + \Gamma^2_{22} \Gamma^1_{12}) - (\Gamma^1_{12} \Gamma^1_{21} + \Gamma^2_{12} \Gamma^1_{22}) = \\
    & = -1 - (0) - \left(\frac{1}{r} \cdot (-r)\right) = -1 - (-1) = 0
  \end{aligned}$$

* **Component $R^2_{\,112}$:**

  $$R^2_{\,112} = \partial_1 \Gamma^2_{21} - \partial_2 \Gamma^2_{11} + \Gamma^l_{21} \Gamma^2_{1l} - \Gamma^l_{11} \Gamma^2_{2l}$$
  $$R^2_{\,112} = \left(-\frac{1}{r^2}\right) - 0 + (\Gamma^2_{21} \Gamma^2_{12}) - 0 = -\frac{1}{r^2} + \left(\frac{1}{r} \cdot \frac{1}{r}\right) = 0$$


* **Component $R^1_{\,112}$:**

  $$\dots$$


* **Component $R^2_{\,212}$:**

  $$\dots$$


```

````

```{dropdown} Derivatives of the components of the metric tensor
:open:

Let $g_{ij} = \mathbf{b}_i \cdot \mathbf{b}_j$, $\mathbf{b}_i \cdot \mathbf{b}^j = \delta_{i}^{j}$ and $\partial_{k} \mathbf{b}_i = \Gamma_{ik}^{l} \mathbf{b}_l$, then

$$\begin{aligned}
  \partial_{k} g_{ij} 
  & = \partial_k \mathbf{b}_i \cdot \mathbf{b}_j + \mathbf{b}_i \cdot \partial_k \mathbf{b}_j 
    = \Gamma_{ik}^{l} g_{lj} + \Gamma_{ik}^{l} g_{il} \ . 
\end{aligned}$$

Thus, swapping indices

$$\begin{aligned}
  \partial_{k} g_{ij} & = \Gamma_{ik}^{l} g_{lj} + \Gamma_{jk}^{l} g_{il} \\
  \partial_{i} g_{jk} & = \Gamma_{ji}^{l} g_{lk} + \Gamma_{ki}^{l} g_{jl} \\
  \partial_{j} g_{ki} & = \Gamma_{kj}^{l} g_{li} + \Gamma_{ij}^{l} g_{kl} \\
\end{aligned}$$

From the latter three relations, it's possible to retrieve the expression of Christoffel coefficients as a function of the components of the metric tensor and their derivatives. As an example, coefficient $\Gamma_{ik}^{l}$ is found summing the first and the second relation, and subtracting the third one,

$$\Gamma_{ik}^l g_{jl} = \frac{1}{2} \left( \partial_{k} g_{ij} + \partial_{i} g_{jk} - \partial_{j} g_{ki} \right) \ ,$$

or

$$\Gamma_{ik}^l = \frac{1}{2} g^{lj} \left( \partial_{k} g_{ij} + \partial_{i} g_{jk} - \partial_{j} g_{ki} \right) \ .$$

```


````{prf:example} Parallel transport of a vector on a sphere

```{dropdown} Details
:open:

Using spherical coordinates $\left(q^1, q^2 \right) = (\theta, \phi)$,[^spherical-extrinsic] the **metric tensor** reads

$$
\left[ g_{ij} \right] = \begin{bmatrix} R^2 \sin^2 q^2 & \cdot \\ \cdot & 1 \end{bmatrix}
\quad , \quad 
\left[ g^{ij} \right] = \begin{bmatrix} \frac{1}{R^2 \sin^2 q^2} & \cdot \\ \cdot & 1 \end{bmatrix}$$

The only non-zero derivative of the components of the metric tensor is 

$$\partial_{2} g_{11} = 2 R^2 \sin q^2 \cos q^2 \ .$$

Non-zero Christoffel symbols are

$$\begin{aligned}
  \Gamma_{ik}^1 
  & = \frac{1}{2} g^{1 j} \left( \partial_k g_{ij} + \partial_{i} g_{jk} - \partial_j g_{ki} \right) = &&   \left( j = 1, \ g^{11} = \frac{1}{R^2 \sin^2 q^2} \right) \\
  & = \frac{1}{2} g^{1 1} \left( \partial_k g_{i1} + \partial_{i} g_{1k} - \partial_1 g_{ki} \right) = && \left( \partial_1 g_{ik} = 0 \right) \\
  & = \frac{1}{2} g^{1 1} \left( \partial_k g_{i1} + \partial_i g_{1k} \right)  \ ,
\end{aligned}$$

then 

$$\Gamma_{12}^{1} = \Gamma_{21}^{1} = \frac{1}{2} \frac{1}{R^2 \sin^2 q^2} 2 R^2 \sin q^2 \cos q^2 \ .$$

[^spherical-extrinsic]: Extrinsic approach. Recalling that $\mathbf{r} = r \hat{\mathbf{r}} = \hat{\mathbf{x}} \left( r \sin \phi \cos \theta \right) + \hat{\mathbf{y}} \left( r \sin \phi \sin \theta \right) + \hat{\mathbf{z}} r \cos \phi$, thus $\mathbf{b}_{1} = \partial_{\theta} \mathbf{r} = -r \sin \phi \sin \theta \, \hat{\mathbf{x}} + r \sin \phi \cos \theta \, \hat{\mathbf{y}}$, and $\mathbf{b}_2 = \partial_{\phi} \mathbf{r} = r \cos \phi \cos \theta \, \hat{\mathbf{x}} + r \cos \phi \sin \theta \, \hat{\mathbf{y}} - r \sin \theta \, \hat{\mathbf{z}}$. The covariant components of the metric tensor are $g_{11} =  r^2 \sin^2 \phi$, $g_{12} = 0$, $g_{22} = r^2$.


```

````

