(pde:hyperbolic:characteristics)=
# Method of characteristics

## Scalar multi-dimensional problem

$$\begin{aligned}
  \mathbf{a}^T(u(\mathbf{x}), \mathbf{x}) \, \boldsymbol\nabla  u(\mathbf{x}) & = c(u(\mathbf{x}), \mathbf{x}) \quad , \quad \mathbf{x} \in D \\
  a_k(u(\mathbf{x}), \mathbf{x}) \frac{\partial}{\partial x_k} u(\mathbf{x}) & = c(u(\mathbf{x}), \mathbf{x}) 
\end{aligned}$$

The method of characteristics aims at transforming the PDE over the domain $D$, in a set of ODEs over lines - the characteristic lines. Both the coordinates of these lines and the unknown function on these lines are written in parametric form as

$$\begin{aligned}
  \mathbf{x} & = \mathbf{X}(s) \\
  u(\mathbf{X}(s)) & = U(s) \ .
\end{aligned}$$

Now, taking the ordinary derivative of $U'(s)$,

$$U'(s) = \frac{d X_k}{d s}(s) \frac{\partial u}{\partial x_k}\left( \mathbf{X}(s) \right) \ .$$

If the characteristic lines are defined by the differential equation $X'_k(s) = a_k(U(s), X(s))$, the set of ODEs become

$$\begin{aligned}
 U'(s) & = c\left(U(s), \mathbf{X}(s)\right) \\
 \mathbf{X}'(s) & = \mathbf{a}\left(U(s), \mathbf{X}(s)\right) \ .
\end{aligned}$$

## Vector multi-dimensional problem

**todo** *Characteristic method fails...characteristic - eikonal - equation. Uncomment*

Let 

$$\begin{aligned}
  \mathbf{u}(t, \mathbf{r}): & \ \mathbb{R} \times \mathbb{R}^d \rightarrow \mathbb{R}^n \\
  \mathbf{F}(   \mathbf{u}): & \ \mathbb{R}^{n} \rightarrow \mathbb{R}^{d} \times \mathbb{R}^n \\
  \mathbf{s}(t, \mathbf{r}): & \ \mathbb{R} \times \mathbb{R}^d \rightarrow \mathbb{R}^n \\
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

This problem can be made a little more general with by defining $\mathbf{x} = (t, \mathbf{r}) = ( x_0, \mathbf{r} )$, as

$$\sum_{j=0}^{d} \mathbf{A}^j \, \partial_j \mathbf{u} = \mathbf{s} \ .$$

The former expression of the hyperbolic problem immediately follows if $\mathbf{A}_0 = \mathbf{I}_n$, $A^0_{ik} = \delta_{ik}$, and 

$$\widetilde{\nabla} \cdot \widetilde{\mathbf{F}} = \partial_0 \mathbf{F}_0 + \sum_{j=1}^{d} \partial_j \mathbf{F}_j = \widetilde{\nabla} \cdot \begin{bmatrix} \ \mathbf{u} \ | \ \mathbf{F} \ \end{bmatrix} \ .$$

as, for $i = 1:n$,

$$\delta_{ik} = \partial_{u_k} F_{0i} \quad \rightarrow \quad F_{0i} = u_k \delta_{ik} = u_i \ .$$


### Taylor expansion of a solution

Starting from the solution on a manifold determined by the equation $S: f(\mathbf{x}) = 0$, $\mathbf{x}_0 \in S$, if the solution is differentiable, the solution in a point $\mathbf{x} = \mathbf{x}_0 + \Delta \mathbf{x}$ reads

$$\begin{aligned}
  \mathbf{u}(\mathbf{x}) & \sim \mathbf{u}(\mathbf{x}_0) + \Delta \mathbf{x} \cdot \nabla \mathbf{u}(\mathbf{x}_0) \\
  u_i(\mathbf{x}) & \sim u_i(\mathbf{x}_0) + \Delta_j \frac{\partial u_i}{\partial x_j} \ .
\end{aligned}$$

Now, with a change of coordinates from $\mathbf{x}$ to $\boldsymbol\xi = (n, \mathbf{t})$, i.e. to local normal and tangential direction,

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

must be invertible, to formally get

$$\partial_n \mathbf{u} = \mathbf{A}_{\hat{\mathbf{n}}}^{-1} \left( \mathbf{s} - \sum_{\ell=1}^{d} \mathbf{A}_{\hat{\mathbf{t}}_\ell} \partial_{t_\ell} \mathbf{u} \right) \ .$$

This expression of the normal derivative of the solution - whenever it exists - can be used to find the approximation of the solution in normal direction w.r.t. the surface $S$, i.e. with $\Delta \mathbf{x} = \Delta \ell \hat{\mathbf{n}}$ as

$$\begin{aligned}
  \mathbf{u}(\mathbf{x}) 
  & \sim \mathbf{u}(\mathbf{x}_0) + \Delta \ell \, \hat{\mathbf{n}} \cdot \nabla \mathbf{u}(\mathbf{x}_0) = \\
  & = \mathbf{u}(\mathbf{x}_0) + \Delta \ell \, \partial_{n} \mathbf{u}(\mathbf{x}_0) \ .
\end{aligned}$$

**If** the matrix $\mathbf{A}_{\hat{\mathbf{n}}}$ is diagonalizable, it's invertible if it has no zero eigenvalue.

**todo** 
- *compatibility conditions*
- *eikonal equation*
- *explicitly treating steady vs. unsteady problems*

### Examples

#### Shallow water

#### Isothermal compressible flow

#### Euler equations for inviscid compressible flows



