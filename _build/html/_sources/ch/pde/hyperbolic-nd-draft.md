(pde:hyperbolic:nd:draft)=
# General hyperbolic problem

(pde:hyperbolic:nd:draft:integral)=
## Integral equations

For a volume $V$ at rest

$$
  \dfrac{d}{dt} \int_{V} \mathbf{u} + \oint_{\partial V} \hat{n} \cdot \mathbf{F} = \int_{V} \mathbf{s}
$$

```{dropdown} Integral equations for a control volume $\ V \ $ at rest

Integral equation for a control volume at rest $V$

$$\begin{aligned}
  & \dfrac{d}{dt} \int_{V} \mathbf{u} + \oint_{\partial V} \mathbf{u} \vec{u} \cdot \hat{n} = \int_{\partial V} \hat{n} \cdot \mathbf{f} + \int_{V} \mathbf{s} \\
  & \dfrac{d}{dt} \int_{V} \mathbf{u} + \oint_{\partial V} \hat{n} \cdot \mathbf{F} = \int_{V} \mathbf{s} \\
\end{aligned}$$

being $\mathbf{u}$ the vector of the conservative variables, $\mathbf{u} \in \mathbb{R}^n$, and $\vec{u}$ the velocity field in the $d$-dimensional domain, and $\mathbf{F} := - \mathbf{f} + \vec{u} \mathbf{u}$.

```

```{dropdown} Integral equations for an arbitary domain $\ v_t \ $

Integral equation for an arbitrary domain $v_t$, with [Reynolds' transport theorem](tensor:calculus:time-derivative-of-integrals:volume-density)

$$\begin{aligned}
  & \dfrac{d}{dt} \int_{v_t} \mathbf{u} + \oint_{\partial v_t} \mathbf{u} ( \vec{u} - \vec{v}_b ) \cdot \hat{n} = \int_{\partial v_t} \hat{n} \cdot \mathbf{f} + \int_{v_t} \mathbf{s} \\ 
  & \dfrac{d}{dt} \int_{v_t} \mathbf{u} - \oint_{\partial v_t} \mathbf{u} \vec{v}_b \cdot \hat{n} + \int_{\partial v_t} \hat{n} \cdot \mathbf{F} = \int_{v_t} \mathbf{s} \\ 
\end{aligned}$$

```

(pde:hyperbolic:nd:draft:integral:jump)=
### Jump conditions

$$
\hat{n} \cdot \vec{v}_b \, \left[ \, \mathbf{u} \, \right] = \hat{n} \cdot \left[ \, \mathbf{F} \, \right] 
$$(eq:pde:hyperbolic:jump)

```{dropdown} From integral equations on $\ v_t \ $ to jump relations

Collapsing $ v_t$ on a surface only the boundary terms on the two sides of the surface persist and the balance equations becomes

$$\begin{aligned}
  \mathbf{0} 
  & = \oint_{\partial v_t} \left( - \hat{n} \cdot \vec{v}_b \mathbf{u} + \hat{n} \cdot \mathbf{F} \right) = \\
  & = \int_{S_{-}} \left( - \hat{n}_{-} \cdot \vec{v}_b \mathbf{u}_{-} + \hat{n}_{-} \cdot \mathbf{F}_{-} \right)  
    + \int_{S_{+}} \left( - \hat{n}_{+} \cdot \vec{v}_b \mathbf{u}_{+} + \hat{n}_{+} \cdot \mathbf{F}_{+} \right) = \\
  & = \int_{S} \left( - \hat{n}_{-} \cdot \vec{v}_b ( \mathbf{u}_{-} - \mathbf{u}_{+} ) + \hat{n}_{-} \cdot ( \mathbf{F}_{-} - \mathbf{F}_{+} ) \right)  
\end{aligned}$$

being $\hat{n}_{-} = - \hat{n}_{+}$. From the arbitrariness of the surface $S$, jump relations follow

$$\hat{n} \cdot \vec{v}_b \, \left[ \, \mathbf{u} \, \right] = \left[ \, \mathbf{F} \, \right] \ ,$$

being $[ \ \cdot \ ] =  (\cdot)_{+} - (\cdot)_{-}$ the jump across the surface.

```

