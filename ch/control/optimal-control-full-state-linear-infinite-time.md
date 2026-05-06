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

the two matrices are related by a similarity transformation, through $\mathbf{P}$.

