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

#### Method of characteristics
**Characteristics.** $\mathbf{U}(t) = \mathbf{u}(X(t), t)$

$$\dfrac{d \mathbf{U}}{dt} - \dfrac{d X}{dt} \partial_x \mathbf{u} + \mathbf{A} \partial_x \mathbf{u} = \mathbf{f}$$

In order to get the equations of characteristic lines where PDE turns into ODEs, the eigenproblem

$$\mathbf{A} \partial_x \mathbf{u} = \dfrac{d X}{d t} \partial_x \mathbf{u} \ ,$$

holds. This problem has non trivial solution if $\frac{d X}{dt}$ and $\partial_x \mathbf{u}$ are pairs of eigenvalues and (right) eigenvectors of the array $\mathbf{A}$.

**Diagonalization.**

$$\mathbf{A} = \mathbf{R} \symbf{\Lambda} \mathbf{L}$$

$$\mathbf{L} \left[ \partial_t \mathbf{u} + \mathbf{R} \symbf{\Lambda} \mathbf{L} \partial_x \mathbf{u} \right] = \mathbf{L} \mathbf{f} $$

Since $\mathbf{L} = \mathbf{R}^{-1}$, and defining the **characteristic variables** by $d \mathbf{q} = \mathbf{L} d \mathbf{u}$ - in linear problems matrix $\mathbf{A}$ is constant, and so its spectral decomoposition, and thus $\mathbf{q} = \mathbf{L} \mathbf{u}$ - , it's possible to recast the original problem in diagonal form

$$\partial_t \mathbf{q} + \symbf{\Lambda} \partial_x \mathbf{q} = \mathbf{L} \mathbf{f}$$

$$\partial_t q_i + \Lambda_i \partial_x q_i = \sum_{k} L_{ik} \, f_k =: F_i \ .$$

Thus, on the $i^{th}$ family of characteristic lines, $\dfrac{d X}{dt} = \lambda_i$, $Q_i(t) = q_i(x(t), t)$ evolves as

$$\dfrac{d Q_i}{d t} = F_i \ .$$

If $F_i = \left[ \mathbf{L} \mathbf{f} \right]_i = 0$, the characteristic variable $q_i$ is constant along the characteristic lines. Once the characteristic variables are determined, the conservative variables are evalauted as $\mathbf{u}(x,t) = \mathbf{R} \mathbf{q}(x,t)$.

#### Domain of influence and domain of dependence

#### Riemann problem
A Riemann problem is defined as the evolution of the initial state 

$$\mathbf{u}(x,t_0) =
  \begin{cases}
  \mathbf{u}_a \ , \hfill \quad x < x_0 \\
  \mathbf{u}_b \ , \hfill \quad x > x_0 \\
\end{cases}$$

This problem is quite useful in quite a wide range of numerical methods for hyperbolic problems - Godunov schemes in Finite Volume Methods -, to evaluate the **boundary state** to be used numerical flux.

For linear problems, the matrix $\mathbf{A}$ is constant ad so it is its spectral decomposition, $\mathbf{A} = \mathbf{R} \symbf{\Lambda} \mathbf{L}$, and the solution of a Riemann problem of an homogeneous linear hyperbolic system can be easily determined analytically with the method of characteristics,

Let's change the origin of space and time, so that the initial state is in $t=0$, and the jump in the initial condiiton in $x = 0$. Each charactersitic variable $q_k(x, t)$ is constant on its family of characteristic lines, $x = X_k(t) = x_{0,k} + \lambda_k t$.

$$q_k(x,t) = q_k(x_{0,k} + \lambda_k t, t) = q_k(x_{0,k}, 0) = q_k(x - \lambda_k t, 0) = L_{ki} u_j(x - \lambda_k t, 0) \ .$$

Thus, the solution in conservative variables $\mathbf{u}(x,t)$ in $x$ at time $t$ reads

$$\begin{aligned}
  \mathbf{u}(x,t) & = \mathbf{R} \mathbf{q}(x,t) \\
  u_i(x,t) & = R_{ik} q_k(x,t) = R_{ik} q_k(x-\lambda_k t, 0) = R_{ik} L_{kj} u_j(x-\lambda_k t, 0) \\
\end{aligned}$$

In a Riemann problem for a $N$-dimensional linear system the solution shows $N+1$ homogeneous regions (at most, in general the same number as the number of the non-coincident eigenvalues $+1$), delimited by the characteristic lines with origin in the discontinuity. Sorting the eigenvalues in increasing order

