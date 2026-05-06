(control:optimal:full-state-fb:linear)=
# Linear system without exogenous inputs

(control:optimal:full-state-fb:linear:variational-approach)=
## Variational approach

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

$$\mathbf{u} = - \widetilde{\mathbf{R}}^{-1} \left( \mathbf{S}^T \mathbf{x} + \mathbf{B}^T \boldsymbol\lambda  \right) \ .$$ (eq:optimal:linear:u-1)

The expression {eq}`eq:optimal:linear:u-1` shows that the optimal control law is a control proportional to the state $\mathbf{x}$ and the co-state $\boldsymbol\lambda$. As it's shown below, there's a proportionality relation between the state and the co-state $\boldsymbol\lambda = \mathbf{P} \mathbf{x}$ as well, with $\mathbf{P}$ a symmetric, semi-positive definite matrix, satisfying some matrix equations. See:

* the relation $\boldsymbol\lambda_t = \mathbf{P}_t \mathbf{x}_t$ arising by the relation {eq}`eq:co-state:sensitivity` with $\mathbf{M} = \mathbf{I}$, $\boldsymbol \lambda_t = \nabla_{\mathbf{x}_t} V$ in the [dynamic programming approach](control:optimal:full-state-fb:linear:dynamic-programming)
* the relation $\boldsymbol\lambda_t = \mathbf{P}_t \mathbf{x}_t$ arising in the [Hamiltonian form of the closed-loop system](control:optimal:full-state-fb:linear:hamiltonian-s) {eq}`eq:optimal:linear:cl:hamiltonian` 

(control:optimal:full-state-fb:linear:hamiltonian-system)=
## Hamiltonian form of the closed-loop system

Now the closed loop system reads

$$
\begin{bmatrix} \dot{\mathbf{x}} \\ \dot{\boldsymbol\lambda} \end{bmatrix}
\begin{bmatrix}
  \mathbf{A} - \mathbf{B} \widetilde{\mathbf{R}}^{-1} \mathbf{S}^T & - \mathbf{B} \widetilde{\mathbf{R}}^{-1} \mathbf{B}^T \\
  -\widetilde{\mathbf{Q}} + \mathbf{S} \widetilde{\mathbf{R}}^{-1} \mathbf{S}^T & - \mathbf{A}^T + \mathbf{S} \widetilde{\mathbf{R}}^{-1} \mathbf{B}^T
\end{bmatrix}
\begin{bmatrix}      \mathbf{x}  \\      \boldsymbol\lambda  \end{bmatrix} \ ,
$$ (eq:optimal:linear:cl:hamiltonian)

with initial condition $\mathbf{x}(0) = \mathbf{x}_0$ and final condition $\boldsymbol\lambda(T) = \mathbf{Q}_T \mathbf{x}(T)$. The solution of this linear system can be formally written using the propagator $\boldsymbol\Psi(t,t_0)$ as

$$\begin{bmatrix} \mathbf{x}(t) \\ \boldsymbol\lambda(t)  \end{bmatrix} = \boldsymbol\Psi(t,t_0) \begin{bmatrix} \mathbf{x}(t_0) \\ \boldsymbol\lambda(t_0) \end{bmatrix} = \begin{bmatrix} \boldsymbol\Psi_{xx}(t,t_0) & \boldsymbol\Psi_{x\lambda}(t,t_0) \\ \boldsymbol\Psi_{\lambda x}(t,t_0) & \boldsymbol\Psi_{\lambda \lambda}(t,t_0) \end{bmatrix} \begin{bmatrix} \mathbf{x}(t_0) \\ \boldsymbol\lambda(t_0) \end{bmatrix}$$

As the initial condition for $\boldsymbol\lambda$ is not known, it's not possible so far to integrate this equation forward in time. 

**Initial condition $\ \boldsymbol\lambda(0)$.** It's possible to find the initial condition for the co-state, using the propagator between $0$ and $T$, and the final condition $\lambda(T) = \mathbf{Q}_T \mathbf{x}_T$. The state of the Hamiltonian system in $T$ reads

