(differential-geometry:surfaces)=
# Surfaces

A surface $S$ is a geometric entity that has a 2-parameter parametric representation. Its points in 3-dimensional (Euclidean) space $E^3$ can be represented with the function

$$S: \, \mathbf{r}(q^1, q^2) \ .$$

(differential-geometry:surfaces:differential)=
## Differential

The differential $d \mathbf{r}$ represents an elementary vector on - tangent to - the surface. From the very definition of the differential of a function, it follows

$$d \mathbf{r} =
  \frac{\partial \mathbf{r}}{\partial q^1} \, d q^1 + \frac{\partial \mathbf{r}}{\partial q^2} \, d q^2 =
  \mathbf{b}_1 \, d q^1 + \mathbf{b}_2 \, d q^2
$$

(differential-geometry:surfaces:differential:first-fundamental-form)=
### Length of the elementary vector on the surface, and the first fundamental form $\mathbf{I}$

$$\begin{aligned}
  \left| d \mathbf{r} \right|^2 = d \mathbf{r} \cdot d \mathbf{r} & = g_{ij} dq^{i} dq^{j} = \\
  & = E \left( dq^1 \right)^2 + 2 F dq^1 dq^2 + G \left( dq^2 \right)^2 = \\
  & = \begin{bmatrix} dq^1 & dq^2 \end{bmatrix} \begin{bmatrix} E & F \\ F & G \end{bmatrix} \begin{bmatrix} dq^1 \\ dq^2 \end{bmatrix} = \\
  & = d \mathbf{q}^T \, \mathbf{I} \, \mathbf{q}
\end{aligned}$$

Here with slight abuse of notation, both geometrical vectors $d \mathbf{r}$ and mathematical vectors - whose components are not transforming as vectors under change of coordinates - collecting the coordinates $d \mathbf{q}$ have been represented with bold symbols.

The elements of the **first fundamental form** are the covariant components $g_{ij}$ of the **metric tensor**,

$$\left[ \mathbf{I} \right]_{ij} = g_{ij} \ .$$ (eq:surface:first-fundamental-form)

(differential-geometry:surfaces:normal-vector)=
## Normal vector

The vectors $\mathbf{b}_1$, $\mathbf{b}_2$ are tangent to the surface $S$. A **regular parametrization** has $\mathbf{b}_1 \times \mathbf{b}_2 \ne \mathbf{0}$ everywhere. A third vector $\mathbf{b}_3 := \hat{\mathbf{n}}$ can be defined so that $|\hat{\mathbf{n}}| = 1$ and $\hat{\mathbf{n}} \cdot \mathbf{b}_{i} = 0$, $i=1:2$. This is a **unit normal vector** to the surface. If the parametrization is regular, then the set of vectors $\{ \mathbf{b}_1, \mathbf{b}_2, \hat{\mathbf{n}} \}$ forms a local(natural)  basis of 3-dimensional vectors space.

The components of the metric tensor are

$$\left[ g_{ab} \right] = \begin{bmatrix} g_{11} & g_{12} & \cdot \\ g_{21} & g_{22} & \cdot \\ \cdot & \cdot & 1 \end{bmatrix} \ ,$$

so that the vectors of the reciprocal basis, $\mathbf{b}^a = g^{ab} \mathbf{b}_b$, read

$$\left\{\begin{aligned}
  \mathbf{b}^1 & = g^{11} \mathbf{b}_1 + g^{12}  \mathbf{b}_2 \\
  \mathbf{b}^2 & = g^{21} \mathbf{b}_1 + g^{22}  \mathbf{b}_2 \\
  \mathbf{b}^3 & = \hat{\mathbf{n}} \ .
\end{aligned} \right.$$

(differential-geometry:surfaces:derivative-of-the-natural-basis)=
## Derivatives of the natural basis

For $i, \, j \in \{ 1, 2 \}$, using the vector $\mathbf{b}_3 = \hat{\mathbf{n}}$, the second-order derivatives of the position on the manifold w.r.t. the coordinates read

$$\frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} = \frac{\partial \mathbf{b}_i}{\partial q^j} = \Gamma_{ij}^{\alpha} \mathbf{b}_{\alpha} = \Gamma_{ij}^1 \mathbf{b}_1 + \Gamma_{ij}^2 \mathbf{b}_2 + \Gamma_{ij}^3 \mathbf{b}_3 \ .$$

Exploiting the orthogonality of the natural basis and its reciprocal, it follows

$$\Gamma_{ij}^{k} = \mathbf{b}^k \cdot \frac{\partial \mathbf{b}_i}{\partial q^j} \ .$$

**Remark.** Comparing two different choices of the orthogonal coordinate $q^3$, (1) unit normal vector $\hat{\mathbf{b}}_3 = \hat{\mathbf{n}}$, (2) non-unitary normal vector $\hat{\mathbf{b}}_3 = \mathbf{n}$, $\hat{\mathbf{b}}^3 = \tfrac{\mathbf{n}}{|\mathbf{n}|^2}$, it's easy to prove that the Christoffel coefficients with upper index $k = 3$, $\Gamma^{3}_{ij}$, are independent from this choice.


