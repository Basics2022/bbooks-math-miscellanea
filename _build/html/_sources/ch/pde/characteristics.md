(pde:hyperbolic:characteristics)=
# Method of characteristics

## Scalar multi-dimensional problem

$$\begin{aligned}
  \mathbf{a}^T(u(\mathbf{x}), \mathbf{x}) \, \boldsymbol\nabla  u(\mathbf{x}) & = c(u(\mathbf{x}), \mathbf{x}) \quad , \quad \mathbf{x} \in D \\
  a_k(u(\mathbf{x}), \mathbf{x}) \frac{\partial}{\partial x_k} u(\mathbf{x}) & = c(u(\mathbf{x}), \mathbf{x}) 
\end{aligned}$$

The method of characteristics aims at transforming the PDE over the domain $D$, in a set of ODEs over lines - the characteristic lines. Both the coordinates of these lines and the unknown function on these lines are written in parametric form as

$$\begin{aligned}
  \mathbf{x} & = \mathbf{X}(s) \\
  u(\mathbf{X}(s)) & = U(s) \ .
\end{aligned}$$

Now, taking the ordinary derivative of $U'(s)$,

$$U'(s) = \frac{d X_k}{d s}(s) \frac{\partial u}{\partial x_k}\left( \mathbf{X}(s) \right) \ .$$

If the characteristic lines are defined by the differential equation $X'_k(s) = a_k(U(s), X(s))$, the set of ODEs become

$$\begin{aligned}
 U'(s) & = c\left(U(s), \mathbf{X}(s)\right) \\
 \mathbf{X}'(s) & = \mathbf{a}\left(U(s), \mathbf{X}(s)\right) \ .
\end{aligned}$$

## Vector multi-dimensional problem

**todo** *Characteristic method fails...characteristic - eikonal - equation. Uncomment*

Let 

$$\begin{aligned}
  \mathbf{u}(t, \mathbf{r}): & \ \mathbb{R} \times \mathbb{R}^d \rightarrow \mathbb{R}^n \\
  \mathbf{F}(   \mathbf{u}): & \ \mathbb{R}^{n} \rightarrow \mathbb{R}^{d} \times \mathbb{R}^n \\
  \mathbf{s}(t, \mathbf{r}): & \ \mathbb{R} \times \mathbb{R}^d \rightarrow \mathbb{R}^n \\
\end{aligned}$$

the conservative form of a hyperbolic problem reads

$$\begin{aligned}
  \partial_t \mathbf{u} + \nabla \cdot \mathbf{F}(\mathbf{u}) & = \mathbf{s} \\
  \partial_t u_i + \partial_j F_{ji} & = s_i \ .
\end{aligned}$$

Expanding the divergence of the flux, the convective (quasi-linear? It makes little to no sense to me...) form follows

$$\begin{aligned}
  s_i 
  & = \partial_t u_i + \sum_{j=1}^{d} \partial_j F_{ji} = \\
  & = \partial_t u_i + \sum_{j=1}^{d} \sum_{k=1}^{n} \partial_j u_k \partial_{u_k} F_{ji} = \\
  & = \partial_t u_i + \sum_{j=1}^{d} \sum_{k=1}^{n} A^{j}_{ik}(\mathbf{u}) \, \partial_j u_k  \ ,
\end{aligned}$$

for every component $i = 1:n$, or

$$\mathbf{s} = \partial_t \mathbf{u} + \sum_{j=1}^{d} \mathbf{A}^j \partial_j \mathbf{u} \ .$$

This problem can be made a little more general with by defining $\mathbf{x} = (t, \mathbf{r}) = ( x_0, \mathbf{r} )$, as

$$\sum_{j=0}^{d} \mathbf{A}^j \, \partial_j \mathbf{u} = \mathbf{s} \ .$$

The former expression of the hyperbolic problem immediately follows if $\mathbf{A}_0 = \mathbf{I}_n$, $A^0_{ik} = \delta_{ik}$, and 

$$\widetilde{\nabla} \cdot \widetilde{\mathbf{F}} = \partial_0 \mathbf{F}_0 + \sum_{j=1}^{d} \partial_j \mathbf{F}_j = \widetilde{\nabla} \cdot \begin{bmatrix} \ \mathbf{u} \ | \ \mathbf{F} \ \end{bmatrix} \ .$$

as, for $i = 1:n$,

$$\delta_{ik} = \partial_{u_k} F_{0i} \quad \rightarrow \quad F_{0i} = u_k \delta_{ik} = u_i \ .$$


### Taylor expansion of a solution

Starting from the solution on a manifold determined by the equation $S: f(\mathbf{x}) = 0$, $\mathbf{x}_0 \in S$, if the solution is differentiable, the solution in a point $\mathbf{x} = \mathbf{x}_0 + \Delta \mathbf{x}$ reads