$$\lambda_1 > \lambda_2 > \dots > \lambda_N \ ,$$

and defining the homogeneous regions

$$\begin{aligned}
  S_0 & : \frac{x}{t} \in (-\infty, \lambda_1) \\
  S_1 & : \frac{x}{t} \in (\lambda_1, \lambda_2) \\
  \dots & \\
  S_i & : \frac{x}{t} \in (\lambda_i, \lambda_{i+1}) \\ 
  \dots & \\
  S_{N-1} & : \frac{x}{t} \in (\lambda_{N-1}, \lambda_{N}) \\ 
  S_{N}   & : \frac{x}{t} \in (\lambda_{N}, +\infty) \\ 
\end{aligned}$$

the solution is in the $S_i$ region is

$$u_i(x,t) = \sum_{\lambda_k > \frac{x}{t}} R_{ik} q_{a,k} +  \sum_{\lambda_k < \frac{x}{t}} R_{ik} q_{b,k}$$ 

```{prf:example} Linear(ized) P-system
:class: dropdown

The linear(ized) P-system around a uniform reference state $\overline{\rho}$, $\overline{u}$ in convective form reads

$$
  \partial_t \begin{bmatrix} \rho \\ u \end{bmatrix} + \begin{bmatrix} \overline{u} & \overline{\rho} \\ \frac{a^2}{\overline{\rho}} & \overline{u} \end{bmatrix} \partial_x \begin{bmatrix} \rho \\ u \end{bmatrix} = \mathbf{0} \ .
$$

**Spectral decomposition.**

$$0 = \left| -\lambda \mathbf{I} + \mathbf{A} \right| = (\overline{u}-\lambda)^2 - a^2$$

$$\lambda_{12} = \overline{u} \mp a \qquad , \qquad \mathbf{r}_{12} = \begin{bmatrix} \overline{\rho} \\ \mp a \end{bmatrix} $$

$$\begin{aligned}
  \mathbf{R} & = \begin{bmatrix} \overline{\rho} & \overline{\rho} \\ - a & a \end{bmatrix} \\
  \mathbf{L} & = \mathbf{R}^{-1} = \frac{1}{2 \overline{\rho} a} \begin{bmatrix} a & -\overline{\rho} \\ a & \overline{\rho} \end{bmatrix} \\
\end{aligned}$$

**Reference state.**

$$|u| \ : \  
\begin{cases}
   = 0 \hfill \qquad \text{at rest} \\
   < a \hfill \qquad \text{subsonic flow} \\
   > a \hfill \qquad \text{supersonic flow to the left/right} \\
\end{cases}
$$

Subsonic: the two families of characteristic lines have opposite direction; supersonic: the two families of characteristic lines have the same direction.

```

```{prf:example} Linearized shallow water equations
```

```{prf:example} Linearized Euler equations (acoustics)
```

```{prf:example} Wave equation
:class: dropdown

A wave equation arises in many different fields of science. As an example, 1-dimensional wave equation descrives the axial dynamics of a truss

$$m \partial_{tt} u - EA \partial_{xx} u = f \ ,$$

that can be recast in the general expression of wave equation

$$\partial_{tt} u - c^2 \partial_{xx} u = F$$

The $2^{nd}$ order differential operator appearing in 1-dimensional wave equation can be factored as the "product" of 2 $1^{st}$ order differentail operators, 

$$\left( \partial_{tt} - c^2 \partial_{xx} \right) u = \left( \partial_t - c \partial_x \right) \left( \partial_t + c \partial_x \right) u$$

and thus a wave equation can be written as

$$\begin{cases}
  \partial_t u + c \partial_x u - w = 0 \\
  \partial_t w - c \partial_x w     = F \\
\end{cases}$$

In the regime of small displacement, the velocity field is the partial time derivative of the dispalcement field, $v = \partial_t u$, and the axial force reads $N = EA \partial_x u$. Exploiting Schwartz's theorem about mixed partial derivatives to write $\partial_t N = EA \partial_x v$, it's possible to write the wave function as the following system of hyperbolic equations in the physical unknowns $v, N$

$$\begin{cases}
  \partial_t N - EA \partial_x v = 0 \\
  \partial_t v - \frac{1}{m}\partial_x N = f
\end{cases}$$


**P-system and wave equation - reference state at rest, $\ \overline{u} = 0$.**

$$\begin{cases}
  \partial_t \rho + \overline{\rho} \partial_x u = 0 \\
  \partial_t u    + \frac{a^2}{\overline{\rho}} \partial_x \rho = 0 \\
\end{cases}$$

Taking time partial derivative of the first and space partial derivative of the second equation times $\overline{\rho}$, and evaluating their difference, a wave equation for $rho$ appears

$$\partial_{tt} \rho - a^2 \partial_{xx} \rho = 0 \ .$$

Analogously, taking space derivative of the first and time derivative of the second, a wave equation for the velocity field appears

$$\partial_{tt} u - a^2 \partial_{xx} u = 0 \ .$$

```




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
:class: dropdown

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
:class: dropdown

