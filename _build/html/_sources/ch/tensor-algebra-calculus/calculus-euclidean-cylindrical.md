(tensor:calculus:cylindrical)=
# Tensor Calculus in Euclidean Spaces - cylindrical coordinates in $E^3$

(tensor:calculus:cylindrical:coordinates)=
## Cylindrical coordiantes and cylindrical coordinates

Using cylindrical coordinates $(q^1, q^2, q^3) = (r, \theta, z)$ and cylindrical base vectors (uniform in space, so that their derivatives are zero), a point in Euclidean vector space $E^3$ can be represented as

$$\vec{r} = r \cos \theta \, \hat{x} + r \sin \theta \, \hat{y} + z \, \hat{z} \ .$$

(tensor:calculus:cylindrical:metric)=
## Natural basis, reciprocal basis, metric tensor, and Christoffel symbols

```{dropdown} Natural basis
Natural basis reads

$$\begin{cases}
\vec{b}_1 = \dfrac{\partial \vec{r}}{\partial q^1} = \dfrac{\partial \vec{r}}{\partial r     } = \cos \theta \, \hat{x} + \sin \theta \, \hat{y} \\
\vec{b}_2 = \dfrac{\partial \vec{r}}{\partial q^2} = \dfrac{\partial \vec{r}}{\partial \theta} = - r \sin \theta \, \hat{x} + r \cos \theta \, \hat{y} \\
\vec{b}_3 = \dfrac{\partial \vec{r}}{\partial q^3} = \dfrac{\partial \vec{r}}{\partial z     } = \hat{z} \\
\end{cases}$$
```

```{dropdown} Metric tensor
Covariant components of metric tensors,

$$g_{ab} = \vec{b}_a \cdot \vec{b}_b \ , $$

can be collected in the diagonal matrix

$$\left[ g_{ab} \right] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & r^2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \ ,$$

while its contra-variant components can be collected in the inverse matrix (easy to compute, since $\left[ g_{ab} \right]$ is diagonal),

$$\left[ g^{ab} \right] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \frac{1}{r^2} & 0 \\ 0 & 0 & 1 \end{bmatrix} \ .$$

```

```{dropdown} Reciprocal basis

Reciprocal basis is readily evaluated using $\vec{b}^a = g^{ab} \, \vec{b}_b$,

$$\begin{cases}
\vec{b}^1 =  \cos \theta \, \hat{x} + \sin \theta \, \hat{y} \\
\vec{b}^2 =  - \dfrac{1}{r} \sin \theta \, \hat{x} + \dfrac{1}{r} \cos \theta \, \hat{y} \\
\vec{b}^3 =  \hat{z} \\
\end{cases}$$

```

```{dropdown} Physical basis
Since metric tensor is diagonal, the cylindrical coordinate system is orthogonal, and its natural and reciprocal basis are orthogonal. A unit orthogonal basis, usually named **physical basis** with unit vector with no physical dimension, is evalated by normalization process,

$$\begin{cases}
  \hat{r}      = \hat{b}_1 = \dfrac{\vec{b}_1}{g_{11}} = \dfrac{\vec{b}^1}{g^{11}} =  \cos \theta \, \hat{x} + \sin \theta \, \hat{y} \\
  \hat{\theta} = \hat{b}_2 = \dfrac{\vec{b}_2}{g_{22}} = \dfrac{\vec{b}^2}{g^{22}} = -\sin \theta \, \hat{x} + \cos \theta \, \hat{y} \\
  \hat{z}      = \hat{b}_3 = \dfrac{\vec{b}_3}{g_{33}} = \dfrac{\vec{b}^3}{g^{33}} =  \hat{z} \ .
\end{cases}$$
```

```{dropdown} Derivatives of natural basis and Christoffel symbols
Derivatives of the natural basis read

$$\begin{aligned}
 \dfrac{\partial \vec{b}_1}{\partial q^1} & = \vec{0} \\
 \dfrac{\partial \vec{b}_2}{\partial q^2} & = -r \cos \theta \, \hat{x} - r \sin \theta \, \hat{y} = - q^1 \, \vec{b}_1 \\
 \dfrac{\partial \vec{b}_3}{\partial q^3} & = \vec{0} \\
 \dfrac{\partial \vec{b}_2}{\partial q^1} = \dfrac{\partial \vec{b}_1}{\partial q^2} & = -\sin \theta \, \hat{x} + \cos \theta \hat{y} = \dfrac{1}{q^1} \, \vec{b}_2 \\
 \dfrac{\partial \vec{b}_3}{\partial q^1} = \dfrac{\partial \vec{b}_1}{\partial q^3} & = \vec{0} \\
 \dfrac{\partial \vec{b}_3}{\partial q^2} = \dfrac{\partial \vec{b}_2}{\partial q^3} & = \vec{0} \\
\end{aligned}$$

so that non-zero Christoffel symbols of a cylindrical coordinate system are

$$\begin{aligned}
  & \Gamma_{12}^{2} = \Gamma_{21}^2 = \dfrac{1}{q^1} \\
  & \Gamma_{22}^{1} = - q^1 \ .
\end{aligned}$$
```

