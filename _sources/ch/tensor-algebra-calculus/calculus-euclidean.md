(tensor:calculus)=
# Tensor Calculus in Euclidean Spaces

This section deals with tensor calculus in Euclidean space or on manifolds embedded in Euclidean spaces, focusing on $d$-dimensional spaces with $d \le 3$, with *inner product*.

This section may rely on results of [differential geometry](differential-geometry:intro).

(tensor:calculus:coordinates)=
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

(tensor:calculus:coordinates:natural-basis)=
### Natural basis
```{prf:definition} Natural basis
Vectors of natural basis

$$\vec{b}_a := \frac{\partial \vec{r}}{\partial q^a}$$

```

```{prf:definition} Reciprocal basis (**todo** move to [Tensor Algebra](tensor:algebra))
Given a basis $\{ \vec{b}_a \}_{a}$, its reciprocal basis the set of vector $\{ \vec{b}^b \}_b$ defined as

$$\vec{b}^b \cdot \vec{b}_a = \delta_{a}^b \ ,$$

being $\delta_a^b$ Kronecker delta.

```

```{prf:definition} Christoffel symbols
Christoffel symbols (of the $2^{nd}$ kind) are defined as the components of the partial derivatives of the vectors of a natural basis w.r.t. the coordinates referred to the natural basis itself,

$$\dfrac{\partial \vec{b}_a}{\partial q^b} = \Gamma_{ab}^c \, \vec{b}_c$$ (def:christoffel:2)

```

```{dropdown} Properties of Christoffel symbols

Exploiting the definition of reciprocal basis, Christoffel symbols can be written as

$$\Gamma_{ab}^c = \vec{b}^c \cdot \dfrac{\partial \vec{b}_a}{\partial q^b} \ .$$

**Symmetry.** Symmetry os the lower indices

$$\Gamma_{ab}^{c} = \Gamma_{ba}^c \ ,$$

readily follows Schwartz theorem about partial derivatives

$$\dfrac{\partial \vec{b}_a}{\partial q^b} = \dfrac{\partial}{\partial q^c}\dfrac{\partial \vec{r}}{\partial q^a} = \dfrac{\partial}{\partial q^a}\dfrac{\partial \vec{r}}{\partial q^b} = \dfrac{\partial \vec{b}_b}{\partial q^a}$$

```


(tensor:calculus:fields)=
## Fields
Function of the points in space $F: E^d \rightarrow V^r$, being $V^r$ a space of tensors of order $r$.


(tensor:calculus:differential-operators)=
## Differential operators

(tensor:calculus:differential-operators:directional-derivative)=
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

(tensor:calculus:differential-operators:gradient)=
### Gradient

The gradient is the differential operator is the first-order differential operator appearing in the definition of the directional derivative, $\nabla F(\vec{r})$. It takes a tensor field $F(\vec{r})$ of order $r$ and gives a tensor field $\nabla F(\vec{r})$ of order $r+1$. Given a set of coordinates $\{q^a\}_{a=1:d}$, the gradient can be written using the reciprocal basis of the natural basis as

$$\nabla F(\vec{r}) = \vec{b}^b(\vec{r}) \frac{\partial F}{\partial q^b}(\vec{r})$$ (def:grad:q)

**Examples.** ...
```{prf:example} Gradient of a scalar field - with general coordinates $q^{a}$
:class: dropdown

Applying the definition {eq}`def:grad:q` of gradient operator, it readily follows

$$\nabla F = \vec{b}^a \dfrac{\partial F}{\partial q^a}$$

```

```{prf:example} Gradient of a vector field - with general coordinates $q^{a}$
:class: dropdown

Applying the definition {eq}`def:grad:q` of gradient operator, rule for the derivative of a product and the definition {eq}`def:christoffel:2` of Christoffel symbols to write derivatives of base vectors,

$$\begin{aligned}
  \nabla F 
  & = \vec{b}^a \dfrac{\partial}{\partial q^a} \left( F^b \vec{b}_b \right) = \\
  & = \vec{b}^a \left[ \dfrac{\partial F^b}{\partial q^a} \vec{b}_b + F^b \dfrac{\partial \vec{b}_b}{\partial q^a} \right] = \\
  & = \vec{b}^a \left[ \dfrac{\partial F^b}{\partial q^a} \vec{b}_b + F^b \, \Gamma_{ab}^c \, \vec{b}_c \right] = \\
  & = \vec{b}^a \otimes \vec{b}_b \left[ \dfrac{\partial F^b}{\partial q^a} + \Gamma_{ac}^b \, F^c \right] \ .
\end{aligned}$$

```

