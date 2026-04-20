(control:optimal:full-state-fb)=
# Full-state feedback

Optimal control can be recast as a **constrained optimization problem**, $J$, where an extreme - optimum - of an objective function must be found, subject to constraints that include the equations of motion. Some constraints may be included into an augmented objective function $\widetilde{J}$ with the methods of [Lagrange multipliers](optimization:constrained:lagrange-multipliers).

```{dropdown} Different models - governing equations
:open:

* Generic ODE

   $$\mathbf{M} \dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})$$

* Linear ODE for deterministic signals

   $$\begin{cases}
     \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B}_u \mathbf{u} + \mathbf{B}_d \mathbf{d} \\
          \mathbf{y}  = \mathbf{C} \mathbf{x} + \mathbf{D}_u \mathbf{u} + \mathbf{D}_d \mathbf{d} + \mathbf{D}_r \mathbf{r}
   \end{cases}$$

* Linear SDE for stochastic signals. Exogenous inputs like disturbances $\mathbf{d}$ and measuerement noise $\mathbf{r}$ can be treated as stochastic processes. Thus, the equations are stochastic equations. As an example, if these noise are **white noise** they can be interpreted as the time derivative of Wiener processes, and the SDE can be written as

    $$ d \mathbf{x} = \mathbf{A} \mathbf{x} \, dt + \mathbf{B}_u \mathbf{u} \, dt + \mathbf{B}_d d \mathbf{w}_d \ ,$$

    begin "$d \mathbf{w}_d = \mathbf{d} \, dt$". While this may look like a useless trick, it helps us recallling that $| d \mathbf{w}_d |^2 \sim dt$, when evaluating covariances.

```

```{dropdown} Different approaches to the solution
:open:

Different approaches to the solution can be used, and help for a detailed comprehension of the topics.


* Variational apporach to constrained optimization,

   $$J(\mathbf{x},\mathbf{u}) = \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}(\tau)) d \tau +  D(\mathbf{x}(T)) - \int_{\tau=0}^{T} \boldsymbol\lambda^T \left( \dot{\mathbf{x}} - \mathbf{f}(\mathbf{x},\mathbf{u}) \right) \ ,$$

   where the equations of motion are constraints inserted in the objective function with the method of Lagrange multipliers.

* Hamilton-Bellman-Jacobi equation

   $$V(\mathbf{x}_t, t; \mathbf{u}) = \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}(\tau)) d \tau +  D(\mathbf{x}(T)) \ ,$$

   with the dynamics of the system subject to the governing equation $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x},\mathbf{u})$, and  the initial condition for the value function - the tail cost function - $x(t) = x_t$. These constraints can be explicitly applied if an expression of the solution of the dynamical equation exists, or they can be added with the method of Lagrange multipliers.

* ...

A common choice of the running cost $C(\mathbf{x},\mathbf{u})$ and the final cost $D(\mathbf{x}(T))$ are

$$\begin{aligned}
C(\mathbf{x}(\tau),\mathbf{u}(\tau)) & = \frac{1}{2}\left\{ \mathbf{x}^T(\tau) \mathbf{Q} \mathbf{x}(\tau) + \mathbf{u}^T(\tau) \mathbf{R} \mathbf{u}(\tau)  \right\} \\
D(\mathbf{x}(T)) & = \frac{1}{2} \mathbf{x}^T(T) \mathbf{Q}_T \mathbf{x}(T)  \ .
\end{aligned}$$



```

**Finite time vs. Infinite time horizon.**

...

(control:optimal:full-state-fb:ode)=
## Generic ODE without exogenous inputs

$$\mathbf{M} \dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u}) \ ,$$

with initial condition $\mathbf{x}(0) = \mathbf{x}_0$.

The objective function combines (weights) the error on a desired performance and the control input, in order to get the desired behavior with feasible control (that can be provided by actuators, without saturation, avoiding unnecessary high power input and too sharp behavior,...)

As an example, if the goal of the control $\mathbf{u}$ is to keep the system around $\mathbf{x} = \mathbf{0}$, the cost function to be minimized can be designed as

$$J = \int_{t=0}^{T} \dfrac{1}{2} \begin{bmatrix} \mathbf{x}^T & \mathbf{u}^T \end{bmatrix} \begin{bmatrix}  \mathbf{Q} & \mathbf{S} \\ \mathbf{S}^T & \mathbf{R} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix} \, dt + \frac{1}{2} \mathbf{x}^T(T) \mathbf{Q}_T \mathbf{x}(T) \ ,$$

with $\mathbf{Q} \ge 0$, and $\mathbf{R} > 0$ and symmetric.

````{dropdown} Constrained optimization
:open:

$$\widetilde{J}(\mathbf{x},\mathbf{u}; \boldsymbol\lambda) = \int_{\tau=0}^{T} C\left( \mathbf{x}(\tau), \mathbf{u}(\tau) \right) \, d\tau + D\left( \mathbf{x}(T) \right) - \int_{\tau=0}^{T} \boldsymbol\lambda^T \left( \mathbf{M} \dot{\mathbf{x}} - \mathbf{f}(\mathbf{x}(\tau), \mathbf{u}(\tau)) \right) \, d \tau \ .$$

