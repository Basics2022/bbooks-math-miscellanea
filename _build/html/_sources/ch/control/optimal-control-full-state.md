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


(control:optimal:full-state-fb:lti)=
## Linear system