(differential-geometry:surfaces:normal-vector-derivatives)=
## Derivatives of the unit normal vector

See {eq}`eq:surface:weingarten`.

$$\partial_k \hat{\mathbf{n}} = - \Gamma_{ik}^{3} \mathbf{b}^i = - g^{il} \Gamma_{ik}^{3} \mathbf{b}_l \ .$$

(differential-geometry:surfaces:geometric-entities)=
## Geometric entities

**Normal vector.** 

$$\mathbf{n}(q^1, q^2) = \frac{\partial \mathbf{r}}{\partial q^1}(q^1, q^2) \times \frac{\partial \mathbf{r}}{\partial q^2}(q^1, q^2) = \mathbf{b}_1(q^1, q^2) \times \mathbf{b}_2(q^1, q^2)$$

**First-order approximation and the tangent plane.**  The equation of the points of the tangent plane $\pi$ in point $\mathbf{r}\left(q^1, q^2 \right)$ follows the orthogonality condition

$$\pi: \, (\mathbf{r} - \mathbf{r}(q^1, q^2)) \cdot \mathbf{n}(q^1, q^2) = 0 \ .$$

**Length of elementary segment on the plane.**

$$\begin{aligned}
|d \mathbf{r}|^2 
  & = d \mathbf{r} \cdot d \mathbf{r} = \\
  & = \left( \mathbf{b}_1 \, d q^1 + \mathbf{b}_2 \, d q^2 \right) \cdot \left( \mathbf{b}_1 \, d q^1 + \mathbf{b}_2 \, d q^2 \right) = \\
  & = g_{11} \, dq^1 \, dq^1 + g_{12} \, dq^1 \, dq^2 + g_{21} \, dq^2 \, dq^1 + g_{22} \, dq^2 \, d q^2 = g_{ij} \, dq^i \, dq^j  
\end{aligned}$$

**Second order approximation and the curvature tensor.**

$$\begin{aligned}
  \mathbf{r}(q^1 + d q^1, q^2 + d q^2) 
  & = \mathbf{r}(q_1, q_2) + \frac{\partial \mathbf{r}}{\partial q^i} \, dq^i + \frac{1}{2} \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \, dq^i dq^j + o\left(|d q^i|^2\right) = \\
  & = \mathbf{r}(q_1, q_2) + \mathbf{b}_{i} \, dq^i + \frac{1}{2} \mathbf{b}_k \Gamma^{k}_{ij} \, dq^i \, dq^j + \frac{1}{2} \hat{\mathbf{n}} \, \Gamma^{3}_{ij} \, dq^i dq^j  + o\left(|d q^i|^2\right) \ , 
\end{aligned}$$

so that

$$\begin{aligned}
\left[ \mathbf{r}(q^1 + d q^1, q^2 + d q^2) - \mathbf{r}(q^1, q^2) \right] \cdot \hat{\mathbf{n}}
 & = \frac{1}{2} \Gamma^3_{ij} \, d q^i \, dq^j = \\
 & = \frac{1}{2} \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \, d q^i \, dq^j = \\
 & = \frac{1}{2} \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \, \mathbf{b}^i \cdot \mathbf{b}_k d q^k \, \mathbf{b}^j \cdot \mathbf{b}_l dq^l = \\
 & = \frac{1}{2} \underbrace{d q^k \mathbf{b}_k}_{d \mathbf{r}} \cdot \left[ \left( \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \right) \mathbf{b}^i \otimes \mathbf{b}^j \right] \cdot \underbrace{d q^l \mathbf{b}_l}_{d\mathbf{r}} = \\
 & = \frac{1}{2} d \mathbf{r} \cdot \mathbb{b} \cdot d \mathbf{r} \ ,
\end{aligned}$$

having defined the **curvature tensor** $\mathbb{b}$,

$$\mathbb{b} = b_{ij} \mathbf{b}^i \otimes \mathbf{b}^j = \left( \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \right) \mathbf{b}^i \otimes \mathbf{b}^j = \Gamma^{3}_{ij} dq^i dq^j \ .$$ (eq:surface:curvature-tensor)

(differential-geometry:surfaces:geometric-entities:curvature-tensor)=
### Curvature tensor, quadratic approximation and second fundamental form

From the second-order Taylor expansion around a point $\mathbf{r}(q^1, q^2)$, the projection of the displacement onto the unit normal vector $\hat{\mathbf{n}}$ measures the distance from the surface to its tangent plane $\pi$:

$$[\mathbf{r}(q^1 + dq^1, q^2 + dq^2) - \mathbf{r}(q^1, q^2)] \cdot \hat{\mathbf{n}} = \Gamma_{ij}^3 dq^i dq^j ,$$

The symmetric covariant tensor of rank 2, defined by its components

$$\left[ \mathbf{II} \right]_{ij} = b_{ij} := \Gamma_{ij}^3 = \hat{\mathbf{n}} \cdot \mathbf{b}_{\alpha} \Gamma_{ij}^{\alpha} = \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} = \hat{\mathbf{n}} \cdot \frac{\partial \mathbf{b}_i}{\partial q^j} = -\frac{\partial \hat{\mathbf{n}}}{\partial q^j} \cdot \mathbf{b}_i ,$$ (eq:second-fundamental-form:normal-projection)