$$\begin{aligned}
  0 = \delta \widetilde{J} 
  & = \int_{t=0}^{T} \delta \mathbf{x}^T \left( \partial_\mathbf{x} C + \partial_{\mathbf{x}} \mathbf{f}^T \boldsymbol\lambda + \mathbf{M}^T \dot{\boldsymbol{\lambda}}\right) d \tau + \\
  & + \int_{t=0}^{T} \delta \mathbf{u}^T \left( \partial_\mathbf{u} C + \partial_{\mathbf{u}} \mathbf{f}^T \boldsymbol\lambda \right) d \tau + \\
  & + \delta \mathbf{x}^T(T) \partial_{\mathbf{x}_T} D + \\
  & + \int_{t=0}^{T} \delta \boldsymbol\lambda^T ( \mathbf{M} \dot{\mathbf{x}} - \mathbf{f}(\mathbf{x}, \mathbf{u}) ) d \tau + \\
  & - \left. \delta \mathbf{x} \mathbf{M}^T \boldsymbol\lambda \right|_{t=0}^{T} \ .
\end{aligned}$$

So that

$$\begin{aligned}
 \delta \boldsymbol\lambda(t): & \quad \mathbf{M}   \dot{\mathbf{x}} = \mathbf{f} \\
                               & \quad \mathbf{x}(0) = \mathbf{x}_0 \\
 \delta \mathbf{x}(t)        : & \quad \mathbf{M}^T \dot{\boldsymbol{\lambda}} = -\partial_{\mathbf{x}} \mathbf{f}^T \boldsymbol\lambda - \partial_{\mathbf{x}} C \\
 \delta \mathbf{x}(T)        : & \quad \mathbf{M}^T \boldsymbol\lambda(T) = \partial_{\mathbf{x}_T} D \\
 \delta \mathbf{u}(t)        : & \quad \mathbf{0} = \partial_\mathbf{u} C + \partial_\mathbf{u} \mathbf{f}^T \boldsymbol\lambda \ .
\end{aligned}$$ (eq:optimal:ode)

The equations can be recast after the definition of the Hamiltonian of the system $H(\mathbf{x},\mathbf{u},\boldsymbol\lambda) = C(\mathbf{x},\mathbf{u}) + \boldsymbol\lambda^T \mathbf{f}(\mathbf{x},\mathbf{u})$ as

$$\begin{aligned}
 \delta \boldsymbol\lambda(t): & \quad \mathbf{0} = - \mathbf{M} \dot{\mathbf{x}} + \partial_{\boldsymbol\lambda} H = - \mathbf{M} \dot{\mathbf{x}} + \mathbf{f} \\
                               & \quad \mathbf{x}(0) = \mathbf{x}_0 \\
 \delta \mathbf{x}(t)        : & \quad \mathbf{M}^T \dot{\boldsymbol{\lambda}} = - \partial_{\mathbf{x}} H \\
 \delta \mathbf{x}(T)        : & \quad \mathbf{M}^T \boldsymbol\lambda(T) = \partial_{\mathbf{x}_T} D \\
 \delta \mathbf{u}(t)        : & \quad \mathbf{0} = \partial_\mathbf{u} H \ .
\end{aligned}$$ (eq:optimal:ode:hamiltonian)


```{dropdown} Gradient descent
:open:

* Start from a control law $\mathbf{u}^{(0)}(t)$,
* the state equation is integrated forward in time to get $\mathbf{x}^{(0)}(t)$, 
* Lagrange multiplier equation is integrated backward in time to get $\boldsymbol\lambda^{(0)}(t)$,
* The control law is updated with an increment $\delta \mathbf{u}$ that's proportional to the gradient of the cost function (with "opposite direction" to get $\delta \widetilde{J} < 0$), i.e. $\mathbf{u}^{(1)}(t) = \mathbf{u}^{(0)}(t) + \delta \mathbf{u}^{(0)}(t)$ with $\delta \mathbf{u}^{(0)}(t) = - c \nabla_{\mathbf{u}(t)} J^{(0)}$, with a positive step $c > 0$ and $\nabla_{\mathbf{u}} J = \mathbf{S}^T \mathbf{x} + \mathbf{R} \mathbf{u} + \partial_{\mathbf{u}} \mathbf{f}^T \boldsymbol\lambda$.
* Repeat previous steps with the updated control law, until convergence.

```

````

````{dropdown} HJB equation - Evaluation equation
:open:

```{dropdown} Without dynamical equations as a constraint introduced with Lagrange multipliers
:open:

$$V(\mathbf{x}_t, t) = \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}(\tau)) d \tau +  D(\mathbf{x}(T)) \ ,$$

subject to the dynamical equations of motion. The value function is a function of two arguments, $\mathbf{x}_t$, and $t$, and the first argument is a function of $t$. Thus the ordinary derivative w.r.t. time $t$ reads

$$\begin{aligned}
  \frac{d}{dt} V(\mathbf{x}_t, t) 
  & = \partial_t V(\mathbf{x}_t,t) +  \partial_\mathbf{x} V \, \dot{\mathbf{x}}   
    = \partial_t V(\mathbf{x}_t,t) +  \partial_\mathbf{x} V \, \mathbf{f} \ , 
\end{aligned}$$

or, using the definition and the rule of derivative for integrals

$$
  \frac{d}{dt} V(\mathbf{x}_t, t) = - C(\mathbf{x}(t), \mathbf{u}(t)) \ .
$$

Comparing the two expressions of the time derivative, Hamilton-Bellman-Jacobi equation for evaluating a given control $\mathbf{u}$ follows

$$0 = \partial_t V(\mathbf{x}_t, t) + \partial_{\mathbf{x}} V(\mathbf{x}_t, t) \, \mathbf{f}(\mathbf{x}_t, \mathbf{u}_t) + C(\mathbf{x}_t, \mathbf{u}_t) \ .$$

```

