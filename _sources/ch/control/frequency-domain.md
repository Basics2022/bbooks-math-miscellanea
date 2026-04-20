(control:frequency)=
# Frequency domain control

(control:frequency:siso)=
## Stability of closed-loop SISO systems

Let $L(s) = G(s) R(s)$ the open-loop transfer function of the the system represented in {numref}`fig-nyquist-block`: the system is explicitly represented as a combination of a plant with transfer function $G(s)$ and a regulator with transfer function $R(s)$. The output of the system $y$, and the error $e = y - y_{ref}$ are related with the reference signals as

$$\begin{aligned}
  y(s) & = \frac{L(s)}{1 + L(s)} y_{ref}(s) \\
  e(s) & = \frac{ 1  }{1 + L(s)} y_{ref}(s) \ .
\end{aligned}$$ (eq:nyquist:tfs)

:::{figure} ./../../media/control/control-reference-nyquist.png
:alt: Nyquist theorem block diagram
:align: center
:name: fig-nyquist-block

Block diagram of the closed-loop system with retroaction on the output error $e = y_{ref} - y$. Here, $G(s)$ is the plant transfer function, $R(s)$ is the regulator transfer function (that can be designed to control a given plant), and $L(s) = G(s) R(s)$ is defined as the open-loop transfer function.

:::

```{dropdown} Details

In Laplace domain, neglecting here the initial conditions,

$$\begin{aligned}
  y = G u = G R e = G R ( y_{ref} - y ) \ ,
\end{aligned}$$

and thus, with $L = G R$ and SISO system (so that TF are not matrix but scalar functions)

$$y(s) = \frac{L(s)}{1 + L(s)} y_{ref}(s) \ .$$

For the output error,

$$e(s) = y_{ref} - y = y_{ref} - G R e \ ,$$

and thus

$$e(s) = \frac{1}{1 + L(s)} y_{ref} \ .$$

```

(control:frequency:siso:cauchy-argument)=
### Cauchy argument principle

For the [Cauchy argument principle](complex:analysis:mero-fun:cauchy-argument-principle), the difference of argument of function $F(s)$ when $s$ performs a counter-clockwise loop over th contour $\Gamma$ enclosing poles $p_n$, and zeros $z_d$ of the function $F(s)$ reads

$$\Delta \text{arg} \{ F(s) \} = \sum_{n} \text{arg}(s - z_n) - \sum_{d} \text{arg}(s-p_d) = Z 2 \pi - P 2 \pi = (Z-P) 2 \pi \ , $$

and thus the the diagram of function $F(s)$ performs 

$$N =  Z - P$$ (eq:cauchy-arg-principle)

loops around the origin $0+i 0$ of the complex plane.


(control:frequency:siso:nyquist)=
### Nyquist stability criterion

Nyquist stability criterion provides the conditions for the stability of the closed loop transfer functions {eq}`eq:nyquist:tfs`. As shown in section about [stability of LTI systems](ode:lti:stability-fb), a linear system is asymptotically stable if all of its poles have negative real parts.

All the closed-loop transfer functions have the same poles (as they have the same denominator, except for *dangerous* cancellations not changing the stability but the observability or the controllability **todo** *Discuss*). 

The poles of the closed loop systems are the zeros of the function $1 + L(s)$. If the closed-loop system is asymptotically stable, it must have no pole with positive real part. As the complex variable $s$ performs a clockwise (and thus, the signs of the relation change w.r.t. Cauchy argument criterion) loop over **Nyquist path** (semicircle in the RHS half-plane; then **todo** discuss the case where poles and zeros are on the imaginary axis...deform the path...). No zero of $1 + G(s)$ with positive real part means $Z = 0$. Using the relation between poles, zeros and loops around the origin given by Cauchy argument principle {eq}`eq:cauchy-arg-principle`, and recalling the opposite direction, it follows that

$$N = P \ ,$$

in order to have $Z = 0$, i.e. the diagram of $1+G(s)$ must perform $N$ counter-clockwise loops around $0+i0$ equal to the number of its poles with positive real parts. As the poles of $1+ G(s)$ are the same as the poles of $G(s)$, it's possible to formulate Nyquist criterion looking at $G(s)$, as 

```{prf:theorem} Nyquist theorem
:label: thm-nyquist

In order for the closed-loop system to be asymptotically stable, the diagram of the open-loop transfer function $G(s)$ must perform a number $N$ of counter-clocwise loops around the *critical point* $-1 + i \, 0$ equal to the number of its zeros with positve real part.

```

(control:siso:bode)=
### Bode stability criterion for minimal phase systems

```{prf:definition} Minimal phase systems
:label: def-minimal-phase

...

```

...


```{prf:theorem} Bode stability criterion
:label: thm-bode

...

```

(control:siso:phase-margin)=
### Phase margin

(control:siso:gain-margin)=
### Gain margin

