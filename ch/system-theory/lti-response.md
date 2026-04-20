(ode:lti:response)=
# LTI system response

Usually the response of LTI to 3 different input are studied
- integrable input, being response to non-zero initial condition equivalent to an impulsive force at time $t = 0$, see [equivalence impulsive force - istantanteous change of state](ode:lti:impulsive-force)
- periodic input
- stochastic input

## LTI

$$\begin{cases}
  \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
  \mathbf{y} = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u}
\end{cases}$$

with initial conditions, $\mathbb{x}(0) = \mathbf{x}_0$.

(ode:lti:response:general)=
## Response of LTI systems

The response of a LTI can be written as the sum of a free and forced response. 

$$\begin{aligned}
  \mathbf{x}(t) & = e^{\mathbf{A} t} \mathbf{x}_0 + \int_{\tau=0}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u}(\tau) \, d \tau \\
  \mathbf{y}(t) & = \mathbf{C} \, e^{\mathbf{A} t} \mathbf{x}_0 + \int_{\tau=0}^{t} \mathbf{C} e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u}(\tau) \, d \tau + \mathbf{D} \mathbf{u}(t) \\
\end{aligned}$$ (eq:lagrange:formula)

```{dropdown} Proof

**todo**
```

```{admonition} Impulse response, $ \mathbf{H}(t)$
:class: tip

Functions

$$\begin{aligned}
  \mathbf{H}_x(t) & := e^{\mathbf{A} t} \mathbf{B} \\
  \mathbf{H}  (t) & := \mathbf{C} e^{\mathbf{A} t} \mathbf{B} + \mathbf{D} \delta(t) \\
\end{aligned}$$

are defined **impulse response functions** for the state $\mathbf{x}$ and the output $\mathbf{y}$, as they determine with the evolution of the state and the output of a system with zero initial condition $\mathbf{x}_0 = \mathbf{0}$ as a consequence of a impulsive force $\mathbf{u}_{\delta}(t) = \mathbf{u} \delta(t)$. Using Lagrange formula {eq}`eq:lagrange:formula`

$$\begin{aligned}
  \mathbf{x}(t) & = e^{\mathbf{A}t} \mathbf{B} \mathbf{u} && = \mathbf{H}_x(t) \mathbf{u} \\ 
  \mathbf{y}(t) & = \left[ \mathbf{C} e^{\mathbf{A}t} \mathbf{B} + \mathbf{D} \delta(t) \right] \mathbf{u} && = \mathbf{H}(t) \mathbf{u} \\
\end{aligned}$$ (eq:lagrange:formula:impulse)


```

```{admonition} Convolution
:class: tip

Integral in Lagrange formula {eq}`eq:lagrange:formula` is the convolution of the impulse response function and the input. Changing the integration variable $z = t - \tau$, $d\tau = - dz$, $\tau = 0: \, z = t$, $\tau = t, \ z = 0$ (and going back from $z$ to $\tau$ as the symbol for the dummy integration variable), it's possible to swap the arguments of the impulsive force and the forcing,

$$\begin{aligned}
  \mathbf{x}(t) & = e^{\mathbf{A} t} \mathbf{x}_0 + \int_{\tau=0}^{t} \mathbf{H}_x(\tau) \mathbf{u}(t-\tau) \, d \tau \\
  \mathbf{y}(t) & = \mathbf{C} \, e^{\mathbf{A} t} \mathbf{x}_0 + \int_{\tau=0}^{t} \mathbf{H}(\tau) \mathbf{u}(t-\tau) \, d \tau \\
\end{aligned}$$ (eq:lagrange:convol)

```

