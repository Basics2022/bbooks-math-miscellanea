(tensor:algebra:isotropic-tensors)=
# Isotropic Tensors

This section provides the definition of isotropic tensors, the general forms of low-rank tensors (from rank-$2$ to rank-$4$ tensors) that may be useful in some fields of science (e.g. in continuum mechanics, in the constitutive law relating stress tensor with strain tensor in isotropic linear elastic media or stress tensor with strain velocity tensor in Newtonian fluids).

```{prf:definition} Isotropic tensor
:label: def-tensor-isotropic

An isotropic tensor is ...

```

The general form of the low-rank isotropic tensors in three-dimensional spaces, $\text{dim}\left( \mathscr{V} \right) = 3$ is proved using the definition of a rank-$r$ tensor as a multilinear map acting on $r$ vectors, and exploiting the invariance of some vector operations under rotations.

## Rank-$2$ isotropic tensors

The most general rank-$2$ isotropic tensor is a scalar multiple of the identity tensor, $\mathbf{A} = a \mathbf{I}$.

```{dropdown} Proof

The action of a rank-$2$ isotropic tensor in $\mathscr{V}$ on every pair of vectors $\mathbf{u}$, $\mathbf{v}$ can be a function of $\mathbf{u} \cdot \mathbf{v}$ only, i.e. the only vector operation:
- producing a scalar
- invariant under rotations
- involving the two vectors $\mathbf{u}$, $\mathbf{v}$ (i.e. the tensor is a multilinear map, $\mathbf{A}(\mathbf{u}, \mathbf{v})$)

Now, using coordinates, the general expression of the isotropic tensor is retrieved comparing the expression built under the isotropic assumption,

$$\begin{aligned}
  \mathbf{A}(\mathbf{u}, \mathbf{v}) 
  & = a \mathbf{u} \cdot \mathbf{v} = \\
  & = a \left( u^i \mathbf{b}_i \right) \cdot \left( v^j \mathbf{b}_j \right) = \\
  & = a u^i v^j g_{ij}
\end{aligned}$$

with the general expression of the action of the stress tensor on the vectors $\mathbf{u}$, $\mathbf{v}$

$$\mathbf{A}(\mathbf{u}, \mathbf{v}) = A_{ij} \mathbf{b}^i \mathbf{b}^j \left( u^k \mathbf{b}_k, v^l \mathbf{b}_l \right) = A_{ij} \delta^i_k \delta^j_l u^k v^l = A_{ij} u^i v^j \ ,$$

so that the *covariant components* read

$$A_{ij} = a g_{ij}$$

and the tensor can be written as

$$\begin{aligned}
  \mathbf{A} 
  = A_{ij} \mathbf{b}^i \mathbf{b}^j 
  & = a g_{ij}\mathbf{b}^i\mathbf{b}^j = \\
  & = a \mathbf{b}^i\mathbf{b}_i = a \delta_i^j \mathbf{b}^i \mathbf{b}_j = \\
  & = a g^{ij} \mathbf{b}_j \mathbf{b}_i = a g^{ij} \mathbf{b}_i \mathbf{b}_j \ .
\end{aligned}$$

```

```{dropdown} Components of the identity tensor
:open:

The identity tensor can be defined as a rank-$2$ tensor whose dot product with any arbitrary $\mathbf{v} \in \mathbf{V}$ gives

$$\mathbf{I} \cdot \mathbf{v} = \mathbf{v} \ .$$

The identity tensor can be written using any vector basis $\{ \mathbf{b}_i \}_i$, and its reciprocal $\{ \mathbf{b}^j \}$ as

$$\mathbf{I} = \mathbf{b}_i \mathbf{b}^i = \mathbf{b}^i \mathbf{b}_i = g_{ij} \mathbf{b}^i \mathbf{b}^j = g^{ij} \mathbf{b}_i \mathbf{b}_j \ ,$$

as it's immediate to prove by direct computation

$$\begin{aligned}
  \mathbf{b}_i \mathbf{b}^i \cdot \mathbf{v} & = \mathbf{b}_i \mathbf{b}^i \cdot \left( v^k \mathbf{b}_k \right) = \mathbf{b}_i \delta^i_k v^k = v^i \mathbf{b}_i = \mathbf{v} \\
  \mathbf{b}^i \mathbf{b}_i \cdot \mathbf{v} & = \mathbf{b}^i \mathbf{b}_i \cdot \left( v_k \mathbf{b}^k \right) = \mathbf{b}^i \delta_i^k v_k = v_i \mathbf{b}^i = \mathbf{v} \\
  g_{ij} \mathbf{b}^i \mathbf{b}^j \cdot \mathbf{v} & = g_{ij} \mathbf{b}^i \mathbf{b}^j \cdot \left( v^k \mathbf{b}_k \right) = \mathbf{b}^i \delta^j_k v^k g_{ij} = \mathbf{b}^i \underbrace{v^k g_{ik}}_{=v_i} = \mathbf{v}  \\
  g^{ij} \mathbf{b}_i \mathbf{b}_j \cdot \mathbf{v} & = g^{ij} \mathbf{b}_i \mathbf{b}_j \cdot \left( v_k \mathbf{b}^k \right) = \mathbf{b}_i \delta_j^k v_k g^{ij} = \mathbf{b}_i \underbrace{v_k g^{ik}}_{=v^i} = \mathbf{v}  \\
\end{aligned}$$

```

## Rank-$3$ isotropic tensors

**todo**