(pde:hyperbolic:nd:draft:differential)=
## Differential equations

In regions where the fields are smooth, differential equations follow from integral equations using [theorems of differential calculus](tensor:calculus:integrals:theorems). 


(pde:hyperbolic:nd:draft:differential:conservative)=
## Conservative form

Conservative form of the differential equations reads

$$
  \partial_t \mathbf{u} + \nabla \cdot \mathbf{F}(\mathbf{u}) = \mathbf{s} \ .
$$(eq:pde:hyperbolic:differential:conservative)

```{dropdown} From integral equations on $\ V \ $ to conservative form of differential equations

For a volume $V$ at rest

$$\begin{aligned}
  \dfrac{d}{dt} \int_{V} \mathbf{u} + \oint_{\partial V} \hat{n} \cdot \mathbf{F} & = \int_{V} \mathbf{s} \\
  \int_{V} \partial_t    \mathbf{u} + \oint_{\partial V} \hat{n} \cdot \mathbf{F} & = \int_{V} \mathbf{s}
\end{aligned}$$

or using components

$$\begin{aligned}
  \int_{V} \partial_t u_i + \oint_{\partial V} n_k F_{ki} & = \int_{V} s_i \ ,
\end{aligned}$$

and using [divergence theorem] under the assumption of sufficient regularity of the flux 

$$\begin{aligned}
  0
  & = \int_{V} \partial_t u_i + \oint_{\partial V} n_k F_{ki} - \int_{V} s_i = \\
  & = \int_{V} \partial_t u_i + \int_{V} \partial_k F_{ki} - \int_{V} s_i = \\
  & = \int_{V} \left\{ \partial_t u_i + \partial_k F_{ki} - s_i \right\} \ ,
\end{aligned}$$

and from the aribitrariness of the domain $V$,

$$\partial_t u_i + \partial_k F_{ki} = s_i \ ,$$

or using abstract vector notation

$$\partial_t \mathbf{u} + \nabla \cdot \mathbf{F} = \mathbf{s} \ .$$


```

$$\partial_t \mathbf{u} + \sum_{k=1}^{d} \mathbf{A}^{(k)}(\mathbf{u}) \, \partial_k \mathbf{u} = \mathbf{s} \ ,$$

with the convection matrices

$$\left\{ \mathbf{A}^{(k)} \right\}_{i \ell} = \partial_{u_{\ell}} F_{ki} \ .$$

```{dropdown} From conservative form to convective form of differential equations

Starting from the component expression {eq}`` of the convective differential equations

$$\begin{aligned}
  s_i
  & = \partial_t u_i + \partial_k F_{ki}(u_\ell) = \\
  & = \partial_t u_i + \partial_{u_{\ell}} F_{ki}(u_\ell) \partial_k u_\ell = \\
  & = \partial_t u_i + A_{i \ell}^{(k)}(u_\ell) \partial_k u_\ell = \\
  & = \partial_t u_i + \sum_{k=1}^éd} A_{i \ell}^{(k)}(u_\ell) \partial_k u_\ell \ ,
\end{aligned}$$

having defined $A_{i \ell}^{(k)} = \partial_{u_{\ell}} F_{ki}$, or using vector notation

$$\partial_t \mathbf{u} + \sum_{k=1}^{d} \mathbf{A}^{(k)}(\mathbf{u}) \partial_k \mathbf{u} = \mathbf{s} \ .$$

```

(pde:hyperbolic:nd:draft:characteristics)=
## Method of characteristics

(pde:hyperbolic:nd:draft:characteristics:spectrum)=
### Spectral decomposition

````{dropdown} Summary of method of characteristics in multi-dimensional domains.

Let 

