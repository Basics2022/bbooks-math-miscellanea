(pde:hyperbolic)=
# Hyperbolic problems

Hyperbolic problems often come from a small-amplitude linearization, or as the non-diffusion (or inviscid) limit of a more general problem.

As a result of these simplification, these problems may experience **shocks** (i.e. discontinuity in the solution, where the differential equations stop to hold, and integral equations and jump conditions are required). **todo** *classification of discontinuities on the massflow across the surface*

The very nature of these problem also suggest methods for the solution or the analysis of these equations, like **characteristic method**.

(pde:hyperbolic:scalar-linear)=
## Scalar linear

### 1-dimensional

$$\partial_t u(x,t) + a \partial_x u(x,t) = f(x,t)$$

**Caracteristic method.** $U(t) = u(X(t), t)$, with the caracteristic curves $X(t)$ defined as those curves where the PDE becomes a ODE. Evaluating the time derivative of the function $u(X(t),t)$, the hyperbolic equation can be recast as

$$\dfrac{d U}{dt} + \left[ a(X(t),t) - \dfrac{d X}{d t} \right] \partial_x u = f(X(t),t) \ .$$

The equation of characteristic lines is

$$\dfrac{d X}{d t} = a(X(t), t) \ ,$$

and the PDE on characteristic line becomes the ODE

$$\dfrac{d U}{d t}(X(t), t) = f(X(t), t) \ .$$

(pde:hyperbolic:scalar-non-linear)=
## Scalar non-linear

(pde:hyperbolic:system-linear)=
## System linear

### 1-dimensional

$$\mathbf{u}(x,t)$$

$$\partial_t \mathbf{u} + \mathbf{A} \partial_x \mathbf{u} = \mathbf{f}$$

**Characteristics.** $\mathbf{U}(t) = \mathbf{u}(X(t), t)$

$$\dfrac{d \mathbf{U}}{dt} - \dfrac{d X}{dt} \partial_x \mathbf{u} + \mathbf{A} \partial_x \mathbf{u} = \mathbf{f}$$

In order to get the equations of characteristic lines where PDE turns into ODEs, the eigenproblem

$$\mathbf{A} \partial_x \mathbf{u} = \dfrac{d X}{d t} \partial_x \mathbf{u} \ ,$$

holds. This problem has non trivial solution if $\frac{d X}{dt}$ and $\partial_x \mathbf{u}$ are pairs of eigenvalues and (right) eigenvectors of the array $\mathbf{A}$.

**Diagonalization.**

$$\mathbf{A} = \mathbf{R} \symbf{\Lambda} \mathbf{L}$$

$$\mathbf{L} \left[ \partial_t \mathbf{u} + \mathbf{R} \symbf{\Lambda} \mathbf{L} \partial_x \mathbf{u} \right] = \mathbf{L} \mathbf{f} $$

Since $\mathbf{L} = \mathbf{R}^{-1}$, and defining $d \mathbf{q} = \mathbf{L} d \mathbf{u}$, it's possible to recast the original problem in diagonal form

$$\partial_t \mathbf{q} + \symbf{\Lambda} \partial_x \mathbf{q} = \mathbf{L} \mathbf{f}$$

$$\partial_t q_i + \Lambda_i \partial_x q_i = \sum_{k} R_{ik} \, f_k =: F_i \ .$$

Thus, on the $i^{th}$ family of characteristic lines, $\dfrac{d X}{dt} = \lambda_i$,

$$\dfrac{d Q_i}{d t} = F_i$$

(pde:hyperbolic:system-non-linear)=
## System non-linear

### 1-dimensional space

$$\mathbf{u}(x,t)$$

$$\begin{aligned}
  & \partial_t \mathbf{u} + \partial_x \mathbf{F}(\mathbf{u}) = \mathbf{f}  && \text{(conservative form)} \\
  & \partial_t \mathbf{u} + \partial_{\mathbf{u}} \mathbf{F}(\mathbf{u}) \partial_x \mathbf{u} = \mathbf{f}  && \text{(convective form)} \\
\end{aligned}$$

## n-dimensional space

$$\mathbf{u}(\vec{r}, t)$$

