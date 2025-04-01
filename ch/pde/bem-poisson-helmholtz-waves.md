<!--
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
-->

(math:green-function)=
# Green's function method

(classical-electromagnetism:green-function:poisson)=
## Poisson equation

General Poisson's problem

$$\begin{cases}
  - \nabla^2 \mathbf{u}(\mathbf{r}, t) = \mathbf{f}(\mathbf{r},t) \\
  \text{+ b.c.}
\end{cases}$$

with common boundary conditions

$$\begin{cases}
\mathbf{u} = \mathbf{g} & \quad \text{on $S_D$} \\
\hat{\mathbf{n}} \cdot \nabla \mathbf{u} = \mathbf{h} & \quad \text{on $S_N$}
\end{cases}$$

over Dirichlet and Neumann regions of the boundary.

Poisson's problem for Green's function, in infinite domain

$$
  - \nabla_{\mathbf{r}}^2 G(\mathbf{r}; \mathbf{r}_0) = \delta(\mathbf{r} - \mathbf{r}_0) \\
$$

Green's function method

$$\begin{aligned}
  E(\mathbf{r}_0, t) u_i(\mathbf{r}_0, t) 
  & =   \int_{\mathbf{r} \in \Omega} u_i(\mathbf{r},t) \delta(\mathbf{r}-\mathbf{r}_0) = \\
  & = - \int_{\mathbf{r} \in \Omega} u_i(\mathbf{r},t) \nabla_{\mathbf{r}}^2 G(\mathbf{r}-\mathbf{r}_0) = \\
  & = - \int_{\mathbf{r} \in \Omega} \nabla_{\mathbf{r}} \cdot ( u_i \nabla_{\mathbf{r}} G - G \nabla_{\mathbf{r}} u_i) - \int_{\mathbf{r} \in \Omega} G \nabla^2 u_i= \\
  & = - \oint_{\mathbf{r} \in \partial \Omega} \hat{\mathbf{n}} \cdot ( u_i \nabla_{\mathbf{r}} G - G \nabla_{\mathbf{r}} u_i) + \int_{\mathbf{r} \in \Omega} G(\mathbf{r}-\mathbf{r}_0) f_i(\mathbf{r}, t) . \\
\end{aligned}$$

An integro-differential boundary problem can be written using boundary conditions. As an example, using Dirichlet and Neumann boundary conditions, the integro-differential problem reads

$$\begin{aligned}
&  E(\mathbf{r}_0, t) \mathbf{u}(\mathbf{r}_0, t) 
+ \int_{\mathbf{r} \in S_N} \mathbf{u}(\mathbf{r},t) \, \hat{\mathbf{n}} \cdot \nabla_{\mathbf{r}} G(\mathbf{r}-\mathbf{r}_0)
- \int_{\mathbf{r} \in S_D} G(\mathbf{r}-\mathbf{r}_0) \, \hat{\mathbf{n}} \cdot \nabla_{\mathbf{r}} \mathbf{u}(\mathbf{r},t) = \\ 
& =
- \int_{\mathbf{r} \in S_D} \mathbf{g}(\mathbf{r},t) \, \hat{\mathbf{n}} \cdot \nabla_{\mathbf{r}} G(\mathbf{r}-\mathbf{r}_0)
+ \int_{\mathbf{r} \in S_N} G(\mathbf{r}-\mathbf{r}_0) \, \mathbf{h}(\mathbf{r},t)  
+ \int_{\mathbf{r} \in \Omega} G(\mathbf{r}-\mathbf{r}_0) \, \mathbf{f}(\mathbf{r}, t) . \\
\end{aligned}$$

Green's function of the Poisson-Laplace equation reads

$$G(\mathbf{r};\mathbf{r}_0) = \frac{1}{4 \pi} \frac{1}{\left| \mathbf{r}-\mathbf{r}_0 \right|} \ .$$

```{dropdown} Green's function of the Laplace equation

$$-\nabla^2 G = 0 \qquad \text{for $\mathbf{r} \ne \mathbf{r}_0$}$$

Solutions with spherical symmetry,

$$0 = \nabla^2 G = \frac{1}{r^2} \left( r^2 G' \right)'
\quad \rightarrow \quad
G'(r) = \frac{A}{r^2} \quad \rightarrow \quad G(r) = - \frac{A}{r} + B
$$

Choosing $B = 0$ s.t. $G(r) \rightarrow 0$ as $r \rightarrow \infty$, and integrating over a sphere centered in $r=0$ to get $A = -\frac{1}{4 \pi}$,

$$1 = \int_{V} \delta(r) = - \int_{V} \nabla^2 G = - \oint_{\partial V} \hat{\mathbf{n}} \cdot \nabla G
= -\oint_{\partial V} \hat{\mathbf{r}} \cdot \hat{\mathbf{r}} \frac{A}{r^2} = - 4 \pi \, A $$

```