$$\begin{aligned}
  \mathbf{u}(t,    \vec{r}): & \ \mathbb{R} \times \mathbb{R}^d \rightarrow \mathbb{R}^n \\
  \mathbf{F}(   \mathbf{u}): & \ \mathbb{R}^{n} \rightarrow \mathbb{R}^{d} \times \mathbb{R}^n \\
  \mathbf{s}(t,    \vec{r}): & \ \mathbb{R} \times \mathbb{R}^d \rightarrow \mathbb{R}^n \\
\end{aligned}$$

the conservative form of a hyperbolic problem reads

$$\begin{aligned}
  \partial_t \mathbf{u} + \nabla \cdot \mathbf{F}(\mathbf{u}) & = \mathbf{s} \\
  \partial_t u_i + \partial_j F_{ji} & = s_i \ .
\end{aligned}$$

Expanding the divergence of the flux, the convective (quasi-linear? It makes little to no sense to me...) form follows

$$\begin{aligned}
  s_i 
  & = \partial_t u_i + \sum_{j=1}^{d} \partial_j F_{ji} = \\
  & = \partial_t u_i + \sum_{j=1}^{d} \sum_{k=1}^{n} \partial_j u_k \partial_{u_k} F_{ji} = \\
  & = \partial_t u_i + \sum_{j=1}^{d} \sum_{k=1}^{n} A^{j}_{ik}(\mathbf{u}) \, \partial_j u_k  \ ,
\end{aligned}$$

for every component $i = 1:n$, or

$$\mathbf{s} = \partial_t \mathbf{u} + \sum_{j=1}^{d} \mathbf{A}^j \partial_j \mathbf{u} \ .$$

This problem can be made a little more general with by defining $\mathbf{x} = (t, \mathbf{r}) = ( x_0, \vec{r} )$, as

$$\sum_{j=0}^{d} \mathbf{A}^j \, \partial_j \mathbf{u} = \mathbf{s} \ .$$

The former expression of the hyperbolic problem immediately follows if $\mathbf{A}_0 = \mathbf{I}_n$, $A^0_{ik} = \delta_{ik}$, and 

$$\widetilde{\nabla} \cdot \widetilde{\mathbf{F}} = \partial_0 \mathbf{F}_0 + \sum_{j=1}^{d} \partial_j \mathbf{F}_j = \widetilde{\nabla} \cdot \begin{bmatrix} \ \mathbf{u} \ | \ \mathbf{F} \ \end{bmatrix} \ .$$

as, for $i = 1:n$,

$$\delta_{ik} = \partial_{u_k} F_{0i} \quad \rightarrow \quad F_{0i} = u_k \delta_{ik} = u_i \ .$$


**Taylor expansion of a solution.** Starting from the solution on a manifold determined by the equation $S: f(\mathbf{x}) = 0$, $\mathbf{x}_0 \in S$, if the solution is differentiable, the solution in a point $\mathbf{x} = \mathbf{x}_0 + \Delta \mathbf{x}$ reads

$$\begin{aligned}
  \mathbf{u}(\mathbf{x}) & \sim \mathbf{u}(\mathbf{x}_0) + \Delta \mathbf{x} \cdot \nabla \mathbf{u}(\mathbf{x}_0) \\
  u_i(\mathbf{x}) & \sim u_i(\mathbf{x}_0) + \Delta x_j \frac{\partial u_i}{\partial x_j}(\mathbf{x}_0) \ .
\end{aligned}$$

Now, with a change of coordinates from $\mathbf{x}$ to $\boldsymbol\xi = (n, \mathbf{t})$, i.e. to local normal and tangential directions,

$$\begin{aligned}
  \nabla \mathbf{u} 
  = \hat{\mathbf{x}}_i \frac{\partial}{\partial x_i} \mathbf{u} 
  = \hat{\mathbf{x}}_i \frac{\partial \mathbf{u}}{\partial x_i} 
  = \hat{\mathbf{x}}_i \frac{\partial \mathbf{u}}{\partial \xi_k} \frac{\partial \xi_k}{\partial x_i} 
  = \hat{\boldsymbol\xi}_k \frac{\partial \mathbf{u}}{\partial \xi_k}
