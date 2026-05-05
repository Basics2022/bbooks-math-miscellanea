(control:optimal:observer:stochastic)=
# Optimal observer for stochastic Gaussian disturbance

Non-Gaussian disturbances can be obtained as the output of [shape filters](system-theroy:shape-filter) with Gaussian inputs.

From the equations of the plant

$$\begin{cases}
 \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} + \mathbf{B}_d \mathbf{d} \\
 \mathbf{y}       = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} + \mathbf{D}_d \mathbf{d} + \mathbf{D}_r \mathbf{r}
\end{cases}$$

and the observer

$$\begin{cases}
 \dot{\mathbf{o}} = \mathbf{A} \mathbf{o} + \mathbf{B} \mathbf{u} + \mathbf{L} \left( \mathbf{y} - \mathbf{y}_o \right) \\
 \mathbf{y}_o     = \mathbf{C} \mathbf{o} + \mathbf{D} \mathbf{u} 
\end{cases}$$

the dynamical equation of the error, $\mathbf{e} = \mathbf{o} - \mathbf{x}$, follows

$$\begin{aligned}
  \dot{\mathbf{e}} 
  & = \dot{\mathbf{o}} - \dot{\mathbf{x}} = \\
  & = \mathbf{A} \mathbf{o} + \mathbf{B} \mathbf{u} + \mathbf{L} \left[ \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} + \mathbf{D}_d \mathbf{d} + \mathbf{D}_r \mathbf{r} - \mathbf{C} \mathbf{o} - \mathbf{D} \mathbf{u} \right] - \mathbf{A} \mathbf{x} - \mathbf{B} \mathbf{u} - \mathbf{B}_d \mathbf{d} = \\
  & = \left( \mathbf{A} - \mathbf{L} \mathbf{C} \right) \mathbf{e} + \left( \mathbf{L} \mathbf{D}_d - \mathbf{B}_d \right) \mathbf{d} + \mathbf{L} \mathbf{D}_r \mathbf{r} = \\
  & = \overline{\mathbf{A}} \mathbf{e} + \begin{bmatrix} \ \overline{\mathbf{B}}_d & \overline{\mathbf{B}}_r \end{bmatrix} \begin{bmatrix} \mathbf{d} \\ \mathbf{r} \end{bmatrix}  = \\
  & = \overline{\mathbf{A}} \mathbf{e} + \overline{\mathbf{B}} \begin{bmatrix} \mathbf{d} \\ \mathbf{r} \end{bmatrix} \ .
\end{aligned}$$

Let the distrubances be a white noise, then the [Lyapunov equation for the autocorrelation matrix of the state](ode:linear:miscellanea:stochastic-response:correlation-matrix:lyapunov) reads

$$\dot{\mathbf{R}}_{\mathbf{e}\mathbf{e}} = \overline{\mathbf{A}}(\mathbf{L}) \mathbf{R}_{\mathbf{e}\mathbf{e}} + \mathbf{R}_{\mathbf{e}\mathbf{e}} \overline{\mathbf{A}}^T(\mathbf{L}) + \overline{\mathbf{B}}(\mathbf{L}) \mathbf{W} \overline{\mathbf{B}}^T (\mathbf{L})\ ,$$

with $\mathbf{W}$ the matrix of the cross-correlations of the white noise distrubances,

$$\mathbf{W} = \begin{bmatrix}
\mathbf{W}_{\mathbf{d}\mathbf{d}} & \mathbf{W}_{\mathbf{d}\mathbf{r}} \\
\mathbf{W}_{\mathbf{r}\mathbf{d}} & \mathbf{W}_{\mathbf{r}\mathbf{r}}
\end{bmatrix} \ .
$$

If stationary conditions are reached, the autocorrelation matrix of the error must satisfy the algebraic version of the Lyapunov equation

$$\mathbf{0} = \overline{\mathbf{A}} (\mathbf{L})\mathbf{R}_{\mathbf{e}\mathbf{e}} + \mathbf{R}_{\mathbf{e}\mathbf{e}} \overline{\mathbf{A}}^T (\mathbf{L})+ \overline{\mathbf{B}}(\mathbf{L}) \mathbf{W} \overline{\mathbf{B}}^T(\mathbf{L}) \ .$$ (eq:observer:error:lyapunov:algebraic)

**Optimal observer.** The optimal observer is defined as the observer that makes the estimation error minimum. As an example, the error can be measured as the weighted trace of the auto-correlation of the error. The constrained optimization problem reads