```{admonition} Linear but not time-invariant
:class: tip

**todo** *The response of linear system, but not time-invariant can be written with the same expression used by Lagrange fomrula {eq}`eq:lagrange:formula`, with $\mathbf{H}(t)$ not equal to ..., but solution of the ODE...*

$$\begin{aligned}
  \boldsymbol{\Phi} \left( \dot{\mathbf{x}} - \mathbf{A}\mathbf{x} \right) & = \boldsymbol{\Phi} \mathbf{B} \mathbf{u} \\
  \dfrac{d}{dt} \left( \boldsymbol{\Phi} \mathbf{x} \right) & = \boldsymbol{\Phi} \mathbf{B} \mathbf{u} \ ,
\end{aligned}$$

with $\dot{\boldsymbol{\Phi}} = - \boldsymbol{\Phi} \mathbf{A}$, and proper initial conditions $\boldsymbol{\Phi}(t,0) = \mathbf{I}$.

...

$$\mathbf{x}(t) = \boldsymbol{\Phi}(t,0) \mathbf{x}_0 + \int_{\tau=0}^{t} \boldsymbol{\Phi}(t, \tau) \mathbf{B}(\tau) \mathbf{u}(\tau) \, d \tau \ .$$

```

(ode:lti:response:equilibria)=
## Equilibria

Equilibrium solution of a ODE is a stationary solution, independent from time, $\dot{\overline{\mathbf{x}}} = \mathbf{0}$. With a steady forcing $\overline{\mathbf{u}}$,

$$\begin{cases}
  \mathbf{0} = \mathbf{A} \overline{\mathbf{x}} + \mathbf{B} \overline{\mathbf{u}} \\
  \mathbf{y} = \mathbf{C} \overline{\mathbf{x}} + \mathbf{D} \overline{\mathbf{u}} \ .
\end{cases}$$

**If $\mathbf{A}$ is not singular**, for every steady forcing $\overline{\mathbf{u}}$ only one equilibrium exists for the system, $\overline{\mathbf{x}} = \mathbf{A}^{-1} \mathbf{B} \overline{\mathbf{u}}$.

**If $\mathbf{A}$ is singular**...**todo** *rely on [Linear algebra](math:linear-algebra:intro)*

(ode:lti:response:stability)=
## Stability

**Asymptotic stability to initial perturbations.** A system is stable under perturbation of initial conditions if the free response goes to zero as $t \rightarrow + \infty$,

$$\lim_{t \rightarrow +\infty} \mathbf{x}_{free}(t) = \mathbf{0} \ .$$

**todo** *for all perturbations*(?).

If matrix $\mathbf{A}$ is diagonalizable, a system is asymptotically stable if all the eigenvalues of the matrix $\mathbf{A}$ have negative real part, $\text{re}\{\lambda_i(\mathbf{A})\} < 0$.

**todo**  *rely on [Linear algebra](math:linear-algebra:intro)*


(ode:lti:response:laplace)=
## Response to integrable input - and Laplace transform

$$\begin{aligned}
  \mathbf{x}(s) & = \left(s \mathbf{I} - \mathbf{A} \right)^{-1} \mathbf{x}_0 + \mathbf{H}_x(s) \mathbf{u}(s) \\
  \mathbf{y}(s) & = \mathbf{C} \, \left( s \mathbf{I} - \mathbf{A} \right)^{-1} \mathbf{x}_0 + \mathbf{H}(s) \mathbf{u}(s)
\end{aligned}$$ (eq:lagrange:formula:laplace)

(ode:lti:response:periodic)=
## Response to periodic input of stable systems - and Fourier transform

Forced response to periodic input of an stable system can be represented in Fourier domain replacing $s$ with $j \omega$ (and dropping $j$ once it's clear we're dealing with Fourier analysis)

$$\begin{aligned}
  \mathbf{x}(\omega) & = \mathbf{H}_x(\omega) \ \mathbf{u}(\omega) \\
  \mathbf{y}(\omega) & = \mathbf{H}  (\omega) \ \mathbf{u}(\omega)
\end{aligned}$$ (eq:lagrange:formula:fourier)

(ode:lti:response:stochastic)=
## Response to stochastic input of stable systems

### Assumptions
...

### Expected value

$$\boldsymbol{\mu}_{\mathbf{x}}(t) := \mathbb{E}[ \mathbf{x}(t) ]$$

Taking expected value of LTI equations

$$\begin{cases}
  \mathbb{E}[\dot{\mathbf{x}}] = \mathbf{A} \mathbb{E}[\mathbf{x}] + \mathbf{B} \mathbb{E}[\mathbf{u}] \\
  \mathbb{E}[     \mathbf{y} ] = \mathbf{C} \mathbb{E}[\mathbf{x}] + \mathbf{D} \mathbb{E}[\mathbf{u}] \\
