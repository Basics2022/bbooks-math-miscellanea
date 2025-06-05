(tensor:algebra)=
# Tensor Algebra

This section introduces tensor algebra

```{warning}
This introduction is meant for **spaces with inner product** that allows to introduce quite naturally the useful concept of the *reciprocal basis* of a given basis of $\mathscr{V}$, belonging to the same space $\mathscr{V}$, somehow avoiding the complications coming from the introduction of dual space $\mathscr{V}^*$ and basis, and everything is required for that. 
```

## Vector space $\mathscr{V}$

A vector space is an algebraic structure with:
- a **set** $\mathscr{V}$, whose elements are called **vectors**, here indicated with bold symbols $\mathbf{v} \in \mathscr{V}$
- a **field** $K$ (usually $\mathbb{R}$ or $\mathbb{C}$), whose elements are calles **scalars**, 
- 2 **operations**, closed w.r.t. the set $\mathscr{V}$:
  - **vector sum**, $\mathbf{u} + \mathbf{v} \in \mathscr{V}$ for  $\forall \mathbf{u}, \ \mathbf{v} \in \mathscr{V}$
  - **multiplication of a scalar and a vector**, $a \mathbf{v} \in \mathscr{V}$ for $\forall a \in K, \ \mathbf{u} \in \mathscr{V}$

  with properties discussed below **todo**
...

### Operations (I)

#### Sum
...

#### Multiplication by a scalar
...

```{prf:definition} Linear combination

A linear combination of $n$ vectors $\{ \mathbf{v}_i \}_{i=1:n}$, $\mathbf{v}_i \in \mathscr{V}$, is the weighted sum

$$a^1 \mathbf{v}_1 + a^2 \mathbf{v}_2 + \dots + a^n \mathbf{v}_n = a^i \mathbf{v}_i \in \mathscr{V} \ ,$$

having used Einstein's summation convention over repeated indices. Here the position of the indices has no particular meaning, but it'll have soon in the following sections.

```

<!--
```{prf:definition} ...
```
-->

#### Inner product

```{admonition} The existence of an inner product is not a requirement of a vector space
:class: warning

...

```

An inner product in a vectors space $\mathscr{V}$ over field $K$ is an operation $\cdot: \mathscr{V} \times \mathscr{V} \rightarrow K$,

$$\mathbf{u} \cdot \mathbf{v} \ ,$$

with the following properties: **todo**


### Basis of a vector space $\mathscr{V}$
```{prf:definition} Basis

A basis is a minimal set of vectors of $\mathscr{V}$ that can represent all the elements of $\mathscr{V}$.

```

```{prf:defiiniiton} Dimension of a vector space

The dimension of a vector space $\mathscr{V}$ is the number of the elements of a basis of the space.

```


```{prf:definition} Reciprocal basis
In a inner product space, the reciprocal basis of a given basis $\{ \mathbf{b}_a \}_{a=1:d}$ is the set of vectors $\{ \mathbf{b}^{b} \}_{b=1:d}$, s.t.

$$\mathbf{b}^b \cdot \mathbf{b}_a = \delta_a^b \ .$$

```

```{prf:definition} "Metric tensor"

$$\begin{aligned}
  g_{ab} & := \mathbf{b}_a \cdot \mathbf{b}_b \\
  g^{ab} & := \mathbf{b}^a \cdot \mathbf{b}^b \\
\end{aligned}$$

```

The following holds

$$\begin{aligned}
  \mathbf{b}_a & = g_{ab} \mathbf{b}^b & (1) \\
  \mathbf{b}^a & = g^{ab} \mathbf{b}_b & (2) \\
\end{aligned}$$ (eq:metric-tensor:basis-transf)

```{dropdown} "Proof"

Taking the dot product with $\mathbf{b}_c$ of the relation {eq}`eq:metric-tensor:basis-transf`(1),

$$\mathbf{b}_c \cdot \mathbf{b}_a = g_{ab} \underbrace{\mathbf{b}_c \cdot \mathbf{b}^b}_{=\delta_c^b} = g_{ac} \ .$$

```

### Change of basis

