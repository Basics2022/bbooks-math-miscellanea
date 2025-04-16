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

#### Two useful lemmas
The next lemma forms the foundation of the well-known [divergence theorem](tensor:calculus:integrals:theorems:divergence) and [gradient theorem](tensor:calculus:integrals:theorems:gradient):  
the proof of these two theorems is based on a straightforward repeated use of this lemma.  
Given how simple this lemma is and how frequently it is applied in writing balances and, more generally, in integration by parts, it is very convenient to remember this simple result.

```{prf:theorem} Lemma 1.
:label: lemma-1

Under the assumptions of [Green's lemma in the plane](multivariable-calculus:green-lemma),

$$
  \int_V \frac{\partial A}{\partial x_i} = \oint_S A n_i
$$
```

```{dropdown} Proof
The reasoning closely follows the one used for the proof of [Green's lemma in the plane](multivariable-calculus:green-lemma).  
For ${\partial A}/{\partial z}$:

$$\begin{aligned}
\int_V \frac{\partial A}{\partial z} = &
\int_R \int_{z = f_1(x,y)}^{z = f_2(x,y)} \frac{\partial A}{\partial z} dz dx dy = \\
= & \int_R [A(x,y,f_2(x,y)) - A(x,y,f_1(x,y))] dx dy
\end{aligned}
$$

The most complex step is transitioning from the integral over $(x,y) \in R$ to the surface integral over $S$, the boundary of volume $V$: the infinitesimal area element $dR$ in the xy-plane is equal to $dR = dx dy$; the drawing and the proof refer to a *simple* volume (as in the case of Green's lemma in the plane, the results can be generalized to domains of arbitrary shape).  
It is possible to divide the surface $S$ into two "halves" $S^+: z = f_2(x,y)$ and $S^-: z = f_1(x,y)$ such that  
$S^+ \cup S^- = S$, and the outward normal has positive and negative z-components respectively ($S^+: \mathbf{\hat{n}}\cdot\mathbf{\hat{z}}>0$, $S^-: \mathbf{\hat{n}} \cdot\mathbf{\hat{z}}<0$).  
The surface element $dR$ is also the projection of the surface element $dS$ onto the xy-plane: in general, $dS$ will not be parallel to the xy-plane and thus will be larger than $dR$. It's not difficult to show that:

$$
 dx dy = dR =
 \begin{cases}
   dS \mathbf{\hat{z}} \cdot \mathbf{\hat{n}}  & \text{on $S^+$} \\
  - dS \mathbf{\hat{z}} \cdot \mathbf{\hat{n}}  & \text{on $S^-$} \\
 \end{cases}
$$

We can now continue the proof:

$$
\begin{aligned}
 & \int_R [A(x,y,f_2(x,y)) - A(x,y,f_1(x,y))] dx dy =   \\
 & \quad = \int_{S^+} A \mathbf{\hat{n}} \cdot\mathbf{\hat{z}} dS + \int_{S^-} A \mathbf{\hat{n}} \cdot\mathbf{\hat{z}} dS = \\
 & \quad =  \oint_S A \mathbf{\hat{z}} \cdot \mathbf{\hat{n}} dS = \\
 & \quad =  \oint_S A n_z dS
\end{aligned}
$$
```

Just as the previous lemma forms the basis for the proof of the [gradient theorem](tensor:calculus:integrals:theorems:gradient) and the [divergence theorem](tensor:calculus:integrals:theorems:divergence),  
the following lemma forms the basis for the proof of the [curl theorem](tensor:calculus:integrals:theorems:curl).

```{prf:theorem} Lemma 2.
:label: lemma-2

Under the assumptions of [Green's lemma in the plane](multivariable-calculus:green-lemma),

$$
  \int_S [\mathbf{\nabla} \times (A \mathbf{\hat{e}_i})] \cdot \mathbf{\hat{n}} = \oint_{\gamma} A dx_i
$$
```