$$\begin{aligned}
  \mathbf{u}(\mathbf{x}) & \sim \mathbf{u}(\mathbf{x}_0) + \Delta \mathbf{x} \cdot \nabla \mathbf{u}(\mathbf{x}_0) \\
  u_i(\mathbf{x}) & \sim u_i(\mathbf{x}_0) + \Delta_j \frac{\partial u_i}{\partial x_j} \ .
\end{aligned}$$

Now, with a change of coordinates from $\mathbf{x}$ to $\boldsymbol\xi = (n, \mathbf{t})$, i.e. to local normal and tangential direction,

$$\begin{aligned}
  \nabla \mathbf{u} 
  = \hat{\mathbf{x}}_i \frac{\partial}{\partial x_i} \mathbf{u} 
  = \hat{\mathbf{x}}_i \frac{\partial \mathbf{u}}{\partial x_i} 
  = \hat{\mathbf{x}}_i \frac{\partial \mathbf{u}}{\partial \xi_k} \frac{\partial \xi_k}{\partial x_i} 
  = \hat{\boldsymbol\xi}_k \frac{\partial \mathbf{u}}{\partial \xi_k}
\end{aligned}$$

Inserting in the hyperbolic equation

$$\begin{aligned}
  s_i
  & = \sum_{j=0}^{d} A^{j}_{ik} \frac{\partial u_k}{\partial x_j} = \\
  & = \sum_{j=0}^{d} A^{j}_{ik} \sum_{\ell=0}^{d} \frac{\partial u_k}{\partial \xi_\ell} \frac{\partial \xi_\ell}{\partial x_j} = \\ 
  & = \sum_{\ell=0}^{d}  \sum_{j=0}^{d}  A^{j}_{ik} \frac{\partial \xi_\ell}{\partial x_j} \frac{\partial u_k}{\partial \xi_\ell} = \\ 
  & = \sum_{\ell=0}^{d}  \sum_{j=0}^{d}  A^{j}_{ik} \xi^\ell_j \frac{\partial u_k}{\partial \xi_\ell} \ ,
\end{aligned}$$

and separating the normal $\ell = 0$ from the tangential $\ell=1:d$ coordinates,

$$\begin{aligned}
  s_i
  & = \sum_{j=0}^{d} A^j_{ik} \xi^0_j \frac{\partial u_k}{\partial \xi_0} + \sum_{\ell=1}^{d} \sum_{j=0}^{d} A^j_{ik} \xi^t_j \frac{\partial u_k}{\partial \xi_t} = \\
  & = \sum_{j=0}^{d} A^j_{ik} n_j \frac{\partial u_k}{\partial n} + \sum_{\ell=1}^{d} \sum_{j=0}^{d} A^j_{ik} t^\ell_j \frac{\partial u_k}{\partial t_\ell} = \\
  & = \sum_{j=0}^{d} n_j \mathbf{A}^j \partial_n \mathbf{u} + \sum_{\ell=1}^{d} \sum_{j=0}^{d} t^\ell_j \mathbf{A}^j \partial_{t_\ell} \mathbf{u} \ .
\end{aligned}$$

On a smooth surface where the solution is known, all the tangential derivatives of the solution are known as well. In order to evaluate the normal derivative $\partial_n \mathbf{u}$ from the PDE, the (formal) inversion of the matrix

$$\mathbf{A}_{\hat{\mathbf{n}}} := \sum_{j=0}^{d} n_j \, \mathbf{A}^j \ ,$$

must be invertible, to formally get

$$\partial_n \mathbf{u} = \mathbf{A}_{\hat{\mathbf{n}}}^{-1} \left( \mathbf{s} - \sum_{\ell=1}^{d} \mathbf{A}_{\hat{\mathbf{t}}_\ell} \partial_{t_\ell} \mathbf{u} \right) \ .$$

This expression of the normal derivative of the solution - whenever it exists - can be used to find the approximation of the solution in normal direction w.r.t. the surface $S$, i.e. with $\Delta \mathbf{x} = \Delta \ell \hat{\mathbf{n}}$ as

$$\begin{aligned}
  \mathbf{u}(\mathbf{x}) 
  & \sim \mathbf{u}(\mathbf{x}_0) + \Delta \ell \, \hat{\mathbf{n}} \cdot \nabla \mathbf{u}(\mathbf{x}_0) = \\
  & = \mathbf{u}(\mathbf{x}_0) + \Delta \ell \, \partial_{n} \mathbf{u}(\mathbf{x}_0) \ .
\end{aligned}$$

**If** the matrix $\mathbf{A}_{\hat{\mathbf{n}}}$ is diagonalizable, it's invertible if it has no zero eigenvalue. Let $\hat{\mathbf{n}}_i$ be a unit vector so that the matrix $\mathbf{A}_{\hat{\mathbf{n}}}$ has an eigenvalue equal to zero $s_0 = 0$, with right and left eigenvectors $\mathbf{r}_0$, $\mathbf{l}_0$. Recalling the expression of the PDE in normal and tangential components

