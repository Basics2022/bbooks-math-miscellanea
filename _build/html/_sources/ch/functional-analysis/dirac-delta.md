(functional-analysis:distributions)=
# Distributions (or generalized functions)
...

(functional-analysis:dirac-delta)=
## Dirac's delta

Dirac's delta $\delta(x)$ is a distribution, or generalized function, with the following properties

1. 

   $$\int_{D} \delta(x-x_0) \, dx = 1  \quad \text{if $x_0 \in D$}$$

2. 

   $$\int_{D} f(x) \delta(x-x_0) \, dx \quad \text{if $x_0 \in D$}$$

for $\forall f(x)$ "regular" **todo** *what does regular mean?*

### Dirac's delta in terms of regular functions

**Approximations ...**

$$\delta(x) \sim r_{\varepsilon}(x) = \begin{cases} \frac{1}{\varepsilon} & x \in \left[-\frac{\varepsilon}{2}, \frac{\varepsilon}{2} \right] \\ 0 & \text{otherwise} \end{cases}$$

as

1. Unitariety

   $$\int_{x=-\infty}^{\infty} r_{\varepsilon}(x-x_0) \, dx = \int_{x=x_0-\frac{\varepsilon}{2}}^{x_0+\frac{\varepsilon}{2}} \frac{1}{\varepsilon} \, dx = 1 \ ,  $$

   for $\forall \varepsilon$;

2. Shift property, using mean-value theorem of continuous functions

   $$\int_{x=-\infty}^{\infty} r_{\varepsilon}(x-x_0) f(x) \, dx = \int_{x=x_0-\frac{\varepsilon}{2}}^{x_0+\frac{\varepsilon}{2}} \frac{1}{\varepsilon} f(x) \, dx = \frac{1}{\varepsilon} \varepsilon f(\xi) \ ,  $$

    with $\xi \in \left[x_0-\frac{\varepsilon}{2}, x_0+\frac{\varepsilon}{2}\right]$, for the mean value theorem. As $\varepsilon \rightarrow 0$, $\xi \rightarrow x_0$, and thus

   $$\int_{x=-\infty}^{\infty} r_{\varepsilon}(x-x_0) f(x) \, dx \rightarrow f(x_0) $$

$$\delta(x) \sim t_{\varepsilon}(x) = \begin{cases} \frac{2}{\varepsilon} \left( 1 - \frac{2 |x|}{\varepsilon} \right) & x \in \left[-\frac{\varepsilon}{2}, \frac{\varepsilon}{2} \right] \\ 0 & \text{otherwise} \end{cases}$$

as

1. Unitariety

   $$\int_{x=-\infty}^{\infty} t_{\varepsilon}(x-x_0) \, dx = \int_{x=x_0-\frac{\varepsilon}{2}}^{x_0+\frac{\varepsilon}{2}} \frac{2}{\varepsilon} \left( 1 - \frac{2 |x|}{\varepsilon} \right) \, dx = \frac{1}{2} \varepsilon \frac{2}{\varepsilon} = 1 \ ,  $$

   for $\forall \varepsilon$;

2. Shift property, using mean-value integration scheme in $x \in \left[x_0-\frac{\varepsilon}{2}, x_0 \right]$,  $x \in \left[x_0, x_0+\frac{\varepsilon}{2} \right]$ (**todo** *why?*)

   $$\begin{aligned}
   \int_{x=-\infty}^{\infty} t_{\varepsilon}(x-x_0) f(x) \, dx
   & = \int_{x=x_0-\frac{\varepsilon}{2}}^{x_0+\frac{\varepsilon}{2}} \frac{2}{\varepsilon} \left( 1 - \frac{2 |x-x_0|}{\varepsilon} \right)  f(x) \, dx = \\
   & = \int_{x=x_0-\frac{\varepsilon}{2}}^{x_0} \frac{2}{\varepsilon} \left( 1 - \frac{2 |x-x_0|}{\varepsilon} \right)  f(x) \, dx 
     + \int_{x=x_0}^{x_0+\frac{\varepsilon}{2}} \frac{2}{\varepsilon} \left( 1 - \frac{2 |x-x_0|}{\varepsilon} \right)  f(x) \, dx = \\
   & = \frac{\varepsilon}{2} \frac{2}{\varepsilon} \left( 1 - \frac{2}{\varepsilon}\frac{\varepsilon}{4} \right)  f\left(x_0-\frac{\varepsilon}{4} \right) \, dx 
     + \frac{\varepsilon}{2} \frac{2}{\varepsilon} \left( 1 - \frac{2}{\varepsilon}\frac{\varepsilon}{4} \right)  f\left(x_0+\frac{\varepsilon}{4} \right) \, dx = \\
   & = \frac{1}{2} f\left( x_0 - \frac{\varepsilon}{4} \right) + \frac{1}{2} f\left( x_0 + \frac{\varepsilon}{4} \right)
   \end{aligned}$$

   As $\varepsilon \rightarrow 0$

   $$\int_{x=-\infty}^{\infty} t_{\varepsilon}(x-x_0) f(x) \, dx \rightarrow f(x_0) $$

**Approximation 1.** For $\alpha \rightarrow +\infty$,

$$\varphi_{\alpha}(x) = \sqrt{\frac{\alpha}{\pi}}e^{-\alpha x^2} \sim \delta(x)$$

Fourier transform of $\varphi_{\alpha}(x)$ reads

