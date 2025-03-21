(complex:fourier:transforms)=
# Relations between Fourier transforms

Some freestyle in changing order of summations and integrals, and use of generalized functions here...check it!

(complex:fourier:transform)=
## Fourier transform of integrable functions

$$F(\nu) := \mathscr{F}\left\{f(t)\right\}(\nu) := \int_{t=-\infty}^{+\infty} f(t) e^{-i 2 \pi \nu t} \, dt \ ,$$

(complex:fourier:series)=
## Fourier transform of the sum of shifted integrable functions

The infinite sum of a shifted integrable function is defined as

$$\tilde{f}_T(t) = \sum_{n=-\infty}^{+\infty} f(t - nT) \ .$$

Its Fourier transform reads

$$\begin{aligned}
  \mathscr{F}\left\{ \tilde{f}_T(t) \right\}(\nu)
  & = \int_{t=-\infty}^{+\infty} \tilde{f}_T(t) e^{-i 2 \pi \nu t} \, dt = \\
  & = \sum_{n=-\infty}^{+\infty} \int_{t=-\infty}^{+\infty} f(t-nT) e^{-i 2 \pi \nu t} \, dt = && (1) \\
  & = \sum_{n=-\infty}^{+\infty} F(\nu) e^{-i 2 \pi \nu n T} = && (2) \\
  & = F(\nu) \sum_{n=-\infty}^{+\infty} e^{-i 2 \pi \nu n T} = && (3) \\
  & = \Delta \nu \, F(\nu) \, \text{III}_{\Delta \nu}(\nu) \ ,
\end{aligned}$$

having used properties of Fourier transform of shifted function in (1), and the properties of Dirac's comb in (3), having defined the frequency resolution 

$$\Delta \nu := \frac{1}{T} \ .$$

This Fourier transform is proportional to the Fourier transform of the original function, sampled in frequency with elementary frequency $\Delta \nu$.

(complex:fourier:dtft)=
## Fourier transform of the a function sampled with a Dirac comb - DTFT

Fourier transform of the original function sampled with $\Delta t \, \text{III}_{\Delta t}(t)$ reads

$$\begin{aligned}
\mathscr{F}\left\{ \Delta t \, f(t) \, \text{III}_{\Delta t}(t) \right\}
 & = \Delta t \int_{t=-\infty}^{+\infty} f(t) \, \text{III}_{\Delta t}(t) e^{-i 2 \pi \nu t} \, dt =  \\
\end{aligned}$$

$$\begin{aligned}
 & \sim \Delta t \frac{1}{\Delta t} \int_{t=-\infty}^{+\infty} f(t) \, \sum_{n=-\infty}^{+\infty} e^{i n \frac{2 \pi}{\Delta t} t} e^{-i 2 \pi \nu t} \, dt =  \\
 & = \sum_{n=-\infty}^{+\infty}  \int_{t=-\infty}^{+\infty} f(t) \, e^{-i 2 \pi \left( \nu - n \overline{\nu} \right) t} \, dt =  \\
 & = \sum_{n=-\infty}^{+\infty} F\left(\nu - n \overline{\nu} \right) = \text{DTFT}(f(t); \Delta t) \ ,
\end{aligned}$$ (eq:dtft:1)

i.e. equals the periodic sum of the Fourier of the original function, with period

$$\overline{\nu} := \frac{1}{\Delta t} \ .$$

From this last sentence and from the [symmetry properties of Fourier transform](complex:fourier:useful-properties:symmetry), **Nyquist-Shannon sampling theorem** follows seamlessly.

```{prf:theorem} Nyquist-Shannon sampling theorem

In order to **avoid aliasing** the sampling frequency must be twice the maxiumum[^shannon-max-frequency] frequency in the signal,

$$\nu_s \ge 2 \nu_{max} \ .$$

```

**todo** check alternative expressions if using the definition of train of impulses instead of the Fourier series of Dirac's comb.

$$\begin{aligned}
 & = \Delta t \int_{t=-\infty}^{+\infty} f(t) \sum_{k=-\infty}^{+\infty} \delta(t - k \Delta t) \, e^{-i 2 \pi \nu t} \, dt = \\
 & = \Delta t \sum_{k=-\infty}^{+\infty} f(k \Delta t)  e^{-i 2 \pi \nu k \Delta t} = \text{DTFT}\left( f(t); \Delta t \right) 
