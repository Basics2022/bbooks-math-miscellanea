(control:optimal:observer)=
# Optimal observer for deterministic disturbances

$$\begin{cases}
 \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} + \mathbf{B}_d \mathbf{d} \\
 \mathbf{y}       = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} + \mathbf{D}_d \mathbf{d} + \mathbf{D}_r \mathbf{r}
\end{cases}$$

$$\begin{cases}
 \dot{\mathbf{o}} = \mathbf{A} \mathbf{o} + \mathbf{B} \mathbf{u} + \mathbf{L} \left( \mathbf{y} - \mathbf{y}_o \right) \\
 \mathbf{y}_o     = \mathbf{C} \mathbf{o} + \mathbf{D} \mathbf{u} 
\end{cases}$$

The error is defined as $\mathbf{e} := \mathbf{o} - \mathbf{x}$, and it's governed by the dynamical equation

$$\dot{\mathbf{e}} = \left( \mathbf{A} - \mathbf{L} \mathbf{C} \right) \mathbf{e} + \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right)  \mathbf{d} - \mathbf{L} \mathbf{D}_r \mathbf{r} \ .$$

This equation shows that the dynamics is asymptotically stable if the matrix $\mathbf{A} - \mathbf{L} \mathbf{C}$ is asymptotically stable. The matrix $\mathbf{L}$ is involved in the dynamics from the exogenous input $\mathbf{d}$ and measurement error $\mathbf{r}$. The design of $\mathbf{L}$ is driven by some requiremenets:
* asymptotic stability of $\mathbf{A} - \mathbf{L}\mathbf{C}$,
* low sensitivity to exogenous input and measurement error.
