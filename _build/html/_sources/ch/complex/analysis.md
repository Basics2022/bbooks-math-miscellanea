(complex:analysis)=
# Complex Analysis

(complex:analysis:fun)=
## Complex functions, $f: \mathbb{C} \rightarrow \mathbb{C}$

A complex function $f$ of complex variable $z = x + i y$, $f: \mathbb{C} \rightarrow \mathbb{C}$, can be written as

$$f(z) = \tilde{u}(z) + i \tilde{v}(z) = u(x,y) + i v(x,y) \ ,$$

as the sum of its real part $u(z)$ and $i$ times its imaginary part $v(x,y)$. Here $x,y \in \mathbb{R}$, while $\tilde{u}(z), \tilde{v}(z): \mathbb{C} \rightarrow \mathbb{R}$ and $u(x,y), v(x,y): \mathbb{R}^2 \rightarrow \mathbb{R}$. With some abuse of notation, tilde won't be always explicitly written when arguments of real and imaginary parts of $f$ functions won't be written.

(complex:analysis:fun:limit)=
### Limit

$$\lim_{z \rightarrow z_0} f(z) = f(z_0) \qquad , \qquad \forall \varepsilon > 0 \ \exists \delta > 0 \ \text{ s.t. } \  |f(z) - f(z_0)| < \delta \ \forall z \text{ s.t. } |z - z_0| < \varepsilon, \ z \ne z_0 \ .$$

(complex:analysis:fun:derivative)=
### Derivative

Using the definition of [limit of complex functions](complex:analysis:fun:derivative), the derivative of a function $f: \mathbb{C} \rightarrow \mathbb{C}$, if it exists, is the limit of incremental ratio,

$$f'(z) = \lim_{\Delta z \rightarrow 0} \frac{f(z + \Delta z) - f(z)}{\Delta z} \ .$$

(complex:analysis:fun:line-integral)=
### Line Integrals

Given a line $\gamma \in \mathbb{C}$, whose parametric form is $z(s)$, with regular parametrization with parameter $s \in [s_0, s_1]$, 

$$\int_{\gamma} f(z) \, dz = \int_{s=s_0}^{s_1} f(z(s)) \, z'(s) \, ds \ .$$

(complex:analysis:holo-fun)=
## Holomorphic Functions - Analytic Functions

```{prf:definition}
A holomorphic function is a function whose [derivative](complex:analysis:fun:derivative) exists.
```

**Examples of analytic functions.** **todo**...

(complex:analysis:holo-fun:cauchy-riemann)=
### Cauchy-Riemann conditions

For a holomorphic function $f(z) = u(x,y) + i v(x,y)$, Cauchy-Riemann conditions

$$\begin{cases}
u_{/x} = v_{/y} \\
u_{/y} = - v_{/x}
\end{cases}$$

hold. The evaluation of the derivative once with $\Delta z = \Delta x$ and once with $\Delta z = i \Delta y$

