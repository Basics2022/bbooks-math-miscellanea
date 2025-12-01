(complex:laplace:applications)=
# Applications of Laplace Transform

## Ordinary differential equations

Exploiting the properties of transforming derivation into product by the complex variable $s$, Laplace transform can be a useful tool in solving [Ordinary differential equations](ode).

Linear ODEs are treated in details in the section about [Linear Time-Invariant Systems](ode:lti).

### First-order linear differential equation with constant coefficients

A Cauchy problem governed by a first-order linear differential equation with constant coefficients reads

$$\begin{cases}
  \dot{u} + a u = f(t)  && \text{for $t > 0$} \\
  u(0^-) = u_0 \ .
\end{cases}$$

**Comments.** 1) For linear differential equations with constant coefficients, a time shift is always possible to set initial conditions in $t_0 = 0$; 2) dealing with **impulsive forces** (more on this in [LTI systems: impulsive forces](ode:lti:impulsive-force)), some attention needs to be paid to the time of initial conditions: if impulsive forces at $t = 0$ may exist, initial conditions need to be set at $t=0^-$; the effect of the impulsive force is equivalent to a jump in initial conditions from $t=0^-$ and $t=0^+$.

```{dropdown} General solution in time domain

Multiplying the ODE by $e^{a t}$,

$$e^{a t} f(t) = e^{a t} \left( \dot{u} + a u \right) = \dfrac{d}{dt} \left( e^{at} u(t) \right)$$

and integrating from $0^-$ to a generic time $t$ &mdash; after changing the dummy integration variable from $\tau$ to $t$ &mdash;

$$e^{at} u(t) - u(0^-) = \int_{\tau = 0^-}^{t} e^{a \tau} f(\tau) d \tau \ ,$$

and thus

$$u(t) = e^{-at}  u(0^-) + \int_{\tau = 0^-}^{t} e^{-a(t- \tau)} f(\tau) d \tau \ .$$

```

The solution of the problem can be also computed using Laplace transform:
1. transforming the problem from time to Laplace domain: the differential problem with unknown $u(t)$ in time is transformed into an algebraic problem $\hat{u}(s)$. Using Laplace **transform of the time derivative**

  $$s \hat{u}(s) + u_0 + a \hat{u}(s) = \hat{f}(s) \ ,$$

2. solving the algebraic problem in Laplace domain for $\hat{u}(s)$

  $$\hat{u}(s) = \dfrac{1}{s + a} u_0 + \dfrac{1}{s + a} f(s) \ .$$

3. transforming back the solution in time domain, $u(t) = \mathscr{L}^{-1}\{ \hat{u}(s) \}$,

   $$\begin{aligned}
     u(t) & = \mathscr{L}^{-1}\{ \hat{u}(s) \} (t) = \\
          & = \mathscr{L}^{-1} \left\{ \dfrac{u_0}{s + a} \right\} +  \mathscr{L}^{-1} \left\{ \dfrac{1}{s + a} \hat{f}(s) \right\} = \\
          & = e^{-at} u_0 + \int_{0^-}^{t} e^{-a(t-\tau)} f(\tau) d \tau \ ,
   \end{aligned}$$

   having used the inverse transform of the exponential $\mathscr{L}\{e^{ct}\} = \int_{t=0^-}^{+\infty} e^{ct} e^{-st} \, dt = \frac{1}{s-c}$, and the inverse transform of the convolution

   $$\hat{f}(s) \hat{g}(s) = \mathscr{L}\{ f(t) \ast g(t) \}(s) = \int_{t=0^-}^{+\infty} \left\{ \int_{\tau=0^-}^{t} f(\tau) g(t-\tau) d \tau \right\} e^{-st} dt \ .$$