$$\mathbf{s} = \mathbf{A}_{\hat{\mathbf{n}}} \partial_n \mathbf{u} + \sum_{\ell=1}^{d} \mathbf{A}_{\hat{\mathbf{d}}_\ell} \partial_{t_\ell} \mathbf{u} \ ,$$

left-multiplying by $\mathbf{l}$ gives

$$\mathbf{l}^T_0 \mathbf{s} = \mathbf{l}_0^T \sum_{\ell=1}^{d} \mathbf{A}_{\hat{\mathbf{d}}_\ell} \partial_{t_\ell} \mathbf{u} = \qquad \dots \qquad = \mathbf{l}_0^T \sum_{k=0}^{d} \mathbf{A}^k \partial_k \mathbf{u} \ .$$


**todo** 
- *compatibility conditions*
- *eikonal equation*
- *explicitly treating steady vs. unsteady problems*

### Examples

#### Isothermal compressible flow

- Conservative variables: $(\rho, \vec{m})$
- Physical variables: e.g. $(\rho, \vec{u})$, $(P, \vec{u})$,...

Conservative form reads

$$\begin{cases}
  \partial_t \rho + \nabla \cdot \mathbf{m} = 0 \\
  \partial_t \mathbf{m} + \nabla \cdot \left[ \frac{\mathbf{m}\otimes\mathbf{m}}{\rho} + \rho a^2 \mathbf{I} \right] = 0 \\
\end{cases}$$

Convective form in a 2-dimensional domain reads

$$
\partial_t \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} +
\begin{bmatrix}
  \cdot & 1     & \cdot \\
  a^2 - \frac{m_x m_x}{\rho^2} & \frac{2 m_x}{\rho} & \cdot \\
      - \frac{m_x m_y}{\rho^2} & \frac{m_y}{\rho} & \frac{m_x}{\rho} \\
\end{bmatrix} \partial_x \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} +
\begin{bmatrix}
  \cdot & \cdot & 1     \\
  - \frac{m_x m_y}{\rho^2} & \frac{m_y}{\rho} & \frac{m_x}{\rho} \\
  a^2 - \frac{m_y m_y}{\rho^2} & \cdot & \frac{2 m_y}{\rho} \\
\end{bmatrix} \partial_y \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} = \mathbf{0}
$$

```{dropdown} Some algebra

$$\begin{aligned}
  0 & = \rho_{/t} + m_{x/x} + m_{y/y}  \\
  0 & = m_{i/t} + \partial_{j} \left( \frac{m_j m_i}{\rho} + \rho a^2 \delta_{ij} \right) \ .
\end{aligned}$$

```

Thus,

$$\begin{aligned}
\mathbf{A}_{\hat{\mathbf{n}}} 
& = 
\begin{bmatrix} 
  \cdot & n_x & n_y \\
  a^2 n_x - u_n u_x & u_x n_x + u_n & u_x n_y \\
  a^2 n_y - u_n u_y & u_y n_x & u_n + u_y n_y \\
\end{bmatrix} = \\
& = 
\begin{bmatrix}
  0 & \mathbf{n}^T \\
  a^2 \mathbf{n} - ( \mathbf{n}^T \mathbf{u} ) \mathbf{u} &  \mathbf{n}^T \mathbf{u} \mathbf{I} + \mathbf{u} \mathbf{n}^T
\end{bmatrix} = \\
& = 
\begin{bmatrix}
  0 & \hat{\mathbf{n}}^T \\
  a^2 \mathbf{n} - ( \mathbf{n} \cdot \mathbf{u} ) \mathbf{u} & ( \mathbf{n} \cdot \mathbf{u} ) \mathbb{I} + \mathbf{u} \otimes \mathbf{n}
\end{bmatrix} \ .
\end{aligned}$$


