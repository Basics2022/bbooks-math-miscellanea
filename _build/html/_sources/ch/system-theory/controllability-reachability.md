(controllability-reachability)=
# Reachability and Controllability

(controllability-reachability:time-continuous)=
## Time-continuous linear systems

The solution of the linear system

$$\begin{aligned}
  \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
       \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} \\
\end{aligned}$$

with initial conditions $\mathbf{x}(0) = \mathbf{x}_0$ reads

$$\mathbf{x}(t) = \boldsymbol\Phi(t,t_0) \mathbf{x}_0 + \int_{\tau=0}^{t} \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau \ ,$$

### Reachability

A state $\mathbf{x}_1$ is reachable if there's a control input $\mathbf{u}(t)$ that can move the system from the initial state $\mathbf{x}_0 = \mathbf{0}$ to the final state $\mathbf{x}_1$ in finite time.


### Controllability

A state $\mathbf{x}_0$ is reachable if there's a control input $\mathbf{u}(t)$ that can move the system from the initial state $\mathbf{x}_0$ to the final state $\mathbf{x}_1 = \mathbf{0}$ in finite time.


```{dropdown} Optimal input and controllability Gramian 
:open:

Let's solve the optimal input defined as the one with the minimal cost $\frac{1}{2}\int_{\tau=0}^{t_1} \left| \mathbf{u}(\tau) \right|^2$, subject to the equations of motion as constraints. **todo** Here the final time $t_1$ is assumed to be known, but in general it's not: include $t_1$ in the optimization, or run several optimizations to find optimal $t_1^*$.

The cost function of the constrained problem reads

$$\widetilde{J}(\mathbf{u};\boldsymbol\lambda) = \frac{1}{2} \int_{\tau=0}^{t_1} \mathbf{u}^T(\tau) \mathbf{u}(\tau) d \tau + \boldsymbol\lambda^T \left( \mathbf{x}_1 - \int_{\tau=0}^{t_1} \boldsymbol\Phi(t_1,\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau \right) \ .$$

Variation w.r.t. $\boldsymbol\lambda$ gives the solution of the equation, i.e. the constraints. Variation w.r.t. the control $\mathbf{u}(\tau)$ gives the optimal control as a function of $\boldsymbol\lambda$

$$\mathbf{u}(\tau) = \mathbf{B}^T(\tau) \boldsymbol\Phi^T(t_1,\tau) \boldsymbol\lambda \ .$$

Replacing this expression in the solution of the dynamical system, an expression of $\boldsymbol\lambda$ in terms of the final state $\mathbf{x}_1$ follows,

$$\mathbf{x}_1 = \int_{\tau=0}^{t_1} \boldsymbol\Phi(t_1,\tau) \mathbf{B}(\tau) \mathbf{B}^T(\tau)\boldsymbol\Phi^T(t_1,\tau) d \tau \boldsymbol\lambda = \mathbf{W}_c(t_1) \boldsymbol\lambda \ ,$$

having introduced the definition of the **controllability Gramian**, $\mathbf{W}_c(t_1)$.

* If $\mathbf{x}_1 \in R(\mathbf{W}_c(t_1))$ is in the range of the controllability Gramian, at least a value of the Lagrange multiplier $\boldsymbol\lambda$ that satisfies the relation - and thus a control driving the system from $\mathbf{0}$ to $\mathbf{x}_1$ - exists.

* If the controllability Gramian is full-rank, it's invertible, the solution of the problem is unique and reads

   $$\boldsymbol\lambda = \mathbf{W}_c^{-1}(t_1) \mathbf{x}_1 \ ,$$

   and the cost of the control is

   $$J = \frac{1}{2} \mathbf{x}_1^T \mathbf{W}_c^{-1} \int_{\tau=0}^{t_1} \boldsymbol\Phi(t_1,\tau) \mathbf{B}(\tau) \mathbf{B}^T(\tau)\boldsymbol\Phi^T(t_1,\tau) d \tau \mathbf{W}_c^{-1} \mathbf{x}_1 = \frac{1}{2} \mathbf{x}_1^T \mathbf{W}_c^{-1} \mathbf{x}_1 \ .$$

* In general, using singular value decomposition of the Gramian $\mathbf{W}_c = \mathbf{U} \boldsymbol\Sigma \mathbf{U}^*$ (as the Gramian is symmetric, $\mathbf{V} = \mathbf{U}$)
  
    $$\mathbf{u}_{\mathbf{x}_1} = \boldsymbol\Sigma \mathbf{u}_{\boldsymbol\lambda} \ ,$$

    with $\mathbf{u}_{\mathbf{v}} := \mathbf{U}^* \mathbf{v}$, the projection of the vector $\mathbf{v}$ onto the unit orthogonal base of $\mathbb{R}^n$. A solution $\mathbf{u}_{\boldsymbol\lambda}$ exists if zero singular values $\sigma_i = 0$ correspond to null projection of the vector $\mathbf{x}_1$ onto the $i^{th}$ vector of the base $\mathbf{u}_i^* \mathbf{x}_1 = \left\{ \mathbf{u}_{\mathbf{x}_1} \right\}_i = 0$. Otherwise a solution of the equation does not exist: in this situation, there's no control law driving the system into $\mathbf{x}_1$, an error in the final state exists, and the problem can be formulated as a optimization problem weighting both the control and the error (resulting in a least square solution of a linear system with no solution?).

```