(classical-electromagnetism:green-function:helmholtz)=
## Helmholtz equation

**todo** from Fourier to Laplace trasnform in the first lines of this section

A Helmholtz's equation can be thouoght as the time Fourier transform of a wave equation,

$$\begin{cases}
  \dfrac{1}{c^2} \partial_{tt} \mathbf{u}(\mathbf{r},t) - \nabla^2 \mathbf{u}(\mathbf{r},t) = \mathbf{f}(\mathbf{r},t) \\
  \text{+ b.c.} \\
  \text{+ i.c.} \ ,
\end{cases}$$

Fourier transform in time of field $\mathbf{u}(\mathbf{r},t)$ reads

$$\tilde{\mathbf{u}}(\mathbf{r}, \omega) = \mathscr{F}\{ \mathbf{u}(\mathbf{r},t) \} = \int_{t=-\infty}^{+\infty} \mathbf{u}(\mathbf{r},t) e^{-i \omega t} \, d \omega$$

and, if $\mathbf{u}(\mathbf{r},t)$ is compact in time, Fourier transform of its time partial derivatives read

$$\begin{aligned}
  \mathscr{F}\{ \dot{\mathbf{u}}(\mathbf{r},t) \} 
  & = \int_{t=-\infty}^{+\infty} \dot{\mathbf{u}}(\mathbf{r},t) e^{-i \omega t} \, d \omega = \\
  & = \mathbf{u}(\mathbf{r},t) e^{-i \omega t} \big|_{t=-\infty}^{+\infty} + i \omega \int_{t=-\infty}^{+\infty} \mathbf{u}(\mathbf{r},t) e^{-i \omega t} \, d \omega = \\
  & = i \omega \mathscr{F}\{  \mathbf{u}(\mathbf{r},t) \}
\end{aligned}$$

$$\mathscr{F}\{ \partial_t^n \mathbf{u}(\mathbf{r},t) \} = (i \omega)^n \tilde{\mathbf{u}} \ .$$

The differential problem in the transformed domain thus reads

$$- \frac{\omega^2}{c^2} \tilde{\mathbf{u}} - \nabla^2 \tilde{\mathbf{u}} = \tilde{\mathbf{f}}$$

Green's function of Helmholtz'e equation reads

$$G(\mathbf{r}, s) =
  \alpha^+ \frac{e^{ \frac{s|\mathbf{r} - \mathbf{r}_0|}{c}}}{|\mathbf{r} - \mathbf{r}_0|} +
  \alpha^- \frac{e^{-\frac{s|\mathbf{r} - \mathbf{r}_0|}{c}}}{|\mathbf{r} - \mathbf{r}_0|}
$$

with $\alpha^+ + \alpha^- = \frac{1}{4 \pi}$.

Being the Laplace transform,

$$\mathscr{L}\{ f(t) \} = \int_{t=0^-}^{+\infty} f(t) e^{-st} dt \ ,$$

the Laplace transform of a causal function with time delay $\tau \ge 0$ reads

$$\mathscr{L}\{ f(t-\tau) \} = \int_{t=0^-}^{+\infty} f(t-\tau) e^{-st} dt = \int_{z = - \tau}^{+\infty} f(z) e^{-s(z+\tau)} \, dz = e^{-s\tau} \, \int_{z = 0}^{+\infty} f(z) e^{-s z} \, dz = e^{-s \tau} \, \mathscr{L}\{ f(t) \}$$

having used causality $f(t) = 0$ for $t < 0$. Laplace transform of Dirac's delta $\delta(t)$ reads

$$\mathscr{L}\{ \delta(t) \} = \int_{t=0^-}^{+\infty} \delta(t) \, dt = 1 \ ,$$

so that $e^{-s \tau} = e^{- s \tau} \, 1 = \mathscr{L}\{ \delta(t-\tau) \}$.

Thus, Green's function for the wave equation reads