$$\begin{aligned}
  & \partial_t \mathbf{u} + \nabla \cdot \mathbf{F}(\mathbf{u}) = \mathbf{f}  && \text{(conservative form)} \\
  & \partial_t \mathbf{u} + \nabla \mathbf{u} \cdot \partial_{\mathbf{u}} \mathbf{F}(\mathbf{u}) = \mathbf{f}  && \text{(convective form)} \\
\end{aligned}$$

Different descritpions of integral problem,

$$\begin{aligned}
  \dfrac{d}{dt} \int_V \mathbf{u} + \oint_{\partial V} \hat{n} \cdot \mathbf{F}(\mathbf{u}) & = \int_V \mathbf{f} && \quad \text{(Eulerian)} \\
  \dfrac{d}{dt} \int_{V_t} \mathbf{u} - \oint_{\partial V_t} \mathbf{u} \vec{u} \cdot \hat{n} + \oint_{\partial V_t} \hat{n} \cdot \mathbf{F}(\mathbf{u}) & = \int_{V_t} \mathbf{f} && \quad \text{(Lagrangian)} \\
  \dfrac{d}{dt} \int_{v_t} \mathbf{u} - \oint_{\partial v_t} \mathbf{u} \vec{u}_b \cdot \hat{n} + \oint_{\partial v_t} \hat{n} \cdot \mathbf{F}(\mathbf{u}) & = \int_{v_t} \mathbf{f} && \quad \text{(arbitrary)}
\end{aligned}$$

**todo** *in coordinates*

$$\begin{aligned} 
  f_i
  & = \partial_t u_i + \partial_{x_k} F_{ki} (u_l) = \\
  & = \partial_t u_i + \partial_{x_k} u_m \partial_{u_m} F_{ki} (u_l) = \\
\end{aligned}$$


```{prf:example} P-system in 1-dimensional domain

$$\begin{cases}
 \partial_t \rho + u \partial_x \rho + \rho \partial_x u = 0 \\
 \rho \partial_t u + \rho u \partial_x u + \partial_x P = 0 \\
\end{cases}$$

with $\partial_x P = a^2 \partial_x \rho$, 

**Convective form**

$$\partial_t \begin{bmatrix} \rho \\ u \end{bmatrix} + \begin{bmatrix} u & \rho \\ \frac{a^2}{\rho} & u \end{bmatrix} \partial_x \begin{bmatrix} \rho \\ u \end{bmatrix} = \underline{0} \ .$$

**Conservative form**

$$\partial_t \begin{bmatrix} \rho \\ \rho u \end{bmatrix} + \partial_x \begin{bmatrix} \rho u \\ \rho u^2 + \rho a^2 \end{bmatrix} = \underline{0} \ .$$


**Spectral decomposition** of $\mathbf{A}(\mathbf{u})$ gives

$$0 = \left| \begin{bmatrix} u - s & \rho \\ \frac{a^2}{\rho} & u - s \end{bmatrix} \right| = (u - s)^2  - a^2$$

$$\begin{aligned}
  s_{1,2} & = u \mp a \\
  \mathbf{R} & = \begin{bmatrix} \rho & \rho \\ a & -a  \end{bmatrix} \\
  \mathbf{L} & = \frac{1}{2 \rho a} \begin{bmatrix} a & \rho \\ a & -\rho  \end{bmatrix} \\
\end{aligned}$$

```