```{dropdown} Eigenvalues. Details

The eigenvalue decomposition of the matrix $\mathbf{A}_{\hat{\mathbf{n}}}$ follows from

$$\begin{aligned}
  0 & = \left| \mathbf{A}_{\hat{\mathbf{n}}} - s \mathbf{I} \right| =
\left|
\begin{bmatrix}
  -s & \mathbf{n}^T \\
  a^2 \mathbf{n} - u_n \mathbf{u} & ( u_n - s ) \mathbf{I} + \mathbf{u} \mathbf{n}^T
\end{bmatrix} 
\right| = \\
  & = -s ( u_n + u_x n_x - s ) ( u_n + u_y n_y - s ) + n_x u_x n_y ( a^2 n_y - u_n u_y ) + n_y u_y n_x ( a^2 n_x - u_n u_x ) + \\
  &  - ( a^2 n_y - u_n u_y ) ( u_x n_x + u_n - s) n_y 
     - ( a^2 n_x - u_n u_x ) ( u_y n_y + u_n - s) n_x
     - s u_x u_y n_x n_y = \\
  & =
            s^3 ( - 1 ) + \\
  & \quad + s^2 ( u_n + u_y n_y + u_n + u_x n_x ) + \\
  & \quad + s   ( - ( u_n + u_x n_x ) ( u_n + u_y n_y ) + n_y ( a^2 n_y - u_n u_y ) + n_x ( a^2 n_x - u_n u_x ) - u_x n_x u_y n_y ) + \\
  & \quad + 1 \cdot (  n_x u_x n_y ( a^2 n_y - u_n u_y ) + n_y u_y n_x ( a^2 n_x - u_n u_x ) - n_y (  a^2 n_y - u_n u_y )( u_x n_x + u_n ) - n_x ( a^2 n_x - u_n u_x )( u_y n_y + u_n ) ) = \\
  & = - s^3 + 3 u_n s^2 + s ( - u_n^2 - u_n (u_x n_x + u_y n_y) - u_x n_x u_y n_y - u_n u_y n_y - u_n u_x n_x + a^2 - u_x n_x u_y n_y ) + \\
  & \quad + ( a^2 \left( n_y^2 u_x n_x + n_x^2 n_y u_y - n_y^2 u_x n_x - n_y^2 u_n - n_x^2 u_y n_y - u_n n_x^2 \right) - u_n u_x n_x u_y n_y - u_n u_x n_x u_y n_y +u_n u_x n_x u_y n_y + u_n^2 u_y n_y + u_n u_x n_x u_y n_y + u_n^2 u_x n_x ) = \\ 
  & = - s^3 + 3 u_n s^2 + s ( a^2 - 3 u_n^2 ) - u_n  ( a^2 - u_n^2 ) = \\
  & = - ( s - u_n )^3 + ( s - u_n ) a^2 = \\
  & = - ( s - u_n ) ( ( s - u_n )^2 - a^2 ) \ .
\end{aligned}$$

```

Thus the eigenvalues of the matrix $\mathbf{A}_{\hat{\mathbf{n}}}$ are

$$s_{1,3} = u_n \mp a \quad , \quad s_2 = u_n \ ,$$

and the right and left eigenvectors follow

$$\begin{aligned}
  \mathbf{R} & = \\
  \mathbf{L} & = \\
\end{aligned}$$



