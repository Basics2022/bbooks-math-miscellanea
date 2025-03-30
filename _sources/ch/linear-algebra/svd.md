(math:svd)=
# Singular Value Decomposition

Singular value decomposition of a matrix $\mathbf{A} \in \mathbb{C}^{m,n}$

$$\mathbf{A}_{(m,n)} = \text{(SVD)} = \mathbf{U}_{(m,m)} \mathbf{S}_{(m,n)} \mathbf{V}^*_{(n,n)}$$

with $\mathbf{U}^* \mathbf{U} = \mathbf{I}_{(m,m)}$, and $\mathbf{V}^* \mathbf{V} = \mathbf{I}_{(n,n)}$, $\mathbf{S} = \text{diag}\{ \sigma_i \}$, $\sigma_i \ge 0$. 

Exploiting the definition of matrix product, the SVD of matrix A can be written as

$$\mathbf{A} = \sum_{i = \min(m,n)} \sigma_i \mathbf{u}_i \mathbf{v}^*_i \ ,$$

see also economic decomposition below.


(math:svd:properties)=
## Properties

**Relation with [range](math:linear-algebra:matrix:subspaces:range) and [kernel](math:linear-algebra:matrix:subspaces:null) the matrix.**

$$\begin{aligned}
  \text{R}(\mathbf{A})   & = \{ \mathbf{u}_i | \sigma_i > 0 \} \\
  \text{K}(\mathbf{A})   & = \{ \mathbf{v}_i | \sigma_i = 0 \} \\
  \text{R}(\mathbf{A}^*) & = \{ \mathbf{v}_i | \sigma_i > 0 \} \\
  \text{K}(\mathbf{A}^*) & = \{ \mathbf{u}_i | \sigma_i = 0\} \\
\end{aligned}$$

It's immediate to prove [$\text{R}(\mathbf{A}) \perp \text{K}(\mathbf{A^*})$](math:linear-algebra:thms:RAperpKAh).

**Full or economic decomposition.** In general the $\mathbf{S}$ of the full decompsition in not square. 

$$\mathbf{A} = \text{(SVD)} = \mathbf{U}_{(m,m)} \mathbf{S}_{(m,n)} \mathbf{V}^*_{(n,n)} = \mathbf{U}^e_{(m,k)} \mathbf{S}^e_{(k,k)} \mathbf{V}^{e *}_{(k,n)} \ ,$$

with $k = \min(m,n)$.

(math:svd:applications)=
## Applications

### Solution of under-determined linear systems

### Norms and optimization
If $L^2$-norm is used for vector norms, see {prf:ref}`svd-optimization-norm`

$$\text{Find } \max_{||\mathbf{x}||=1} ||\mathbf{A} \mathbf{x}||^2$$

$$\mathbf{x}^* \mathbf{A}^* \mathbf{A} \mathbf{x} = \mathbf{x}^* \mathbf{V} \mathbf{S}^* \underbrace{\mathbf{U}^* \mathbf{U}}_{\mathbf{I}} \mathbf{S} \underbrace{\mathbf{V}^* \mathbf{x}}_{\mathbf{z}}$$

and $\mathbf{z} = \mathbf{V}^* \mathbf{x}$ is unitary as well (since $1= \mathbf{x}^* \mathbf{x} = \mathbf{z}^* \mathbf{V}^* \mathbf{V} \mathbf{z} = \mathbf{z}^* \mathbf{z} $).

After defining $\mathbf{S}_2 := \mathbf{S}^* \mathbf{S}$, the problem thus becomes

$$\text{Find} \max_{||\mathbf{z}|| = 1} \mathbf{z}^* \mathbf{S}_2 \mathbf{z}$$

