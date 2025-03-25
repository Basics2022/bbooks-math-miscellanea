(complex:fourier)=
# Fourier Transforms

- Fourier series: continuous time, periodic function in time
- Fourier transform: continuous time, non-periodic function in time
- Discrete Fourier transform (DFT):
- Discrete time Fourier transform (DTFT):


(complex:fourier:fs)=
## Fourier Series

For a $T$-periodic function,

$$g(t) \sim \frac{a_0}{2} + \sum_{n=1}^{+\infty} \left[ a_n \, \cos\left( n \frac{2\pi}{T} t \right) + b_n \, \sin\left( n \frac{2 \pi }{T} t \right) \right] \ ,$$

**todo** Prove it with properties of integrals of $\sin$ and $\cos$ over $t \in \left[ 0, T \right]$; prove convergence to average value at jumps

The exponential form reads

$$g(t) \sim \sum_{n=-\infty}^{+\infty} c_n e^{i n \frac{2 \pi }{T}t} \ ,$$ (eq:fourier-series:exp)

where 

$$c_n = \frac{1}{T} \int_{t=0}^{T} f(t) \, e^{-i n \frac{2\pi}{T} t} \ .$$ (eq:fourier-series:exp:coeff)

```{dropdown} Proof

Exploiting the properties of integrals of complex exponentials with $k \in \mathbb{Z}$

$$\int_{t=0}^{T} e^{i k \frac{2 \pi}{T} t} \, dt = 
\begin{cases}
\frac{1}{i k \frac{2 \pi}{T}} \left.\left[ e^{ik \frac{2\pi}{T} t} \right]\right|_{t=0}^{T} = 0 \hfill \qquad \text{if $ k \ne 0$} \\
T \hfill \text{if $ k = 0$}
\end{cases}
$$

$$\int_{t=0}^{T} f(t) e^{-i m \frac{2 \pi}{T} t} \, dt
 \sim \int_{t=0}^{T} \sum_{n=-\infty}^{+\infty} c_n e^{i n \frac{2 \pi }{T}t}  e^{-i m \frac{2 \pi}{T} t}
 \sim \sum_{n=-\infty}^{+\infty} c_n \sim \int_{t=0}^{T} e^{i (n-m) \frac{2 \pi }{T}t} 
 \sim T \, c_m \ .
$$
```


(complex:fourier:ft)=
## Fourier Transform

$$\mathscr{F}\left\{ g(t) \right\}(f) := \int_{t = -\infty}^{+\infty} g(t) \, e^{-i 2 \pi f t} \, dt .$$


### Properties

**Linearity.**

**[Dirac delta](functional-analysis:dirac-delta).**

$$\mathscr{L}\left\{ \delta(t) \right\} = \int_{t=-\infty}^{+\infty} \delta(t) \, e^{-i 2 \pi f t} \, dt = 1 $$

**Time delay.**

**Derivative.**

**Integral.**

**Initial value.**

**Final value.**

### Inverse Fourier Transform

$$\mathscr{F}^{-1}\left\{ G(f) \right\}(t) := \int_{f = -\infty}^{+\infty} G(f) \, e^{i 2 \pi f t} \, df .$$

**Proof using Dirac's delta expression.**

$$\begin{aligned}
\mathscr{F}^{-1}\left\{ G(f) \right\}(t) := \int_{f = -\infty}^{+\infty} G(f) \, e^{i 2 \pi f t} \, df 
  & = \int_{f = -\infty}^{+\infty} \int_{\tau=-\infty}^{+\infty} g(\tau) e^{-i 2 \pi f \tau} \, e^{i 2 \pi f t} \, df = \\ 
  & = \int_{f = -\infty}^{+\infty} \int_{\tau=-\infty}^{+\infty} g(\tau) e^{-i 2 \pi f \tau} \, e^{i 2 \pi f t} \, df = \\ 
  & = \int_{f = -\infty}^{+\infty} \int_{\tau=-\infty}^{+\infty} g(\tau) e^{i 2 \pi f (t-\tau)} \, df = \\ 
  & = \int_{\tau=-\infty}^{+\infty} g(\tau) \delta(t-\tau) \, d\tau = g(t) \ . 