$$\min_{\mathbf{L}} \text{Tr}\left( \mathbf{W}_{\mathbf{e}} \mathbf{R}_{\mathbf{e}\mathbf{e}} \right) \ ,$$

subject to Lyapunov equation as a constraint.

```{dropdown} Details of the constrained optimization
:open:

The optimal solution is found, setting equal to zero the derivatives of the objective function

$$\widetilde{J} = \text{Tr}\left( \mathbf{W}_{\mathbf{e}} \mathbf{R}_{\mathbf{e}\mathbf{e}} + \boldsymbol\Lambda\left\{ (\mathbf{A} - \mathbf{L}\mathbf{C}) \mathbf{R} + \mathbf{R} ( \mathbf{A} - \mathbf{L} \mathbf{C} )^T + \begin{bmatrix} \mathbf{L} \mathbf{D}_d - \mathbf{B}_d & \mathbf{L} \mathbf{D}_r \end{bmatrix} \mathbf{W} \begin{bmatrix} \mathbf{D}_d^T \mathbf{L}^T - \mathbf{B}_d^T \\ \mathbf{D}_r^T  \mathbf{L}^T \end{bmatrix}  \right\} \right) \ ,$$

w.r.t. the matrices $\mathbf{L}$, $\boldsymbol\Lambda$, $\mathbf{R}$

$$\begin{aligned}
 \mathbf{0} & = \frac{\partial \widetilde{J}}{\partial \mathbf{R}} = \mathbf{W}_{\mathbf{e}}^T + (\mathbf{A} - \mathbf{L}\mathbf{C})^T \boldsymbol\Lambda^T + (\mathbf{A}-\mathbf{L}\mathbf{C})\boldsymbol\Lambda^T \\
 \mathbf{0} & = \frac{\partial \widetilde{J}}{\partial \boldsymbol\Lambda} = \text{algebraic Lyapunov equation for $\mathbf{R}_{\mathbf{e}\mathbf{e}}$} \\
 \mathbf{0} & = \frac{\partial \widetilde{J}}{\partial \mathbf{L}} = - ( \mathbf{C} \mathbf{R} \boldsymbol\Lambda )^T - \boldsymbol\Lambda \mathbf{R} \mathbf{C}^T + \\
  & \qquad \qquad + \boldsymbol\Lambda^T \mathbf{L} \left( \mathbf{D}_d \mathbf{W}_{dd} \mathbf{D}^T_d \right)^T + \boldsymbol\Lambda \mathbf{L} \left( \mathbf{D}_d \mathbf{W}_{dd} \mathbf{D}^T_d \right) + \\
  & \qquad \qquad + \boldsymbol\Lambda^T \mathbf{L} \left( \mathbf{D}_r \mathbf{W}_{rr} \mathbf{D}^T_r \right)^T + \boldsymbol\Lambda \mathbf{L} \left( \mathbf{D}_r \mathbf{W}_{rr} \mathbf{D}^T_r \right) + \\
  & \qquad \qquad + \boldsymbol\Lambda^T \mathbf{L} \left( \mathbf{D}_r \mathbf{W}_{rd} \mathbf{D}^T_d \right)^T + \boldsymbol\Lambda \mathbf{L} \left( \mathbf{D}_r \mathbf{W}_{rd} \mathbf{D}^T_d \right) + \\
  & \qquad \qquad + \boldsymbol\Lambda^T \mathbf{L} \left( \mathbf{D}_d \mathbf{W}_{dr} \mathbf{D}^T_r \right)^T + \boldsymbol\Lambda \mathbf{L} \left( \mathbf{D}_d \mathbf{W}_{dr} \mathbf{D}^T_r \right) + \\
  & \qquad \qquad - \boldsymbol\Lambda \mathbf{B}_d \mathbf{W}_{dd} \mathbf{D}_d^T - \boldsymbol\Lambda^T \mathbf{B}_d \mathbf{W}_{dd} \mathbf{D}_d^T + \\
  & \qquad \qquad - \boldsymbol\Lambda \mathbf{B}_d \mathbf{W}_{dr} \mathbf{D}_r^T - \boldsymbol\Lambda \mathbf{B}_d \mathbf{W}_{dr} \mathbf{D}_r^T
\end{aligned}$$

Collecing the symmetric (**todo** why this assumption?) matrix $\boldsymbol\Lambda$ (is it possible to collect this matrix and set the other factor to zero?)

$$\mathbf{L} = \left[ \mathbf{R}_{\mathbf{e}\mathbf{e}} \mathbf{C}^T + \mathbf{B}_d \left( \mathbf{W}_{dd} \mathbf{D}_d^T + \mathbf{W}_{dr} \mathbf{D}_r^T \right) \right] \left[ 
  \mathbf{D}_d \mathbf{W}_{dd} \mathbf{D}^T_d +
  \mathbf{D}_d \mathbf{W}_{dr} \mathbf{D}^T_r +
  \mathbf{D}_r \mathbf{W}_{rd} \mathbf{D}^T_d +
  \mathbf{D}_r \mathbf{W}_{rr} \mathbf{D}^T_r
\right]^{-1} \ ,$$ (eq:observer:gauss:L)

Replacing the expression {eq}`eq:observer:gauss:L` of the $\mathbf{L}$ matrix into the algebraic Lyapunov equation {eq}`eq:observer:error:lyapunov:algebraic` for the autocorrelation $\mathbf{R}_{\mathbf{e}\mathbf{e}}$, a Riccati equation in $\mathbf{R}_{\mathbf{e} \mathbf{e}}$ appears.


```