\end{aligned}$$

Inserting in the hyperbolic equation

$$\begin{aligned}
  s_i
  & = \sum_{j=0}^{d} A^{j}_{ik} \frac{\partial u_k}{\partial x_j} = \\
  & = \sum_{j=0}^{d} A^{j}_{ik} \sum_{\ell=0}^{d} \frac{\partial u_k}{\partial \xi_\ell} \frac{\partial \xi_\ell}{\partial x_j} = \\ 
  & = \sum_{\ell=0}^{d}  \sum_{j=0}^{d}  A^{j}_{ik} \frac{\partial \xi_\ell}{\partial x_j} \frac{\partial u_k}{\partial \xi_\ell} = \\ 
  & = \sum_{\ell=0}^{d}  \sum_{j=0}^{d}  A^{j}_{ik} \xi^\ell_j \frac{\partial u_k}{\partial \xi_\ell} \ ,
\end{aligned}$$

and separating the normal $\ell = 0$ from the tangential $\ell=1:d$ coordinates,

$$\begin{aligned}
  s_i
  & = \sum_{j=0}^{d} A^j_{ik} \xi^0_j \frac{\partial u_k}{\partial \xi_0} + \sum_{\ell=1}^{d} \sum_{j=0}^{d} A^j_{ik} \xi^t_j \frac{\partial u_k}{\partial \xi_t} = \\
  & = \sum_{j=0}^{d} A^j_{ik} n_j \frac{\partial u_k}{\partial n} + \sum_{\ell=1}^{d} \sum_{j=0}^{d} A^j_{ik} t^\ell_j \frac{\partial u_k}{\partial t_\ell} = \\
  & = \sum_{j=0}^{d} n_j \mathbf{A}^j \partial_n \mathbf{u} + \sum_{\ell=1}^{d} \sum_{j=0}^{d} t^\ell_j \mathbf{A}^j \partial_{t_\ell} \mathbf{u} \ .
\end{aligned}$$

On a smooth surface where the solution is known, all the tangential derivatives of the solution are known as well. In order to evaluate the normal derivative $\partial_n \mathbf{u}$ from the PDE, the (formal) inversion of the matrix

$$\mathbf{A}_{\hat{\mathbf{n}}} := \sum_{j=0}^{d} n_j \, \mathbf{A}^j \ ,$$

must be feasible, and thus $\mathbf{A}_{\hat{\mathbf{n}}}$ must be invertible, to formally get

$$\partial_n \mathbf{u} = \mathbf{A}_{\hat{\mathbf{n}}}^{-1} \left( \mathbf{s} - \sum_{\ell=1}^{d} \mathbf{A}_{\hat{\mathbf{t}}_\ell} \partial_{t_\ell} \mathbf{u} \right) \ .$$

This expression of the normal derivative of the solution - whenever it exists - can be used to find the approximation of the solution in normal direction w.r.t. the surface $S$, i.e. with $\Delta \mathbf{x} = \Delta \ell \hat{\mathbf{n}}$ as

$$\begin{aligned}
  \mathbf{u}(\mathbf{x}) 
  & \sim \mathbf{u}(\mathbf{x}_0) + \Delta \ell \, \hat{\mathbf{n}} \cdot \nabla \mathbf{u}(\mathbf{x}_0) = \\
  & = \mathbf{u}(\mathbf{x}_0) + \Delta \ell \, \partial_{n} \mathbf{u}(\mathbf{x}_0) \ .
\end{aligned}$$

**If** the matrix $\mathbf{A}_{\hat{\mathbf{n}}}$ is diagonalizable, it's invertible if it has no zero eigenvalue. Let $\hat{\mathbf{n}}_i$ be a unit vector so that the matrix $\mathbf{A}_{\hat{\mathbf{n}}}$ has an eigenvalue equal to zero $s_0 = 0$, with right and left eigenvectors $\mathbf{r}_0$, $\mathbf{l}_0$. Recalling the expression of the PDE in normal and tangential components

