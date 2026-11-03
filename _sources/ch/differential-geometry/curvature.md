(differential-geometry:curvature)=
# Curvature

This section is devoted to curvature, and its different descriptions:
* [**Extrinsic curvature**](differential-geometry:curvature:extrinsic), i.e. the description of the curvature of a $n$-manifold embedded in a $n+1$-space, as it's usually done in the description of [2-dimensional surfaces in the 3-dimensional Euclidean space](differential-geometry:surfaces).
* [**Intrinsic curvature**](differential-geometry:curvature:intrinsic), i.e. the description of a curvature of a $n$-manifold without the need for an embedding in a higher-dimensional space. This approach exploits the concepts of parallel transport, that - when applied to a vector field on a closed loop, see [Parallel transport around a closed loop and the Riemann tensor](differential-geometry:curvature:intrinsic:riemann-curvature-tensor:riemann-tensor) - provides the definition of Riemann tensor, {prf:ref}`def-differential-geometry-riemann-tensor`. This is the common approach to [Einstein General Relativity](https://basics2022.github.io/bbooks-physics-modern/ch/relativity-general/intro.html): spacetime is a 4-dimensional manifold, and it's not embedded in a 5-dimensional space in the original formulation of GR theory.

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
:label: coordinate-field-commutation

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
  & = - v^\xi R^{\nu}_{\ \ \xi \alpha \beta \xi} X^\alpha Y^\beta \ ,
\end{aligned}$$

having introduced the definition of the **Riemann tensor**, $R^{\nu}_{\ \ \alpha \beta \xi}$.

```{prf:definition} Riemann tensor
:label: def-differential-geometry-riemann-tensor

$$R^{\nu}_{\ \ \xi \alpha \beta} := \partial_{\alpha} \Gamma^{\nu}_{\beta \xi} - \partial_{\beta} \Gamma^{\nu}_{\alpha \xi} + \Gamma_{\alpha \eta}^{\nu} \Gamma_{\beta \xi}^{\eta} - \Gamma_{\beta \eta}^{\nu} \Gamma_{\alpha \xi}^{\eta} \ . $$

```

**Remark.** The contribution of the Lie bracket, required to close the loop, annihilates with other two terms.

**Remark.** Exploiting the anti-symmetry of the Riemann tensor, $R^{\nu}_{\ \ \alpha \beta \xi} = - R^{\nu}_{\ \ \beta \alpha \xi}$, it's possible to recast the expression of the parallel transport of the vector field $\mathbf{v}$ along the elementary closed path $\gamma_{X,Y}$ built with the vector fields $X$, $Y$ as

$$\begin{aligned}
  H^\nu = \Delta v^{nu} 
  & := \oint_{\gamma_{X,Y}}d q^{\mu} \left\{  \partial_{\mu} v^{\nu}  \right\}_{||} =  \\
  & := - \oint_{\gamma_{X,Y}}  v^{\xi} \, \Gamma_{\mu \xi}^{\nu} \, d q^{\mu} =  \\
  &  = - \frac{1}{2} v^{\xi} \, R^{\nu}_{\ \ \xi \alpha \beta} \left( X^{\alpha} Y^{\beta} - X^{\beta} Y^{\alpha} \right) + \text{higher order terms} = \\
  &  = - \frac{1}{2} v^{\xi} \, R^{\nu}_{\ \ \xi \alpha \beta} \, A^{\alpha \beta} + \text{higher order terms} \ ,
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

(differential-geometry:curvature:intrinsic:riemann-curvature-tensor:properties)=
#### Properties

$$R_{ab\mathbf{cd}} = - R_{ab\mathbf{dc}}$$ (eq:riemann-tensor:prop-1)

```{dropdown} Proof

```

$$R_{\mathbf{ab}cd} = - R_{\mathbf{ba}cd}$$ (eq:riemann-tensor:prop-2)

```{dropdown} Proof

```

$$0 = R_{\mathbf{ab} cd} = R_{cd\mathbf{ab}}$$ (eq:riemann-tensor:prop-3)

```{dropdown} Proof

```

$$0 = R_{\mathbf{a} bcd} + R_{\mathbf{a} cdb} + R_{\mathbf{a} dbc}$$ (eq:riemann-tensor:prop-4)

```{dropdown} Proof

```

$$0 = R_{\mathbf{ab} cd;e} + R_{\mathbf{ab} de;c} + R_{\mathbf{ab} ec;d}$$ (eq:riemann-tensor:prop-5)

```{dropdown} Proof

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

having used the **Weingarten equation** {eq}`eq:differential-geometry:curvature:weingarten`, $\partial_j \mathbf{n} = - g^{kl} b_{jk} \mathbf{b}_l = - b^{\ \ l}_j \mathbf{b}_l$. 

```{admonition} Symmetries of $\ \mathbb{b}$

Since $b_{ij} := \Gamma^{n+1}_{ij}$, then these symbols are symmetric $b_{ij} = b_{ji}$. Since $b_{i}^{\ \ l} = b_{ij} g^{jl}$, exploiting the symmetries of the symbols $b_{ij}$ and $g^{kl}$, it follows 

$$b_{i}^{\ \ l} = b_{ij} g^{jl} = b_{ji} g^{jl} = b^{l}_{\ \ i} \ .$$


```

Equating every tangential components of $\partial_{jk} \mathbf{b}_i$ and $\partial_{kj} \mathbf{b}_i$, it follows for the component $l$,

$$
\partial_j \Gamma_{ik}^l + \Gamma_{ik}^m \Gamma_{mj}^l - \Gamma_{ik}^{n+1} b^l_j = 
\partial_k \Gamma_{ij}^l + \Gamma_{ij}^m \Gamma_{mk}^l - \Gamma_{ij}^{n+1} b^l_k \ ,
$$

or, rearranging

$$
\underbrace{\partial_j \Gamma_{ik}^l - \partial_k \Gamma_{ij}^l + \Gamma_{ik}^m \Gamma_{mj}^l - \Gamma_{ij}^m \Gamma_{mk}^l}_{ = R^{l}_{\ \ ijk} } = \Gamma_{ik}^{n+1} b^l_j - \Gamma_{ij}^{n+1} b^l_k \ ,
$$

having introduced the definition of **Riemann curvature tensor** $R^{l}_{\ \ ijk}$. Writing $\Gamma^{n+1}_{ij} = b_{ij}$, as done in {eq}`eq:second-fundamental-form:normal-projection` dealing with curvature and second fundamental form, it follows

$$R^{l}_{\ \ ijk} = b_{ik} b^l_j - b_{ij} b^l_k $$ (eq:riemann:second-fundamental-form)

<!-- = b_{ik} b_{jm} g^{lm} - b_{ij} b_{km} g^{lm} \ .$$ -->


See also [General Relativity: Differential Geometry: Curvature Tensor](https://basics2022.github.io/bbooks-physics-modern/ch/relativity-general/differential-geometry.html#curvature-tensor)

(differential-geometry:curvature:intrinsic:relation-with-extrinsic-curvature:2d-surface)=
#### Riemann tensor for 2-dimensional surfaces

$$R_{mijk} = g_{ml} R^{l}_{\ \ ijk} = g_{ml} \left( b_{ik} b^l_j - b_{ij} b^l_k \right) = b_{ik} b_{jm} - b_{ij} b_{mk} \ . $$

For a 2-dimensional surface, indices belong to the set $\{ 1, 2 \}$. In general, it has 16 components. Exploiting symmetries of the Riemann tensor, it's possible to find a smaller set of independent components. Property {eq}`eq:riemann-tensor:prop-1`, $R_{mijk} = -R_{mikj}$, sets all the elements with $k = j$ to zero, i.e. 8 components are set to zero. Only 4 of the remaining components could be independent. Let's say we choose the - possibly - independent components to be the one with $j = 1$, $k = 2$, i.e. 

$$\left\{ R_{1112}, R_{1212}, R_{2112}, R_{2212} \right\}$$

Property {eq}`eq:riemann-tensor:prop-2`, $R_{mijk} = -R_{imjk}$, sets the elements $R_{mijk}$ with $m = i$ to zero, and thus the number of possibly independent components becomes 2, since $R_{1112} = R_{2212} = 0$. The same property implies that $R_{2112} = - R_{1212}$, so the number of possibly independent components becomes 1, usually chosen as $R_{1212}$.

Thus, non-zero components are

$$R_{1212} = - R_{2112} = - R_{1221} = R_{2121} \ .$$

Using {eq}`eq:riemann:second-fundamental-form`, it can be proved that the component $R_{1212}$ is equal to the determinant of the second fundamental form $\mathbb{b}$, 

$$R_{1212} = b_{22} b_{11} - b_{12}^2 =  L N - M^2 = K g \ .$$

having introduced the **Gaussian curvature**, using its expression as the ratio of the determinant of the second and first fundamental form {eq}`eq:differential-geometry:gaussian-curvature`, $K = \frac{\text{det}\left\{ b_{ij} \right\} }{\text{det}\left\{ g_{ij} \right\} } = \frac{LN - M^2}{g}$.

**Ricci tensor.** The components of Ricci tensor, $R_{ik} := g^{mj} R_{mijk}$, are

$$\begin{aligned}
  R_{11} & = g^{mj} R_{m1j1} = g^{22} R_{2121} = \ \ g^{22} K g = g_{11} K  \\
  R_{12} & = g^{mj} R_{m1j2} = g^{21} R_{2112} = -   g^{21} K g = g_{12} K  \\
  R_{21} & = g^{mj} R_{m2j1} = g^{12} R_{1221} = -   g^{12} K g = g_{21} K  \\
  R_{22} & = g^{mj} R_{m2j2} = g^{11} R_{1212} = \ \ g^{11} K g = g_{22} K  \ ,\
\end{aligned}$$

i.e. Ricci tensor of a 2-dimensional surface is proportional to the metric tensor, and the proportionality constant is the Gaussian curvature,

$$R_{ij} = K g_{ij} \ .$$

**Scalar curvature.** The scalar curvature, $R := g^{ij} R_{ij}$, is simply $R = 2 K$.

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
:label: parallel-transport-sphere

```{dropdown} Coordinates and metric tensor
:open:

Using spherical coordinates $\left(q^1, q^2 \right) = (\theta, \phi)$,[^spherical-extrinsic] the **metric tensor** reads

$$
\left[ g_{ij} \right] = \begin{bmatrix} R^2 \sin^2 q^2 & \cdot \\ \cdot & R^2 \end{bmatrix}
\quad , \quad 
\left[ g^{ij} \right] = \begin{bmatrix} \frac{1}{R^2 \sin^2 q^2} & \cdot \\ \cdot & \frac{1}{R^2} \end{bmatrix} \ ,$$

with constant $R$, i.e. the radius of the sphere.

[^spherical-extrinsic]: Extrinsic approach. Recalling that $\mathbf{r} = r \hat{\mathbf{r}} = \hat{\mathbf{x}} \left( r \sin \phi \cos \theta \right) + \hat{\mathbf{y}} \left( r \sin \phi \sin \theta \right) + \hat{\mathbf{z}} r \cos \phi$, thus $\mathbf{b}_{1} = \partial_{\theta} \mathbf{r} = -r \sin \phi \sin \theta \, \hat{\mathbf{x}} + r \sin \phi \cos \theta \, \hat{\mathbf{y}}$, and $\mathbf{b}_2 = \partial_{\phi} \mathbf{r} = r \cos \phi \cos \theta \, \hat{\mathbf{x}} + r \cos \phi \sin \theta \, \hat{\mathbf{y}} - r \sin \theta \, \hat{\mathbf{z}}$. The covariant components of the metric tensor are $g_{11} =  r^2 \sin^2 \phi$, $g_{12} = 0$, $g_{22} = r^2$.

```

```{dropdown} Christoffel symbols
:open:

The only non-zero derivative of the components of the metric tensor is 

$$\partial_{2} g_{11} = 2 R^2 \sin q^2 \cos q^2 \ .$$

Non-zero Christoffel symbols are

* with upper index = 1:

   $$\begin{aligned}
     \Gamma_{ik}^1 
     & = \frac{1}{2} g^{1 j} \left( \partial_k g_{ij} + \partial_{i} g_{jk} - \partial_j g_{ki} \right) = &&   \left( j = 1, \ g^{11} = \frac{1}{R^2 \sin^2 q^2} \right) \\
     & = \frac{1}{2} g^{1 1} \left( \partial_k g_{i1} + \partial_{i} g_{1k} - \partial_1 g_{ki} \right) = && \left( \partial_1 g_{ik} = 0 \right) \\
     & = \frac{1}{2} g^{1 1} \left( \partial_k g_{i1} + \partial_i g_{1k} \right)  \ ,
   \end{aligned}$$
   
   then 
   
   $$\Gamma_{12}^{1} = \Gamma_{21}^{1} = \frac{1}{2} \frac{1}{R^2 \sin^2 q^2} 2 R^2 \sin q^2 \cos q^2 = \frac{\cos q^2}{\sin q^2} \ .$$

* with upper index = 2:

   $$\begin{aligned}
     \Gamma_{ik}^2 
     & = \frac{1}{2} g^{2 j} \left( \partial_k g_{ij} + \partial_{i} g_{jk} - \partial_j g_{ki} \right) = &&   \left( j = 2, \ g^{22} = \frac{1}{R^2} \right) \\
     & = \frac{1}{2} g^{22} \left( \partial_k g_{i2} + \partial_{i} g_{2k} - \partial_2 g_{ki} \right) = && \left( \partial g_{2 \cdot} = 0 , \ \partial_{2} g_{11} = 2 R^2 \sin q^2 \cos q^2 \right) \\
     & = - \frac{1}{2} g^{22} \partial_{2} g_{ik} \ ,
   \end{aligned}$$
   
   then 
   
   $$\Gamma_{11}^{2} = - \sin q^2 \cos q^2 \ .$$

Non-zero derivatives of the Christoffel symbols

$$\partial_2 \Gamma_{12}^1 = \partial_2 \Gamma_{21}^1 = - \frac{1}{\sin^2 q^2} \ ,$$
$$\partial_2 \Gamma_{11}^2 = \sin^2 q^2 - \cos^2 q^2 \ .$$

```

```{dropdown} Parallel transport along a meridian, $\ \theta = \text{const.}$, i.e. $\ q^1 = \text{const.}$
:open:

A meridian can be parametrized with $q^2 = \phi$ as a parameter, as the coordinate $q^1 = \theta$ is constant, and thus $dq^1 = 0$. The parallel transport of the vector field thus becomes a system of 2 equations in 2 unknowns $v^1(q^2)$, $v^2(q^2)$, namely

$$\left\{\begin{aligned}
 d_2 v^1 & = - \Gamma_{12}^1 v^1 - \Gamma_{22}^1 v^2 = - \text{cot}\left( q^2 \right) v^1( q^2 ) \\
 d_2 v^2 & = - \Gamma_{12}^2 v^1 - \Gamma_{22}^2 v^2 = 0 \\
\end{aligned}\right.$$

Thus the solution reads

$$\left\{ \begin{aligned}
  v^1( \phi ) & = v^1_0 \frac{\sin \phi_0}{\sin \phi} \\
  v^2( \phi ) & = v^2_0 \\
\end{aligned} \right.$$

**Details.** Thus $v_2\left( q^2 \right) = \overline{v^2}$, and $v^1$ can be evaluated with **separation of variables**,

$$\begin{aligned}
  \int_{v_1}^{v_2} \frac{d v}{v} & = - \int_{x_1}^{x_2} \text{cot}(x) \, dx \\
  \left.\ln \left( v \right)\right|_{v_1}^{v_2} & = - \left.\ln \left( \sin \phi \right)\right|_{\phi_1}^{\phi_2} \\
  \frac{v_2}{v_1} & = \frac{ \sin \phi_1 }{ \sin \phi_2 } \\
  v_2 \sin \phi_2 & = v_1 \sin \phi_1 \ .
\end{aligned}$$

being 

$$\int \text{cot}(x) dx = \int \frac{\cos x}{\sin x} dx = \int \frac{d \sin x}{\sin x} = \ln \left( \sin x \right) \ .$$

**Remark.** The first equation of the system can be written as $v'(x) = - \frac{\cos(x)}{\sin(x)} v(x)$, or

$$0 = v'(x) \sin(x) + v(x) \cos(x) = \tfrac{d}{dx} \left( v(x) \sin(x) \right)\ .$$

<!--
A meridian can be parametrized with $q^2 = \phi$ as a parameter, as the coordinate $q^1 = \theta$ is constant, and thus $dq^1 = 0$. The integral of the parallel transport of the vector $\mathbf{v}$ on a meridian is

$$\begin{aligned}
  \Delta v^\nu = \int_{q^2 = \phi_1}^{\phi_2} d q^2 \left\{ \partial_2 v^\nu \right\}_{||} 
  & = - \int_{q^2 = \phi_1}^{\phi_2} \Gamma_{\xi 2}^{\nu} v^{\xi} d q^2 \ ,
\end{aligned}$$

having used {eq}`eq:differential-geometry:curvature:parallel-transport:component-increment` to write $\left\{ \partial_\mu v^\nu \right\}_{||} = - \Gamma_{\xi \mu}^{\nu} v^{\xi} $.

Thus the two components of the parallel transport are

$$\begin{aligned}
  \Delta v^1 
  & = - \int_{q^2 = \phi_1}^{\phi_2} \Gamma_{\xi 2}^{1} v^{\xi} d q^2 = \\
  & = - \int_{q^2 = \phi_1}^{\phi_2} \Gamma_{1 2}^{1} v^{1} d q^2 \\
  \Delta v^2 & = - \int_{q^2 = \phi_1}^{\phi_2} \Gamma_{\xi 2}^{2} v^{\xi} d q^2 = 0 \\
\end{aligned}$$
-->


```

```{dropdown} Parallel transport along a parallel, $\ \phi = \text{const.}$, i.e. $\ q^2 = \text{const.}$
:open:

A parallel can be parametrized with $q^1 = \theta$ as a parameter, as the coordinate $q^2 = \overline{\phi}$ is constant, and thus $dq^2 = 0$. The parallel transport of the vector field thus becomes a system of 2 equations in 2 unknowns $v^1(q^1)$, $v^2(q^1)$, namely

$$\left\{\begin{aligned}
 d_1 v^1 (q^1) & = - \Gamma_{11}^1 v^1 - \Gamma_{21}^1 v^2 = - \text{cot}\left( q^2 \right) v^2 (q^1) \\
 d_1 v^2 (q^1) & = - \Gamma_{11}^2 v^1 - \Gamma_{21}^2 v^2 =   \sin\left( q^2 \right) \cos\left( q^2 \right) \, v^1  (q^1) \\
\end{aligned}\right.$$

As $q^2 = \overline{\phi}$ is constant, 

$$\left\{ \begin{aligned}
  v^1( \theta ) & = v_1 \frac{\sin \phi_1}{\sin \phi} \\
  v^2( \theta ) & = 0 \\
\end{aligned} \right.$$

**Details.**

$$\left\{ \begin{aligned}
  \frac{d v^{1}}{d \theta} (\theta) & = - \frac{\cos(\phi)}{\sin(\phi)} \, v^2(\theta) \\
  \frac{d v^{2}}{d \theta} (\theta) & =   \sin(\phi) \cos(\phi) \, v^1(\theta) \\
\end{aligned} \right.$$

Taking the derivative $\frac{d}{d\theta}$ of the first equation, and replacing $\frac{d v^2}{d \theta}$ with the second equation, 

$$\begin{aligned}
 0
 & = \left( v^1 \right)'' + \frac{\cos(\phi)}{\sin(\phi)} \sin(\phi) \cos(\phi) \, v^1(\theta) = \\
 & = \left( v^1 \right)''(\theta) + \cos^2(\phi) \, v^1(\theta) \ ,
\end{aligned}$$

and thus 

* if $\cos(\phi) \ne 0$

   $$\left\{ \begin{aligned}
     v^1(\theta) & = A \cos\left( \cos(\phi) \theta\right) + B \sin\left( \cos(\phi) \theta\right) \\
     v^2(\theta) & = - \frac{\sin(\phi)}{\cos(\phi)} \left[ - A \cos(\phi) \sin\left( \cos(\phi) \theta\right) + B \cos(\phi) \cos\left( \cos(\phi) \theta\right) \right] \\
                 & = A \sin(\phi) \sin\left( \cos(\phi) \theta\right) - B \sin(\phi) \cos\left( \cos(\phi) \theta\right) \\
   \end{aligned} \right.$$

   Choosing the reference of $\theta$, to be $\theta = 0$ at the beginning of the path, then the initial conditions simplify to

   $$\left\{ \begin{aligned}
     v^1_0 & = A \\
     v^2_0 & = - \sin(\phi) B \ ,
   \end{aligned} \right.
   \quad \rightarrow \quad
   \left\{ \begin{aligned} A & = v^1_0 \\ B & = - \frac{v^2_0}{\sin \phi} \end{aligned} \right.$$

* if $\cos(\phi) = 0$, then $v^1(\theta) = v^1_0$, $v^2(\theta) = v^2_0$ constant. 

```

```{dropdown} Parallel transport from the equator to the pole and back
:open:

Let a vector $\mathbf{v}$ on the equator and parallel to the local meridian, i.e. $\mathbf{v} = v^\phi \mathbf{b}_2$ in $(\theta, \phi) = \left( 0, \frac{\pi}{2} \right)$.

**1. Parallel transport along the equator, $\phi = \frac{\pi}{2}$, $\theta$ from $0$ to $\overline{\theta}$.** The equator is described by the coordinate $\phi = \frac{\pi}{2}$, and thus $\cos \phi = 0$. The solution of the parallel transport equation on the equator gives constant $v^1(\theta)$ and $v^2(\theta)$. Thus,

   $$v^1\left(\overline{\theta}\right) = 0 \quad , \quad v^2\left(\overline{\theta}\right) = v^\phi \ .$$

**2. Parallel transport along the meridian, $\theta = \overline{\theta}$, $\phi$ from $\frac{\pi}{2}$ to $\delta \phi$.**
   
   $$v^1\left( 0 \right) = 0 \quad , \quad v^2\left(\overline{\theta}\right) = v^\phi \ .$$

**3.** *Parallel transport along a small circle around the pole to avoid singularity.*

   $$\left\{ \begin{aligned}
     v^1(\theta)
     & = v^1_0 \cos\left( \cos(\phi) \theta\right) - \frac{v^2_0}{\sin \phi} \sin\left( \cos(\phi) \theta\right) = \\
     & = - \frac{v^\phi}{\sin \delta \phi} \sin\left( \cos(\delta \phi) \theta\right) \\
     v^2(\theta)
     & = v^1_0 \sin(\phi) \sin\left( \cos(\phi) \theta\right) + v^2_0 \cos\left( \cos(\phi) \theta\right) = \\
     & = v^\phi \cos\left( \cos(\delta \phi) \theta\right) 
   \end{aligned} \right.$$

   *The final values are* $v^1 = \frac{v^\phi}{\sin \delta \phi} \sin( \cos(\delta \phi) \theta )$, $v^2 = v^\phi \cos( \cos(\delta \phi) \theta )$. *Exchanging the reference value for $\theta$ should be enough.* **todo** *check!*

**4. Parallel transport along the meridian, $\theta = 0$, $\phi$ from $\delta \phi$ to $\frac{\pi}{2}$.**
   
   $$\begin{aligned}
     v^1\left( 0 \right) 
     & = \frac{\sin(\delta \phi)}{\sin( \pi / 2)} \frac{v^\phi}{\sin \delta \phi} \sin( \cos(\delta \phi) \theta ) = \\
     & = v^\phi \sin( \cos(\delta \phi) \theta ) \\
     & \rightarrow v^\phi \sin( \theta ) \quad \text{for $\delta \phi \rightarrow 0$} \\
     v^2\left( 0 \right)
     & = v^\phi \cos( \cos(\delta \phi) \theta ) \\
     & \rightarrow v^{\phi} \cos( \theta ) \quad \text{for $\delta \phi \rightarrow 0$} \ .
   \end{aligned}$$

**Result.** The final vector after the parallel transport over the closed path is the initial vector rotated by the angle $\theta$.

<!--

$$\left\{ \begin{aligned}
  v^1( \phi ) & = v^1_0 \frac{\sin \phi_0}{\sin \phi} \\
  v^2( \phi ) & = v^2_0 \\
\end{aligned} \right.$$

-->

````

````{prf:example} Riemann tensor on the 2-dimensional sphere
:label: riemann-tensor-sphere

With $\left( q^1, q^2 \right) = \left( \theta, \phi \right)$,

$$
\Gamma_{12}^{1} = \Gamma_{21}^{1} = \frac{\cos \phi}{\sin \phi} \quad , \quad
\Gamma_{11}^{2} = - \sin \phi \cos \phi
$$

$$
\partial_2 \Gamma_{12}^{1} = \partial_2 \Gamma_{21}^{1} = - \frac{1}{\sin^2 \phi} \quad , \quad
\partial_2 \Gamma_{11}^{2} = \sin^2 \phi - \cos^2 \phi
$$

Riemann tensor,

$$R^{\nu}_{\ \ \alpha \beta \xi} := \partial_{\alpha} \Gamma^{\nu}_{\beta \xi} - \partial_{\beta} \Gamma^{\nu}_{\alpha \xi} + \Gamma_{\alpha \eta}^{\nu} \Gamma_{\beta \xi}^{\eta} - \Gamma_{\beta \eta}^{\nu} \Gamma_{\alpha \xi}^{\eta} \ . $$

with the symmetry $R^{\nu}_{\ \ \alpha \beta \xi} = - R^{\nu}_{\ \ \beta \alpha \xi}$, for a 2-dimensional manifold there's need to evaluate only 4 components (are all these 4 components independent?)

$$\begin{aligned}
  R^{\mathbf{1}}_{\ \ 12 \mathbf{1}} & = 0 \\
  R^{\mathbf{1}}_{\ \ 12 \mathbf{2}} & = -\partial_2 \Gamma_{12}^{1} + \Gamma^{1}_{21} \Gamma^{1}_{12} = \frac{1}{\sin^2 \phi} - \frac{\cos^2 \phi}{\sin^2 \phi} = \frac{1}{\sin^2 \phi} \\
  R^{\mathbf{2}}_{\ \ 12 \mathbf{1}} & = - \partial_{2} \Gamma_{11}^{2} + \Gamma^2_{11} \Gamma_{21}^{1} = - \sin^2 \phi + \cos^2 \phi - \cos^2\phi = - \sin^2 \phi \\
  R^{\mathbf{2}}_{\ \ 12 \mathbf{2}} & = 0 \\
\end{aligned}$$

Lowering the first index of the non-zero components - **todo** *Fix the order of the indices to match common definition*

$$\begin{aligned}
  R_{1122} & = g_{11} R^{1}_{\ \ 122} = \frac{R^2 \sin^2 \phi}{\sin^2 \phi} = R^2 \\
  R_{2122} & = g_{22} R^{2}_{\ \ 121} = - R^2 \sin^2 \phi \ .
\end{aligned}$$





````


