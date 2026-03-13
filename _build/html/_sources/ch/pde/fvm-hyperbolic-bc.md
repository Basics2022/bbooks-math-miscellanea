(pde:fvm:hyperbolic:bc)=
# Boundary conditions in hyperbolic problems

(pde:fvm:hyperbolic:bc:wall)=
## Wall

### Domain at rest

```{prf:example} Wall for Roe flux in 1-dimensional P-sys

**Roe intermediate state for a P-sys** is

$$\begin{bmatrix} \hat{\rho} \\ \hat{m} \end{bmatrix} = \begin{bmatrix} \hat{\rho} \\ \hat{\rho} \hat{u} \end{bmatrix} \ ,$$

with $\hat{\rho}$ satisfying consistency (as an example $\hat{\rho} = \sqrt{\rho_L \rho_R}$ or $\hat{\rho} = \frac{1}{2} \left( \rho_L + \rho_R \right)$), and 

$$\hat{u} = \frac{\sqrt{\rho_L} u_L + \sqrt{\rho_R} u_R}{\sqrt{\rho_L}+\sqrt{\rho_R}} \ .$$

Wall boundary conditions for a P-sys implies no mass flux through the wall. The state of the ghost cell outside the domain is prescribed as

$$\mathbf{u}_{g} = \begin{bmatrix} \rho_{g} \\ \rho_{g} u_{g} \end{bmatrix} \ ,$$

with $\rho_{g} = \rho_{\partial}$, $u_{g} = - u_{\partial}$. Roe intermediate state across the wall boundary interface has velocity

$$\hat{u}_{\partial} = \frac{\sqrt{\rho_g} u_g + \sqrt{\rho_{\partial}} u_{\partial}}{\sqrt{\rho_g} + \sqrt{\rho_{\partial}}} = 0 \ .$$

**Upwind matrix in Roe flux.** Using the spectral decomposition of the matrix 

$$\mathbf{A} = \begin{bmatrix} u & \rho \\ \frac{a^2}{\rho} & u  \end{bmatrix} \ ,$$

i.e.

$$
\mathbf{R} = \begin{bmatrix} \rho & \rho \\ a & -a \end{bmatrix} \quad , \quad
\boldsymbol\Lambda = \begin{bmatrix} u-a & 0 \\ 0 & u+a \end{bmatrix} \quad , \quad
\mathbf{L} = \begin{bmatrix} \frac{1}{2\rho} & \frac{1}{2a} \\ \frac{1}{2\rho} & -\frac{1}{2a} \end{bmatrix}
$$

the upwind matrix evaluated on the Roe intermediate state (no need for entropy fix; with entropy fix, the result doesn't change anyway, as there's no eigenvalue close to zero) reads

$$\begin{aligned}
|\hat{\mathbf{A}}|
= \hat{\mathbf{R}} \left| \hat{\boldsymbol{\Lambda}} \right| \hat{\mathbf{L}} 
& = \begin{bmatrix} \rho & \rho \\ a & -a \end{bmatrix} \begin{bmatrix} a & 0 \\ 0 & a \end{bmatrix} \begin{bmatrix} \frac{1}{2\rho} & \frac{1}{2a} \\ \frac{1}{2\rho} & -\frac{1}{2a} \end{bmatrix} = \\
& = \begin{bmatrix} \rho a & \rho a \\ a^2 & -a^2 \end{bmatrix} \begin{bmatrix} \frac{1}{2\rho} & \frac{1}{2a} \\ \frac{1}{2\rho} & -\frac{1}{2a} \end{bmatrix} = \\
& = \begin{bmatrix} a & 0 \\ 0 & a \end{bmatrix} \ . 
\end{aligned}$$

**Roe flux.** Putting everything together, Roe flux at wall reads

$$\begin{aligned}
  \mathbf{F}_{\partial} 
  & = \frac{1}{2} \left[ \mathbf{F}_{g} + \mathbf{F}_{\partial} - \left| \hat{\mathbf{A}} \right| \left( \mathbf{u}_{g} - \mathbf{u}_{\partial} \right) \right] = \\
  & = \frac{1}{2} \left[ \begin{bmatrix} -m_\partial \\ \rho_\partial \left( a^2 + u^2_\partial \right)  \end{bmatrix} + \begin{bmatrix} m_\partial \\ \rho_g \left( a^2 + u^2_\partial \right) \end{bmatrix} - \begin{bmatrix} a & 0 \\ 0 & a \end{bmatrix} \left( \begin{bmatrix} \rho_\partial \\ -m_\partial \end{bmatrix} - \begin{bmatrix} \rho_\partial \\ m_\partial \end{bmatrix} \right) \right] = \\
  & = \begin{bmatrix} 0 \\ \rho_\partial ( a + u_\partial )^2 \end{bmatrix} \ ,
\end{aligned}$$

i.e. there's **no mass flux** across the wall, as the first component of the vector $\mathbf{F}_\partial$ is zero.



```

```{prf:example} Wall for Roe flux in 1-dimensional Euler equations


```

### Moving domain



(pde:fvm:hyperbolic:bc:characteristics)=
## Characteristic-based boundary conditions