$$\mathbf{s} = \mathbf{A}_{\hat{\mathbf{n}}} \partial_n \mathbf{u} + \sum_{\ell=1}^{d} \mathbf{A}_{\hat{\mathbf{d}}_\ell} \partial_{t_\ell} \mathbf{u} \ ,$$

left-multiplying by $\mathbf{l}$ gives

$$\begin{aligned}
  \mathbf{l}^T_0 \mathbf{s} 
  & = \mathbf{l}_0^T \left( \mathbf{A}_{\hat{\mathbf{n}}} \partial_{\hat{n}} \mathbf{u} + \sum_{\ell=1}^{d} \mathbf{A}_{\hat{\mathbf{d}}_\ell} \partial_{t_\ell} \mathbf{u} \right) = \\
  & = \mathbf{l}_0^T \sum_{\ell=1}^{d} \mathbf{A}_{\hat{\mathbf{d}}_\ell} \partial_{t_\ell} \mathbf{u} = \\
  & = \mathbf{l}_0^T \sum_{k=0}^{d} \mathbf{A}^k \partial_k \mathbf{u} \ ,
\end{aligned}$$

i.e. the **compatibility condition** on the surface with unit normal $\hat{\mathbf{n}}$ that makes $s_0 = 0$,

$$\mathbf{l}_0^T \mathbf{s} = \mathbf{l}_0^T \sum_{k=0}^{d} \mathbf{A}^k \partial_k \mathbf{u} = \mathbf{l}_0^T \widetilde{\nabla} \cdot \widetilde{\mathbf{F}} \ .$$

Surfaces with unit normal vectors $\hat{\mathbf{n}}$ making eigenvalues of the matrix $\mathbf{A}_{\mathbf{n}}$ equal to zero are defined as **characteristic surfaces**. On each characteristic surface, the corresponding compatibility condition holds.

````

(pde:hyperbolic:nd:draft:characteristics:spectrum:change-vars)=
### Change of variables

Let $\mathbf{u}$ the set of conservative variables[^spectral-cons-phys] and let $\mathbf{v}$ another set of variables. Let the transfomration of variables $\mathbf{v}(\mathbf{u})$ be invertible and let $\mathbf{u}(\mathbf{v})$ be the inverse transformation. Let $\mathbf{U}_{\mathbf{v}}$ the gradient of the transformation $\mathbf{u}(\mathbf{v})$ w.r.t. variables $\mathbf{v}$ and $\mathbf{V}_{\mathbf{u}}$ the gradient of the inverse transformation $\mathbf{v}(\mathbf{u})$, so that the differentials of the variables read

$$d \mathbf{u} = \mathbf{U}_{\mathbf{v}} d \mathbf{v} \quad , \quad d \mathbf{v} = \mathbf{V}_{\mathbf{u}} d \mathbf{u} \ .$$

These gradients are mutually inverse, $\mathbf{U}_{\mathbf{v}} = \mathbf{V}^{-1}_{\mathbf{u}}$. 
The convective form of the equations using $\mathbf{u}$ or $\mathbf{v}$ as primary variables are respectively

$$\begin{aligned}
 & \partial_t \mathbf{u} + \sum_{k=1}^{d} \mathbf{A}^{\mathbf{u}, k} \partial_k \mathbf{u} = \mathbf{s}^{\mathbf{u}} \\
 & \partial_t \mathbf{v} + \sum_{k=1}^{d} \mathbf{A}^{\mathbf{v}, k} \partial_k \mathbf{v} = \mathbf{s}^{\mathbf{v}} \\
\end{aligned}$$

with 

$$\begin{aligned}
  \mathbf{A}^{\mathbf{v},k} & = \mathbf{V}_{\mathbf{u}} \mathbf{A}^{\mathbf{u},k} \mathbf{U}_{\mathbf{v}} \\
  \mathbf{s}^{\mathbf{v}}   & = \mathbf{V}_{\mathbf{u}} \mathbf{s}^{\mathbf{u}}  \ .
\end{aligned}$$