Let $T_{a}^b$ the elements of the matrix of change of basis, representing the vectors of the basis $\{ \widetilde{b}_a \}$ as linear combinations of the vectors of the basis $\{ \mathbf{b}_b \}$,

$$\widetilde{\mathbf{b}}_b = T_b^a \mathbf{b}_a \ .$$

**Inverse transformation.** Let $\widetilde{T}$ be the elements of the inverse transformation,

$$\mathbf{b}_c = \widetilde{T}_{c}^{b} \widetilde{\mathbf{b}}_b = \widetilde{T}_{c}^{b}  T_b^a \mathbf{b}_a \ ,$$

and thus 

$$\widetilde{T}_{c}^{b}  T_b^a = \delta_{c}^a \ .$$

**Transformation of the reciprocal basis.** **todo**

#### Transformation of components

A vector $\mathbf{v}$ can be represented in different basis, as different linear combinations of the elements of those bases,

$$\mathbf{v} = v^{a} \mathbf{b}_a = \widetilde{v}^b \widetilde{\mathbf{b}}_b \ .$$

Given the rules of change of basis, the rule of transformation of components immediately follwos

$$\begin{aligned}
  & \widetilde{\mathbf{b}}_b = T_b^a \mathbf{b}_a                 && \widetilde{v}^b = \widetilde{T}^b_a v^a \\ 
  & \mathbf{b}_b = \widetilde{T}_{b}^{a} \widetilde{\mathbf{b}}_a &&           {v}^b = T^{b}_a \widetilde{v}^a
\end{aligned}$$

```{dropdown} Proof

$$\mathbf{v} = v^a \mathbf{b}_a = \underbrace{v^a \widetilde{T}^{b}_a}_{\widetilde{v}^b} \widetilde{\mathbf{b}}_b = \widetilde{v}^b \widetilde{\mathbf{b}}_b $$

or

$$\mathbf{v} = \widetilde{v}^b \widetilde{\mathbf{b}}_b = \underbrace{\widetilde{v}^b \widetilde{T}^{b}_c}_{v^c} \mathbf{b}_c = v^c \mathbf{b}_c$$

```

It's clear that the vectors of the bases and the components follow inverse transformations to preserve the **invariance of vector w.r.t. a change of basis**: the vector $\mathbf{v}$ doesn't change if we change our description of it, by changing a basis.

```{admonition} Matrix of change of basis as a tensor (**todo** maybe later? Tensor not introduced yet here)
:class: tip

The rule of transformation between different basis can be interpreted using dot product between tensors and vectors

$$\begin{aligned}
  \widetilde{\mathbf{b}}_b = T^{a}_b \mathbf{b}_a
  & = T^{a}_c \mathbf{b}_a \delta^c_b =  T^{a}_c \mathbf{b}_a \otimes \mathbf{b}^c \cdot \mathbf{b}_b = \left(  T^{a}_c \mathbf{b}_a \otimes \mathbf{b}^c \right) \cdot \mathbf{b}_b = \mathbb{T} \cdot \mathbf{b}_b \\
\end{aligned}$$
<!--  
  & = \delta^c_b T^{a}_c \mathbf{b}_a  = \mathbf{b}_b \cdot \mathbf{b}^c T^{a}_c \mathbf{b}_a  = \mathbf{b}_b \cdot \left(  T^{a}_c \mathbf{b}^c \otimes \mathbf{b}_a \otimes \mathbf{b}^c \right) = \mathbb{T} \cdot \mathbf{b}_b \\
-->

```


```{admonition} Inverse and transpose
:class: warning

Interpreting the indices of the transformation matrix as the indices of rows and columns of a 2x2 matrix, transformation of components involves the transpose of the inverse matrix, as the indices $a$, $b$ are swapped.

```

```{prf:example}

```