```{prf:example} Gradient of a $2^{nd}$-order tensor field - with general coordinates $q^{a}$
:class: dropdown

Applying the definition {eq}`def:grad:q` of gradient operator, rule for the derivative of a product and the definition {eq}`def:christoffel:2` of Christoffel symbols to write derivatives of base vectors,

$$\begin{aligned}
  \nabla F 
  & = \vec{b}^a \dfrac{\partial}{\partial q^a} \left( F^{bc} \vec{b}_b \otimes \vec{b}_c \right) = \\
  & = \vec{b}^a \left[ \dfrac{\partial F^{bc}}{\partial q^a} \vec{b}_b \, \vec{b}_c + F^{bc} \dfrac{\partial \vec{b}_b}{\partial q^a} \, \vec{b}_c + F^{bc} \vec{b}_b \dfrac{\partial \vec{b}_c}{\partial q^a} \right] = \\
  & = \vec{b}^a \left[ \dfrac{\partial F^{bc}}{\partial q^a} \vec{b}_b \, \vec{b}_c + F^{bc} \Gamma_{ab}^d \, \vec{b}_d \, \vec{b}_c + F^{bc} \, \Gamma_{d}^{ac} \, \vec{b}_b \, \vec{b}_d \right] = \\
  & = \vec{b}^a \otimes \vec{b}_b \otimes \vec{b}_c \left[ \dfrac{\partial F^{bc}}{\partial q^a} + \Gamma_{ad}^b \, F^{dc} + \Gamma^{c}_{ad} \, F^{bd}  \right] \ .
\end{aligned}$$

```

(tensor:calculus:differential-operators:divergence)=
### Divergence

Divergence opearator is a first-order differential operator that can be defined as the contraction of the first two indices of the gradient,

$$\nabla \cdot F = C_{1}^{2}\left( \nabla F \right) \ .$$

It takes a tensor field $F(\vec{r})$ of order $r \ge 1$ and gives a tensor field $\nabla \cdot F(\vec{r})$ of order $r-1 \ge 0$.

```{prf:example} Divergence of a vector field - with general coordiantes $q^{a}$
:class: dropdown

Applying contraction to the gradient of a vector field, it readily follows,

$$\begin{aligned}
  \nabla \cdot \left( F^b \vec{b}_b \right)
  & = C_{1}^{2} \left( \nabla F \right) = \\
  & = C_1^2 \left( \vec{b}^a \otimes \vec{b}_b \left[ \dfrac{\partial F^b}{\partial q^a} + \Gamma_{ac}^b \, F^c \right] \right) = \\
  & = \dfrac{\partial F^a}{\partial q^a} + \Gamma_{ac}^a \, F^c
\end{aligned}$$

```

```{prf:example} Divergence of a $2^{nd}$-order tensor field - with general coordiantes $q^{a}$
:class: dropdown

Applying contraction to the gradient of a vector field, it readily follows,

$$\begin{aligned}
  \nabla \cdot \left( F^{bc} \vec{b}_b \otimes \vec{b}_c \right)
  & = C_{1}^{2} \left( \nabla F \right) = \\
  & = C_1^2 \left( \vec{b}^a \otimes \vec{b}_b \otimes \vec{b}_c \left[ \dfrac{\partial F^{bc}}{\partial q^a} + \Gamma_{ad}^b \, F^{dc} + \Gamma^{c}_{ad} \, F^{bd}  \right]  \right) = \\
  & = \vec{b}_c \, \left[ \dfrac{\partial F^{ac}}{\partial q^a} + \Gamma_{ad}^a \, F^{dc} + \Gamma^{c}_{ad} \, F^{ad}  \right] 
\end{aligned}$$

```

(tensor:calculus:differential-operators:laplacian)=
### Laplacian

Laplacian operator is second-order differential operator that can be defined as the divergence of the gradient,

$$\Delta F = \nabla^2 F = \nabla \cdot \nabla F \ .$$

```{prf:example} Laplacian of a scalar field - with general coordinates $q^a$
:class: dropdown

$$
\nabla \cdot \nabla F
  & = C_{1}^2 \left[ \nabla \left( \nabla F \right) \right] = \\
  & = C_{1}^2 \left[ \nabla \left( \vec{b}^a \dfrac{\partial F}{\partial q^a} \right) \right] = \\
  & = C_{1}^2 \left[ \nabla \left( \vec{b}_b \, g^{ab} \, \dfrac{\partial F}{\partial q^a} \right) \right] = \\
  & = C_{1}^2 \left[ \vec{b}^c \frac{\partial}{\partial q^c} \left( \vec{b}_b \, g^{ab} \, \dfrac{\partial F}{\partial q^a} \right) \right] = \\
  & = C_{1}^2 \left\{ \vec{b}^c \left[ \vec{b}_b \, \frac{\partial}{\partial q^c} \left( \, g^{ab} \, \dfrac{\partial F}{\partial q^a} \right) + g^{ab} \dfrac{\partial F}{\partial q^a} \dfrac{\partial \vec{b}_b}{\partial q^c} \right] \right\} = \\
  & = C_{1}^2 \left\{ \vec{b}^c \left[ \vec{b}_b \, \frac{\partial}{\partial q^c} \left( \, g^{ab} \, \dfrac{\partial F}{\partial q^a} \right) + g^{ab} \dfrac{\partial F}{\partial q^a} \, \Gamma_{bc}^d \, \vec{b}_d \right] \right \} = \\
  & = C_{1}^2 \left\{ \vec{b}^c \, \vec{b}_b \left[ \frac{\partial}{\partial q^c} \left( \, g^{ab} \, \dfrac{\partial F}{\partial q^a} \right) + g^{ad} \, \Gamma_{cd}^b \, \dfrac{\partial F}{\partial q^a} \right] \right \} = \\
  & = \frac{\partial}{\partial q^b} \left( \, g^{ab} \, \dfrac{\partial F}{\partial q^a} \right) + g^{ad} \, \Gamma_{bd}^b \, \dfrac{\partial F}{\partial q^a} \ .
$$

```

