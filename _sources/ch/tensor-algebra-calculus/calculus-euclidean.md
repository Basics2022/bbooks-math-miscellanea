(tensor:calculus)=
# Tensor Calculus in Euclidean Spaces

This section deals with tensor calculus in Euclidean space or on manifolds embedded in Euclidean spaces, focusing on $d$-dimensional spaces with $d \le 3$, with *inner product*.

This section may rely on results of [differential geometry](differential-geometry:intro).

## Coordinates
A set of parameters $\{q^a\}_{a=1:d}$ to represent vector (or point) in space,

$$\vec{r}(q^a)$$

if $\vec{r} \in E^{d}$, $a=1:d$.

In $E^3$,
- **Coordinate lines**, 2-parameter family of lines, keeping 2 coordinates constant. As an example, coordinate lines with constant $q^2, \, q^3$

  $$\vec{r}_1(q^1) = \vec{r}(q^1, \bar{q}^2, \bar{q}^3) \ .$$

- **Coordinate surfaces,** 1-parameter family of surfaces, keeping 1 coordinate constant. As an example, coordinate surfaces with constant $q^1$,

  $$\vec{r}_{23}(q^2, q^3) = \vec{r}(\bar{q}^1, q^2, q^3) \ .$$

```{prf:definition} Regular parametrization
If $\frac{\partial \vec{r}}{\partial q^a} \ne 0$.
```

### Natural basis
```{prf:definition} Natural basis
Vectors of natural basis

$$\vec{b}_a := \frac{\partial \vec{r}}{\partial q^a}$$

```

```{prf:definition} Christoffel symbols
```


## Fields
Function of the points in space $F: E^d \rightarrow V^r$, being $V^r$ a space of tensors of order $r$.


## Differential operators

### Directional derivative

$$F(\vec{r}) = F\left(\vec{r}\left(q^a\right)\right) = f(q^a)$$
$$f(q^a + \beta \Delta q^a) = F(\vec{r}(q^a + \beta \Delta q^a))$$

$$\vec{r}(q^a) + \alpha \vec{v} = \vec{r}(q^a + \beta \Delta q^a) \sim \vec{r}(q^a) + \frac{\partial \vec{r}}{\partial q^b} \beta \Delta q^b $$
$$\alpha \vec{v} \sim \beta \frac{\partial \vec{r}}{\partial q^b}(q^a) \, \Delta q^b = \beta \vec{b}_b(q^a) \Delta q^b
\qquad \rightarrow \qquad \Delta q^b = \frac{\alpha}{\beta} \vec{b}^b(q^a) \cdot \vec{v} $$

The directional derivative for an arbitrary vector $\vec{v} \in V$

$$\frac{d}{d \alpha} F(\vec{r} + \alpha \vec{v})\bigg|_{\alpha = 0}$$

is evaluated as the limit for $\alpha \rightarrow 0$ of the incremental ratio

$$\begin{aligned}
 \frac{F(\vec{r} + \alpha \vec{v}) - F(\vec{r})}{\alpha} 
 & \sim \frac{f(q^a + \beta \Delta q^a) - f(q^a)}{\alpha} = \\ 
 & \sim \frac{1}{\alpha} \frac{\partial f}{\partial q^b}(q^a) \beta \Delta q^b = \\
 & \sim \vec{v} \cdot \vec{b}^b(q^a) \frac{\partial f}{\partial q^b}(q^a) = \\
 & = \vec{v} \cdot \nabla F(\vec{r})
\end{aligned}$$

### Gradient

The gradient is the differential operator is the first-order differential operator appearing in the definition of the directional derivative, $\nabla F(\vec{r})$. It takes a tensor field $F(\vec{r})$ of order $r$ and gives a tensor field $\nabla F(\vec{r})$ of order $r+1$. Given a set of coordinates $\{q^a\}_{a=1:d}$, the gradient can be written using the reciprocal basis of the natural basis as

$$\nabla F(\vec{r}) = \vec{b}^b(\vec{r}) \frac{\partial F}{\partial q^b}(\vec{r})$$

**Examples.** ...

### Divergence

Divergence opearator is a first-order differential operator that can be defined as the contraction of the first two indices of the gradient,

$$\nabla \cdot F = C_{1}^{2}\left( \nabla F \right) \ .$$

It takes a tensor field $F(\vec{r})$ of order $r \ge 1$ and gives a tensor field $\nabla \cdot F(\vec{r})$ of order $r-1 \ge 0$.

### Laplacian

Laplacian operator is second-order differential operator that can be defined as the divergence of the gradient,

$$\Delta F = \nabla^2 F = \nabla \cdot \nabla F \ .$$

### Curl


## Integrals in $E^d$, $d \le 3$

### Line integrals

#### Density 

Integrals

$$ \int_{\vec{r}\in\gamma} F(\vec{r})$$

represent the summation of contributions $F(\vec{r})$ over elementary segments of path $\gamma$, whose dimension is $|d \vec{r}|$, i.e. implicitly means

$$\int_{\vec{r}\in\gamma} F(\vec{r}) = \int_{\vec{r} \in \gamma} F(\vec{r}) \, |d \vec{r}| \ .$$