```{prf:example} Rotation

As the inverse of a rotation is its transpose, $\widetilde{T}^{b}_{a} = T^{a}_b$. So the rule of transformation of components follows the same rule of change of basis. As an example, let the transformation between two Cartesian bases be the rotation

$$
\begin{aligned}
 \widetilde{\mathbf{x}} & = \ \ \cos \theta \, \mathbf{x} + \sin \theta \, \mathbf{y} \\
 \widetilde{\mathbf{y}} & =   - \sin \theta \, \mathbf{x} + \cos \theta \, \mathbf{y}
\end{aligned}
\quad , \quad 
\begin{aligned}
 \mathbf{x} & =     \cos \theta \, \widetilde{\mathbf{x}} - \sin \theta \, \widetilde{\mathbf{y}} \\
 \mathbf{y} & =     \sin \theta \, \widetilde{\mathbf{x}} + \cos \theta \, \widetilde{\mathbf{y}}
\end{aligned}
$$

Let a vector 

$$\begin{aligned}
  \mathbf{v}
  & = v_x \mathbf{x} + v_y \mathbf{y} = \\
  & = v_x \left( \cos \theta \, \widetilde{\mathbf{x}} - \sin \theta \, \widetilde{\mathbf{y}} \right) + v_y \left( \sin \theta \, \widetilde{\mathbf{x}} + \cos \theta \, \widetilde{\mathbf{y}} \right) = \\
  & = \widetilde{v}_x \widetilde{\mathbf{x}} + \widetilde{v}_y \widetilde{\mathbf{y}} = \\
  & = \widetilde{v}_x \left( \cos \theta \, \mathbf{x} + \sin \theta \, \mathbf{y} \right) + \widetilde{v}_y \left( - \sin \theta \, \mathbf{x} + \cos \theta \, \mathbf{y} \right) 
\end{aligned}$$

and thus

$$
\begin{aligned}
  \widetilde{v}_x & = \ \ \cos \theta \, v_x + \sin \theta \, v_y \\
  \widetilde{v}_y & =   - \sin \theta \, v_x + \sin \theta \, v_y \\
\end{aligned}
\quad , \quad 
\begin{aligned}
  v_x & = \ \ \cos \theta \, \widetilde{v}_x - \sin \theta \, \widetilde{v}_y \\
  v_y & = \ \ \sin \theta \, \widetilde{v}_x + \sin \theta \, \widetilde{v}_y \\
\end{aligned}
$$


```

### Operations

#### Tensor product of vectors

$$\mathbf{v}_{(1)} \otimes \mathbf{v}_{(2)} \otimes \dots \otimes \mathbf{v}_{(r)}$$

or writing each vector as a linear combination of the elements of a basis $\mathbf{b}_a$,

$$\mathbf{v}_{(i)} = v_{(i)}^{a_i} \mathbf{b}_{a_i} \ , \dots$$

$$\begin{aligned}
  \mathbf{v}_{(1)} \otimes \mathbf{v}_{(2)} \otimes \dots \otimes \mathbf{v}_{(3)}
  & = \left(  v_{(1)}^{a_1} \mathbf{b}_{a_1} \right) \otimes \left(  v_{(2)}^{a_2} \mathbf{b}_{a_2} \right) \otimes \dots \otimes \left( v_{(r)}^{a_r} \mathbf{b}_{a_r} \right) = \\
  & = v_{(1)}^{a_1} \, v_{(2)}^{a_2} \, \dots \, v_{(r)}^{a_r} \mathbf{b}_{a_1} \otimes \mathbf{b}_{a_2} \otimes \dots \otimes \mathbf{b}_{a_r}
\end{aligned}$$

The result of the tensor product of $r$ vectors is a rank-$r$ tensor, $\mathbb{T}$, as it will be clear below, with components 

$$T^{a_1 a_2 \dots a_r} = v_{(1)}^{a_1} \, v_{(2)}^{a_2} \, \dots \, v_{(r)}^{a_r} \ .$$


## Space of tensors

```{prf:definition}
```

### Operations (I)

#### Sum

#### Multiplication by a scalar

```{admonition} Vector space of tensors
:class: tip

The set of tensors of a given rank with the operations of sum and multiplication by a scalar defined above forms a vector space.

```

### Basis

#### Change of basis and rule of transformation of components - classical definition of a tensor

$$\begin{aligned}
  \widetilde{\mathbf{b}}_{i_a} & = T_{i_b}^{i_a} \mathbf{b}_{i_b} \\
             \mathbf{b }_{i_a} & = \widetilde{T}_{i_a}^{i_b} \widetilde{\mathbf{b}}_{i_b} \\