\end{cases}$$

**todo** 
- *is it possible to swap time derivative and expected value operators?*
- *does time derivative of a stochastic process always exist? What's the right way to interpret time derivative in stochastic equations? As an increment?*

  $$d \mathbf{x} = \mathbf{A} \mathbf{x} \, d t + \mathbf{B} \mathbf{u} \, d t$$

  so that if $\mathbf{u}(t) \sim \boldsymbol{\xi}(t)$, then $\mathbf{u} \, dt \sim d \mathbf{W}$

## Analysis of response of LTI in Fourier domain

**Energy or power.** For
- time integrable signals: don't average in time; energy
- periodic or stochastic non-integrable signals: average in time; power

**Stationary stochastic process.** Strong-sense (joint probability independent from time) or wide-sense (moments up to order $m$ are independent on time)

**Ergodic process.** Average over random process can be replaced with average over time.

```{admonition} Example of stationary non-ergodic process

As an example of stationary, but not ergodic process is a random process whose realizations are

$$X_t = \theta \ , \qquad \forall t \in [0,T]$$

with $\theta$ drawn from a random variable $\Theta$, with average $\mu$. Average in time over a realization gives $\theta$, while average over realizations gives $\mu$ for all $t$,

$$\begin{aligned}
  \text{Avg. in time over a realization:       } & \quad  \dfrac{1}{T} \int_{t=0}^{T} X_t \, dt = \dfrac{1}{T} \int_{t=0}^{T} \theta \, dt = \theta \\
  \text{Avg. in probability over realizations: } & \quad  \mathbb{E}[X_t] = \mathbb{E}[\Theta] = \mu \ .
\end{aligned}$$

```

```{admonition} White noise...

```
### Stationary Ergodic processes

**Auto-correlation**

$$\mathbf{R}_{XX}(t_1, t_2) = \mathbb{E}\left[ \mathbf{X}_{t_1} \, \mathbf{X}_{t_2}^* \right]$$

**Auto-covariance**

$$\mathbf{K}_{XX}(t_1, t_2) = \mathbb{E}\left[ (\mathbf{X}_{t_1} - \boldsymbol{\mu}_{t_1} ) (\mathbf{X}_{t_2} - \boldsymbol{\mu}_{t_2} )^* \right]$$

For stationary processes, both auto-correlation and auto-covariance don't depend on two time instant $t_1$, $t_2$ but only on the time-shift between them, $t_2 = t_1 + \tau$,

$$\mathbf{R}_{XX}(\tau) = \mathbb{E}\left[ \mathbf{X}_{t} \, \mathbf{X}_{t + \tau}^* \right] \ , \qquad \forall t \ .$$


```{dropdown} Autocorrelation and ESD of time integrable processes
:open:

With causal, $\mathbf{x}(t \le 0) = 0$, and integrable processes, autocorrelation is defined as

$$\tilde{\mathbf{R}}_{xx}(\tau) = \int_{t = 0}^{+\infty} \mathbf{x}(t) \mathbf{x}^*(t+\tau) \, d t \ ,$$

**Energy Spectral Density (ESD)** is defined as its Fourier transform

$$\tilde{\boldsymbol{\Phi}}_{xx}(f) = \mathscr{F} \left\{ \mathbf{R}_{xx}(\tau) \right\} (f) \ ,$$


```