$$\begin{bmatrix} \mathbf{x}(T) \\ \boldsymbol\lambda(T)  \end{bmatrix} = \begin{bmatrix} \boldsymbol\Psi_{xx}(T,t_0) & \boldsymbol\Psi_{x\lambda}(T,t_0) \\ \boldsymbol\Psi_{\lambda x}(T,t_0) & \boldsymbol\Psi_{\lambda \lambda}(T,t_0) \end{bmatrix} \begin{bmatrix} \mathbf{x}(t_0) \\ \boldsymbol\lambda(t_0) \end{bmatrix}$$

so that (using the second block of the equations first, and then replacing $\mathbf{x}_T$ from the first block),

$$\begin{aligned}
  \mathbf{0}
  & = - \boldsymbol\lambda_T + \boldsymbol\Psi_{\lambda \lambda}(T,t_0) \boldsymbol\lambda_0 + \boldsymbol\Psi_{\lambda x}(T,t_0) \mathbf{x}_0  = \\
  & = - \mathbf{Q}_T \mathbf{x}_T + \boldsymbol\Psi_{\lambda \lambda}(T,t_0) \boldsymbol\lambda_0 + \boldsymbol\Psi_{\lambda x}(T,t_0) \mathbf{x}_0  = \\
  & = - \mathbf{Q}_T \left[ \boldsymbol\Psi_{xx}(T,t_0) \mathbf{x}_0+\boldsymbol\Psi_{x\lambda}(T,t_0) \boldsymbol\lambda_0 \right] + \boldsymbol\Psi_{\lambda \lambda}(T,t_0) \boldsymbol\lambda_0 + \boldsymbol\Psi_{\lambda x}(T,t_0) \mathbf{x}_0  \ ,
\end{aligned}$$

and thus

$$\boldsymbol\lambda_0 = \left(\boldsymbol\Psi_{\lambda \lambda}(T,t_0) - \mathbf{Q}_T \boldsymbol\Psi_{x\lambda}(T,t_0) \right)^{-1} \left( \mathbf{Q}_T \boldsymbol\Psi_{xx}(T,t_0) - \boldsymbol\Psi_{\lambda x}(T,t_0) \right) \mathbf{x}_0 \ ,$$

or

$$\boldsymbol\lambda_0 = \mathbf{P}_0 \mathbf{x}_0 \ .$$

**Relation between $\mathbf{x}(t)$ and $\boldsymbol\lambda(t)$.**

$$\begin{aligned}
  \mathbf{x}_t 
  & = \boldsymbol\Psi_{xx}(t,t_0) \mathbf{x}_0 + \boldsymbol\Psi_{x\lambda}(t,t_0) \boldsymbol\lambda_0 = \\
  & = \left[ \boldsymbol\Psi_{xx}(t,t_0) + \boldsymbol\Psi_{x\lambda}(t,t_0) \mathbf{P}_0 \right] \mathbf{x}_0 \ , \\
  \boldsymbol{\lambda}_t 
  & = \boldsymbol\Psi_{\lambda x}(t,t_0) \mathbf{x}_0 + \boldsymbol\Psi_{\lambda \lambda}(t,t_0) \boldsymbol\lambda_0 = \\
  & = \left[ \boldsymbol\Psi_{\lambda x}(t,t_0) + \boldsymbol\Psi_{\lambda\lambda}(t,t_0) \mathbf{P}_0 \right] \mathbf{x}_0 = \\
  & = \left[ \boldsymbol\Psi_{\lambda x}(t,t_0) + \boldsymbol\Psi_{\lambda\lambda}(t,t_0) \mathbf{P}_0 \right] \left[ \boldsymbol\Psi_{xx}(t,t_0) + \boldsymbol\Psi_{x\lambda}(t,t_0) \mathbf{P}_0 \right]^{-1} \mathbf{x}_t \ .
\end{aligned}$$

or 

$$\boldsymbol\lambda(t) = \mathbf{P}(t) \mathbf{x}(t) \ .$$

**todo** 
* Does this inverse matrix exist? ...

(control:optimal:full-state-fb:linear:dynamic-programming)=
## Dynamic programming approach

