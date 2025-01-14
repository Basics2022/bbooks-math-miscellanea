(complex:fourier)=
# Fourier Transforms

- Fourier series: continuous time, periodic function in time
- Fourier transform: continuous time, non-periodic function in time
- Discrete Fourier transform (DFT):
- Discrete time Fourier transform (DTFT):


(complex:fourier:fs)=
## Fourier Series

For a $T$-periodic function,

$$g(t) $$



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

**Proof.**

<!--
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

$$\varphi(t):= e^{-\pi|t|^2}$$

$$
\mathscr{F}\{ \varphi(t) \} 
 = \int_{t=-\infty}^{+\infty} \varphi(t) e^{-i \omega t} \, dt 
 = \int_{t=-\infty}^{+\infty} e^{-\pi|t|^2} e^{-i \omega t} \, dt 
 = 2 \int_{t=0}^{+\infty} e^{-\pi t^2} e^{-i \omega t} \, dt 
 = \dots
 = 2 e^{-\frac{\omega^2}{4 \pi}} = 2 e^{-\pi f^2} \ .
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
-->

<!--
    The Fourier transform of the convolution $\varphi_{\varepsilon} \ast f$ reads
    
    $$\mathscr{F}\left\{ \varphi_\varepsilon \ast f \right\} = \mathscr{F}\left\{ \varphi_\varepsilon \right\} \mathscr{F}\left\{ f \right\} = \frac{1}{\varepsilon} \varepsilon 2 e^{-\frac{\varepsilon^2 \omega^2}{4 \pi}} F(\omega)$$
-->