```{dropdown} Derivatives w.r.t. a matrix
:open:

$$\frac{\partial \text{Tr}(\mathbf{A} \mathbf{B})}{\partial \mathbf{A}} = \frac{\partial \text{Tr}(\mathbf{A} \mathbf{B})}{\partial A_{ij}} = \dfrac{\partial ( A_{ab} B_{ba} )}{\partial A_{ij}} = \delta_{ai} \delta_{bj} B_{ba} = B_{ji} = \mathbf{B}^T$$

$$\frac{\partial \text{Tr}(\mathbf{A} \mathbf{B})}{\partial \mathbf{B}} = \frac{\partial \text{Tr}(\mathbf{A} \mathbf{B})}{\partial B_{ij}} = \dfrac{\partial ( A_{ab} B_{ba} )}{\partial B_{ij}} = A_{ab} \delta_{ib} \delta_{aj} = A_{ji} = \mathbf{A}^T$$

$$\frac{\partial \text{Tr}(\mathbf{A} \mathbf{B}^T)}{\partial \mathbf{B}} = \frac{\partial \text{Tr}(\mathbf{A} \mathbf{B})}{\partial B_{ij}} = \dfrac{\partial ( A_{ab} B_{ab} )}{\partial B_{ij}} = A_{ab} \delta_{ia} \delta_{bj} = A_{ij} = \mathbf{A}$$

$$\frac{\partial \text{Tr}(\mathbf{A} \mathbf{B} \mathbf{A}^T)}{\partial \mathbf{A}} = \frac{\partial \text{Tr}(\mathbf{A} \mathbf{B} \mathbf{A}^T)}{\partial A_{ij}} = \dfrac{\partial ( A_{ab} B_{bc} A_{ac} )}{\partial A_{ij}} = B_{jc} A_{ic} + A_{ib} B_{bj} = \mathbf{A} \mathbf{B}^T + \mathbf{A} \mathbf{B} \ .$$

$$\frac{\partial \text{Tr}(\mathbf{A} \mathbf{B} \mathbf{C})}{\partial \mathbf{B}} = \frac{\partial \text{Tr}(\mathbf{A} \mathbf{B} \mathbf{C})}{\partial B_{ij}} = \dfrac{\partial ( A_{ab} B_{bc} C_{ca} )}{\partial B_{ij}} = A_{ai} C_{ja} = \mathbf{A}^T \mathbf{C}^T \ .$$

$$\frac{\partial \text{Tr}(\mathbf{C} \mathbf{A} \mathbf{B} \mathbf{A}^T)}{\partial \mathbf{A}} = \frac{\partial \text{Tr}(\mathbf{C} \mathbf{A} \mathbf{B} \mathbf{A}^T)}{\partial A_{ij}} = \dfrac{\partial ( C_{ab} A_{bc} B_{cd} A_{ad} )}{\partial A_{ij}} = C_{ai} B_{jd} A_{ad} + C_{ib} A_{bc} B_{cj} = \mathbf{C}^T \mathbf{A} \mathbf{B}^T + \mathbf{C} \mathbf{A} \mathbf{B} \ .$$

$$\text{Tr}(\mathbf{A} \mathbf{B}) = A_{ij} B_{ji} = \text{Tr}( \mathbf{B} \mathbf{A} )$$


```