is the **second fundamental form** (or curvature tensor) of the surface embedded in $E^3$. The last equality holds from the derivatives w.r.t. $q^j$ of the relation $\hat{\mathbf{n}} \cdot \mathbf{b}_i = 0$.

The quadratic form $b_{ij} dq^i dq^j$ characterizes the local deviation of the surface from the tangent plane $\pi$. Let $w_n(q^1,q^2) = d \mathbf{r} \cdot \mathbb{b} \cdot d \mathbf{r}$ the normal deviation of the surface w.r.t. the tangent plane, then

$$w_n(q^1,q^2) = \frac{1}{2} b_{ij} dq^{i} dq^{j} \ .$$

The curvature tensor $\mathbb{b}$ is a **symmetric** order-2 tensor, locally built on a 2-dimensional vector space. In analogy - anyway pay attention that tensors are not matrices - with [spectral decomposition of symmetric matrices](math:spectral:symmetric), its **spectral decomposition** is 

$$\mathbb{b} = \kappa_1 \mathbf{v}_1 \otimes \mathbf{v}_1 + \kappa_2 \mathbf{v}_2 \otimes \mathbf{v}_2 \ ,$$

being $\kappa_1$, $\kappa_2 \in \mathbb{R}$ the **real eigenvalues**, and $\mathbf{v}_1$, $\mathbf{v}_2$ the unit **orthogonal** basis defined by the **eigenvectors** of the eigenvalue problem

$$\mathbb{b} \cdot \mathbf{v}_i = \kappa_i \mathbf{v}_i \ , \qquad i \in \{ 1, 2 \} \ .$$

The eigenvectors $\mathbf{v}_{1,2}$ defines the **principal directions**, while the eigenvalues $\kappa_{1,2}$ are defined as the **principal curvatures**.

````{dropdown} Eigenvalue problem
:open:

The eigenvalues of the tensor $\mathbb{b}$ are the same eigenvalues as the matrix containing its mixed components $[b^{i}_{\ \ j}]$. This immediately follows as the $m^{\rm th}$ contravariant component of the eigenvalue problem

$$\mathbb{b} \cdot \mathbf{v}_{(\alpha)} = \kappa_{(\alpha)} \mathbf{v}_{(\alpha)} \ ,$$

is

$$b^{m}_{\ \ j} v^{j}_{(\alpha)} = \kappa_{(\alpha)} v^{m}_{(\alpha)} \ .$$

```{dropdown} Proof

$$\begin{aligned}
  \mathbb{b} \cdot \mathbf{v}_{(\alpha)} & = \kappa_{(\alpha)} \mathbf{v}_{(\alpha)} \\
  \left( b_{ij} \mathbf{b}^i \otimes \mathbf{b}^j \right) \cdot \left( v^l_{(\alpha)} \mathbf{b}_l \right) & = \kappa_{(\alpha)} v^m_{(\alpha)} \mathbf{b}_m \\
  b_{ij} v^j_{(\alpha)} \mathbf{b}^i & = \kappa_{(\alpha)} v^m_{(\alpha)} \mathbf{b}_m \\
  g^{im} b_{ij} v^j_{(\alpha)} \mathbf{b}_m & = \kappa_{(\alpha)} v^m_{(\alpha)} \mathbf{b}_m \\
  b^{m}_{\ \ j} v^j_{(\alpha)} \mathbf{b}_m & = \kappa_{(\alpha)} v^m_{(\alpha)} \mathbf{b}_m \\
\end{aligned}$$

i.e. in components $b^{m}_{\ \ j} v^{j}_{(\alpha)} = \kappa_{(\alpha)} v^m_{(\alpha)}$, or

$$\left( b^{m}_{\ \ j} - \kappa_{(\alpha)} \delta^{m}_{\ \ j}  \right) v^{j}_{(\alpha)} = 0 \ .$$

```

Even more explicitly, the condition $\text{det}\left( b^{m}_{\ \ j} - \kappa_{(\alpha)} \delta^{m}_{\ \ j} \right) = 0$ becomes

$$0 = \left| \begin{bmatrix} b^{1}_{\ \ 1} - \kappa_{(\alpha)} & b^{1}_{\ \ 2} \\ b^{2}_{\ \ 1} & b^{2}_{\ \ 2} - \kappa_{(\alpha)} \end{bmatrix} \right| = \kappa_{(\alpha)}^2 - \left( b^{1}_{\ \ 1} + b^{2}_{\ \ 2} \right) \kappa_{(\alpha)} + b^1_{\ \ 1} b^{2}_{\ \ 2} - b^{1}_{\ \ 2} b^{2}_{\ \ 1} = \kappa^2_{(\alpha)} - \text{tr}\{ \mathbf{B} \} \kappa_{(\alpha)} + \text{det}\{ \mathbf{B} \}\  .$$

The eigenvalues are

