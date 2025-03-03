(pde:ns)=
# Navier-Stokes equations

Incompressible Navier-Stokes equations read

$$\begin{cases}
  \rho \partial_t \vec{u} + \rho \left( \vec{u} \cdot \nabla \right) \vec{u} - \mu \nabla^2 \vec{u} + \nabla P = \rho \vec{g} \\
  \nabla \cdot \vec{u} = 0 \ . 
\end{cases}$$

Mass balance equation is replaced by the incompressiblity kinematic constraint, $\nabla \cdot \vec{u} = 0$: this constraint is not dynamic, as time derivative of density does not appear in the equation. With the incompressibility constraint, mass equation tells us that material particles keep their density constant,

$$0 = \underbrace{\partial_t \rho + \vec{u} \cdot \nabla \rho}_{=\frac{D \vec{\rho}}{D t}} + \rho \underbrace{\nabla \cdot \vec{u}}_{=0} = \frac{D \rho}{D t} \ , $$

whose solution can be written using material coordinates $\vec{r}_0$ as $\rho(\vec{r}(\vec{r}_0,t), t) = \rho_0(\vec{r}_0, t)$.

## Incompressibility constraint
Incompressibility constraint makes thermodynamic fade, while pressure field is replaced by/contains the contribution of a Lagrangian multiplier related to the incompressiblity constraint.

### Wave-vector transformed space
Transforming the fields from physical space to the wave-vector space $\widetilde{u}(\vec{\kappa}, t) = \mathscr{F}\left\{ \vec{u}(\vec{r},t) \right\}$, Navier-Stokes equations for incompressible fluids with uniform and constant density $\rho(\vec{r},t) = \rho$ becomes

$$\begin{cases}
  \rho \partial_t \widetilde{u} + \mathscr{F}\left\{ \left( \vec{u} \cdot \nabla \right) \vec{u} \right\} + \mu |\vec{\kappa}|^2 \widetilde{u} + i \vec{k} \widetilde{P} = \rho \widetilde{g} \\
  i \vec{\kappa} \cdot \widetilde{u} = 0 \ .
\end{cases}$$

Taking the divergence of the momentum balance equation, i.e. taking the scalar product with $i \vec{\kappa}$ in the transformed space, and using the incompressibility constraint to set $i \vec{\kappa} \cdot \widetilde{u} = 0$,

$$i \vec{\kappa} \cdot \mathscr{F}\left\{ (\vec{u} \cdot \nabla ) \vec{u} \right\} - |\vec{\kappa}|^2 \widetilde{P} = i \vec{\kappa} \cdot \rho \widetilde{g} \ ,$$

so that the transformed pressure field becomes

$$\widetilde{P} = \frac{i \vec{\kappa}}{|\vec{\kappa}|^2} \cdot \mathscr{F} \left\{ \left( \vec{u} \cdot \nabla \right) \vec{u} - \rho \vec{g} \right\} \ ,$$ 

Replacing this expression in the transformed Navier-Stokes equations, the meaning of the pressure field as a Lagrange multiplier associated with incompressibility constraint becomes clear, 

$$\rho \partial_t \widetilde{u} + \mu |\vec{\kappa}|^2 \widetilde{u} = \left[ 1 - \frac{\vec{\kappa} \vec{\kappa}}{|\vec{\kappa}|^2} \right] \cdot \mathscr{F}\left\{ - (\vec{u} \cdot \nabla) \vec{u} + \rho \widetilde{g} \right\}$$

as the orthogonal projector $[ 1 - \frac{\vec{\kappa} \vec{\kappa}}{|\vec{\kappa}|^2}]$ onto the space of divergence-free functions acts on the non-linear and forcing terms.

## Weak formulation of the problem
<!--
  & = \int_{V} \vec{w} \cdot \left[ \rho \partial_t \vec{u} + \rho ( \vec{u} \cdot \nabla ) \vec{u} - 2 \mu \nabla \cdot \left( \frac{1}{2} \left(  \nabla \vec{u} + \nabla^T \vec{u} \right) \right) + \nabla P - \rho \vec{g} \right] - \int_{V} v \nabla \cdot \vec{u} = \\
-->

$$\begin{aligned}
  0
  & = \int_{V} \vec{w} \cdot \left[ \rho \partial_t \vec{u} + \rho ( \vec{u} \cdot \nabla ) \vec{u} - 2 \mu \nabla \cdot \mathbb{D}(\vec{u}) + \nabla P - \rho \vec{g} \right] - \int_{V} v \nabla \cdot \vec{u} = \\
  & = \int_{V} \vec{w} \cdot \left[ \rho \partial_t \vec{u} + \rho ( \vec{u} \cdot \nabla ) \vec{u} \right] + \int_V 2 \mu \nabla \vec{w} : \mathbb{D} - \int_V \nabla \cdot \vec{w} P - \int_V \rho \vec{g} - \int_{V} v \nabla \cdot \vec{u} - \int_{\partial V} \hat{n} \cdot \left( \mathbb{S} - P \mathbb{I} \right) \cdot \vec{w} \ ,
\end{aligned}$$

## Non-linear term

Different ways to treat the non-linear term:

- Semi-linear approximation of the non-linear term

   $$( \vec{u}(\vec{r}, t^n) \cdot \nabla ) \vec{u}(\vec{r}, t^n) \sim ( \vec{u}^*(\vec{r}, t^n) \cdot \nabla ) \vec{u}(\vec{r}, t^n) \ , $$

   with $\vec{u}^*(\vec{r}, t^n)$ an approximation of $\vec{u}(\vec{r},t^n)$ involving values of the velocity field at previous time-steps, as an example

   $$\vec{u}^*(\vec{r}, t^n) = 
   \begin{cases}
      \vec{u}(\vec{r}, t^{n-1}) & \text{$1^{st}$-order} \\
      2 \vec{u}(\vec{r}, t^{n-1}) - \vec{u}(\vec{r}, t^{n-2}) & \text{$2^{nd}$-order} \\
   \end{cases}$$