\end{aligned}$$

**Proof.** By the *dominated convergence theorem*, it follows that

$$\begin{aligned}
  \int_{\mathbb{R}} e^{i 2 \pi x \xi} F(\xi) \, d \xi
  & = \lim_{\varepsilon \rightarrow 0} \int_{\mathbb{R}} \underbrace{e^{-\pi \varepsilon^2 \xi^2 + i 2 \pi x \xi}}_{G(\xi;x,\varepsilon)} F(\xi) \, d \xi = \\
  & = \lim_{\varepsilon \rightarrow 0} \int_{\mathbb{R}} g(y;x,\varepsilon) f(y) \, dy = \\
  & = \lim_{\varepsilon \rightarrow 0} \int_{\mathbb{R}} \varphi_{\varepsilon}(x-y) \, f(y) \, dy = \\
  & = \int_{\mathbb{R}} \delta(x-y) \, f(y) \, dy = f(x)
\end{aligned}$$

**Lemma 1.** The Fourier transform of function $\varphi(t):= e^{-\pi|t|^2}$ reads

$$\begin{aligned}
\mathscr{F}\{ \varphi(t) \}(\omega) 
 & = \int_{t=-\infty}^{+\infty} \varphi(t) e^{-i \omega t} \, dt = \\ 
 & = \int_{t=-\infty}^{+\infty} e^{-\pi|t|^2} e^{-i \omega t} \, dt = \\
 & = \int_{t=-\infty}^{+\infty} e^{-\pi \left( t^2 + i \frac{\omega}{\pi} t - \frac{\omega^2}{4 \pi^2}  \right)} \, dt \, e^{- \frac{\omega^2}{4 \pi^2}} = \\
 & = \int_{t=-\infty}^{+\infty} e^{-\pi \left( t + i \frac{\omega}{2 \pi}  \right)^2} \, dt \, e^{- \frac{\omega^2}{4 \pi}} = \\
 & = e^{- \frac{\omega^2}{4 \pi}} \ ,
\end{aligned}$$

having evaluated [the integral $\int_{-\infty}^{+\infty} e^{-\alpha x^2}$](integral:e^x2) with $\alpha = \pi$. **todo** *justify the result for complex exponential. Use Bromwich contour integrals*

**Lemma 2.** Fourier transform of $f(\alpha t)$, $\alpha > 0$

$$\mathscr{F}\{ f(\alpha t) \}(\omega) = \int_{\mathbb{R}} f(\alpha t) e^{-j\omega t} \, dt = \int_{\tau \in \mathbb{R}} f(\tau) e^{-j \frac{\omega}{\alpha} \tau} \, d\tau \frac{1}{\alpha} = \frac{1}{\alpha} F\left(\frac{\omega}{\alpha} \right) $$

**Lemma 3.** $\frac{1}{\varepsilon} \varphi\left(\frac{t}{\varepsilon} \right) \rightarrow \delta(x)$ for $\varepsilon \rightarrow 0$

$$\mathscr{F}\left\{\frac{1}{\varepsilon}\varphi\left(\frac{t}{\varepsilon} \right) \right\}(\omega) = \frac{1}{\varepsilon} \varepsilon e^{-\frac{\omega^2}{4 \pi \varepsilon^2}} = e^{-\frac{\omega^2}{4 \pi \varepsilon^2}}$$

0. Fourier transform

$$G(f) = \int_{t=-\infty}^{\infty} e^{-i \omega t} g(t) \, dt$$

1. 

$$g(t) = e^{i \alpha t} \psi(t)$$

