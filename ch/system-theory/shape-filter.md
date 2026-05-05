(system-theory:shape-filter)=
# Shape filter

From the [response of LTI systems to stochastic input](ode:lti:response:stochastic), the auto-correlation of a zero-mean stationary process $x(t)$ (and thus its auto-covariance) reads

$$\mathbf{R}_{\mathbf{x} \mathbf{x}}(\tau) = \mathbb{E}\left[ \mathbf{x}_t \mathbf{x}^*_{t + \tau} \right] \ .$$

Fourier transform of this auto-correlation is defined as its **power spectral density, PSD**,

$$\boldsymbol\Phi_{\mathbf{x} \mathbf{x}} (f) := \mathscr{F} \{ \mathbf{R}_{\mathbf{x} \mathbf{x}} (\tau) \} (f) \ .$$

For a linear system whose input-output relation reads

$$\mathbf{y}(s) = \mathbf{H}(s) \mathbf{u}(s) \ ,$$

the PSD of the output can be written as a function of the PSD of the input and the Fourier transform of the transfer function as

$$\boldsymbol\Phi_{\mathbf{y}\mathbf{y}} (f) = \overline{\mathbf{H}}(f) \boldsymbol\Phi_{\mathbf{u}\mathbf{u}}(f) \mathbf{H}^T(f) \ .$$

A [white noise](https://basics2022.github.io/bbooks-statistics/ch/prob/white-noise.html) can be defined as a random process with

* zero expected value

   

* Dirac's delta auto-correlation






