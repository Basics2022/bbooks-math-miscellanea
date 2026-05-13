(complex:z-transform)=
# Z-transform

```{dropdown} Contents
:open:

* Definition
* Elementary transforms
* Region of convergence
* Applications
  * Solution of difference equations
  * Analysis of stability of numerical integration methods
  * Discrete-time design of filters and discrete-time systems. Relation between continuous-time and discrete-time systems due to sampling. Relation with Laplace transform.

```

(complex:z-transform:def)=
## Definition

Z-transform can be considered as a discrete-time counterpart of the [Laplace transform](complex:laplace), as section [Laplace transform of a sampled function]() tries to show.
Z-transform converts a discrete-time signal $\{ x_n \}$ into a complex-valued function $X(z)$. Similarly to the [definition of Laplace transform](complex:laplace:def-thm:def), Z-transform can be either two-sided

$$X(z) = \mathscr{Z}\{ x_n \}(z) = \sum_{n=-\infty}^{+\infty} x_n z^{-n} \ ,$$

or one-sided

$$X(z) = \mathscr{Z}\{ x_n \}(z) = \sum_{n=0}^{+\infty} x_n z^{-n} \ ,$$

that can be also thought as the two-sided transform of **causal time-series**, i.e. $x_{k} = 0$, $\forall k < 0$.


(complex:z-transform:z-dtft)=
### Z-transform and discrete-time Fourier transform (DTFT)

The [discrete-time Fourier transform](complex:fourier:dtft) of a sequence, that can be written as {eq}`eq:dtft:1`, 

$$\text{DTFT}(x(t); \Delta t)(\nu) = \Delta t \sum_{n=-\infty}^{+\infty} x(n \Delta t)  e^{-i 2 \pi \nu n \Delta t} \ ,$$

can be thought as a scaled Z-transform of the signal, evaluated in $z = i \omega \Delta t = i 2 \pi \nu \Delta t$,

$$\text{DTFT}(x(t); \Delta t)(\nu) = \Delta t \left.\left[ \sum_{n=-\infty}^{+\infty} x_n  z^{-n} \right]\right|_{z=e^{i \omega \Delta t}} = \Delta t X(z=e^{i \omega \Delta t}) \ ,$$


(complex:z-transform:z-laplace)=
### Laplace transform of a sampled function

**Delta sampling.** Let $\widetilde{x}(t) = x(t) \text{III}_{\delta t}(t) = x(t) \sum_{m = - \infty}^{+\infty} \delta(t - m \Delta t)$ the sampling of the continuous-time function $x(t)$ with Dirac's comb. Its one-sided Laplace transform reads

$$\begin{aligned}
  \mathscr{L}\{ \widetilde{x}(t) \}(s)
  & = \int_{t=0^-}^{+\infty} \widetilde{x}(t) e^{-s t} dt = \\
  & = \sum_{m=-\infty}^{+\infty} \int_{t=0^-}^{+\infty} x(t) \delta( t - m \Delta t ) e^{-s t} dt = \\
  & = \sum_{m= 0     }^{+\infty} x(m \Delta t) e^{-s m \Delta t} = \\
  & = \sum_{m= 0     }^{+\infty} x(t_m) e^{-s t_m} = \\
  & = \sum_{m= 0     }^{+\infty} x_m z^{-m} \ ,
\end{aligned}$$ (eq:z-transform:sampling:delta)

with $x_m = x(t_m)$, $t_m = m \Delta t$, and $z = e^{s \Delta t}$. Here the summation runs over $m = 0:+\infty$, as the integral of $\delta(t - m \Delta t)$ produces a non-zero result only for $m \ge 0$. The relation {eq}`eq:z-transform:sampling:delta` shows that the Laplace transform of the Dirac delta sampled function is equivalent to the Z-transform of its samples, if the relations between $t_m$ and $m$ and $z$ and $s \Delta t$ hold.

**Sample and Hold.**

$$\begin{aligned}
  \mathscr{L}\{ \widetilde{x}(t) \}(s)
  & = \int_{t=0^-}^{+\infty} \widetilde{x}(t) e^{-s t} dt = \\
  & = \sum_{m=-\infty}^{+\infty} \int_{t=t_m}^{t_{m+1}} x(t_m) e^{-s t} dt = \\
  & = \sum_{m=-\infty}^{+\infty} x(t_m) \frac{1}{s} \left[ e^{-s t_m} - e^{-s t_{m+1}} \right] = \\
  & = \frac{1 - e^{-s \Delta t}}{s} \sum_{m=-\infty}^{+\infty} x_m e^{-s t_m} = \\
  & = \dots