```{dropdown} Right and left eigenvectors. Details

For $s_{1,3} = u_n \mp  a$,

$$
\mathbf{0} = \begin{bmatrix} -u_n \pm a & \mathbf{n}^T \\ a^2 \mathbf{n} - u_n \mathbf{u} & \pm a \mathbf{I} + \mathbf{u} \mathbf{n}^T \end{bmatrix}
\begin{bmatrix} \hat{\rho} \\ \hat{\mathbf{m}} \end{bmatrix}
$$

From the first equation it follows $\hat{m}_n = ( u_n \mp a ) \hat{\rho}$, and thus the momentum equation gives

$$\begin{aligned}
  \mathbf{0}
  & = \hat{\rho} ( a^2 \mathbf{n} - u_n \mathbf{u} ) \pm a \hat{\mathbf{m}} + \mathbf{u} \hat{m}_n = \\
  & = \hat{\rho} ( a^2 \mathbf{n} - u_n \mathbf{u} ) \pm a \hat{\mathbf{m}} + \mathbf{u} ( u_n \mp a ) \hat{\rho} = \\
  & = \hat{\rho} ( a^2 \mathbf{n} \mp a \mathbf{u} ) \pm a \hat{\mathbf{m}} \ ,
\end{aligned}$$

and thus

$$\hat{\mathbf{m}}_{1,3} = \hat{\rho}_{1,3} ( \mathbf{u} \mp a \mathbf{n} ) \ . $$

For $s_{2} = u_n$,

$$
\mathbf{0} = \begin{bmatrix} -u_n & \mathbf{n}^T \\ a^2 \mathbf{n} - u_n \mathbf{u} & \mathbf{u} \mathbf{n}^T \end{bmatrix}
\begin{bmatrix} \hat{\rho} \\ \hat{\mathbf{m}} \end{bmatrix}
$$

From the first equation it follows $\hat{m}_n = u_n \hat{\rho}$, and thus the momentum equation gives

$$\begin{aligned}
  \mathbf{0}
  & = \hat{\rho} ( a^2 \mathbf{n} - u_n \mathbf{u} ) + \mathbf{u} \, \hat{m}_n = \\
  & = \hat{\rho} ( a^2 \mathbf{n} - u_n \mathbf{u} ) + \mathbf{u} \, u_n \, \hat{\rho} = \\
  & = \hat{\rho}   a^2 \mathbf{n} \ ,
\end{aligned}$$

and thus $\hat{\rho}_2 = 0$. The components of the momentum readily follows from mass equation that is equivalent to the condition

$$\mathbf{n}^T \hat{\mathbf{m}}_{2} = 0 \ ,$$

i.e. as an example $\hat{\mathbf{m}}_{2} = \begin{bmatrix} n_y \\ -n_x \end{bmatrix}$.

Assuming positive density, it's possible to write all the eigenvectors with the proper physical dimensions, and collect them in the matrix of right eigenvectors,

$$\mathbf{R} = \begin{bmatrix}
  \rho & 0 & \rho \\
  \rho ( u - a n_x ) &   \rho a n_y &  \rho ( u + a n_x ) \\ 
  \rho ( v - a n_y ) & - \rho a n_x &  \rho ( v + a n_y ) 
\end{bmatrix} \ .$$

The determinant reads

$$\begin{aligned}
  \frac{1}{\rho^3 a^2} |\mathbf{R}|
  & =   n_y ( v + n_y ) - ( u - n_x ) n_x - n_y ( v - n_y ) + n_x ( u + n_x ) = 2 \ .
\end{aligned}$$

The inverse matrix reads

$$\begin{aligned}
\mathbf{L} 
& = \frac{1}{|\mathbf{R}|} \, \rho^2 \,
\begin{bmatrix}
   a ( a + u_n )       &  - a n_x  & -   a n_y \\
   2a( n_x v - n_y u ) & 2 a n_ y  & - 2 a n_x \\
   a ( a - u_n )       &    a n_x  &     a n_y \\
\end{bmatrix} = \\
& =
\frac{1}{2 \rho a^2}
\begin{bmatrix}
   a ( a + u_n )       &  - a n_x  & -   a n_y \\
   2a( n_x v - n_y u ) & 2 a n_ y  & - 2 a n_x \\
   a ( a - u_n )       &    a n_x  &     a n_y \\
\end{bmatrix} \ .
\end{aligned}$$

as

$$\begin{aligned}
   L_{11} & \propto  a n_y (v+a n_y) + a n_x (u+a n_x) = a u_n + a^2   \\ 
  -L_{21} & \propto (u-a n_x)(v+a n_y) - (v-a n_y) (u+a n_x) = 2 a u n_y - 2 a n_x v   \\ 
   L_{31} & \propto -a n_x (u-a n_x) - a n_y (v- a n_y) = - a u_n + a^2  \\ 
  -L_{12} & \propto a n_x \\ 
   L_{22} & \propto ( v+ a n_y) - (v - a n_y) = 2 a n_y   \\ 
  -L_{32} & \propto - a n_x   \\ 
   L_{13} & \propto - a n_y   \\ 
  -L_{23} & \propto ( u + a n_x ) - ( u - a n_x ) = 2 a n_x  \\ 
   L_{33} & \propto a n_y   \\ 
\end{aligned}$$

Some check

$$\begin{aligned}
  \mathbf{L} \mathbf{R} 
  & = \frac{1}{2 \rho a^2} \begin{bmatrix} a ( a + u_n) & - a \mathbf{n}^T \\ 2 a (n_x v - n_y u) & 2 a \mathbf{t}^T \\ a ( a - u_n ) & a \mathbf{n}^T \end{bmatrix} \begin{bmatrix} 1 & 0 & 1 \\ \mathbf{u} - a \mathbf{n} & a \mathbf{t} & \mathbf{u} + a \mathbf{n} \end{bmatrix} \, \rho = \\
  & = \frac{1}{2 a^2} \begin{bmatrix}
  a^2 + a u_n - a u_n + a^2 & - a\mathbf{n}^T\mathbf{t} &  a^2 + a u_n - a u_n - a^2 \\
  2 a ( n_x v - n_y u ) + 2 a ( n_y u - n_x v ) & 2 a^2 &  2 a ( n_x v - n_y u ) + 2 a ( n_y u - n_x v ) \\
  a^2 - a u_n + a u_n - a^2 &   a\mathbf{n}^T\mathbf{t} &  a^2 - a u_n + a u_n + a^2 \\
  \end{bmatrix} = \mathbf{I}_3 \ .
\end{aligned}$$

```

**Normal vectors of the characteristic surfaces.** For **locally supersonic flows**, $|\mathbf{u}| > a$, there are three directions, i.e. three unit vectors $\hat{\mathbf{n}}_i$ that make the eigenvalues equal to zero,

$$\hat{\mathbf{n}}_{1,3} \cdot \mathbf{u} = \pm a \quad , \quad \hat{\mathbf{n}}_{2} \cdot \mathbf{u} = 0 \ ,$$

or equivalently

$$\hat{\mathbf{n}}_{1,3} \cdot \left( \mathbf{u} \mp a \hat{\mathbf{n}}_{1,3} \right) = 0 \quad , \quad \hat{\mathbf{n}}_2 \cdot \mathbf{u} = 0 \ .$$

