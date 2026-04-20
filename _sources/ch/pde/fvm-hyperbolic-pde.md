(pde:fvm:hyperbolic)=
# FVM for hyperbolic problems

```{dropdown} Approach
:open:

- Integral equations, often from balance or conservation laws
- First, problems in 1-dimensional domains are treated. Most of the features of a finite volume method are treated for 1-dimensional problems
  - flux: characteristics and common schemes
  - implementation: evaluation of flux at interfaces and distribution on cells
  - boundary conditions
  - ...

  then everything is naturally generalized to multi-dimensional domain: each interface of a cell in a multi-dimensional domain is locally treated as a 1-dimensional domain.

- [Numerical flux](pde:fvm:hyperbolic:flux)
  - features:
    - must be conservative...
    - must satisfy **entropy condition**, i.e. produce the physical solution (the limit of viscous problem for negligible viscosity) among the infinite possible solutions
  - schemes:
    - low-order
      - [Godunov](pde:fvm:hyperbolic:flux:godunov): the numerical flux is evaluated after solving a [Riemann problem](pde:hyperbolic:riemann-pb) at each cell interface, taking the $x = 0$ state $\mathbf{u}(x=0, t)$ to evaluate the flux $\mathbf{F}(\mathbf{u})$ at that cell boundary
      - [Roe](pde:fvm:hyperbolic:flux:roe) (~ linearized Godunov) + [entropy fix](pde:fvm:hyperbolic:flux:entropy-fix) required for the numerical method to select the physical solution
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
  - **CFL (Courant-Friedrichs-Lewy) condition** for explicit-time schemes (it could hold locally...),
   
     $$\Delta t \le \frac{\Delta x}{|\lambda|_{\max}}$$

  - ...*results about fluxes*...

```

(pde:fvm:hyperbolic:flux)=
## Numerical fluxes

(pde:fvm:hyperbolic:flux:godunov)=
### Godunov flux

The numerical flux in Godunov scheme is the flux $\mathbf{F}$ evaluated with the state at the interface of two neighboring cells, resulting from  the solution of the [Riemann problem](pde:hyperbolic:riemann-pb) between the two cells. 

For a piecewise constant approximation of the fields (like in standard finite volume methods), the evolution at each cell interface can be treated as a Riemann problem

In order to calculate the numerical flux at the interface $i$, separating cells $A$, $B$
1. The Riemann problem is solved at interface $i$ separating the two cells with uniform fields $\mathbf{u}_A(t)$, $\mathbf{u}_B(t)$. Let $\mathbf{u}_i(x,t+\Delta t)$ be the solution, being $x$ a local coordinate (orthogonal to the interface for multi-dimensional domains) with $x=0$ at the interface, and $\Delta t > 0$. Riemann problem is a **non-linear problem**, so a non-linear solver is required. In order to avoid (expensive) non-linear methods, [Roe scheme](pde:fvm:hyperbolic:flux:roe) is introduced in the next section. 
2. The state at interface $\mathbf{u}_i(x=0,t+\Delta t)$ is retrieved from the solution of the Riemann problem
3. The numerical flux is evaluated with the state at the interface

   $$\mathbf{F}_i(t) = \mathbf{F}(\mathbf{u}_i(0,t)) \ .$$

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

2. **Consistency.** From this choice of sign, consistency of the velocity follows immediately,

$$\lim_{\mathbf{u}_L, \mathbf{u}_R \rightarrow \mathbf{u}} \hat{\mathbf{u}}(\mathbf{u}_L, \mathbf{u}_R) = \mathbf{u} \ .$$

Arbitrary intermediate value of the density $\hat{\rho}$ needs to satisfy consistency, as well. Just as an example, if $\hat{\rho}$ is chosen to be the average of the densities, $\hat{\rho} = \frac{1}{2}(\rho_L + \rho_R)$, this is consistent choice.