```{dropdown} With dynamical equations as a constraint introduced with Lagrange multipliers
:open:

$$\begin{aligned}
  V(\mathbf{x}_t, t; \boldsymbol\lambda)
  & = \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}(\tau)) d \tau +  D(\mathbf{x}(T)) - \int_{\tau=t}^{T} \boldsymbol\lambda^T ( \mathbf{M} \dot{\mathbf{x}} - \mathbf{f} ) d \tau \ ,
\end{aligned}$$

so that the variation (where's the variation w.r.t. $t$? Integration extreme is not prescribed) reads

$$\begin{aligned}
  \delta V(\mathbf{x}_t, t; \mathbf{u}, \boldsymbol\lambda)
  & = \int_{\tau=t}^{T} \left\{ \delta \mathbf{x}^T \partial_{\mathbf{x}} C + \delta \mathbf{u}^T \partial_{\mathbf{u}} C \right\} d \tau + \delta \mathbf{x}_T \partial_{\mathbf{x}_T} D(\mathbf{x}(T)) + \\
  & - \int_{\tau=t}^{T} \delta \boldsymbol\lambda^T ( \mathbf{M} \dot{\mathbf{x}} - \mathbf{f} ) d \tau + \int_{\tau=t}^T \delta \mathbf{x}^T \mathbf{M}^T \dot{\boldsymbol\lambda} \, d \tau + \\
  & - \delta \mathbf{x}^T(T) \mathbf{M}^T \boldsymbol\lambda(T) + \delta \mathbf{x}^T_t \mathbf{M}^T \boldsymbol\lambda(t) + \\
  & + \int_{\tau=t}^{T} \left\{ \delta \mathbf{x}^T \partial_{\mathbf{x}} \mathbf{f}^T \boldsymbol\lambda + \delta \mathbf{u}^T \partial_{\mathbf{u}} \mathbf{f}^T \boldsymbol\lambda \right\} d \tau
\end{aligned}$$

All the variations but $\delta \mathbf{x}_t$ are identically zero if the equations {eq}`eq:optimal:ode` are satisfied, the variation w.r.t. $\delta \mathbf{x}_t$ shows that the sensitivity to the initial state in the value function $\mathbf{x}_t$ equals the value of the Lagrange multiplier $\boldsymbol\lambda(t)$,

$$\nabla_{\mathbf{x}_t} V(\mathbf{x}_t, t; ...) = \boldsymbol\lambda(t) \ ,$$

with $\boldsymbol\lambda(t)$ part of the solution of the equations {eq}`eq:optimal:ode`. Thus the Lagrange multiplier $\boldsymbol\lambda(t)$ provides an information (first order, sensitivity) about the change in the value function $V(\mathbf{x}_t, t)$ for small changes of the intial state $\mathbf{x}_t$, i.e.

$$\delta_{\mathbf{x}_t} V(\mathbf{x}_t, t) \sim \delta \mathbf{x}_t^T \nabla_{\mathbf{x}_t} V + o(|\delta \mathbf{x}_t|) =  \delta \mathbf{x}^T_t \boldsymbol\lambda(t) + o(|\delta \mathbf{x}_t|) \ .$$

**todo**

* useful to exploit adjoint info for sensitivity

```

````

````{dropdown} HJB equation - Optimality equation
:open:

$$\begin{aligned}
  V^*(\mathbf{x}_t, t) = \min_{\mathbf{u}} V(\mathbf{x}_t, t) =
  & = \min_{\mathbf{u}} \left\{ \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}(\tau)) d \tau +  D(\mathbf{x}(T)) \right\} = \\
  & =                           \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}^*(\tau)) d \tau +  D(\mathbf{x}(T)) \ ,
\end{aligned}$$

subject to the dynamical equations of motion. The value function is a function of two arguments, $\mathbf{x}_t$, and $t$, and the first argument is a function of $t$. Thus the ordinary derivative w.r.t. time $t$ reads

$$\begin{aligned}
  \frac{d}{dt} V^*(\mathbf{x}_t, t) 
  & = \partial_t V^*(\mathbf{x}_t,t) +  \partial_\mathbf{x} V^* \, \dot{\mathbf{x}}   
    = \partial_t V^*(\mathbf{x}_t,t) +  \partial_\mathbf{x} V^* \, \mathbf{f}(\mathbf{x}_t,\mathbf{u}^*_t) \ , 
\end{aligned}$$

or, using the definition and the rule of derivative for integrals