```{dropdown} Autocorrelation and PSD of infinite-time processes
:open:

Using average over time as an approximation of the probability average

$$\mathbb{E}[ f(t) ] \sim \lim_{T \rightarrow +\infty} \dfrac{1}{T} \int_{t=0}^{T} f(\tau) \, d \tau \ ,$$

**Power Spectral Density (PSD)**, defined as the Fourier transform of the auto-correlation, reads

$$\begin{aligned}
  \boldsymbol{\Phi}_{YY}(f)
  & = \mathscr{F}[ \mathbf{R}_{YY}(\tau) ](f) = \\ 
  & = \int_{\tau = -\infty}^{+\infty} \mathbb{E} \left[ \mathbf{y}(t) \mathbf{y}^*(t+\tau) \right]  \, e^{-i 2 \pi f \tau} \, d \tau \ .
\end{aligned}$$

For asymptotically stable systems subject to periodic forcing, response to non-homogenoeus initial conditions vanishes while the forced response can be written either in Fourier or in time domain, exploiting the property of the transform of convolution {prf:ref}`transform:fourier:convolution`, as

$$\begin{aligned}
  \mathbf{y}(f) = \mathbf{H}(f) \, \mathbf{u}(f) \qquad , \qquad
  \mathbf{y}(t) = \mathbf{H} \ast \mathbf{u}(t) = \int_{\tau=-\infty}^{+\infty} \mathbf{H}(\tau) \mathbf{u}(t - \tau) \, d \tau \ .
\end{aligned}$$

Inserting harmonic response into the expression of PSD, it becomes

$$\begin{aligned}
  \boldsymbol{\Phi}_{YY}(f)
  & = \int_{\tau = -\infty}^{+\infty} \mathbb{E} \left[ \left( \int_{\xi=-\infty}^{+\infty} \mathbf{H}(\xi) \, \mathbf{u}(t - \xi) \, d\xi \right) \left( \int_{\chi=-\infty}^{+\infty} \mathbf{H}(\chi) \, \mathbf{u}(t+\tau-\chi) \, d \chi \right)^* \right]  \, e^{-i 2 \pi f \tau} \, d \tau  = && (1) \\ 
  & = \int_{\tau = -\infty}^{+\infty} \, \int_{\xi=-\infty}^{+\infty} \, \int_{\chi=-\infty}^{+\infty}  \mathbf{H}(\xi) \mathbb{E} \left[ \mathbf{u}(t - \xi)  \mathbf{u}^*(t+\tau-\chi) \right] \mathbf{H}^*(\chi) \, e^{-i 2 \pi f \tau} \, d \tau \, d \chi \, d \xi = && (2) \\ 
  & = \int_{\tau = -\infty}^{+\infty} \, \int_{\xi=-\infty}^{+\infty} \, \int_{\chi=-\infty}^{+\infty}  \mathbf{H}(\xi) \mathbb{E} \left[ \mathbf{u}(t )  \mathbf{u}^*(t+\tau-\chi+\xi) \right] \mathbf{H}^*(\chi) \, e^{-i 2 \pi f \tau} \, d \tau \, d \chi \, d \xi = && (3) \\ 
  & = \int_{z = -\infty}^{+\infty} \, \int_{\xi=-\infty}^{+\infty} \, \int_{\chi=-\infty}^{+\infty}  \mathbf{H}(\xi) \mathbb{E} \left[ \mathbf{u}(t )  \mathbf{u}^*(t+z) \right] \mathbf{H}^*(\chi) \, e^{-i 2 \pi f \left( z - \xi + \chi \right)} \, d z \, d \chi \, d \xi = \\ 
  & = \int_{\xi = -\infty}^{+\infty} \mathbf{H}(\xi) \, e^{i 2 \pi f \xi} \, d \xi \, \int_{z=-\infty}^{+\infty} \mathbf{R}_{uu}(z) \, e^{-i 2 \pi f z } \, dz \, \int_{\chi=-\infty}^{+\infty} \mathbf{H}^*(\chi) \, e^{-i 2 \pi f \chi } \, d \chi = (4) \\ 
  & = \overline{\mathbf{H}}(f) \, \boldsymbol{\Phi}_{uu}(f) \, \mathbf{H}^T(f) \ .
\end{aligned}$$

having used $(1)$ the fact that the impulse response function is deterministic, $(2)$ time shift in the autocorrelation for a **stationary** random process $\mathbf{u}(t)$ as an input, and $(3)$ the change of coordinates $(z, \xi, \chi) = (\tau-\chi+\xi, \xi, \chi)$, and $(4)$ a slight notation abuse ndicating Fourier transform with the same symbols of the functions in time domain.


<!--
$$\begin{aligned}
  \boldsymbol{\Phi}_{YY}(f) & = \mathscr{F}[ \mathbf{R}_{YY}(\tau) ](f) 
     = \int_{\tau = -\infty}^{+\infty} \mathbf{R}_{YY}(\tau) e^{- i 2 \pi f \tau } \, d \tau = \\
   & = \int_{\tau = -\infty}^{+\infty} \lim_{T\rightarrow + \infty} \dfrac{1}{T} \int_{t=0}^{+\infty} \mathbf{y}(t) \mathbf{y}^*(t+\tau) \, dt \, e^{-i 2 \pi f \tau} \, d \tau = \\
\end{aligned}$$

with 

$$\mathbf{y}(t) = \int_{\xi = 0}^{t} \mathbf{h}(\xi) \, \mathbf{u}(t - \xi) \, d \xi \ , $$

it becomes

$$\begin{aligned}
  \boldsymbol{\Phi}_{YY}(f) 
   & = \int_{\tau = -\infty}^{+\infty} \lim_{T\rightarrow + \infty} \dfrac{1}{T} \int_{t=0}^{T} \left( \int_{\xi=0}^{t} \mathbf{h}(\xi) \mathbf{u}(t - \xi) d \xi \right) \, \left( \int_{\chi = 0}^t \mathbf{h}(\chi) \mathbf{u}(t+\tau-\chi) \, d \chi \right)^* \, dt \, e^{-i 2 \pi f \tau} \, d \tau = \\
   & = \lim_{T\rightarrow + \infty} \dfrac{1}{T} \int_{t=0}^{T} \int_{\tau = -\infty}^{+\infty}  \int_{\xi=0}^{t} \int_{\chi = 0}^t \int_{\tau = -\infty}^{+\infty} \mathbf{h}(\xi)  \mathbf{u}(t - \xi)  \mathbf{u}^*(t+\tau-\chi) \mathbf{h}^*(\chi) \, e^{-i 2 \pi f \tau} \, d \xi  \, d \chi \, dt d \tau = \\
\end{aligned}$$

and, shifting $\mathbf{u}$ back of $+\chi$, defining $z = \dots$, so that  **todo** *check extremes of integration*

$$\begin{aligned}
  \boldsymbol{\Phi}_{YY}(f) 
   & = \int_{\tau = -\infty}^{+\infty}  \int_{\xi=0}^{t} \int_{\chi = 0}^t \int_{\tau = -\infty}^{+\infty} \mathbf{h}(\xi) \lim_{T\rightarrow + \infty} \dfrac{1}{T} \int_{t=0}^{T}  \mathbf{u}(t)  \mathbf{u}^*(t+\tau-\chi+\xi) \mathbf{h}^*(\chi) \, e^{-i 2 \pi f \tau} \, d \xi  \, d \chi \, dt d \tau = \\
   & = \int_{\tau = -\infty}^{+\infty}  \int_{\xi=0}^{t} \int_{\chi = 0}^t \int_{\tau = -\infty}^{+\infty} \mathbf{h}(\xi) \lim_{T\rightarrow + \infty} \dfrac{1}{T} \int_{t=0}^{T}  \mathbf{u}(t)  \mathbf{u}^*(t+z) \mathbf{h}^*(\chi) \, e^{-i 2 \pi f (z + \chi - \xi)} \, d \xi  \, d \chi \, dt \, d z = \\
   & = \int_{z = \dots}^{\dots}  \int_{\xi=\dots}^{\dots} \int_{\chi = \dots}^{\dots} \mathbf{h}(\xi) \, \mathbf{R}_{UU}(z) \, \mathbf{h}^*(\chi) \, e^{-i 2 \pi f (z + \chi - \xi)} \, d \xi  \, d \chi \, d z = \\
   & = \left( \int_{\xi = \dots}^{\dots} \mathbf{h}(\xi) \, e^{i 2 \pi f \xi} \, d \xi \right) \left( \int_{z=\dots}^{\dots} \mathbf{R}_{UU}(z) e^{-i 2 \pi f z } \, dz \right) \left( \int_{\chi = \dots}^{\dots} \mathbf{h}^*(\chi) \, e^{-i 2 \pi f \chi} \, d \chi \right) = \\
   & = \overline{\mathbf{H}}(f) \, \boldsymbol{\Phi}_{UU}(f) \, \mathbf{H}^T(f) \ .
\end{aligned}$$
-->


```



