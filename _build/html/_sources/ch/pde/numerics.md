(pde:numerics)=
# Introduction to numerical methods for PDEs

Different numerical methods for PDEs rely on the discretization of different formulations of the continunuos problems. As an example,
- **FDM, Finite difference methods** rely on the approximation of derivatives of the **strong formulation** of the problem
- [**FEM, Finite element methods**](pde:fem) rely on a finite dimensional approximation of the **weak formulation** of the problem; usually the finite dimensional approximation can be interpreted as a projection of a infinite dimensional continuous problem onto a finite dimensional space, the space of the choosen finite elements
- [**FVM, Finite volume methods**](pde:fvm) rely on an approximation of the **integral formulation** of the problem
- [**BEM, Boundary elemement methods**](pde:bem) rely on an approximation of a **boundary integral formulation** of  the problem, when it's feasible and convenient
- ...*spectral methods*, *spectral element methods*,...

**Characteristics.**
- grid: domain-grid-based, buondary-grid-based, grid-free methods
- range of interaction: short in physical space for FDV, FEM, FVM; long-range for boundary element methods, even though clustering techniques are available, like FMM; (usually) over the whole domain in space, short-range interaction in wave-number space for spectral methods; 

**Pros and cons.** *More suited methods for each problems...; domain, order,...*

