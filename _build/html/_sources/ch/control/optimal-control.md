(control:optimal)=
# Optimal control

Optimal control can be recast as a **constrained optimization problem**, $J$, where an extreme - optimum - of an objective function must be found, subject to constraints that include the equations of motion. Some constraints may be included into an augmented objective function $\widetilde{J}$ with the methods of [Lagrange multipliers](optimization:constrained:lagrange-multipliers).

**Finite time vs. Infinite time horizon.**

## Generic ODE

$$\mathbf{M} \dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})$$

The objective function combines (weights) the error on a desired performance and the control input, in order to get the desired behavior with feasible control (that can be provided by actuators, without saturation, avoiding unnecessary high power input and too sharp behavior,...)

As an example, if the goal of the control $\mathbf{u}$ is to keep the system around $\mathbf{x} = \mathbf{0}$, the cost function to be minimized can be designed as

$$J = \int_{t=0}^{T} \dfrac{1}{2} \begin{bmatrix} \mathbf{x}^T & \mathbf{u}^T \end{bmatrix} \begin{bmatrix}  \mathbf{Q} & \mathbf{S} \\ \mathbf{S}^T & \mathbf{R} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix} \, dt \ .$$


## LTI

$$J = \int_{t=0}^{T} \dfrac{1}{2} \begin{bmatrix} \mathbf{x}^T & \mathbf{u}^T \end{bmatrix} \begin{bmatrix}  \mathbf{Q} & \mathbf{S} \\ \mathbf{S}^T & \mathbf{R} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \mathbf{u} \end{bmatrix} \, dt$$

$$\begin{cases}
  \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
       \mathbf{y}  = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} \\
\end{cases}$$

### Infinite-horizon full-state feedback

No need for an [observer](control:observer). The system is assumed to be stable. The augmented cost function reads 

$$\widetilde{J}(\mathbf{x}, \mathbf{u}; \boldsymbol{\lambda}) = \int_{t=0}^{+\infty} \left\{ \dfrac{1}{2} \mathbf{x}^T \mathbf{Q} \mathbf{x} + \mathbf{x}^T \mathbf{S} \mathbf{u} + \dfrac{1}{2} \mathbf{u}^T \mathbf{R} \mathbf{u} - \boldsymbol{\lambda}^T (\dot{\mathbf{x}} - \mathbf{A} \mathbf{x} - \mathbf{B}  \mathbf{u} ) \right\} \, dt \ ,$$

with given initial conditions $\mathbf{x}(0) = \mathbf{x}_0$, so that $\delta \mathbf{x}_0 = \mathbf{0}$.

Using [calculus of variations](calculus-variations:intro), the variations of the cost function w.r.t. $\mathbf{x}$, $\mathbf{u}$, $\boldsymbol{\lambda}$ read

$$\begin{aligned}
 \delta_{\mathbf{x}}           : & \quad  \mathbf{Q} \mathbf{x} + \mathbf{S} \mathbf{u} + \dot{\boldsymbol{\lambda}} + \mathbf{A}^T \boldsymbol{\lambda} = \mathbf{0} \\
 \delta_{\mathbf{u}}           : & \quad  \mathbf{S}^T \mathbf{x} + \mathbf{R} \mathbf{u} + \mathbf{B}^T \boldsymbol{\lambda} = \mathbf{0} \\
 \delta_{\boldsymbol{\lambda}} : & \quad  \dot{\mathbf{x}} - \mathbf{A} \mathbf{x} - \mathbf{B} \mathbf{u} = \mathbf{0} \\
\end{aligned}$$

From the variation w.r.t. $\mathbf{u}$, since $\mathbf{R} > 0$ and thus innvertible,

$$\mathbf{u} = - \mathbf{R}^{-1} \left( \mathbf{S}^T \mathbf{x} + \mathbf{B}^T \boldsymbol{\lambda} \right)$$

Now, assuming the relation $\boldsymbol{\lambda} = \mathbf{P} \mathbf{x}$, it follows

$$\begin{aligned}
  \dot{\boldsymbol{\lambda}} 
  & = - \mathbf{Q} \mathbf{x} - \mathbf{S} \mathbf{u} - \mathbf{A}^T \boldsymbol{\lambda} = \\
  & = \left\{ - \mathbf{Q}+ \mathbf{S} \mathbf{R}^{-1} \left( \mathbf{S}^T + \mathbf{B}^T \mathbf{P} \right) - \mathbf{A}^T \mathbf{P} \right\} \mathbf{x}  \\
  \dot{\boldsymbol{\lambda}}
  & = \dot{\mathbf{P}} \mathbf{x} + \mathbf{P} \dot{\mathbf{x}} = \\
  & = \dot{\mathbf{P}} \mathbf{x} + \mathbf{P} \left( \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \right) = \\
  & = \left\{ \dot{\mathbf{P}} + \mathbf{P} \left[ \mathbf{A} - \mathbf{B} \mathbf{R}^{-1} \left( \mathbf{S}^T + \mathbf{B}^T \mathbf{P} \right)  \right] \right\} \mathbf{x} \ ,
\end{aligned}$$

and comparing the two different expressions of $\dot{\boldsymbol{\lambda}}$, if the equality holds for any $\mathbf{x}$, the **dynamical Riccati equation** for $\mathbf{P}$ is derived as

$$\dot{\mathbf{P}} + \mathbf{P} \widetilde{\mathbf{A}} + \widetilde{\mathbf{A}}^T \mathbf{P} - \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} + \widetilde{\mathbf{Q}} = \mathbf{0} \ ,$$

where $\widetilde{\mathbf{A}} = \mathbf{A} - \mathbf{B} \mathbf{R}^{-1} \mathbf{S}^T $ and $\widetilde{\mathbf{Q}} = \mathbf{Q} - \mathbf{S} \mathbf{R}^{-1} \mathbf{S}^T$. Riccati equation is a non-linear dynamical matrix equation in $\mathbf{P}$. Algorithms for computing the solution of dynamical and algebraic equation exists, see {prf:ref}`control-optimal-riccati`.

<!--
$$\dot{\mathbf{P}} = - \mathbf{P} \left( \mathbf{A} - \mathbf{B} \mathbf{R}^{-1} \mathbf{S}^T \right) - \left( \mathbf{A} - \mathbf{B} \mathbf{R}^{-1} \mathbf{S}^T \right)^T \mathbf{P} + \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} - \left( \mathbf{Q} - \mathbf{S} \mathbf{R}^{-1} \mathbf{S}^T \right)$$
-->

Once $\mathbf{P}$ is evaluated, the control law reads

$$\mathbf{u} = - \mathbf{R}^{-1} \left( \mathbf{S}^T + \mathbf{B}^T \mathbf{P} \right) \mathbf{x} \ .$$

For infinite-horizone, the algebraic equation (ARE) for the steady state is solved after setting $\dot{\mathbf{P}} = \mathbf{0}$, the solution for a LTI system is a constant matrix $\mathbf{P}$, and thus the control law is a proportional feedback on the full-state of the system,

$$\mathbf{u} = - \mathbf{G} \mathbf{x} \ ,$$

with $\mathbf{G} = \mathbf{R}^{-1} \left( \mathbf{S}^T + \mathbf{B}^T \mathbf{P} \right)$.

```{prf:example} Solution of Riccati equation
:label: control-optimal-riccati
...

```

**Properties.** **todo**
- $\mathbf{P}$ symmetric? definite positive? ...
- ...


