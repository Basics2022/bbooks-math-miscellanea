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

$$
  de = T \, ds + \frac{p}{\rho^2} d \rho \ ,
$$(eq:pde:hyperbolic:euler:first-principle)

from the principles of thermodynamics, and the definition of the entropy $s$ in classical thermodynamics. Following [Gibbs' mathematical foundation of classical thermodynamics](https://basics2022.github.io/bbooks-physics-thermodynamics/ch/principles-gibbs-phase-rule.html), the partial derivatives of the internal energy can be related to temperature, pressure and density

$$
  T = \left( \frac{\partial e}{\partial s} \right)_\rho
  \quad , \quad
  \frac{p}{\rho^2} =  \left( \frac{\partial e}{\partial \rho} \right)_s .
$$(eq:pde:hyperbolic:euler:first-principle:partial-ders)

```

```{dropdown} Speed of sound, $\ a(\rho, s)$.
:open:

As it should be clear from the study of Euler equations as an hyperbolic system  the speed of sound $a$ can be defined as

$$
  a^2(\rho, s) = \left( \frac{\partial p}{\partial \rho} \right)_s \ .
$$(eq:pde:hyperbolic:euler:speed-of-sound:rho-s)

As an example, the definition of the speed of sound appears in two of the eigenvalues of the system, as shown in {eq}`eq:pde:hyperbolic:differential:convective:euler:rho-u-s:eigval` using the convective form {eq}`eq:pde:hyperbolic:differential:convective:euler:rho-u-s:mat` of the equations using $(\rho, \vec{u}, s)$ as primary variables.

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
\end{aligned}$$(eq:pde:hyperbolic:euler:speed-of-sound:rho-e)

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
$$(eq:pde:hyperbolic:cons-vars:euler)

$$
\mathbf{F} = \begin{bmatrix} \vec{m} \\ \frac{\vec{m} \otimes \vec{m}}{\rho} + p \mathbb{I} \\ H^t \frac{\vec{m}}{\rho} \end{bmatrix}
$$(eq:pde:hyperbolic:flux:euler)

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
$$(eq:pde:hyperbolic:jump:euler)

(pde:hyperbolic:nd:euler:differential)=
## Differential equations

In regions where the fields are smooth, from integral to differential equations using [theorems of differential calculus](tensor:calculus:integrals:theorems)

(pde:hyperbolic:nd:euler:differential:conservative)=
### Conservative form

Conservative form of the differential equations immediately follows introducing the expressions {eq}`eq:pde:hyperbolic:cons-vars:euler` of the conservative variables and {eq}`eq:pde:hyperbolic:flux:euler` of the flux in the general expression of the conservative form of hyperbolic problems {eq}`eq:pde:hyperbolic:differential:conservative`

$$
  \partial_t \begin{bmatrix}  \rho \\ \vec{m} \\ E^t \end{bmatrix} + \nabla \cdot \begin{bmatrix} \vec{m} \\ \frac{\vec{m}\otimes\vec{m}}{\rho} + p \mathbb{I} \\ H^t \frac{\vec{m}}{\rho}  \end{bmatrix} = \mathbf{0} \ .
$$(eq:pde:hyperbolic:differential:conservative:euler)

(pde:hyperbolic:nd:euler:differential:convective)=
### Convective forms

```{dropdown} Convective form with conservative variables
:open:

Using Cartesian coordinates for a 2-dimensional domain,

$$\begin{cases}
  \partial_t \rho + \partial_x m_x + \partial_y m_y = 0 \\
  \partial_t m_x + \partial_x \left( \frac{m_x^2}{\rho} + \Pi \right) + \partial_y \left( \frac{m_x m_y}{\rho}     \right) = 0 \\
  \partial_t m_y + \partial_x \left( \frac{m_x m_y}{\rho}     \right) + \partial_y \left( \frac{m_y^2}{\rho} + \Pi \right) = 0 \\
  \partial_t E^t + \partial_x \left( \left( E^t + \Pi \right) \frac{m_x}{\rho} \right) + \partial_y \left( \left( E^t + \Pi \right) \frac{m_y}{\rho} \right) = 0
\end{cases}$$

$$\begin{cases}
  \partial_t \rho + \partial_x m_x + \partial_y m_y = 0 \\
  \partial_t m_x - \frac{m_x^2}{\rho^2} \partial_x \rho + 2 \frac{m_x}{\rho} \partial_x m_x + \partial_x \Pi - \frac{m_x m_y}{\rho^2} \partial_y \rho + \frac{m_y}{\rho} \partial_y m_x + \frac{m_x}{\rho} \partial_y m_y = 0 \\
  \partial_t m_x  - \frac{m_x m_y}{\rho^2} \partial_x \rho + \frac{m_y}{\rho} \partial_x m_x + \frac{m_x}{\rho} \partial_x m_y - \frac{m_y^2}{\rho^2} \partial_y \rho + 2 \frac{m_y}{\rho} \partial_y m_y + \partial_y \Pi= 0 \\
  \partial_t E^t - u h^t \partial_x \rho + h^t \partial_x m_x + u \partial_x E^t + u \partial_x \Pi - v h^t \partial_y \rho + h^t \partial_y m_y + v \partial_y E^t + v \partial_y \Pi = 0
\end{cases}$$

and using the matrix formalism

$$\begin{aligned}
  \partial_t \begin{bmatrix} \rho \\ m_x \\ m_y \\ E^t \end{bmatrix} 
 & + \begin{bmatrix}
  0 & 1  & 0 & 0 \\
  -u^2 + \Pi_{\rho} & 2 u + \Pi_u & \Pi_v & \Pi_{E^t}  \\
  -uv    & v & u & \cdot \\
  (-h^t + \Pi_\rho ) u & h^t + u \Pi_{m_x} & u \Pi_{m_y} & u ( 1 + \Pi_{E^t} ) \\
   \end{bmatrix} \partial_x \begin{bmatrix} \rho \\ m_x \\ m_y \\ E^t \end{bmatrix} + \\
 & + \begin{bmatrix}
  0 & 0 & 1 & 0 \\
  -uv    & v & u & \cdot \\
  -v^2 + \Pi_{\rho} & \Pi_u & 2 v + \Pi_v & \Pi_{E^t} \\
  ( -h^t + \Pi_\rho ) v & v \Pi_{m_x} & h^t + v \Pi_{m_y} & v ( 1 + \Pi_{E^t} ) \\
   \end{bmatrix} \partial_y \begin{bmatrix} \rho \\ m_x \\ m_y \\ E^t \end{bmatrix} = \mathbf{0}
\end{aligned}$$(eq:pde:hyperbolic:differential:convective:euler:cons-vars:mat)

```

```{dropdown} Convective form with primary variables $\ (\rho, \vec{u}, e)$.
:open:

$$\begin{cases}
  \partial_t \rho + \rho \nabla \cdot \vec{u} + \vec{u} \cdot \nabla \rho = 0 \\
  \partial_t \vec{u} + \vec{u} \cdot \nabla \vec{u} + \frac{1}{\rho} \nabla p = \vec{0} \\
  \partial_t e + \vec{u} \cdot \nabla e + \frac{1}{\rho} p \nabla \cdot \vec{u} = 0 \ .
\end{cases}$$(eq:pde:hyperbolic:differential:convective:euler:rho-u-e)

or using Cartesian coordinates and matrix formalism

$$\begin{aligned}
  \partial_t \begin{bmatrix} \rho \\ u \\ v \\ e \end{bmatrix}
 + \begin{bmatrix}
   u                      & \rho            & \cdot & \cdot \\
   \frac{p_\rho|_e}{\rho} & u               & \cdot & \frac{p_e|_\rho}{\rho}  \\
   \cdot                  & \cdot           & u     & \cdot  \\
   \cdot                  & \frac{p}{\rho}  & \cdot & u \\
   \end{bmatrix} \partial_x \begin{bmatrix} \rho \\ u \\ v \\ e \end{bmatrix}
 + \begin{bmatrix}
   v                      & \cdot           & \rho           & \cdot \\
   \cdot                  & v               & \cdot          & \cdot \\
   \frac{p_\rho|_e}{\rho} & \cdot           & v              & \frac{p_e|_\rho}{\rho}  \\
   \cdot                  & \cdot           & \frac{p}{\rho} & v \\
   \end{bmatrix} \partial_y \begin{bmatrix} \rho \\ u \\ v \\ e \end{bmatrix} = \mathbf{0}
\end{aligned}$$(eq:pde:hyperbolic:differential:convective:euler:rho-u-e:mat)


```

```{dropdown} Convective form with primary variables $\ (\rho, \vec{u}, s)$.
:open:

Using the thermodynamic relation $de = T ds + \frac{p}{\rho^2} d \rho$ and combining mass and internal energy equations, the differential equation $D_t s = 0$ follows for the entropy, having introduced the material derivative $D_t \_ = \partial_t \_ + \vec{u} \cdot \nabla \_$. The convective form of the equations becomes

$$\begin{cases}
  \partial_t \rho + \rho \nabla \cdot \vec{u} + \vec{u} \cdot \nabla \rho = 0 \\
  \partial_t \vec{u} + \vec{u} \cdot \nabla \vec{u} + \frac{1}{\rho} \nabla p = \vec{0} \\
  \partial_t s + \vec{u} \cdot \nabla s = 0 \ .
\end{cases}$$(eq:pde:hyperbolic:differential:convective:euler:rho-u-s)

or using Cartesian coordinates and matrix formalism in a 2-dimensional domain

$$\begin{aligned}
  \partial_t \begin{bmatrix} \rho \\ u \\ v \\ s \end{bmatrix}
 + \begin{bmatrix}
   u                      & \rho            & \cdot & \cdot \\
   \frac{p_\rho|_s}{\rho} & u               & \cdot & \frac{p_s|_\rho}{\rho}  \\
   \cdot                  & \cdot           & u     & \cdot  \\
   \cdot                  & \cdot           & \cdot & u \\
   \end{bmatrix} \partial_x \begin{bmatrix} \rho \\ u \\ v \\ s \end{bmatrix}
 + \begin{bmatrix}
   v                      & \cdot           & \rho           & \cdot \\
   \cdot                  & v               & \cdot          & \cdot \\
   \frac{p_\rho|_s}{\rho} & \cdot           & v              & \frac{p_s|_\rho}{\rho}  \\
   \cdot                  & \cdot           & \cdot          & v \\
   \end{bmatrix} \partial_y \begin{bmatrix} \rho \\ u \\ v \\ s \end{bmatrix} = \mathbf{0}
\end{aligned}$$(eq:pde:hyperbolic:differential:convective:euler:rho-u-s:mat)

Using this expression of the equations, it's pretty easy to find the eigenvalues of the system, evaluating the eigenvalues of the matrix

$$
\mathbf{A}^{\mathbf{v}}_{\hat{n}} = n_x \mathbf{A}^\mathbf{v}_x + n_y \mathbf{A}^\mathbf{v}_y =
\begin{bmatrix}
  u_n & \rho \mathbf{n}^T & \cdot \\
  \frac{p_\rho|_s}{\rho} & u_n \mathbf{I}_2 &  \frac{p_s|_\rho}{\rho} \\
  \cdot & \cdot & u_n
\end{bmatrix}
$$

as the zeros of the following equation,

$$0 = | \mathbf{A}_{\hat{n}}^{\mathbf{v}} - s \mathbf{I}_4| = ( u_n - s )^2 \left( ( u_n - s )^2 - \left.\frac{\partial p}{\partial \rho}\right|_s \right) = ( u_n - s )^2 \left( ( u_n - s )^2 - a^2 \right) \ ,$$

having used the definition of the spped of sound {eq}`eq:pde:hyperbolic:euler:speed-of-sound:rho-s`. Thus the **eigenvalues of the system** are

$$\begin{aligned}
  s_{1,4} & = u_n \mp a \\
  s_{2,3} & = u_n \ .
\end{aligned}$$(eq:pde:hyperbolic:differential:convective:euler:rho-u-s:eigval)

```



(pde:hyperbolic:nd:euler:differential:spectrum)=
### Spectral decomposition

It may be convenient to evaluate the spectrum using physical variables $\mathbf{v} = (\rho, \vec{u}, e)$ and then use the rules for the spectral decomposition after a [change of variables](pde:hyperbolic:nd:draft:characteristics:spectrum:change-vars) to get the spectrum in terms of the conservative variables.

**Transformation of variables.** The tranformation between physical variables $\mathbf{v} = (\rho, \vec{u}, e)$ and the conservative variables $\mathbf{u} = ( \rho, \vec{m}, E^t )$ reads

$$\begin{aligned}
\mathbf{v}(\mathbf{u}) = \begin{bmatrix} \rho \\ \vec{u} \\ e \end{bmatrix} = \begin{bmatrix} \rho \\ \frac{\vec{m}}{\rho} \\ \frac{E^t}{\rho} - \frac{|\vec{m}|^2}{2 \rho^2} \end{bmatrix}
\qquad , \qquad
\mathbf{u}(\mathbf{v}) = \begin{bmatrix} \rho \\ \vec{m} \\ E^t \end{bmatrix} = \begin{bmatrix} \rho \\ \rho \vec{u} \\ \rho \left( e + \frac{|\vec{u}|^2}{2} \right) \end{bmatrix} \ .
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