```

````

````{prf:example} Euler equations. Intermediate state

**Intermediate state.** For each value of $\hat{\rho}$,

$$\begin{aligned}
  \hat{u}   & = \frac{\sqrt{\rho_L} u_L + \sqrt{\rho_R} u_R}{\sqrt{\rho_L} + \sqrt{\rho_R}} \\
  \hat{h}^t & = \langle h^t \rangle_{\sqrt{\rho}} = \frac{ \sqrt{\rho_L} h^t_L + \sqrt{\rho_R} h^t_R }{\sqrt{\rho_L} + \sqrt{\rho_R}}
\end{aligned}$$

while $\hat{\rho}$ can be found (if not trivial) solving an additional condition

$$\Delta P =
    \Delta \rho \, \partial_\rho \Pi(\hat{\rho},\hat{\rho}\hat{u},\hat{E}^t(\hat{\rho}, \hat{u}, \hat{h}^t)) 
  + \Delta m    \, \partial_m    \Pi(\hat{\rho},\hat{\rho}\hat{u},\hat{E}^t(\hat{\rho}, \hat{u}, \hat{h}^t)) 
  + \Delta E^t  \, \partial_{E^t}\Pi(\hat{\rho},\hat{\rho}\hat{u},\hat{E}^t(\hat{\rho}, \hat{u}, \hat{h}^t)) \ .$$

If this condition is an identity - as it is for a perfect ideal gas - any value of $\hat{\rho}$ satisfying consistency is allowed.


```{dropdown} Details

3. **Conservation**

$$\mathbf{A}(\hat{\mathbf{u}})(\mathbf{u}_L - \mathbf{u}_R) = \mathbf{F}_L - \mathbf{F}_R \ .$$

explicitly, using conservative variables

$$
\begin{bmatrix} 0 & 1 & 0 \\ - \frac{m^2}{\rho^2} + \partial_\rho \Pi & \frac{2 m}{\rho} + \partial_m \Pi & \partial_{E^t} \Pi \\ - \frac{m}{\rho^2}(E^t+\Pi)+ \frac{m}{\rho}\partial_\rho \Pi & \frac{1}{\rho} (E^t + \Pi) + \frac{m}{ \rho} \partial_{m} \Pi & \frac{m}{\rho} \left( 1 + \partial_{E^t} \Pi \right) \end{bmatrix}
\begin{bmatrix} \rho_L - \rho_R \\ m_L - m_R \\ E^t_L - E^t_R \end{bmatrix} = 
\left|\begin{bmatrix} \rho \\ \frac{m^2}{\rho} + \Pi(\rho,m,E^t) \\ \frac{m}{\rho} \left( E^t+\Pi(\rho,m,E^t) \right) \end{bmatrix}\right|^L_R 
$$

or


$$
\begin{bmatrix} 0 & 1 & 0 \\ - \hat{u}^2 + \partial_\rho \Pi & 2 \hat{u} + \partial_m \Pi & \partial_{E^t} \Pi \\ - \hat{u} \hat{h}^t + \hat{u} \partial_\rho \Pi & \hat{h}^t + \hat{u} \partial_{m} \Pi & \hat{u} \left( 1 + \partial_{E^t} \Pi \right) \end{bmatrix}
\begin{bmatrix} \rho_L - \rho_R \\ \rho_L u_L - \rho_R u_R \\ E^t_L - E^t_R \end{bmatrix} = 
\left|\begin{bmatrix} \rho \\ \rho u^2 + \Pi(\rho,m,E^t) \\ \rho u h^t  \end{bmatrix}\right|^L_R 
$$

<!--
Using the values of partial derivatives of the function $p(\rho, e) = p\left(\rho, \frac{E^t}{\rho} - \frac{m^2}{2\rho^2} \right) = \Pi(\rho, m, E^t)$ evaluated [here:Non-linear systems:example:Euler equation in 1-dimensional domain](pde:hyperbolic:dimensions)

$$\begin{aligned}
  \partial_\rho \Pi & = c^2 + \partial_e P|_{\rho} \left( - \frac{{h^t}^2}{\rho} + \frac{u^2}{\rho} \right) \\
  \partial_m    \Pi & =       \partial_e P|_{\rho} \left( - \frac{m}{\rho^2}  \right) \\
  \partial_{E^t}\Pi & =       \partial_e P|_{\rho} \left(   \frac{1}{\rho  }  \right) \\
  c^2 & = \partial_\rho P|_{e} + \frac{p}{\rho^2} \partial_e p|_{\rho} \ .
\end{aligned}$$
-->

* The first equation is an identity