$$
  \frac{d}{dt} V^*(\mathbf{x}_t, t) = - C(\mathbf{x}(t), \mathbf{u}^*(t)) \ .
$$

Comparing the two expressions of the time derivative, Hamilton-Bellman-Jacobi equation for evaluating a given control $\mathbf{u}$ follows

$$0 = \partial_t V^*(\mathbf{x}_t, t) + \partial_{\mathbf{x}} V^*(\mathbf{x}_t, t) \, \mathbf{f}(\mathbf{x}_t, \mathbf{u}^*_t) + C(\mathbf{x}_t, \mathbf{u}^*_t) \ ,$$

or

$$0 = \partial_t V^*(\mathbf{x}_t, t) + \min_{\mathbf{u}} \left\{ \partial_{\mathbf{x}} V^*(\mathbf{x}_t, t) \, \mathbf{f}(\mathbf{x}_t, \mathbf{u}_t) + C(\mathbf{x}_t, \mathbf{u}_t) \right\} \ .$$


````


(control:optimal:full-state-fb:linear)=
## Linear system

Let the dynamical equation of a system be

$$\begin{cases}
 \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
      \mathbf{y}  = \mathbf{C}_y \mathbf{x} + \mathbf{D}_y \mathbf{u} \\
      \mathbf{z}  = \mathbf{C}_z \mathbf{x} + \mathbf{D}_z \mathbf{u} \ ,
\end{cases}$$

with measurment output $\mathbf{y}$ and performance output $\mathbf{z}$, and with running and final cost

$$\begin{aligned}
C(\mathbf{x},\mathbf{u})
 & = \frac{1}{2} \left( \mathbf{z}^T \mathbf{Q} \mathbf{z} + \mathbf{u}^T \mathbf{R} \mathbf{u} \right) = \\
 & = \frac{1}{2} \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix}^T
               \begin{bmatrix}
                 \mathbf{C}_z^T \mathbf{Q} \mathbf{C}_z & \mathbf{C}_z^T \mathbf{Q} \mathbf{D}_z \\
                 \mathbf{D}_z^T \mathbf{Q} \mathbf{C}_z & \mathbf{D}_z^T \mathbf{Q} \mathbf{D}_z + \mathbf{R} \\
               \end{bmatrix}
               \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix} = \\
 & = \frac{1}{2} \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix}^T
               \begin{bmatrix}
                 \widetilde{\mathbf{Q}} & \mathbf{S} \\
                 \mathbf{S}^T & \widetilde{\mathbf{R}}
               \end{bmatrix}
               \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix}\ ,
\end{aligned}$$

$$D(\mathbf{x}_T) = \frac{1}{2} \mathbf{x}^T(T) \mathbf{Q}_T \mathbf{x}(T) \ .$$

The equations {eq}`eq:optimal:ode` become

$$\begin{aligned}
 \delta \boldsymbol\lambda(t): & \quad \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
                               & \quad \mathbf{x}(0) = \mathbf{x}_0 \\
 \delta \mathbf{x}(t)        : & \quad \dot{\boldsymbol{\lambda}} = - \mathbf{A}^T \boldsymbol\lambda - \widetilde{\mathbf{Q}} \mathbf{x} - \mathbf{S} \mathbf{u} \\
 \delta \mathbf{x}(T)        : & \quad \boldsymbol\lambda(T) = \mathbf{Q}_T \mathbf{x}(T) \\
 \delta \mathbf{u}(t)        : & \quad \mathbf{0} = \widetilde{\mathbf{R}} \mathbf{u} + \mathbf{S}^T \mathbf{x} + \mathbf{B}^T \boldsymbol\lambda \ .
\end{aligned}$$ (eq:optimal:ode:linear)

The weights onf the control are definite positive, $\widetilde{\mathbf{R}} > 0$, and thus invertible. The control can be written as a function of the state and the co-state as

$$\mathbf{u} = - \widetilde{\mathbf{R}}^{-1} \left( \mathbf{S}^T \mathbf{x} + \mathbf{B}^T \boldsymbol\lambda  \right) \ .$$

Now the closed loop system reads

$$
\begin{bmatrix} \dot{\mathbf{x}} \\ \dot{\boldsymbol\lambda} \end{bmatrix}
\begin{bmatrix}
  \mathbf{A} - \mathbf{B} \widetilde{\mathbf{R}}^{-1} \mathbf{S}^T & - \mathbf{B} \widetilde{\mathbf{R}}^{-1} \mathbf{B}^T \\
  -\widetilde{\mathbf{Q}} + \mathbf{S} \widetilde{\mathbf{R}}^{-1} \mathbf{S}^T & - \mathbf{A}^T + \mathbf{S} \widetilde{\mathbf{R}}^{-1} \mathbf{B}^T
\end{bmatrix}
\begin{bmatrix}      \mathbf{x}  \\      \boldsymbol\lambda  \end{bmatrix} \ ,
$$

with initial condition $\mathbf{x}(0) = \mathbf{x}_0$ and final condition $\boldsymbol\lambda(T) = \mathbf{Q}_T \mathbf{x}(T)$. The solution can be written as

