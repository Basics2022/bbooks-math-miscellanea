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