\end{aligned}$$ (eq:z-transform:sampling:sah)

with $z = e^{s \Delta t}$, $s = \frac{1}{\Delta t} \ln z$.

## Inverse transform

...

## Elementary one-sided transforms

In this section, some elementary Z-transforms are collected. These can be interpreted as the discrete-time counterpart of the [elementary Laplace transforms](complex:laplace:def-thm:elementary)

**Linearity.**

**Kronecker delta.** $x_n = \delta_{0n} = \left\{ \begin{aligned} & 1 && n = 0 \\ & 0 && n \ne 0 \end{aligned}\right.$ 

$$\mathscr{Z}\{ \delta_{0n} \}(z) = \sum_{n=0}^{+\infty} \delta_{n0} z^{-n} = 1 \ .$$

**"Time" delay.** Z-transform of a causal sequence $x_n$ (with $x_n = 0$ for $n < 0$), $x_{n-k}$ with $k \ge 0$

$$
  \mathscr{Z}\{ x_{n-k} \}(z) = z^{-k} X(z)
$$

```{dropdown} Proof

$$\begin{aligned}
  \mathscr{Z}\{ x_{n-k} \}(z) 
  & = \sum_{n=0}^{+\infty} x_{n-k} z^{-n} = \\
  & = \sum_{n=k}^{+\infty} x_{n-k} z^{-(n-k)} z^{-k} = \\
  & = \sum_{n=0}^{+\infty} x_{n} z^{-n} z^{-k} = \\
  & = z^{-k} X(z) \ .
\end{aligned}$$

```

**First difference backward.** Directly follows from the Z-transform of time delay

$$\mathscr{Z}\left\{ x_n - x_{n-1} \right\} = \left( 1 - z^{-1} \right) X(z)$$

**First difference forward.**

**Accumulation.**

**Convolution.**

**Initial value.** If $x_n$ is causal, i.e. $x_n = 0$ for $n < 0$, then

$$x_{0} = \lim_{z \rightarrow +\infty} X(z) \ .$$

```{dropdown} Proof
:open:

$$X(z) = x_0 + \sum_{n=1}^{+\infty} x_n z^{-n}$$

As 

$$\left|\sum_{n=1}^{+\infty} x_n z^{-n} \right| \le \sum_{n=1}^{+\infty} \left| x_n z^{-n} \right| \le M \sum_{n=1}^{+\infty} |z|^{-n} = M \frac{1}{|z|} \frac{1}{1 - \frac{1}{|z|}} \ ,$$

for every $z$, with $|z| > 1$ s.t. the geometric series is convergent. As $|z| \rightarrow + \infty$, the series goes to zero, and thus

$$\lim_{z \rightarrow +\infty} X(z) = x_0 \ .$$


```

**Final value.** If *the poles of $(z-1) X(z)$ are inside the unit circle (condition for as.stability)*, then

$$x_{+\infty} = \lim_{z \rightarrow 1} (z-1) X(z) \ .$$

```{dropdown} Proof
:open:

...


```



## Applications

### Solution of difference equations

From $k$-order difference equation to system of $1$-order difference equations, as it can be done with ODEs. For ODEs

$$x^{(k)} + a_{k-1} x^{(n-1)} + \dots + a_1 \dot{x} + a_0 x = f(t)$$

may be written as a first-order $k$-dimensional system

$$\dot{\mathbf{z}} = \mathbf{f}(\mathbf{z},t) \ $$

$$\begin{bmatrix} \dot{z}_0  \\ \dot{z}_1 \\ \dots \\ \dot{z}_{k-1} \end{bmatrix} = \begin{bmatrix} z_1 \\ z_2 \\ \dots \\ - a_{k-1} z_{k-1} - \dots - a_1 z_1 - a_0 z_0 + f(t) \end{bmatrix}$$

For a difference equation

$$x_{n} + a_{1} x_{n-1} + \dots + a_{k-1} x_{n-k+1} = f_n$$

may be written as

$$\mathbf{z}_{n+1} = \mathbf{f}(\mathbf{z}_n, t_n)$$

$$\begin{bmatrix} z_{0,n} \\ z_{1,n} \\ \dots  \\ z_{k-1,n} \end{bmatrix} = \begin{bmatrix} z_{1,n-1} \\ z_{2,n-1} \\ \dots \\ f_n - a_{1} z_{k-1,n-1} \dots - a_{k-1} z_{0,n-1} \end{bmatrix}$$

with $z_{j,n} = x_{n-k+1+j}$, for $j=0:k-1$. 


### Analysis of stability of numerical integration methods for ODEs