$$\begin{bmatrix} \mathbf{x}(t) \\ \boldsymbol\lambda(t)  \end{bmatrix} = \boldsymbol\Psi(t,t_0) \begin{bmatrix} \mathbf{x}(t_0) \\ \boldsymbol\lambda(t_0) \end{bmatrix} = \begin{bmatrix} \boldsymbol\Psi_{xx}(t,t_0) & \boldsymbol\Psi_{x\lambda}(t,t_0) \\ \boldsymbol\Psi_{\lambda x}(t,t_0) & \boldsymbol\Psi_{\lambda \lambda}(t,t_0) \end{bmatrix} \begin{bmatrix} \mathbf{x}(t_0) \\ \boldsymbol\lambda(t_0) \end{bmatrix}$$

so that the state in $T$ reads

$$\begin{bmatrix} \mathbf{x}(T) \\ \boldsymbol\lambda(T)  \end{bmatrix} = \begin{bmatrix} \boldsymbol\Psi_{xx}(T,t_0) & \boldsymbol\Psi_{x\lambda}(T,t_0) \\ \boldsymbol\Psi_{\lambda x}(T,t_0) & \boldsymbol\Psi_{\lambda \lambda}(T,t_0) \end{bmatrix} \begin{bmatrix} \mathbf{x}(t_0) \\ \boldsymbol\lambda(t_0) \end{bmatrix}$$

so that

$$\begin{aligned}
  \mathbf{0}
  & = - \boldsymbol\lambda_T + \boldsymbol\Psi_{\lambda \lambda}(T,t_0) \boldsymbol\lambda_0 + \boldsymbol\Psi_{\lambda x}(T,t_0) \mathbf{x}_0  = \\
  & = - \mathbf{Q}_T \mathbf{x}_T + \boldsymbol\Psi_{\lambda \lambda}(T,t_0) \boldsymbol\lambda_0 + \boldsymbol\Psi_{\lambda x}(T,t_0) \mathbf{x}_0  = \\
  & = - \mathbf{Q}_T \left[ \boldsymbol\Psi_{xx}(T,t_0) \mathbf{x}_0+\boldsymbol\Psi_{x\lambda}(T,t_0) \boldsymbol\lambda_0 \right] + \boldsymbol\Psi_{\lambda \lambda}(T,t_0) \boldsymbol\lambda_0 + \boldsymbol\Psi_{\lambda x}(T,t_0) \mathbf{x}_0  \ ,
\end{aligned}$$

and thus

$$\boldsymbol\lambda_0 = \left(\boldsymbol\Psi_{\lambda \lambda} - \mathbf{Q} \boldsymbol\Psi_{x\lambda}(T,t_0) \right)^{-1} \left( \mathbf{Q} \boldsymbol\Psi_{xx}(T,t_0) - \boldsymbol\Psi_{\lambda x} \right) \mathbf{x}_0 \ .$$

```{dropdown} Value function and relation $\ \boldsymbol\lambda = \mathbf{P} \mathbf{x}$
:open:

Let the value function be

$$V(\mathbf{x}_t,t; \mathbf{u}) = \frac{1}{2} \int_{\tau=t}^{T} \left\{ \mathbf{x}^T_\tau \widetilde{\mathbf{Q}}_\tau \mathbf{x}_\tau + \mathbf{x}^T_\tau \mathbf{S}_\tau \mathbf{u}_\tau + \mathbf{u}^T_\tau \mathbf{S}^T_\tau \mathbf{x}_\tau + \mathbf{u}_\tau^T \widetilde{\mathbf{R}}_\tau \mathbf{u}_\tau \right\}  d \tau \, + \frac{1}{2} \mathbf{x}_T^T \mathbf{Q}_T \mathbf{x}_T \ ,$$

subject to the equations of motion as constraints $\dot{\mathbf{x}}_\tau = \mathbf{A}_\tau \mathbf{x}_\tau + \mathbf{B}_\tau \mathbf{u}_\tau$, and the initial condition $\mathbf{x}(t) = \mathbf{x}_t$. This constraint can be introduced either 1) expressing the state $\mathbf{x}_\tau$ as a function of the initial state and the input

$$\mathbf{x}_\tau = \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \ ,$$

or 2) with the methods of Lagrange multipliers. A **co-state** $\boldsymbol\lambda_t$ - corresponding to the Lagrange multiplier - can be evaluated as

$$\boldsymbol\lambda_t = \nabla_{\mathbf{x}_t} V \ .$$

**Method 1.**

$$\begin{aligned}
  V(\mathbf{x}_t,t; \mathbf{u}) 
  & = \frac{1}{2} \int_{\tau=t}^{T} \left\{ \left( \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \right)^T \widetilde{\mathbf{Q}}_\tau \left( \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \right) \right\} + \\
  & + \frac{1}{2} \int_{\tau=t}^{T} \left\{ \left( \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \right)^T \mathbf{S}_\tau \mathbf{u}_\tau \right\} d \tau + \\
  & + \frac{1}{2} \int_{\tau=t}^{T} \left\{  \mathbf{u}_\tau^T \mathbf{S}_\tau^T \left( \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \right)\right\} d \tau + \\
  & + \frac{1}{2} \int_{\tau=t}^{T} \mathbf{u}_\tau^T \widetilde{\mathbf{R}}_\tau \mathbf{u}_\tau \,  d \tau + \\
  & + \frac{1}{2} \left( \boldsymbol\Phi(T,t) \mathbf{x}_t + \int_{\xi=t}^{T} \boldsymbol\Phi(T,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi  \right)^T \mathbf{Q}_T \left( \boldsymbol\Phi(T,t) \mathbf{x}_t + \int_{\xi=t}^{T} \boldsymbol\Phi(T,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi  \right) = \\
\end{aligned}$$

and thus

$$\begin{aligned}
  \boldsymbol\lambda_t 
  & = \nabla_{\mathbf{x}_t} V = \\
  & = \int_{\tau=t}^T \left( \boldsymbol\Phi^T(\tau,t) \widetilde{\mathbf{Q}}_\tau \mathbf{x}_\tau + \boldsymbol\Phi^T(\tau,t) \mathbf{S}_\tau \mathbf{u}_\tau \right) \, d \tau + \boldsymbol\Phi^T(T,t) \mathbf{Q}_T \mathbf{x}_T = \\ 
  & = \left\{ \int_{\tau=t}^T \boldsymbol\Phi(\tau,t)^T \widetilde{\mathbf{Q}}_\tau \boldsymbol\Phi(\tau,t) \, d \tau + \boldsymbol\Phi^T(T,t) \mathbf{Q}_T \boldsymbol\Phi(T,t) \right\} \mathbf{x}_t + \int_{\tau=t}^T \boldsymbol\Phi^T(\tau,t) \mathbf{S}_\tau \mathbf{u}_\tau \, d \tau \ .
\end{aligned}$$

From optimization, $\mathbf{u}_\tau = - \widetilde{\mathbf{R}}^{-1}_\tau \left( \mathbf{B}_\tau^T \boldsymbol\lambda_\tau + \mathbf{S}^T_\tau \mathbf{x}_\tau \right)$,

**Method 2.**

```

