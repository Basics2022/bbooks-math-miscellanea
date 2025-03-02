(pde:nc)=
# Navier-Cauchy equations

Navier-Cauchy equations are the differential balance equation of the momentum of an elastic isotropic medium in the regime of small strain and displacement,

$$\rho_0 \partial_{tt} \vec{s} = \rho_0 \vec{g} + \nabla \cdot \symbf{\sigma} \ . $$

Stress tensor for an isotropic medium reads

$$\begin{aligned}
  \symbf{\sigma}
   & = 2 \mu \symbf{\varepsilon} + \lambda \, \text{tr} \left( \symbf{\varepsilon} \right) \mathbb{I} = \\
   & = \left( 2 \mu \symbf{\varepsilon} - \frac{2}{3} \mu \, \text{tr}(\symbf{\varepsilon}) \mathbb{I} \right) + \left( \lambda + \frac{2}{3} \mu \right) \, \text{tr} \left( \symbf{\varepsilon} \right) \mathbb{I} \ ,
\end{aligned}$$

with the small strain tensor

$$\symbf{\varepsilon} = \frac{1}{2} \left( \nabla \vec{s} + \nabla^T \vec{s} \right) \ .$$

Essential, natural and Robin boundary conditions read

$$\begin{aligned}
  & \vec{s} = \overline{\vec{s}} && \vec{r} \in S_D && \text{esserntial - Dirichlet b.c.}  \\
  & \hat{n} \cdot \symbf{\sigma} = \overline{\vec{t}}_n && \vec{r} \in S_N && \text{natural - Neumann b.c.}  \\
  & a \vec{s} + \hat{n} \cdot \symbf{\sigma} = \vec{b} && \vec{r} \in S_R && \text{Robin b.c.} \\
\end{aligned}$$

## Weak formulation

For $\forall \vec{w} \in \dots$

$$\begin{aligned}
  0
  & = - \int_V \rho \vec{w} \cdot \partial_{tt} \vec{s} + \int_V \rho_0 \vec{w} \cdot \vec{g} + \int_{V} \vec{w} \cdot \nabla \cdot \symbf{\sigma} = \\ 
  & = - \int_V \rho \vec{w} \cdot \partial_{tt} \vec{s} + \int_V \rho_0 \vec{w} \cdot \vec{g} + \int_{\partial V} \hat{n} \cdot \symbf{\sigma} \cdot \vec{w} - \int_{V} \nabla \vec{w} : \symbf{\sigma} 
\end{aligned}$$

The volume integral containing the stress tensor can be written either as

$$\begin{aligned}
  \int_V \nabla \vec{w} : \symbf{\sigma} 
  & = \int_V w_{i/j} \left[ \mu \left( s_{i/j} + s_{j/i} \right) + \lambda s_{k/k} \delta_{ij} \right] = \\
  & = \int_V \mu w_{i/j} \left( s_{i/j} + s_{j/i} \right) + \int_V \lambda w_{j/j} s_{k/k} 
\end{aligned}$$

or

$$\begin{aligned}
  \int_V \frac{1}{2} \left( \nabla \vec{w} + \nabla^T \vec{w} \right) : \symbf{\sigma} 
  & = \int_V \frac{1}{2} \left( w_{i/j} + w_{j/i} \right) \left[ \mu \left( s_{i/j} + s_{j/i} \right) + \lambda s_{k/k} \delta_{ij} \right] = \\
  & = \int_V \frac{\mu}{2} \left( w_{i/j} + w_{j/i} \right) \left( s_{i/j} + s_{j/i} \right) + \int_{V} \lambda w_{j/j} s_{k/k} 
\end{aligned}$$

The weak formulation of the Navier-Cauchy equations reads

$$\int_V \rho_0 \vec{w} \cdot \partial_{tt} \vec{s} + \int_{V} 2 \mu \frac{\nabla \vec{w} + \nabla^T \vec{w}}{2} : \frac{\nabla \vec{s} + \nabla^T \vec{s}}{2} + \int_{V} \lambda \nabla \cdot \vec{w} \, \nabla \cdot \vec{s} + \int_{S_R} \vec{w} \cdot a \vec{s} = \int_{V} \rho_0 \vec{w} \cdot \vec{g} + \int_{S_N} \vec{w} \cdot \overline{\vec{t}}_n + \int_{S_R} \vec{w} \cdot \vec{b} \ ,$$

for $\forall \vec{w} \in \dots$, and with $\vec{s} = \overline{\vec{s}}$ for $\vec{r} \in S_D$.