$$\begin{aligned}
& f'(z) = \lim_{\Delta z \rightarrow 0} \frac{f(z+\Delta z) - f(z)}{\Delta z} = \\ 
& = \left\{
\begin{aligned}
  \lim_{\Delta x \rightarrow 0} \frac{f(x+\Delta x,y) - f(x,y)}{\Delta x} = \lim_{\Delta x \rightarrow 0} \frac{u(x+\Delta x,y) + i v(x+\Delta x,y) - u(x,y) - i v(x,y)}{\Delta x} = u_{/x} + i v_{/x} \\ 
  \lim_{\Delta y \rightarrow 0} \frac{f(x,y+\Delta y) - f(x,y)}{i \Delta y} = \lim_{\Delta y \rightarrow 0}  \frac{u(x,y+\Delta y) + i v(x,y+\Delta y) - u(x,y) - i v(x,y)}{i \Delta y} = -i u_{/y} + v_{/y} \\ 
\end{aligned}
\right.
\end{aligned}$$

provides the proof.

(complex:analysis:holo-fun:cauchy-thm)=
### Cauchy Theorem
For a holomorphic function $f$, $f: \Omega \subseteq \mathbb{C} \rightarrow \mathbb{C}$

$$\oint_{\gamma} f(z) \, dz = 0 \ ,$$

for $\forall \gamma \subset \Omega$. Proof follows from [Green's lemma](multivariable-calculus:green-lemma), and [Cauchy-Riemann conditions](complex:analysis:holo-fun:cauchy-riemann)

$$\begin{aligned}
  \oint_{\gamma} f(z) dz & = \oint_{\gamma} \left( u(x,y) + i v(x,y) \right) \left( dx + i dy \right) = \\
  & = \oint_{\gamma} \left( u dx - v dy \right) + i \oint_{\gamma} \left( u dy + v dx \right) = \\
  & = - \int_{S} \left( \underbrace{u_{/y} + v_{/x}}_{=0} \right) \, dx \, dy + i \int_{S} \left( \underbrace{u_{/x} - v_{/y}}_{=0}  \right) \, dx \, dy = 0 \ .
\end{aligned}$$


(complex:analysis:useful-int)=
## Useful integrals

(complex:analysis:useful-int:path-independence)=
### Independence of line integral for holomorphic functions
For a function $f(z)$ analytic in $D$, the line integral on paths $\ell_{ab,i}$ with the same extreme points $a$, $b$ contained in $D$ is independent on the path, but only depends on the extreme points $a$, $b$,

$$\int_{\ell_{ab,1}} f(z) \, dz = \int_{\ell_{ab,2}} f(z) \, dz$$

The proof readily follows, using [Cauchy theorem](complex:analysis:holo-fun:cauchy-thm) applied to a function $f(z): D \subseteq \mathbb{C} \rightarrow \mathbb{C}$, analytic in $D$, and splitting the closed path $\gamma$ into two paths $\ell_1$, $\ell_2$ with the same extreme points, $\gamma = \ell_1 \cup (- \ell_2)$

$$0 = \oint_{\gamma} f(z) \, dz = \int_{\ell_1} f(z) \, dz + \int_{-\ell_2} f(z) \, dz = \int_{\ell_1} f(z) \, dz - \int_{\ell_2} f(z) \, dz \ .$$

(complex:analysis:useful-int:path-independence:sum)=
### Sum and difference of line integrals

(complex:analysis:useful-int:path-independence:z^n)=
### Integral of $z^n$

Given a path $\gamma$ embracing $z=0$ only once in counter-clockwise direction, and $n \in \mathbb{Z}$

$$\oint_{\gamma} z^n \, dz = \left\{ \begin{aligned}  2 \pi i & \qquad \text{if $n = -1$} \\ 0 & \qquad \text{otherwise} \end{aligned} \right.$$

Since $z^n$ is analytic everywhere (**todo** *prove it! Add a section with proofs for common functions*) except for $z=0$, it's possible to evaluate the integral on a circle with center $z=0$ and radius $R$. Using polar expression of the complex numbers on the circle, $z = R e^{i \theta}$, $\theta \in [0, 2 \pi]$, $R$ const, the differential becomes $dz = i R e^{i \theta} d \theta$ and the integral

$$\begin{aligned}
\oint_{\gamma} z^n \, dz
  & = \int_{\theta=0}^{2 \pi} \left( R e^{i\theta}\right)^n i R e^{i \theta} d \theta = \\
  & = i \int_{\theta=0}^{2 \pi} R^{n+1} e^{i (n+1) \theta} d \theta = \\
  & = \left\{ \begin{aligned}
    & \text{if $n=-1$} & : & \quad  i 2 \pi \\
    & \text{otherwise} & : & \quad  i R^{n+1} \frac{1}{i(n+1)} \left.e^{i(n+1)\theta}\right|_{\theta=0}^{2\pi} = \frac{R^{n+1}}{n+1} ( 1 - 1 ) = 0 \\
  \end{aligned} \right.\\
\end{aligned}$$

(complex:analysis:mero-fun)=
## Meromorphic functions

```{prf:definition}
A meromorphic function in a domain is a function holomorphic everywhere except for a (finite?) number of poles. **check**
```

(complex:analysis:singularities)=
### Singularities

```{prf:definition} Pole
A pole of order $n$ of a function $f(z)$ is a complex number $a$ so that

$$f(z) = \frac{\phi(z)}{(z-a)^n} \ ,$$

with $\phi(z)$ holomorphic in $\phi(a) \ne 0$ 
```

**Examples.** ...

```{prf:definition} Branch

```

**Examples.** $f(z) = z^{\frac{1}{2}}$

```{prf:definition} Removable singularities
```

**Example.** $f(z) = \frac{\sin z}{z}$

**Other irregularities.**


(complex:analysis:mero-fun:laurent)=
### Laurent Series
Given a function $f(z)$, in a disk $D_{a,\varepsilon}: 0 < |z-a| < \varepsilon$, its Laurent series centered in $a$ is the convergent (to $f(z)$, **todo** *which type of convergnence?*) series

$$f(z) \sim \sum_{n=-\infty}^{+\infty} a_n (z-a)^n \ ,$$ (eq:laurent)

with

$$a_n = \frac{1}{2 \pi i}\int_{\gamma} f(z) \, (z-a)^{-(n+1)} \, dz$$ (eq:laurent:coeff)

and $\gamma$ embracing $z = a$ once counter-clockwise. Proof follows immediately inserting the expressions of the coefficients $a_n$ and using the [integral of $z^n$](complex:analysis:useful-int:path-independence:z^n). Evaluating the integral {eq}`eq:laurent:coeff` of the coefficients of the Laurent series, using {eq}`eq:laurent` to replace $f(z)$ with its series

$$\begin{aligned}
  a_n & = \frac{1}{2 \pi i}\oint_{\gamma} \sum_{m=-\infty}^{+\infty} a_m (z-a)^m (z-a)^{-(n+1)} = \\
  & = \frac{1}{2 \pi i} \oint_{\gamma} \sum_{m=-\infty}^{+\infty} a_m (z-a)^{m - n - 1}  \, dz = \\
  & = \frac{1}{2 \pi i} \oint_{\gamma} a_n \, z^{-1} \, dz = \\
  & = a_n \ . 
\end{aligned}$$

**todo** *Some freestyle with function and its convergent series...add some detail, and the meaning of convergence*

(complex:analysis:mero-fun:cauchy-formula)=
### Cauchy formula
For an analytic function $f(z)$,

$$f(a) = \frac{1}{2 \pi i} \oint_{\gamma} \frac{f(z)}{z-a} \, dz$$

Proof readily follows using the [integral of $z^n$](complex:analysis:useful-int:path-independence:z^n) on the Taylor series of $\frac{f(z)}{z-a}$ whose $0^{th}$ order term reads $f(a)$,

$$\frac{1}{2\pi i} \oint_{\gamma} \frac{f(a)+\sum_{m=1}^{+\infty} f'(a) (z-a)^m}{z-a} \, dz = \frac{1}{2\pi i} \oint_{\gamma} \frac{f(a)}{z-a} \, dz = f(a) \frac{2 \pi i}{2 \pi i} = f(a) \ .$$

(complex:analysis:mero-fun:residues)=
### Residues

```{prf:definition} Residue
The residue of function $f$ in $a$, $\text{Res}(f,a)$ is a complex number $R$ so that $f(z) - \frac{R}{(z-a)}$ has analytic antiderivative in a disk $D_{a,\varepsilon}: \ 0 < |z-a| < \varepsilon$.
```

**todo** Explain this definition. Couldn't be possible to use $\text{Res}(f,a) = \frac{1}{2 \pi i} \oint_{\gamma} f(z) \, dz = a_{-1}$ instead?

**Properties.**
- If $f(z)$ is analytic in $D_{a,\varepsilon}$ and has a pole of order $n$ in $z = a$, its Laurent series has $a_m=0$ for $m < n$ and reads

  $$f(z) = \sum_{m=-n}^{+\infty} a_m (z-a)^m \ ,$$ (eq:laurent:pole-n)

  with $a_{-n} \ne 0$. Since $f(z)$ has a pole of order $n$ in $z = a$, it can be written as

  $$f(z) = \frac{\phi(z)}{(z-a)^n} \ ,$$

  with $\phi(z)$ analytic in $D_{a,\varepsilon}$ and $\phi(a) \ne 0$. Since $\phi(z)$ is analytic, it has a Taylor series (or a Laurent series with non-negative powers),

  $$\phi(z) \sim \sum_{m=0}^{+\infty} b_m (z-a)^m \ ,$$

  (**todo** *prove it! Extension of the real case. Add a link to the proof*) and thus

  $$f(z) \sim \sum_{m=0}^{+\infty} b_m (z-a)^{m-n} = \sum_{m=-n}^{+\infty} b_{m+n} (z-a)^{m} = \sum_{m=-n}^{+\infty} a_{m} (z-a)^m \ , $$

  with $a_m = b_{m+n}$.

- For simple closed path $\gamma$ (embracing $a$ only once counter-clokwise) in $D_{a, \varepsilon}$,

  $$\oint_{\gamma} f(z) \, dz = 2 \pi i a_{-1} = 2 \pi i \text{Res}(f,a)$$ (eq:residue-thm:0)

  The proof readily follows, using the [integral of $z^n$](complex:analysis:useful-int:path-independence:z^n) and Laurent series {eq}`eq:laurent` of $f(z)$,

  $$\oint_{\gamma} f(z) \, dz = \oint_{\gamma} \sum_{m=-\infty}^{+\infty} a_m (z-a)^m \, dz = 2 \pi i a_{-1} \ .$$

- For a pole $a$ of order $n$, the following holds

  $$a_{-1} =  \frac{1}{(n+1)!} \lim_{z \rightarrow a} \frac{d^{n-1}}{dz^{n-1}} \left[ (z-a)^n \, f(z) \right]$$

  The proof follows using Laurent series {eq}`eq:laurent:pole-n} for a function with pole of order $n$, and evaluating the $(n-1)^{th}$ order derivative

  $$\begin{aligned}
   \frac{d^{n-1}}{dz^{n-1}} \left[ (z-a)^n f(z) \right] 
    & = \frac{d^{n-1}}{dz^{n-1}} \left[ (z-a)^n \sum_{m=-n}^{+\infty} a_n (z-a)^m \right] = \\
    & = \dfrac{d^{n-1}}{dz^{n-1}} \left[ \sum_{m=-n}^{+\infty} a_n (z-a)^{m+n} \right] = \\
    & = \dfrac{d^{n-1}}{dz^{n-1}} \left[ \sum_{m=0}^{+\infty} a_{m-n} (z-a)^{m} \right] = \\
    & = \dfrac{d^{n-2}}{dz^{n-2}} \left[ \sum_{m=0}^{+\infty} m a_{m-n} (z-a)^{m-1} \right] = \\
    & = \dfrac{d^{n-3}}{dz^{n-3}} \left[ \sum_{m=0}^{+\infty} m(m-1) a_{m-n} (z-a)^{m-2} \right] = \\
    & = \dots = \\
    & = \left[ \sum_{m=0}^{+\infty} m! \, a_{m-n} (z-a)^{m-n+1} \right] \\
  \end{aligned}$$

  and then letting $z \rightarrow a$, so that only the term with $m-n+1 = 0$ survives
  
  $$\lim_{z \rightarrow a} \frac{d^{n-1}}{dz^{n-1}} \left[ (z-a)^n \sum_{m=-n}^{+\infty} a_n (z-a)^m \right] = (n-1)! \, a_{-1} \ .$$


(complex:analysis:mero-fun:residues-thm)=
### Residue Theorem

```{prf:theorem} Residue Theorem
Given $f(z)$ with a finite number of poles $p_n \in D$, then

$$\int_{\gamma} f(z) \, dz = 2 \pi i \ \sum_{n} I(\gamma, p_n) \text{Res}(f,p_n) \ ,$$

being $\gamma$ a path in $D$, and $I(\gamma, p_n)$ the winding index of the path $\gamma$ around pole $p_n$ (+1 for each counter-clockwise loop, -1 for each clockwise loop).

```
The proof readily follows extending the result for a single pole {eq}`eq:residue-thm:0` to general number of poles and general paths $\gamma$ embracing (with sign) each pole $p_n$ $I(\gamma,p_n)$ times, with the same techinques shown in section [Sum and difference of line integrals](complex:analysis:useful-int:path-independence:sum).


### Evaluation of integrals

### Inverse Laplace Transform
Given Laplace transform

$$F(s) := \mathscr{L}\{f(t)\}(s) := \int_{t=0^-}^{+\infty} f(t) e^{-st} \, dt \ ,$$

the inverse transform can be evaluated as

$$f(t) = \mathscr{L}^{-1}\{F(s)\}(t) := \lim_{T \rightarrow +\infty} \frac{1}{2 \pi i} \int_{s = a-iT}^{a+iT} e^{st} F(s) \, ds \ ,$$

with $a > \text{Re}\{p_n\}$ for each pole of the function $F(s)$, evaluated on the vertical line $s = a+iy$, $y \in [-T,T]$, $ds = i d y$,

$$\begin{aligned}
  \lim_{T \rightarrow +\infty} \frac{1}{2 \pi i} \int_{s = a-iT}^{a+iT} e^{st} F(s) \, ds 
  & = \lim_{T \rightarrow +\infty} \frac{1}{2 \pi i} \int_{s = a-iT}^{a+iT} e^{st} \int_{\tau=0^-}^{+\infty} f(\tau) e^{-s\tau} \, d \tau  \, ds = \\
  & = \lim_{T \rightarrow +\infty} \frac{1}{2 \pi i} \int_{y = -iT}^{iT} e^{(a+iy)t} \int_{\tau=0^-}^{+\infty} f(\tau) e^{-(a+iy)\tau} \, d \tau  \, i dy = \\
  & = \lim_{T \rightarrow +\infty} \frac{1}{2 \pi} \int_{y = -iT}^{iT} \int_{\tau=0^-}^{+\infty} e^{iy(t-\tau)} e^{a(t-\tau)} f(\tau) \, d \tau  \, dy = \\
  & = \dots \\
  & = \int_{\tau=0^-}^{+\infty} \delta(t-\tau) e^{a(t-\tau)} f(\tau) d \tau = f(t) \ .
\end{aligned}$$

having used the transform of [Dirac's delta](functional-analysis:dirac-delta) $\delta(t) = \frac{1}{2\pi} \int_{\omega=-\infty}^{+\infty} e^{-j \omega t} \, d\omega$.

**todo** *If $a > \text{Re}\{p_n\}$, the contour build with the vertical line with real part $a$ and the arc of circumference on its*