```{dropdown} Optimal control
:open:

HJB optimality equation

$$0 = \partial_t V^*(\mathbf{x}_t, t) + \min_{\mathbf{u}} \left\{ \partial_{\mathbf{x}} V^*(\mathbf{x}_t, t) \, \mathbf{f}(\mathbf{x}_t, \mathbf{u}_t) + C(\mathbf{x}_t, \mathbf{u}_t) \right\} \ .$$

$$\begin{aligned}
  \mathbf{0}
  & = \delta_{\mathbf{u}} V = \\
  & = \int_{\tau=t}^{T} \left\{ \int_{\xi=t}^\tau \delta \mathbf{u}_\xi^T  \mathbf{B}_\xi^T \boldsymbol\Phi^T(\tau,\xi)  \, d \xi \, \left( \widetilde{\mathbf{Q}}_\tau \mathbf{x}_\tau + \mathbf{S}_\tau \mathbf{u}_\tau \right) + \delta \mathbf{u}_\tau^T \mathbf{S}^T_\tau \mathbf{x}_\tau + \delta \mathbf{u}_\tau^T \widetilde{\mathbf{R}} \mathbf{u}_\tau + \mathbf{B}_\tau^T \boldsymbol\Phi^T(T,\tau) \mathbf{Q}_T \mathbf{x}_T \right\} \, d \tau = \\
  & \\
  & = \text{TODO...details about variable swap in the integrals of the first term} = \\
  & \\
  & = \int_{\tau=t}^{T} \delta \mathbf{u}_\tau^T \left\{ \mathbf{B}^T_\tau \underbrace{\left( \int_{\xi=\tau}^T \boldsymbol\Phi^T(\xi,\tau) \left( \widetilde{\mathbf{Q}}_\xi \mathbf{x}_\xi + \mathbf{S}_\xi \mathbf{u}_\xi \right) \, d \xi + \boldsymbol\Phi^T(T,\tau) \mathbf{Q} \mathbf{x}_T \right)}_{\boldsymbol\lambda_\tau} + \mathbf{S}^T_\tau \mathbf{x}_\tau + \widetilde{\mathbf{R}} \mathbf{u}_\tau \right\} \, d \tau \ ,
\end{aligned}$$

and thus, from the arbitrariety of $\delta \mathbf{u}_\tau$, and since $\widetilde{\mathbf{R}}$ is required  to be invertible

$$\mathbf{u}_\tau = - \widetilde{\mathbf{R}}^{-1}_\tau \left( \mathbf{B}_\tau^T \boldsymbol\lambda_\tau + \mathbf{S}^T_\tau \mathbf{x}_\tau \right) \ .$$


```