$$G(\mathbf{r},t; \mathbf{r}_0, t_0) = 
  \alpha^+ \frac{ \delta \left( t - t_0 + \frac{|\mathbf{r}-\mathbf{r}_0|}{c} \right)}{|\mathbf{r} - \mathbf{r}_0|} +
  \alpha^- \frac{ \delta \left( t - t_0 - \frac{|\mathbf{r}-\mathbf{r}_0|}{c} \right)}{|\mathbf{r} - \mathbf{r}_0|}
$$

If $t \ge t_0$, and $G(\mathbf{r}, t; \mathbf{r}_0, t_0)$ connects the past $t_0$ with the future $t$, the first term is not causal, and thus $\alpha^+ = 0$ and

$$G(\mathbf{r},t; \mathbf{r}_0, t_0) = \frac{1}{4 \pi} \frac{ \delta \left( t - t_0 - \frac{|\mathbf{r}-\mathbf{r}_0|}{c} \right)}{|\mathbf{r} - \mathbf{r}_0|} \ .$$


```{dropdown} Green's function of Helmholtz's equation

$$\frac{s^2}{c^2} G - \nabla^2 G = \delta(r)$$

$$G(r) = \frac{\alpha e^{k r} + \beta e^{-kr}}{r}$$

Proof:
- Gradient

  $$\nabla G(r) = \hat{\mathbf{r}} \partial_r G = \hat{\mathbf{r}} \frac{\alpha (k r - 1) e^{kr} + \beta(-k r - 1)e^{-kr}}{r^2}$$

- Laplacian

  $$\begin{aligned}
    \nabla^2 G(r) & = \frac{1}{r^2} \left( r^2 G'(r) \right)' = \\
    & = \frac{1}{r^2} \left(  \alpha (k r - 1) e^{kr} + \beta(-k r - 1)e^{-kr}\right)' = \\
    & = \frac{1}{r^2} \left( \alpha k e^{kr} + \alpha k^2 r  e^{kr} - \alpha k e^{kr} - \beta k e^{-kr} + \beta k^2 r e^{-kr} + \beta k e^{-kr}  \right) = \\
    & = \frac{1}{r} \left( \alpha e^{kr} + \beta e^{-kr} \right) k^2 = k^2 G(r) \ .
  \end{aligned}$$

  and thus $k^2 G(r) - \nabla^2 G = 0$, for $r \ne 0$;

- Unity

  $$1 = \int_{V} \delta(r) = \int_V \left( k^2 G - \nabla^2 G \right) = \int_V k^2 G - \oint_{\partial V} \hat{\mathbf{n}} \cdot \nabla G $$

  the second term is the sum of two contributions of the form

  $$\oint_{\partial V} \hat{\mathbf{n}} \cdot \nabla G^{\pm} = \oint_{\partial V} \frac{\alpha^{\pm}(\pm k r - 1) e^{\pm k r}}{r^2} = 4 \pi \alpha^{\pm} (\pm k r - 1) e^{\pm k r}$$

  the first term is the sum of two contributions of the form

  $$\begin{aligned}
    k^2 \int_{V} G(r)
      & = k^2 \int_{V} \frac{\alpha^{\pm} e^{\pm k r}}{r} = \\
      & = k^2 \alpha^{\pm} \int_{R = 0}^{r} \int_{\phi=0}^{\pi} \int_{\theta=0}^{2 \pi} \frac{e^{\pm k R}}{R} R^2 \sin \phi \, dR \, d \phi \, d \theta = \\
      & = k^2 \alpha^{\pm} \, 4 \pi \int_{R = 0}^{r} R \, e^{\pm k R} \, dR \ .
  \end{aligned}$$

  the last integral can be evaluated with integration by parts

  $$\begin{aligned}
    \int_{R = 0}^{r} R \, e^{\pm k R} \, dR
    & = \left.\left[ \frac{1}{\pm k} e^{\pm k R } R \right]\right|_{R=0}^{r} \mp \frac{1}{k} \int_{R=0}^{r} e^{\pm k R} \, dR = \\
    & = \frac{1}{\pm k} e^{\pm k r } r  - \frac{1}{k^2} e^{\pm k R} + \frac{1}{k^2} = \\
  \end{aligned}$$

  Thus summing everything together,

  $$\begin{aligned}
    1 & = \alpha^+ \left[ 4 \pi k^2 \left( \frac{r}{k} e^{k r} - \frac{1}{k^2} e^{kr} + \frac{1}{k^2} \right) - 4 \pi \left( k r - 1 \right) e^{kr} \right] + \alpha^- \left[ \dots \right] = \\
      & = 4 \pi \left( \alpha^+ + \alpha^- \right) \ .
  \end{aligned}$$

```