\end{aligned}$$ (eq:dtft:2)

[^shannon-max-frequency]: Usually there's no such a frequency above which the signal is exactly zero, but usually there's a frequency above which the spectrum of the signal is approximately zero, i.e. below a threshold where it can be treated as zero, and introduce no aliasing.

(complex:fourier:dft)=
## Fourier transform of the sum of shifted integral functions sampled with a Dirac comb

Fourier transform of the periodic sum

$$\Delta t \, \tilde{f}(t) \, \text{III}_{\Delta t}(t) = \Delta t \, \sum_{n=-\infty}^{+\infty} f(t-nT) \, \text{III}_{\Delta t}(t) $$

reads

$$\begin{aligned}
\mathscr{F}\left\{ \Delta t \, \tilde{f}(t) \, \text{III}_{\Delta t}(t) \right\}(\nu) 
  & = \Delta t \int_{t=-\infty}^{+\infty} \sum_{n=-\infty}^{+\infty} f(t-nT) \sum_{k=-\infty}^{+\infty} \delta(t-k \Delta t) \, e^{-i 2 \pi \nu t } \, dt = \\
  & = \Delta t \sum_{n=-\infty}^{+\infty} \sum_{k=-\infty}^{+\infty} f(k \Delta t - nT) \, e^{-i 2 \pi \nu k \Delta t } = \\
\end{aligned}$$

and defining $k \Delta \tau_n := k \Delta t - nT$,

$$\begin{aligned}
& = \Delta t \sum_{n=-\infty}^{+\infty} \sum_{k=-\infty}^{+\infty} f(k \Delta \tau_n) e^{-i 2 \pi \nu k \Delta \tau_n} e^{-i 2 \pi \nu n T} = \\
& = \underbrace{\Delta t \sum_{k=-\infty}^{+\infty} f(k \Delta \tau_n) e^{-i 2 \pi \nu k \Delta \tau_n}}_{=\text{DTFT}(f(t), \Delta t)} \, \underbrace{\sum_{n=-\infty}^{+\infty} e^{-i 2 \pi \nu n T}}_{= \Delta \nu \, \text{III}_{\Delta \nu}(\nu)} = \\
& = \text{DTFT}(f(t), \Delta t) \, \Delta \nu \, \text{III}_{\Delta \nu}(\nu) \ .
\end{aligned}$$

<span style="color:red"> **todo** **check!** check the change of coordinates that makes DTFT appear</span>

<span style="color:red"> **todo** **check!** what follows
or, using the relation between $\Delta t$ and $T = N \Delta t$, $\Delta \nu = \frac{1}{T}$, and thus

$$\Delta t \, \Delta \nu = \Delta t \, \frac{1}{T} = \frac{1}{N} \ ,$$

it follows 

$$
 = \frac{1}{N} \sum_{k=-\infty}^{+\infty} f(k \Delta \tau_n) e^{-i 2 \pi \nu k \Delta \tau_n} \ \text{III}_{\Delta \nu}(\nu) \ .
$$
</span>

(complex:fourier:useful-properties)=
## Useful properties

(complex:fourier:useful-properties:dirac-comb)=
### Dirac's comb $\text{III}_T(t)$
Dirac comb $\text{III}_T(t)$ is defined as a train of Dirac's delta

$$\text{III}_T(t) = \sum_{m=-\infty}^{+\infty} \delta(t-mT) \ .$$

Coefficients {eq}`eq:fourier-series:exp:coeff` of the Fourier series {eq}`eq:fourier-series:exp` of a $T$-periodic train of Dirac delta for $t \in \left[-\frac{T}{2}, \frac{T}{2} \right]$, read

$$c_n = \frac{1}{T} \int_{t=0}^{T} \delta(t) \, e^{-i n \frac{2\pi}{T} t} = \frac{1}{T} \ ,$$

and thus the Fourier series of Dirac comb $\text{III}_T(t)$ reads

$$\text{III}_T(t) = \sum_{m=-\infty}^{+\infty} \delta(t-mT) \sim \frac{1}{T} \sum_{n=-\infty}^{+\infty} e^{i n \frac{2\pi}{T} t} \ .$$

(complex:fourier:useful-properties:symmetry)=
### Symmetry of Fourier transform










