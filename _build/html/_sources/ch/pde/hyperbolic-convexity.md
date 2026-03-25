(pde:hyperbolic:entropy)=
# Convexity in hyperbolic problems

Convexity of the entropy function and the flux are assumption used discussing [physical solutions in hyperbolic problems](pde:hyperbolic:entropy).

Convexity of the entropy flux $\eta''(u) \ge 0$ is a requirement for the entropy inequality

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
:open:

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