$$\begin{aligned}
  \kappa_{(\alpha)} 
  & = \frac{ \text{tr}\left\{ \mathbf{B} \right\} }{2} \mp \sqrt{ \left( \frac{ \text{tr}\left\{ \mathbf{B} \right\} }{2} \right)^2 - \text{det}\{ \mathbf{B} \} } \ .
\end{aligned}$$

with $\mathbf{B}$ the matrix collecting the mixed components of the curvature tensor, $[\mathbf{B}]_{ij} = \left[ b^{i}_{\ \ j} \right]$. For a 2-dimensional matrix, it's easy to prove the general relations between its trace, determinant and eigenvalues,

$$\begin{aligned}
  \text{tr }\{ \mathbf{B} \} & = \kappa_{1} + \kappa_2 \\
  \text{det}\{ \mathbf{B} \} & = \kappa_{1} \cdot \kappa_2 \ .
\end{aligned}$$


<!--
**Remark.** Eigenvalues are real, as
... **todo** *check and uncomment*

$$\begin{aligned}
  \left( \frac{\text{tr}\{ \mathbf{B} \}}{2} \right)^2 - \text{det}\{ \mathbf{B} \} 
  & = \frac{\left( b^{1}_{\ \ 1} \right)^2 + 2 b^{1}_{\ \ 1} b^{2}_{\ \ 2} + \left( b^{2}_{\ \ 2} \right)^2 }{4} - \left( b^{1}_{\ \ 1} b^{2}_{\ \ 2} - b^{1}_{\ \ 2} b^{2}_{\ \ 1} \right) = \\
  & = \frac{\left( b^{1}_{\ \ 1} \right)^2 - 2 b^{1}_{\ \ 1} b^{2}_{\ \ 2} + \left( b^{2}_{\ \ 2} \right)^2 }{4} + b^{1}_{\ \ 2} b^{2}_{\ \ 1} = \\
  & = \frac{\left( b^{1}_{\ \ 1} - b^{2}_{\ \ 2} \right)^2 }{4} + g^{1 k} b_{k 2} g^{l 2} b_{l 1} = \\
\end{aligned}$$

with

$$b^{1}_{\ \ 2} = g^{1k} b_{k2} = g^{k1} b_{2k} = b$$
-->

````

```{dropdown} Spectral decomposition of symmetric matrices

Let $\mathbf{A}$ be real-valued symmetric, i.e. $\mathbf{A} = \mathbf{A}^T$, $A_{ij} \in \mathbb{R}$. Let $\{ \lambda_i \}_i$, $\{ \mathbf{v}_i \}_i$ the sets of eigenvalues and corresponding eigenvectors. Taking two different eigenvalues

$$\begin{aligned}
  \mathbf{A} \mathbf{v}_i & = \lambda_i \mathbf{v}_i \\
  \mathbf{A} \mathbf{v}_k & = \lambda_k \mathbf{v}_k \ .
\end{aligned}$$

Taking the product on the left of the first equation with $\mathbf{v}_k^T$, and of the second equation with $\mathbf{v}_i^T$, and taking the difference of these two equations

$$0 = \left( \lambda_i - \lambda_k \right) \mathbf{v}_k^T \mathbf{v}_i \ .$$

This equation has solutions either if $\lambda_i = \lambda_k$, or - if $\lambda_i \ne \lambda_k$ - if $\mathbf{v}_k^T \mathbf{v}_i = 0$, i.e. if the eigenvectors with two different eigenvalues are orthogonal. Thus, the matrix $\mathbf{A}$ can be written as a linear combination

$$\mathbf{A} = \lambda_1 \mathbf{v}_1 \mathbf{v}_1^T + \lambda_2 \mathbf{v}_2 \mathbf{v}_2^T \ ,$$

with $\mathbf{v}_1$, and $\mathbf{v}_2$ orthogonal (even if the two eigenvalues of $\mathbf{A}$ have the same value, using $\mathbf{v}_1^T \mathbf{v}_2 = 0$ as an orthogonality condition of the vectors associated with the same eigenvalue with algebraic multiplicity greater than $1$). As a double-proof, the action of $\mathbf{A}$ on a generic vector $\mathbf{w} = w_1 \mathbf{v}_1 + w_2 \mathbf{w}_2$ is

$$\mathbf{A} \mathbf{w} = \mathbf{A} \left( w_1 \mathbf{v}_1 + w_2 \mathbf{v}_2 \right) = w_1 \lambda_1 \mathbf{v}_1 + w_2 \lambda_2 \mathbf{v}_2$$

or

$$\left( \lambda_1 \mathbf{v}_1 \mathbf{v}_1^T + \lambda_2 \mathbf{v}_2 \mathbf{v}_2^T \right) \mathbf{w} = \left(  \lambda_1 \mathbf{v}_1 \mathbf{v}_1^T + \lambda_2 \mathbf{v}_2 \mathbf{v}_2^T \right) \left( w_1 \mathbf{v}_1 + w_2 \mathbf{v}_2 \right) = w_1 \lambda_1 \mathbf{v}_1 + w_2 \lambda_2 \mathbf{v}_2 \ .$$

The **eigenvalues of a symmetric matrix** are **real**, since

$$\mathbf{v}_i^* \left( \mathbf{A} \mathbf{v}_i \right) = \mathbf{v}_i^* ( \lambda_i \mathbf{v}_i )$$

while the product of the adjoint and $\mathbf{v}_i$ - with $\mathbf{A}$

$$\mathbf{v}_i^* \mathbf{A} \mathbf{v}_i = \lambda_i^* \mathbf{v}_i^* \mathbf{v}_i \ .$$

The difference of the latter two equations gives

$$0 = ( \lambda_i - \lambda_i^* ) \mathbf{v}_i^* \mathbf{v}_i \quad \rightarrow \quad \lambda_i^* = \lambda_i \ ,$$

i.e. $\lambda_i \in \mathbb{R}$.

```