Let $\hat{\mathbf{u}}$ the unit vector along the local velocity field, it follows

$$u \hat{\mathbf{u}} \cdot \hat{\mathbf{n}}_{1,3} = \pm a \ ,$$

i.e.

$$\cos \theta_{1,3} = \pm \frac{a}{u} = \pm \frac{1}{M} \ .$$

For **locally subsonic flows**, $|\mathbf{u}| < a$, the eigenvalues $s_{1,3}$ are always negative and positive respectively, while the eigenvalue $s_2$ becomes equal to zero for unit vectors that are orthogonal w.r.t. the local velocity.

```{dropdown} Right and left eigenvectors

Right eigenvector problem reads

$$\mathbf{A} \mathbf{R} = \mathbf{R} \mathbf{S} \ ,$$

s.t. $\mathbf{A} \mathbf{r}_i = s_i \mathbf{r}_i$, with $\mathbf{r}_i$ the $i^{th}$ column of matrix $\mathbf{R}$.

Left eigenvector problem reads

$$\mathbf{L} \mathbf{A} = \mathbf{S} \mathbf{L} \ ,$$

s.t. $\mathbf{l}_i^T \mathbf{A} = s_i \mathbf{l}_i^T \mathbf{A}$, with $\mathbf{l}_i^T$ the $i^{th}$ row of matrix $\mathbf{L}$.

```

**Compatibility equations.** For **locally supersonic flows**, for $s_{1,3} = u_n \mp a$, $u_n = \pm a$ to get $s_{1,3} = 0$, and thus the left eigenvectors for those choices of unit vector become

$$\begin{aligned}
  \mathbf{l}_{0; 1,3}^T
  & = \frac{1}{2 \rho a^2} \begin{bmatrix} \  a ( a \pm u_n ) \ | \ \mp a \mathbf{n}^T_{1,3} \end{bmatrix} = \\
  & = \frac{1}{2 \rho a} \begin{bmatrix} \ 2 a \ | \mp \mathbf{n}^T_{1,3} \ \end{bmatrix} \ .
\end{aligned}$$

The quasi linear form of the equations becomes

**todo** *Check algebra, and UNCOMMENT!*

$$\begin{aligned}
0 
& = \frac{1}{2 \rho a} \left[ \ 2 a \ | \ \mp \mathbf{n}^T_{1,3} \ \right] \left( 
\partial_t \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} +
\begin{bmatrix}
  \cdot & 1     & \cdot \\
  a^2 - \frac{m_x m_x}{\rho^2} & \frac{2 m_x}{\rho} & \cdot \\
      - \frac{m_x m_y}{\rho^2} & \frac{m_y}{\rho} & \frac{m_x}{\rho} \\
\end{bmatrix} \partial_x \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} +
\begin{bmatrix}
  \cdot & \cdot & 1     \\
  - \frac{m_x m_y}{\rho^2} & \frac{m_y}{\rho} & \frac{m_x}{\rho} \\
  a^2 - \frac{m_y m_y}{\rho^2} & \cdot & \frac{2 m_y}{\rho} \\
\end{bmatrix} \partial_y \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} = \mathbf{0}
\right) = \\
0
& = \dots \partial_t \dots + \\
& \quad + \left[ \mp a^2 n_x \pm u_n u_x \ | \ 2 a  \mp u_x n_x \mp u_n \ | \ \mp n_y u_x \ \right] \partial_x \begin{bmatrix} \rho \\ \mathbf{m} \end{bmatrix} +  \\
& \quad + \left[ \mp a^2 n_y \pm u_n u_y \ | \ \mp n_x u_y \ | \ 2 a \mp u_y n_y \mp u_n \ \right] \partial_y \begin{bmatrix} \rho \\ \mathbf{m} \end{bmatrix} = \\
& =       \left[ \left( \mp a^2 n_x \pm u_n u_x \right) \partial_x + \left( \mp a^2 n_y \pm u_n u_y \right) \partial_y \right] \rho + \\
&  \quad+ \left[ \left( 2 a \mp u_x n_x \mp u_n \right) \partial_x + \left( \mp n_x u_y             \right) \partial_y \right] m_x  + \\
&  \quad+ \left[ \left( \mp n_x u_y             \right) \partial_x + \left( 2 a \mp u_y n_y \mp u_n \right) \partial_y \right] m_y  = \\
\end{aligned}$$

**Remarks.** It can be proved that $d m_x = ( u \mp a n_x ) d \rho$, and $d m_y = ( v \mp a n_y ) d \rho$.

