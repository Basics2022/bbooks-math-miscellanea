(complex:fourier:transforms)=
# Relations between Fourier transforms

```{warning}

Some freestyle in changing order of summations and integrals, and use of generalized functions here...check it!

```


```{dropdown} Different Fourier transforms

Different Fourier transforms exist, depending if the original function is:
- time discrete/time continuous 
- periodic/non-periodic

namely,
- FS, Fourier series: time continuous, periodic function (or finite domain, with a periodic extension)
- FT, Fourier transform: time continuous, non-periodic function
- DTFT, discrete-time Fourier transform: time didscrete, infinite-length sequence
- DFT, discrete Fourier transform: time discrete, finite-length sequence (and then with a periodic extension)

```

Different forms of Fourier transforms exist, depending on the features of the original function and its domain. The bridge between continous and discrete domains is the [**Dirac' comb**](complex:fourier:useful-properties:dirac-comb), $\text{III}_{\Delta x}(x) := \sum_{m=-\infty}^{+\infty} \delta(x - m \Delta x)$, that can be used to **model sampling** of continous functions into sequences of discrete values, both in time and frequency domain.

Here 
* the standard **Fourier transform** of integrable functions is recalled
* the Fourier transform of an infinite sum of $T$-shifted integrable function is evaluated, resulting in the sampled (and scaled) Fourier transform of the original function, with sampling frequency $\Delta \nu = \frac{1}{T}$. Here $T$ plays the role of the sampling period. ...**Fourier series**
* the Fourier transform of a $\Delta t$-sampled (and scaled) integrable function is evaluated, resulting in the infinite sum of $\overline{\nu}$-shifted Fourier transform of the original function, with $\nu_s = \frac{1}{\Delta t}$. Here $\Delta t$ plays the role of the discrete time-step, inverse of the sampling frequency...**Discrete-time Fourier transform**
* putting the last two points together, the Fourier transform of a infinite sum of $T$-shifted $\Delta t$-sampled function is evaluated resulting in...**DFT**


(complex:fourier:transform)=
## Fourier transform of integrable functions

$$F(\nu) := \mathscr{F}\left\{f(t)\right\}(\nu) := \int_{t=-\infty}^{+\infty} f(t) e^{-i 2 \pi \nu t} \, dt \ ,$$

...

this is the starndard Fourier transform.

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
## Discrete-time Fourier transform

```{dropdown} Fourier transform of an integrable function sampled with a Dirac comb
:open:

Fourier transform of the original function sampled with $\Delta t \, \text{III}_{\Delta t}(t)$ reads

$$\begin{aligned}
\mathscr{F}\left\{ \Delta t \, f(t) \, \text{III}_{\Delta t}(t) \right\}
 & = \Delta t \int_{t=-\infty}^{+\infty} f(t) \, \text{III}_{\Delta t}(t) e^{-i 2 \pi \nu t} \, dt =  \\
\end{aligned}$$

$$\begin{aligned}
 & \sim \Delta t \frac{1}{\Delta t} \int_{t=-\infty}^{+\infty} f(t) \, \sum_{n=-\infty}^{+\infty} e^{i n \frac{2 \pi}{\Delta t} t} e^{-i 2 \pi \nu t} \, dt =  \\
 & = \sum_{n=-\infty}^{+\infty}  \int_{t=-\infty}^{+\infty} f(t) \, e^{-i 2 \pi \left( \nu - n \nu_s \right) t} \, dt =  \\
 & = \sum_{n=-\infty}^{+\infty} F\left(\nu - n \nu_s \right) = \text{DTFT}(f(t); \Delta t) \ ,
\end{aligned}$$ (eq:dtft:1)

i.e. equals the periodic sum of the Fourier of the original function, with period

$$\nu_s := \frac{1}{\Delta t} \ .$$

From this last sentence and from the [symmetry properties of Fourier transform](complex:fourier:useful-properties:symmetry), **Nyquist-Shannon sampling theorem** follows seamlessly.

```

```{prf:theorem} Nyquist-Shannon sampling theorem
:label: thm-shannon-nyquist

In order to **avoid aliasing** the sampling frequency must be twice the maxiumum[^shannon-max-frequency] frequency in the signal,

$$\nu_s \ge 2 \nu_{max} \ .$$

[^shannon-max-frequency]: Usually there's no such a frequency above which the signal is exactly zero, but usually there's a frequency above which the spectrum of the signal is approximately zero, i.e. below a threshold where it can be treated as zero, and introduce no aliasing.

```

```{dropdown} Alternative form of DTFT
:open:

**todo** check alternative expressions if using the definition of train of impulses instead of the Fourier series of Dirac's comb.

$$\begin{aligned}
 & = \Delta t \int_{t=-\infty}^{+\infty} f(t) \sum_{k=-\infty}^{+\infty} \delta(t - k \Delta t) \, e^{-i 2 \pi \nu t} \, dt = \\
 & = \Delta t \sum_{k=-\infty}^{+\infty} f(k \Delta t)  e^{-i 2 \pi \nu k \Delta t} = \text{DTFT}\left( f(t); \Delta t \right) 
\end{aligned}$$ (eq:dtft:2)


```

(complex:fourier:dft)=
## Discrete Fourier transform

The discrete Fourier transform is a Fourier transform of a finite sequence of $N$ elements $\{ f_n \}_{n=0:N-1}$, defined as

$$F_k := \sum_{n=0}^{N-1} f_n \, e^{-i 2 \pi \frac{k}{N}{n}} \ , \quad \text{for $k = 0:N-1$} \ ,$$

whose inverse transform reads

$$f_n := \frac{1}{N} \sum_{k=0}^{N-1} F_k \, e^{ i 2 \pi \frac{k}{N}{n}} \ , \quad \text{for $n = 0:N-1$} \ ,$$

```{dropdown} Proof of inverse DFT
:open:

$$\begin{aligned}
  \sum_{k=0}^{N-1} F_k e^{i 2 \pi \frac{k n}{N}} 
  & = \sum_{k=0}^{N-1} \sum_{m=0}^{N-1} f_m e^{i 2 \pi \frac{k (n-m)}{N}} = \\
  & = \sum_{m=0}^{N-1} f_m \sum_{k=0}^{N-1} e^{i 2 \pi \frac{k (n-m)}{N}} = \\
  & = \sum_{m=0}^{N-1} f_m \left\{\begin{aligned}
    & 0 && m \ne n \\
    & N && m = n  \\
  \end{aligned}\right\} = \\
  & = \sum_{m=0}^{N-1} f_m \, N \, \delta_{mn} = N \, f_n \ .
\end{aligned}$$


```


```{dropdown} Fourier transform of the sum of shifted integral functions sampled with a Dirac comb
:open:

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

<!--
<span style="color:red"> **todo** **check!** check the change of coordinates that makes DTFT appear</span>
-->

Using the relation between sampling time $\Delta t$ and sampling period $T = N \Delta t$, $\Delta \nu = \frac{1}{T}$, and thus

$$\Delta t \, \Delta \nu = \Delta t \, \frac{1}{T} = \frac{1}{N} \ ,$$

it follows 

$$\begin{aligned}
\mathscr{F}\left\{ \Delta t \, \tilde{f}(t) \, \text{III}_{\Delta t}(t) \right\}(\nu) 
 & = \text{DTFT}(f(t), \Delta t) \, \Delta \nu \, \text{III}_{\Delta \nu}(\nu) = \\
 & = \Delta t \Delta \nu \sum_{k=-\infty}^{+\infty} f(k \Delta \tau_n) e^{-i 2 \pi \nu k \Delta \tau_n} \text{III}_{\Delta \nu}(\nu) = \\
 & = \frac{1}{N} \sum_{k=-\infty}^{+\infty} f(k \Delta \tau_n) e^{-i 2 \pi \nu k \Delta \tau_n} \ \text{III}_{\Delta \nu}(\nu) \ .
\end{aligned}$$

```

(complex:fourier:useful-properties)=
## Useful properties

(complex:fourier:useful-properties:dirac-comb)=
### Dirac's comb $\text{III}_{\Delta t}(t)$
Dirac comb $\text{III}_{\Delta t}(t)$ is defined as a train of Dirac's delta

$$\text{III}_{\Delta t}(t) = \sum_{m=-\infty}^{+\infty} \delta(t-m \Delta t) \ .$$

Dirac comb $$\text{III}_{\Delta t}(t)$$ is a $\Delta t$-periodic (generalized) function. Thus (...), it can be represented as its Fourier series, here in the exponential form {eq}`eq:fourier-series:exp`, as

$$\text{III}_{\Delta t}(t) \sim \sum_{n=-\infty}^{+\infty} c_n e^{i n \frac{2 \pi}{\Delta t} t}\ .$$

with coefficients given by {eq}`eq:fourier-series:exp:coeff`

$$\begin{aligned}
  c_n 
  & = \frac{1}{\Delta t} \int_{t=-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}} \text{III}_{\Delta t}(t) \, e^{-i n \frac{2\pi}{\Delta t} t} = \\
  & = \frac{1}{\Delta t} \int_{t=-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}} \sum_{m=-\infty}^{+\infty} \delta(t - m \Delta t) \, e^{-i n \frac{2\pi}{\Delta t} t} = \\
  & = \frac{1}{\Delta t} \int_{t=-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}} \delta(t) \, e^{-i n \frac{2\pi}{\Delta t} t} = \frac{1}{T} \ .
\end{aligned}$$

The Fourier series of Dirac comb $\text{III}_{\Delta t}(t)$ reads

$$\text{III}_{\Delta t}(t) = \sum_{m=-\infty}^{+\infty} \delta(t-m \Delta t) \sim \frac{1}{\Delta t} \sum_{n=-\infty}^{+\infty} e^{i n \frac{2\pi}{\Delta t} t} \ ,$$

i.e. as an infinite sum of uniform-amplitude harmonics with discrete frequencies $\nu_n$, that are integer multiple of a fundamental freqeuncy $\nu_s = \frac{1}{\Delta t}$, being $\Delta t$ the sampling time (time-step of the discrete sequence), inverse of sampling frequency.



(complex:fourier:useful-properties:symmetry)=
### Symmetry of Fourier transform










