(complex:laplace)=
# Laplace Transform

$$\mathscr{L}\left\{ f(t) \right\}(s) := \int_{t=0^-}^{+\infty} e^{-st} f(t) \, dt = F(s) \ .$$

## Inverse transform
$$f(t) = \mathscr{L}^{-1}\left\{ F(s) \right\} = \dots$$

## Properties
**Linearity.**

$$\mathscr{L}\{ a f(t) + b g(t) \}(s) = a F(s) + b G(s)$$

**[Dirac delta](functional-analysis:dirac-delta).**

$$\mathscr{L}\left\{ \delta(t) \right\} = \int_{t=0^-}^{+\infty} \delta(t) \, e^{st} \, dt = 1 $$

**Time delay.** If $f(t) = 0$ for $t < 0$ ("causality"), for $\tau > 0$,

$$\mathscr{L}\{ f(t-\tau) \}(s) = e^{-s \tau} F(s)$$

Proof readily follows direct computation with change of variable $z = t - \tau$, $dt = dz$

$$\mathscr{L}\{ f(t - \tau) \}(s) = \int_{t=0^-}^{+\infty} f(t-\tau) e^{-s t} \, dt = \int_{z = - \tau}^{+\infty} f(z) e^{-s z } \, dz \, e^{-s \tau} = \int_{z = 0}^{+\infty} f(z) e^{-s z } \, dz \, e^{-s \tau} = e^{-s \tau} F(s) \ . $$

**"Frequency shift"**

$$\mathscr{L}\{ f(t) e^{a t} \}(s) = F(s-a)$$

Direct computation gives

$$\mathscr{L}\{ f(t) e^{a t} \}(s) = \int_{t=0^-}^{+\infty} f(t) e^{a t} e^{-st} \, dt =  \int_{t=0^-}^{+\infty} f(t) e^{-(s-a)t} \, dt = F(s-a)$$

**Derivative.**

$$\mathscr{L}\{ f'(t) \}(s) = s F(s) - f(0^-) \ .$$

Proof readily follows direct computation, with integration by parts

$$\mathscr{L}\{ f'(t) \}(s) = \int_{t=0^-}^{+\infty} f'(t) e^{-s t} \, dt = \left[ f(t) e^{-s t} \right]|_{t = 0^-}^{+\infty} + s \int_{t=0^-}^{+\infty} f(t) e^{-s t} \, dt = s F(s) - f(0^-) \ ,$$

provided that $\lim_{s \rightarrow +\infty} f(t) e^{-s t} = 0$.

**Integral.**

$$\mathscr{L}\left\{ \int_{\tau=0}^{t} f(\tau) \, d \tau \right\}(s) = \frac{1}{s} F(s) \ .$$

Proof readily follows direct computation, with integration by parts

$$\mathscr{L}\left\{ \int_{\tau=0^-}^{t} f(\tau) \, d \tau \right\}(s) = \int_{t=0^-}^{+\infty} \int_{\tau=0^-}^{t} f(\tau) \, d \tau e^{-s t} \, dt = \left[ -\frac{e^{-st}}{s} \int_{\tau=0^-}^{t} f(\tau) \, d\tau \right]_{t=0}^{+\infty} + \frac{1}{s} \int_{t=0}^{+\infty} f(t) e^{-s t} \, dt = \frac{1}{s} F(s) \ ,$$ 

provided that $\int_{\tau=0^-}^{0} f(\tau) d \tau = 0$ and $\lim_{t \rightarrow +\infty}\frac{e^{-st}}{s} \int_{\tau=0^-}^{+\infty} f(\tau) \, d \tau = 0$.

**Convolution.**

$$\begin{aligned}
  \mathscr{L}\left\{ f(t) \ast g(t) \right\} 
  & = \int_{t=0^-}^{+\infty} \int_{\tau=-\infty}^{+\infty} f(t-\tau) g(\tau) \, d \tau \, e^{-s t }\, dt = && (1) \\
  & = \int_{\tau=-\infty}^{+\infty} \int_{z=-\tau^-}^{+\infty} f(z) g(\tau) \, e^{-s (z + \tau)}\, d\tau \, dz = (2) \\
  & = \int_{z=0^-}^{+\infty} f(z) \, e^{-s z }\, dz \int_{\tau=0^-}^{+\infty} g(\tau) e^{-s \tau} = \\
  & = \mathscr{L}\{ f(t) \}(s) \, \mathscr{L}\{ g(t) \} (s) \ .
\end{aligned}$$ (laplace:convolution)

having performed the change of coordinates $z = t - \tau$, $\tau = \tau$, with unitary Jacobian, 

$$\frac{\partial(t,\tau)}{\partial(z,\tau)} = \partial_z t \partial_{\tau} \tau - \partial_z \tau \partial_z t =  1 \cdot 1 - 1 \cdot 0 = 1 ,$$

given the proper description of the domain of integration summarised in the extremes of integration in (1), and causality - i.e. all the functions $f(t)$ are identically zero for $t < 0$ - in (2).

**Initial value.** If ...

$$f(0^+) = \lim_{s \rightarrow + \infty} s F(s)$$

From direct computation,

$$\begin{aligned}
 \lim_{s \rightarrow +\infty} s F(s)
 & = \lim_{s \rightarrow +\infty} s \int_{t = 0^-}^{+\infty} f(t) \, e^{-st} \, dt = \\
 & = \lim_{s\rightarrow + \infty} \left\{ \left[s \left(-\frac{e^{-st}}{s}\right)f(t) \right]\bigg|_{t=0}^{+\infty} + \int_{t=0}^{+\infty} e^{-st} f'(t) \, dt \right\} = \\
 & = \lim_{s \rightarrow +\infty} \left\{ \left[-e^{-st} f(t) \right]\bigg|_{t=0}^{+\infty} + \int_{t=0}^{+\infty} e^{-st} f'(t) \, dt \right\} = \\
 & = f(0) \ ,
\end{aligned}$$

provided that $\lim_{s \rightarrow +\infty} \lim_{t \rightarrow +\infty} e^{-s t} f(t) = 0$ and $\lim_{s \rightarrow + \infty} \int_{t=0}^{+\infty} e^{-st} f'(t) \, dt = 0$.

**Final value.** If ...

$$f(+\infty) = \lim_{s \rightarrow 0} s F(s)$$

From direct computation (**todo** *check and/or explain proof*),

$$\begin{aligned}
 \lim_{s \rightarrow 0} s F(s)
 & = \lim_{s \rightarrow 0} s \int_{t = 0^-}^{+\infty} f(t) \, e^{-st} \, dt = \\
 & = \lim_{s \rightarrow 0} \left\{ \left[s \left(-\frac{e^{-st}}{s}\right)f(t) \right]\bigg|_{t=0}^{+\infty} + \int_{t=0}^{+\infty} e^{-st} f'(t) \, dt \right\} = \\
 & = \lim_{s \rightarrow 0} \left\{ \left[-e^{-st} f(t) \right]\bigg|_{t=0}^{+\infty} + \int_{t=0}^{+\infty} e^{-st} f'(t) \, dt \right\} = \\
 & = f(0) + f(+\infty) - f(0) = f(+\infty) \ ,
\end{aligned}$$

provided that $\lim_{s \rightarrow 0} \lim_{t \rightarrow +\infty} e^{-s t} f(t) = 0$.