#### Mean curvature

```{dropdown} Mean curvature
:open:

The mean curvature is defined as the arithmetic average of the principal curvatures, $H := \frac{1}{2} \left( \kappa_1 + \kappa_2 \right)$.

$$\begin{aligned}
  H 
  & = \frac{1}{2} \left( \kappa_1 + \kappa_2 \right) = \\
  & =\frac{ \text{tr} \{ [ b^{i}_{\ \ j} ] \} }{2} = \frac{1}{2} b^{i}_{\ \ i} = \\
  & = \frac{1}{2} g^{ij} b_{ij} = \frac{1}{2} \left( g^{11} b_{11} + g^{12} b_{12} + g^{21} b_{21} + g^{22} b_{22} \right) = \\
  & = \frac{1}{2} [ g_{ij} ]^{-1} b_{ij} = \frac{1}{2 \left( g_{11} g_{22} - g_{12}^2 \right)} \left( g_{22} b_{11} - g_{12} b_{12} - g_{21} b_{21} + g_{11} b_{22} \right)
\end{aligned}$$

```

#### Gaussian curvature

```{dropdown} Gaussian curvature
:open:

Gaussian curvature is defined as the determinant of $b^{i}_{\ \ j}$,

$$K = \text{det} \{ b^{i}_{\ \ j} \} = \dfrac{\text{det}\{ b_{ij} \}}{\text{det}\{ g_{ij} \}} = \frac{\text{det}\{ \mathbf{II} \}}{\text{det}\{ \mathbf{I} \}} \ ,$$ (eq:differential-geometry:gaussian-curvature)

as $b_{ij} = g_{il} b^{l}_{\ \ j}$.


```


#### Principal curvatures

```{dropdown} Principal curvatures, as extreme values
:open:

Let the spectral decomposition of the symmetric tensor $\mathbb{b}$ be

$$\mathbb{b} = \kappa_1 \mathbf{v}_1 \otimes \mathbf{v}_1 + \kappa_2 \mathbf{v}_2 \otimes \mathbf{v}_2 \ ,$$

with $\mathbf{v}_i \cdot \mathbf{v}_j = \delta_{ij}$, and $\kappa_1 \ge \kappa_2$. Let $\hat{\mathbf{t}} = \cos \theta \mathbf{v}_1 + \sin \theta \mathbf{v}_2$ a unit-length vector a function of $\theta$, to investigate the local curvature of the surface as a function of $\theta$. Then the curvature of the surface in $\hat{\mathbf{t}}$-direction - see curvature of a line on a surface {eq}`eq:surface:line-on-surface:curvature` - is

$$\kappa(\theta) = \hat{\mathbf{t}} \cdot \mathbb{b} \cdot \hat{\mathbf{t}} = \kappa_1 \cos^2 \theta + \kappa_2 \sin^2 \theta \ .$$

Thus, it immediately follows that 

$$\begin{aligned}
  & \max_{\theta} \kappa(\theta) = \kappa\left(\theta=           0 \right) = \kappa\left(\theta=           \pi \right) = \kappa_1 \\
  & \min_{\theta} \kappa(\theta) = \kappa\left(\theta=\frac{\pi}{2}\right) = \kappa\left(\theta=\frac{3}{2}\pi \right) = \kappa_2 \\
\end{aligned}$$

```