```{dropdown} ...
:open:

If (**todo** why?) $\boldsymbol\lambda = \mathbf{P} \mathbf{x}$,  

**Using HJB equation.**

$$V(\mathbf{x}_t,t; \mathbf{u}) = \frac{1}{2} \int_{\tau=t}^{T} \dots  d \tau \, + \frac{1}{2} \mathbf{x}_T^T \mathbf{Q}_T \mathbf{x}_T + \dots$$

**Proportional control.** This should not be an assumption, but a result of the problem *!!!*

If $\mathbf{u} = - \mathbf{G} \mathbf{x}$, the solution of the closed-loop system

$$\dot{\mathbf{x}} = \left( \mathbf{A} - \mathbf{B} \mathbf{G} \right) \mathbf{x}$$

reads $\mathbf{x}(\tau) = \boldsymbol\Psi_c(\tau,t) \mathbf{x}(t)$. The value function becomes

$$\begin{aligned}
  V(\mathbf{x}_t,t; \mathbf{G})
  & = \frac{1}{2} \mathbf{x}_t^T \int_{\tau=t}^T \boldsymbol\Phi^T_c(\tau,t) \left( \widetilde{\mathbf{Q}} - \mathbf{G}^T \mathbf{S}^T - \mathbf{S} \mathbf{G} + \mathbf{G}^T \widetilde{\mathbf{R}} \mathbf{G} \right) \boldsymbol\Phi_c(\tau,t) \, d \tau \, \mathbf{x}_t + \frac{1}{2} \mathbf{x}_t^T \boldsymbol\Phi_c^T(T,t) \mathbf{Q}_T \boldsymbol\Phi_c(T,t) \mathbf{x}_t = \\
  & = \frac{1}{2} \mathbf{x}_t^T \left\{ \int_{\tau=t}^T \boldsymbol\Phi^T_c(\tau,t) \left( \widetilde{\mathbf{Q}} - \mathbf{G}^T \mathbf{S}^T - \mathbf{S} \mathbf{G} + \mathbf{G}^T \widetilde{\mathbf{R}} \mathbf{G} \right) \boldsymbol\Phi_c(\tau,t) \, d \tau + \boldsymbol\Phi_c^T(T,t) \mathbf{Q}_T \boldsymbol\Phi_c(T,t)\right\} \mathbf{x}_t  = \\
  & = \frac{1}{2} \mathbf{x}_t^T \mathbf{P}(t) \mathbf{x}_t \ .
\end{aligned}$$

Thus, the costate reads $\boldsymbol\lambda = \nabla_{\mathbf{x}_t} V = \mathbf{P} \mathbf{x}$.

Matrix $\mathbf{P}$ satisfies a [Lyapunov equation](lyapunov-eq),

$$\dot{\mathbf{P}} = \mathbf{A}^T \mathbf{P} + \mathbf{P}\mathbf{A} + \left( \widetilde{\mathbf{Q}} - \mathbf{G}^T \mathbf{S}^T - \mathbf{S} \mathbf{G} + \mathbf{G}^T \widetilde{\mathbf{R}} \mathbf{G} \right) \ ,$$

as it can be easily found by direct computation of the time derivative of $\mathbf{P}$.



```


```{dropdown} Decoupled weights
:open:

Let $\mathbf{S} = \mathbf{0}$, then $\mathbf{u} = - \widetilde{\mathbf{R}}^{-1} \mathbf{B}^T \boldsymbol\lambda$, and thus the control is a linear combination of the co-state.

The transformation $\mathbf{v} := \mathbf{u} + \widetilde{\mathbf{R}}^{-1} \mathbf{S}^T \mathbf{x}$, make a coupled objective function for the original system a decoupeld objective function for a modified system.

```

**todo**
* Are $\Psi$ matrices invertible?
* Properties of the Hamilton matrix...
* What's a conjugate point?
* ...



```{dropdown} Coupled state-input weights
:open:

$$J = \frac{1}{2} \int_{\tau=0}^{T} \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix}^T \begin{bmatrix} \mathbf{Q} & \mathbf{S} \\ \mathbf{S}^T & \mathbf{R} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix} d \tau + \frac{1}{2} \mathbf{x}_T^T \mathbf{Q}_T \mathbf{x}_T$$


```