```{prf:example} Laplacian of a vector field - with general coordinates $q^a$
:class: dropdown

$$
\nabla \cdot \nabla F
  & = C_{1}^2 \left[ \nabla \left( \nabla F \right) \right] = \\
  & = C_{1}^2 \left\{ \nabla \left[ \vec{b}^a \, \vec{b}_b \left( \dfrac{\partial F^b}{\partial q^a} + \Gamma^{b}_{ac} F^c \right) \right] \right\} = \\
  & = C_{1}^2 \left\{ \nabla \left[ \vec{b}_c \, \vec{b}_b \,  g^{ac} \left( \dfrac{\partial F^b}{\partial q^a} + \Gamma^{b}_{ac} F^c \right) \right] \right\} = \\
  & = C_{1}^2 \left\{ \nabla \cdot \left((\nabla F)^{cb} \, \vec{b}_c \, \vec{b}_b \right) \right\} = \\
  & = C_{1}^2 \left\{ \vec{b}^a \, \vec{b}_c \, \vec{b}_b \, \left[ \dfrac{\partial (\nabla F)^{cb}}{\partial q^a} 
     + \Gamma_{ad}^c (\nabla F)^{db} + \Gamma_{ad}^b (\nabla F)^{cd} \right] \right\} = \\
  & = \vec{b}_b \, \left[ \dfrac{\partial (\nabla F)^{ab}}{\partial q^a} 
     + \Gamma_{ad}^a (\nabla F)^{db} + \Gamma_{ad}^b (\nabla F)^{ad} \right] = \ .
$$

```

(tensor:calculus:differential-operators:curl)=
### Curl


(tensor:calculus:integrals)=
## Integrals in $E^d$, $d \le 3$

(tensor:calculus:integrals:line)=
### Line integrals

(tensor:calculus:integrals:line:density)=
#### Density 

Integrals

$$ \int_{\vec{r}\in\gamma} F(\vec{r})$$

represent the summation of contributions $F(\vec{r})$ over elementary segments of path $\gamma$, whose dimension is $|d \vec{r}|$, i.e. implicitly means

$$\int_{\vec{r}\in\gamma} F(\vec{r}) = \int_{\vec{r} \in \gamma} F(\vec{r}) \, |d \vec{r}| \ .$$

Given a regular parametrization of the curve $\vec{r}(q^1)$ (with increasing $q^1$ so that $|dq^1| = dq^1$), and the differential $d \vec{r} = \vec{r}'(q^1) \, d q^1$, the integral can be written as an integral in the parameter $q^1$

$$\int_{q=q^1_a}^{q^1_b} F(\vec{r}(q^1)) \, |\vec{r}'(q^1)| \, dq^1 \ ,$$

with $\vec{r}(q^1_a)$, $\vec{r}(q^1_b)$ the extreme points of path $\gamma$.

(tensor:calculus:integrals:line:work)=
#### Work

Integrals

$$\int_{\vec{r} \in \gamma} F(\vec{r}) \cdot \hat{t}(\vec{r})$$

implicitly mean

$$\int_{\vec{r} \in \gamma} F(\vec{r}) \cdot \hat{t}(\vec{r}) = \int_{\vec{r} \in \gamma} F(\vec{r}) \cdot \hat{t}(\vec{r}) |d \vec{r}| = \int_{\vec{r} \in \gamma} F(\vec{r}) \cdot d \vec{r} \ ,$$

as $\hat{t} = \frac{d \vec{r}}{|d \vec{r}|}$.
Given a regular parametrization of the curve $\vec{r}(q^1)$ (with increasing $q^1$ so that $|dq^1| = dq^1$), and the differential $d \vec{r} = \vec{r}'(q^1) \, d q^1$, the integral can be written as an integral in the parameter $q^1$