The equations using $\mathbf{v}$ immediately follows after introducing the relation between the differentials and pre-multiplication of the equations by $\mathbf{V}_{\mathbf{u}}$,

[^spectral-cons-phys]: Once the problem is written in convective form, this set of variable could be an arbitrary set of variables and not only the conservative variables.


````{dropdown} Change of variables and spectral decomposition of the matrix $\ \mathbf{A}_{\hat{n}} \ $.

Starting from a set of variables $\mathbf{u}$ and the convective form of the equations

$$\mathbf{s} = \partial_t \mathbf{u} + \sum_{k} \mathbf{A}^k \partial_k \mathbf{u} \ ,$$

using another set of variables $\mathbf{v}$, the equations become

$$\begin{aligned}
  \mathbf{s} & = \partial_t \mathbf{u} + \sum_{k} \mathbf{A}^k \partial_k \mathbf{u} \\
  \mathbf{s} & = \mathbf{U}_{\mathbf{v}}(\mathbf{v}) \partial_t \mathbf{v} + \sum_{k} \mathbf{A}^k  \mathbf{U}_{\mathbf{v}}(\mathbf{v}) \partial_k \mathbf{v} \ ,
\end{aligned}$$

being $d \mathbf{u} = \mathbf{U}_{\mathbf{v}} d \mathbf{v}$. If the transformation is non-singular, and $\mathbf{U}_{\mathbf{v}}^{-1} = \mathbf{V}_{\mathbf{u}}(\mathbf{v})$, then the differential equations can be recast as

$$\partial_t \mathbf{v} + \sum_{k} \mathbf{V}_{\mathbf{u}} \mathbf{A}^k \mathbf{U}_{\mathbf{v}} \partial_k \mathbf{v} = \mathbf{V}_{\mathbf{u}} \mathbf{s}$$

With a coordinate transformation, the normal and tangential matrices become

$$\begin{aligned}
  \mathbf{A}^{\mathbf{v}}_{\mathbf{n}} 
  & = \sum_k n_k \mathbf{V}_{\mathbf{u}} \mathbf{A}^k \mathbf{U}_{\mathbf{v}} = \\
  & =  \mathbf{V}_{\mathbf{u}} \underbrace{\sum_k n_k \mathbf{A}^k}_{ \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} } \mathbf{U}_{\mathbf{v}} =   
       \mathbf{V}_{\mathbf{u}} \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} \mathbf{U}_{\mathbf{v}} \ ,
\end{aligned}$$

$$\mathbf{A}^{\mathbf{v}}_{\mathbf{t}_i} = \dots = \mathbf{V}_{\mathbf{u}} \mathbf{A}^{\mathbf{u}}_{\mathbf{t}_i} \mathbf{U}_{\mathbf{v}} \ .$$

**If** the change of variables is non-singular, the Jacobian matrices $\mathbf{V}_\mathbf{u}$, $\mathbf{U}_\mathbf{v}$ are non singular and reciprocally inverse. Thus, the **determinant** of the matrix $\mathbf{A}_{\mathbf{n}}$ is independent from the set of chosen variables, as

$$\begin{aligned}
 \text{det}\left( \mathbf{A}_{\mathbf{n}}^{\mathbf{v}} \right) 
 & = \text{det}\left( \mathbf{V}_{\mathbf{u}} \right) \text{det}\left( \mathbf{A}_{\mathbf{n}}^{\mathbf{u}} \right) \text{det}\left( \mathbf{U}_{\mathbf{v}} \right) = \\
 & = \text{det}\left( \mathbf{V}_{\mathbf{u}} \right) \text{det}\left( \mathbf{A}_{\mathbf{n}}^{\mathbf{u}} \right) \text{det}\left( \mathbf{V}_{\mathbf{u}} \right)^{-1} = \\
 & = \text{det}\left( \mathbf{A}_{\mathbf{n}}^{\mathbf{u}} \right) \ .
\end{aligned}$$

Thus, the **eigenvalues** are independent from the set of variables as well

