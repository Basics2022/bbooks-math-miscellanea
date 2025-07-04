(ode:lti:stability-fb)=
# LTI: stability and feedback

```{dropdown} Contents
:open:

- Stability of a SISO LTI, w.r.t. non-zero i.c. or impulsive input
- 
- 

```

## Stability of a LTI - SISO

### Transfer function
Let the SISO input-output relation of a LTI system be represented in Laplace domain by the transfer function $G(s)$,

$$y(s) = G(s) u(s)$$

For rational transfer functions

$$G(s) = k \dfrac{\prod_{n=1}^N (z_n - s)}{\prod_{d=1}^{D} (p_d - s)}  = \dfrac{\sum_{n=1}^{N} a_n s^n}{\sum_{d=0}^{D} b_d s^d} \ ,$$

with $z_n$ the zeros, $p_d$ the poles, and $k = \frac{a_0}{b_0} = \lim_{s \rightarrow 0} G(s)$ the static gain. If the system is strictly proper, $N < D$, and the TF can be written as a **sum of partial functions**. As an example, for a transfer function with simple poles

$$G(s) = \sum_{d=1}^{N} \dfrac{A_d}{(p_d-s)} \ , $$

while for a pole $p_d$ with multiplicity $m_d> 1$ all the terms $\propto \frac{1}{(p_d-s)^{e_d}}$, with $e_d = 1:m_d$ must be included, see example below.

$$G(s) = \sum_{d=1}^{N} \dfrac{A_d}{(p_d-s)^{e_d}} \ , $$


```{prf:example} Sum of partial fractions of a TF with poles with multiplicity $> 1$
:class: dropdown

Let's write the rational function $G(s) = \frac{s+1}{(s+2)^3}$ as a sum of partial functions,

$$\begin{aligned}
  G(s)
  & = \dfrac{s+1}{(s+2)^3} = \\
  & = \dfrac{A}{s+2} + \dfrac{B}{(s+2)^2} + \dfrac{C}{(s+2)^3} = \\
  & = \dfrac{A(s+2)^2+B(s+2)+C}{(s+2)^3} = \\
  & = \dfrac{s^2(A) + s(4A + B) + 4A+2B+C}{(s+2)^3} \ ,
\end{aligned}$$

The value of the coefficients $A$, $B$, $C$ is computed comparing the first and the last expression of the numerator of $G(s)$

$$\begin{cases}
  s^2  : \quad A = 0 \\
  s\ \ : \quad 4A + B = 1 \\
  1\ \ : \quad 4A + 2B + C = 1 \\
\end{cases}
\qquad \rightarrow \qquad
\begin{cases}
 A =  0 \\
 B =  1 \\
 C = -1
\end{cases}$$

and thus

$$G(s) =  \dfrac{s+1}{(s+2)^3} = \dfrac{1}{(s+2)^2} - \dfrac{1}{(s+2)^3} \ . $$

```

### Stability w.r.t. non-zero initial conditions - or w.r.t. implusive input - in time domain

Transfer function $G(s)$ represents the free the function w.r.t. impulsive input. Response in time domain can be evaluated as the inverse Laplace transform of the transfer function,

$$y(t) = \mathscr{L}^{-1} \left\{ y(s) \right\} = \mathscr{L}^{-1} \left\{ \sum_{n_d=1}^{D} \dfrac{R_d}{(s-p_d)} \right\} = \sum_{d=1}^{D} R_d \, e^{p_d t} \ .$$

If $\text{re}\{ p_d \} < 0$ for $\forall d$, then the response is asymptotically stble for $t \rightarrow +\infty$, as $|e^{p_d t}| = e^{\text{re}\{p_d\} t} \rightarrow 0$, for $t \rightarrow + \infty$.


## Stability of closed-loop systems

### Cauchy argument principle

For the [Cauchy argument principle](complex:analysis:mero-fun:cauchy-argument-principle), the difference of argument of function $F(s)$ when $s$ performs a counter-clockwise loop over th contour $\Gamma$ enclosing poles $p_n$, and zeros $z_d$ of the function $F(s)$ reads

$$\Delta \text{arg} \{ F(s) \} = \sum_{n} \text{arg}(s - z_n) - \sum_{d} \text{arg}(s-p_d) = Z 2 \pi - P 2 \pi = (Z-P) 2 \pi \ , $$

and thus the the diagram of function $F(s)$ performs 

$$N =  Z - P$$ (eq:cauchy-arg-principle)

loops around the origin $0+i 0$ of the complex plane.


### Nyquist stability criterion

Nyquist stability criterion provides some conditions for the stability of a closed loop transfer function 

$$G_c(s) := \dfrac{G(s)}{1+G(s)} \ , $$

being $G(s)$ the open loop transfer function, and the feedback with the opposite of the output ($y = G(s) \left( u - y \right)$).

The poles of the closed loop systems are the zeros of the function $1 + G(s)$. If the closed-loop system is asymptotically stable, it must have no pole with positive real part. As the complex variable $s$ performs a clockwise (and thus, the signs of the relation change w.r.t. Cauchy argument criterion) loop over **Nyquist path** (semicircle in the RHS half-plane; then **todo** discuss the case where poles and zeros are on the imaginary axis...deform the path...). No zero of $1 + G(s)$ with positive real part means $Z = 0$. Using the relation between poles, zeros and loops around the origin given by Cauchy argument principle {eq}`eq:cauchy-arg-principle`, and recalling the opposite direction, it follows that

$$N = P \ ,$$

in order to have $Z = 0$, i.e. the diagram of $1+G(s)$ must perform $N$ counter-clockwise loops around $0+i0$ equal to the number of its poles with positive real parts. As the poles of $1+ G(s)$ are the same as the poles of $G(s)$, it's possible to formulate Nyquist criterion looking at $G(s)$, as 

```{prf:theorem} Nyquist criterion

In order for the closed-loop system to be asymptotically stable, the diagram of the open-loop transfer function $G(s)$ must perform a number $N$ of counter-clocwise loops around the *critical point* $-1 + i \, 0$ equal to the number of its zeros with positve real part.

```

### Bode stability criterion for minimal phase systems

```{prf:definition} Minimal phase systems

```

...

Safetry gain margin, safety phase margin...

```{prf:theroem} Bode stability criterion

```