```{dropdown} Decoupled state-input weights
:open:

The problem can be decoupled with a transformation

$$\begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix} = \begin{bmatrix} \mathbf{I} & \mathbf{0} \\ \mathbf{T} & \mathbf{I} \end{bmatrix} \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix} $$

so that

$$\begin{aligned}
  \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix}^T \begin{bmatrix} \mathbf{Q} & \mathbf{S} \\ \mathbf{S}^T & \mathbf{R} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix}
  & = \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix}^T \begin{bmatrix} \mathbf{I} & \mathbf{T}^T \\ \mathbf{0} & \mathbf{I} \end{bmatrix} \begin{bmatrix} \mathbf{Q} & \mathbf{S} \\ \mathbf{S}^T & \mathbf{R} \end{bmatrix} \begin{bmatrix} \mathbf{I} & \mathbf{0} \\ \mathbf{T} & \mathbf{I} \end{bmatrix}  \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix} = \\
  & = \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix}^T \begin{bmatrix} \mathbf{Q} + \mathbf{T}^T \mathbf{S}^T & \mathbf{S} + \mathbf{T}^T \mathbf{R} \\ \mathbf{S}^T & \mathbf{R} \end{bmatrix} \begin{bmatrix} \mathbf{I} & \mathbf{0} \\ \mathbf{T} & \mathbf{I} \end{bmatrix}  \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix} = \\ 
  & = \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix}^T \begin{bmatrix} \mathbf{Q} + \mathbf{T}^T \mathbf{S}^T + \mathbf{S} \mathbf{T} + \mathbf{T}^T \mathbf{R} \mathbf{T} & \mathbf{S} + \mathbf{T}^T \mathbf{R} \\ \mathbf{S}^T + \mathbf{R} \mathbf{T} & \mathbf{R} \end{bmatrix} \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix} \ ,
\end{aligned}$$

Extra-diagonal terms are identically zero if $\mathbf{T} = - \mathbf{R}^{-1} \mathbf{S}^T$. The coordinate transformation becomes

$$\begin{aligned}
 \mathbf{x} & = \widetilde{\mathbf{x}} \\
 \mathbf{u} & = -\mathbf{R}^{-1} \mathbf{S}^T \widetilde{\mathbf{x}} + \widetilde{\mathbf{u}} \\
\end{aligned}$$

and the running cost reads

$$
  \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix}^T \begin{bmatrix} \mathbf{Q} - \mathbf{S} \mathbf{R}^{-1} \mathbf{S}^T & \mathbf{0} \\ \mathbf{0} & \mathbf{R} \end{bmatrix} \begin{bmatrix} \widetilde{\mathbf{x}} \\ \widetilde{\mathbf{u}} \end{bmatrix} \ .
$$

The linear system

$$\begin{aligned}
  \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
       \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} \\
\end{aligned}$$

becomes

$$\begin{aligned}
  \dot{\widetilde{\mathbf{x}}} & = \left( \mathbf{A} - \mathbf{B} \mathbf{R}^{-1} \mathbf{S}^T \right) \widetilde{\mathbf{x}} + \mathbf{B} \widetilde{\mathbf{u}} \\
       \mathbf{y}  & = \left( \mathbf{C} - \mathbf{D} \mathbf{R}^{-1} \mathbf{S}^T \right) \widetilde{\mathbf{x}} + \mathbf{D} \widetilde{\mathbf{u}} 
\end{aligned}$$

```

```{dropdown} Decoupled system
:open:

$$J = \frac{1}{2} \int_{\tau=0}^{T} \begin{bmatrix} \mathbf{x} \\ \widetilde{\mathbf{u}} \end{bmatrix}^T \begin{bmatrix} \hat{\mathbf{Q}} & \mathbf{0} \\ \mathbf{0} & \mathbf{R} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \widetilde{\mathbf{u}} \end{bmatrix} d \tau + \frac{1}{2} \mathbf{x}_T^T \mathbf{Q}_T \mathbf{x}_T - \int_{\tau=0}^{t} \boldsymbol\lambda^T \left( \dot{\mathbf{x}} - \hat{\mathbf{A}} \mathbf{x} + \mathbf{B} \widetilde{\mathbf{u}} \right) d \tau .$$

Optimization gives

$$\begin{aligned}
 \delta \boldsymbol\lambda(t): & \quad \dot{\mathbf{x}} = \hat{\mathbf{A}} \mathbf{x} + \mathbf{B} \widetilde{\mathbf{u}} \\
                               & \quad \mathbf{x}(0) = \mathbf{x}_0 \\
 \delta \mathbf{x}(t)        : & \quad \dot{\boldsymbol{\lambda}} = - \hat{\mathbf{A}}^T \boldsymbol\lambda - \hat{\mathbf{Q}} \mathbf{x} \\
 \delta \mathbf{x}(T)        : & \quad \boldsymbol\lambda(T) = \mathbf{Q}_T \mathbf{x}(T) \\
 \delta \mathbf{u}(t)        : & \quad \mathbf{0} = \mathbf{R} \widetilde{\mathbf{u}} + \mathbf{B}^T \boldsymbol\lambda \ .
\end{aligned}$$ (eq:optimal:ode:linear:decoupling)

The modified optimal control reads

$$\widetilde{\mathbf{u}} = - \mathbf{R}^{-1} \mathbf{B}^T \boldsymbol\lambda$$

and thus

$$\mathbf{u} = - \mathbf{R}^{-1} \left( \mathbf{S}^T \mathbf{x} + \mathbf{B}^T \boldsymbol\lambda \right) \ .$$

$$\mathbf{x}(t) = \hat{\boldsymbol\Phi}(t,t_0)\mathbf{x}_0 + \int_{\tau=t_0}^{t} \hat{\boldsymbol\Phi}(t,\tau) \mathbf{B}_\tau \widetilde{\mathbf{u}}(\tau) d \tau \ $$

$$\boldsymbol\lambda_t = \partial_{\mathbf{x}_t} V = \left[ \int_{\tau=t}^{T} \hat{\boldsymbol\Phi}^T(\tau,t) \hat{\mathbf{Q}}_\tau \hat{\boldsymbol\Phi}(\tau,t) \, d \tau + \hat{\boldsymbol\Phi}^T(T,t) \mathbf{Q}_T \hat{\boldsymbol\Phi}(T,t) \right] \mathbf{x}_t = \mathbf{P}(t,T) \mathbf{x}_t \ . $$

```

$$\partial_t \hat{\boldsymbol\Phi}(t,\tau) = \hat{\mathbf{A}}(t)  \hat{\boldsymbol\Phi}(t,\tau) \ .$$

$$\partial_T \mathbf{P}$$


