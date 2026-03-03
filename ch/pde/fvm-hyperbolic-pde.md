(pde:fvm:hyperbolic)=
# FVM for hyperbolic problems

```{dropdown} Approach
:open:

- Integral equations, often from balance or conservation laws
- [Numerical flux](pde:fvm:hyperbolic:flux)
  - features:
    - must be conservative...
    - must satisfy entropy condition, i.e. produce the physical solution (the limit of viscous problem for negligible viscosity) among the infinite possible solutions
  - schemes:
    - low-order
      - [Godunov](pde:fvm:hyperbolic:flux:godunov): the numerical flux is evaluated after solving a [Riemann problem]() at each cell interface, taking the $x = 0$ state $\mathbf{u}(x=0, t)$ to evaluate the flux $\mathbf{F}(\mathbf{u})$ at that cell boundary
      - [Roe](pde:fvm:hyperbolic:flux:roe) (~ linearized Godunov)
    - high-order schemes:
      - improve accuracy of differentiable solutions (no shock, no discontinuity) on regular grids
      - fail to represent the physical solution
    - high-resolution, (TVD schemes with flux limiters, MUSCL,...):
      - high-order methods where the solution is differentiable
      - low order method where the solution has discontinuities
      - high-resolution achieved as a linear combination of a low and high order flux

         $$F(u_{i+1/2}) = f^{low}_{i+1/2} + \phi(r_{i-1,i}) \left( f^{high}_{i+1/2} - f^{low}_{i+1/2} \right) \ ,$$

         being $\phi(r_{i,i+1})$ the flux limiter, i.e. a function of the gradient $r_i$ of the solution on the grid

- Theorems about numerics:
  - ...

```

(pde:fvm:hyperbolic:flux)=
## Numerical fluxes

(pde:fvm:hyperbolic:flux:godunov)=
### Godunov flux

...

(pde:fvm:hyperbolic:flux:roe)=
### Roe flux

Instead of solving the original non-linear problem,

$$\begin{aligned}
  \mathbf{0} 
  & = \partial_t \mathbf{u} + \partial_x \mathbf{F}(\mathbf{u}) = \\
  & = \partial_t \mathbf{u} + \mathbf{A}(\mathbf{u}) \partial_x \mathbf{u} \ .
\end{aligned}$$

a Roe solver aims at solving a linearized problem at each interface, namely

$$\mathbf{0} = \partial_t \mathbf{u} + \hat{\mathbf{A}}(\mathbf{u}_L, \mathbf{u}_R) \partial_x \mathbf{u} \ ,$$

being $\hat{\mathbf{A}}(\mathbf{u}_L, \mathbf{u}_R)$ an approximation of the convection matrix $\mathbf{A}(\mathbf{u})$ built with the states in the cells sharing the interface of interest: in time-explicit schemes, states in the cells $\mathbf{u}_L$, $\mathbf{u}_R$ are known, and so it is the linearized matrix $\hat{\mathbf{A}}(\mathbf{u}_L, \mathbf{u}_R)$.

**Intermediate state, $\hat{\mathbf{u}}$.** The linearized matrix can be written as the original matrix evaluated for an *intermediate state* $\hat{\mathbf{u}}(\mathbf{u}_L, \mathbf{u}_R)$,

$$\hat{\mathbf{A}}(\mathbf{u}_L, \mathbf{u}_R) = \mathbf{A}(\hat{\mathbf{u}}(\mathbf{u}_L, \mathbf{u}_R)) \ .$$

**Roe flux.** Roe flux looks similar to upwind scheme,

