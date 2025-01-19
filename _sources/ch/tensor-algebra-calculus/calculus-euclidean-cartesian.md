(tensor:calculus:cartesian)=
# Tensor Calculus in Euclidean Spaces - Cartesian coordinates in $E^3$

Using Cartesian coordinates $(q^1, q^2, q^3) = (r, \theta, z)$ and Cartesian base vectors (uniform in space, so that their derivatives are zero), a point in Euclidean vector space $E^3$ can be represented as

$$\vec{r} = x \, \hat{x} + y \, \hat{y} + z \, \hat{z} \ .$$

(tensor:calculus:cartesian:metric)=
## Natural basis, reciprocal basis, metric tensor, and Christoffel symbols

Cartesian coordinates in Euclidean spaces are a very special coordinate system, with reciprocal basis everywhere coinciding with natural basis, with uniform basis in space (zero second-order derivative of space w.r.t. coordinates, and thus zero first order derivative of base vectors, and thus identically zero Christoffel symbols), and components of the metric tensor equal to the identity matrix

$$\begin{cases}
  \vec{b}_1 = \vec{b}^1 = \hat{x} \\
  \vec{b}_2 = \vec{b}^2 = \hat{y} \\
  \vec{b}_3 = \vec{b}^3 = \hat{z} \\
\end{cases}$$

$$\left[g_{ab} \right] = \left[ g^{ab} \right] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

$$\Gamma_{ab}^c = 0 \qquad , \qquad \forall a,b,c = 1:3 \ .$$


(tensor:calculus:cartesian:differential-operators)=
## Differential operators
(tensor:calculus:cartesian:differential-operators:gradient)=

### Gradient
(tensor:calculus:cartesian:differential-operators:directional-der)=

```{prf:example} Gradient of a scalar field
:class: dropdown

$$\nabla F = \hat{x} \, \partial_x F + \hat{y} \, \partial_y F + \hat{z} \, \partial_z F_z$$

```
```{prf:example} Gradient of a vector field
:class: dropdown

$$\begin{aligned}
\nabla F 
  & = \nabla (F_x \hat{x} + F_y \hat{y} + F_z \hat{z}) = \\
  & = \hat{x} \otimes \hat{x} \, \partial_x F_x + \hat{x} \otimes \hat{y} \, \partial_x F_y + \hat{x} \otimes \hat{z} \, \partial_x F_z + \\
  & + \hat{y} \otimes \hat{x} \, \partial_y F_x + \hat{y} \otimes \hat{y} \, \partial_y F_y + \hat{y} \otimes \hat{z} \, \partial_y F_z + \\
  & + \hat{z} \otimes \hat{x} \, \partial_z F_x + \hat{z} \otimes \hat{y} \, \partial_z F_y + \hat{z} \otimes \hat{z} \, \partial_z F_z + \\
\end{aligned}$$

```
```{prf:example} Gradient of a $2^{nd}$-order tensor field
:class: dropdown
```
### Directional derivative
(tensor:calculus:cartesian:differential-operators:divergence)=
### Divergence
```{prf:example} Divergence of a vector field
:class: dropdown

$$\begin{aligned}
 \nabla \cdot F 
  & = \nabla \cdot \left( F_x \, \hat{x} + F_y \, \hat{y} + F_z \, \hat{z} \right) = \\
  & = \partial_x F_x + \partial_y F_y + \partial_z F_z \ .
\end{aligned}$$

```
```{prf:example} Divergence of a $2^{nd}$-order tensor field
:class: dropdown

$$\begin{aligned}
 \nabla \cdot F 
  & = \nabla \cdot \left( F_{ab} \vec{e}_a \otimes \vec{e}_b \right) = \\
  & = \vec{e}_c \dfrac{\partial F_{ab}}{\partial q^a} = \\
  & = \hat{x} \left[ \partial_x F_{xx} + \partial_y F_{yx} + \partial_z F_{zx} \right] + \\ 
  & + \hat{y} \left[ \partial_x F_{xy} + \partial_y F_{yy} + \partial_z F_{zy} \right] + \\ 
  & + \hat{z} \left[ \partial_x F_{xz} + \partial_y F_{yz} + \partial_z F_{zz} \right] \ .
\end{aligned}$$

```
(tensor:calculus:cartesian:differential-operators:laplacian)=
### Laplacian
```{prf:example} Laplacian of a scalar field
:class: dropdown

$$\nabla^2 F = \partial_{xx} F + \partial_{yy} F + \partial_{zz} F$$

```
```{prf:example} Laplacian of a vector field
:class: dropdown
```