```{dropdown}
:open:

$$\begin{aligned}
  ( u_x \mp a n_x ) ( \mp a^2 n_x \pm u_n u_x) 
  & = \mp a^2 n_x u_x \pm u_x^2 u_n + a^3 n_x^2 - a u_n u_x n_x \\
\end{aligned}$$

$$\begin{aligned}
  ( u_x \mp a n_x ) ( 2a \mp u_x n_x \mp u_n ) 
  & = 2 a u_x \mp u_x^2 n_x \mp u_x u_n \mp 2 a^2 n_x + a u_x n_x^2 + a n_x u_n = \\
  & = 2 a u_x \mp u_x^2 n_x - u_x a \mp 2 a^2 n_x + a u_x n_x^2 \pm a^2 n_x = \\
  & = a u_x \mp a^2 n_x \mp u_x^2 n_x + a u_x n_x^2 = \\
\end{aligned}$$

```


```{dropdown} Comparing directional derivative of $\ \rho \ $ and $ \ m_x \ $

$$\begin{aligned}
 & ( \mp a^2 n_x \pm u_n u_x ) ( \mp n_x u_y ) = ? = ( \mp a^2 n_y \pm u_n u_y ) ( 2 a \mp u_x n_x \mp u_n ) \\
 0 & \ ? = a^2 n_x^2 u_y - u_n u_x n_x u_y \pm 2 a^3 n_y - a^2 u_x n_x n_y - a^2 u_n n_y \mp 2a u_n u_y + u_n u_x u_y n_x + u_n^2 u_y \\
 0 & \ ? = a^2 n_x^2 u_y \pm 2 a^3 n_y - a^2 u_x n_x n_y - a^2 u_n n_y \mp 2a u_n u_y + u_n^2 u_y \\
 0 & \ ? = a^2 u_y - a^2 n_y^2 u_y \pm 2 a^3 n_y - a^2 u_x n_x n_y - a^2 u_n n_y \mp 2a u_n u_y + u_n^2 u_y \\
\end{aligned}$$

and if $u_n = \pm a$,

$$\begin{aligned}
 0 & \ ? = a^2 u_y - a^2 n_y^2 u_y \pm 2 a^3 n_y - a^2 u_x n_x n_y - a^2 u_n n_y \mp 2a u_n u_y + u_n^2 u_y \\
 0 & \ ? = a^2 u_y - a^2 n_y^2 u_y \pm 2 a^3 n_y - a^2 u_x n_x n_y \mp a^3 n_y - 2a^2 u_y + a^2 u_y \\
 0 & \ ? =         - a^2 n_y ( n_y u_y + n_x u_x) \pm 2 a^3 n_y \mp a^3 n_y                      \\
 0 & \ ? =        \mp a^3 n_y                     \pm 2 a^3 n_y \mp a^3 n_y  = 0 \ .
\end{aligned}$$

```


<!--
$$\begin{aligned}
& = \dots \partial_t \dots \mp a^2 \partial_n \rho \pm u_n u \partial_u \rho +2 a \partial_x m_x \mp n_x u \partial_u m_x \mp u_n \partial_x m_x + 2 a \partial_y m_y \mp n_y u \partial_u m_y \mp u_n \partial_y m_y = \\
& = \dots \partial_t \dots \mp a^2 \partial_n \rho + a u \partial_u \rho \mp n_x u \partial_u m_x - a \partial_x m_x \mp n_y u \partial_u m_y - a \partial_y m_y + 2 a \partial_x m_x + 2 a \partial_y m_y = \\
& = \dots \partial_t \dots \mp a^2 \partial_n \rho + a u \partial_u \rho \mp \rho n_x u \partial_u u_x \mp n_x u_x u \partial_u \rho - a \partial_x m_x \mp \rho n_y \partial_u u_y \mp u_y n_y \partial_u \rho - a \partial_y m_y + 2 a \partial_x m_x + 2 a \partial_y m_y = \\
& = \dots \partial_t \dots \mp a^2 \partial_n \rho + a u \partial_u \rho \mp \rho n_x u \partial_u u_x \mp u_n u \partial_u \rho - a \partial_x m_x \mp \rho n_y u \partial_u u_y - a \partial_y m_y + 2 a \partial_x m_x + 2 a \partial_y m_y = \\
& = \dots \partial_t \dots \mp a^2 \partial_n \rho \mp \rho n_x u \partial_u u_x \mp \rho n_y u \partial_u u_y + a \partial_x m_x + a \partial_y m_y = \\
\end{aligned}$$
-->
...

For $s_2 = u_n$, $u_n = 0$ to get $s_2 = 0$, and thus the corresponding left eigenvector reads

$$\mathbf{l}_{0;2}^T = \frac{1}{\rho a} \left[ - \mathbf{t}^T \mathbf{u} \ | \ \mathbf{t}^T \right] \ ,$$

with $\mathbf{t} = \begin{bmatrix} n_y \\ - n_x \end{bmatrix}$, so that $\mathbf{t}^T \mathbf{n} = 0$. The quasi linear form of the equations becomes

