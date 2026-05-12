(complex:fourier)=
# Fourier Transforms

Fourier transforms are linear transformations of functions usually relating a physical domain of time and/or space, with a domain of frequency and/or wave-vectors.



```{dropdown} Contents.
:open:

[**Fourier series**](complex:fourier:series). Fourier series is defined for finite-domain or periodic, time-continuous functions, or - more generally - continuous functions in the physical domain.

[**Fourier transform**](complex:fourier:transform). Fourier transform is defined for infinite-domain non-periodic, time-continuous functions, or - more generally - continuous functions in the physical domain.

[**Relations between Fourier transforms and sampling**](complex:fourier:transforms). Fourier series, Fourier transform, discrete time Fourier transform and discrete Fourier transforms are presented, and their relations discussed. Fundamental results about **evenly-spaced sampling** seamlessly follows, as **Shannon-Nyquist theorem**, {prf:ref}`thm-shannon-nyquist`, shows.


```
Different Fourier transforms exist, depending if the original function is:
- time discrete/time continuous 
- periodic/non-periodic

| Transform | Time domain | Frequency domain |
| :--- | :--- | :---  |
| Fourier transform   | Continuous function in infinite domain | Continuous function in infinite domain |
| Fourier series      | Continuous function in finite domain (or periodic function in infinite domain) | Discrete function in compact range |
| Discrete-time Fourier transform | Discrete function (or continuous function sampled with Dirac's comb) in infinite domain | Continous periodic spectrum in infinite domain |
| Discrete Fourier transform      | Discrete (or continuous, sampled with Dirac's comb) function in finite domain (or periodic in infinite domain) | Discrete periodic spectrum in infinite domain |

Fourier transforms can be useful in:
- highlighting the frequency content of functions
- solving problems: sometimes, it can be easier to transform a problem in frequency domain, solve it in frequency domain, and transform the solution back to the physical domain



