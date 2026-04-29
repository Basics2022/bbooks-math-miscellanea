(control:closed-loop:requirements-performance:siso:ref-tracking)=
# Reference tracking (SISO)

Setting $\mathbf{F} = \mathbf{I}$ in {numref}`fig-closed-loop-tfs`, and neglecting disturbances, the transfer functions between the output and the reference and between the tracking error and the reference signal are

$$\begin{aligned}
  E(s) & = \frac{1}{1 + G(s) R(s)} Y_{\text{ref}}(s) \\
  Y(s) & = \frac{G(s)R(s)}{1 + G(s) R(s)} Y_{\text{ref}}(s) \\
\end{aligned}$$

**Polynomial forcing.** 

```{dropdown} Laplace transform of polynomial signals
:open:

Laplace transform of (casual) polynomial signals immediately follows from the transform of a Dirac's delta and the property of the Laplace transform of the integral of a function,

$$\mathscr{L}\left\{ \int_{\tau=0}^{t} f(\tau) \, d \tau \right\} = \frac{F(s)}{s} \ , $$

being $F(s)$ the Laplace transform of function $f(t)$. Indeed, a ramp can be interpreted as the integral of a Dirac's delta, a casual parabolic signal is the integral of the ramp, and so on.

**Dirac's delta.** 

$$F_{-1} := F_{\delta} = \mathscr{L} \{ \delta(t) \} = \int_{t = 0^-}^{+\infty} \delta(t) e^{-st} dt  = 1 \ . $$

**Step.** Step is the integral of the Dirac's delta.

$$F_0 := F_{\text{step}} = \mathscr{L} \{ 1 \} = \frac{1}{s} \ .$$

**Ramp.** Step is the integral of the Dirac's delta.

$$F_1 := F_{\text{ramp}} = \mathscr{L} \{ t \} = \frac{1}{s^2} \ .$$

**Signal $t^n$, $n \in \mathbb{N}$.** 

$$\mathscr{L} \left\{ t^n \right\} = \frac{1}{s^{n+1}} \ .$$

```

**Limit of the tracking error of polynomial forcing, for $t \rightarrow +\infty$.**
Assuming the system is stable, the free-response to initial condition vanishes. Using **final value** property of Laplace transform (see [Laplace transform definition and properties](complex:laplace:def-thm)),

$$\lim_{t \rightarrow + \infty} e(t) = \lim_{s \rightarrow 0} s E(s) \ .$$

Let the open-loop transfer function $L(s) = G(s) R(s)$ be $L(s) = \frac{N(s)}{s^p D(s)}$, having explicitly written the integrators (the factors $\frac{1}{s}$ in the denominator of the TF), so that $D(0) \ne 0$, $N(s) \ne 0$. For casual systems $|N| \le p + |D|$. The closed-loop function reads

$$\frac{1}{1 + L(s)} = \frac{s^p D(s)}{ s^p D(s) + N(s) } \ .$$

Let $Y_{\text{ref}}(s) = C_0 + \frac{C_1}{s} + \dots + \frac{C_{m+1}}{s^{m+1}}$ the Laplace transform of a $m$-degree polynomial reference, the limit value of the tracking error reads

$$\begin{aligned}
  \lim_{t \rightarrow + \infty} e(t) 
  & = \lim_{s \rightarrow 0} s E(s) = \\
  & = \lim_{s \rightarrow 0} \frac{ s^{p+1} D(s) }{ s^p D(s) + N(s) } \left( C_0 + \frac{C_1}{s} + \dots + \frac{C_{m+1}}{s^{m+1}} \right) = \\
  & = \lim_{s \rightarrow 0} \frac{ s^{p-m} D(s) }{ s^p D(s) + N(s) } \left( s^{m+1}C_0 + s^m C_1 + \dots + C_{m+1} \right) = \\
  & = \left\{
  \begin{aligned}
    & 0                 && \ , \qquad p > m \\
    & \frac{D(0)}{N(0)} && \ , \qquad p = m \\
    & +\infty           && \ , \qquad p < m \\
  \end{aligned} \right.
\end{aligned}$$



**Type of the system.**