```{prf:definition} Controllability Gramian
:label: def:controllability-gramian

$$
\mathbf{W}_c(t,t_0) := \int_{\tau=t_0}^{t} \boldsymbol\Phi(\tau,t_0) \mathbf{B}(\tau) \mathbf{B}^T(\tau) \boldsymbol\Phi^T(\tau,t_0) d \tau
$$ (eq:controllability-gramian:def)

```

Controllability Gramian satisfies the [Lyapunov equation](lyapunov-eq)

$$
 \dot{\mathbf{W}}_c(t) = \mathbf{B}(t) \mathbf{B}^T(t) + \mathbf{A}(t) \mathbf{W}_c(t) + \mathbf{W}_c(t) \mathbf{A}^T(t) \ ,
$$

with initial conditions $\mathbf{W}_c(0) = \mathbf{0}$, as the integral vanishes with the same values of the lower and upper extremes of integration.

```{dropdown} Lyapunov equation for the controllability Graminan
:open:

$$\begin{aligned}
 \frac{d}{dt} \mathbf{W}_c(t)
 & = \frac{d}{dt} \int_{\tau=0}^{t} \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{B}^T(\tau)\boldsymbol\Phi^T(t,\tau) d \tau = \\
 & = \mathbf{B}(t) \mathbf{B}^T(t) + \int_{\tau=0}^{t} \partial_t \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{B}^T(\tau)\boldsymbol\Phi^T(t,\tau) d \tau + \int_{\tau=0}^{t} \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{B}^T(\tau) \partial_t \boldsymbol\Phi^T(t,\tau) d \tau = \\
 & = \mathbf{B}(t) \mathbf{B}^T(t) + \mathbf{A}(t) \mathbf{W}_c(t) + \mathbf{W}_c(t) \mathbf{A}^T(t) \ ,
\end{aligned}$$

as $\boldsymbol\Phi(t,t) = \mathbf{I}$, and $\partial_t \boldsymbol\Phi(t,\tau) = \mathbf{A}(t) \boldsymbol\Phi(t,\tau)$.


```

```{dropdown} Controllability for LTI systems
:open:

For LTI systems $\boldsymbol\Phi(t,t_0) = e^{\mathbf{A}(t-t_0)}$. The controllability Gramian becomes

$$\mathbf{W}_c(t) = \int_{\tau=0}^{t} e^{\mathbf{A} (t-\tau)} \mathbf{B} \mathbf{B}^T e^{\mathbf{A}^T (t-\tau)} d \tau$$

A vector $\mathbf{v}$ belongs to the null space of $\left( e^{\mathbf{A}t} \mathbf{B} \right)^T$ if

$$0 = \mathbf{v}^T e^{\mathbf{A}t} \mathbf{B} \ .$$

Using the definition of the exponential matrix $e^{\mathbf{A}t} := \sum_{n=0}^{+\infty} \frac{\mathbf{A}^n t^n}{n!}$, it follows 

$$0 = \mathbf{v}^T \sum_{n=0}^{+\infty} \frac{\mathbf{A}^n t^n}{n!} \mathbf{B}$$

Thus..., a vector $\mathbf{v}$ is in the null-space of $\mathbf{W}_c$ (symmetric! Be precise and use [orthogonality between range and kernel of the adjoint](math:linear-algebra:thms:RAperpKAh) if it's orthogonal to the columns of the matrix

$$\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{A} \mathbf{B} & \dots & \mathbf{A}^{n-1} \mathbf{B} \end{bmatrix} \ ,$$

i.e. $\mathbf{v}^T \mathcal{C} = \mathbf{0}$. If the column space of matrix $\mathcal{C}$ spans $\mathbb{R}^n$, then the system is fully controllable.

```

**Obs.** If $\mathbf{v}^T \mathbf{A}^n \mathbf{B}$ for $n = 0:N-1$, thus it holds for all the integer exponent $n \ge N$, as a consequence of the [Cayley-Hamilton theorem](cayley-hamilton), i.e. $\mathbf{A}^n$ can be written as a linear combination of the powers $\mathbf{A}^k$, $k = 0:n-1$.


(controllability-reachability:time-discrete)=
## Time-discrete linear systems