$$\begin{aligned}
 \mathscr{F}\{ \varphi_{\alpha}(x) \}(k)
 & = \int_{x=-\infty}^{+\infty} \varphi_\alpha(x) e^{-ikx} \, dx = \\
 & = \int_{x=-\infty}^{+\infty} \sqrt{\frac{\alpha}{\pi}} e^{-\alpha x^2} e^{-ikx} \, dx = \\
 & = \sqrt{\frac{\alpha}{\pi}} \int_{x=-\infty}^{+\infty} e^{-\alpha \left( x + i \frac{k}{2 \alpha} \right)^2} \, dx \, e^{-\frac{k^2}{4 \alpha}} = \\
 & = \sqrt{\frac{\alpha}{\pi}} \, \sqrt{\frac{\pi}{\alpha}} \, e^{-\frac{k^2}{4 \alpha}} =  e^{-\frac{k^2}{4 \alpha}} \ ,\\
\end{aligned}$$

for $\alpha \rightarrow +\infty$,

$$\mathscr{F}\{ \varphi_{\alpha}(x) \}(k) \rightarrow 1$$

and thus $\varphi_\alpha(x) \rightarrow \delta(x)$ for $\alpha \rightarrow +\infty$.

**Approximation 2.** For $a \rightarrow +\infty$ 

$$\frac{1}{2 \pi} \int_{k=-2\pi a}^{2 \pi a} e^{i k x} \, dk = \int_{y=-a}^{+a} e^{i 2 \pi y x} \, dy \sim \delta(x)$$

or

$$\begin{aligned}
  \delta(x)
  & \sim \frac{1}{2 \pi} \int_{k=-2\pi a}^{2 \pi a} e^{i k x} \, dk = \frac{1}{2 \pi} \left( \int_{k=-2\pi a}^{0} e^{i k x} \, dk +  \int_{0}^{k=2\pi a} e^{i k x} \, dk \right) = \frac{1}{2 \pi} \int_{k = 0}^{2 \pi a} \left( e^{ikx} + e^{ikx} \right) \, dx = \frac{1}{\pi} \int_{x=0}^{2 \pi a} \cos(k x) \, dk \\
  & = \int_{y=-a}^{+a} e^{i 2 \pi y x} \, dy = \dots = \int_{y = 0}^{a} (e^{i 2 \pi y x} + e^{i 2 \pi y x}) \, dy = 2 \int_{y=0}^{a} \cos(2 \pi y x) \, dy \ .
\end{aligned}$$

**Approximation 3.** For $a \rightarrow +\infty$ 

$$\frac{\sin(2 \pi x a)}{\pi x} \sim \delta(x)$$

Directly follows from integral of approximation 2,

$$\int_{y=-a}^{+a} e^{i 2 \pi y x} \, dy = \frac{1}{i 2 \pi x} \left. e^{i 2 \pi y x}\right|_{y=-a}^{+a} = \frac{1}{\pi x} \frac{e^{i 2 \pi a x} - e^{-i 2 \pi a x}}{2 i} = \frac{\sin(2 \pi x a)}{\pi x}$$

**Approximation 4.** For $x \in [-\pi, \pi]$, and $N \rightarrow +\infty$

$$\frac{1}{2\pi}\sum_{n=-N}^{N} e^{i n x} = \frac{1}{2 \pi} \frac{\sin\left(\left(N+\frac{1}{2}\right)x\right)}{\sin\left( \frac{x}{2} \right)} \sim \delta(x)$$

<!--
Fourier transform reads

$$\begin{aligned}
\mathscr{F}\left\{ \int_{y=-\infty}^{+\infty} e^{i 2 \pi y x} \, dy \right\}(z)
& = \int_{x=-\infty}^{+\infty} \int_{y=-\infty}^{+\infty} e^{i 2 \pi y x} \, dy \, e^{-i 2 \pi z x} \, dx = \\
& = \int_{y=-\infty}^{+\infty} \int_{x=-\infty}^{+\infty} e^{i 2 \pi (y-z) x} \, dx \, dy = \\
& = \lim_{X \rightarrow +\infty} \int_{y=-\infty}^{+\infty} \frac{1}{i 2 \pi (y-z)} \left[ e^{i 2 \pi (y-z) X} - e^{-i 2 \pi (y-z) X} \right] \, dy = \\ 
& = \lim_{X \rightarrow +\infty} \int_{w=-\infty}^{+\infty} \frac{1}{i 2 \pi w} \left[ e^{i 2 \pi w X} - e^{-i 2 \pi w X} \right] \, dw = \\ 
& = \lim_{X \rightarrow +\infty} \int_{w=-\infty}^{+\infty} \frac{\sin(2\pi w X)}{\pi w} \, dw = \\ 
& = \lim_{X \rightarrow +\infty} \int_{w=-\infty}^{+\infty} \frac{\sin(2\pi w X)}{2 \pi w X} \, d ( 2 \pi w X ) \frac{1}{\pi} = \\
& = \lim_{X \rightarrow +\infty} \dots
\end{aligned}$$
-->

(integral:e^x2)=
```{dropdown} Integral $I = \int_{-\infty}^{+\infty} e^{-\alpha x^2} \, dx$

$$\begin{aligned}
  I^2 
  & = \int_{x=-\infty}^{+\infty} e^{-\alpha x^2} \, dx \, \int_{y=-\infty}^{+\infty} e^{-\alpha y^2} \, dy = \\
  & = \int_{x=-\infty}^{+\infty} \int_{y=-\infty}^{+\infty} e^{-\alpha (x^2 + y^2)} \, dx \, dy = \\
  & = \int_{\theta=0}^{2\pi} \int_{r=0}^{+\infty} e^{-\alpha r^2} \, r \, dr \, d \theta = \\
  & = 2 \pi \frac{1}{2 \alpha} \int_{r=0}^{+\infty} e^{-\alpha r^2} d \left(\alpha r^2 \right) = \\
  & = \frac{\pi}{\alpha} \left[ - e^{\alpha r^2} \right]\bigg|_{r = 0}^{+\infty} = \frac{\pi}{\alpha} \ .
\end{aligned}$$
```


