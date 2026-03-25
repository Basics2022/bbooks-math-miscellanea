(pde:hyperbolic:entropy)=
# Physical solution in hyperbolic problems

```{dropdown} Topics
:open:

This section deals with:
- existence of infinite number of solution of hyperbolic problems, and existence of one physical solution of the problem as the inviscid limit of the solution of the diffusive problem
- definition of an entropy function, $\eta(u)$, and its flux, $q(\eta)$
- properties of the entropy functions, and fluxes: **convex**, and non-convex fluxes
- discussion of the general case, and examples (Euler equations, P-sys, shallow water)

```

(pde:hyperbolic:entropy:1d-scalar)=
## Scalar non-linear equation in 1-dimensional domain

The hyperbolic equation for $u(x,t)$, $\partial_t u + \partial_x F(u) = 0$, is often the inviscid limit of the 2-nd order equation

$$\partial_t u + \partial_x F(u) - \partial_x \left( \varepsilon \partial_x u \right) = 0 \ .$$

Term $\varepsilon \partial_x u$ represents a diffusive flux, and the inviscid limit is defined by the condition $\varepsilon \rightarrow 0$.

**Definition of an entropy function $\eta(u)$, and its flux $q(u)$**. Let $\eta(u)$ be a function of the field $u$. Evaluating its time derivative using the viscous equation, 

$$\begin{aligned}
  \partial_t \eta(u) 
  & = \eta'(u) \partial_t u = \\
  & = \eta'(u) \left[ - \partial_x F(u) - \partial_x ( \varepsilon \partial_x u ) \right] = \\
  & = - \eta'(u) F'(u) \partial_x u - \eta'(u) ( \varepsilon u_{/x} )_{/x} \ .
\end{aligned}$$

If a function $q(u)$ satisfies the condition 

$$q'(u) = \eta'(u) F'(u) \ ,$$

function $\eta(u)$ can be defined as an **entropy function** and $q(u)$ as the corresponding **entropy flux**.

**Differential inequality.** Let these functions exist. Then

$$\partial_t \eta + \partial_x q = - \eta' \left( \varepsilon u_{/x} \right)_{/x} \ ,$$

is a differential balance equation for the entropy. The last term can be manipulated to find

