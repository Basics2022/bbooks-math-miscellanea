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
$$ (eq:ode:system:linear:sol)

with 

$$\begin{cases}
  \frac{\partial}{\partial t} \boldsymbol\Phi(t,t_0) = \mathbf{A}(t) \boldsymbol\Phi(t,t_0) \\
  \boldsymbol\Phi(t,t_0) = \mathbf{I} \ ,
\end{cases}$$

or alternatively, $\partial_{t_0} \boldsymbol\Phi(t,t_0) = \boldsymbol\Phi(t,t_0) \mathbf{A}(t_0)$.



```{dropdown} General solution - details

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

(ode:linear:miscellanea:stochastic-response)=
## Stochastic response

(ode:linear:miscellanea:stochastic-response:correlation-matrix)=
### Correlation matrix

Using the general expression of the solution {eq}`eq:ode:system:linear:sol` of the linear system {eq}`eq:ode:system:linear`, the following relation holds for the correlation $\mathbf{R}_{\mathbf{x}\mathbf{x}}(t,\tau) := \mathbb{E}[ \mathbf{x}(t) \mathbf{x}^*(\tau) ]$,

$$\mathbf{R}_{\mathbf{x}\mathbf{x}}(t, \tau) = \boldsymbol\Phi(t,t_0) \mathbf{P}_0 \boldsymbol\Phi^*(t,t_0) + \int_{\lambda=t_0}^{t} \int_{\chi=t_0}^{\tau}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{R}_{\mathbf{u}\mathbf{u}}(\lambda, \chi) \mathbf{B}^*(\chi) \boldsymbol\Phi^*(\tau,\chi)  d \lambda \, d \chi \ ,$$

or for $\mathbf{P}_{\mathbf{x}\mathbf{x}}(t) := \mathbf{R}_{\mathbf{x} \mathbf{x}}(t,t)$

$$\mathbf{P}_{\mathbf{x}\mathbf{x}}(t) = \boldsymbol\Phi(t,t_0) \mathbf{P}_0 \boldsymbol\Phi^*(t,t_0) + \int_{\lambda=t_0}^{t} \int_{\chi=t_0}^{t}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{R}_{\mathbf{u}\mathbf{u}}(\lambda, \chi) \mathbf{B}^*(\chi) \boldsymbol\Phi^*(t,\chi)  d \lambda \, d \chi \ .$$

```{dropdown} Details

$$\begin{aligned}
  \mathbf{R}_{\mathbf{x} \mathbf{x}}(t, \tau) 
  & = \mathbb{E}\left[ \mathbf{x}(t) \mathbf{x}^*(\tau) \right] = \\
  & = \mathbb{E} \left[ \boldsymbol\Phi(t,t_0) \mathbf{x_0} \mathbf{x_0}^* \boldsymbol\Phi^*(t,t_0) \right] + \\
  & + \mathbb{E}\left[ \int_{\lambda=t_0}^{t}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{u}(\lambda) d \lambda \, \mathbf{x_0}^* \boldsymbol\Phi^*(t,t_0) \right] + \\
  & + \mathbb{E}\left[ \boldsymbol\Phi(t,t_0) \mathbf{x_0} \int_{\lambda=t_0}^{t} \mathbf{u}^*(\lambda) \mathbf{B}^*(\lambda)  \boldsymbol\Phi^*(t,\lambda) d\lambda \right] + \\
  & + \mathbb{E}\left[ \int_{\lambda=t_0}^{t}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{u}(\lambda) d \lambda \left( \int_{\chi=t_0}^{\tau}  \boldsymbol\Phi(\tau,\chi) \mathbf{B}(\chi) \mathbf{u}(\chi) d \chi \right)^* \right] \ ,
\end{aligned}$$

and applying the expectation opearator only on stochastic functions,

$$\begin{aligned}
  \mathbf{R}_{\mathbf{x} \mathbf{x}}(t, \tau) 
  & = \boldsymbol\Phi(t,t_0) \mathbb{E} \left[  \mathbf{x_0} \mathbf{x_0}^* \right] \boldsymbol\Phi^*(t,t_0) + \\
  & + \int_{\lambda=t_0}^{t}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbb{E} \left[ \mathbf{u}(\lambda) \mathbf{x}^*_0 \right] d \lambda \boldsymbol\Phi^*(t,t_0) + \\
  & + \boldsymbol\Phi(t,t_0) \int_{\lambda=t_0}^{t} \mathbb{E}\left[ \mathbf{x_0} \mathbf{u}^*(\lambda) \right] \mathbf{B}^*(\lambda)  \boldsymbol\Phi^*(t,\lambda) d\lambda  + \\
  & + \int_{\lambda=t_0}^{t} \int_{\chi=t_0}^{\tau}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbb{E}\left[ \mathbf{u}(\lambda) \mathbf{u}^*(\chi) \right]  \mathbf{B}^*(\chi) \boldsymbol\Phi^*(\tau,\chi)  d \lambda \, d \chi \ .
\end{aligned}$$

Assuming uncorrelated input noise and uncertainty on the initial conditions, $\mathbb{E}[ \mathbf{u}(t) \mathbf{x}^*_0 ] = \mathbf{0}$, and thus