Given a regular parametrization of the curve $\vec{r}(q^1)$ (with increasing $q^1$ so that $|dq^1| = dq^1$), and the differential $d \vec{r} = \vec{r}'(q^1) \, d q^1$, the integral can be written as an integral in the parameter $q^1$

$$\int_{q=q^1_a}^{q^1_b} F(\vec{r}(q^1)) \, |\vec{r}'(q^1)| \, dq^1 \ ,$$

with $\vec{r}(q^1_a)$, $\vec{r}(q^1_b)$ the extreme points of path $\gamma$.

#### Work

Integrals

$$\int_{\vec{r} \in \gamma} F(\vec{r}) \cdot \hat{t}(\vec{r})$$

implicitly mean

$$\int_{\vec{r} \in \gamma} F(\vec{r}) \cdot \hat{t}(\vec{r}) = \int_{\vec{r} \in \gamma} F(\vec{r}) \cdot \hat{t}(\vec{r}) |d \vec{r}| = \int_{\vec{r} \in \gamma} F(\vec{r}) \cdot d \vec{r} \ ,$$

as $\hat{t} = \frac{d \vec{r}}{|d \vec{r}|}$.
Given a regular parametrization of the curve $\vec{r}(q^1)$ (with increasing $q^1$ so that $|dq^1| = dq^1$), and the differential $d \vec{r} = \vec{r}'(q^1) \, d q^1$, the integral can be written as an integral in the parameter $q^1$

$$\int_{q^1=q^1_a}^{q^1_b} F(\vec{r}(q^1)) \cdot \vec{r}'(q^1) \, dq^1$$

### Surface integrals

Given two coordinates $q^1, \, q^2$ describing a surface, $\vec{r}(q^1, q^2)$ the elementary surface with unit normal reads

$$\hat{n} \, dS = d \vec{r}_1 \times d \vec{r}_2 = \frac{\partial \vec{r}}{\partial q^1} \times \frac{\partial \vec{r}}{\partial q^2} \, dq^1 \, dq^2 \ ,$$

and the elementary surface thus reads

$$|dS| = |\hat{n} dS| = \left| \frac{\partial \vec{r}}{\partial q^1} \times \frac{\partial \vec{r}}{\partial q^2} \, dq^1 \, dq^2  \right|$$

#### Density

Integrals

$$\int_{\vec{r} \in S} F(\vec{r}) $$

implicitly mean

$$\int_{\vec{r} \in S} F(\vec{r}) = \int_{\vec{r} \in S} F(\vec{r}) |d S| \ .$$

Given regular parametrization of the surface, $\vec{r}(q^1, \, q^2), \ (q^1, q^2) \in Q^{12}$, the integral can be written as the multi-dimensional integral in coordinates $q^1, \ q^2$,

$$\int_{\vec{r} \in S} F(\vec{r}) = \int_{(q^1,q^2) \in Q^{12}} F(\vec{r}(q^1,q^2)) \left| \frac{\partial \vec{r}}{\partial q^1} \times \frac{\partial \vec{r}}{\partial q^2}  \, dq^1 \, dq^2 \right|$$

#### Flux

Integrals

$$\int_{\vec{r} \in S} \hat{n}(\vec{r}) \cdot F(\vec{r}) $$

implicitly mean

$$\int_{\vec{r} \in S} \hat{n}(\vec{r}) \cdot F(\vec{r}) = \int_{\vec{r} \in S} \hat{n}(\vec{r}) \cdot F(\vec{r}) |dS| $$

Given regular parametrization of the surface, $\vec{r}(q^1, \, q^2), \ (q^1, q^2) \in Q^{12}$, the integral can be written as the multi-dimensional integral in coordinates $q^1, \ q^2$,

$$\int_{\vec{r} \in S} \hat{n}(\vec{r}) \cdot F(\vec{r}) = \int_{(q^1,q^2) \in Q^{12}} \frac{\partial \vec{r}}{\partial q^1} \times \frac{\partial \vec{r}}{\partial q^2} \cdot  F(\vec{r}(q^1,q^2))\, dq^1 \, dq^2 $$

### Volume

$$dV = \frac{\partial \vec{r}}{\partial q^1} \cdot \frac{\partial \vec{r}}{\partial q^2} \times \frac{\partial \vec{r}}{\partial q^3} \, dq^1 \, dq^2 \, d q^3 \ . $$ 

#### Density

Integrals

$$\int_{\vec{r} \in V} F(\vec{r})$$

implicitly mean

$$\int_{\vec{r} \in V} F(\vec{r}) = \int_{\vec{r} \in V} F(\vec{r}) \, |dV| \ .$$

Given regular parametrization of the volume, $\vec{r}(q^1, \, q^2, \, q^3), \ (q^1, q^2, q^3) \in Q$, the integral can be written as the multi-dimensional integral in coordinates $q^1, \, q^2, \, q^3$,

$$\int_{\vec{r} \in V} F(\vec{r}) |d V| = \int_{(q^1,q^2,q^3) \in Q} F(\vec{r}(q^1,q^2,q^3))  \left| \frac{\partial \vec{r}}{\partial q^1} \cdot \frac{\partial \vec{r}}{\partial q^2} \times \frac{\partial \vec{r}}{\partial q^3} \, dq^1 \, dq^2 \, d q^3 \right| \ .$$