$$\begin{aligned}
  0 
  & = \partial_t \eta + \partial_x q - \eta' \left( \varepsilon u_{/x} \right)_{/x} = \\
  & = \partial_t \eta + \partial_x q - \left( \varepsilon \eta'(u) u_{/x} \right)_{/x} + \eta''(u) \varepsilon \left( u_{/x} \right)^2 \ ,
\end{aligned}$$

For $\varepsilon \ge 0$, for **convex entropy function** $\eta''(u)$, a differential inequality follows

$$
   \partial_t \eta + \partial_x q + \left( \varepsilon \eta'(u) u_{/x} \right)_{/x} \le 0 \ .
$$

**Integral inequality and jump conditions.** Differential inequality is the local counterpart of the integral equation for a volume $V$ at rest

$$\frac{d}{dt} \int_{V} \eta + \oint_{\partial V} n_x \, q + \oint_{\partial V} \varepsilon q'(u) u_{/x} n_x \le 0 \ ,$$

or for a generic volume $v_t$, 

$$\frac{d}{dt} \int_{v_t} \eta - \oint_{\partial v_t} n_x v_b \eta + \oint_{\partial v_t} n_x \, q + \oint_{\partial v_t} \varepsilon q'(u) u_{/x} n_x \le 0 \ ,$$

being $v_b$ the velocity of the points of the boundary of the domain $\partial v_t$. Jump condition in the inviscid limit $\varepsilon \rightarrow 0$ follows from the collapse of the volume on a surface ($\frac{|v_t|}{|\partial v_t|} \rightarrow 0$), and from the arbitrariness of this surface

$$v_b [ \eta ] \ge [ q ] \ .$$

**Weak shocks.** Expanding in Taylor series jump condition for weak shocks provides an alternative version of the entropy condition, as a relation between the eigenvalues of the system and the shock speed. The shock speed reads $\dot{s} = \frac{[f]}{[u]} = \frac{f_R-f_L}{u_R - u_L}$. Taylor expansion of jump condition relies on Taylor expansion of the jumps there in and of the speed of the shock

$$\begin{aligned}
  f_R - f_L & = f'(L) \Delta u + f''(L) \frac{\Delta u^2}{2} + f'''(L) \frac{\Delta u^3}{6} + o(\Delta u^3) \\
  \dot{s}   & = f'(L) + f''(L) \frac{\Delta u}{2} + f'''(L) \frac{\Delta u^2}{6} + o(\Delta u^2) \\
  \eta_R - \eta_L  & = \eta'(L) \Delta u + \eta''(L) \frac{\Delta u^2}{2} + \eta'''(L) \frac{\Delta u^3}{6} + o(\Delta u^3) \\
     q_R -    q_L  & =    q'(L) \Delta u +    q''(L) \frac{\Delta u^2}{2} +    q'''(L) \frac{\Delta u^3}{6} + o(\Delta u^3) \\
\end{aligned}$$

and comparing terms of the same order

$$\begin{aligned}
  0 \le \Delta u ( \eta'_L f'_L - q'_L ) + \Delta u^2 \left( \frac{1}{2} f'_L \eta''_L + \frac{1}{2} f''_L \eta'_L - \frac{1}{2} q''_L \right) + \Delta u^3 \left( \frac{1}{6} \eta'''_L f'_L + \frac{1}{4} \eta''_L f''_L + \frac{1}{6} \eta'_L f'''_L - \frac{1}{6} q'''_L \right) + o(\Delta u^3) \ .
\end{aligned}$$

Exploiting the relation $q' = \eta' f'$, and evaluating higher-order derivatives

$$\begin{aligned}
  q'' & = \eta'' f' + \eta' f'' \\
  q'''& = \eta''' f' + 2 \eta'' f'' + \eta' f''' \\
\end{aligned}$$

it follows that the first two terms of the jump condition inequality are identically zero, so that it can be written as

$$0 \le -\frac{1}{12} \Delta u^3 \eta''_L f''_L \ .$$

For a system with **convex entropy function** $\eta''(u) \ge 0$, and **convex flux** $f''(u) \ge 0$, it follows that $\Delta u \le 0$, i.e. $u_R < u_L$. Using the Taylor expansion (either centered in the left or right state) of the speed of the shock,

$$\begin{aligned}
  \dot{s} & = f'_L + f''_L \frac{\Delta u}{2} \le f'_L \\
  \dot{s} & = f'_R - f''_R \frac{\Delta u}{2} \ge f'_R \\
\end{aligned}$$

the relation between the eigenvalues of the systems in the left $\lambda_L = f'(u_L)$ and right state $\lambda_R = f'(u_R)$, and the speed of the shock immediately follows

$$\lambda_L \ge \dot{s} \ge \lambda_R \ .$$

(pde:hyperbolic:entropy:1d-scalar:burgers)=
### Burgers' equation

<!--
The flux of Burgers' equation is $F(u) = \frac{u^2}{2}$. Thus, the relation between an entropy function and its flux reads

$$q'(u) = u \eta'(u) \ .$$

Solutions can be easily found with polynomial functions. A standard choice providing $\eta''(u) \ge 0$ is

$$\eta(u) = \frac{u^2}{2} \quad , \quad q(u) = \frac{u^3}{3} \ .$$

With thiss choice, jump relation reads

$$v_b \frac{1}{2} ( u^2_R - u^2_L ) \ge \frac{1}{3} ( u^3_R - u^3_L ) \ .$$
$$v_b \frac{1}{2} ( u_R + u_L ) \ge \frac{1}{3} ( u^2_R + u_R u_L + u^2_L ) \ .$$

The speed of a shock is $\dot{s} = \frac{[F]}{[u]} = \frac{u_R + u_L}{2}$, so that the jump condition across a shock reads

$$\begin{aligned}
  0 
  & \le \frac{1}{4} ( u_R^2 + 2 u_R u_L + u_L^2 ) - \frac{1}{3} ( u_R^2 +  u_R u_L + u_L^2 ) = \\
\end{aligned}$$
-->

(pde:hyperbolic:entropy:1d-system)=
## Non-linear system of equations in 1-dimensional domain

$$\partial_t \mathbf{u} + \partial_x \mathbf{F}(\mathbf{u}) = \mathbf{0} \ .$$

If a shock originates from the $i^{th}$ characteristic family, the condition $\lambda_{i,L} \ge \dot{s}_i \ge \lambda_{i,R}$ holds.

```{dropdown} Details
:open:

Let $\mathbf{A}(\mathbf{u}) = \nabla_{\mathbf{u}} \mathbf{F}(\mathbf{u})$ the convection matrix, $\mathbf{A} = \mathbf{R} \boldsymbol\Lambda \mathbf{L}$ its spectral decomposition, and $\mathbf{v}$ the characteristic variables s.t. $d \mathbf{v} = \mathbf{L} d \mathbf{u}$, or $d \mathbf{u} = \mathbf{R} d \mathbf{v}$. 

The convective form of the equation reads

$$\partial_t \mathbf{u} + \mathbf{A} \partial_x \mathbf{u} = \mathbf{0} \ ,$$

or in diagonal form using characteristic variables,

$$\partial_t \mathbf{v} + \boldsymbol\Lambda \partial_x \mathbf{v} = \mathbf{0} \ .$$

A shock originating from the $i^{th}$ family of characteristics comes from the scalar equation

$$\partial_t v_i + \lambda_i \partial_x v_i = 0 \ .$$

The speed of the shock satisfies $\dot{s}_i [ \mathbf{u} ]_i = [ \mathbf{F}(\mathbf{u}) ]_i$, with $[ \mathbf{u} ]_i = \mathbf{u}_i^+ - \mathbf{u}_i^-$, and

$$\begin{aligned}
  \mathbf{u}_i^- & = \mathbf{u}(\mathbf{v}_{\notin i}, v_i^-) \\
  \mathbf{u}_i^+ & = \mathbf{u}(\mathbf{v}_{\notin i}, v_i^+) \\
\end{aligned}$$

Taylor expansion of the relation gives (no sum on $i$, as $\Delta v_i$ is the only non-zero component of $\Delta \mathbf{v}$ across a shock originating from the $i^{th}$ family of characteristics)

$$\begin{aligned}
 \dot{s}_i \Delta_i u_k 
 & = \Delta_i F_k = \\
 & = \partial_{u_\ell} F_k \Delta_i u_\ell + \frac{1}{2} \partial_{u_\ell u_m} F_k \Delta_i u_{\ell} \Delta_i u_{m} = \\
 & = A_{k \ell} R_{\ell i} \Delta v_i + \frac{1}{2} \partial_{u_\ell u_m} F_k \Delta_i u_{\ell} \Delta_i u_{m} 
\end{aligned}$$

Exploiting spectral decomposition of the convection matrix

$$\left( \dot{s}_i R_{ki} - R_{km} \Lambda_{mn} \underbrace{L_{n\ell} R_{\ell i}}_{\delta_{ni}} \right) \Delta v_i = \frac{1}{2} \partial_{u_\ell u_m} F_k \Delta_i u_\ell \Delta_i u_m$$

$$\left( \dot{s}_i - \lambda_i \right) R_{ki}\Delta v_i = \frac{1}{2} \partial_{u_\ell u_m} F_k \Delta_i u_\ell \Delta_i u_m$$

$$\left( \dot{s}_i - \lambda_i \right) \Delta_i u_k = \frac{1}{2} \partial_{u_\ell u_m} F_k \Delta_i u_\ell \Delta_i u_m \ .$$

If the flux is convex (here the flux is a vector quantity. Is this the requirement for each of its components $F_k$?), i.e. the Hessian is (semi)definite positive, the right-hand side is always non-negative.


The following relations have been used above

$$d u_l = R_{lm} d v_m \ .$$

$$\Delta_i u_l = \partial_{v_m} u_l \underbrace{\Delta_i v_m}_{= \delta_{im} \Delta v_i} = \partial_{v_i} u_l \Delta v_i = R_{li} \Delta v_i \ .$$

```

```{dropdown} Entropy function for systems
:open:

Let $\eta(\mathbf{u})$ the entropy function of the system $\partial_t \mathbf{u} + \partial_x \mathbf{F}(\mathbf{u}) = \mathbf{0}$. It follows

$$\begin{aligned}
  \partial_t \eta
  & = \partial_{u_i} \eta \, \partial_t u_i \\
  & = - \partial_{u_i} \eta \, \partial_{x} F_i = \\
  & = - \partial_{u_i} \eta \, \partial_{u_j} F_i \, \partial_x u_j = \\
  & = - \partial_{u_j} q \, \partial_x u_j = \\
  & = - \partial_x q \ ,
\end{aligned}$$

i.e. the compatibility equation between the entropy function $\eta(\mathbf{u})$ and the entropy flux $q(\mathbf{u})$ reads

$$\partial_{u_j} q = \partial_{u_j} F_i \, \partial_{u_i} \eta = A_{ij} \partial_{u_i} \eta \ ,$$

or using vector formalism

$$\nabla_{\mathbf{u}} q = \nabla_{\mathbf{u}} \mathbf{F} \cdot \nabla_{\mathbf{u}} \eta = \mathbf{A} \cdot \nabla_{\mathbf{u}} \eta \ .$$

```

```{dropdown} Entropy function in diffusive equations
:open:

Let $\partial_t \mathbf{u} + \partial_x \mathbf{F}(\mathbf{u}) = \partial_x( \mathbf{D} \partial_x \mathbf{u} )$ the diffusive equation. The entropy equation becomes


$$\begin{aligned}
  \partial_t \eta
  & = \partial_{u_i} \eta \, \partial_t u_i \\
  & = - \partial_{u_i} \eta \, \partial_{x} F_i + \partial_{u_i} \eta \partial_x \left( D_{ik} \partial_x u_k \right) = \\
  & = - \partial_{u_i} \eta \, \partial_{u_j} F_i \, \partial_x u_j + \partial_x \left( \partial_{u_i} \eta D_{ik} \partial_x u_k \right) - \partial_x \partial_{u_i} \eta D_{ik} \partial_{x} u_k = \\
  & = - \partial_{u_j} q \, \partial_x u_j + \partial_x \left( \partial_{u_i} \eta D_{ik} \partial_x u_k \right) - \partial_x u_l \partial_{u_l u_i} \eta D_{ik} \partial_{x} u_k \ .
\end{aligned}$$

By definition, if the **diffusion term** is **compatible** with the entropy function, the matrix (is this a matrix, a tensor or a matrix of tensors?) $\nabla_{\mathbf{u} \mathbf{u}} \cdot \mathbf{D}$ is semi-definite positive. If the diffusion term is compatible with the entropy function, in the inviscid limit $D_{ik} \rightarrow 0$, the entropy inequality becomes

$$\partial_t \eta - \partial_x q \le 0 \ .$$

```
```{dropdown} Entropy variables

Now, let the **entropy variables** be $\mathbf{w} := \nabla_{\mathbf{u}} \eta$, $w_i = \partial_{u_i} \eta$. The last term becomes

$$\begin{aligned}
  \frac{\partial u_l}{\partial x} \frac{\partial u_k}{\partial x} \frac{\partial}{\partial u_l} \frac{\partial}{\partial u_i} \eta D_{ik} 
  & = \frac{\partial u_l}{\partial x} \frac{\partial u_k}{\partial x} \frac{\partial}{\partial u_l} w_i D_{ik} = \\
  & = \frac{\partial w_i}{\partial x} D_{ik} \frac{\partial u_k}{\partial x} = \\
  & = \partial_x \mathbf{w} \cdot \mathbf{D} \cdot \left( \nabla_{\mathbf{u} \mathbf{u}} \eta \right)^{-1} \cdot \partial_x \mathbf{w} \ ,
\end{aligned}$$

being
 
$$\partial_x \mathbf{u} = \partial_x \mathbf{w} \cdot \nabla_{\mathbf{w}} \mathbf{u} = \partial_x \mathbf{w} \cdot \left( \nabla_{\mathbf{u}} \mathbf{w} \right)^{-1} = \partial_x \mathbf{w} \cdot \left( \nabla_{\mathbf{u} \mathbf{u}} \eta \right)^{-1}$$

or, by symmetry of the Hessian, $\partial_x \mathbf{u} = \left( \nabla_{\mathbf{u} \mathbf{u}} \eta \right)^{-1} \cdot \partial_x \mathbf{w}$.

Compatibility between the diffusion and the entropy function needs $\mathbf{D} \cdot \left( \nabla_{\mathbf{u} \mathbf{u}} \eta \right)^{-1}$ to be semi-definite positive.


$$\partial_x u_k = \partial_{w_j} u_k \partial_x w_j = \left[ \partial_{u_k} w_j \right]^{-1} \partial_x w_j \ ,$$

$$\delta_{ij} = \partial_{u_i} w_k \partial_{w_k} u_j \ .$$

```


(pde:hyperbolic:entropy:1d-system:p-sys)=
### P-system

A common choice of *entropy function* in a P-system is the mechanical energy (the "reversible" part of the energy).

$$\eta = \rho \left( \frac{1}{2} u^2 + a^2 \ln \frac{\rho}{\rho_0} \right) \ .$$

This quantity decreases across shocks. Corresponding flux reads

$$q = \rho \left( \frac{1}{2} u^2 + a^2 \ln \frac{\rho}{\rho_0} + a^2 \right) u \ .$$

```{dropdown} Details
:open:

Taking the time derivative of the entropy function,

$$\begin{aligned}
 \eta_{/t} 
 & = \rho_{/t} \frac{u^2}{2} + \rho u u_{/t} + a^2 \rho_{/t} \ln \frac{\rho}{\rho_0} + a^2 \rho_{/t} = \\
 & = \left( \frac{u^2}{2} + a^2 \ln \frac{\rho}{\rho_0} + a^2 \right) \rho_{/t} + u \rho u_{/t} = \\
 & = - \left( \frac{u^2}{2} + a^2 \ln \frac{\rho}{\rho_0} + a^2 \right) (\rho u)_{/x} - u \left( \rho u u_{/x} + a^2 \rho_{/x} \right) = \\
 & = - \left( \rho \frac{u^2}{2} u \right)_{/x} \underbrace{- a^2 \ln \frac{\rho}{\rho_0} \rho u_{/x} - a^2 \ln \frac{\rho}{\rho_0} u \rho_{/x} - a^2 \rho_{/x} u}_{= - \left( a^2 \rho \ln \frac{\rho}{\rho_0} u \right)_{/x}} \underbrace{- a^2 \rho u_{/x} - a^2 \rho_{/x} u}_{= - ( a^2 \rho u )_{/x}} = \\
 & = - \left[ \left( \rho \frac{u^2}{2} + a^2 \rho \ln \frac{\rho}{\rho_0} + \rho a^2  \right) u \right]_{/x} \ .
\end{aligned}$$



<!--
P-system equations don't include total energy equation, but only mass and momentum balance. From momentum balance kinetic energy (and mechanical energy) balance can be derived after multiplication by the velocity field $u = \frac{m}{\rho}$.

Convective form of viscous P-system equations reads

$$\begin{cases}
  \partial_t \rho + u \partial_{x} \rho + \rho \partial_x u = 0 \\
  \rho \partial_t u + \rho u \partial_x u + \partial_x p - \partial_x ( \nu \partial_x u ) = 0 \ .
\end{cases}$$

...
-->

```

(pde:hyperbolic:entropy:1d-system:shallow-water)=
### Shallow water
 
(pde:hyperbolic:entropy:1d-system:euler)=
### Euler equations



