(control:optimal:margins)=
# Phase and gain margin of optimal control

Some results are available for phase and gain margin of optimal control, on the input side. **todo** *discuss*
The relationship between the actual input to the plant $u$ and an additive input error $\Delta u$ reads

$$u = \Delta u + u_c = \Delta u + K e = \Delta u + K (x_{ref} - x) = \Delta u + K x_{ref} + K H u \ ,$$

for a SISO or

$$\mathbf{u} = \left[ \mathbf{I} + \mathbf{K}(s) \mathbf{H}(s) \right]^{-1} \Delta\mathbf{u} + \left[ \mathbf{I} + \mathbf{K}(s) \mathbf{H}(s) \right]^{-1} \mathbf{K}(s) \mathbf{x}_{ref} \ ,$$

for a MIMO system. The additive input error $\Delta u$ can be thought as the difference between the ideal/design condition, due to un-modelled parts, failures, and any other form of discrepancy to the model altering the gain and the phase (adding delay) of the ideal control $u_c$.


:::{figure} ./../../media/control/optimal-control-margin-1.png
:alt: Block diagram for the optimal control margins
:align: center
:name: fig-optimal-control-margin-block

Block diagram of optimal control closed-loop system with retroaction on the error $e = x_{ref} - x$ on the full state. 

:::

```{dropdown} Details

For a SISO system, the relation between $u$ and $\Delta u$ reads

$$u = \Delta u + u_c = \Delta u + K e = \Delta u + K (x_{ref} - x) = \Delta u + K x_{ref} + K H u \ ,$$

and thus

$$u = \frac{1}{1+K H} \Delta u + \frac{K}{1 + K H} x_{ref} \ .$$

For a MIMO systems, TFs are matrix TFs and thus matrix inversion is required (as the division between matrix makes no sense at all),

$$\mathbf{u} = \left[ \mathbf{I} + \mathbf{K}(s) \mathbf{H}(s) \right]^{-1} \Delta\mathbf{u} + \left[ \mathbf{I} + \mathbf{K}(s) \mathbf{H}(s) \right]^{-1} \mathbf{K}(s) \mathbf{x}_{ref} \ .$$

```

(control:optimal:margins:siso)=
## SISO

```{dropdown} Details
:open:

Starting from the algebraic Lyapunov equation for the matrix $\mathbf{P}$

$$\mathbf{0} = \mathbf{A}^T \mathbf{P} + \mathbf{P} \mathbf{A} - \mathbf{K} \mathbf{R} \mathbf{K}^T + \mathbf{Q} \ ,$$

with the optimal matrix of gains, $\mathbf{K} = \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P}$. Adding and subtracting $s \mathbf{I} \mathbf{P}$, and defining the matrix $\mathbf{G}(s) = ( s \mathbf{I} - \mathbf{A} )^{-1}$,

$$\begin{aligned}
  \mathbf{0}
  & = \mathbf{A}^T \mathbf{P} + \mathbf{P} \mathbf{A} - \mathbf{K} \mathbf{R} \mathbf{K}^T + \mathbf{Q} = \\
  & = ( \mathbf{A} + s \mathbf{I} )^T \mathbf{P} + \mathbf{P} ( \mathbf{A} - s \mathbf{I} ) - \mathbf{K} \mathbf{R} \mathbf{K}^T + \mathbf{Q} = \\
  & = \mathbf{G}^{-T}(-s) \mathbf{P} + \mathbf{P} \mathbf{G}^{-1}(s) - \mathbf{K} \mathbf{R} \mathbf{K}^T + \mathbf{Q} \ .
\end{aligned}$$

Pre-multiplication by $\mathbf{B}^T \mathbf{G}^T(-s)$ and post-multiplication by $\mathbf{G}(s) \mathbf{B}$ gives

$$\begin{aligned}
  \mathbf{0}
  & = - \mathbf{B}^T \mathbf{P} \mathbf{G}(s) \mathbf{B} - \mathbf{B}^T \mathbf{G}^T(-s) \mathbf{P} \mathbf{B} - \mathbf{B}^T \mathbf{G}^{T}(-s) \mathbf{K} \mathbf{R} \mathbf{K}^T \mathbf{G}(s) \mathbf{B} + \mathbf{B}^T \mathbf{G}^{T}(-s) \mathbf{Q} \mathbf{G}(s) \mathbf{B} = \\
  & = - \mathbf{K} \mathbf{R} \mathbf{G}(s) \mathbf{B} - \mathbf{B}^T \mathbf{G}^T(-s) \mathbf{R} \mathbf{K}^T - \mathbf{B}^T \mathbf{G}^{T}(-s) \mathbf{K} \mathbf{R} \mathbf{K}^T \mathbf{G}(s) \mathbf{B} + \mathbf{B}^T \mathbf{G}^{T}(-s) \mathbf{Q} \mathbf{G}(s) \mathbf{B} = \\
  & = - \mathbf{K} \mathbf{R} \mathbf{H}(s) - \mathbf{H}^T(-s) \mathbf{R} \mathbf{K}^T - \mathbf{H}^{T}(-s) \mathbf{K} \mathbf{R} \mathbf{K}^T \mathbf{H}(s) + \mathbf{H}^{T}(-s) \mathbf{Q} \mathbf{H}(s) = \\
\end{aligned}$$

having used the expression of the optimal gain matrix to write $\mathbf{B}^T \mathbf{P} = \mathbf{K} \mathbf{R}$.

```


(control:optimal:margins:siso)=
## MIMO