$$\int_{q^1=q^1_a}^{q^1_b} F(\vec{r}(q^1)) \cdot \vec{r}'(q^1) \, dq^1$$

(tensor:calculus:integrals:surface)=
### Surface integrals

Given two coordinates $q^1, \, q^2$ describing a surface, $\vec{r}(q^1, q^2)$ the elementary surface with unit normal reads

$$\hat{n} \, dS = d \vec{r}_1 \times d \vec{r}_2 = \frac{\partial \vec{r}}{\partial q^1} \times \frac{\partial \vec{r}}{\partial q^2} \, dq^1 \, dq^2 \ ,$$

and the elementary surface thus reads

$$|dS| = |\hat{n} dS| = \left| \frac{\partial \vec{r}}{\partial q^1} \times \frac{\partial \vec{r}}{\partial q^2} \, dq^1 \, dq^2  \right|$$

(tensor:calculus:integrals:surface:density)=
#### Density

Integrals

$$\int_{\vec{r} \in S} F(\vec{r}) $$

implicitly mean

$$\int_{\vec{r} \in S} F(\vec{r}) = \int_{\vec{r} \in S} F(\vec{r}) |d S| \ .$$

Given regular parametrization of the surface, $\vec{r}(q^1, \, q^2), \ (q^1, q^2) \in Q^{12}$, the integral can be written as the multi-dimensional integral in coordinates $q^1, \ q^2$,

$$\int_{\vec{r} \in S} F(\vec{r}) = \int_{(q^1,q^2) \in Q^{12}} F(\vec{r}(q^1,q^2)) \left| \frac{\partial \vec{r}}{\partial q^1} \times \frac{\partial \vec{r}}{\partial q^2}  \, dq^1 \, dq^2 \right|$$

(tensor:calculus:integrals:surface:flux)=
#### Flux

Integrals

$$\int_{\vec{r} \in S} \hat{n}(\vec{r}) \cdot F(\vec{r}) $$

implicitly mean

$$\int_{\vec{r} \in S} \hat{n}(\vec{r}) \cdot F(\vec{r}) = \int_{\vec{r} \in S} \hat{n}(\vec{r}) \cdot F(\vec{r}) |dS| $$

Given regular parametrization of the surface, $\vec{r}(q^1, \, q^2), \ (q^1, q^2) \in Q^{12}$, the integral can be written as the multi-dimensional integral in coordinates $q^1, \ q^2$,

$$\int_{\vec{r} \in S} \hat{n}(\vec{r}) \cdot F(\vec{r}) = \int_{(q^1,q^2) \in Q^{12}} \frac{\partial \vec{r}}{\partial q^1} \times \frac{\partial \vec{r}}{\partial q^2} \cdot  F(\vec{r}(q^1,q^2))\, dq^1 \, dq^2 $$

(tensor:calculus:integrals:volume)=
### Volume

$$dV = \frac{\partial \vec{r}}{\partial q^1} \cdot \frac{\partial \vec{r}}{\partial q^2} \times \frac{\partial \vec{r}}{\partial q^3} \, dq^1 \, dq^2 \, d q^3 \ . $$ 

(tensor:calculus:integrals:volume:density)=
#### Density

Integrals

$$\int_{\vec{r} \in V} F(\vec{r})$$

implicitly mean

$$\int_{\vec{r} \in V} F(\vec{r}) = \int_{\vec{r} \in V} F(\vec{r}) \, |dV| \ .$$

Given regular parametrization of the volume, $\vec{r}(q^1, \, q^2, \, q^3), \ (q^1, q^2, q^3) \in Q$, the integral can be written as the multi-dimensional integral in coordinates $q^1, \, q^2, \, q^3$,

$$\int_{\vec{r} \in V} F(\vec{r}) |d V| = \int_{(q^1,q^2,q^3) \in Q} F(\vec{r}(q^1,q^2,q^3))  \left| \frac{\partial \vec{r}}{\partial q^1} \cdot \frac{\partial \vec{r}}{\partial q^2} \times \frac{\partial \vec{r}}{\partial q^3} \, dq^1 \, dq^2 \, d q^3 \right| \ .$$


(tensor:calculus:integrals:theorems)=
### Theorems

(tensor:calculus:integrals:theorems:gradient)=
#### Gradient theorem

$$\int_{V} \nabla f = \oint_{\partial V} f \hat{n}$$

(tensor:calculus:integrals:theorems:divergence)=
#### Divergence theorem

$$\int_{V} \nabla \cdot \vec{f} = \oint_{\partial V} \vec{f} \cdot \hat{n}$$

(tensor:calculus:integrals:theorems:curl)=
#### Curl theorem

$$\int_{S} \left[ \nabla \times \vec{f} \right] \cdot \hat{n} = \oint_{\partial S} \vec{f} \cdot \hat{t}$$

