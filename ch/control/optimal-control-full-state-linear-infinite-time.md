(control:optimal:full-state-fb:linear:infinite-time-horizon)=
# Linear system without exogenous inputs - infinite time horizon

In the infinite-time horizon, under the assumption of stabilizability and observability (**todo** Prove it!), the optimal control law for a LTI system is a proportional control law,

$$\mathbf{u} = - \mathbf{K} \mathbf{x} = - \mathbf{R}^{-1} ( \mathbf{B}^T \mathbf{P} + \mathbf{S}^T ) \mathbf{x} \ ,$$

with the constant matrix $\mathbf{P}$ satisfying the **algebraic Riccation equation (ARE)**

$$\mathbf{0} = \mathbf{P} \hat{\mathbf{A}} + \hat{\mathbf{A}}^T \mathbf{P} + \hat{\mathbf{Q}} - \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} \ ,$$ (eq:optimal:infinite-time:p-are)

with $\hat{\mathbf{A}} = \mathbf{A} - \mathbf{B} \mathbf{R}^{-1} \mathbf{S}^T$ and $\hat{\mathbf{Q}} = \mathbf{Q} - \mathbf{S} \mathbf{R}^{-1} \mathbf{S}^T$. 

Introducing the relation $\boldsymbol\lambda(t) = \mathbf{P} \mathbf{x}(t)$ - with constant $\mathbf{P}$ - into the Hamiltonian system

$$
\begin{bmatrix} \dot{\mathbf{x}} \\ \dot{\boldsymbol\lambda} \end{bmatrix}
\begin{bmatrix}
  \mathbf{A} - \mathbf{B} \widetilde{\mathbf{R}}^{-1} \mathbf{S}^T & - \mathbf{B} \widetilde{\mathbf{R}}^{-1} \mathbf{B}^T \\
  -\widetilde{\mathbf{Q}} + \mathbf{S} \widetilde{\mathbf{R}}^{-1} \mathbf{S}^T & - \mathbf{A}^T + \mathbf{S} \widetilde{\mathbf{R}}^{-1} \mathbf{B}^T
\end{bmatrix}
\begin{bmatrix}      \mathbf{x}  \\      \boldsymbol\lambda  \end{bmatrix} \ ,
$$

it's possible to get 2 "decoupled" (the coupling lies in the relation $\boldsymbol\lambda = \mathbf{P} \mathbf{x}$) equations for $\mathbf{x}$ and $\boldsymbol\lambda$,

$$\begin{aligned}
  \dot{\mathbf{x}} & = \left( \hat{\mathbf{A}} - \mathbf{B} \widetilde{\mathbf{R}}^{-1} \mathbf{B}^T \mathbf{P} \right) \mathbf{x} \\
  \dot{\boldsymbol{\lambda}} & = - \left( \hat{\mathbf{A}}^T + \hat{\mathbf{Q}} \mathbf{P}^{-1} \right) \boldsymbol\lambda \ . 
\end{aligned}$$

If the matrix $\mathbf{P}$ is chosen as the solution of the ARE {eq}`eq:optimal:infinite-time:p-are`, then the two equations have opposite eigenvalues, as

$$\begin{aligned}
  \hat{\mathbf{A}}^T + \hat{\mathbf{Q}} \mathbf{P}^{-1}
  & = \left( \hat{\mathbf{A}}^T \mathbf{P} + \hat{\mathbf{Q}} \right) \mathbf{P}^{-1} = \\
  & = \left( - \mathbf{P} \hat{\mathbf{A}} + \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} \right) \mathbf{P}^{-1} = \\
  & = - \mathbf{P} \left(  \hat{\mathbf{A}} - \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} \right) \mathbf{P}^{-1} \ ,
\end{aligned}$$

the two matrices are related by a similarity transformation, through $\mathbf{P}$, with a minus sign.

Thus, the transition matrix of the state and the co-state in the closed-loop systems are dual, in the sense of