**Conservative form**

$$\partial_t \begin{bmatrix} \rho \\ \rho u \\ \rho e^t \end{bmatrix} + \partial_x \begin{bmatrix} \rho u \\ \rho u^2 + P \\ \rho u h^t  \end{bmatrix} = \underline{0} \ ,$$

with $h^t = e^t + \frac{P}{\rho}$ and $e^t = e + \frac{u^2}{2}$, and the pressure field can be written as a function of the other thermodynamic variables. As an example, using conservative variables $(\rho, m, E^t) = (\rho, \rho u, \rho e^t) = \left(\rho, \rho u, \rho \left(e + \frac{u^2}{2}\right) \right)$

$$P(\rho, e) = P\left(\rho, \frac{E^t}{\rho} - \frac{m^2}{2 \rho^2}\right) = \Pi\left( \rho, m, E^t \right)$$

so that

$$\begin{aligned}
 \partial_{\rho} \Pi
  & = \partial_\rho P \big|_e + \partial_e P \big|_\rho \left( -\frac{E^t}{\rho^2} + \frac{m^2}{\rho^3} \right) = \\
  & = \partial_\rho P \big|_e + \partial_e P \big|_\rho \left( - \frac{e^t}{\rho} + \frac{u^2}{\rho} \right) \\
  & = c^2 - \frac{P}{\rho^2} \partial_e P \big|_\rho + \partial_e P \big|_\rho \left( - \frac{e^t}{\rho} + \frac{u^2}{\rho} \right) \\
  & = c^2 + \partial_e P \big|_\rho \left( - \frac{h^t}{\rho} + \frac{u^2}{\rho} \right) \\
 \partial_{m   } \Pi & = \partial_e P \big|_\rho \left( - \frac{m}{\rho^2}  \right) \\
 \partial_{E^t } \Pi & = \partial_e P \big|_\rho \left( \frac{1}{\rho} \right) \\
\end{aligned}$$

<!--

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

-->

The speed of sound reads

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
  & \quad + (u^2 - \partial_\rho \Pi) \left( u (1 + \partial_{E^t} \Pi) - s \right) = \\
  & = -s^3 + \\
  & \quad + s^2 \left( 2 u + \partial_m \Pi + u + u \partial_{E^t} \Pi  \right) + \\
  & \quad + s   \left( - 2 u^2 - 2u^2 \partial_{E^t} \Pi - u \partial_m \Pi - u \partial_m \Pi \, \partial_{E^t} \Pi + \partial_{E^t} \Pi \, h^t + u \partial_{E^t} \Pi \, \partial_m \Pi - u^2 + \partial_{\rho} \Pi  \right) + \\
  & \quad +     \left( -u h^t \partial_{E^t} \Pi + u \partial_{\rho} \Pi \, \partial_{E^t} \Pi + u^3 + u^3 \partial_{E^t} \Pi - u \partial_{\rho} \Pi - u \partial_{\rho} \Pi \, \partial_{E^t} \Pi \right) + \\
  & = -s^3 + \\
  & \quad + s^2 \left( 3 u + \partial_m \Pi + u \partial_{E^t} \Pi  \right) + \\
  & \quad + s   \left( - 3 u^2 - 2u^2 \partial_{E^t} \Pi - u \partial_m \Pi + \partial_{E^t} \Pi \, h^t + \partial_{\rho} \Pi  \right) + \\
  & \quad +     \left( u^3 - u h^t \partial_{E^t} \Pi + u^3 \partial_{E^t} \Pi - u \partial_{\rho} \Pi \right) = \\
  & = - (s - u)^3 + ( s - u ) c^2 = \\
  & = ( s - u ) \left[ -(s-u)^2 + c^2 \right]