$$\mathbf{R}_{\mathbf{x}\mathbf{x}}(t, \tau) = \boldsymbol\Phi(t,t_0) \mathbf{P}_0 \boldsymbol\Phi^*(t,t_0) + \int_{\lambda=t_0}^{t} \int_{\chi=t_0}^{\tau}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{R}_{\mathbf{u}\mathbf{u}}(\lambda, \chi) \mathbf{B}^*(\chi) \boldsymbol\Phi^*(\tau,\chi)  d \lambda \, d \chi \ ,$$

with the definition

$$\mathbf{P}_{\mathbf{x}\mathbf{x}}(t) := \mathbf{R}_{\mathbf{x}\mathbf{x}}(t,t) \ .$$

```

If the input is a white noise, $\mathbf{R}_{\mathbf{u} \mathbf{u}}(t,\tau) = \mathbf{U}(t) \delta(t - \tau)$,

$$\mathbf{P}_{\mathbf{x}\mathbf{x}}(t) = \boldsymbol\Phi(t,t_0) \mathbf{P}_0 \boldsymbol\Phi^*(t,t_0) + \int_{\lambda=t_0}^{t} \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{U}(\lambda) \mathbf{B}^*(\lambda) \boldsymbol\Phi^*(\tau,\lambda)  d \lambda $$

```{dropdown} Details

$$\begin{aligned}
& \int_{\lambda=t_0}^{t} \int_{\chi=t_0}^{\tau}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{R}_{\mathbf{u}\mathbf{u}}(\lambda, \chi) \mathbf{B}^*(\chi) \boldsymbol\Phi^*(\tau,\chi)  d \lambda \, d \chi = \\
& = \int_{\lambda=t_0}^{t} \int_{\chi=t_0}^{\tau}  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{U}(\lambda) \delta(\lambda-\chi) \mathbf{B}^*(\chi) \boldsymbol\Phi^*(\tau,\chi)  d \lambda \, d \chi = \\
& = \int_{\lambda=t_0}^{\min\{ t, \tau\}} \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{U}(\lambda) \mathbf{B}^*(\lambda) \boldsymbol\Phi^*(\tau,\lambda)  d \lambda \ ,
\end{aligned}$$

as 

$$\int_{\chi=t_0}^{\tau} \delta(\lambda-\chi) \mathbf{B}^*(\chi) \boldsymbol\Phi^*(\tau,\chi) d \chi =
\left\{ \begin{aligned}  
   \mathbf{B}^*(\lambda) \boldsymbol\Phi^*(\tau,\lambda) & \quad , \quad \text{if } \ \lambda \in [ t_0, \tau ] \\
   0 & \quad , \quad \text{otherwise} \\
\end{aligned} \right.$$

```

(ode:linear:miscellanea:stochastic-response:correlation-matrix:lyapunov)=
#### Lyapunov equation of the correlation matrix

Matrix $\mathbf{P}(t)$ satisfies the following Lyapunov equation,

$$\dot{\mathbf{P}} = \mathbf{A} \mathbf{P} + \mathbf{P} \mathbf{A}^* + \mathbf{B} \mathbf{U} \mathbf{B}^* \ .$$ (eq:lyapunov:correlation)

```{dropdown} Details
:open:

$$\begin{aligned}
 \frac{d \mathbf{P}}{d t} 
 & = \partial_t \boldsymbol\Phi \mathbf{P}_0 \boldsymbol\Phi + \boldsymbol\Phi \mathbf{P}_0 \partial_t \boldsymbol\Phi + \underbrace{\boldsymbol\Phi(t,t)}_{\mathbf{I}} \mathbf{B}(t) \mathbf{U}(t) \mathbf{B}^*(t) \underbrace{\boldsymbol\Phi(t,t)}_{=\mathbf{I}} + \\
 & + \int_{\lambda=t_0}^{t} \left\{ \partial_t  \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{U}(\lambda) \mathbf{B}^*(\lambda) \boldsymbol\Phi^*(\tau,\lambda) + \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{U}(\lambda) \mathbf{B}^*(\lambda) \partial_t \boldsymbol\Phi^*(\tau,\lambda) \right\} d \lambda = \\
 & = \mathbf{B}(t) \mathbf{U}(t) \mathbf{B}^*(t) + \mathbf{A}(t) \underbrace{\left[ \boldsymbol\Phi(t,t_0) \mathbf{P}_0 \boldsymbol\Phi^*(t,t_0) + \int_{\lambda=t_0}^{t} \boldsymbol\Phi(t,\lambda) \mathbf{B}(\lambda) \mathbf{U}(\lambda) \mathbf{B}^*(\lambda) \boldsymbol\Phi(t,\lambda) \right]}_{=\mathbf{P}(t)} + \left[ \dots \right]^* \mathbf{A}^*(t) = \\
 & = \mathbf{A} \mathbf{P} + \mathbf{P} \mathbf{A}^* + \mathbf{B} \mathbf{U} \mathbf{B}^* \ .
\end{aligned}$$


```