$$\begin{aligned}
0 
& = \frac{1}{\rho a} \left[ \ - \mathbf{t}^T \mathbf{u} \ | \ \mathbf{t}^T \ \right] \left( 
\partial_t \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} +
\begin{bmatrix}
  \cdot & 1     & \cdot \\
  a^2 - \frac{m_x m_x}{\rho^2} & \frac{2 m_x}{\rho} & \cdot \\
      - \frac{m_x m_y}{\rho^2} & \frac{m_y}{\rho} & \frac{m_x}{\rho} \\
\end{bmatrix} \partial_x \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} +
\begin{bmatrix}
  \cdot & \cdot & 1     \\
  - \frac{m_x m_y}{\rho^2} & \frac{m_y}{\rho} & \frac{m_x}{\rho} \\
  a^2 - \frac{m_y m_y}{\rho^2} & \cdot & \frac{2 m_y}{\rho} \\
\end{bmatrix} \partial_y \begin{bmatrix} \rho \\ m_x \\ m_y \end{bmatrix} = \mathbf{0}
\right) = \\
0
& = [ \ - \mathbf{t}^T \mathbf{u} \ | \ \mathbf{t}^T \ ] \partial_t \begin{bmatrix} \rho \\ \mathbf{m} \end{bmatrix} + \\
& \quad  + [ \ t_x a^2 - \mathbf{t}^T \mathbf{u} u_x \ | \ - \mathbf{t}^T \mathbf{u} + t_x u_x + \mathbf{t}^T \mathbf{u} \ | \ t_y u_x \ ] \partial_x \begin{bmatrix} \rho \\ \mathbf{m} \end{bmatrix} + \\
& \quad  + [ \ t_y a^2 - \mathbf{t}^T \mathbf{u} u_y \ | \ t_x u_y \ | \ - \mathbf{t}^T \mathbf{u} + t_y u_y + \mathbf{t}^T \mathbf{u} \ ] \partial_y \begin{bmatrix} \rho \\ \mathbf{m} \end{bmatrix} = \\
0
& = [ \ - \mathbf{t}^T \mathbf{u} \ | \ \mathbf{t}^T \ ] \partial_t \begin{bmatrix} \rho \\ \mathbf{m} \end{bmatrix} + \\
& \quad +  a^2 \left( t_x \partial_x + t_y \partial_y \right) \rho - u_t \left( u_x \partial_x + u_y \partial_y \right) \rho + t_x \left( u_x \partial_x + u_y \partial_y \right) m_x + t_y \left( u_x \partial_x + u_y \partial_y \right) m_y = \\
& = 
\end{aligned}$$

or choosing $\hat{\mathbf{t}} = \hat{\mathbf{u}}$, s.t. $\mathbf{u} = u \hat{\mathbf{t}}$,

$$\begin{aligned}
0 
& = \dots \partial_t \dots + a^2 \partial_u \rho - u^2 \partial_u \rho + u t_x \partial_u m_x + u t_y \partial_u m_y = \\
& = \dots \partial_t \dots + a^2 \partial_u \rho - u^2 \partial_u \rho + \rho \underbrace{u t_x}_{u_x} \partial_u u_x + \rho \underbrace{u t_y}_{u_y} \partial_u u_y + \underbrace{ u u_x t_x \partial_u \rho + u u_y t_y \partial_u \rho}_{ = u^2 \partial_u \rho} = \\
& = \dots \partial_t \dots + a^2 \, \partial_u \rho + \rho \partial_u \frac{|\mathbf{u}|^2}{2} \ .
\end{aligned}$$

In **steady conditions**, dividing by $\rho \ne 0$

$$0 = a^2 \, \frac{\partial_u \rho}{\rho} + \partial_u \frac{u^2}{2} = \partial_u \left( a^2 \ln \rho + \frac{u^2}{2} \right) \ .$$

This is the isothermal version of the Bernoulli's theorem along a streamline for compressible flows, in absence of volume force. This can be derived from momentum equation in steady conditions, after scalar multiplication by the velocity field

$$\begin{aligned}
  0 
  & = \mathbf{u} \cdot \left[ \rho \mathbf{u} \cdot \nabla \mathbf{u} + \nabla p \right] = \\
  & = \mathbf{u} \cdot \left[ \rho \nabla \frac{|\mathbf{u}|^2}{2} + \boldsymbol\omega \times \mathbf{u} + \nabla p \right] = \\
  & = \rho \mathbf{u} \cdot \left[ \nabla \frac{|\mathbf{u}|^2}{2} + a^2 \frac{\nabla \rho}{\rho} \right] = \\
  & = \rho \mathbf{u} \cdot \nabla \left( \frac{|\mathbf{u}|^2}{2} + a^2 \ln \rho  \right) \ .
\end{aligned}$$

#### Euler equations for inviscid compressible flows


#### Shallow water


