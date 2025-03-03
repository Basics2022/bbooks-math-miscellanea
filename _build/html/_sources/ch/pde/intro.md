(pde)=
# Introduction to Partial Differential Equations

Partial differential equations usually comes from balance equations in **continuum mechanics**. Integral equations are the most general form of these equations, and an equivalent differential problem only exists if the fields involved in the equations are regular enough, for their derivatives to exist - and to apply theorems requiring some regularity of the functions.

Classical numerical methods:
- **FVM**: directly solves the **integral problem**, solving integral balance equations for cells in which the domain is divided
- **FDM**: given the problem in **differential form**, FDM directly approximates space derivatives of the **strong formulation** of the problem
- **FEM**: given the problem in **differential form**, FEM projects the **weak formulation** of the problem on a finite-dimensional space

- **BEM**: *integro-differential equation*, *singularities*,...

- **Spectral methods**,...
- **SEM**,...

(pde:examples)=
## Examples

In Physics:
- Advection equation

    $$\partial_t u + \vec{a} \cdot \nabla u = f$$

- Diffusion equation

    $$\partial_t u - \nu \nabla^2 u = f$$

- Hyperbolic equation/system of equations

    $$\partial_t \mathbf{u} + \nabla \cdot \mathbf{F}(\mathbf{u}) = \mathbf{f} $$

- Wave equation

    $$\frac{1}{c^2} \partial_{tt} u - \nabla^2 u = f$$

## Balance equations in physics

- Small-strain continuum mechanics

  $$\rho \partial_{tt} \vec{s} = \rho_0 \vec{g} + \nabla \cdot \symbf{\sigma}(\symbf{\varepsilon})$$

- Heat conduction

- Fluid dynamics

   - Navier-Stokes for compressible fluids  (conservative or convective equations)

     $$\begin{cases}
     \end{cases}$$

   - Navier-Stokes for incompressible fluids (convective form,...)

     $$\begin{cases}
        \rho \partial_t \vec{u} + \rho (\vec{u} \cdot \nabla ) \vec{u} - \mu \nabla^2 \vec{u} + \nabla P = \rho \vec{g} \\
        \nabla \cdot \vec{u} = 0
     \end{cases}$$

**todo** 
- Different forms of equations may be more or less convenient for different solution approaches
- Most of the physical laws comes from integral balance equation of the form

   $$\dfrac{d}{dt} \int_{V_t} \rho \mathbf{u} = \int_{V_t} \rho \mathbf{r} + \oint_{\partial V_t} \hat{n} \cdot \mathbf{T}(\mathbf{u})$$

   whose local - differential - form (in case of differentiable functions) readily follows from the application of Reynolds' transport theorem and divergence theorem to transform time derivative and boundary terms

   $$\begin{aligned}
     & \partial_t \left( \rho \mathbf{u} \right) + \nabla \cdot (\rho \mathbf{u} \vec{u}) = \rho \mathbf{r} + \nabla \cdot \mathbf{T}(\mathbf{u}) \\
     & \partial_t \left( \rho \mathbf{u} \right) + \nabla \cdot \mathbf{F}(\mathbf{u}) = \rho \mathbf{r} \ ,
   \end{aligned}$$

   and the physical meaning of each term is evident and readily expalinable as flux or volume or surface sources.
- Further manipulation/simplification may cover the clear meaning of the terms of the differential equation. As an example, the conservative form of Navier-Stokes equations for incompressible fluids with constant and uniform density read

  $$\begin{cases}
    \partial_t \left( \rho \vec{u} \right) + \nabla \cdot ( \rho \vec{u} \otimes \vec{u} ) = \rho \vec{g} + \nabla \cdot \mathbb{T} \\
    \nabla \cdot \vec{u} = 0 \ ,
  \end{cases}$$

  where the stress tensor for a Newtonian fluid reads

  $$\begin{aligned}
    \mathbb{T}
    & = - p \mathbb{I} + 2 \mu \mathbb{D} + \lambda \left( \nabla \cdot \vec{u} \right) \mathbb{I} \\
    & = - p \mathbb{I} + \mu \left( \nabla \vec{u} + \nabla^T \vec{u} \right) + \lambda \left( \nabla \cdot \vec{u} \right) \mathbb{I}
  \end{aligned}$$

  Using the incompressibility constraint $\nabla \cdot \vec{u}$, and treating the density $\rho$ as a constant and uniform parameter, the convective form of the Navier-Stokes equations reads

  $$\begin{cases}
    \rho \partial_t \vec{u} + \rho \left( \vec{u} \cdot \nabla \right) \vec{u} = \rho \vec{g} - \nabla P + 2 \mu \nabla \cdot \mathbb{D} \\
    \nabla \cdot \vec{u} = 0 \ .
  \end{cases}$$

  The divergence of the viscous stress tensor becomes

  $$2 \mu \nabla \cdot \mathbb{D} = \mu \nabla \cdot \left( \nabla \vec{u} + \nabla^T \vec{u} \right) = \mu \left( \nabla^2 \vec{u} + \nabla \underbrace{\left( \nabla \cdot \vec{u} \right)}_{= 0} \right) = \mu \nabla^2 \vec{u} \ ,$$

  so that one of the most common form of incompressible Navier-Stokes equations follows

  $$\begin{cases}
    \rho \partial_t \vec{u} + \rho ( \vec{u} \cdot \nabla ) \vec{u} - \mu \nabla^2 \vec{u} + \nabla P = \rho \vec{g} \\
    \nabla \cdot \vec{u} = 0 \ .
  \end{cases}$$

  It should be evident that in the latter form of Navier-Stokes equations no divergence explicitly appears, so that the right expression of surface source terms can't be found immediately. In momentum equation, surface source terms come from surface stress acting on the boundary of the domain, whose expression reads

  $$\begin{aligned}
    \vec{t}_n 
    & = \hat{n} \cdot \mathbb{T} = \\
    & = \hat{n} \cdot \left(- P \mathbb{I} + 2 \mu \mathbb{D} \right) = \\
    & = \hat{n} \cdot \left(- P \mathbb{I} + \mu \left( \nabla \vec{u} + \nabla^T \vec{u} \right) \right) = \\
    & = - P \hat{n} +  \hat{n} \cdot \left( \mu \left( \nabla \vec{u} + \nabla^T \vec{u} \right) \right) = \\
  \end{aligned}$$

  As an example, in [weak formulation of incompressible Navier-Stokes problem](ode:weak:ns-inc) the **natural boundary condition** arising in the method depends on the expression of the strong formulation of the NS problem. If one needs to prescribe stress boundary conditions, it could be an idea to start from NS equations w/o extra simplifications. 



