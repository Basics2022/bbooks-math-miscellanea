(math:schur)=
# Schur decomposition

Any square matrix $\mathbf{A} \in \mathbb{C}^{n,n}$ can be written as

$$\mathbf{A} = \mathbf{Q} \mathbf{U} \mathbf{Q}^* \ ,$$

with $\mathbf{U}$ upper triangular and $\mathbf{Q}$ unitary, s.t. $\mathbf{Q}^{-1} = \mathbf{Q}^*$.

```{dropdown} Proof by induction
:open:

This proof uses induction[^induction-ref] on the dimension of the matrix $\mathbf{A} \in \mathbb{C}^{n,n}$. For $n = 1$, the transformation is trivial

$$A = 1 \cdot A \cdot 1 \ .$$

Now, let's prove the relation for $n$, assuming that it's true for $n-1$. A vector $\mathbf{v}_1 \in \mathbb{C}$ s.t. $\mathbf{A} \mathbf{v}_1 = s_1 \mathbf{v}_1$ exists for some $s_1 \in \mathbb{C}$. Then it's possible to build a orthonormal basis of \mathbb{C}^{n}, complementing $\mathbf{v}_1$,

$$\mathbf{V} = \begin{bmatrix} \ \mathbf{v}_1 & \mathbf{v}_2 & \dots & \mathbf{v}_n \ \end{bmatrix} \ .$$

Evaluating the product $\mathbf{V}^* \mathbf{A} \mathbf{V}$,

$$\begin{aligned}
  \mathbf{V}^* \mathbf{A} \mathbf{V}
  & = \begin{bmatrix} \mathbf{v}_1^* \\ \mathbf{v}_2^* \\ \dots \\ \mathbf{v}_n^* \end{bmatrix} \mathbf{A} \begin{bmatrix} \ \mathbf{v}_1 & \mathbf{v}_2 & \dots & \mathbf{v}_n \ \end{bmatrix} = \\
  & = \begin{bmatrix} \mathbf{v}_1^* \\ \mathbf{v}_2^* \\ \dots \\ \mathbf{v}_n^* \end{bmatrix} \begin{bmatrix} \ \mathbf{A} \mathbf{v}_1 & \mathbf{A} \mathbf{v}_2 & \dots & \mathbf{A} \mathbf{v}_n \ \end{bmatrix} = \\
  & = \begin{bmatrix} \mathbf{v}_1^* \\ \mathbf{v}_2^* \\ \dots \\ \mathbf{v}_n^* \end{bmatrix} \begin{bmatrix} \ s_1 \mathbf{v}_1 & \mathbf{A} \mathbf{v}_2 & \dots & \mathbf{A} \mathbf{v}_n \ \end{bmatrix} = \\
  & = \begin{bmatrix}
    s_1 & \mathbf{v}_1^* \mathbf{A} \mathbf{v}_2 & \dots & \mathbf{v}_1^* \mathbf{A} \mathbf{v}_n \\
      0 & \mathbf{v}_2^* \mathbf{A} \mathbf{v}_2 & \dots & \mathbf{v}_2^* \mathbf{A} \mathbf{v}_n \\
  \dots & \dots                                  & \dots & \dots                                  \\
      0 & \mathbf{v}_n^* \mathbf{A} \mathbf{v}_2 & \dots & \mathbf{v}_n^* \mathbf{A} \mathbf{v}_n
    \end{bmatrix} = \\
  & = \begin{bmatrix} s_1 & \mathbf{a}_1^* \\ \mathbf{0} & \mathbf{A}_1 \end{bmatrix} = \mathbf{T}
\end{aligned}$$

Thus $\mathbf{A} = \mathbf{V} \mathbf{T} \mathbf{V}^*$. Induction assumes that $\mathbf{A}_1 = \mathbf{Q}_1 \mathbf{U}_1 \mathbf{Q}_1^*$, so that

$$\begin{aligned}
  \mathbf{A} 
  & = \mathbf{V} \mathbf{T} \mathbf{V}^* = \\
  & = \mathbf{V} \begin{bmatrix} s_1 & \mathbf{a}_1^* \\ \mathbf{0} & \mathbf{A}_1 \end{bmatrix} \mathbf{V}^* = \\
  & = \mathbf{V} \begin{bmatrix} s_1 & \mathbf{a}_1^* \\ \mathbf{0} & \mathbf{Q}_1 \mathbf{U}_1 \mathbf{Q}_1^* \end{bmatrix} \mathbf{V}^* = \\
  & = \underbrace{\mathbf{V} \begin{bmatrix} 1 & \mathbf{0}^* \\ \mathbf{0} & \mathbf{Q}_1 \ \end{bmatrix}}_{=\mathbf{Q}} \underbrace{\begin{bmatrix} s_1 & \mathbf{a}_1^* \\ \mathbf{0} & \mathbf{U}_1 \end{bmatrix}}_{= \mathbf{U}} \underbrace{\begin{bmatrix} 1 & \mathbf{0}^* \\ \mathbf{0} & \mathbf{Q}_1^* \end{bmatrix} \mathbf{V}^*}_{=\mathbf{Q}^*} = \\
  & = \mathbf{Q} \mathbf{U} \mathbf{Q}^* \ .
\end{aligned}$$

As the existence of Schur decomposition for $\mathbf{A}_1 \in \mathbb{C}^{n-1,n-1}$ implies the existence of Schur decomposition for $\mathbf{A} \in \mathbb{C}^{n,n}$, the proof is complete.

[^induction-ref]: **todo** Add a reference to induction in math notes, in sections about logics, either for [high-school](https://basics2022.github.io/bbooks-math-miscellanea-hs/intro.html) or in this personal notes. Find something in the old .pdf material.

```

```{dropdown} Lemma
:open:

For every matrix $\mathbf{A} \in \mathbb{C}^{n,n}$, there is a vector $\mathbf{v} \in \mathbb{C}^n$, $\mathbf{v} \ne \mathbf{0}$, so that $\mathbf{A} \mathbf{v} = a \mathbf{v}$, for some value of $a \in \mathbb{C}$. This relation holds for non-trivial vectors $\mathbf{v}$ if

$$\left( \mathbf{A} - s \mathbf{I} \right) \mathbf{v} = \mathbf{0} \ ,$$

i.e. $\mathbf{v} \in \text{Ker}\left( \mathbf{A} - s \mathbf{I} \right)$, i.e. $\text{Ker}\left( \mathbf{A} - s \mathbf{I} \right)$ is not empty.
This is true if

$$0 = \left| \mathbf{A} - s \mathbf{I} \right| \ .$$

This is a polynomial equation of degree $n$ and thus, for the [fundamental theorem of algebra](complex:algebra:fundamental-theorem), it has at least one complex solution, $s = \overline{s}$. For $s = \overline{s}$, a vector $\mathbf{v}$ satisfying $\mathbf{A} \mathbf{v} = \overline{s} \mathbf{v}$.

```