(tensor:calculus:cylindrical:differential-operators)=
## Differential operators
(tensor:calculus:cylindrical:differential-operators:gradient)=
### Gradient
```{prf:example} Gradient of a scalar field
:class: dropdown

$$\begin{aligned}
  \nabla F 
  & = \vec{b}^a \dfrac{\partial F}{\partial q^a} = \\
  & = \hat{b}_a \, g^{aa} \, \dfrac{\partial F}{\partial q^a} = \\
  & = \hat{r} \, \dfrac{\partial F}{\partial  r} 
    + \hat{\theta} \, \dfrac{1}{r} \, \dfrac{\partial F}{\partial \theta}  
    + \hat{z} \dfrac{\partial F}{\partial z} \ . 
\end{aligned}$$

```
```{prf:example} Gradient of a vector field
:class: dropdown

<!--
$$\begin{aligned}
 \vec{F}
 & = F^1 \, \vec{b}_1 + F^2        \, \vec{b}_2    + \vec{F}^3 \, \vec{b}_3 = \\
 & = F_1 \, \vec{b}^1 + F_2        \, \vec{b}^2    + \vec{F}_3 \, \vec{b}^3 = \\
 & = F_r \, \hat{r}   + F_{\theta} \, \hat{\theta} + \vec{F}_z \, \hat{z} \ .
\end{aligned}$$
-->

$$\begin{aligned}
  \nabla F 
  & = \vec{b}^a \otimes \vec{b}_b \left[ \dfrac{\partial F^b}{\partial q^a} + \Gamma_{ac}^b \, F^c \right] = \\
  & = \dots = \\
  & =  \vec{b}^1 \otimes \vec{b}_1 \, \partial_1 F^1 
  && + \vec{b}^1 \otimes \vec{b}_2 \, \left[ \partial_1 F^2 + \Gamma_{12}^2 F^2 \right]
  && + \vec{b}^1 \otimes \vec{b}_3 \, \partial_1 F^3 \\
  &  + \vec{b}^2 \otimes \vec{b}_1 \, \left[ \partial_2 F^1 + \Gamma_{22}^1 F^2 \right]
  && + \vec{b}^2 \otimes \vec{b}_2 \, \left[ \partial_2 F^2 + \Gamma_{21}^2 F^1 \right]
  && + \vec{b}^2 \otimes \vec{b}_3 \, \partial_2 F^3 \\
  &  + \vec{b}^3 \otimes \vec{b}_1 \, \partial_3 F^1 
  && + \vec{b}^3 \otimes \vec{b}_2 \, \partial_3 F^2 
  && + \vec{b}^3 \otimes \vec{b}_3 \, \partial_3 F^3 \\
  &  = \hat{r     } \otimes \hat{r     } \, \partial_r F_r   
  && + \hat{r     } \otimes \hat{\theta} \, \frac{1}{r} \left[ \partial_r (r F_{\theta}) + F_{\theta} \right]
  && + \hat{r     } \otimes \hat{z     } \, \partial_r F_z \\
  &  + \hat{\theta} \otimes \hat{r     } \, \frac{1}{r} \left[ \partial_\theta F_r - r F_{\theta} \right]
  && + \hat{\theta} \otimes \hat{\theta} \, \left[ \partial_\theta \left( \frac{F_\theta}{r} \right) + \frac{F_r}{r} \right]
  && + \hat{\theta} \otimes \hat{z     } \, \frac{1}{r} \partial_{\theta} F_z \\
  &  + \hat{z     } \otimes \hat{r     } \, \partial_z F_x   
  && + \hat{z     } \otimes \hat{\theta} \, \frac{1}{r} \partial_\theta F_y   
  && + \hat{z     } \otimes \hat{z     } \, \partial_z F_z \ .
\end{aligned}$$

```

```{prf:example} Gradient of a $2^{nd}$-order tensor field
:class: dropdown
```
(tensor:calculus:cylindrical:differential-operators:directional-der)=
### Directional derivative
(tensor:calculus:cylindrical:differential-operators:divergence)=
### Divergence
(tensor:calculus:cylindrical:differential-operators:laplacian)=
```{prf:example} Divergence of a vector field
:class: dropdown

$$\begin{aligned}
  \nabla \cdot \vec{F} 
  & = \dfrac{\partial F^a}{\partial q^a} + \Gamma_{ac}^a \, F^c = \\
  & = \dfrac{\partial F_r}{\partial r} + \dfrac{\partial}{\partial \theta}\left( \frac{F_\theta}{r} \right) + \frac{F_\theta}{r} + \dfrac{\partial F_z}{\partial z} = \\
\end{aligned}$$
```
```{prf:example} Divergence of a $2^{nd}$-order tensor field
:class: dropdown
```
### Laplacian
```{prf:example} Laplacian of a scalar field
:class: dropdown
```
```{prf:example} Laplacian of a vector field
:class: dropdown
```