```{dropdown} Value function and relation $\ \boldsymbol\lambda = \mathbf{P} \mathbf{x}$
:open:

Let the value function be

$$V(\mathbf{x}_t,t; \mathbf{u}) = \frac{1}{2} \int_{\tau=t}^{T} \left\{ \mathbf{x}^T_\tau \widetilde{\mathbf{Q}}_\tau \mathbf{x}_\tau + \mathbf{x}^T_\tau \mathbf{S}_\tau \mathbf{u}_\tau + \mathbf{u}^T_\tau \mathbf{S}^T_\tau \mathbf{x}_\tau + \mathbf{u}_\tau^T \widetilde{\mathbf{R}}_\tau \mathbf{u}_\tau \right\}  d \tau \, + \frac{1}{2} \mathbf{x}_T^T \mathbf{Q}_T \mathbf{x}_T \ ,$$

subject to the equations of motion as constraints $\dot{\mathbf{x}}_\tau = \mathbf{A}_\tau \mathbf{x}_\tau + \mathbf{B}_\tau \mathbf{u}_\tau$, and the initial condition $\mathbf{x}(t) = \mathbf{x}_t$. This constraint can be introduced either 1) expressing the state $\mathbf{x}_\tau$ as a function of the initial state and the input

$$\mathbf{x}_\tau = \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \ ,$$

or 2) with the methods of Lagrange multipliers. A **co-state** $\boldsymbol\lambda_t$ - corresponding to the Lagrange multiplier - can be evaluated as

$$\boldsymbol\lambda_t = \nabla_{\mathbf{x}_t} V \ .$$

**Method 1.** Using the expression {eq}`eq:ode:system:linear:sol` of the [general solution of a linear system of ODEs](ode:linear:miscellanea:general-solution) for $\tau > t$ with initial conditions $\mathbf{x}(t) = \mathbf{x}_t$ and input $\mathbf{u}(\tau)$,

$$\begin{aligned}
  V(\mathbf{x}_t,t; \mathbf{u}) 
  & = \frac{1}{2} \int_{\tau=t}^{T} \left\{ \left( \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \right)^T \widetilde{\mathbf{Q}}_\tau \left( \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \right) \right\} + \\
  & + \frac{1}{2} \int_{\tau=t}^{T} \left\{ \left( \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \right)^T \mathbf{S}_\tau \mathbf{u}_\tau \right\} d \tau + \\
  & + \frac{1}{2} \int_{\tau=t}^{T} \left\{  \mathbf{u}_\tau^T \mathbf{S}_\tau^T \left( \boldsymbol\Phi(\tau,t) \mathbf{x}_t + \int_{\xi=t}^{\tau} \boldsymbol\Phi(\tau,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi \right)\right\} d \tau + \\
  & + \frac{1}{2} \int_{\tau=t}^{T} \mathbf{u}_\tau^T \widetilde{\mathbf{R}}_\tau \mathbf{u}_\tau \,  d \tau + \\
  & + \frac{1}{2} \left( \boldsymbol\Phi(T,t) \mathbf{x}_t + \int_{\xi=t}^{T} \boldsymbol\Phi(T,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi  \right)^T \mathbf{Q}_T \left( \boldsymbol\Phi(T,t) \mathbf{x}_t + \int_{\xi=t}^{T} \boldsymbol\Phi(T,\xi) \mathbf{B}_\xi \mathbf{u}_\xi \, d \xi  \right) = \\
\end{aligned}$$

the relation $\boldsymbol\lambda_t = \nabla_{\mathbf{x}_t} V$ gives

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

with final conditions

$$\mathbf{P}(T) = \mathbf{Q}_T \ ,$$

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

```{dropdown} Lyapunov and Riccati equations
:open:

Control law in the uncoupled coordinates,

$$\begin{aligned}
  \widetilde{\mathbf{u}}
  & = - \mathbf{R}^{-1} \mathbf{B}^T \boldsymbol\lambda = \\
  & = - \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} \mathbf{x} = \\
  & = - \widetilde{\mathbf{K}} \mathbf{x} \ ,
\end{aligned}$$

and

$$\begin{aligned}
  \mathbf{u} 
  & = \widetilde{\mathbf{u}} - \mathbf{R}^{-1} \mathbf{S}^T \mathbf{x} = \\
  & = - \mathbf{R}^{-1} \left( \mathbf{B}^T \mathbf{P} + \mathbf{S}^T \right) \mathbf{x} = \\
  & = - \mathbf{K} \mathbf{x} \ .
