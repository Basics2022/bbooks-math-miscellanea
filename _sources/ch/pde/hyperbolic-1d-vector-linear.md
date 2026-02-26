(pde:hyperbolic:problems:1d-vector-linear)=
# Linear vector equation

**Differential equation.**

$$\begin{aligned}
  \mathbf{r}
  & = \partial_t \mathbf{u} + \mathbf{A} \partial_x \mathbf{u}                 && \text{  convective form} \\
  & = \partial_t \mathbf{u} + \partial_x \left( \mathbf{A} \mathbf{u} \right)  && \text{conservative form} 
\end{aligned}$$

**Integral eqaution.** On a control volume $V$ at rest

$$\int_{V} \mathbf{r} = \dfrac{d}{dt} \int_V \mathbf{u} + \oint_{\partial V} n_x \mathbf{A} \mathbf{u} \ .$$

Integral equation in an arbitrary domain $v_t$ can be derived using [Reynolds' transport theorem](tensor:calculus:time-derivative-of-integrals:volume-density).

**Method of characteristics.** Let $\mathbf{A}$ be diagonalizable, 

$$\begin{aligned}
  \mathbf{A} \mathbf{R} & = \mathbf{R} \mathbf{S} \\
  \mathbf{A} & = \mathbf{R} \mathbf{S} \mathbf{L} \\
\end{aligned}$$

Using spectral decomposition and multiplying the PDE by $\mathbf{L}$, the PDE is transformed in a set of scalar PDE equations,

$$\begin{aligned}
  \mathbf{L} \mathbf{r}
  & = \mathbf{L} \left( \partial_t \mathbf{u} + \mathbf{R} \mathbf{S} \mathbf{L} \partial_x \mathbf{u} \right) = \\
  & = \mathbf{L} \partial_t \mathbf{u} + \mathbf{S} \mathbf{L} \partial_x \mathbf{u} = \\
  & = \partial_t \mathbf{v} + \mathbf{S} \partial_x \mathbf{v} \ ,
\end{aligned}$$

or 

$$\partial_t v_i + s_i \partial_x v_i = L_{ik} r_k \ ,$$

having introduced the characteristic variables $\mathbf{v}(x,t) := \mathbf{L} \mathbf{u}(x,t)$. If the source is not function of the unknown function $\mathbf{u}(x,t)$, this is a system of decoupled PDEs. The solution of the vector PDE follows from the solution of $n$ scalar PDE linear equations. Using methods of characteristics, the solution of the $i^{th}$ scalar PDE equation can be recast as the solution of pairs of ODEs, after writing $V_i(t) = v_i(X_i(t), t)$, being $X_i(t)$ the equation of a curve belonging to the $i^{th}$ familiy of characteristics,

$$\begin{cases}
  \dot{X}_i = s_i \\
  \dot{V}_i = L_{ik} r_k \ .
\end{cases}$$

As the spectral decomposition of a constant matrix is constant, the characteristic lines are straight lines $X_i(t) = s_i t + c$. In general, the solution of the dynamical equations of the characteristic variables $V_i$ is a full system of $n$ ODEs.

**Particular case: no source.** As a particular case, if the source term is identically zero, $\mathbf{r}(x,t) = \mathbf{0}$, characteristic variable $V_i(t)$ is constant along each characteristic line $X_i(t;\dots)$ of the $i^{th}$ family of characteristics.

...

$$u_k(x,t) = R_{ki} v_i(x,t) = R_{ri} v_i(x_{0,i} + s_i(t-t_{0,i}), t) \ .$$