Manipulating the objective function as $\sum_{i} \sigma_i^2 |z_i|^2 $, the constraint optimization problem has global maximum $\sigma_1^2$ (sorted singular values from the largest to the smalles) when $\mathbf{z}_1 = (1,0,0,\dots,0)^T$. Going back to the original variable, optimal condition
- is achieved for $\mathbf{x}_1 = \mathbf{v}_1$;
- has value $\max_{||\mathbf{x}||=1}||\mathbf{A}\mathbf{x}|| = \sigma_1^2$
- and the response of the system is $\mathbf{y}_1 = \sigma_1 \mathbf{u}_1$ as

  $$\begin{aligned}
    \mathbf{y}_1
    := \mathbf{A} \mathbf{x}_1 
    = \mathbf{U} \mathbf{S} \mathbf{V}^* \mathbf{v}_1 
    = \sum_{k} \left( \sigma_k \mathbf{u}_k \mathbf{v}_k^* \right) \mathbf{v}_1 
    = \sigma_1 \mathbf{u}_1 \ .
  \end{aligned}$$

```{prf:example} Other norms - variations of the $L^2$-norm
:label: svd-optimization-norm

This kind of problem may results as the discrete counterpart of a continuous problem, as an example from [finite element methods](pde:fem), where $\mathbf{x}$, $\mathbf{y}$ contain the coefficients of the basis functions. In this case, the discrete counterpart of the continous norm-measure of the continuous fields may involve a "mass matrix" (symmetric, definite positive - and thus with Choloeski factorization...),

$$\begin{aligned}
  \int_{\Omega_x} |x(\vec{r})|^2 d \vec{r} & \simeq \mathbf{x}^* \mathbf{M}_x \mathbf{x} \\
  \int_{\Omega_y} |y(\vec{r})|^2 d \vec{r} & \simeq \mathbf{y}^* \mathbf{M}_y \mathbf{y}
\end{aligned}$$

Continuous and discrete optimization problems are


$$\text{Find } \max_{|x(\vec{r})|_{L^2(\Omega_x)}=1} |y|^2_{L^2(\Omega_y)} $$

$$\text{Find } \max_{\mathbf{x}^*\mathbf{M}_x  \mathbf{x}=1} \mathbf{x}^* \mathbf{A}^* \mathbf{M}_y \mathbf{A} \mathbf{x} $$

with the relation $\mathbf{y} = \mathbf{A} \mathbf{x}$ between the discrete input and output.

This problem can be easily (and efficiently?) recast to the standard form of the problem, using [Cholesky decomposition](math:matrix-factorization) of matrix $\mathbf{M}_x = \mathbf{L}_x \mathbf{L}_x^*$, with the definition of the variable $\mathbf{z} = \mathbf{L}_x^* \mathbf{x}$

$$\text{Find } \max_{||\mathbf{z}||=1} \mathbf{z}^* \mathbf{L}_x^{-1} \mathbf{A}^* \mathbf{L}_y \mathbf{L}_y^* \mathbf{A} \mathbf{L}_x^{-*} \mathbf{z} $$

This problem can be efficiently solved with iterative algorithms to compute the SVD of the matrix $\widetilde{\mathbf{A}} := \mathbf{L}_y^* \mathbf{A} \mathbf{L}_x^{-*}$, that doesn't need the expensive full inversion of a matrix but only its action on a vector (instead of evaluating the inverse, a linear system - here triangular! Easier to solve - can be efficiently solved). Algorithms like **Arnoldi algorithm** evaluates the largest eigenvalues or singular values(if no options to set other goals) and the corresponding eigenvectors and singular vectors, alternating **power iterations** and **orthogonalization**. Here power iteration to evaluate the action of the matrix $\widetilde{\mathbf{A}} = \mathbf{L}_y^* \mathbf{A}\mathbf{L}_x^{-*}$ on a generic vector $\mathbf{z}$ is made of the following steps:
 1. solution of the linear system $\mathbf{L}^*_x \mathbf{a} = \mathbf{z}$ $\rightarrow \ \mathbf{a} = \dots$
 2. matrix-vector multiplication $\mathbf{b} = \mathbf{A} \mathbf{a}$
 3. matrix-vector multiplication $\mathbf{c} = \mathbf{L}^*_y \mathbf{b}$

Once the SVD is solved, with $\mathbf{z}_1 = \mathbf{v}_1$

$$\begin{aligned}
  \mathbf{x}_1 & = \mathbf{L}_x^{-*} \mathbf{v}_1 \\
  \mathbf{y}_1 & = \mathbf{A} \mathbf{x}_1 = \sigma_1 \mathbf{L}_y^{-*} \mathbf{u}_1 \\
\end{aligned}$$




```