\end{aligned}$$

$$\begin{aligned}
  \mathbf{A}
  & = A^{i_1 \dots i_p} \mathbf{b}_{i_1} \dots \mathbf{b}_{i_p} = \\
  & = A^{i_1 \dots i_p} \left( T_{i_1}^{j_1} \widetilde{\mathbf{b}}_{j_1} \right) \dots \left( T_{i_p}^{j_p} \widetilde{\mathbf{b}}_{j_p} \right) = \\
  & = A^{i_1 \dots i_p} T_{i_1}^{j_1} \dots  T_{i_p}^{j_p} \widetilde{\mathbf{b}}_{j_1} \dots \widetilde{\mathbf{b}}_{j_p} = \\
  & = \widetilde{A}^{j_1 \dots j_p} \widetilde{\mathbf{b}}_{j_1} \dots \widetilde{\mathbf{b}}_{j_p} \ ,
\end{aligned}$$

with 

$$\widetilde{A}^{j_1 \dots j_p} = A^{i_1 \dots i_p} T_{i_1}^{j_1} \dots  T_{i_p}^{j_p} \ .$$ (eq:tensor:comp-transf)

```{prf:definition} Classical definition of a tensor

Relation {eq}`eq:tensor:comp-transf` is the "historical" definition of a tensor, through the law of transformation of its components following a change of basis. 

```

### Operations (II)

#### Tensor product

The tensor product of a $p$-rank tensor $\mathbf{A}$ and a $q$-rank tensor $\mathbf{B}$ is the $(p+q)$-rank tensor $\mathbf{A} \otimes \mathbf{B} = \mathbf{A} \mathbf{B}$, that can be defined using component representation in a given basis,

$$\begin{aligned}
  \mathbf{A} \otimes \mathbf{B} 
  & = \left( A^{a_1 \dots a_p} \mathbf{b}_{a_1} \dots \mathbf{b}_{a_p} \right) \otimes \left( B^{b_1 \dots b_q} \mathbf{b}_{b_1} \dots \mathbf{b}_{b_q} \right) = \\
  & = A^{a_1 \dots a_{p-1} a_p} \, B^{b_1 \, b_2 \dots b_q} \mathbf{b}_{a_1} \dots \mathbf{b}_{a_p} \mathbf{b}_{b_1} \dots\mathbf{b}_{b_q}
\end{aligned}$$

#### Dot product

The dot product of a $p$-rank tensor $\mathbf{A}$ and a $q$-rank tensor $\mathbf{B}$ is the $(p+q-2)$-rank tensor $\mathbf{A} \cdot \mathbf{B}$, that can be defined using component representation in a given basis,

$$\begin{aligned}
  \mathbf{A} \cdot \mathbf{B} 
  & = \left( A^{a_1 \dots a_p} \mathbf{b}_{a_1} \dots \mathbf{b}_{a_p} \right) \cdot \left( B_{b_1 \dots b_q} \mathbf{b}^{b_1} \dots \mathbf{b}^{b_q} \right) = \\
  & = A^{a_1 \dots a_p} \, B_{b_1 \dots b_q} \mathbf{b}_{a_1} \dots \underbrace{ \mathbf{b}_{a_p} \cdot \mathbf{b}^{b_1} }_{= \delta_{a_p}^{b_1} } \dots \mathbf{b}^{b_q} = \\
  & = A^{a_1 \dots a_{p-1} k} \, B_{k \, b_2 \dots b_q} \mathbf{b}_{a_1} \dots \mathbf{b}_{a_{p-1}} \mathbf{b}^{b_2} \dots \mathbf{b}^{b_q}
\end{aligned}$$

#### Contraction

Contraction of a pair of index of a $p$-rank tensor $\mathbf{A}$ returns a $p-2$-rank tensor defined as

$$\begin{aligned}
  C_{a}^b \left( \mathbf{A} \right) 
  & = \dots \\
\end{aligned}$$

#### Exterior product
**todo** *see exterior algebra*

### Invariants

## Exterior algebra

$$\land$$

### Exterior product
Generalization of the vector product

