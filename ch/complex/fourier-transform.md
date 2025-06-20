(complex:fourier:transform)=
# Fourier Transform

**Contents**: [definition](complex:fourier:transform:def); [properties](complex:fourier:transform:properties); [inverse transform](complex:fourier:transform:inverse); [Plancherel's theorem](complex:fourier:transform:plancherel); [uncertainty relation](complex:fourier:transform:uncertainty)

(complex:fourier:transform:def)=
## Definition

...

$$\mathscr{F}\left\{ g(t) \right\}(f) := \int_{t = -\infty}^{+\infty} g(t) \, e^{-i 2 \pi f t} \, dt .$$


(complex:fourier:transform:properties)=
## Properties


**Linearity**

**[Dirac delta](functional-analysis:dirac-delta).**

$$\mathscr{L}\left\{ \delta(t) \right\} = \int_{t=-\infty}^{+\infty} \delta(t) \, e^{-i 2 \pi f t} \, dt = 1 $$ (eq:complex:fourier:transform:properties:delta)

**Time delay.**

**Derivative.**

**Integral.**

**Initial value.**

**Final value.**

```{prf:property} Transform of convolution
:label: transform:fourier:convolution

$$\mathscr{F}\left\{ a \ast b (t)  \right\}(f) = \mathscr{F}\left\{ a(t) \right\}(f) \, \mathscr{F}\left\{ b(t) \right\}(f)$$


```
```{dropdown} Proof.

$$\begin{aligned}
  \mathscr{F}\left\{ a \ast b (t)  \right\}(f)
  & = \int_{t = -\infty}^{+\infty} \int_{\tau=-\infty}^{+\infty} a(\tau) b(t - \tau) \, d \tau \, e^{-i 2 \pi f t} \, d t = && (1) \\
  & = \int_{\tau=-\infty}^{+\infty} a(\tau) \, e^{-i 2 \pi f \tau} \, d \tau \, \int_{z = -\infty}^{+\infty} b(z) \, e^{-i 2 \pi f z} = \\
  & = \mathscr{F}\{ a(t) \}(f) \, \mathscr{F}\{ b(t) \} (f) \ ,
\end{aligned}$$

having used $(1)$ transformation of coordinates $(z, \tau) = (t - \tau, \tau)$ with unit Jacobian

$$\dfrac{\partial(z, \tau)}{\partial(t, \tau)} = \left|\begin{matrix} 1 & - 1 \\ 0 & 1 \end{matrix}\right| = 1 \ .$$

```


(complex:fourier:transform:inverse)=
## Inverse Fourier Transform

Under the assumptions ...**todo**, the inverse Fourier transform reads

$$\mathscr{F}^{-1}\left\{ G(f) \right\}(t) := \int_{f = -\infty}^{+\infty} G(f) \, e^{i 2 \pi f t} \, df .$$

```{dropdown} Proof using Dirac's delta expression.

$$\begin{aligned}
\mathscr{F}^{-1}\left\{ G(f) \right\}(t) := \int_{f = -\infty}^{+\infty} G(f) \, e^{i 2 \pi f t} \, df 
  & = \int_{f = -\infty}^{+\infty} \int_{\tau=-\infty}^{+\infty} g(\tau) e^{-i 2 \pi f \tau} \, e^{i 2 \pi f t} \, df = \\ 
  & = \int_{f = -\infty}^{+\infty} \int_{\tau=-\infty}^{+\infty} g(\tau) e^{-i 2 \pi f \tau} \, e^{i 2 \pi f t} \, df = \\ 
  & = \int_{f = -\infty}^{+\infty} \int_{\tau=-\infty}^{+\infty} g(\tau) e^{i 2 \pi f (t-\tau)} \, df = \\ 
  & = \int_{\tau=-\infty}^{+\infty} g(\tau) \delta(t-\tau) \, d\tau = g(t) \ . 
\end{aligned}$$

```

```{dropdown} Proof using dominated convergence theorem and Fubini's lemma.
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

```

<!--
    The Fourier transform of the convolution $\varphi_{\varepsilon} \ast f$ reads
    
    $$\mathscr{F}\left\{ \varphi_\varepsilon \ast f \right\} = \mathscr{F}\left\{ \varphi_\varepsilon \right\} \mathscr{F}\left\{ f \right\} = \frac{1}{\varepsilon} \varepsilon 2 e^{-\frac{\varepsilon^2 \omega^2}{4 \pi}} F(\omega)$$
-->

(complex:fourier:transform:plancherel)=
## Plancherel's theorem

...assumptions...**todo**

$$\int_{f=-\infty}^{+\infty} |G(f)|^2 \, df = \int_{t=-\infty}^{+\infty} |g(t)|^2 \, dt $$ (eq:fourier:transform:plancherel:magnitude)

and

$$\int_{f=-\infty}^{+\infty} A^*(f) \, G(f)\, df = \int_{t=-\infty}^{+\infty} a^*(t) \, g(t) \, dt \ .$$ (eq:fourier:transform:plancherel)

```{dropdown} Proof of Plancherel's thm for the magnitude

$$\begin{aligned}
\int_{f=-\infty}^{+\infty} |G(f)|^2 \, df 
& = \int_{f=-\infty}^{+\infty} G(f)^* G(f) \, df =  \\
& = \int_{f=-\infty}^{+\infty} \left( \int_{t_1=-\infty}^{+\infty} g(t_1) e^{-i 2 \pi f t_1} dt_1 \right)^* \left( \int_{t_2=-\infty}^{+\infty} g(t_2) e^{-i 2 \pi f t_2} dt_2  \right) \, df =  \\
& =  \int_{t_1, t_2=-\infty}^{+\infty} g^*(t_1) \, g(t_2) \, \int_{f=-\infty}^{+\infty} e^{i 2 \pi f ( t_1 - t_2 )} \, df \, dt_1 \, dt_2 =  && (1) \\
& =  \int_{t_1, t_2=-\infty}^{+\infty} g^*(t_1) \, g(t_2) \, \delta( t_1 - t_2 ) \, dt_1 \, dt_2 = && (2) \\
& =  \int_{t_1=-\infty}^{+\infty} g^*(t_1) \, g(t_1) \, dt_1 = && (3) \\
& =  \int_{t_1=-\infty}^{+\infty} |g(t_1)|^2 \, dt_1 \ .
\end{aligned}$$

having used (1) the approximation {eq}`eq:dirac:fourier-transform` of Dirac's delta, and (2) property {eq}`dirac-delta:prop-2` of Dirac's delta, and (3) the expression of the absolute value of complex functions $g^*(t_1) g(t_1) = |g(t_1)|^2$.

```


```{dropdown} Proof of Plancherel's thm for the product of functions

$$\begin{aligned}
\int_{f=-\infty}^{+\infty} A^*(f) \, G(f) \, df 
& = \int_{f=-\infty}^{+\infty} G(f)^* G(f) \, df =  \\
& = \int_{f=-\infty}^{+\infty} \left( \int_{t_1=-\infty}^{+\infty} a(t_1) e^{-i 2 \pi f t_1} dt_1 \right)^* \left( \int_{t_2=-\infty}^{+\infty} g(t_2) e^{-i 2 \pi f t_2} dt_2  \right) \, df =  \\
& =  \int_{t_1, t_2=-\infty}^{+\infty} a^*(t_1) \, g(t_2) \, \int_{f=-\infty}^{+\infty} e^{i 2 \pi f ( t_1 - t_2 )} \, df \, dt_1 \, dt_2 =  && (1) \\
& =  \int_{t_1, t_2=-\infty}^{+\infty} a^*(t_1) \, g(t_2) \, \delta( t_1 - t_2 ) \, dt_1 \, dt_2 = && (2) \\
& =  \int_{t_1=-\infty}^{+\infty} a^*(t_1) \, g(t_1) \, dt_1 \ .
\end{aligned}$$

having used (1) the approximation {eq}`eq:dirac:fourier-transform` of Dirac's delta, and (2) property {eq}`dirac-delta:prop-2` of Dirac's delta.

```
(complex:fourier:transform:uncertainty)=
## Uncertainty relation

An uncertainty relation holds linking standard deviations of a probability density function in time domain and a probability density function built with its Fourier transform. From this very same relation, [Heisenberg uncertainty relation](https://basics2022.github.io/bbooks-physics-modern/ch/quantum-mechanics/intro.html#heisenberg-uncertainty-relation) between position and momentum in [Quantum Mechanics](https://basics2022.github.io/bbooks-physics-modern/ch/quantum-mechanics/intro.html) seamlessly follows.

Given a function $g(t)$ whose square of the absolute value is normalized to one, and thus it can be used as a probability density function in time domain,

$$\int_{t = -\infty}^{+\infty} |g(t)|^2 \, dt =  \int_{t = -\infty}^{+\infty} g^*(t) \, g(t) \, dt = 1 \ .$$

for [Plancherel's theorem](complex:fourier:transform:plancherel), the square of the magnitude of Fourier transform $G(f)$ is unitary as well,

$$\int_{f = -\infty}^{+\infty} |G(f)|^2 \, df =  \int_{f = -\infty}^{+\infty} G^*(f) \, G(f) \, df = 1 \ ,$$

and thus it can be interpreted as a probability density function in frequency domain. The following uncertainty relation holds

$$\sigma_{t,g}^2 \sigma_{f,G}^2 \ge \left( \frac{1}{2 \pi} \frac{1}{2} \right)^2 \ , $$

or in terms of pulsation $\omega = 2 \pi \, f$,

$$\sigma_{t,g}^2 \sigma_{\omega,G}^2 \ge \left( \frac{1}{2} \right)^2 \ , $$

```{admonition} Heisenberg uncertainty relation in quantum mechanics
:name: fourier-uncertainty-heisenberg

Space and momentum representation of the state function $\Psi$ are related by the transformation,

$$\langle x | \Psi \rangle := \psi(x,t) = \int_{p=-\infty}^{+\infty} \psi_p(p,t) \, e^{i \frac{p}{\hbar} x} \, dp \ ,$$

as it's shown in the section [Quantum Mechanics:From position to momentum representation](https://basics2022.github.io/bbooks-physics-modern/ch/quantum-mechanics/intro.html#from-position-to-momentum-representation).
The wave number reads $k = \frac{p}{\hbar}$. Starting from the uncertainty relation between the space coordinate $x$ and the wave number $k$,

$$\sigma_{x} \sigma_{k} \ge  \frac{1}{2}  \ , $$

Heisenberg uncertainty principle for position and momentum (for the same Cartesian coordinates) reads

$$\sigma_{x} \sigma_{p} \ge \frac{\hbar}{2} \ . $$

```

````{dropdown} Proof of the uncertainty relation
:open:

Assuming zero average $\overline{t} = 0$, $\overline{f} = 0$ (see below for proof without this assumption)

$$\begin{aligned}
 \sigma_{t,g}^2 \sigma_{f,G}^2
 & = \int_{t=-\infty}^{+\infty} \left| t \right|^2 \, g^*(t) \, g(t)  \, dt \,  \int_{f=-\infty}^{+\infty} \left| f \right|^2 \, G^*(f) \, G(f) \, df = \\
 & = \int_{t=-\infty}^{+\infty} \left| t  \, g(t) \right|^2 \, dt \,  \int_{f=-\infty}^{+\infty} \left| f  \,  G(f)\right|^2 \, df = && (1) \\
 & = \int_{t=-\infty}^{+\infty} \left| t  \, g(t) \right|^2 \, dt \, \int_{t=-\infty}^{+\infty} \left|  -\frac{i}{2 \pi} \, \dot{g}(t) \right|^2 \, dt \ge && (2) \\
 & = \left| \int_{t=-\infty}^{+\infty} - t  \, g^*(t)  \frac{i}{2 \pi} \, \dot{g}(t) \, dt \right|^2 \ge && (3)  \\
 & = \left( \frac{1}{2\pi} \right)^2 \left( \frac{1}{2} \right)^2
\end{aligned}$$

having used in

```{dropdown} (1) 

$$\mathscr{F}\{ \dot{g}(t) \}(f) = \int_{t=-\infty}^{+\infty} \dot{g}(t) e^{-i 2 \pi f t} \, dt = \dots = i 2 \pi \, f \, G(f) \ , $$
$$f \, G(f) = -i \, \frac{\mathscr{F}\{ \dot{g}(t) \}}{2 \pi}$$

and thus [Plancherel's theorem](complex:fourier:transform:plancherel)

$$\begin{aligned}
 \int_{f=-\infty}^{+\infty} | f \, G(f) |^2 \, df
 & = \int_{f=-\infty}^{+\infty} \left|  -\frac{i}{2 \pi} \, \mathscr{F}\{ \dot{g}(t) \} \right|^2 \, df = \\
 & = \int_{t=-\infty}^{+\infty} \left|  -\frac{i}{2 \pi} \, \dot{g}(t) \right|^2 \, dt
\end{aligned}$$

```

in (2) Cauchy-Schwartz inequality,

```{dropdown} (3)

$$\begin{aligned}
  a 
  & := \int_{t=-\infty}^{+\infty} t g^*(t) \dot{g}(t) \, dt = \\
  &  = \underbrace{\left[ t \, g^*(t) \, g(t) \right]|_{-\infty}^{+\infty}}_{=0} - \int_{t=-\infty}^{+\infty} \dfrac{d}{dt} \left( t g^*(t) \right) g(t) \, dt = \\
  & = - \int_{t=-\infty}^{+\infty}  g^*(t) \,  g(t) \, dt - \int_{t=-\infty}^{+\infty} t \dot{g}^*(t) g(t) \, dt = \\
  & = - 1 - a^* \ .
\end{aligned}$$

$$-1 = a + a^* = 2 \, \text{re}\{a\} \ ,$$

and thus

$$|a|^2 \ge \text{re}\{a\}^2 = \frac{1}{4} \ .$$


```

If $\overline{t} \ne 0$, or $\overline{f} \ne 0$,

$$\begin{aligned}
 \sigma_{t,g}^2 \sigma_{f,G}^2
 & = \int_{t=-\infty}^{+\infty} \left| t - \overline{t} \right|^2 \, g^*(t) \, g(t)  \, dt \,  \int_{f=-\infty}^{+\infty} \left| f - \overline{f} \right|^2 \, G^*(f) \, G(f) \, df = \\
 & = \int_{t=-\infty}^{+\infty} \left| ( t - \overline{t} ) \, g(t) \right|^2 \, dt \,  \int_{f=-\infty}^{+\infty} \left| ( f - \overline{f} ) \,  G(f)\right|^2 \, df = && (1) \\
 & = \dots \\
\end{aligned}$$


````