$$\begin{aligned}
  0 & = \text{det}\left( s \mathbf{I} - \mathbf{A}^{\mathbf{v}}_{\mathbf{n}} \right) = \\
    & = \text{det} \left( \mathbf{V}_{\mathbf{u}} \right) \text{det}\left( s \mathbf{I} - \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} \right) \text{det} \left( \mathbf{U}_{\mathbf{v}} \right) = \\
    & = \text{det}\left( s \mathbf{I} - \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} \right) \ .
\end{aligned}$$

The relation between **right eigenvectors** immediately follows

$$\begin{aligned}
  \mathbf{A}^{\mathbf{v}}_{\mathbf{n}} \mathbf{R}^\mathbf{v} & = \mathbf{R}^\mathbf{v} \mathbf{S} \\
  \mathbf{V}_{\mathbf{u}} \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} \mathbf{U}_{\mathbf{v}} \mathbf{R}^\mathbf{v} & = \mathbf{R}^\mathbf{v} \mathbf{S} \\
  \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} \underbrace{\mathbf{U}_{\mathbf{v}} \mathbf{R}^\mathbf{v}}_{\mathbf{R}^\mathbf{u}} & = \underbrace{\mathbf{U}_{\mathbf{v}} \mathbf{R}^\mathbf{v}}_{\mathbf{R}^\mathbf{u}} \mathbf{S} \\
  \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} \mathbf{R}^\mathbf{u} & = \mathbf{R}^\mathbf{u} \mathbf{S} \ ,
\end{aligned}$$

with $\mathbf{R}^{\mathbf{u}} = \mathbf{U}_{\mathbf{v}} \mathbf{R}^\mathbf{v}$, or for any individual eigenvector $\mathbf{r}^\mathbf{u}_i = \mathbf{U}_{\mathbf{v}} \mathbf{r}^{\mathbf{v}}_i$.

The relation between **left eigenvectors** analogously follows

$$\begin{aligned}
  \mathbf{L}^\mathbf{v} \mathbf{A}^{\mathbf{v}}_{\mathbf{n}} & = \mathbf{S} \mathbf{L}^\mathbf{v} \\
  \mathbf{L}^\mathbf{v} \mathbf{V}_{\mathbf{u}} \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} \mathbf{U}_{\mathbf{v}} & = \mathbf{S} \mathbf{L}^\mathbf{v} \\
  \underbrace{\mathbf{L}^\mathbf{v} \mathbf{V}_{\mathbf{u}}}_{\mathbf{L}^\mathbf{u}} \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} & = \mathbf{S} \underbrace{\mathbf{L}^\mathbf{v} \mathbf{V}_{\mathbf{u}}}_{\mathbf{L}^\mathbf{u}}  \\
  \mathbf{L}^\mathbf{u} \mathbf{A}^{\mathbf{u}}_{\mathbf{n}} & = \mathbf{S} \mathbf{L}^\mathbf{u}  \ ,
\end{aligned}$$

with $\mathbf{L}^{\mathbf{u}} = \mathbf{L}^\mathbf{v} \mathbf{U}_{\mathbf{v}}$, or for any individual eigenvector $\left( \mathbf{l}^\mathbf{u}_i \right)^T = \left( \mathbf{l}^\mathbf{v}_i \right)^T \mathbf{U}_\mathbf{v}$, or $\mathbf{l}^\mathbf{u}_i = \mathbf{U}_\mathbf{v}^T \mathbf{l}^\mathbf{v}_i$.


````


* Eigenvalues, right and left eigenvectors
* Characteristic lines/surfaces, and compatibility conditions

(pde:hyperbolic:nd:draft:riemann)=
## Riemann problem

* Useful in numerical schemes in finite volume methods, using Godunov flux

(pde:hyperbolic:nd:draft:riemann:roe)=
### Linearization - Roe intermediate state

* Local linearization of the problem, to reduce the computational cost of solving non-linear Riemann problems at all the interfaces in a grid in FVM

(pde:hyperbolic:nd:draft:bc)=
## Boundary conditions

* characteristic-based
* wall
* ...

