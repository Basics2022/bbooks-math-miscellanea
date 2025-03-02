(pde:elliptic)=
# Elliptic equations

(pde:elliptic:poisson)=
## Poisson equation

Given the volume density source $f(\vec{r})$ and the diffusivity $\nu(\vec{r})$, Poisson equation for the scalar field $\phi(\vec{r})$ reads

$$- \nabla \cdot ( \nu \nabla \phi) = f \qquad \vec{r} \in V$$

with proper boundary conditions on $\partial V$. As an example, tipical boundary conditions are:

$$\begin{aligned}
  & \phi(\vec{r}) = g(\vec{r}) && \vec{r} \in S_D && \text{esserntial - Dirichlet b.c.}  \\
  & \nu \hat{n} \cdot \nabla \phi(\vec{r}) = h(\vec{r}) && \vec{r} \in S_N && \text{natural - Neumann b.c.}  \\
  & a \phi(\vec{r}) + \nu \hat{n} \cdot \nabla \phi(\vec{r}) = b(\vec{r}) && \vec{r} \in S_R && \text{Robin b.c.} \\
\end{aligned}$$

(pde:elliptic:poisson:weak)=
### Weak formulation

For $\forall w \in \dots$ (functional space, recall some results about existence and uniqueness of the solution, Lax-Milgram theorem,...)

$$\begin{aligned}
  0
  &  = \int_V w \, \left\{ \nabla \cdot (\nu \nabla \phi) + f \right\} = \\
  &  = \oint_{\partial V} w \hat{n} \cdot (\nu \nabla \phi) + \int_V \left\{ - \nu \nabla \vec{w} \cdot \nabla \phi  + w f \right\} = \\
\end{aligned}$$

Splitting boundary contribution as the sum from single contributions from different regions, and applying boundary conditions, setting $w = 0$ for $\vec{r} \in S_D$ (see the ways to prescribe essential boundary conditions),

$$\begin{aligned}
  0 = \int_{S_D} \underbrace{w}_{= 0} \hat{n} \cdot (\nu \nabla \phi) + \int_{S_N} w \underbrace{\hat{n} \cdot (\nu \nabla \phi)}_{ = h} + \int_{S_R} w \underbrace{ \hat{n} \cdot (\nu \nabla \phi)}_{ = b - a \phi } + \int_V \left\{ - \nu \nabla \vec{w} \cdot \nabla \phi  + w f \right\} \ .
\end{aligned}$$

and rearranging the equation separating terms containing unknowns from known contributions,

$$\int_{V} \nu \nabla w \cdot \nabla \phi + \int_{S_R} w a \phi = \int_{V} w f + \int_{S_N} w h + \int_{S_R} w b \qquad \forall w \in \dots \ ,$$

and $\phi = g$, for $\vec{r} \in S_D$.


```{dropdown} Different ways to prescribe essential boundary conditions

**Strong formulation.**

**Using Lagrance multiplier - weak formulation of essential boundary conditions.** Adding a the essential boundary condition as a constraint with Lagrange multipliers in the weak formulation of the problem,

$$\dots + \int_{S_D} w_D ( \phi - g ) \ ,$$

...


```