(classical-electromagnetism:green-function:waves)=
## Wave equation
Wave equation general problem

$$\begin{cases}
  \dfrac{1}{c^2} \partial_{tt} \mathbf{u}(\mathbf{r},t) - \nabla^2 \mathbf{u}(\mathbf{r},t) = \mathbf{f}(\mathbf{r},t) \\
  \text{+ b.c.} \\
  \text{+ i.c.} \\
\end{cases}$$

Green's problem of the wave equation

$$\frac{1}{c^2} \partial_{tt} G(\mathbf{r},t;\mathbf{r}_0,t_0) - \nabla_{\mathbf{r}}^2 G(\mathbf{r},t;\mathbf{r}_0,t_0) = \delta(\mathbf{r}-\mathbf{r}_0) \delta(t-t_0)$$

Integration by parts

$$\begin{aligned}
  E(\mathbf{r}_{\alpha}, t_{\alpha}) \mathbf{u}(\mathbf{r}_{\alpha},t_{\alpha}) & = \int_{t \in T} \int_{\mathbf{r} \in V} \delta(t-t_{\alpha}) \delta(\mathbf{r}-\mathbf{r}_{\alpha}) \mathbf{u}(\mathbf{r},t) = \\
  & = \int_{t \in T} \int_{\mathbf{r} \in V} \left\{ \frac{1}{c^2} \partial_{tt} G - \nabla^2_{\mathbf{r}} G \right\} \mathbf{u} = \\
  & = \int_{t \in T} \int_{\mathbf{r} \in V} \left\{ \frac{1}{c^2} \left[ \partial_t \left( \mathbf{u} \partial_t G - G \partial_t \mathbf{u} \right) + G \partial_{tt} \mathbf{u} \right] - \nabla_{\mathbf{r}} \cdot \left( \nabla_{\mathbf{r}} G \, \mathbf{u} - G \nabla_{\mathbf{r}} \mathbf{u} \right) - G \, \nabla^2_{\mathbf{r}} \mathbf{u} \right\} = \\
  & = \int_{\mathbf{r} \in V} \frac{1}{c^2} \left[ \mathbf{u}(\mathbf{r},t) \partial_t G(\mathbf{r},t; \mathbf{r}_{\alpha},t_{\alpha}) - G(\mathbf{r},t; \mathbf{r}_{\alpha},t_{\alpha}) \partial_t \mathbf{u}(\mathbf{r},t) \right] \bigg|_{t_0}^{t_1} + \\
  & \quad + \int_{t \in T} \oint_{\mathbf{r} \in \partial V} \left\{ - \hat{\mathbf{n}}(\mathbf{r},t) \cdot \nabla_{\mathbf{r}} G(\mathbf{r},t; \mathbf{r}_{\alpha},t_{\alpha}) \, \mathbf{u}(\mathbf{r},t) + G(\mathbf{r},t; \mathbf{r}_{\alpha},t_{\alpha}) \, \hat{\mathbf{n}}(\mathbf{r},t) \cdot \nabla_{\mathbf{r}} \mathbf{u}(\mathbf{r},t) \right\} + \\
  & \quad + \int_{t \in T}  \int_{\mathbf{r} \in V} G(\mathbf{r},t; \mathbf{r}_{\alpha},t_{\alpha}) \underbrace{ \left\{ \frac{1}{c^2} \partial_{tt} \mathbf{u}(\mathbf{r},t) - \nabla^2_{\mathbf{r}} \mathbf{u}(\mathbf{r},t) \right\}}_{= \mathbf{f}(\mathbf{r},t)} \\
\end{aligned}$$


$$\begin{aligned}
  \int_{t \in T} \int_{\mathbf{r} \in V} \frac{1}{4 \pi}\frac{\delta\left( t-t_{\alpha} + \frac{|\mathbf{r} - \mathbf{r}_{\alpha}|}{c} \right)}{|\mathbf{r} - \mathbf{r}_{\alpha}|} \, \mathbf{f}(\mathbf{r},t) 
  & = \int_{\mathbf{r} \in V \cap B_{|\mathbf{r} - \mathbf{r}_{\alpha}| \le c (t_\alpha - t)}} \frac{1}{4 \pi |\mathbf{r} - \mathbf{r}_{\alpha}|} \mathbf{f}\left(\mathbf{r}, t_{\alpha} - \frac{|\mathbf{r}-\mathbf{r}_{\alpha}|}{c}\right)
\end{aligned}$$




