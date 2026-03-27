(pde:hyperbolic:convexity)=
# Convexity in hyperbolic problems

Convexity of the entropy function and the flux are assumption used discussing [physical solutions in hyperbolic problems](pde:hyperbolic:entropy).

Convexity of the entropy function, $\eta''(u) \ge 0$, and the flux $F$, F''(u)$$, is a requirement for the entropy inequality.

Next section discusses [problems with non-convex fluxes](pde:hyperbolic:non-convex), and the **Olenik-criterion**.

## Examples

```{dropdown} Burgers' equation
:open:

* Flux: $F(u) = \frac{u^2}{2}$
* Entropy: $\eta(u) = \frac{u^2}{2}$
* Entropy flux: $q(u) = \frac{u^3}{3}$

so that the compatibility condition $q'(u) = F'(u) \eta'(u)$ is satisfied.

The flux is convex, $F''(u) = 1 > 0$; the entropy function is convex as well, $\eta''(u) = 1 > 0$.

```


```{dropdown} P-system

$$
\partial_t \begin{bmatrix} \rho \\ m \end{bmatrix}
+ \partial_x \begin{bmatrix} m \\ \frac{m^2}{\rho} + \rho a^2 \end{bmatrix} 
= \partial_x \begin{bmatrix} 0 \\ \mu \partial_x \left( \frac{m}{\rho} \right) \end{bmatrix}
$$

* Flux: $F(\mathbf{u}) = \begin{bmatrix} m \\ \frac{m^2}{\rho} + \rho a^2 \end{bmatrix} $
* Entropy: $\eta(\mathbf{u}) = \frac{m^2}{2 \rho} + a^2 \rho \ln \frac{\rho}{\rho_0}$
* Diffusion flux: $\begin{bmatrix} 0 & 0 \\ - \mu \frac{m}{\rho^2} & \mu \frac{1}{\rho} \end{bmatrix} \partial_x \begin{bmatrix} \rho \\ m \end{bmatrix}$

**Flux.** First component

$$\nabla_{\mathbf{u}} F_1 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

$$\nabla_{\mathbf{u} \mathbf{u}} F_1 = \mathbf{0}_2 \ .$$

Second component

$$\nabla_{\mathbf{u}} F_2 = \begin{bmatrix} a^2 - \frac{m^2}{\rho^2} \\ 2 \frac{m}{\rho} \end{bmatrix}$$

$$\nabla_{\mathbf{u} \mathbf{u}} F_2 = \begin{bmatrix} 2 \frac{m^2}{\rho^3} & - \frac{2 m}{\rho^2} \\ - \frac{2 m}{\rho^2} & \frac{2}{\rho} \end{bmatrix} \ .$$

**Entropy.** Gradient 

$$\nabla_{\mathbf{u}} \eta = \begin{bmatrix} - \frac{m^2}{2 \rho^2} + a^2\left( 1 + \ln \frac{\rho}{\rho_0} \right) \\ \frac{m}{\rho} \end{bmatrix}$$

and Hessian

$$\nabla_{\mathbf{u} \mathbf{u}} \eta = \begin{bmatrix}  \frac{m^2}{\rho^3} + \frac{a^2}{\rho} & - \frac{m}{\rho^2} \\ - \frac{m}{\rho^2} & \frac{1}{\rho} \end{bmatrix}$$

**Compatibility of diffusion and entropy.**

$$
\nabla_{\mathbf{u} \mathbf{u}} \eta \cdot \mathbf{D} = 
\mu \begin{bmatrix} \frac{m^2}{\rho^4} & -\frac{m}{\rho^3} \\ - \frac{m}{\rho^3} & \frac{1}{\rho^2} \end{bmatrix}
$$

This matrix is semi-definite positive with one zero eigenvalue (associated with exact conservation and no dissipation in mass equation), and the other eigenvalue

```

