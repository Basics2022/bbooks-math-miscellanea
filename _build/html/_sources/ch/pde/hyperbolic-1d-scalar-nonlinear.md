(pde:hyperbolic:problems:1d-scalar-nonlinear)=
# Scalar non-linear equation

**todo list**

- When does a jump occur? I.e. when is the physical solution discontinuous? Have non physical jumps already been discussed?
- Boundary conditions for hyperbolic problems
- ...

(pde:hyperbolic:problems:scalar-nonlinear:examples)=
## Examples

(pde:hyperbolic:problems:scalar-nonlinear:examples:burgers)=
### Burgers's equation

(pde:hyperbolic:problems:scalar-nonlinear:examples:burgers:equations)=
#### Differential equation and integral balance

Burgers' differential equation reads

$$\begin{aligned}
  0
  & = \partial_t u + u \partial_x u =            && \text{(convective form)}   \\
  & = \partial_t u + \partial_x \frac{u^2}{2} =  && \text{(conservative form)} \\
  & = \partial_t u + \partial_x F(u) \ ,
\end{aligned}$$

being the flux $F(u) = \frac{u^2}{2}$, and it can be derived as the local counterpart of the integral balance equation, 

$$\begin{aligned}
  0
  & = \frac{d}{dt} \int_V u + \oint_{\partial V} n_x \frac{u^2}{2}  
    = \frac{d}{dt} \int_V u + \left. F(u(x)) \right|_{a}^{b} \ ,
\end{aligned}$$

for a control volume at rest $V = [a, b]$. For a control volume with arbitrary motion $v_t = [a_t, b_t]$ the integral balance equation reads

$$\begin{aligned}
  0
  & = \frac{d}{dt} \int_{v_t} u - \oint_{\partial v_t} \hat{\mathbf{n}} \cdot \mathbf{v}_b \, u + \oint_{\partial v_t} n_x F(u) = \\
  & = \frac{d}{dt} \int_{v_t} u - \oint_{\partial v_t} n_x v_{b,x} \, u + \oint_{\partial v_t} n_x F(u) = \\
  & = \frac{d}{dt} \int_{v_t} u + \left. \left[ F(u(x)) - v_{b,x} u(x) \right] \right|_{a}^{b} \ ,
\end{aligned}$$

having used Reynolds' transport theorem[^reynolds-transport], and the unit normal vector in the only space direction $n_x(x=a) = -1$ on the left extreme and $n_x(x=b) = 1$ on the right extreme of the domain $V = [a,b]$.

[^reynolds-transport]: For a generic volume $v_t$, $d_t \int_{v_t} f = \int_{v_t} \partial_t f + \oint_{\partial v_t} \hat{\mathbf{n}} \cdot \mathbf{v}_b \, f$. Thus, for a control volume at rest $V$, $d_t \int_V f = \int_V \partial_t f$. Comparing the two expressions, it immediately follows that $d_t \int_{v_t} f = d_t \int_{V \equiv v_t} f + \oint_{\partial v_t} \hat{\mathbf{n}} \cdot \mathbf{v}_b \, f$.

(pde:hyperbolic:problems:scalar-nonlinear:examples:burgers:jump)=
#### Jump condition

Jump condition immediately follows from the integral form of the balance equations for the arbitrary volume $v_t$.

$$[ F ] = v_{b,x} [ u ] \ .$$

For Burgers' equation, $F(u) = \frac{u^2}{2}$, and thus the jump relation becomes

$$
  \frac{u^2_2}{2} - \frac{u^2_1}{2} = v_{b,x} \left( u_2 - u_1 \right) \ ,
$$

and thus, except for the trivial condition $u_1 = u_2$ where no jump occurs,

$$v_{b,x} = \frac{1}{2} \left( u_2 + u_1 \right) \ ,$$

the velocity of the point where the discontinuity appears - the shock - is the average of the velocity $u$ on its sides.

**todo** *When does a jump occur? I.e. when is the physical solution discontinuous? Have non physical jumps already been discussed?*

(pde:hyperbolic:problems:scalar-nonlinear:examples:burgers:characteristics)=
#### Characteristics

Let $U(t) = u(X(t), t)$. Burgers' equation can be recast as[^characterstics-time-der]

[^characterstics-time-der]: Using derivation of composite functions, $d_t U(t) = d_t u(X(t), t) = \partial_t u + d_t X \partial_x u =$ $ \partial_t u|_{(x,t)=(X(t),t)} + \dot{X}(t) \partial_x u|_{(x,t)=(X(t),t)}$.

