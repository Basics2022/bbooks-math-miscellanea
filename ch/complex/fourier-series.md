(complex:fourier:series)=
# Fourier Series

For a $T$-periodic function,

$$g(t) \sim \frac{a_0}{2} + \sum_{n=1}^{+\infty} \left[ a_n \, \cos\left( n \frac{2\pi}{T} t \right) + b_n \, \sin\left( n \frac{2 \pi }{T} t \right) \right] \ ,$$

**todo** Prove it with properties of integrals of $\sin$ and $\cos$ over $t \in \left[ 0, T \right]$; prove convergence to average value at jumps

The exponential form reads

$$g(t) \sim \sum_{n=-\infty}^{+\infty} c_n e^{i n \frac{2 \pi }{T}t} \ ,$$ (eq:fourier-series:exp)

where 

$$c_n = \frac{1}{T} \int_{t=0}^{T} f(t) \, e^{-i n \frac{2\pi}{T} t} \ .$$ (eq:fourier-series:exp:coeff)

```{dropdown} Proof

Exploiting the properties of integrals of complex exponentials with $k \in \mathbb{Z}$

$$\int_{t=0}^{T} e^{i k \frac{2 \pi}{T} t} \, dt = 
\begin{cases}
\frac{1}{i k \frac{2 \pi}{T}} \left.\left[ e^{ik \frac{2\pi}{T} t} \right]\right|_{t=0}^{T} = 0 & \hfill \qquad \text{if $ k \ne 0$} \\
T & \hfill \text{if $ k = 0$}
\end{cases}
$$

$$\int_{t=0}^{T} f(t) e^{-i m \frac{2 \pi}{T} t} \, dt
 \sim \int_{t=0}^{T} \sum_{n=-\infty}^{+\infty} c_n e^{i n \frac{2 \pi }{T}t}  e^{-i m \frac{2 \pi}{T} t}
 \sim \sum_{n=-\infty}^{+\infty} c_n \sim \int_{t=0}^{T} e^{i (n-m) \frac{2 \pi }{T}t} 
 \sim T \, c_m \ .
$$
```