$$

being

$$\begin{aligned}
  \partial_m \Pi + u \partial_{E^t} \Pi
  & = \left( - \frac{u}{\rho}  + \frac{u}{\rho} \right) \partial_\rho P \big|_e = 0 \\
  - 2u^2 \partial_{E^t} \Pi - u \partial_m \Pi + \partial_{E^t} \Pi \, h^t + \partial_{\rho} \Pi 
  & =  - \frac{u^2}{\rho} \partial_\rho P\big|_e + \frac{1}{\rho} \partial_e P\big|_\rho \, h^t + \partial_\rho P\big|_e + \partial_e P\big|_\rho \left( -\frac{e^t}{\rho} + \frac{u^2}{\rho} \right) = \\
  & = \partial_{e} P \big|_{\rho} \frac{P}{\rho^2} + \partial_{\rho} P \big|_e = \\
  & = c^2 \\
 - u \partial_{\rho} \Pi + u^3 \partial_{E^t} \Pi - u h^t \partial_{E^t} \Pi
  & = u \left( - \partial_\rho P \big|_e - \partial_e P \big|_{\rho} \left( -\frac{e^t}{\rho} + \frac{u^2}{\rho} \right) + \frac{u^2}{\rho} \partial_e P\big|_\rho - \frac{h^t}{\rho} \partial_e P\big|_{\rho}  \right) \\
  & = u \left( -\partial_\rho P\big|_e - \frac{P}{\rho^2} \partial_e P \big|_\rho \right) = \\
  & = - u c^2 \ .
\end{aligned}$$

Thus,

$$s_{1,3} = u \mp c \quad , \quad s_{2} = u $$

$$
\mathbf{r}_{1,3} = \begin{bmatrix} 1 \\ u \mp c \\ \dots \end{bmatrix} \hat{\rho}
 \quad , \quad
\mathbf{r}_2 = \begin{bmatrix} \dots \\ 0 \\ \dots \end{bmatrix} \hat{\rho}
$$

being

$$\begin{aligned}
  \hat{E}^t \partial_{E^t} \Pi
  & = \left[  u^2 - \partial_\rho \Pi + ( -u \pm c -\partial_m \Pi ) (u \mp c) \right] \hat{\rho} = \\
  & = \left[  u^2 - \partial_\rho \Pi - u^2 + \pm 2 u c - c^2  -\partial_m \Pi (u \mp c) \right] \hat{\rho} = \\
  & = \left[ - c^2 - \partial_e P \big|_\rho \left( - \frac{h^t}{\rho} + \frac{u^2}{\rho} \right) \pm 2 u c - c^2  + \frac{u}{\rho} \partial_e P \big|_\rho (u \mp c) \right] \hat{\rho} = \\
  & = \left[ - 2 c^2 + \partial_e P \big|_\rho \, \frac{h^t}{\rho} \pm 2 u c  \mp  \frac{u c}{\rho} \partial_e P\big|_\rho \right] \hat{\rho} = \\
\end{aligned}$$

$$\mathbf{R} = \dots $$
$$\mathbf{L} = \dots $$

```

```{prf:example} Shallow water equation in $1$-dimensional domain

Let $b(x)$..., $h(x)$ the height of the free surface, $\eta(x) = h(x) - b(x)$ the depth.

Derivative of integrals with non-constant extremes

$$\partial_x \int_{z=0}^{\eta(x,t)} \rho u \, dz = \int_{z=0}^{\eta(x,t)} \partial_x (\rho u) \, dz + \rho u(x,\eta(x,t),t) \partial_x \eta(x,t) \ .$$


Continuity equation reads

$$\partial_t \rho + \partial_x (\rho u ) + \partial_z (\rho w) = 0 \ ,$$

for fluids with constant and uniform density

$$\begin{aligned}
  0
  & = \int_{z=0}^{\eta(x,t)} \left( \partial_t \rho + \partial_x (\rho u) + \partial_z (\rho w) \right) \, dz = \\
  & = \partial_x \int_{z=0}^{\eta(x,t)} (\rho u) \, dz - \rho u(x,\eta,t) \partial_x \eta + \rho w(x,\eta(x,t),t) = \\
  & = \partial_x \int_{z=0}^{\eta(x,t)} (\rho u) \, dz + \rho \partial_t \eta = 
  & \simeq \partial_x \left(  \rho \eta u \right) + \partial_t \left( \rho \eta \right) \ .