```{dropdown} Curves on a surface
:open:

Let $\gamma$ be a curved defined on a surface $S: \mathbf{r}(q^1,q^2)$. Then the curve $\gamma$ can be represented in parametric form as $\mathbf{r}(q^1(s), q^2(s))$, using the arc-length parameter $s$.

The tangent vector to the curve $\gamma$ is

$$\hat{\mathbf{t}}(s) := \mathbf{r}'(s) = \dfrac{d q^i}{d s} \partial_{q^i} \mathbf{r} = \dfrac{d q^i}{d s} \mathbf{b}_i \ ,$$

summing over $i \in \{ 1, 2 \}$. The derivative of the  tangent vector is proportional to the normal vector, through the curvature, i.e. $\hat{\mathbf{t}}'(s) = \kappa(s) \hat{\mathbf{n}}(s)$,

$$\hat{\mathbf{t}}'(s) = \left[ \frac{d^2 q^i}{ds^2} + \Gamma_{jk}^{i} \frac{d q^{j}}{d s} \frac{d q^{k}}{d s} \right] \mathbf{b}_i + \Gamma^{3}_{jk} \dfrac{d q^j}{ds} \dfrac{d q^k}{ds} \hat{\mathbf{n}} \ .$$

The curvature of this curve thus reads

$$\begin{aligned}
  \kappa(s) 
  & = \hat{\mathbf{t}}'(s) \cdot \hat{\mathbf{n}} = \\
  & = \Gamma_{jk}^{3} \dfrac{dq^j}{ds} \dfrac{dq^k}{ds} = \\
  & = \left( \dfrac{dq^j}{ds} \mathbf{b}_j \right) \cdot \left( \Gamma_{ab}^{3} \mathbf{b}^{a} \mathbf{b}^b \right) \cdot \left( \dfrac{dq^k}{ds} \mathbf{b}_k \right) = \\
  & = \hat{\mathbf{t}}(s) \cdot \mathbb{b}(s) \cdot \hat{\mathbf{t}}(s) \ .
\end{aligned}$$ (eq:surface:line-on-surface:curvature)

```

<!--
```{dropdown} Principal curvatures and diagonalization
:open:

$$\mathbb{b} = b_{ij} \mathbf{b}^i \otimes \mathbf{b}^j = b_{i}^{\ \ j} \mathbf{b}^i \otimes \mathbf{b}_j = \kappa_{(i)} \delta_{ij} \mathbf{v}_i \otimes \mathbf{v}_j $$

```
-->

<!--

Using the metric tensor $g_{ij}$ (the *first fundamental form*), we can define the mixed curvature tensor $b^i_j = g^{ik} b_{kj}$ and compute the fundamental intrinsic scalar measures of curvature:

* **Mean Curvature ($H$):**

  $$H = \frac{1}{2} b^i_i = \frac{1}{2} g^{ij} b_{ij} = \frac{g_{22}b_{11} - 2g_{12}b_{12} + g_{11}b_{22}}{2(g_{11}g_{22} - g_{12}^2)}$$

* **Gaussian Curvature ($K$):**

  $$K = \det(b^i_j) = \frac{\det(b_{ij})}{\det(g_{ij})} = \frac{b_{11}b_{22} - b_{12}^2}{g_{11}g_{22} - g_{12}^2}$$

-->


<!--
(differential-geometry:surfaces:geometric-entities:curvature-tensor:principal)=
#### Principal Curvatures and Directions

The extreme values of the normal curvature $\kappa_n = \frac{b_{ij}dq^i dq^j}{g_{ij}dq^i dq^j}$ are the **principal curvatures** $\kappa_1$ and $\kappa_2$, which are the eigenvalues of the tensor $b^i_j$:

$$\det(b^i_j - \kappa \delta^i_j) = 0 \quad \implies \quad \kappa^2 - 2H\kappa + K = 0 .$$

Thus, the principal curvatures satisfy:

$$\kappa_{1,2} = H \pm \sqrt{H^2 - K} .$$

* The Gaussian curvature is the product of the principal curvatures: $K = \kappa_1 \kappa_2$.
* The Mean curvature is the average of the principal curvatures: $H = \frac{1}{2}(\kappa_1 + \kappa_2)$.

...
-->

(differential-geometry:surfaces:geometric-entities:fundamental-forms-and-egregium-thm)=
## Fundamental forms and Gauss egregium theorem

First and second fundamental forms arieses when dealing with vector quantities of a surface. Let $\mathbf{r}(u,v)$  be a parametrization of the surface, here $(q^1, q^2), (u, v)$. 

* The differential, i.e. an elementary vectors on the surface, contains the first derivative of the parametrization and reads $d \mathbf{r} = \mathbf{b}_i d q^i = \mathbf{r}_i d q^i = \mathbf{r}_u du + \mathbf{r}_v dv$, 

* the covariant components of the metric tensor reads $g_{ij} = \mathbf{b}_i \cdot \mathbf{b}_j$

* the **first fundamental form** appears in the legnth of an elementary vector on the surface,

  $$|d \mathbf{r}|^2 = d \mathbf{r} \cdot d \mathbf{r} = g_{uu} du^2 + 2 g_{uv} du dv + g_{vv} dv^2 = E du^2 + 2 F du dv + G dv^2 \ ,$$

  having introduced the common symbols $E$, $F$, $G$.

* the derivitves of the vectors of the natural basis induced by the parametrization, i.e. the second derivative of the manifold, are 

   $$\partial_{k} \mathbf{b}_i = \partial_{ki} \mathbf{r} =: \Gamma_{ik}^\alpha \mathbf{b}_\alpha \ ,$$

   with $i$, $k \in \{ 1 , 2 \}$, $\alpha \in \{ 1, 2, 3 \}$, and $\mathbf{b}_3 = \hat{\mathbf{n}}$.