$$\mathscr{F}\{ g(t) \}(\omega) = \int_{t=-\infty}^{+\infty} g(t) e^{-i \omega t} \, dt = \int_{t=-\infty}^{+\infty} \psi(t) e^{i \alpha t} e^{-i \omega t} \, dt =  \int_{t=-\infty}^{+\infty} \psi(t) e^{-i (\omega-\alpha) t} \, dt = \mathscr{F}\{ \psi(t) \}(\omega-\alpha) \ .$$

2. 

$$\psi(t) = \phi(\alpha t)$$

$$
\mathscr{F}\{ \psi(t) \} 
 = \int_{t=-\infty}^{+\infty} \psi(t) e^{-i \omega t} \, dt 
 = \int_{t=-\infty}^{+\infty} \phi(\alpha t) e^{-i \omega t} \, dt 
 = \int_{\tau = -\infty}^{+\infty} \phi(\tau) e^{-i \frac{\omega}{\alpha} \tau} \, \frac{d \tau}{\alpha} 
 = \frac{1}{\alpha} \mathscr{F}\{ \phi(t) \}\left( \frac{\omega}{\alpha} \right) \ .
$$

3. Fubini's theorem

4. 

$$\varphi(t):= e^{-\pi t^2}$$

$$
\mathscr{F}\{ \varphi(t) \} 
 = \int_{t=-\infty}^{+\infty} \varphi(t) e^{-i \omega t} \, dt 
 = \int_{t=-\infty}^{+\infty} e^{-\pi t^2} e^{-i \omega t} \, dt 
$$

$$0 = \oint_{\gamma} e^{-\alpha |z|^2} \, dz = \int_{\dots} \dots$$

$$z = R e^{i \theta}, \quad dz = i R e^{i \theta} d \theta$$
$$\int_{C/4} e^{-\alpha |z|^2} \, dz = \int_{\theta=0}^{\frac{\pi}{2}} e^{-\alpha R^2} i R e^{i\theta} d \theta = i R e^{-\alpha R^2 } \frac{e^{-i \theta}}{i}|_{\theta= 0}^{\frac{\pi}{2}}$$

$$\begin{aligned}
  \int_{t=0}^{+\infty} e^{-\pi t^2} e^{-i \omega t} \, dt 
  & = \int_{t=0}^{+\infty} e^{-\left( \pi t^2 + i \omega t - \frac{\omega^2}{4 \pi} \right)} \, dt \, e^{-\frac{\omega^2}{4 \pi}} = \\
  & = \int_{t=0}^{+\infty} e^{-\pi \left( t + i \frac{\omega}{2 \pi} \right)^2} \, dt \, e^{-\frac{\omega^2}{4 \pi}} \\
\end{aligned}$$


5. $\varphi_{\varepsilon}(t) = \frac{1}{\varepsilon^n} \varphi\left( \frac{t}{\varepsilon} \right)$, $t \in \mathbb{R}^n$, is an approximation of Dirac's delta for $\varepsilon \rightarrow 0$, so that

    $$\begin{aligned}
      & \lim_{\varepsilon \rightarrow 0} \int_{t = -\infty}^{+\infty} \varphi_{\varepsilon}(t- \tau) f(t) \, dt = f(\tau) \\
      & \lim_{\varepsilon \rightarrow 0} \int_{t = -\infty}^{+\infty} \varphi_{\varepsilon}(t) \, dt = 1 \\
    \end{aligned}$$
   
    As the Fourier transform $\mathscr{F}\left\{\varphi_{\varepsilon}(t)\right\}(\omega) \rightarrow 1$ for $\varepsilon \rightarrow 0$, then $\varphi_{\varepsilon}(t) \rightarrow \delta(t)$.
<!--
    The Fourier transform of the convolution $\varphi_{\varepsilon} \ast f$ reads
    
    $$\mathscr{F}\left\{ \varphi_\varepsilon \ast f \right\} = \mathscr{F}\left\{ \varphi_\varepsilon \right\} \mathscr{F}\left\{ f \right\} = \frac{1}{\varepsilon} \varepsilon 2 e^{-\frac{\varepsilon^2 \omega^2}{4 \pi}} F(\omega)$$
-->
