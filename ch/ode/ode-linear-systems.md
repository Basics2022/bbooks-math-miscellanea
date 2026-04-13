(ode:linear:miscellanea)=
# Linear systems

(ode:linear:miscellanea:general-solution)=
## General solution

The general solution of the initial value problem

$$\begin{aligned}
  & \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
  & \mathbf{x}(t_0) = \mathbf{x}_0
\end{aligned}$$ (eq:ode:system:linear)

with no impulsive forcing in $t_0$ reads

$$
   \mathbf{x}(t) & = \boldsymbol\Phi(t,t_0) \mathbf{x_0} + \int_{\tau=t_0}^{t}  \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau \\
$$

with 

$$\begin{cases}
  \frac{\partial}{\partial t} \boldsymbol\Phi(t,t_0) = \mathbf{A}(t) \boldsymbol\Phi(t,t_0) \\
  \boldsymbol\Phi(t,t_0) = \mathbf{I} \ ,
\end{cases}$$

or alternatively, $\partial_{t_0} \boldsymbol\Phi(t,t_0) = \boldsymbol\Phi(t,t_0) \mathbf{A}(t_0)$.



```{dropdown} General solution - details
:open:

Pre-multiplication of equation {eq}`eq:ode:system:linear` by $\boldsymbol\phi(t)$, with $\dot{\boldsymbol\phi}(t) = - \boldsymbol\phi(t) \mathbf{A}(t)$ gives

$$\begin{aligned}
  \boldsymbol\phi(t) \dot{\mathbf{x}} - \boldsymbol\phi(t) \mathbf{A} \mathbf{x} & = \boldsymbol\phi(t) \mathbf{B} \mathbf{u} \\
  \boldsymbol\phi(t) \dot{\mathbf{x}} + \dot{\boldsymbol\phi}(t) \mathbf{x} & = \boldsymbol\phi(t) \mathbf{B} \mathbf{u} \\
  \frac{d}{dt} \left( \boldsymbol\phi(t) \mathbf{x} \right) & = \boldsymbol\phi(t) \mathbf{B} \mathbf{u} \\
\end{aligned}$$

and integration - without impulsive forces in $t = t_0$, that would cause jump in initial conditions, see [section about impulsive force](ode:lti:impulsive-force) - 

$$\begin{aligned}
  \boldsymbol\phi(t) \mathbf{x} - \boldsymbol\phi(t_0) \mathbf{x_0} & = \int_{\tau=t_0}^{t} \boldsymbol\phi(\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau \\
\end{aligned}$$

and thus

$$\begin{aligned}
   \mathbf{x}(t) & = \boldsymbol\phi^{-1}(t) \boldsymbol\phi(t_0) \mathbf{x_0} + \int_{\tau=t_0}^{t}  \boldsymbol\phi^{-1}(t)\boldsymbol\phi(\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau \\
\end{aligned}$$

or, defining $\boldsymbol\Phi(a,b) := \boldsymbol\phi^{-1}(a) \boldsymbol\phi(b)$,

$$\begin{aligned}
   \mathbf{x}(t) & = \boldsymbol\Phi(t,t_0) \mathbf{x_0} + \int_{\tau=t_0}^{t}  \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau \\
\end{aligned}$$

with $\boldsymbol\Phi(t,t_0)$ satisfying the initial value problem

$$\begin{cases}
  \frac{\partial}{\partial t} \boldsymbol\Phi(t,t_0) = \mathbf{A}(t) \boldsymbol\Phi(t,t_0) \\
  \boldsymbol\Phi(t,t_0) = \mathbf{I} \ .
\end{cases}$$

The initial conditions follows from the solution, as the integral identically vanishes as $t \rightarrow t_0$ if there's no impulsive force in $t_0$. The matrix differential equation follows from the definition of the function $\boldsymbol\Phi(t,\tau)$ in terms of $\boldsymbol\phi(t)$ and from the time derivative of the inverse of a matrix

$$\frac{d}{dt} \boldsymbol\phi^{-1} = - \boldsymbol\phi^{-1} \dot{\boldsymbol\phi} \boldsymbol\phi^{-1} \ ,$$

as $\mathbf{0} = \frac{d}{dt} \mathbf{I} = \frac{d}{dt} \left( \boldsymbol\phi^{-1} \boldsymbol\phi \right)$.

Time derivative of $\boldsymbol\Phi(t,\tau)$ w.r.t. the first argument reads

$$\begin{aligned}
  \partial_t \boldsymbol\Phi(t,\tau) 
  & = \partial_t \left( \boldsymbol\phi^{-1}(t) \boldsymbol\phi(\tau) \right) = \\
  & = \frac{d}{dt} \boldsymbol\phi^{-1}(t) \, \boldsymbol\phi(\tau) = \\
  & = - \boldsymbol\phi^{-1}(t) \dot{\boldsymbol\phi}(t) \boldsymbol\phi^{-1}(t) \, \boldsymbol\phi(\tau) = \\
  & =   \underbrace{\boldsymbol\phi^{-1}(t) \boldsymbol\phi(t)}_{=\mathbf{I}} \mathbf{A}(t) \underbrace{\boldsymbol\phi^{-1}(t)  \, \boldsymbol\phi(\tau)}_{\boldsymbol\Phi(t,\tau)} = \\
  & = \mathbf{A}(t) \boldsymbol\Phi(t, \tau) \ .
\end{aligned}$$

Derivative w.r.t. the second argument simply reads

$$\begin{aligned}
  \partial_{\tau} \boldsymbol\Phi(t,\tau) 
  & = \boldsymbol\phi^{-1}(t) \frac{d}{d\tau} \boldsymbol\phi(\tau) = \\
  & = \boldsymbol\phi^{-1}(t) \boldsymbol\phi(\tau) \mathbf{A}(\tau) = \\
  & = \boldsymbol\Phi(t,\tau) \mathbf{A}(\tau) \ .
\end{aligned}$$



```

##  