$$0 = d_t U - \dot{X} \partial_x u + u \partial_x u \ .$$

A characteristic line is defined as a curve for which the coefficient of the spatial partial differential equation is zero, i.e. $\dot{X}(t) = U(X(t),t)$. On these lines, the PDE becomes a ODE, so that it's somehow equivalent **todo** *be more precies* to the system of ODEs

$$\begin{cases}
  \dot{X}(t) = U(X(t), t) \\
  \dot{U}(t) = 0 \ .
\end{cases}$$

These equations need initial and boundary conditions. 

**todo** *Boundary conditions for hyperbolic problems*

Let $x_0$, $t_0$ a point in space and time where the solution is known, $u_0 = u(x_0, t_0)$. On the characteristic line originating from $x_0, t_0$, the velocity is constant in time as $\dot{U}(t) = 0$, and thus $U(t)_{X(t;x_0,t_0)} = u_0$. The characteristic line satisfying the first equation and the initial conditions is the line with equation

$$X(t; t_0,x_0, u_0) = u_0 ( t - t_0 ) + x_0 \ .$$

(pde:hyperbolic:problems:scalar-nonlinear:examples:burgers:riemann)=
#### Riemann problem

Riemann problem is defined as the PDE with a discontinuity in a piecewise constant initial conditons. For an unbounded domain $V = (-\infty, + \infty)$[^unbounded-domain]

[^unbounded-domain]: In an unbounded domain, there's no need to treat boundary conditions...**todo** *add link to boundary conditions for hyperbolic problems*.

$$u(x,0) = \left\{ \begin{aligned} u_1 && , \quad x < 0 \\ u_2 && , \quad x > 0\end{aligned} \right. $$

Two cases must be discussed here: $1)$ $u_1 < u_2$, $2)$ $u_1 > u_2$.

**Expansion fan, $u_1 < u_2$.** A self-similar solution exists between lines $r_1: \, x = u_1 t$ and $r_2: \, x = u_2 t$. Defining $\xi := \frac{x}{t}$, the solution becomes $u(x, t) = U\left( \xi(x,t) \right)$, so that

$$\begin{aligned} 
 & \partial_t U = \partial_t \xi U'(\xi) = - \frac{x}{t^2} U'(\xi) \\
 & \partial_x U = \partial_x \xi U'(\xi) =   \frac{1}{t  } U'(\xi) \ ,
\end{aligned}$$

so that Burgers' equation in the rarefaction fan becomes

$$0 = \partial_t u + u \partial_x u = \frac{1}{t} \left[ - \xi + U(\xi) \right] U'(\xi) \ .$$

Looking for a continuous solution blending the two states, the condition $U'(\xi) = 0$ is not feasible. Then,

$$U(\xi) = \xi \ ,$$

or

$$u(x,t) = \frac{x}{t} \quad , \quad \frac{x}{t} \in [ u_1 , u_2 ] \ .$$

The solution of the Riemann problem reads

$$u(x,t) = \left\{ \begin{aligned} 
  u_1         \quad & , \quad  \frac{x}{t} \le u_1 \\
  \frac{x}{t} \quad & , \quad  \frac{x}{t} \in [u_1, u_2] \\ 
  u_2         \quad & , \quad  \frac{x}{t} \ge u_2
\end{aligned} \right.$$


**Shock, $u_1 > u_2$.** Characteristic method fails at a shock originating from the origin. Characteristic lines originating from $x < 0$ have a slope $\dot{X}(t) = u_1$ larger than the slope of the characteristic lines originating from $x > 0$: characteristic lines collapses into the shock, that has velocity

$$\dot{s} = \frac{u_1 + u_2}{2} \ .$$

The solution of the Riemann problem reads

$$u(x,t) = \left\{ \begin{aligned} 
  u_1         \quad & , \quad  \frac{x}{t} < \dot{s} \\
  u_2         \quad & , \quad  \frac{x}{t} > \dot{s}
\end{aligned} \right.$$

(pde:hyperbolic:problems:scalar-nonlinear:examples:burgers:boundary-conditions)=
#### Boundary conditions

In order to have a well-defined hyperbolic problem, boundary conditions are **required** on the regions of the boundary **where the information enters the domain**. For a scalar problem, the local direction of the information is determined by the velocity of the local characteristic lines. For Burgers' equation, the direction of the local intormation is just the sign of the velocity of the characteristics, that is equal to the local velocity. Thus, boundary conditions are strictly needed on the left boundary $x = a$ if $u(a, t) > 0$ and on the right boundary $x = b$ if $u(b, t) < 0$.




