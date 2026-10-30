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

For $i=1:2$, $j=1:2$

$$\frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} = \frac{\partial \mathbf{b}_i}{\partial q^j} = \Gamma_{ij}^k \mathbf{b}_k = \Gamma_{ij}^1 \mathbf{b}_1 + \Gamma_{ij}^2 \mathbf{b}_2 + \Gamma_{ij}^3 \mathbf{b}_3 \ ,$$

so that

$$\Gamma_{ij}^{k} = \mathbf{b}^k \cdot \frac{\partial \mathbf{b}_i}{\partial q^j} \ .$$

**Remark.** Comparing two different choices of the orthogonal coordinate $q^3$, (1) unit normal vector $\hat{\mathbf{b}}_3 = \hat{\mathbf{n}}$, (2) non-unitary normal vector $\hat{\mathbf{b}}_3 = \mathbf{n}$, $\hat{\mathbf{b}}^3 = \tfrac{\mathbf{n}}{|\mathbf{n}|^2}$, it's easy to prove that the Christoffel coefficients with upper index $k = 3$, $\Gamma^{3}_{ij}$, are independent from this choice.

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
  & = \mathbf{r}(q_1, q_2) + \frac{\partial \mathbf{r}}{\partial q^i} \, dq^i + \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \, dq^i dq^j + o\left(|d q^i|^2\right) = \\
  & = \mathbf{r}(q_1, q_2) + \mathbf{b}_{i} \, dq^i + \mathbf{b}_k \Gamma^{k}_{ij} \, dq^i \, dq^j +  \hat{\mathbf{n}} \, \Gamma^{3}_{ij} \, dq^i dq^j  + o\left(|d q^i|^2\right) \ , 
\end{aligned}$$

so that

$$\begin{aligned}
\left[ \mathbf{r}(q^1 + d q^1, q^2 + d q^2) - \mathbf{r}(q^1, q^2) \right] \cdot \hat{\mathbf{n}}
 & = \Gamma^3_{ij} \, d q^i \, dq^j = \\
 & = \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \, d q^i \, dq^j = \\
 & = \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \, \mathbf{b}^i \cdot \mathbf{b}_k d q^k \, \mathbf{b}^j \cdot \mathbf{b}_l dq^l = \\
 & = \underbrace{d q^k \mathbf{b}_k}_{d \mathbf{r}} \cdot \left[ \left( \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \right) \mathbf{b}^i \otimes \mathbf{b}^j \right] \cdot \underbrace{d q^l \mathbf{b}_l}_{d\mathbf{r}} = \\
 & = d \mathbf{r} \cdot \mathbb{b} \cdot d \mathbf{r} \ ,
\end{aligned}$$

having defined the **curvature tensor** $\mathbb{b}$,

$$\mathbb{b} = b_{ij} \mathbf{b}^i \otimes \mathbf{b}^j = \left( \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} \right) \mathbf{b}^i \otimes \mathbf{b}^j \ .$$

(differential-geometry:surfaces:geometric-entities:curvature-tensor)=
### Curvature tensor

From the second-order Taylor expansion around a point $\mathbf{r}(q^1, q^2)$, the projection of the displacement onto the unit normal vector $\hat{\mathbf{n}}$ measures the distance from the surface to its tangent plane $\pi$:

$$[\mathbf{r}(q^1 + dq^1, q^2 + dq^2) - \mathbf{r}(q^1, q^2)] \cdot \hat{\mathbf{n}} = \Gamma_{ij}^3 dq^i dq^j = b_{ij} dq^i dq^j .$$

The symmetric covariant tensor of rank 2, defined by its components

$$b_{ij} := \Gamma_{ij}^3 = \hat{\mathbf{n}} \cdot \frac{\partial^2 \mathbf{r}}{\partial q^i \partial q^j} = -\frac{\partial \hat{\mathbf{n}}}{\partial q^i} \cdot \mathbf{b}_j ,$$

is the **second fundamental form** (or curvature tensor) of the surface embedded in $E^3$.

The quadratic form $b_{ij} dq^i dq^j$ characterizes the local deviation of the surface from the tangent plane $\pi$. Using the metric tensor $g_{ij}$ (the *first fundamental form*), we can define the mixed curvature tensor $b^i_j = g^{ik} b_{kj}$ and compute the fundamental intrinsic scalar measures of curvature:

* **Mean Curvature ($H$):**
  $$H = \frac{1}{2} b^i_i = \frac{1}{2} g^{ij} b_{ij} = \frac{g_{22}b_{11} - 2g_{12}b_{12} + g_{11}b_{22}}{2(g_{11}g_{22} - g_{12}^2)}$$

* **Gaussian Curvature ($K$):**
  $$K = \det(b^i_j) = \frac{\det(b_{ij})}{\det(g_{ij})} = \frac{b_{11}b_{22} - b_{12}^2}{g_{11}g_{22} - g_{12}^2}$$

(differential-geometry:surfaces:geometric-entities:curvature-tensor:principal)=
#### Principal Curvatures and Directions

The extreme values of the normal curvature $\kappa_n = \frac{b_{ij}dq^i dq^j}{g_{ij}dq^i dq^j}$ are the **principal curvatures** $\kappa_1$ and $\kappa_2$, which are the eigenvalues of the tensor $b^i_j$:

$$\det(b^i_j - \kappa \delta^i_j) = 0 \quad \implies \quad \kappa^2 - 2H\kappa + K = 0 .$$

Thus, the principal curvatures satisfy:

$$\kappa_{1,2} = H \pm \sqrt{H^2 - K} .$$

* The Gaussian curvature is the product of the principal curvatures: $K = \kappa_1 \kappa_2$.
* The Mean curvature is the average of the principal curvatures: $H = \frac{1}{2}(\kappa_1 + \kappa_2)$.

...