```{dropdown} Proof
For $A\mathbf{\hat{e}_x}$, we have ${\nabla} \times (A \mathbf{\hat{e}_x}) =
{\partial A}/{\partial z} \mathbf{\hat{e}_y} - {\partial A}/{\partial y} \mathbf{\hat{e}_z}$.
The surface $S$ is written in parametric form as: $\mathbf{r} = x\mathbf{\hat{e}_x} +
y\mathbf{\hat{e}_y} + z(x,y)\mathbf{\hat{e}_z}$. The vector ${\partial \mathbf{r}}/{\partial y} = \mathbf{\hat{e}_y} +
{\partial z}/{\partial y} \mathbf{\hat{e}_z} $ is tangent to the surface $S$ and hence perpendicular to the normal $\mathbf{\hat{n}}$:

$$
\begin{aligned}
0 = \mathbf{\hat{n}} \cdot \left(\mathbf{\hat{e}_y} +
\frac{\partial z}{\partial y} \mathbf{\hat{e}_z} \right)
\end{aligned}
$$

Now writing $[\mathbf{\nabla} \times (A \mathbf{\hat{e}_x})] \cdot \mathbf{\hat{n}}$:

$$
 [\mathbf{\nabla} \times (A \mathbf{\hat{e}_x})] \cdot \mathbf{\hat{n}} =
  \frac{\partial A}{\partial z} \mathbf{\hat{e}_y} \cdot \mathbf{\hat{n}}
   - \frac{\partial A}{\partial y} \mathbf{\hat{e}_z}\cdot \mathbf{\hat{n}} =
  - \left[ \frac{\partial A}{\partial z} \frac{\partial z}{\partial y} +
  \frac{\partial A}{\partial y}  \right] \mathbf{\hat{e}_z}\cdot \mathbf{\hat{n}}
$$

Recognizing that $\frac{\partial A(x,y,z(x,y))}{\partial y} = \frac{\partial A}{\partial z} \frac{\partial z}{\partial y} +
  \frac{\partial A}{\partial y}$, we can write:

$$
 \int_S [\mathbf{\nabla} \times (A \mathbf{\hat{e}_x})] \cdot \mathbf{\hat{n}} =
 - \int_S \frac{\partial A}{\partial y} \underbrace{\mathbf{\hat{e}_z}\cdot \mathbf{\hat{n}} dS}_{dR = dx dy} =
 - \int_R \frac{\partial A}{\partial y} dx dy = \int_\gamma A dx
$$
```




(tensor:calculus:integrals:theorems:gradient)=
#### Gradient theorem

...**todo** *assumptions*...

$$\int_{V} \nabla f = \oint_{\partial V} f \hat{n}$$

```{dropdown} Proof for simple domains $\ V$
:open:

This result immediately follows from Lemma 1 {prf:ref}`lemma-1`

$$\oint_{\partial V} f \hat{n} = \hat{x}_i  \oint_{\partial V} f n_i = \hat{x}_i \int_{V} \partial_i f =  \int_{V} \hat{x}_i \partial_i f = \int_{V} \nabla \vec{f} \ , $$

having (1) exploited the freedom to put unit vectors of the Cartesian basis inside the integrals, as they're unifrom - constant in space -, and (2) recognized the expression of the [gradient of a scalar field expressed using Cartesian coordinates](tensor:calculus:cartesian:differential-operators:gradient), as shown in {prf:ref}`cartesian:gradient:scalar`.

<!--
Here the surface integral is evaluated using Cartesian coordinates, and each component is computed separately.
The surface integral of the $z$-component can be written as the contribution of an upper and a lower surface, having splitted the surface $\partial V$ is splitted in an upper and lower surface depending on the sign of the projection of the local unit normal vector $\hat{n}$ with the unit vector $\hat{z}$ associated with the $z$-coordinate of a set of Cartesian coordinates $x,y,z$. Each elementary contribution of this pair of surface, can be parametrized using $x, y$ coordinates, and the 

$$\begin{aligned}
  \hat{z} \cdot \oint_S f \hat{n} = \oint_{S} f n_z 
  & = \int_{S_z^+} f n_z + \int_{S_z^-} f n_z = \\
  & = \int_{\Omega_{x,y}} \big( f(x,y,z^+(x,y)) - f(x,y,z^-(x,y)) \big) dx dy = && (1) \\
  & = \int_{\Omega_{x,y}} \int_{z={z^-(x,y)}}^{z^+(x,y)} \dfrac{\partial}{\partial z} f(x,y,z) \, dz \, dx \, dy = && (2) \\
  & = \int_{\vec{r} \in V} \dfrac{\partial}{\partial z} f(x,y,z) \ .
\end{aligned}$$

having (1) recognized the integral in $z$ between the lower and upper surfaces $z^-(x,y)$, $z^+(x,y)$, and the volume integral evaluated with a parametrization with Cartesian coordinates. 

Repeating the same process for $x$ and $y$ coordinates the desired result is proved, explicitly

$$\begin{aligned}
  \oint_{\partial V} f \hat{n}
  & = \hat{x} \hat{x} \cdot \oint_{\partial V} f \hat{n} +  \hat{y} \hat{y} \cdot \oint_{\partial V} f \hat{n} + \hat{z} \hat{z} \cdot \oint_{\partial V} f \hat{n} = \\
  & = \hat{x} \int_V \partial_x f +  \hat{y} \int_V \partial_y f + \hat{z} \int_V \partial_z f = && (1) \\
  & = \int_V \left( \hat{x} \partial_x f +  \hat{y} \partial_y f + \hat{z}  \partial_z f \right) = \int_V \nabla f && (2) \ ,
\end{aligned}$$

having (1) exploited the freedom to put unit vectors of the Cartesian basis inside the integrals, as they're unifrom - constant in space -, and (2) recognized the expression of the [gradient of a scalar field expressed using Cartesian coordinates](tensor:calculus:cartesian:differential-operators:gradient), as shown in {prf:ref}`cartesian:gradient:scalar`.
-->

```