$$\boldsymbol\Phi_{cl,x}(t,t_0) = \boldsymbol\Phi_{cl,\lambda}^T(t_0,t) \ .$$

**Lyapunov criterium for stability.** Let $V(x) = \mathbf{x}^T \mathbf{P} \mathbf{x}$, its time derivative reads

$$\begin{aligned}
  \dot{V}(x(t)) 
  & = \dot{\mathbf{x}}^T \mathbf{P} \mathbf{x} + \mathbf{x}^T \mathbf{P} \dot{\mathbf{x}} = \\
  & = \mathbf{x}^T ( \hat{\mathbf{A}} - \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} )^T \mathbf{P} \mathbf{x} + \mathbf{x}^T \mathbf{P} ( \hat{\mathbf{A}} - \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} ) \mathbf{x} = \\
  & = \mathbf{x}^T ( \hat{\mathbf{A}}^T \mathbf{P} + \mathbf{P} \hat{\mathbf{A}} - 2 \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} ) \mathbf{x} = \\
  & = - \mathbf{x}^T ( \hat{\mathbf{Q}} + \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} ) \mathbf{x} = \\
  & \le 0 \ ,
\end{aligned}$$

for all $\mathbf{x} \ne \mathbf{0}$, if the matrix $\hat{\mathbf{Q}} + \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P}$ is a positive definite matrix.

```{dropdown} Asymptotic stability and detectability of $\ (\hat{\mathbf{A}}, \hat{\mathbf{Q}}^{1/2})$
:open:

For asymptotic stability, we require the pair $(\hat{A}, \hat{Q}^{1/2})$ to be detectable (see [observability and detectability](observability-detectability). Here is the proof logic:

* define the null space: suppose there exists a trajectory $x(t)$ such that $\dot{V}(x(t)) = 0$ for all $t \geq 0$.

* analyze the terms: Since both $\hat{Q}$ and $PBR^{-1}B^TP$ are positive semi-definite, $\dot{V} = 0$ implies that $x^T \hat{Q} x = 0$ and $x^T PBR^{-1}B^TP x = 0$ simultaneously.

* vanishing control: If $x^T PBR^{-1}B^TP x = 0$, then the optimal control input $u = -R^{-1}B^T P x$ must be zero, as 

   $$0 = \mathbf{x}^T \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{R} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} \mathbf{x} = \mathbf{u}^T \mathbf{R} \mathbf{u} \ ,$$

   forces $\mathbf{u} = \mathbf{0}$, as the weight matrix on the control must be positive definite, $\mathbf{R} > 0$ (update the condition for mixed weights, and/or weights on performance outputs with $\widetilde{\mathbf{R}}$).

* the residual dynamics: in this "unobservable" region where $\dot{V}=0$, the dynamics simplify to $\dot{x} = \hat{A} x$.

* the constraint: for $\dot{V}$ to remain zero, we also require $\mathbf{x}^T \hat{\mathbf{Q}} \mathbf{x} = 0$, and with $\hat{\mathbf{Q}}^{1/2}$ as the [Choleski factor](math:cholesky) of the semi-definite positive matrix, $\hat{\mathbf{Q}}^{1/2} \mathbf{x}(t) = 0$ for all $t$.

All the statements above can be then summarized as the condition of detectability of a linear system

$$\left\{\begin{aligned}
  \dot{\mathbf{x}} & = \hat{\mathbf{A}} \mathbf{x} \\
       \mathbf{y}  & = \hat{\mathbf{Q}}^{1/2} \mathbf{x} \\
\end{aligned}\right.$$


```


**Schur decoposition.**

$$\mathbf{U}^T \mathbf{H} \mathbf{U} = \mathbf{T} = \begin{bmatrix} \mathbf{T}_{11} & \mathbf{T}_{12} \\ \mathbf{0} & \mathbf{T}_{22} \end{bmatrix}$$