```{prf:example} Euler equations in 1-dimensional domain

**Conservative form**

$$\partial_t \begin{bmatrix} \rho \\ \rho u \\ \rho e^t \end{bmatrix} + \partial_x \begin{bmatrix} \rho u \\ \rho u^2 + P \\ \rho u h^t  \end{bmatrix} = \underline{0} \ ,$$

with $h^t = e^t + \frac{P}{\rho}$ and $e^t = e + \frac{u^2}{2}$, and the pressure field can be written as a function of the other thermodynamic variables. As an example, using conservative variables $(\rho, m, E^t) = (\rho, \rho u, \rho e^t) = \left(\rho, \rho u, \rho \left(e + \frac{u^2}{2}\right) \right)$

$$P(\rho, e) = P\left(\rho, \frac{E^t}{\rho} - \frac{m^2}{2 \rho^2}\right) = \Pi\left( \rho, m, E^t \right)$$

so that

$$\begin{aligned}
 \partial_{\rho} \Pi & = \partial_\rho P \big|_e + \partial_e P \big|_\rho \left( -\frac{E^t}{\rho^2} + \frac{m^2}{\rho^3} \right) \\
 \partial_{m   } \Pi & = \partial_e P \big|_\rho \left( - 2 \frac{m}{\rho^2}  \right) \\
 \partial_{E^t } \Pi & = \partial_e P \big|_\rho \left( \frac{1}{\rho} \right) \\
\end{aligned}$$



$$dP = \left( \frac{\partial P}{\partial \rho} \right)_{e} d \rho + \left( \frac{\partial P}{\partial e} \right)_{\rho} d e$$

while starting from $P(s, \rho)$

$$\begin{aligned}
  dP
  & = \left( \frac{\partial P}{\partial \rho} \right)_{s} d \rho + \left( \frac{\partial P}{\partial s} \right)_{\rho} d s = \\
  & = c^2(\rho, s) d \rho + \left( \frac{\partial P}{\partial s} \right)_{\rho} d s  \ .
\end{aligned}$$

$$P(\rho, s(\rho, e))$$

$$d P = \partial_\rho P \big|_{s} d \rho + \partial_s P\big|_{\rho} \left( \partial_{\rho} s \big|_{e} d \rho + \partial_e s \big|_{\rho} d e  \right)$$

and using $d s = \frac{d e}{T} - \frac{P}{\rho^2 T} d \rho \ ,$

$$P(\rho, s) = P(\rho, e(\rho, s))$$

$$\begin{aligned}
  c^2
  & = \partial_\rho P\big|_s = \\
  & = \partial_\rho P\big|_e + \partial_e P\big|_{\rho} \, \partial_\rho e\big|_s = \\
  & = \partial_\rho P\big|_e + \frac{P}{\rho^2} \partial_e P \big|_{\rho} \ ,
\end{aligned}$$

**Conservative form in conservative variables.**

$$\partial_t \begin{bmatrix} \rho \\ m \\ E^t \end{bmatrix} + \partial_x \begin{bmatrix} m \\ \frac{m^2}{\rho} + \Pi(\rho,m,E^t) \\ \frac{m}{\rho} \left(E^t + \Pi(\rho, m, E^t)\right)  \end{bmatrix} = \underline{0} \ ,$$

**Convective form in conservative variables.**

$$\partial_t \begin{bmatrix} \rho \\ m \\ E^t \end{bmatrix} + \partial_x \begin{bmatrix} 0 & 1 & 0 \\ - \frac{m^2}{\rho^2} + \partial_\rho \Pi & \frac{2 m}{\rho} + \partial_m \Pi & \partial_{E^t} \Pi \\ - \frac{m}{\rho^2}(E^t+\Pi)+ \frac{m}{\rho}\partial_\rho \Pi & \frac{1}{\rho} (E^t + \Pi) + \frac{m}{ \rho} \partial_{m} \Pi & \frac{m}{\rho} \left( 1 + \partial_{E^t} \Pi \right)  \end{bmatrix} \partial_x \begin{bmatrix} \rho \\ m \\ E^t \end{bmatrix}  = \underline{0} \ ,$$

**Spectral decomposition** of $\mathbf{A}(\mathbf{u})$

$$
  0
  & = \left| \begin{bmatrix} -s & 1 & 0 \\ 
   -u^2 + \partial_\rho \Pi & 2 u + \partial_m \Pi - s & \partial_{E^t} \Pi \\
   - u \left(e^t+\frac{P}{\rho} \right)+ u \partial_\rho \Pi & e^t + \frac{P}{\rho} + u \partial_{m} \Pi & u \left( 1 + \partial_{E^t} \Pi \right) - s
  \end{bmatrix} \right| = \\
  & = - s \left[ \left( 2 u + \partial_m \Pi - s  \right) \left( u \left( 1 + \partial_{E^t} \Pi \right) - s \right) - \partial_{E^t} \Pi \left( h^t + u \partial_m \Pi \right) \right] + \\
  & \quad - u h^t \partial_{E^t} \Pi + u \partial_\rho \Pi \partial_{E^t} \Pi + \\
  & \quad + (u^2 - \partial_\rho \Pi) \left( u (1 + \partial_{E^t} \Pi) - s \right)
$$

```
