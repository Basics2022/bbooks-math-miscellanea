(control:optimal:full-state-fb)=
# Full-state feedback

Optimal control can be recast as a **constrained optimization problem**, $J$, where an extreme - optimum - of an objective function must be found, subject to constraints that include the equations of motion. Some constraints may be included into an augmented objective function $\widetilde{J}$ with the methods of [Lagrange multipliers](optimization:constrained:lagrange-multipliers).


```{dropdown} Contents 
:open:

* [Generic ODE without exogenous inputs](control:optimal:full-state-fb:ode): 
* [Linear system without exogenous inputs](control:optimal:full-state-fb:linear): 
* [Linear system without exogenous inputs - infinite time horizon](control:optimal:full-state-fb:linear:infinite-time-horizon)

```

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

    formally writing the differential of the Wiener process $d \mathbf{w}_d$ as a white noise $\mathbf{d}$ times $dt$, "$d \mathbf{w}_d = \mathbf{d} \, dt$". While this may look like a useless trick, it helps us recallling that $| d \mathbf{w}_d |^2 \sim dt$, when evaluating covariances.

```

```{dropdown} Different approaches to the solution
:open:

Different approaches to the solution can be used, and help for a detailed comprehension of the topics.


* **Variational apporach** to constrained optimization,

   $$J(\mathbf{x},\mathbf{u}) = \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}(\tau)) d \tau +  D(\mathbf{x}(T)) - \int_{\tau=0}^{T} \boldsymbol\lambda^T \left( \dot{\mathbf{x}} - \mathbf{f}(\mathbf{x},\mathbf{u}) \right) \ ,$$

   where the equations of motion are constraints inserted in the objective function with the method of Lagrange multipliers.

* **Dynamic programming approach**, leading to **Hamilton-Jacobi-Bellman (HJB) equation** for the **value function** $V(t)$

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
...



