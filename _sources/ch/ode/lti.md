(ode:lti)=
# Linear Time-Invariant Systems

A linear time invariant system is governed by a linear ODE with constant coefficients. These equations can be recast as a first order system of ODEs,

$$\begin{cases}
  \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
       \mathbf{y}  = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} \\
  \mathbf{x}(0^-) = \mathbf{x}_0
\end{cases}$$

Exploiting the [properties of matrix exponential](ode:lti:matrix-properties) the general expression of the state can be written as the sum of the free response to initial condition and the forced response.

$$\begin{aligned}
  \mathbf{x}(t) & = e^{\mathbf{A}t} \mathbf{x}_0 + \int_{\tau=0^-}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u} (\tau) \, d \tau \\
  \mathbf{y}(t) & = \mathbf{C} e^{\mathbf{A}t} \mathbf{x}_0 + \mathbf{C} \int_{\tau=0^-}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u} (\tau) \, d \tau  + \mathbf{D} \mathbf{u}(t) \\
\end{aligned}$$

```{dropdown} Proof in time domain

Multipying by $e^{-\mathbf{A} t}$,

$$\begin{aligned}
  e^{-\mathbf{A}t} ( \dot{x}(t) - \mathbf{A} \mathbf{x}(t) ) & = e^{-\mathbf{A} t} \mathbf{B} \mathbf{u}(t) \\
    \dfrac{d}{dt} \left( \mathbf{x} e^{-\mathbf{A}t} \right) & = e^{-\mathbf{A} t} \mathbf{B} \mathbf{u}(t) \\
\end{aligned}$$

and integrating from $0^-$ to a generic time value $t$,

$$e^{-\mathbf{A}t} \mathbf{x}(t) - \mathbf{x}_0 = \int_{\tau=0^-}^{t} e^{-\mathbf{A}\tau} \mathbf{B} \mathbf{u} (\tau) \, d \tau$$

The state $\mathbf{x}(t)$ can be written as the sum of the free response and a force response. The general expression of the state and the output as a function reads 

$$\begin{aligned}
  \mathbf{x}(t) & = e^{\mathbf{A}t} \mathbf{x}_0 + \int_{\tau=0^-}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u} (\tau) \, d \tau \\
  \mathbf{y}(t) & = \mathbf{C} e^{\mathbf{A}t} \mathbf{x}_0 + \mathbf{C} \int_{\tau=0^-}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u} (\tau) \, d \tau  + \mathbf{D} \mathbf{u}(t) \\
\end{aligned}$$

```

**Laplace domain.**
The [Laplace transform](complex:laplace) of the problem reads

$$\begin{cases}
   s \hat{\mathbf{x}} = \mathbf{A} \hat{\mathbf{x}} + \mathbf{B} \hat{\mathbf{u}} + \mathbf{x}_0 \\
     \hat{\mathbf{y}} = \mathbf{C} \hat{\mathbf{x}} + \mathbf{D} \hat{\mathbf{u}} \\
\end{cases}$$

$$(s\mathbf{I} - \mathbf{A}) \hat{\mathbf{x}} = \mathbf{B} \hat{\mathbf{u}} + \mathbf{x}_0$$

$$\begin{aligned}
  \hat{\mathbf{x}}(s) & = (s\mathbf{I} - \mathbf{A})^{-1} \mathbf{x}_0 + (s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} \hat{\mathbf{u}}(s) \\
  \hat{\mathbf{y}}(s) & = \mathbf{C} (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{x}_0 + \left[ \mathbf{C} (s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} + \mathbf{D} \right] \hat{\mathbf{u}}(s)
\end{aligned}$$


Performing inverse Laplace transform allows to go back to time domain (just use Laplace inverse transform of a matrix exponential, and the formula {eq}`laplace:convolution` for Laplace transform of convolution).


## Impulsive force
The effect of an impulsive force at time $t=0$ is equivalent to an instantaneous change in the initial state, from time $0^-$ before the impulse to time $0^+$ after the impulse. Splitting the input $\mathbf{u}(t)$ as the sum of impulsive input and regular input,

$$\begin{aligned}
  \mathbf{u}(t) & = \mathbf{u}_r(t) + \mathbf{u}_\delta \delta(t) \\
  \hat{\mathbf{u}}(s) & = \hat{\mathbf{u}}_r(s) + \mathbf{u}_\delta \\
\end{aligned}$$

the solution in time and Laplace domain reads

$$\begin{aligned}
  \mathbf{x}(t)
  & = e^{\mathbf{A}t} \mathbf{x}_0 + \int_{\tau=0^-}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B} \left( \mathbf{u}_r (\tau) + \mathbf{u}_\delta \delta(\tau) \right) \, d \tau = \\ 
  & = e^{\mathbf{A}t} \left( \mathbf{x}_0 + \mathbf{B} \mathbf{u}_\delta \right) + \int_{\tau=0^-}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u}_r (\tau) \, d \tau \\
  \mathbf{y}(t)
  & = \mathbf{C} e^{\mathbf{A}t} \left( \mathbf{x}_0 + \mathbf{B} \mathbf{u}_\delta \right) + \int_{\tau=0^-}^{t} \mathbf{C} e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u}_r (\tau) \, d \tau + \mathbf{D} \mathbf{u}_r(t) + \mathbf{D} \mathbf{u}_\delta(t) \\
