(ode:lti:stability-fb)=
# LTI: stability and feedback

```{dropdown} Contents
:open:

- Stability of a SISO LTI, w.r.t. non-zero i.c. or impulsive input
- 
- 

```

(ode:lti:stability-fb:siso)=
## Stability of a LTI - SISO

(ode:lti:stability-fb:siso:tf)=
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

(ode:lti:stability-fb:siso:impulsive-input)=
### Stability w.r.t. non-zero initial conditions - or w.r.t. implusive input - in time domain

Transfer function $G(s)$ represents the free the function w.r.t. impulsive input. Response in time domain can be evaluated as the inverse Laplace transform of the transfer function,

$$y(t) = \mathscr{L}^{-1} \left\{ y(s) \right\} = \mathscr{L}^{-1} \left\{ \sum_{n_d=1}^{D} \dfrac{R_d}{(s-p_d)} \right\} = \sum_{d=1}^{D} R_d \, e^{p_d t} \ .$$

If $\text{re}\{ p_d \} < 0$ for $\forall d$, then the response is asymptotically stble for $t \rightarrow +\infty$, as $|e^{p_d t}| = e^{\text{re}\{p_d\} t} \rightarrow 0$, for $t \rightarrow + \infty$.