(tensor:calculus:integrals:theorems:divergence)=
#### Divergence theorem

...**todo** *assumptions*...

$$\int_{V} \nabla \cdot \vec{f} = \oint_{\partial V} \vec{f} \cdot \hat{n}$$

```{dropdown} Proof
:open:

This result immediately follows from Lemma 1 {prf:ref}`lemma-1`

$$\oint_{\partial V} \vec{f} \cdot \hat{n} =  \oint_{\partial V} f_i n_i = \int_{V} \partial_i f_i =  \int_{V} \nabla  \cdot \vec{f} \ , $$

having (1) exploited the freedom to put unit vectors of the Cartesian basis inside the integrals, as they're unifrom - constant in space -, and (2) recognized the expression of the [divergence of a vector field expressed using Cartesian coordinates](tensor:calculus:cartesian:differential-operators:divergence), as shown in {prf:ref}`cartesian:divergence:vector`.

<!--
Using Cartesian coordinates to write the scalar product 

$$\vec{f} \cdot \hat{n} = f_x n_x + f_y n_y + f_z n_z \ ,$$

and repeating the same procedure used in the proof of the [gradient theorem](tensor:calculus:integrals:theorems:gradient) for each term in the sum, the proof immediately follows

$$\begin{aligned}
  \oint_{\partial V} \vec{f} \cdot \hat{n} 
  & =  \oint_{\partial V} \big( f_x n_x + f_y n_y + f_z n_z  \big) = \\
  & =  \int_{V} \big( \partial_x f_x + \partial_y f_y + \partial_z f_z \big) = \int_V \nabla \cdot \vec{f} \ .
\end{aligned}$$

having recognized the expression of the [divergence of a vector field expressed using Cartesian coordinates](tensor:calculus:cartesian:differential-operators:divergence), as shown in {prf:ref}`cartesian:divergence:vector`.
-->

```

(tensor:calculus:integrals:theorems:curl)=
#### Curl theorem

...**todo** *assumptions*...

$$\int_{S} \left[ \nabla \times \vec{f} \right] \cdot \hat{n} = \oint_{\partial S} \vec{f} \cdot \hat{t}$$

```{dropdown} Proof
:open:

This proof seamlessly follows from Lemma {prf:ref}`lemma-2`, applied to all the Cartesian contributions of the vector field

$$\vec{f} = f_x \hat{x} + f_y \hat{y} + f_z \hat{z} \ ,$$

as

$$\int_S \left( \nabla \times \vec{f} \right) \cdot \hat{n} = \int_S \left( \nabla \times f_i \hat{x}_i \right) \cdot \hat{n} = \oint_{\partial S} f_i t_i = \oint_{\partial S} \vec{f} \cdot \hat{t} \ .$$



<!--
is performed using Cartesian coordinates, and evaluating the curl of each component of the vector field 

$$\vec{f} = f_x \hat{x} + f_y \hat{y} + f_z \hat{z} \ ,$$

at a time and exploting linearity to put together these results. Let's evaluate the surface integral for a vector field $f_z \hat{z}$

$$\begin{aligned}
  \int_S \hat{n} \cdot \left( \nabla \times ( f_z \hat{z} ) \right) 
  & = \int_S \left( n_x \hat{x} + n_y \hat{y} + n_z \hat{z} \right) \cdot \left( \hat{x} \partial_y f_z - \hat{y} \partial_x f_z \right) =  \\
  & = \int_S \left( n_x \partial_y f_z - n_y \partial_x f_z \right) = && (1) \\
  & = \int_{\Omega_{yz}} \partial_y f_z \, dy \, dz - \int_{\Omega_{xz}} \partial_x f_z  \, dx \, dz = && (2) \\
  & = \int_{\partial \Omega_{yz}} f_z \, dz + \int_{\partial \Omega_{xz}} f_z \, dz
\end{aligned}$$
-->

```

