(math:linear-algebra:matrix)=
# Matrices

$\mathbf{A} \in \mathbb{K}^{m,n} $ with usually $\mathbb{K}^{m,n} = \mathbb{R}^{m,n}$ or $\mathbb{C}^{m,n}$

**Hermitian matrix.** The Hermitian matrix $\mathbf{A}^*$ of a matrix $\mathbf{A}$ is the transpose and complex conjugate matrix (if $\mathbb{K} = \mathbb{C}$),

$$[\mathbf{A}^*]_{ij} = A^*_{ji} \ ,$$

with the notation of $a^*$ for the complex conjugate of a numerical quantity.

(math:linear-algebra:matrix:subspaces)=
## Subspaces

(math:linear-algebra:matrix:subspaces:range)=
### Range, Image

$$R(\mathbf{A}) = \left\{ \mathbf{y} \in \mathbb{K}^m \ | \ \exists \mathbf{x} \in \mathbb{K}^m \ , \text{ s.t. } \mathbf{A} \mathbf{x} = \mathbf{y} \right\}$$

The range of a matrix $\mathbf{A}$ is the linear space built on the columns of $\mathbf{A}$, since the operation $\mathbf{A} \mathbf{x}$ represents nothing but a linear combination of the columns of matrix.

(math:linear-algebra:matrix:subspaces:null)=
### Null, Kernel

$$K(\mathbf{A}) = \left\{ \mathbf{x} \in \mathbb{K}^n \ | \ \mathbf{A} \mathbf{x} = \mathbf{0} \right\}$$

(math:linear-algebra:thms)=
## Theorem

(math:linear-algebra:thms:RAperpKAh)=
### Orthogonality of $R(\mathbf{A})$ and $K(\mathbf{A^*})$

The following holds,

$$R(\mathbf{A}) \perp K(\mathbf{A^*}) \ ,$$

meaning that $\forall \mathbf{u} \in R(\mathbf{A})$ and $\forall \mathbf{v} \in K(\mathbf{A}^*)$, $\mathbf{u}^* \mathbf{v} = 0$.

```{dropdown} Proof.

$$\begin{aligned}
  \mathbf{u} & = \mathbf{A} \mathbf{x} \\
  \mathbf{0} & = \mathbf{A}^* \mathbf{v} 
\end{aligned}$$

and thus, premultiplication by $\mathbf{x}^*$ of the second relation gives

$$0 = \mathbf{x}^* \mathbf{0} = \underbrace{\mathbf{x}^* \mathbf{A}^*}_{=(\mathbf{A}  \mathbf{x})^* = \mathbf{u}^*} \mathbf{v} = \mathbf{u}^* \mathbf{v} \ .$$

```

This theorem becomes quite useful, e.g. for constrained linear systems and projections... (e.g. N-S, or other constrained linear systems...)

**todo** add links
