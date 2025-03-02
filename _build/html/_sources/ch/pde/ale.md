(pde:ale-description)=
# Arbitrary Lagrangian-Eulerian description

Reynold's transport theorem allows for the formulation of intergal equations, and grid-based methods like FVM, on moving grids and changing domains. Rules for derivatives of composite functions provide the relations between time derivatives in a Lagrangian, Eulerian, or arbitrary description,

$$\begin{aligned}
  & \left.\dfrac{\partial f}{\partial t}\right|_{\vec{r}_0} = \left.\dfrac{\partial f}{\partial t}\right|_{\vec{r}} + \vec{u}   \cdot \nabla f \\
  & \left.\dfrac{\partial f}{\partial t}\right|_{\vec{r}_b} = \left.\dfrac{\partial f}{\partial t}\right|_{\vec{r}} + \vec{u}_b \cdot \nabla f \\
\end{aligned}$$

Equations governing the motion of the grid are usually required as well. E.g.: 
- known and prescribed motion of the grid;
- boundary conditions only without changing grids (for small displacements)
- pseudo-elastic deformation (usually good for small strain and displacement; 
- for large displacements of/or models with complex geometry, sliding and/or overlapping grids could an option for grid-based methods.

(pde:ale-description:integral)=
## Integral problem

Application of Reynolds theorem to the balance equation of the quantity $\mathbf{u}$ for a material volume $V_t$

$$\dfrac{d}{dt} \int_{V_t} \rho \mathbf{u} = \int_{V_t} \rho \mathbf{f} + \oint_{\partial V_t} \hat{n} \cdot \mathbf{T} \ .$$

provides the expression of the balance equation for a geometrical volume $v_t$ in arbitrary motion,

$$\dfrac{d}{dt} \int_{v_t} \rho \mathbf{u} + \oint_{\partial v_t} \rho \mathbf{u} \left( \vec{u} - \vec{u}_b \right) \cdot \hat{n} = \int_{v_t} \rho \mathbf{f} + \oint_{\partial v_t} \hat{n} \cdot \mathbf{T} \ .$$

Here, the integral forulation of the problem will be applied to each element of the grid in arbitrary motion, for domains with variable geometry.

(pde:ale-description:differential)=
## Differential problem

Rules for derivatives of composite functions allows to write the differential w.r.t. the variables associated with the points of a moving grid. A balance equation in convective form can be written as

$$\begin{aligned}
  \rho \dfrac{D \mathbf{u}}{D t} & = \rho \mathbf{f} + \nabla \cdot \mathbf{T} \\
  \rho \left[ \dfrac{\partial \mathbf{u}}{\partial t} + \vec{u} \cdot \nabla \mathbf{u} \right] & = \\
  \rho \left[ \left.\dfrac{\partial \mathbf{u}}{\partial t}\right|_{\vec{r}_b} + \left( \vec{u} - \vec{u}_b \right) \cdot \nabla \mathbf{u} \right] & = \\
\end{aligned}$$