Let's take Poisson equations for a scalar function $u(\vec{r})$ to show all the possible approaches above. Here we start from the most general version of the equation, namely the integral form. As it's shown in [Continuum Mechanics:Governing Equations](https://basics2022.github.io/bbooks-physics-continuum-mechanics/ch/continuum/governing-equations.html), the most general form of balance equations is the integral form, while the differential form can be seamlessly derived only when the quantities involved are regular enough, to apply Stokes' theorem and for the derivatives appearing to exist.

The problem of interest can be interpreted as the problem of finding the temperature field $u(\vec{r})$ during steady heat conduction in the domain $\Omega$, with distributed volume heat source $f(\vec{r})$. Fourier's law assume that condcution heat flux is proportional to the gradient of the temperature, $\vec{q} = - k \nabla u$. Temperature is prescribed, $u = g$ on the region of the boundary $S_D$, while the heat flux is prescribed  $\hat{n} \cdot \vec{q} = h$ on the region of the boundary $S_N$.

The **integral formulation** of the problem for all the boundary reads

$$0 = - \oint_{\partial \Omega} \hat{n} \cdot \vec{q} + \int_{\Omega} f \ .$$ (eq:example:pde:poisson:integral)

```{prf:example} Finite volume methods
:label: pde:ex:fvm

Finite volume methods rely on a tassellation of the domain $\Omega = \cup_k \Omega_k$, to write and solve the integral balance equation {eq}`eq:example:pde:poisson:integral` for all the elemantary domain $\Omega_k$.

$$0 = - \oint_{\partial \Omega_k} \hat{n} \cdot \vec{q} + \int_{\Omega_k} f \ .$$ (eq:example:pde:poisson:integral:elementary)

evaluating volume integrals with the internal variables of the cell $\Omega_k$, and boundary flux with the variables of the cell $\Omega_k$ and the neighbouring cells $\Omega_i \in B_k$. Introducing the definition of numerical flux $F_{ik}(u_i, u_k)$ at the interface between a generic discrete version of the balance equation  {eq}`eq:example:pde:poisson:integral:elementary` for the $k^{th}$ element becomes

$$0 = - \sum_{\Omega_i \in B_k} F_{ik}(u_i, u_k) + S_k(u_k) \ .$$

Different numerical methods differs in the evaluation of fluxes and sources.
FVM is **conservative** as it evaluate flux at interfaces and then distribute it to neighoring cells, see {prf:ref}`fvm:property:conservation`. A rough elementwise-uniform variable with jump at interfaces and diffusive flux,

$$F_{ik} = - A_{ik} \, k \, \frac{u_i - u_k}{d_{ik}} \ ,$$

with $d_{ik}$ equal to the distance of the centers of elements $i$ and $k$, leads to the balance equation for the internal volume $\Omega_k$,

$$ 0 = \sum_{i} A_{ik} \, k \, \frac{u_i-u_k}{d_{ik}} + V_k f_k \ .$$

Volumes at the boundary are influenced by fluxes at the boundaries and boundary conditions in general. 

For regular cubic mesh, $A_{ik} = \Delta x$, $d_{ik} = \Delta x$, $V_k = \Delta x$, and thus the equations for internal elements become

$$0 = k \sum_{i \in \Omega_k} \frac{u_i - u_k}{\Delta x^2} + f_k \ ,$$

where the summation is exactly equal to the center-difference stencil for the Laplacian, used in finite difference method {prf:ref}`pde:ex:fdm`.


```

**If fields are regular enough** to apply Stokes' theorem, it's possible to derive differential problem from the integral formulation,

$$\begin{aligned}
  0 
    = - \oint_{\partial V} \hat{n} \cdot \vec{q} + \int_{V} f 
    = - \int_{V} \nabla \cdot \vec{q} + \int_{V} f = \int_{V} \left( - \nabla \cdot \vec{q} + f  \right)
\end{aligned}$$

Exploiting the arbitrariety of the volume $V$, the **strong form** of the differential problem is the Poisson equation with suitable boundary conditions,

$$\begin{cases}
  - \nabla \cdot \left( k \nabla u \right) = f(\vec{r}) \ , & \vec{r} \in V \\
  u = g(\vec{r})                                        \ , & \vec{r} \in S_{D} \\
  \hat{n} \cdot \nabla u = h(\vec{r})                   \ , & \vec{r} \in S_{N}  \\
\end{cases}$$

only holds in regions of the domain where the functions involved are continuous and differentiable, i.e. everything written in the problem is not meaningful, i.e. at least it exists. 


```{prf:example} Finite difference methods
:label: pde:ex:fdm

Finite different method approximates the strong form of the problem, building a stencil to evaluate an approximation of the Laplacian. On a cubic regular grid ($\Delta x = \Delta y = \Delta z$), the Laplacian van be evaluated with a 7-point stencil

$$\begin{aligned}
  \nabla^2 u
  & = \partial_{xx} u + \partial_{yy} u + \partial_{zz} u = \\
  & = \dfrac{u_{i+1,j,k} - 2 u_{i,j,k} + u_{i-1,j,k}}{\Delta x^2} + \dfrac{u_{i,j+1,k} - 2 u_{i,j,k} + u_{i,j-1,k}}{\Delta y^2} + \dfrac{u_{i,j,k+1} - 2 u_{i,j,k} + u_{i,j,k-1}}{\Delta z^2} =  \\
  & = \dfrac{1}{\Delta x^2} \left[ - 6 u_{i,j,k} + u_{i+1,j,k} + u_{i-1,j,k} + u_{i,j+1,k} + u_{i,j-1,k} + u_{i,j,k+1} + u_{i,j,k-1} \right] = \\
  & = \dfrac{1}{\Delta x^2} \sum_{i \in B_k} (u_i - u_k)
\end{aligned}$$

and it's equal to the same expression already provided for the rough finite volume method with regular grid, in {prf:ref}`pde:ex:fvm`

```

Starting from strong formulation of the differential problem, the **weak formulation** of the problem is derived:
- multiplying the strong problem by an arbitrary test function $w(\vec{r})$ compatible with the essential constraints
- integrating over the whole domain

$$\begin{aligned}
  0
  & = \int_{V} w(\vec{r}) \cdot \left[ - \nabla \cdot \left( k \nabla u \right) - f(\vec{r}) \right] = \\
  & = \int_{V} \left\{  k \nabla w(\vec{r}) \cdot  \nabla u(\vec{r}) - w(\vec{r}) f(\vec{r}) \right\} - \oint_{\partial V} w(\vec{r}) \, \hat{n} \cdot \nabla u \qquad \forall w(\vec{r}) \ .
\end{aligned}$$

Using a test function $w(\vec{r})$ equal to zero on the boundary where essential boundary conditions are prescribed $\left.w\right|_{S_D} = 0$, and introducing the natural boundary conditions of the Neumann boundary $S_N$, $\left. \hat{n} \cdot \nabla u\right|_{S_N} = h$,

$$\int_{V} k \nabla w \cdot \nabla u = \int_V w f + \int_{S_N} w h \ , \quad \forall w$$

compatible with essential boundary conditions.

```{prf:example} Finite element methods
:label: pde:ex:fem

Finite element methods build an $N$-dimensional systems:
- approximating the solution as a linear combination of $N$ base functions, $u(\vec{r}) = \sum_j \phi_j(\vec{r}) u_j$
- testing the equation over $N$ independent test functions $\psi_i(\vec{r})$

i.e. the $i^{th}$ equation becomes

$$\int_{V} k \nabla \psi_i(\vec{r}) \cdot \nabla \phi_j(\vec{r}) \, u_j = \int_{V} \psi_i(\vec{r}) f + \int_{S_N} \psi_i(\vec{r}) h \ ,$$

or briefly

$$K_{ij} u_j = f_i \qquad , \qquad \mathbf{K} \mathbf{u} = \mathbf{f} \ .$$

A common choice uses the same functions both as test and base functions, $\psi_i(\vec{r}) = \phi_i(\vec{r})$.


```

The differential problem in strong form can be recast as a boundary element problem exploiting the properties of Green's functions $G(\vec{r}; \vec{r}_0)$

$$\begin{aligned}
  E(\vec{r}_0) u(\vec{r}_0) 
  & = \int_{\vec{r} \in V} u(\vec{r}) \delta(\vec{r}- \vec{r}_0) \, dV = \\
  & = - \int_{\vec{r} \in V} u(\vec{r}) \nabla^2 G(\vec{r};\vec{r}_0) \, dV = \\
  & = - \oint_{\vec{r} \in \partial V} u(\vec{r}) \hat{n}(\vec{r}) \cdot \nabla G(\vec{r};\vec{r}_0) \, dS 
      + \oint_{\vec{r} \in \partial V} G(\vec{r};\vec{r}_0) \hat{n}(\vec{r}) \cdot \nabla u(\vec{r}) \, dS
      - \int_{\vec{r} \in V} G(\vec{r}; \vec{r}_0) \nabla^2 u (\vec{r}) \, dV  = \\
  & = - \oint_{\vec{r} \in \partial V} u(\vec{r}) \hat{n}(\vec{r}) \cdot \nabla G(\vec{r};\vec{r}_0) \, dS 
      + \oint_{\vec{r} \in \partial V} G(\vec{r};\vec{r}_0) \hat{n}(\vec{r}) \cdot \nabla u(\vec{r}) \, dS
      + \int_{\vec{r} \in V} G(\vec{r}; \vec{r}_0) f(\vec{r}) \, dV \ .
\end{aligned}$$

The value of the unknown function or the flux $\hat{n} \cdot \nabla u$ are known on the Dirichlet and Neumann regions of the boundary respectively, and so the integro-differential problem becomes

$$E(\vec{r}_0) u(\vec{r}_0) + \int_{S_N} u \hat{n} \cdot \nabla G \, dS - \int_{S_D} G \, \hat{n} \cdot \nabla u \, dS = \int_{S_D} g \hat{n} \cdot \nabla G \, dS - \int_{S_N} G h \, dS + \int_{\vec{r} \in V} G f \, dV$$

The unknown function on is approximated on the boundary $\partial V$ of the domain as a $N$-finite dimensional approximation, as an example

$$u(\vec{r}) = \sum_{j} \phi_j(\vec{r}) u_j \qquad , \qquad \vec{r} \in \partial V \ ,$$

and the integro-differential equation is evaluated in $N$ different points $\vec{r}_{0,i}$ in order to get a $N,N$ linear equation in the 