```{dropdown} Euler equations for compressible flows
:open:

Navier-Stokes equations

$$\begin{aligned}
  & \partial_t \rho + \nabla \cdot ( \rho \mathbf{u} ) = 0 \\
  & \rho D_t \mathbf{u} = \nabla \cdot \mathbb{T} \\
  & \rho D_t e^t = \nabla \cdot ( \mathbb{T} \cdot \mathbf{u} ) - \nabla \cdot \mathbf{q} \ ,
\end{aligned}$$

with $\mathbb{T} = -p \mathbb{I} + 2  \mu \mathbb{D} + \lambda ( \nabla \cdot \mathbf{u} ) \mathbb{I}$ the constitutive equation for Newtonian fluids, and $\mathbf{q} = - k \nabla T$ if Fourier law holds.

The conservative form of the equations in 1-dimensional domain reads

$$
\partial_t \begin{bmatrix} \rho \\ m \\ E^t \end{bmatrix} + 
\partial_x \begin{bmatrix} m \\ \frac{m^2}{\rho} + p \\ \frac{m}{\rho} \left( E^t + p \right) \end{bmatrix} = 
\partial_x \begin{bmatrix} 0 \\ ( \mu + \lambda ) \partial_x \left( \frac{m}{\rho} \right) \\ ( \mu + \lambda ) \frac{m}{\rho} \partial_x \left( \frac{m}{\rho} \right) - q \end{bmatrix}
$$

The convective form using $(\rho, u, e)$ as primary variables reads

$$
\dots
$$

Entropy function is chosen as the thermodynamic entropy volume density $\eta = \rho s$. Entropy equation naturally follows from the thermodynamic relation $ds = \frac{1}{T} \left( de - \frac{p}{\rho^2} d \rho \right)$,

$$\rho \partial_t s + \rho \mathbf{u} \cdot \nabla s = \frac{2 \mu |\mathbb{D}|^2 + \lambda (\nabla \cdot \mathbf{u})^2}{T} + \frac{k |\nabla T|^2}{T^2} - \nabla \cdot \left(\frac{\mathbf{q}}{T}\right)$$

or in conservative form (using mass equation)

$$\partial_t \left( \rho s \right) + \nabla \cdot \left( \rho s \mathbf{u} \right) = \frac{2 \mu |\mathbb{D}|^2 + \lambda (\nabla \cdot \mathbf{u})^2}{T} + \frac{k |\nabla T|^2}{T^2} - \nabla \cdot \left(\frac{\mathbf{q}}{T}\right)$$

* Flux: $F(\mathbf{u}) = \begin{bmatrix} m \\ \frac{m^2}{\rho} + p \\ \frac{m}{\rho}(E^t+p) \end{bmatrix} $
* Entropy: $\eta(\mathbf{u}) = \rho s \left( \rho, \mathbf{m}, E^t \right)$
* Diffusion flux: $\begin{bmatrix} 0 & 0 & 0 \\ - (\mu+\lambda) \frac{m}{\rho^2} & (\mu+\lambda) \frac{1}{\rho} & 0 \\ \dots & \dots & \dots \end{bmatrix} \partial_x \begin{bmatrix} \rho \\ m \\ E^t \end{bmatrix}$

**Flux.** First component

$$\nabla_{\mathbf{u}} F_1 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$$

$$\nabla_{\mathbf{u} \mathbf{u}} F_1 = \mathbf{0}_3 \ .$$

Second component

$$\nabla_{\mathbf{u}} F_2 = \begin{bmatrix} - \frac{m^2}{\rho^2} + \Pi_{/\rho} \\ 2 \frac{m}{\rho} + \Pi_{/m} \\ \Pi_{E^t} \end{bmatrix}$$

$$\nabla_{\mathbf{u} \mathbf{u}} F_2 = \begin{bmatrix} \dots \\ \dots \\ \dots \end{bmatrix} \ .$$

Third component

$$\nabla_{\mathbf{u}} F_2 = \begin{bmatrix} \dots \\ \dots \\ \dots \end{bmatrix}$$

$$\nabla_{\mathbf{u} \mathbf{u}} F_2 = \begin{bmatrix} \dots \\ \dots \\ \dots \end{bmatrix} \ .$$

**Entropy.** Gradient 

$$\nabla_{\mathbf{u}} \eta = \begin{bmatrix} s + \rho s_{/\rho} \\ \rho s_{/m} \\ \rho s_{/E^t} \end{bmatrix}$$

and Hessian

$$\nabla_{\mathbf{u} \mathbf{u}} \eta = 
\begin{bmatrix}
2 s_{/\rho} + \rho s_{/\rho \rho} & s_{/m} + \rho s_{\rho m} &  s_{/E^t} + \rho s_{\rho E^t} \\
                           \dots  &          \rho s_{m    m} &             \rho s_{m    E^t} \\
                           \dots  &          \dots           &             \rho s_{E^t  E^t} \\
\end{bmatrix}
$$

**Compatibility of diffusion and entropy.**

$$
\nabla_{\mathbf{u} \mathbf{u}} \eta \cdot \mathbf{D} = 
\mu \begin{bmatrix} \frac{m^2}{\rho^4} & -\frac{m}{\rho^3} \\ - \frac{m}{\rho^3} & \frac{1}{\rho^2} \end{bmatrix}
$$

This matrix is semi-definite positive with one zero eigenvalue (associated with exact conservation and no dissipation in mass equation), and the other eigenvalue

```