$$\begin{aligned}
  \mathbf{F}^{Roe}
  & = \frac{1}{2} \left( \mathbf{F}(\mathbf{u}_L) + \mathbf{F}(\mathbf{u}_R) - \left| \hat{\mathbf{A}}(\mathbf{u}_L, \mathbf{u}_R) \right| (\mathbf{u}_L - \mathbf{u}_R) \right) = \\
  & = \frac{1}{2} \left( \mathbf{F}(\mathbf{u}_L) + \mathbf{F}(\mathbf{u}_R) - \hat{\mathbf{R}} \left| \hat{\boldsymbol{\Lambda}} \right| \hat{\mathbf{L}} (\mathbf{u}_L - \mathbf{u}_R) \right) \ .
\end{aligned}$$

**Properties.** Roe matrix needs to satisfy the following properties:

1. **diagonalization**: $\hat{\mathbf{A}}$ is diagonalizable
2. **consistency**: if $\mathbf{u}_L, \mathbf{u}_R \rightarrow \mathbf{u}$, then $\hat{\mathbf{u}} \rightarrow \mathbf{u}$
3. **conservation**: $\mathbf{A}(\hat{\mathbf{u}}) \left( \mathbf{u}_L - \mathbf{u}_R \right) = \mathbf{F}(\mathbf{u}_L) - \mathbf{F}(\mathbf{u}_R)$

````{prf:example} P-sys. Intermediate state

**Intermediate state.** For each value of $\hat{\rho}$,

$$\hat{u} = \frac{\sqrt{\rho_L} u_L + \sqrt{\rho_R} u_R}{\sqrt{\rho_L} + \sqrt{\rho_R}} \ ,$$

and thus

$$\hat{m} = \hat{\rho} \hat{u} \ .$$

```{dropdown} Details

3. **Conservation**

$$\mathbf{A}(\hat{\mathbf{u}})(\mathbf{u}_L - \mathbf{u}_R) = \mathbf{F}_L - \mathbf{F}_R \ .$$

explicitly, using conservative variables

$$
\begin{bmatrix} 0 & 1 \\ a^2 - \frac{\hat{m}^2}{\hat{\rho}^2} & 2 \frac{\hat{m}}{\hat{\rho}}  \end{bmatrix}
\begin{bmatrix} \rho_L - \rho_R \\ m_L - m_R \end{bmatrix} = 
\begin{bmatrix} \rho_L - \rho_R \\ \frac{m_L^2}{\rho_L} + \rho_L a^2 - \frac{m_R^2}{\rho_R} - \rho_R a^2 \end{bmatrix} \ .
$$

The first equation is identically satisfied. The second equation in $\hat{u}$ reads

$$\begin{aligned}
  0
  & = (a^2 - \hat{u}^2) (\rho_L - \rho_R) + 2 \hat{u} \left( \rho_L u_L - \rho_R u_R \right) - \rho_L u_L^2 - \rho_L a^2 + \rho_R u_R^2 + \rho_R a^2 =  \\
  & = - \hat{u}^2 (\rho_L - \rho_R) + 2 \hat{u} \left( \rho_L u_L - \rho_R u_R \right) - \rho_L u_L^2 + \rho_R u_R^2 =  \\
\end{aligned}$$

and collecting terms

$$\begin{aligned}
  0
  & = \rho_L ( \hat{u} - u_L )^2 - \rho_R (\hat{u} - u_R )^2 
\end{aligned}$$

or, with $\rho > 0$,

$$\sqrt{\rho_L} ( \hat{u} - u_L ) = \mp \sqrt{\rho_R} (\hat{u} - u_R) \ ,$$

so that the solution that avoids singularities for $\rho_L = \rho_R$ (the one with the minus sign above) reads

$$\hat{u} = \frac{\sqrt{\rho_L} u_L + \sqrt{\rho_R} u_R}{\sqrt{\rho_L} + \sqrt{\rho_R}} \ ,$$

2. **Consistency.** From this choice of sign, consistency follows immediately,

$$\lim_{\mathbf{u}_L, \mathbf{u}_R \rightarrow \mathbf{u}} \hat{\mathbf{u}}(\mathbf{u}_L, \mathbf{u}_R) = \mathbf{u} \ .$$

```

````

