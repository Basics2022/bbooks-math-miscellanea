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

```{dropdown} Numerical methods
:open:

1-dimensional Poisson equation:
* [Finite Element Methods](pde:fem:poisson-1d)
* [Finite Volume Methods](pde:fvm:poisson-1d)
* *Finite Difference Methods*
* *Boundary Element Methods*
* *Spectral Methods* and *Spectral Element Methods*

```

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

(pde:elliptic:poisson:weaki:uniqueness)=
### Existence and uniqueness

Assuming two solutions $u_1(\mathbf{r})$, $u_2(\mathbf{r})$ exist for the Poisson problem

$$\begin{cases}
  - \nabla \cdot ( \nu \nabla u ) = f  \qquad \mathbf{r} \in V \\
  u|_{S_D} = g \\
  \nu \hat{n} \cdot \nabla u|_{S_N} = h
\end{cases}$$

Their difference $\delta u (\mathbf{r}) := u_2(\mathbf{r}) - u_1(\mathbf{r})$ then satisfies the homogeneous problem

$$\begin{cases}
  - \nabla \cdot ( \nu \nabla \delta u ) = 0  \qquad \mathbf{r} \in V \\
  \delta u|_{S_D} = 0 \\
  \nu \hat{n} \cdot \nabla \delta u|_{S_N} = 0
\end{cases}$$

The norm of the gradient of the difference of the solution reads

$$\begin{aligned}
  \int_{V} \nu |\nabla \delta u|^2
  & = \int_{V} \nu \nabla \delta u \cdot \nabla \delta u = \\
  & = \int_{V} \nabla \cdot \left( \delta u \, \nu \nabla \delta u \right) - \int_{V} \delta u \, \underbrace{\nabla \cdot ( \nu \nabla \delta u )}_{ = 0 } = \\
  & = \oint_{\partial V} \delta u \, \nu \hat{n} \cdot \nabla \delta u = \\
  & = \int_{S_D} \underbrace{ \delta u}_{ \delta u|_{S_D} = 0} \nu \hat{n} \cdot \nabla \delta u + \int_{S_N} \delta u \underbrace{\nu \hat{n} \cdot \nabla \delta u}_{\nu \hat{n} \cdot \nabla \delta u|_{S_N} = 0} = \\
  & = 0 \ .
\end{aligned}$$

**If** $\nu(\mathbf{r}) > 0$ for $\forall \mathbf{r} \in V$[^diffusion-coeff], it follows that

$$\nabla \delta u = \nabla (u_2 - u_1) = 0 \ ,$$

and thus the two solutions differs at most by an additive constant,

$$u_2(\mathbf{r}) - u_1(\mathbf{r}) = c \ .$$

**If** the Dirichlet boundary has non-null dimension, it forces the value of the functions to coincide on that boundary, $u_2(\mathbf{r}) = u_1(\mathbf{r})$ on $S_D$, and thus sets the value  of the additive constant $c$ to be zero, $c = 0$, and 

$$u_2(\mathbf{r}) = u_1(\mathbf{r}) \ ,$$

thus proving the uniqueness of the solution of the Poisson problem, with non-negative diffusion coefficient and non-zero dimension of Dirichlet boundary.

[^diffusion-coeff]: As an example, this condition appears in physical systems with non-zero and positive diffusion coefficients in diffusion problems, like thermal conduction or specie diffusion via Fick's law.

