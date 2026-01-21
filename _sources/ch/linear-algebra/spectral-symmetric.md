(math:spectral:symmetric)=
# Spectral decomposition of symmetric matrices

In this section the spectral decomposition of symmetric matrices (or Hermitian, if defined on the complex field), $\mathbf{A} = \mathbf{A}^*$, is discussed.

```{prf:theorem} Spectral theorem of a symmetric matrix

A symmetric matrix has a spectral decomposition, with a complete set of unit orthogonal vectors and real eigenvalues,

$$\mathbf{A} = \mathbf{R} \mathbf{S} \mathbf{R}^* \ ,$$

with $\mathbf{R} = \left[ \ \mathbf{r}_1 \ | \ \dots \ | \mathbf{r}_n \ \right]$, and $\mathbf{r}_i^* \mathbf{r}_k = \delta_{ik}$, and $\mathbf{S} = \text{diag}\{ s_i \}$, $s_i \in \mathbb{R}$.

```

```{dropdown} Proof
:open:

**todo** *By construction...*

```

$$\begin{aligned}
  \mathbf{A}
  & = \mathbf{R} \mathbf{S} \mathbf{R}^* = \\
  & = \begin{bmatrix} \mathbf{r}_1 & \dots & \mathbf{r}_n \end{bmatrix} \text{diag}\{ s_i \} \begin{bmatrix} \mathbf{r}_1^* \\ \dots \\ \mathbf{r}_n^* \end{bmatrix} = \\
  & = \begin{bmatrix} s_1 \mathbf{r}_1 & \dots & s_n \mathbf{r}_n \end{bmatrix} \begin{bmatrix} \mathbf{r}_1^* \\ \dots \\ \mathbf{r}_n^* \end{bmatrix} = \\
  & = s_1 \mathbf{r}_1 \mathbf{r}_1^* + \dots + s_n \mathbf{r}_n \mathbf{r}_n^* \ .
\end{aligned}$$


**Properties.** 
- Left and right eigenvectors are the same. This immediately follows from the symmetry of the matrix and the definition of the left and right eigenvectors

   $$\begin{aligned}
     \mathbf{A} \mathbf{r}_k   & = s_k \mathbf{r}_k \\
     \mathbf{l}_j^* \mathbf{A} & = s^*_j \mathbf{l}_i^* \quad \rightarrow \quad \mathbf{A} \mathbf{l}_j = s_j \mathbf{l}_j \ ,
   \end{aligned}$$

- Eigenvalues are real, as
  
  $$0 = \mathbf{l}^*_k \left( \mathbf{A} \mathbf{r}_k \right) - \left( \mathbf{l}_k^* \mathbf{A} \right) \mathbf{r}_k = \left( s_k - s^*_k \right) \mathbf{l}^*_k \mathbf{r}_k = 2 \, \text{im}\{ s_k \} \underbrace{\mathbf{l}^*_k \mathbf{r}_k}_{ = | \mathbf{r}_k |^2} \ ,$$

  and thus $\text{im} \{ s_k \} = 0$.

- Eigenvectors with different eigenvalues are orthogonal, as

  $$0 = \mathbf{l}^*_j \left( \mathbf{A} \mathbf{r}_k \right) - \left( \mathbf{l}_j^* \mathbf{A} \right) \mathbf{r}_k = \left( s_k - s^*_j \right) \mathbf{l}^*_j \mathbf{r}_k \ ,$$

  and thus $\mathbf{l}^*_j \mathbf{r}_k = 0$ for $j \ne k$, if $s_j \ne s_k$. Left and right eigenvectors are orthogonal w.r.t. matrix $\mathbf{A}$ as well.