* The derivatives of the elements of the first form w.r.t. the coordinates are - as $\hat{\mathbf{n}} \cdot \mathbf{r}_u = \hat{\mathbf{n}} \cdot \mathbf{r}_v = 0$,

   $$\begin{aligned}
     E_u & = 2 \mathbf{r}_{uu} \cdot \mathbf{r}_{u}                                        && = 2 \Gamma_{11}^{1} g_{11} + 2 \Gamma_{11}^2 g_{12} \\
     E_v & = 2 \mathbf{r}_{uv} \cdot \mathbf{r}_{u}                                        && = 2 \Gamma_{12}^{1} g_{11} + 2 \Gamma_{12}^2 g_{12} \\
     F_u & =   \mathbf{r}_{uu} \cdot \mathbf{r}_{v} + \mathbf{r}_{u} \cdot \mathbf{r}_{vu} && =   \Gamma_{11}^{1} g_{12} +   \Gamma_{11}^2 g_{22} +  \Gamma_{12}^{1} g_{11} +   \Gamma_{12}^2 g_{12} \\
     F_v & =   \mathbf{r}_{uv} \cdot \mathbf{r}_{v} + \mathbf{r}_{u} \cdot \mathbf{r}_{vv} && =   \Gamma_{12}^{1} g_{12} +   \Gamma_{12}^2 g_{22} +  \Gamma_{22}^{1} g_{11} +   \Gamma_{22}^2 g_{12} \\
     G_u & = 2 \mathbf{r}_{vu} \cdot \mathbf{r}_{v}                                        && = 2 \Gamma_{21}^{1} g_{12} + 2 \Gamma_{21}^2 g_{22} \\
     G_v & = 2 \mathbf{r}_{vv} \cdot \mathbf{r}_{v}                                        && = 2 \Gamma_{22}^{1} g_{12} + 2 \Gamma_{22}^2 g_{22} \\
   \end{aligned}$$

   and thus
   
   $$\begin{aligned}
     \mathbf{r}_{uu} \cdot \mathbf{r}_{u}  & = \Gamma_{11}^{1} g_{11} + \Gamma_{11}^2 g_{12} && = \frac{1}{2} E_u \\
     \mathbf{r}_{uu} \cdot \mathbf{r}_{v}  & = \Gamma_{11}^{1} g_{12} + \Gamma_{11}^2 g_{22} && = F_u - \frac{1}{2} E_v \\
     \mathbf{r}_{uv} \cdot \mathbf{r}_{u}  & = \Gamma_{12}^{1} g_{11} + \Gamma_{12}^2 g_{12} && = \frac{1}{2} E_v \\
     \mathbf{r}_{uv} \cdot \mathbf{r}_{v}  & = \Gamma_{21}^{1} g_{12} + \Gamma_{21}^2 g_{22} && = \frac{1}{2} G_u \\
     \mathbf{r}_{vv} \cdot \mathbf{r}_{u}  & = \Gamma_{22}^{1} g_{11} + \Gamma_{22}^2 g_{12}&& = F_v - \frac{1}{2} G_u \\
     \mathbf{r}_{vv} \cdot \mathbf{r}_{v}  & = \Gamma_{22}^{1} g_{12} + \Gamma_{22}^2 g_{22} && = \frac{1}{2} G_v \\
   \end{aligned}$$

   Each pair of equations can be written as

   $$\begin{bmatrix} E & F \\ F & G \end{bmatrix} \begin{bmatrix} \Gamma_{a b}^{1} \\ \Gamma_{a b}^{2} \end{bmatrix} = \begin{bmatrix} \dots \\ \dots \end{bmatrix} \ ,$$

   i.e., if the matrix is non-singular, i.e. if $\mathbf{r}_u \times \mathbf{r}_v \ne \mathbf{0}$, then Christoffel symbols can be written in terms of the coefficients of the first form and their derivatives.

* the **second fundamental form** appears in the second-order derivative of the manifold. With an extrinsic approach, with the 2-dimensional surface embedded in a 3-dimensional space,

   $$\partial_{k} \mathbf{b}_i = \partial_{ki} \mathbf{r} =: \Gamma_{ik}^\alpha \mathbf{b}_\alpha \ ,$$

   with $i$, $k$ running on $\{ 1, 2\}$, while $\alpha$ running on $\{ 1, 2, 3 \}$ with the third component identifying the normal direction. The second-order local approximation of the surface reads

   $$\begin{aligned}
     \mathbf{r}(q^k+d q^k) 
     & \sim \mathbf{r}(q^k) + d q^i \, \mathbf{r}_i(q^k) + \frac{1}{2} dq^i dq^j \mathbf{r}_{ij}(q^k) = \\
     & \sim \mathbf{r}(q^k) + d q^i \, \mathbf{b}_i + \frac{1}{2} dq^i dq^j \Gamma_{ij}^{\alpha} \mathbf{b}_{\alpha}  \ ,
   \end{aligned}$$

   so that the projection normal to the tangent plane defined by $\mathbf{b}_1$, $\mathbf{b}_2$ is

   $$\mathbf{\hat{n}} \cdot \left( \mathbf{r}(q^k+dq^k) - \mathbf{r}(q^k) \right) = \frac{1}{2} dq^i dq^j \Gamma^3_{ij} \ ,$$

   i.e. a quadratic form of the coordinates $(q^1, q^2)$, whose coefficients define the second fundamental form, i.e.

   $$\mathbf{\hat{n}} \cdot \left( \mathbf{r}(q^k+dq^k) - \mathbf{r}(q^k) \right) = \frac{1}{2} \left( L dq^1 dq^1 + 2 M dq^1 dq^2 + N dq^2 dq^2 \right) \ ,$$

   with

   $$\begin{aligned}
     L & = \Gamma^{3}_{11} = \mathbf{r}_u \cdot \partial_u \hat{\mathbf{n}} \\
     M & = \Gamma^{3}_{12} = \mathbf{r}_u \cdot \partial_v \hat{\mathbf{n}} = \mathbf{r}_v \cdot \partial_u \hat{\mathbf{n}} \\
     N & = \Gamma^{3}_{22} = \mathbf{r}_v \cdot \partial_v \hat{\mathbf{n}} \\
   \end{aligned}$$

   having exploited the relation {eq}`eq:second-fundamental-form-derivative-n`.