\end{aligned}$$

so that $\mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} = \mathbf{K} - \mathbf{R}^{-1} \mathbf{S}^T$.

Relation between the co-state an the state

$$\boldsymbol\lambda = \mathbf{P} \mathbf{x} \ .$$

State and co-state dynamical equations

$$\begin{aligned}
  \dot{\mathbf{x}} & = \hat{\mathbf{A}} \mathbf{x} + \mathbf{B} \widetilde{\mathbf{u}} \\
  \dot{\boldsymbol\lambda} & = - \hat{\mathbf{A}}^T \boldsymbol{\lambda} - \hat{\mathbf{Q}} \mathbf{x} \\
\end{aligned}$$

**Riccati equation for $\boldsymbol\lambda$.**

$$-\hat{\mathbf{A}}^T \mathbf{P} \mathbf{x} - \hat{\mathbf{Q}} \mathbf{x} = \dot{\mathbf{P}} \mathbf{x} + \mathbf{P} \hat{\mathbf{A}} \mathbf{x} - \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} \mathbf{x} \ . $$

For arbitrary $\mathbf{x}$, Riccati equation follows

$$\begin{aligned}
\mathbf{0} 
 & = \dot{\mathbf{P}} + \mathbf{P} \hat{\mathbf{A}} + \hat{\mathbf{A}}^T \mathbf{P} + \hat{\mathbf{Q}} - \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} = \\
 & = \dot{\mathbf{P}} + \mathbf{P} \left( \mathbf{A} - \mathbf{B} \mathbf{R}^{-1} \mathbf{S}^T \right) + \left( \mathbf{A} - \mathbf{B} \mathbf{R}^{-1} \mathbf{S}^T \right)^T \mathbf{P} + \left( \mathbf{Q} - \mathbf{S} \mathbf{R}^{-1} \mathbf{S}^T \right) - \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} \ .
\end{aligned}$$

**Lyapunov equation for $\boldsymbol\lambda$.** Replacing $\mathbf{K} = \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P}$,

$$\begin{aligned}
 \mathbf{0} 
  & = \dot{\mathbf{P}} + \mathbf{P} \mathbf{A} - \mathbf{K}^T \mathbf{S}^T + \mathbf{S} \mathbf{R}^{-1} \mathbf{S}^T + \mathbf{A}^T \mathbf{P} - \mathbf{S} \mathbf{K} + \mathbf{S} \mathbf{R}^{-1} \mathbf{S}^T + \mathbf{Q} - \mathbf{S} \mathbf{R}^{-1} \mathbf{S}^T - \left( \mathbf{K} - \mathbf{R}^{-1} \mathbf{S}^T \right)^T \mathbf{R} \left( \mathbf{K} - \mathbf{R}^{-1} \mathbf{S}^T \right) = \\
  & = \dot{\mathbf{P}} + \mathbf{P} \mathbf{A} + \mathbf{A}^T \mathbf{P} + \mathbf{Q} + \mathbf{S}\mathbf{R}^{-1} \mathbf{S} - \mathbf{S} \mathbf{K} - \mathbf{K}^T \mathbf{S}^T - \mathbf{K}^T \mathbf{R} \mathbf{K} + \mathbf{S} \mathbf{R}^{-1} \mathbf{R} \mathbf{K} + \mathbf{K}^T \mathbf{R} \mathbf{R}^{-1} \mathbf{S}^T - \mathbf{S} \mathbf{R}^{-1} \mathbf{R} \mathbf{R}^{-1} \mathbf{S}^T = \\
  & = \dot{\mathbf{P}} + \mathbf{P} \mathbf{A} + \mathbf{A}^T \mathbf{P} + \mathbf{Q} - \mathbf{K}^T \mathbf{R} \mathbf{K} \ .
\end{aligned}$$

```


```{dropdown} ...
:open:

$$\partial_t \hat{\boldsymbol\Phi}(t,\tau) = \hat{\mathbf{A}}(t)  \hat{\boldsymbol\Phi}(t,\tau) \ .$$

<!--
$$\partial_T \mathbf{P}$$
-->

```