* Invariant object: $\mathbf{u} \times \mathbf{v} \cdot \mathbf{w}$
* Retrieve components, to find Levi-Civita symbols
* Discuss invariance under rotation and symmetry (pseudo-tensor)

## Rank-$4$ isotropic tensors

```{dropdown} Proof

The action of a rank-$4$ isotropic tensor in $\mathscr{V}$ on every set of 4 vectors $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$, $\mathbf{x}$ can be a function of the products of scalar products 

$$\begin{aligned}
  & \mathbf{u} \cdot \mathbf{v} \, \mathbf{w} \cdot \mathbf{x} \\
  & \mathbf{u} \cdot \mathbf{w} \, \mathbf{v} \cdot \mathbf{x} \\
  & \mathbf{u} \cdot \mathbf{x} \, \mathbf{v} \cdot \mathbf{w} \ ,
\end{aligned}$$

i.e. any possible combinations through scalar products of different vectors

- producing a scalar
- invariant under rotations
- involving all the 4 vectors $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$, $\mathbf{x}$ (i.e. the tensor is a multilinear map, $\mathbf{A}(\mathbf{u}, \mathbf{v}, \mathbf{w}, \mathbf{x})$)

Now, using coordinates, the general expression of the isotropic tensor is retrieved comparing the expression built under the isotropic assumption,

$$\begin{aligned}
  \mathbf{A}(\mathbf{u}, \mathbf{v}) 
  & = a \mathbf{u} \cdot \mathbf{v} \, \mathbf{w} \cdot \mathbf{x}
    + b \mathbf{u} \cdot \mathbf{w} \, \mathbf{v} \cdot \mathbf{x}
    + c \mathbf{u} \cdot \mathbf{x} \, \mathbf{v} \cdot \mathbf{w} = \\
  & = a \, g_{ij} g_{kl} u^i v^j w^k x^l
    + b \, g_{ij} g_{kl} u^i w^j v^k x^l
    + c \, g_{ij} g_{kl} x^i v^j v^k w^l = \\
  & = \left( a \ g_{ij} g_{kl} + b \ g_{ik} g_{jl} + c \ g_{il} g_{jk} \right) u^i v^j w^k x^l \ ,
\end{aligned}$$

with the general expression of the action of the stress tensor on the vectors $\mathbf{u}$, $\mathbf{v}$

$$\begin{aligned}
\mathbf{A}(\mathbf{u}, \mathbf{v})
& = A_{ijkl} \mathbf{b}^i \mathbf{b}^j \mathbf{b}^k \mathbf{b}^l \left( u^m \mathbf{b}_m, v^n \mathbf{b}_n,  u^p \mathbf{b}_p, v^q \mathbf{b}_q \right) = \\
& = A_{ijkl} \delta^i_m \delta^j_n \delta^k_p \delta^l_q u^m v^n w^p x^q = A_{ijkl} u^i v^j w^k x^l \ ,
\end{aligned}$$

so that the *covariant components* read

$$A_{ijkl} = a \ g_{ij} g_{kl} + b \ g_{ik} g_{jl} + c \ g_{il} g_{jk} \ ,$$

and the tensor can be written as

$$\begin{aligned}
  \mathbf{A} 
  = A_{ijkl} \mathbf{b}^i \mathbf{b}^j \mathbf{b}^k \mathbf{b}^l
  & = \left(  a \ g_{ij} g_{kl} + b \ g_{ik} g_{jl} + c \ g_{il} g_{jk} \right) \mathbf{b}^i \mathbf{b}^j \mathbf{b}^k \mathbf{b}^l = \\
\end{aligned}$$

```

```{dropdown} Linear isotropic relation between two rank-$2 \ $ tensors
:open:

$$\mathbf{A} = \mathbf{Q} : \mathbf{B}$$

$$\begin{aligned}
  \mathbf{Q} : \mathbf{B} 
  & = \left( Q_{ijkl} \mathbf{b}^i \mathbf{b}^j \mathbf{b}^k \mathbf{b}^l \right) : \left( B^{mn} \mathbf{b}_m \mathbf{b}_n  \right) = \\
  & = Q_{ijkl} B^{kl} \mathbf{b}^i \mathbf{b}^j = \\
  & = \left( a \, g_{ij} g_{kl}    + b \, g_{ik} g_{jl} + c \, g_{il} g_{jk} \right) B^{kl} \mathbf{b}^i \mathbf{b}^j = \\
  & = \left( a \, g_{ij} B_l^{\ l} + b \, B_{ij}        + c \, B_{ji} \right) \mathbf{b}^i \mathbf{b}^j = \\ 
  & = \left( a \, g_{ij} B_l^{\ l} + b \, B_{ij}        + c \, B_{ji} \right) \mathbf{b}^i \mathbf{b}^j = \\ 
\end{aligned}$$

depends on the three constant $a$, $b$, $c$ of the isotropic tensor.

```

```{dropdown} Linear isotropic relation between two symmetric rank-$2 \ $ tensors
:open:

If $B_{ij} = B_{ji}$, the double-dot product becomes

$$\mathbf{A} = \mathbf{Q} : \mathbf{B} = \left( a \, g_{ij} B_l^{\ l} + d \, B_{ij} \right) \mathbf{b}^i \mathbf{b}^j \ ,$$

 depends only on two constants $a$, $d$, having defined $d = b + c$. This is a common condition in continuum mechanics, where some constitutive law links two symmetric rank-$2$ tensors, like the stress and strain tensors for linear elastic media, or the stress and strain velocity tensors for Newtonian fluids.


```



