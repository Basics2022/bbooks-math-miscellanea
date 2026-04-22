(control:optimal:margins)=
# Phase and gain margin of optimal control

Some results are available for phase and gain margin of optimal control, on the input side. **todo** *discuss*
The relationship between the actual input to the plant $u$ and an additive input error $\Delta u$ reads

$$u = \Delta u + u_c = \Delta u + K e = \Delta u + K (x_{ref} - x) = \Delta u + K x_{ref} + K H u \ ,$$

$$u = \frac{1}{1 + K H(s)} \Delta u(s) + \frac{K}{1 + KH(s)} x_{ref}(s) \ ,$$ (eq:optimal:input:siso:tfs)

for a SISO or

$$\mathbf{u} = \left[ \mathbf{I} + \mathbf{K}(s) \mathbf{H}(s) \right]^{-1} \Delta\mathbf{u} + \left[ \mathbf{I} + \mathbf{K}(s) \mathbf{H}(s) \right]^{-1} \mathbf{K}(s) \mathbf{x}_{ref} \ ,$$ (eq:optimal:input:mimo:tfs)

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

$$u(s) = \frac{1}{1+K H(s)} \Delta u(s) + \frac{K}{1 + K H(s)} x_{ref}(s) \ .$$

For a MIMO systems, TFs are matrix TFs and thus matrix inversion is required (as the division between matrix makes no sense at all),

$$\mathbf{u}(s) = \left[ \mathbf{I} + \mathbf{K} \mathbf{H}(s) \right]^{-1} \Delta\mathbf{u}(s) + \left[ \mathbf{I} + \mathbf{K} \mathbf{H}(s) \right]^{-1} \mathbf{K} \mathbf{x}_{ref}(s) \ .$$

```

(control:optimal:margins:siso)=
## SISO


$$\left| 1 + S(j\omega) \right|^2 \ge 1 \ .$$

```{dropdown} Details

Starting from the algebraic Lyapunov equation for the matrix $\mathbf{P}$

$$\mathbf{0} = \mathbf{A}^T \mathbf{P} + \mathbf{P} \mathbf{A} - \mathbf{K} \mathbf{R} \mathbf{K}^T + \mathbf{Q} \ ,$$

with the optimal matrix of gains, $\mathbf{K} = \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P}$. Adding and subtracting $s \mathbf{I} \mathbf{P}$, and defining the matrix $\mathbf{G}(s) = ( s \mathbf{I} - \mathbf{A} )^{-1}$,

$$\begin{aligned}
  \mathbf{0}
  & = \mathbf{A}^T \mathbf{P} + \mathbf{P} \mathbf{A} - \mathbf{K}^T \mathbf{R} \mathbf{K} + \mathbf{Q} = \\
  & = ( \mathbf{A} + s \mathbf{I} )^T \mathbf{P} + \mathbf{P} ( \mathbf{A} - s \mathbf{I} ) - \mathbf{K}^T \mathbf{R} \mathbf{K} + \mathbf{Q} = \\
  & = \mathbf{G}^{-T}(-s) \mathbf{P} + \mathbf{P} \mathbf{G}^{-1}(s) - \mathbf{K}^T \mathbf{R} \mathbf{K} + \mathbf{Q} \ .
\end{aligned}$$

Pre-multiplication by $\mathbf{B}^T \mathbf{G}^T(-s)$ and post-multiplication by $\mathbf{G}(s) \mathbf{B}$ gives

$$\begin{aligned}
  \mathbf{0}
  & = - \mathbf{B}^T \mathbf{P} \mathbf{G}(s) \mathbf{B} - \mathbf{B}^T \mathbf{G}^T(-s) \mathbf{P} \mathbf{B} - \mathbf{B}^T \mathbf{G}^{T}(-s) \mathbf{K}^T \mathbf{R} \mathbf{K} \mathbf{G}(s) \mathbf{B} + \mathbf{B}^T \mathbf{G}^{T}(-s) \mathbf{Q} \mathbf{G}(s) \mathbf{B} = \\
  & = - \mathbf{R} \mathbf{K} \mathbf{G}(s) \mathbf{B} - \mathbf{B}^T \mathbf{G}^T(-s) \mathbf{K}^T \mathbf{R} - \mathbf{B}^T \mathbf{G}^{T}(-s) \mathbf{K}^T \mathbf{R} \mathbf{K} \mathbf{G}(s) \mathbf{B} + \mathbf{B}^T \mathbf{G}^{T}(-s) \mathbf{Q} \mathbf{G}(s) \mathbf{B} = \\
  & = - \mathbf{R} \mathbf{K} \mathbf{H}(s) - \mathbf{H}^T(-s) \mathbf{K}^T \mathbf{R} - \mathbf{H}^{T}(-s) \mathbf{K}^T \mathbf{R} \mathbf{K} \mathbf{H}(s) + \mathbf{H}^{T}(-s) \mathbf{Q} \mathbf{H}(s) \ ,
\end{aligned}$$

having used the expression of the optimal gain matrix to write $\mathbf{B}^T \mathbf{P} = \mathbf{R} \mathbf{K}$, and defined the open-loop *input* TF matrix $\mathbf{S}(s) := \mathbf{K} \mathbf{H}(s)$. Moving terms with or without $\mathbf{S}(s)$ on two different sides of the equality, and adding \mathbf{R}, and collecting terms, it follows

$$\left[ \mathbf{I} + \mathbf{S}^T(-s) \right] \mathbf{R} \left[ \mathbf{I} + \mathbf{S}(s) \right] = \mathbf{R} + \mathbf{H}^{T}(-s) \mathbf{Q} \mathbf{H}(s) \ .$$

Moving to Fourier domain, $s = j \omega$, and recalling that $\mathbf{S}^T(-j\omega) = \mathbf{S}^*( j \omega ) $,

$$\left[ \mathbf{I} + \mathbf{S}^*(j \omega) \right] \mathbf{R} \left[ \mathbf{I} + \mathbf{S}(j \omega) \right] = \mathbf{R} + \mathbf{H}^*(j\omega) \mathbf{Q} \mathbf{H}(j\omega) \ .$$

**todo** *Notation for semi-definite positive symmetric matrices*

$$\left[ \mathbf{I} + \mathbf{S}^*(j \omega) \right] \mathbf{R} \left[ \mathbf{I} + \mathbf{S}(j \omega) \right] \ge \mathbf{R} \ .$$

For a 1-dimensional state SISO system, $\mathbf{R} = r$, $\mathbf{S}(s) = S(s)$, and thus

$$\left| 1 + S(j\omega) \right|^2 \ge 1 \ .$$



```


(control:optimal:margins:mimo)=
## MIMO

$$\left[ \mathbf{I} + \mathbf{S}^*(j \omega) \right] \mathbf{R} \left[ \mathbf{I} + \mathbf{S}(j \omega) \right] \ge \mathbf{R} \ .$$

with $\mathbf{H}(s) = (s \mathbf{I} - \mathbf{A})^{-1} \mathbf{B}$, and $\mathbf{S}(s) = \mathbf{K} \mathbf{H}(s)$ the open-loop TF between $\Delta \mathbf{u}$ and the ideal control loop $\mathbf{u}_c$, and $\mathbf{I} + \mathbf{S}(s)$ the (inverse of the) transfer function between $\Delta \mathbf{u}$ and $\mathbf{u}$, as shown in {eq}`eq:optimal:input:mimo:tfs`.


