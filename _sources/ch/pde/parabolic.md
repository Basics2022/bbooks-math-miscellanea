(pde:parabolic)=
# Parabolic equations

(pde:parabolic:heat)=
## Heat equation

Heat equation for a scalar field $\phi(\vec{r},t)$ can be interpreted as the unsteady equation of a [Poisson equation](pde:elliptic:poisson),

$$\partial_t \phi - \nabla \cdot (\nu \nabla \phi) = f \qquad (\vec{r}, t) \in V \times [0, T] \ ,$$

with proper boundary and initial conditions, $\phi(\vec{r},0) = \phi_0(\vec{r})$. Common boundary conditions are the same as the one discussed for Poisson problem.

(pde:parabolic:heat:weak)=
### Weak formulation

For $\forall w \in \dots$ (functional space, recall some results about existence and uniqueness of the solution, Lax-Milgram theorem,...)

$$\begin{aligned}
  0
  &  = \int_V w \, \left\{ - \partial_t \phi + \nabla \cdot (\nu \nabla \phi) + f \right\} = \\
  &  = \oint_{\partial V} w \hat{n} \cdot (\nu \nabla \phi) + \int_V \left\{ - \partial_t \phi - \nu \nabla \vec{w} \cdot \nabla \phi  + w f \right\} = \\
\end{aligned}$$

Splitting boundary contribution as the sum from single contributions from different regions, and applying boundary conditions, setting $w = 0$ for $\vec{r} \in S_D$ (see the ways to prescribe essential boundary conditions),

$$\begin{aligned}
  0 = \int_{S_D} \underbrace{w}_{= 0} \hat{n} \cdot (\nu \nabla \phi) + \int_{S_N} w \underbrace{\hat{n} \cdot (\nu \nabla \phi)}_{ = h} + \int_{S_R} w \underbrace{ \hat{n} \cdot (\nu \nabla \phi)}_{ = k - \phi } + \int_V \left\{ - \partial_t \phi  - \nu \nabla \vec{w} \cdot \nabla \phi  + w f \right\} \ .
\end{aligned}$$

and rearranging the equation separating terms containing unknowns from known contributions,

$$\int_{V} w \partial_t \phi + \int_{V} \nu \nabla w \cdot \nabla \phi + \int_{S_R} w \phi = \int_{V} w f + \int_{S_N} w h + \int_{S_R} w k \qquad \forall w \in \dots \ ,$$

and $\phi = g$, for $\vec{r} \in S_D$.



