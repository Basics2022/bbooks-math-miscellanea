(pde:hyperbolic:intro)=
# Hyperbolic problems and conservation laws

**todo**
- In fluid dynamics: no viscosity, no heat conduction
- In this limit, the equation may produce non-physical equations, i.e. solutions that are not the limit of the solution of the full problem in the limit of $\mathbf{F}^d(\nabla \mathbf{u}) \rightarrow \mathbf{0}$
- How many equations in how many variables?
- Linear diffusion flux $\mathbf{F}^d = \dots$
- Entropy condition, to select the physical solution from all the possible solutions

(pde:hyperbolic:intro:integral)=
## Integral equations

Many laws can be written as integral balance equations for a material volume $V_t$,

$$\begin{aligned}
  & \dfrac{d}{dt} \int_{V_t} \mathbf{u} + \oint_{\partial V_t} \hat{\mathbf{n}} \cdot \mathbf{F}(\mathbf{u}, \nabla \mathbf{u}) = \int_{V_t} \mathbf{s} \\
  & \dfrac{d}{dt} \int_{V_t} u_i + \oint_{\partial V_t} n_j \, F_{ji} = \int_{V_t} s_i \\
\end{aligned}$$

or for generic volume $v_t$, using [Reynolds' transport theorem](tensor:calculus:time-derivative-of-integrals:volume-density),

$$\dfrac{d}{dt} \int_{v_t} \mathbf{u} + \oint_{\partial v_t} \mathbf{u} \left( \mathbf{v} - \mathbf{v}_b \right) \cdot \hat{\mathbf{n}} + \oint_{\partial v_t} \hat{\mathbf{n}} \cdot \mathbf{F}(\mathbf{u}, \nabla \mathbf{u}) = \int_{v_t} \mathbf{s} \ ,$$

being $\mathbf{v}$ the velocity of the continuous medium and $\mathbf{v}_b$ the velocity of the boundary $\partial v_t$.

The flux can be often written as a sum of a *conservative part* and a *diffusion part* as 

$$\begin{aligned}
  \mathbf{F}(\mathbf{u}, \nabla \mathbf{u})
  & = \mathbf{F}(\mathbf{u}) + \mathbf{F}^d(\nabla \mathbf{u}) \ ,
\end{aligned}$$

with slight abuse of notation in writing the conservative flux with the same letter as the full flux.

Under some conditions, the diffusion part goes to zero. 

(pde:hyperbolic:intro:jump)=
## Jump relations

Collapsing the volume $v_t$ on a surface, volume terms vanish faster than the surface terms. Jump conditions follow from the arbitrariety of this surface

$$\begin{aligned}
  \mathbf{0}
  & = \hat{\mathbf{n}}_1 \cdot \left[ (\mathbf{v}_1-\mathbf{v}_b) \mathbf{u} + \mathbf{F}_1 \right] 
    + \hat{\mathbf{n}}_2 \cdot \left[ (\mathbf{v}_2-\mathbf{v}_b) \mathbf{u} + \mathbf{F}_2 \right] = \\
  & = \hat{\mathbf{n}}   \cdot \left[ (\mathbf{v}-\mathbf{v}_b) \mathbf{u} + \mathbf{F} \right] = \\
  & = \left[ v_n^{rel} \mathbf{u} + \mathbf{F}_n \right] \ .
\end{aligned}$$


(pde:hyperbolic:intro:differential)=
## Differential equations

If the functions are differentiable, with divergence theorem and exploiting the arbitrariety of the volume $v_t$

$$\begin{aligned}
  \partial_t u_i + \partial_j F_{ji} & = s_i \\
  \partial_t \mathbf{u} + \nabla \cdot \mathbf{F} & = \mathbf{s} \ .
\end{aligned}$$