* The second equation in $\hat{u}$ gives

   $$\begin{aligned}
     0 
     & = - \left.\left[ \rho ( \hat{u} - u )^2 \right]\right|_R^L +  \left.\left( \rho \partial_\rho \hat{\Pi} + \rho u \partial_m \hat{\Pi} + E^t \partial_{E^t} \hat{\Pi} - \Pi \right)\right|_{R}^{L} \ ,
   \end{aligned}$$

* The third equation in $\hat{h}^t$ gives
   
   $$\begin{aligned}
     0 
     & = \left.\left[ \rho ( u - \hat{u} ) \hat{h}^t \right]\right|_R^L + \left.\left[ \hat{u} \rho \partial_\rho \hat{\Pi} + \hat{u} m \partial_m \hat{\Pi} + \hat{u} E^t \partial_{E^t} \hat{\Pi} + \hat{u} \underbrace{E^t}_{= \rho h^t - p} - \rho u h^t \right]\right|_L^R = \\
     & = \left.\left[ \rho ( u - \hat{u} ) \hat{h}^t + \rho h^t ( \hat{u} - u ) \right]\right|_R^L + \hat{u} \left.\left[ \rho \partial_\rho \hat{\Pi} + m \partial_m \hat{\Pi} + E^t \partial_{E^t} \hat{\Pi} - \Pi \right]\right|_L^R = \\ 
     & = \left.\left[ \rho ( u - \hat{u} ) ( \hat{h}^t - h^t ) \right]\right|_R^L + \hat{u} \left.\left[ \rho \partial_\rho \hat{\Pi} + m \partial_m \hat{\Pi} + E^t \partial_{E^t} \hat{\Pi} - \Pi \right]\right|_L^R \ .
   \end{aligned}$$

Adding the condition $\Delta P = \Delta \rho \partial_\rho \hat{\Pi} + m \partial_m \hat{\Pi} + E^t \partial_{E^t} \hat{\Pi}$, the second equation can be solved for $\hat{u}$ (choosing the solution providing consistency - see P-sys example for a brief discussion)

$$\hat{u} = \langle u \rangle_{\sqrt{\rho}} = \frac{ \sqrt{\rho_L} u_L + \sqrt{\rho_R} u_R }{\sqrt{\rho_L} + \sqrt{\rho_R}}$$

and the third equation can be solved for $\hat{h}^t$ (using $\sqrt{\rho_L}(u_L - \hat{u}) = - \sqrt{\rho_R}(u_R - \hat{u})$ from the expression of $\hat{u}$ to get the equation $\sqrt{\rho}(\hat{h}^t - h^t_L) = - \sqrt{\rho_R}(\hat{h}^t - h^t_R)$),

$$\hat{h}^t = \langle h^t \rangle_{\sqrt{\rho}} = \frac{ \sqrt{\rho_L} h^t_L + \sqrt{\rho_R} h^t_R }{\sqrt{\rho_L} + \sqrt{\rho_R}}$$

For a medium with generic equations of state, the condition about $\Delta p$ introduced above can be eventually solved to find the value of $\hat{\rho}$. For a perfect ideal gas (PIG), this condition is an identity providing no additional information on the value of $\hat{\rho}$

2. **Consistency.** ...


```

````

(pde:fvm:hyperbolic:flux:entropy-fix)=
### Entropy fix

Entropy fix is required to exploit numerical dissipation in choosing the physical solution, when some eigenvalue is close to zero. As an example, a threshold is set as a ratio of the local speed of sound $a$, e.g. $\delta = 0.1 \div 0.2$ and the Roe matrix is modified as

$$\hat{\mathbf{A}}^{s\, fix} = \hat{\mathbf{R}} \left| \hat{\boldsymbol{\Lambda}}^{s\, fix} \right| \hat{\mathbf{L}} \ ,$$

with 

$$
\left| \hat{\boldsymbol{\Lambda}}^{s\, fix}_{i} \right| = 
\left\{\begin{aligned} 
  & |\lambda_i| && |\lambda_i| \ge \delta a \\
  & \frac{|\lambda_i|^2}{2 \delta a} + \frac{\delta a}{2} && |\lambda_i| < \delta a \\
\end{aligned}\right.
$$

**todo** *Add discussion about* **numerical dissipation** *and some numerical examples...*