```{dropdown} Weingarten formula, derivatives of the normal vector and fundamental forms
:open:

**Weingarten formula.** *See also {eq}`eq:differential-geometry:curvature:weingarten`*. Differentiating $\hat{\mathbf{n}} \cdot \mathbf{b}_i = 0$,

$$\partial_k \hat{\mathbf{n}} \cdot \mathbf{b}_i = - \hat{\mathbf{n}} \cdot \partial_k \mathbf{b}_i = - \hat{\mathbf{n}} \cdot \mathbf{b}_\alpha \Gamma^{\alpha}_{ik} = - \Gamma^3_{ik} \ ,$$

so that it immediately follows that the derivatives of the unit normal vector w.r.t. the coordinates $q^k$ are

$$\partial_k \hat{\mathbf{n}} = - \Gamma_{ik}^{3} \mathbf{b}^i = - g^{il} \Gamma_{ik}^{3} \mathbf{b}_l \ ,$$ (eq:surface:weingarten)

or, explicitly

$$\left\{ \begin{aligned}
  \partial_1 \hat{\mathbf{n}} & = - \Gamma_{i1}^{3} \mathbf{b}^i = - g^{il} \Gamma_{i1}^{3} \mathbf{b}_l \\
  \partial_2 \hat{\mathbf{n}} & = - \Gamma_{i2}^{3} \mathbf{b}^i = - g^{il} \Gamma_{i2}^{3} \mathbf{b}_l \\
\end{aligned}\right.$$

Exploiting the orhogonality with the reciprocal basis,  $\mathbf{b}^i \cdot \mathbf{b}_j = \delta^i_j$, it follows

$$\Gamma_{ik}^3 = \partial_{i} \hat{\mathbf{n}} \cdot \mathbf{b}_k \ .$$ (eq:second-fundamental-form-derivative-n)

Since the reciprocal basis is $\mathbf{b}^i = g^{ik} \mathbf{b}_k = [ g_{ik} ]^{-1} \mathbf{b}_k$, or - with matrix formalism with vectors as elements -

$$
  \begin{bmatrix} \mathbf{b}^1 \\ \mathbf{b}^2 \end{bmatrix} 
  = \begin{bmatrix} E & F \\ F & G \end{bmatrix}^{-1} \begin{bmatrix} \mathbf{b}_1 \\ \mathbf{b}_2 \end{bmatrix}
  = \frac{1}{EG-F^2} \begin{bmatrix} G & -F \\ -F & E \end{bmatrix} \begin{bmatrix} \mathbf{b}_1 \\ \mathbf{b}_2 \end{bmatrix}
$$

then, the derivatives of the unit normal vector are

$$\left\{ \begin{aligned}
  \hat{\mathbf{n}}_u & = \hat{\mathbf{n}}_1 = - \Gamma_{11}^3 \mathbf{b}^1 - \Gamma_{21}^3 \mathbf{b}^2 = \\
  & = - \frac{1}{EG-F^2} \left\{ \left(   \Gamma_{11}^3 G - \Gamma_{21}^{3} F \right) \mathbf{b}_1 + \left( - \Gamma_{11}^3 F + \Gamma_{12}^{3} E  \right) \mathbf{b}_2 \right\} =\\ 
  & = \frac{MF-LG}{EG-F^2} \mathbf{r}_u + \frac{LF-ME}{EG-F^2} \mathbf{r}_v \\
  \hat{\mathbf{n}}_v & = \hat{\mathbf{n}}_2 = - \Gamma_{12}^3 \mathbf{b}^1 - \Gamma_{22}^3 \mathbf{b}^2 = \\
  & = - \frac{1}{EG-F^2} \left\{ \left(   \Gamma_{12}^3 G - \Gamma_{22}^{3} F \right) \mathbf{b}_1 + \left( - \Gamma_{12}^3 F + \Gamma_{22}^{3} E  \right) \mathbf{b}_2 \right\} = \\
  & = \frac{NF-MG}{EG-F^2} \mathbf{r}_u + \frac{MF-NE}{EG-F^2} \mathbf{r}_v \\
\end{aligned} \right.$$

```