\end{aligned}$$

$$
  \hat{\mathbf{x}}(s) & = (s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} \hat{\mathbf{u}}_r(s) + (s\mathbf{I} - \mathbf{A})^{-1} \left( \mathbf{x}_0 + \mathbf{B} \mathbf{u}_\delta \right) \\
  \hat{\mathbf{y}}(s) & = \left[ \mathbf{C} (s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} + \mathbf{D} \right] \hat{\mathbf{u}}_r(s) + \mathbf{C} (s\mathbf{I} - \mathbf{A})^{-1} \left( \mathbf{x}_0 + \mathbf{B} \mathbf{u}_\delta \right) + \mathbf{D} \mathbf{u}_{\delta}
$$

(ode:lti:matrix-properties)=
## Properties

**Matrix exponential.**

$$e^{\mathbf{A} t} = \sum_{k = 0}^{+\infty} \frac{\mathbf{A}^k t^k}{k!} \ .$$

Assuming it's possible swap derivative operator and summation (when?), it's possible to write

$$\frac{d}{dt} e^{\mathbf{A}t} = \dfrac{d}{dt} \sum_{k = 0}^{+\infty} \frac{\mathbf{A}^k t^k}{k!} = \sum_{k=1}^{+\infty} k t^{k-1} \frac{\mathbf{A}^k t^{k-1}}{k!} = \mathbf{A} e^{\mathbf{A} t} \ .$$

**Laplace transform of exponential matrix.**

$$\begin{aligned}
  \mathscr{L}\left\{ e^{\mathbf{A}t} \right\}(s)
  & := \int_{t=0^-}^{+\infty} e^{\mathbf{A} t} e^{-s t} \, dt = \\
  & = \int_{t=0^-}^{+\infty} e^{(-s\mathbf{I} + \mathbf{A}) t} \, dt = \\
  & = (-s\mathbf{I} + \mathbf{A})^{-1} \left.e^{(-s\mathbf{I} + \mathbf{A}) t}\right|_{t=0^-}^{+\infty} = \\
  & = (- s \mathbf{I} + \mathbf{A})^{-1} \ ,
\end{aligned}$$

for all the values of $s$ for which $-s\mathbf{I} + \mathbf{A}$ is asymptotically stable, i.e. has all the eignevalues (thus, assuming that the matrix $\mathbf{A}$ can be diagonalizable. What happens if not? Exploit other matrix decompositions to draw conclusions) with negative real parts, and thus for all the values of $s > \max \text{re}\{ s_k(\mathbf{A}) \}$, as it's shown in {prf:ref}`matrix-stability-spectrum`

```{prf:example} Asymptotic stability of a matrix $\ \mathbf{A}$
:label: matrix-stability-spectrum

An $N \times N$ diagnonalizable matrix $\mathbf{A}$,

$$\mathbf{A} \mathbf{v}_k = \mathbf{v}_k \, s_k$$ (eq:matrix-stability:spectrum:A)

has all the eigenvalues with negative real part, $\text{re}\left\{ s_k \right\} < 0$, $\forall k=1:N$.

The eigenvalues of a matrix $a \mathbf{I} + \mathbf{A}$ are $a + s_k$, while the eigenvectors are the same as those of the matrix $\mathbf{A}$. This can be easily proved adding $a \mathbf{I} \mathbf{v}_k$ to both sides of equation {eq}`eq:matrix-stability:spectrum:A`,

$$\left( a \mathbf{I} + \mathbf{A} \right) \mathbf{v}_k = \mathbf{v}_k (a + s_k) \ .$$

```

**Transform of the convolution.**




