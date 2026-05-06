(system-theory:shape-filter)=
# Shape filter

**Response of a LTI to stochastic inputs.**
From the [response of LTI systems to stochastic input](ode:lti:response:stochastic), the auto-correlation of a zero-mean stationary process $x(t)$ (and thus its auto-covariance) reads

$$\mathbf{R}_{\mathbf{x} \mathbf{x}}(\tau) = \mathbb{E}\left[ \mathbf{x}_t \mathbf{x}^*_{t + \tau} \right] \ .$$

Fourier transform of this auto-correlation is defined as its **power spectral density, PSD**,

$$\boldsymbol\Phi_{\mathbf{x} \mathbf{x}} (f) := \mathscr{F} \{ \mathbf{R}_{\mathbf{x} \mathbf{x}} (\tau) \} (f) \ .$$

For a linear system whose input-output relation reads

$$\mathbf{y}(s) = \mathbf{H}(s) \mathbf{u}(s) \ ,$$

the PSD of the output can be written as a function of the PSD of the input and the Fourier transform of the transfer function as

$$\boldsymbol\Phi_{\mathbf{y}\mathbf{y}} (f) = \overline{\mathbf{H}}(f) \boldsymbol\Phi_{\mathbf{u}\mathbf{u}}(f) \mathbf{H}^T(f) \ .$$ (eq:psd:io:vector)

**SISO system.** The transfer function is a scalar function for a SISO system, and thus

$$\Phi_{yy}(f) = \overline{H}(f) \Phi_{uu}(f) H(f) = \left| H(f) \right|^2 \Phi_{uu}(f) \ ,$$ (eq:psd:io:scalar)

as the product of a complex number by its complex cojugate is equal to the square of its modulus.

**White noise.**
A [white noise](https://basics2022.github.io/bbooks-statistics/ch/prob/white-noise.html) $\xi(t)$ can be defined as a random process with

* zero expected value, $\mathbb{E}[\xi_t] = 0$
* Dirac's delta auto-correlation, $\mathbb{E}[\xi_t \xi_{t+\tau}] = \delta(\tau)$.

[Fourier transform of a Dirac's delta](functional-analysis:dirac-delta) is $1$, and thus the PSD of a white noise is

$$\boldsymbol\Phi_{\xi \xi}(f) = 1 \ .$$


**SISO shape filter.** A process $y(t)$ with the desired PSD $\Phi_{yy}(f)$ is the output of a shape filter - a dynamical system - with TF $H(f)$ satisfying the relation $|H(f)|^2 = \Phi_{yy}(f)$, fed by a white noise with unit autocovariance. This can be immediately proved inserting $\Phi_{uu}(f) = 1$ in the relation {eq}`eq:psd:io:scalar`.

(system-theory:shape-filter:augmented-system)=
## LTI system with non-white noise disturbance

Let the linear system 

$$\left\{\begin{aligned}
  \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} + \mathbf{B}_d \mathbf{d} \\
       \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} + \mathbf{D}_d \mathbf{d} + \mathbf{D}_r \mathbf{r} \\
\end{aligned}\right.$$

$$\left\{\begin{aligned}
  \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} + \mathbf{B}_n \mathbf{n} \\
       \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} + \mathbf{D}_n \mathbf{n} \\
\end{aligned}\right.$$

have non-white noise disturbances $\mathbf{n} = \begin{bmatrix} \ \mathbf{d} & \mathbf{r} \ \end{bmatrix}$, whose PSD is known and that can be modeled as the output of a shape filter fed by a white-noise $\mathbf{w}$,

$$\left\{\begin{aligned}
  \dot{\mathbf{x}}_n & = \mathbf{A}_{n}  \mathbf{x}_n + \mathbf{B}_{nn} \mathbf{w}_n  \\
       \mathbf{n}    & = \mathbf{C}_{nn} \mathbf{x}_n  \ ,
\end{aligned}\right.$$

then, the augmented system becomes

$$\left\{\begin{aligned}
  \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B}_n \mathbf{C}_{nn} \mathbf{x}_n + \mathbf{B} \mathbf{u} \\
  \dot{\mathbf{x}}_n & = \mathbf{A}_{n}  \mathbf{x}_n + \mathbf{B}_{nn} \mathbf{w}_n  \\
       \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D}_n \mathbf{C}_{nn} \mathbf{x}_n + \mathbf{D} \mathbf{u} \\
\end{aligned}\right.$$

or

$$\left\{\begin{aligned}
  \begin{bmatrix} \dot{\mathbf{x}} \\ \dot{\mathbf{x}}_n \end{bmatrix} & =
  \begin{bmatrix} \mathbf{A} & \mathbf{B}_n \mathbf{C}_{nn} \\ \cdot & \mathbf{A}_n \end{bmatrix}
  \begin{bmatrix}      \mathbf{x}  \\      \mathbf{x}_n \end{bmatrix} 
  + \begin{bmatrix} \mathbf{B} \\ \cdot \end{bmatrix} \mathbf{u} + \begin{bmatrix} \cdot \\ \mathbf{B}_{nn} \end{bmatrix} \mathbf{w}_n \\
  \mathbf{y} & = \begin{bmatrix} \mathbf{C} & \mathbf{D}_n \mathbf{C}_{nn} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \mathbf{x}_{n} \end{bmatrix} + \mathbf{D} \mathbf{u}
\end{aligned}\right.$$

(system-theory:shape-filter)=
## Example

A 1-dimensional non-white noise process $d$ has PSD, $\Phi_{dd}(\omega) = | H(j \omega) |^2$ with

$$H(s) = \frac{s}{(s-p_1)(s-p_2)} = \frac{s}{s^2 + a_1 s + a_0} \ .$$

with $a_0 = p_1 p_2$, $a_1 = - ( p_1 + p_2 )$.

Using the [controller canonical realization](system-theory:state-space-realizations:ccf), a state-space representation of the shape filter follows

$$\left\{\begin{aligned}
 \begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} & = \begin{bmatrix} \cdot & 1 \\ - a_0 & - a_1 \end{bmatrix} \begin{bmatrix} \cdot \\ 1 \end{bmatrix} w \\
 y & = \begin{bmatrix} \ 0 & 1 \ \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \ .
\end{aligned}\right.$$

**Lyapunov equation for the coorelation matrix $\ d$.** Correlation matrix of the state can be evaluated as the solution of the [Lyapunov equation for the correlation matrix](ode:linear:miscellanea:stochastic-response:correlation-matrix:lyapunov), for systems - like the shape filter - with a white noise input.

**Non-strictly proper system.** If a LTI fed by a white noise process as an input is not striclty proper, $\mathbf{D} \ne \mathbf{0}$, ... 
* the output has infinite variance (it can be split as a colored noise + white noise), 
* PSD doesn't decay to zero as $\omega \rightarrow 0$
* Lyapunov equation for variance doesn't converge to a finite value solution

**todo** prove these statements