\end{aligned}$$

having linked the velocity to the material derivative of the position, whose vertical component reads

$$w(x,\eta(x,t), t) = \dfrac{D \eta}{Dt} = \partial_t \eta(x,t) + u(x,\eta(x,t),t) \partial_x \eta \ .$$


Assuming hydrostatic pressure distribution, $p = P_a + \rho g z$ at depth $z$ under the level of local free surface,

Momentum equation reads

$$\begin{aligned}
  0
  & = \partial_t (\rho u) + \partial_x (\rho u^2) + \partial_z (\rho u w) + \partial_x P \ .
\end{aligned}$$

and integration in $z$-direction **todo** Explicitly treat the $z$ term

$$\begin{aligned}
  0
  & = \partial_t (\rho \eta u) + \partial_x (\rho u^2 \eta) + \partial_x \int_{z=0}^{\eta(x)} (P_a + \rho g z) \, dz = \\
  & = \partial_t (\rho \eta u) + \partial_x \left(\rho u^2 \eta + \frac{1}{2} \rho g \eta^2 \right)  \ .
\end{aligned}$$


**Conservative form of the equations.**

$$\begin{cases}
  \partial_t (\eta) + \partial_x m = 0 \\
  \partial_t m + \partial_x \left( \frac{m^2}{\eta} + \frac{g \eta^2}{2} \right) = 0 \\
\end{cases}$$

**Convective form of the equations.**

$$
  \partial_t \begin{bmatrix} \eta \\ m \end{bmatrix} + \begin{bmatrix} 0 & 1 \\ -\frac{m^2}{\eta^2}+g\eta & 2 \frac{m}{\eta} \end{bmatrix} \partial_x \begin{bmatrix} \eta \\ m \end{bmatrix} = \underline{0}
$$

**Spectrum of matrix $\mathbf{A}(\mathbf{u})$.**

$$0 = |\mathbf{A}(\mathbf{u}) - s^2 \mathbf{I}| = -s \left( 2 u - s \right) + u^2 - g \eta = (s-u)^2 - g  \eta \ .$$


```



```{prf:example} P-system in n-dimensional domain

- Conservative variables: $(\rho, \vec{m})$
- Physical variables: e.g. $(\rho, \vec{u})$, $(P, \vec{u})$,...

$$\begin{cases}
  \partial_t \rho + \nabla \cdot \vec{m} = 0 \\
  \partial_t \vec{m} + \nabla \cdot \left[ \frac{\vec{m}\otimes\vec{m}}{\rho} + \rho a^2 \mathbb{I} \right] = 0 \\
\end{cases}$$


```

```{prf:example} Euler system in n-dimensional domain

- Conservative variables: $(\rho, \vec{m}, E^t)$
- Physical variables: e.g. $(\rho, \vec{u}, e)$,...

$$\begin{cases}
  \partial_t \rho + \nabla \cdot \vec{m} = 0 \\
  \partial_t \vec{m} + \nabla \cdot \left[ \frac{\vec{m}\otimes\vec{m}}{\rho} + \Pi \, \mathbb{I} \right] = \vec{0} \\
  \partial_t E^t + \nabla \cdot \left[ \frac{\vec{m} (E^t + \Pi)}{\rho} \right] = 0
\end{cases}$$

where $\Pi$ represents the pressure field as a function of the conservative varaibles,

$$\Pi\left(\rho, \vec{m}, E^t\right) = P\left( \rho, e\right) = P\left( \rho, \frac{E^t}{\rho}-\frac{|\vec{m}|^2}{\rho^3}  \right) \ ,$$

and $P$ the pressure field expressed by the **equation of state of the fluid** as a function of density and internal energy per unit mass as the pair of independent variables determining the thermodynamic state.


```

```{prf:example} Shallow water equations in 2-dimensional domain

$$\begin{cases}
  \partial_t (\rho \eta) + \nabla \cdot (\rho \eta \vec{u}) = 0 \\
  \partial_t (\rho \eta \vec{u}) + \nabla \cdot \left(\rho \eta \vec{u} \vec{u} + \frac{1}{2} \rho g \eta^2 \mathbb{I} \right) = 0 \\
\end{cases}$$


```


