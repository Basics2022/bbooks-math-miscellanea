(differential-geometry:intro)=
# Introduction to Differential Geometry

Geometric entities embedded in 3-dimensional Euclidean space
* [Lines](differential-geometry:lines)
* [Surfaces](differential-geometry:surfaces)

**Euclidean space, $E^3$.** Points in space can be represented with Cartesian coordinates $\{ x^i \}_{i=1:3}$, i.e. $\mathbf{r}(x^i)$. As shown in the introduction to [tensor calculus](tensor:calculus), the [natural basis](tensor:calculus:coordinates:natural-basis) induced by a set of coordinates $\{ q^a \}_a$ is

$$\mathbf{b}_{a} := \frac{\partial \mathbf{r}}{\partial q^a} (q^b) \ .$$

For a set of Cartesian coordinates, the induced natural basis - whose vectors are often denoted with the letters $\hat{\mathbf{e}}_i$, or $\hat{\mathbf{x}}_i$ - is **orthonormal**, and uniform (constant, independent from the coordinates) in space, i.e.

$$\mathbf{b}_a = \hat{\mathbf{x}}_a = \frac{\partial \mathbf{r}}{\partial x^a} \ .$$

Thus, 

* the **position vector** $\mathbf{r}$ can be written as 

   $$\mathbf{r} = x^a \hat{\mathbf{x}}_a \ ,$$

* as the vectors of the natural basis are not functions of the coordinates- as they're uniform in space -, then their space derivatives - and the Christoffell symbols - are identically zero,

   $$0 = \dfrac{\partial \hat{\mathbf{x}}_a}{\partial x^b} =  \dfrac{\partial^2 \mathbf{r}}{\partial x^a \partial x^b} \quad , \quad \Gamma_{ab}^c \equiv 0 \ ,$$

* as the basis is orthonormal, $\hat{\mathbf{x}}_i \cdot \hat{\mathbf{x}}_j = \delta_{ij}$, then the components of the metric tensor are
  
   $$\left[ g_{ab} \right] = \left[ g^{ab} \right] = \mathbf{I}_3 \ ,$$

* from the definition of the reciprocal basis, $\mathbf{b}^a = g^{ab} \mathbf{b}_b$, it follows that the reciprocal basis of a Cartesian basiscoincides the basis itself.





