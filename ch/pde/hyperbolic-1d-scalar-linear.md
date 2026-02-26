(pde:hyperbolic:problems:1d-scalar-linear)=
# Scalar linear equation

**Differential equation.**

$$\begin{aligned}
  r
  & = \partial_t u + a \partial_x u      && \text{  convective form}   \\
  & = \partial_t u + \partial_x ( a u )  && \text{conservative form}
\end{aligned}$$

**Integral equation.** On a control volume $V$ at rest

$$0 = \dfrac{d}{dt} \int_V u + \oint_{\partial V} n_x a u \ .$$

Integral equation in an arbitrary domain $v_t$ can be derived using [Reynolds' transport theorem](tensor:calculus:time-derivative-of-integrals:volume-density).

**Method of characteristics.** Let $U(t) = u(X(t), t)$. From derivative of composite functions,

$$d_t U(t) = \partial_t u|_{X(t),t} + \dot{X}(t) \partial_x u|_{X(t),t} \ ,$$

and thus the PDE can be recast as a system of two ODEs

$$\begin{cases}
  \dot{X}(t) = a \\
  \dot{U}(t) = r
\end{cases}$$

...
