(pde:hyperbolic:nd:euler)=
# Euler equations

(pde:hyperbolic:nd:euler:thermodynamics)=
## Thermodynamics and constitutive equations

**todo** *Reference to [Physics: Thermodynamics](https://basics2022.github.io/bbooks-physics-thermodynamics/intro.html) bbook*

````{dropdown} Thermodynamics
:open:

```{dropdown} Principles of thermodynamics and differential of the internal energy
:open:

The differential of the internal energy as a function of $s, \rho$ as independent thermodynamic variables, $e(\rho, s)$ reads

$$de = T \, ds + \frac{p}{\rho^2} d \rho \ ,$$

from the principles of thermodynamics, and the definition of the entropy $s$ in classical thermodynamics. Following Gibbs' mathematical foundation of classical thermodynamics, it immediately follows 

$$
T = \left( \frac{\partial e}{\partial s} \right)_\rho
\quad , \quad
\frac{p}{\rho^2} =  \left( \frac{\partial e}{\partial \rho} \right)_s .
$$

```

```{dropdown} Speed of sound, $\ a(\rho, s)$.
:open:

As it should be clear from the study of hyperbolic systems, the speed of sound $a$ can be defined as

$$a^2(\rho, s) = \left( \frac{\partial p}{\partial \rho} \right)_s \ .$$

```

```{dropdown} Speed of sound, and change of independent thermodynamic variables
:open:

All the relations in this box mainly exploit **rule of derivatives of composite functions** and basic thermodynamic relations.

As an example, if the pressure is defined as a function of $(\rho, e)$, and the relation $e(\rho,s)$ is known, with pressure can be written as $p(\rho, e) = p(\rho, e(\rho,s))$. With the derivation of the composite function, an alternative expression of the speed of sound follows

$$\begin{aligned}
  a^2
  & = \left( \frac{\partial p}{\partial \rho} \right)_s = \\
  & = \left( \frac{\partial p}{\partial \rho} \right)_e + \left( \frac{\partial e}{\partial \rho} \right)_s \left( \frac{\partial p}{\partial e} \right)_\rho = \\
  & = \left( \frac{\partial p}{\partial \rho} \right)_e + \frac{p}{\rho^2} \left( \frac{\partial p}{\partial e} \right)_\rho \ .
\end{aligned}$$

Conservative variables of Euler equations are $(\rho, \vec{m}, E^t) = \left( \rho, \rho \vec{u}, \rho \left( e + \frac{|\vec{u}^2}{2} \right) \right)$. Pressure as a function of conservative variable reads

$$p = \Pi \left( \rho, \vec{m}, E^t \right) = \Pi \left( \rho, \rho \vec{u}, \rho e(\rho,s) + \rho \frac{|\vec{u}|^2}{2} \right)$$



```

````

```{dropdown} Constitutive equations for an ideal Newtonian fluid
:open:

* Stress tensor $\mathbb{T} = - p \mathbb{I}$
* Stress vector $\vec{t}_{\hat{n}} = \hat{n} \cdot \mathbb{T} = - p \hat{n}$
* Heat conduction flux $\vec{q} = \vec{0}$

```

(pde:hyperbolic:nd:euler:integral)=
## Integral equations

Conservative variables and flux are respectively

$$
\mathbf{u} = \begin{bmatrix} \rho \\ \vec{m} \\ E^t \end{bmatrix} 
\quad , \quad
\mathbf{F} = \begin{bmatrix} \vec{m} \\ \frac{\vec{m} \otimes \vec{m}}{\rho} + p \mathbb{I} \\ H^t \frac{\vec{m}}{\rho} \end{bmatrix}
$$

```{dropdown} Integral equations for a control volume $\ V \ $ at rest

Integral equation for a control volume at rest $V$ immediately follows from the three principles of classial mechanics: conservation of mass, 2-nd principle of Newtonian dynamics, 1-st principle of thermodynamics

$$\begin{aligned}
  \frac{d}{dt} \int_{V} \rho         + \oint_{\partial V} \rho         \vec{u} \cdot \hat{n} & = 0 \\
  \frac{d}{dt} \int_{V} \rho \vec{u} + \oint_{\partial V} \rho \vec{u} \vec{u} \cdot \hat{n} & = - \oint_{\partial V} p \hat{n} \\
  \frac{d}{dt} \int_{V} \rho e^t     + \oint_{\partial V} \rho e^t     \vec{u} \cdot \hat{n} & = - \oint_{\partial V} p \vec{u} \cdot \hat{n} \\
\end{aligned}$$

with the need for an equation of state with the expression of pressure $p$ as a function of the dynamical variables $p = \Pi(\rho, \vec{u}, e^t)$. Using conservative variables $(\rho, \vec{m}, E^t) = (\rho, \rho \vec{u}, \rho e^t)$

$$\begin{aligned}
  \frac{d}{dt} \int_{V} \rho    + \oint_{\partial V} \vec{m} \cdot \hat{n} & = 0 \\
  \frac{d}{dt} \int_{V} \vec{m} + \oint_{\partial V} \left( \frac{\vec{m} \otimes \vec{m}}{\rho} + p \mathbb{I} \right) \cdot \hat{n} & = 0 \\
  \frac{d}{dt} \int_{V} E^t     + \oint_{\partial V} H^t \frac{\vec{m}}{\rho} \cdot \hat{n} & = 0 \ .
\end{aligned}$$

having defined the total enthalpy per unit volume 

$$H^t = \rho h^t = \rho \left( e^t + \frac{p}{\rho} \right) = \rho \left( e + \frac{p}{\rho} + \frac{|\vec{u}|^2}{2} \right) = \rho \left( h + \frac{|\vec{v}|^2}{2} \right) \ .$$

```

```{dropdown} Integral equations for an arbitrary domain $\ v_t \ $

Integral equation for an arbitrary domain $v_t$, with [Reynolds' transport theorem](tensor:calculus:time-derivative-of-integrals:volume-density)

$$\begin{aligned}
  \frac{d}{dt} \int_{v_t} \rho         + \oint_{\partial v_t} \rho         ( \vec{u} - \vec{v}_b ) \cdot \hat{n} & = \\
  \frac{d}{dt} \int_{v_t} \rho \vec{u} + \oint_{\partial v_t} \rho \vec{u} ( \vec{u} - \vec{v}_b ) \cdot \hat{n} & = \\
  \frac{d}{dt} \int_{v_t} \rho e^t     + \oint_{\partial v_t} \rho e^t     ( \vec{u} - \vec{v}_b ) \cdot \hat{n} & = \\
\end{aligned}$$

```

(pde:hyperbolic:nd:euler:integral:jump)=
### Jump conditions

Jump conditions {eq}`eq:pde:hyperbolic:jump` for Euler equations read

$$
  \vec{v}_b \cdot \hat{n} \left[ \left( \begin{matrix} \rho \\ \vec{m} \\ E^t \end{matrix} \right) \right] = \hat{n} \cdot \left[ \left( \begin{matrix} \vec{m} \\\frac{\vec{m} \vec{m}}{\rho} + p \\ H^t \end{matrix} \right) \right]
$$(eq:pde:hyperbolic:jump:eule)

(pde:hyperbolic:nd:euler:differential)=
## Differential equations

In regions where the fields are smooth, from integral to differential equations using [theorems of differential calculus](tensor:calculus:integrals:theorems)

(pde:hyperbolic:nd:euler:differential:conservative)=
### Conservative form

(pde:hyperbolic:nd:euler:differential:convective)=
### Convective forms

(pde:hyperbolic:nd:euler:differential:spectrum)=
### Spectral decomposition

It may be convenient to evaluate the spectrum using physical variables $\mathbf{v} = (\rho, \vec{u}, e)$ and then use the rules for the spectral decomposition after a [change of variables](pde:hyperbolic:nd:draft:characteristics:spectrum:change-vars) to get the spectrum in terms of the conservative variables.

**Transformation of variables.** The tranformation between physical variables $\mathbf{v} = (\rho, \vec{u}, e)$ and the conservative variables $\mathbf{u} = ( \rho, \vec{m}, E^t )$ reads

$$\begin{aligned}
\mathbf{v}(\mathbf{u}) & = \begin{bmatrix} \rho \\ \vec{u} \\ e \end{bmatrix} = \begin{bmatrix} \rho \\ \frac{\vec{m}}{\rho} \\ \frac{E^t}{\rho} - \frac{|\vec{m}|^2}{2 \rho^2} \end{bmatrix}
\qquad , \qquad
\mathbf{u}(\mathbf{v}) & = \begin{bmatrix} \rho \\ \vec{m} \\ E^t \end{bmatrix} = \begin{bmatrix} \rho \\ \rho \vec{u} \\ \rho \left( e + \frac{|\vec{u}|^2}{2} \right) \end{bmatrix} \ .
\end{aligned}$$

**Gradients of the transformations.**

$$
\mathbf{U}_{\mathbf{v}} = 
\begin{bmatrix}
  1 & \cdot & \cdot & \cdot \\
  u & \rho  & \cdot & \cdot \\
  v & \cdot & \rho  & \cdot \\
  e + \frac{|\mathbf{u}|^2}{2} & \rho u & \rho v & \rho \\
\end{bmatrix}
= 
\begin{bmatrix}
 1 & \cdot & \cdot \\ 
 \mathbf{u} & \mathbf{I}_2 & \cdot \\
 e^t & \rho \mathbf{u}^T & \rho
\end{bmatrix}
$$

$$
\mathbf{V}_{\mathbf{u}} = 
\mathbf{U}_{\mathbf{v}}^{-1} = 
\begin{bmatrix}
  1 & \cdot & \cdot & \cdot \\
  -\frac{u}{\rho} & \frac{1}{\rho}  & \cdot & \cdot \\
  -\frac{v}{\rho} & \cdot & \frac{1}{\rho}  & \cdot \\
  \frac{1}{\rho} \left( \frac{|\mathbf{u}|^2}{2} - e \right) & -\frac{ u}{\rho} & -\frac{ v}{\rho} & \frac{1}{\rho} \\
\end{bmatrix} 
=
\begin{bmatrix}
  1 & \cdot & \cdot \\
  - \frac{\mathbf{u}}{\rho} & \frac{1}{\rho} \mathbf{I}_2 & \cdot \\
  \frac{1}{\rho} \left( |\mathbf{u}|^2 - e^t \right) & - \frac{\mathbf{u}^T}{\rho} & \frac{1}{\rho}
\end{bmatrix} 
$$

**Spectral decomposition of $\mathbf{A}_{\hat{n}}^{\mathbf{v}}$, using $\mathbf{v}=(\rho, \vec{u}, e)$.** The normal convective matrix using physical variables $\mathbf{v}$ reads

$$\mathbf{A}_{\hat{n}}^{\mathbf{v}} = \begin{bmatrix} u_n & \rho \mathbf{n}^T & \cdot \\ \frac{1}{\rho}\partial_\rho p|_e \mathbf{n} & u_n \mathbf{I} & \frac{1}{\rho}\partial_e p|_{\rho} \mathbf{n} \\ \cdot & \frac{p}{\rho} \mathbf{n}^T & u_n \end{bmatrix} \ ,$$

```{dropdown} Eigenvalues
:open:

In a 2-dimensional domain, the system of equations is 4-dimensional, and its eigenvalues are

$$\left\{ u_n - a, u_n, u_n, u_n + a \right\} \ .$$

In a 3-dimensional domain, the system of equations is 5-dimensional, and its eigenvalues are

$$\left\{ u_n - a, u_n, u_n, u_n, u_n + a \right\} \ .$$

```

```{dropdown} Right eigenvectors
:open:

In a 2-dimensional domain

$$
\mathbf{R}^\mathbf{v} =
\begin{bmatrix}
  \rho            & \rho                                                   & 0     & \rho  \\
 -a n_x           & 0                                                      & a n_y & a n_x \\
 -a n_y           & 0                                                      &-a n_x & a n_y \\
  \frac{p}{\rho}  & -\rho \frac{\partial_\rho p|_e}{\partial_e p|_{\rho}}  & 0     & \frac{p}{\rho}
\end{bmatrix}
=
\begin{bmatrix}
  \rho            & \rho                                                   & 0               & \rho  \\
 -a \mathbf{n}    & \mathbf{0}                                             & a \mathbf{t}    & a \mathbf{n} \\
  \frac{p}{\rho}  & -\rho \frac{\partial_\rho p|_e}{\partial_e p|_{\rho}}  & 0               & \frac{p}{\rho}
\end{bmatrix}
$$

```

```{dropdown} Left eigenvectors
:open:

In a 2-dimensional domain

$$
\mathbf{L}^\mathbf{v} =
\begin{bmatrix}
 \frac{P_\rho}{2 \rho a^2} & - \frac{1}{2a} \mathbf{n}^T & \frac{P_e}{2 \rho a^2} \\
 \frac{P}{\rho^2} \frac{P_e}{\rho a^2} & \mathbf{0}^T & - \frac{P_e}{\rho a^2} \\
 0 & \frac{\mathbf{t}^T}{a} & 0 \\
 \frac{P_\rho}{2 \rho a^2} & + \frac{1}{2a} \mathbf{n}^T & \frac{P_e}{2 \rho a^2} \\
\end{bmatrix}
$$

```

**Spectral decomposition of $\mathbf{A}_{\hat{n}}^{\mathbf{u}}$, using $\mathbf{u}=(\rho, \vec{m}, E^t)$.** 

```{dropdown} Right eigenvectors
:open:

In a 2-dimensional domain

$$
\mathbf{R}^\mathbf{u} =
\begin{bmatrix}
  \rho                           & \rho                                                         & 0                 & \rho                      \\
  \vec{m} - \rho a \hat{n}       & \vec{m}                                                      & \rho a \hat{t}    & \vec{m} + \rho a \hat{n}  \\
  H^t - m_n a                    & \frac{|\vec{m}|^2}{\rho} - \rho \frac{\Pi_{\rho}}{\Pi_{E^t}} & a m_t             & H^t + m_n a                  
\end{bmatrix}
$$

```

```{dropdown} Left eigenvectors
:open:

In a 2-dimensional domain

$$
\mathbf{L}^\mathbf{u} =
\frac{1}{2 \rho a^2}
\begin{bmatrix}
  \Pi_\rho + a u_n & - a n_x + \Pi_{m_x}  & - a n_y + \Pi_{m_y} & \Pi_{E^t} \\
   2 a^2 - 2 \Pi_{\rho} & - 2 \Pi_{m_x} & 2 - \Pi_{m_y} & - 2 \Pi_{E^t} \\
  - 2 a u_t & 2 a t_x & 2 a t_y & 0 \\
  \Pi_\rho - a u_n &   a n_x + \Pi_{m_x}  &   a n_y + \Pi_{m_y} & \Pi_{E^t} \\
\end{bmatrix}
$$

```


```{dropdown} Some algebra

Right eigenvectors w.r.t. conservative variables are

$$\begin{aligned}
\mathbf{R}^\mathbf{u} = \mathbf{U}_{\mathbf{v}} \mathbf{R}^{\mathbf{v}} 
& =
\begin{bmatrix}
  \rho & \rho & 0 & \rho \\
  \rho u - \rho a n_x & \rho u & \rho a n_y & \rho u + \rho a n_x \\
  \rho u - \rho a n_y & \rho v &-\rho a n_x & \rho u + \rho a n_y \\
  \rho e^t - \rho u_n a + p & \rho e^t - \rho^2 \frac{P_\rho}{P_e} & \rho a u_t & \rho e^t + \rho u_n a + p 
\end{bmatrix} = \\
& =
\begin{bmatrix}
  \rho & \rho & 0 & \rho \\
  \rho u - \rho a n_x & \rho u & \rho a n_y & \rho u + \rho a n_x \\
  \rho u - \rho a n_y & \rho v &-\rho a n_x & \rho u + \rho a n_y \\
  \rho h^t - \rho u_n a & \rho e^t - \rho^2 \frac{P_\rho}{P_e} & \rho a u_t & \rho h^t + \rho u_n a
\end{bmatrix} \ ,
\end{aligned}$$

with $h^t = e^t + \frac{|\mathbf{u}|^2}{2}$, and 

$$\rho e^t - \rho^2 \frac{P_\rho}{P_e} = \rho e^t + P - P - \rho^2 \frac{P_\rho}{P_e} = \rho h^t - \frac{\rho^2}{P_e} \left( \frac{P}{\rho^2} P_e + P_\rho \right) = \rho h^t - \frac{\rho^2}{P_e} a^2 \ .$$ 

Or using the derivatives of $\Pi(\rho, \mathbf{m}, E^t)$,

$$\begin{aligned}
  E^t - \rho^2 \frac{P_\rho}{P_e} 
  & = E^t - \rho^2 \frac{\partial_\rho \Pi - \partial_{E^t} \Pi (-e^t + |\mathbf{u}|^2)}{\rho \partial_{E^t} \Pi } = \\
  & = E^t - \rho \frac{\partial_\rho \Pi}{\partial_{E^t} \Pi} - E^t + \rho |\mathbf{u}|^2 = \\
  & = \rho |\mathbf{u}|^2 - \rho \frac{\partial_\rho \Pi}{\partial_{E^t} \Pi} \ .
\end{aligned}$$

Left eigenvectors w.r.t. conservative variables are

$$\begin{aligned}
\mathbf{L}^\mathbf{u} = \mathbf{L}^{\mathbf{v}} \mathbf{V}_{\mathbf{u}} 
& = 
\begin{bmatrix}
  \frac{P_\rho}{2 \rho a^2} + \frac{u_n}{2 \rho a} + \frac{1}{2 \rho a^2} \frac{P_e}{\rho} (|\mathbf{u}|^2 - e^t) & 
  - \frac{1}{2 \rho a} n_x - \frac{u}{2 \rho a^2}\frac{P_e}{\rho} &
  - \frac{1}{2 \rho a} n_y - \frac{v}{2 \rho a^2}\frac{P_e}{\rho} &
  \frac{P_e}{2 \rho^2 a^2} \\
  \frac{P}{\rho^2}\frac{P_e}{\rho a^2} - \frac{P_e}{\rho a^2} \frac{|\mathbf{u}|^2 - e^t}{\rho} &
    \frac{P_e}{\rho a^2} \frac{u}{\rho} &
    \frac{P_e}{\rho a^2} \frac{v}{\rho} &
  - \frac{P_e}{\rho^2 a^2} \\
  - \frac{u_t}{\rho a} & \frac{t_x}{\rho a} & \frac{t_y}{\rho a} & 0 \\
  \frac{P_\rho}{2 \rho a^2} - \frac{u_n}{2 \rho a} + \frac{1}{2 \rho a^2} \frac{P_e}{\rho} (|\mathbf{u}|^2 - e^t) & 
    \frac{1}{2 \rho a} n_x - \frac{u}{2 \rho a^2}\frac{P_e}{\rho} &
    \frac{1}{2 \rho a} n_y - \frac{v}{2 \rho a^2}\frac{P_e}{\rho} &
  \frac{P_e}{2 \rho^2 a^2} \\
\end{bmatrix} = \\
& =
\frac{1}{2 \rho a^2}
\begin{bmatrix}
  \Pi_\rho + a u_n & - a n_x + \Pi_{m_x}  & - a n_y + \Pi_{m_y} & \Pi_{E^t} \\
   2 a^2 - 2 \Pi_{\rho} & - 2 \Pi_{m_x} & 2 - \Pi_{m_y} & - 2 \Pi_{E^t} \\
  - 2 a u_t & 2 a t_x & 2 a t_y & 0 \\
  \Pi_\rho - a u_n &   a n_x + \Pi_{m_x}  &   a n_y + \Pi_{m_y} & \Pi_{E^t} \\
\end{bmatrix}
\end{aligned}$$

being

$$\begin{aligned}
  \Pi_\rho & = P_\rho + \frac{ P_e }{\rho} \left( - e^t + |\mathbf{u}|^2 \right) \\
  \Pi_{\mathbf{m}} & = -\frac{\mathbf{u}}{\rho} P_e \\
  \Pi_{E^t} & = \frac{1}{\rho} P_e
\end{aligned}$$

$$\begin{aligned}
2 \frac{P}{\rho^2} P_e - 2 P_e \frac{|\mathbf{u}|^2 - e^t}{\rho}
& = 2 \frac{P}{\rho^2} P_e + 2 P_\rho - 2 \Pi_\rho = \\
& = 2 a^2 - 2 \Pi_\rho
\end{aligned}$$

and the speed of sound

$$a^2(\rho,s) = \partial_\rho P|_s$$

with $P(\rho, e(\rho,s))$

$$\begin{aligned}
  a^2 
  & = \partial_\rho P|_e + \partial_\rho e|_s \, \partial_e P|_\rho  = \\
  & = \partial_\rho P|_e + \frac{P}{\rho^2}\partial_e \, P|_\rho  \ .
\end{aligned}$$


```

* Eigenvalues, right and left eigenvectors
* Characteristic lines/surfaces, and compatibility conditions

(pde:hyperbolic:nd:euler:riemann)=
## Riemann problem

* Useful in numerical schemes in finite volume methods, using Godunov flux

(pde:hyperbolic:nd:euler:riemann:roe)=
### Linearization - Roe intermediate state

* Local linearization of the problem, to reduce the computational cost of solving non-linear Riemann problems at all the interfaces in a grid in FVM

(pde:hyperbolic:nd:euler:bc)=
## Boundary conditions

* characteristic-based
* wall
* ...

