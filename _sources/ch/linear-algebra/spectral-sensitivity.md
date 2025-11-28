(math:spectral:sensitivity)=
# Sensitivity of spectral decomposition

Matrices involved in a eigenvalue problem can be function of some parameters $p$. Sensitivity analysis evaluates first-order changes[^first-order-taylor] of eigenvalues and eigenvectors following a increment of the parameter $p = \overline{p} + \Delta p$,

$$\begin{aligned}
  s_i(p) & = s_i(\overline{p}) + \Delta p \, s_{i/p} (\overline{p}) + o(\Delta p) \\
  \mathbf{u}_i(p) & = \mathbf{u}_i(\overline{p}) + \Delta p \, \mathbf{u}_{i/p} (\overline{p}) + o(\Delta p) \ .
\end{aligned}$$

Here the terms $s_{i/p}(\overline{p})$ and $\mathbf{u}_{i/p}(\overline{p})$ are the **sensitivity** of the $i^{th}$ eigenvalue and eigenvector respectively w.r.t. to an increment $\Delta p$ of the variable $p$, starting from the reference configuration determined by the value $\overline{p}$ of the parameter.

**Rank of sensitivity.** Sensitivity of eigenvalue to a scalar parameter is a scalar quantity. Sensitivity of eivenvector to a scalar parameter is a vector quantity. If the parameter $\mathbf{p}$ is a vector quantity, sensitivity of eigenvalue w.r.t. $\mathbf{p}$ is a vector quantity, and sensitivity of eigenvector w.r.t. $\mathbf{p}$ is a matrix (or tensor, sometimes...) quantity.

[^first-order-taylor]: First order changes should be meant as derivatives w.r.t. the parameter $p$, evaluated for the reference value of $\overline{p}$ that appear in a Taylor series of the quantity of interest, $s(p_i) = s(\overline{p}_i) + \Delta p_k \, \partial_{p_k} s(\overline{p}_i) + o(\Delta p_i)$.

(math:spectral:sensitivity:first-order)=
## Generalized eigenvalue problem (first order)

Sensitivity of eigenvalue and right eigenvector to a parameter $p$ of matrices $\mathbf{A}(p)$, $\mathbf{B}(p)$ read

$$s_{i/p} = \mathbf{w}_i^* \left( \mathbf{A}_{/p} - s_i \mathbf{B}_{/p} \right) \mathbf{u}_i $$ (eq:eig:sens:first:eigenvalue)
$$\mathbf{u}_{i/p} = \sum_{a \notin \{i\}} \mathbf{w}_a^* \left( - \mathbf{A}_{/p} + s_i \mathbf{B} \right) \mathbf{u}_i \dfrac{1}{s_a - s_i} \mathbf{u}_a \ ,$$

having exploited normalization condition $\mathbf{w}_i^* \mathbf{B} \mathbf{u}_i = 1$, being $\mathbf{u}_i$ and $\mathbf{w}_i$ the[^multiple-ev] right and left eigenvectors associated with eigenvalue $s_i$.

[^multiple-ev]: Eigenvalues with algebraic and geometric multiplicity larger than one, $m_i^{(a)} = m_i^{(g)} > 1$, have the associated eigenvectors that spans a subspace of dimension $m_i$. In this subspace, it's always possible to define a set of orthogonal vectors. **todo** write it better; refer to introduction to spectral decomposition... **todo** treat sensitivity to parameters of eigenvalues and eigenvectors with multiplicity larger than one...

(math:spectral:sensitivity:first-order:right-left)=
### Right and left eigenvalue problem

Right and left eigenvalue problems are defined as

$$\begin{aligned}
  \mathbf{A} \mathbf{u}_i & = s_i \mathbf{B} \mathbf{u}_i \\
  \mathbf{v}_j^* \mathbf{A} & = s_j \mathbf{v}_j^* \mathbf{B} \\
\end{aligned}$$ (eq:eig:right-left)

```{prf:property} Eigenvalues of the right and left spectral problems

Left and right eigenvalue problems have the same set of eigenvalues.

```
```{dropdown} Proof
**todo**
```

```{prf:property} Orthogonality conditions of right and left spectral problems

Left and right eigenvectors associated with different eigenvalues are orthogonal w.r.t. the matrices of the system, i.e.

$$\begin{aligned}
  \mathbf{v}_j^* \mathbf{B} \mathbf{u}_i & = b^{(i)} \delta_{ij} \\
  \mathbf{v}_j^* \mathbf{A} \mathbf{u}_i & = a^{(i)} \delta_{ij} \ ,
\end{aligned}$$

with $a^{(i)} = s_i b^{(i)}$. Parameters $a^{(i)}$, $b^{(i)}$ are not uniquely determined, and one of them (or their combination) can be used in a **normalization condition** removing arbitrarieness of eigenvectors to a multiplicative factor.

```
```{dropdown} Proof

Starting from the left and right eigenvalue problems {eq}`eq:eig:right-left` for two different eigenvalues $s_i \ne s_j$, and multiplying (on the left) the right eigenvalue problem by $\mathbf{v}_j^*$ and multiplying (on the right) the left eigenvalue problem by $\mathbf{u}_i$

$$\begin{aligned}
  \mathbf{v}_j^* \mathbf{A} \mathbf{u}_i & = s_i \mathbf{v}_j^* \mathbf{B} \mathbf{u}_i \\
  \mathbf{v}_j^* \mathbf{A} \mathbf{u}_i & = s_j \mathbf{v}_j^* \mathbf{B} \mathbf{u}_i \\
\end{aligned}$$ (eq:eig:right-left:ortho:1)

and subracting the two equations

$$0 = (s_i - s_j) \mathbf{v}_j^* \mathbf{B} \mathbf{u}_i$$
$$\rightarrow \qquad 0 = \mathbf{v}_j^* \mathbf{B} \mathbf{u}_i \quad \text{ if $s_i \ne s_j$} \ ,$$ (eq:eig:right-left:ortho:B)

as the left-hand-side terms are the same, and $s_i \ne s_j$. As {eq}`eq:eig:right-left:ortho:B` holds, from {eq}`eq:eig:right-left:ortho:1` it also follows that

$$\rightarrow \qquad 0 = \mathbf{v}_j^* \mathbf{A} \mathbf{u}_i \quad \text{ if $s_i \ne s_j$} \ .$$ (eq:eig:right-left:ortho:A)

These relations don't hold for left and right eigenvectors associated with the same eigenvalues, and thus these conditions can be used as normalization conditions.

```

### Sensitivity of eigenvalue

The derivative w.r.t. parameter $p$ of the right eigenvalue problem

$$\mathbf{A}(p) \mathbf{u}_i(p) = s_i(p) \mathbf{B}(p) \mathbf{u}_i(p) \ ,$$

reads

$$0 = ( \mathbf{A}_{/p} - s_{i/p} \mathbf{B} - s_i \mathbf{B}_{/p}) \mathbf{u}_i + (\mathbf{A} - s_i \mathbf{B} ) \mathbf{u}_{i/p} \ .$$

Multiplying on the left by the left eigenvector $\mathbf{w}_i$, and recalling that the left eigenvalue problem reads $0 = \mathbf{w}_i^* \left( \mathbf{A} - s_i \mathbf{B} \right)$, the last term is identically zero and

$$0 = \mathbf{w}_i^*  ( \mathbf{A}_{/p} - s_{i/p} \mathbf{B} - s_i \mathbf{B}_{/p}) \mathbf{u}_i \ ,$$

so that it's possible to find the expression of the eigenvalue sensitivity as

$$
s_{i/p}
  = \dfrac{\mathbf{w}_i \left( \mathbf{A}_{/p} - s_i \mathbf{B}_{/p} \right) \mathbf{u}_i}{\mathbf{w}_i^* \mathbf{B} \mathbf{u}_i} 
  = \mathbf{w}_i \left( \mathbf{A}_{/p} - s_i \mathbf{B}_{/p} \right) \mathbf{u}_i \ ,
$$ (eq:eig:sens:first:eval)

where the last step exploits the normalization condition $\mathbf{w}_i^* \mathbf{B} \mathbf{u}_i = b^{(i)} = 1$.

### Sensitivity of eigenvector

The sensitivity of the eigenvector $\mathbf{u}_{i/p}$ is the solution of the linear system that can be obtained from the derivative of the eigenvalue problem,

$$(\mathbf{A} - s_i \mathbf{B} ) \mathbf{u}_{i/p} = \underbrace{- ( \mathbf{A}_{/p} - s_{i/p} \mathbf{B} - s_i \mathbf{B}_{/p}) \mathbf{u}_i}_{=:\mathbf{b}_i} \ ,$$

once the sensitivity of the eigenvector $s_{i/p}$ is known from expression {eq}`eq:eig:sens:first:eval`.

```{prf:property} Linear system is singular, $ \text{K}(A) = \{ \mathbf{u}_i \}$

Linear system is singular as $s_i$ is an eigenvalue of the problem, $|\mathbf{A} - s_i \mathbf{B}| = 0$, and the kernel of the matrix is the space spanned by the right eigenvectors associated with $s_i$, as

$$\left( \mathbf{A} - s_i \mathbf{B} \right) \mathbf{u}_i = \mathbf{0} \ .$$

```

As the matrix of the linear system is singular, the linear system has **no solution if** the right-hand side is not in the range of the matrix of the system, i.e. $\mathbf{b}_i \notin \text{R}(\mathbf{A}-s_i \mathbf{B})$.

Fortunately, the RHS belongs to the range of the matrix, $\mathbf{b}_i \in \text{R}(\mathbf{A}- s_i \mathbf{B})$, as it's proved in the box below.

```{prf:property} $\ \mathbf{b}_i \in \text{R}(\mathbf{A} - s_i \mathbf{B})$

If $\mathbf{b}_i$ belongs to $\text{R}(\mathbf{A} - s_i \mathbf{B})$, it's orthogonal to $\text{K}(\mathbf{A}^* - s_i^* \mathbf{B}^*)$ and viceversa, by theorem ... **todo** add link

Kernel of $\mathbf{A}^* - s_i^* \mathbf{B}^*$ is spanned by the left eigenvectors $\mathbf{v}_i$. Thus, using expression of the eigenvalue sensitivity in evaluating the product

$$\begin{aligned}
  \mathbf{v}_i^* \mathbf{b}_i 
  & = - \mathbf{v}_i^* \left(  \mathbf{A}_{/p} - s_{i/p} \mathbf{B} - s_i \mathbf{B}_{/p}) \mathbf{u}_i \right) = \\
  & = - \mathbf{v}_i^* \left(  \mathbf{A}_{/p} - s_i \mathbf{B}_{/p}) \mathbf{u}_i \right) + \mathbf{v}_i^* \left( \mathbf{A}_{/p} - s_i \mathbf{B}_{/p} \right) \mathbf{u}_i  \underbrace{\mathbf{v}_i^* \mathbf{B} \mathbf{u}_i}_{ = 1} = \\
  & = 0 \ ,
\end{aligned}$$

it's readily proved that $\mathbf{v}^*_i \mathbf{b}_i = 0$. **todo** treat the case where eigenvalue multiplicity is larger than 1.

```

As the singular linear system has at least a solution, it has infinite solution as the kernel of the matrix is not empty. If $\widetilde{\mathbf{u}_{/p}}$ is a solution of the system, adding a linear combination of the vectors of $\text{K}(\mathbf{A} - s_i \mathbf{B}) = \{ \mathbf{u}_i \}$ produces a solution as well,

$$\widetilde{\mathbf{u}_{i/p}} + \mathbf{U}_i \boldsymbol{\beta} \ ,$$

as $(\mathbf{A} - s_i \mathbf{B}) \mathbf{U}_i = \mathbf{0}$, being $\mathbf{U}_i$ the matrix whose columns are the right eigenvectors $\mathbf{u}_i$ associated with eigenvalue $s_i$, spanning the kernel of the matrix.

In order to remove this arbitrariness, it's possible to introduce the orthogonality condition $\mathbf{V}_i^* \mathbf{B} \widetilde{\mathbf{u}_{i/p}} = \mathbf{0}$, setting the coefficients of the linear combination of the vectors of the kernel $\boldsymbol\beta = \mathbf{0}$.

```{prf:property} Augmented linear system

$$\begin{bmatrix} \mathbf{A} - s_i \mathbf{B} &  \mathbf{U}_i \\ \mathbf{V}_i^* \mathbf{B} & \mathbf{0} \end{bmatrix}
 \begin{bmatrix} \widetilde{\mathbf{u}_{i/p}} \\ \boldsymbol{\beta} \end{bmatrix} = \begin{bmatrix} \mathbf{b}_i \\ \mathbf{0} \end{bmatrix}
$$

If everything goes right, the coefficients $\boldsymbol{\beta}$ must be zero.


```

```{prf:property} Decomposition of the soluton using the modal basis

Writing the solution as a linear combination of the right eigenvectors,

$$\widetilde{\mathbf{u}_{i/p}} = \mathbf{U}_{\notin i} \boldsymbol\alpha + \mathbf{U}_i \boldsymbol\beta \ ,$$

it's possible to solve for $\boldsymbol\alpha$ and for $\boldsymbol\beta$ and then retrieve the solution of the underdetermined linear system. Projecting the linear system on $\mathbf{V}_{\notin i}$, and prescibing the orthogonality condition $\mathbf{V}_i^* \mathbf{B} \widetilde{\mathbf{u}_{i/p}} = \mathbf{0}$ on the solution, two decoupled sets of equations for $\boldsymbol\alpha$ and $\boldsymbol\beta$ appears,

$$\left\{ \begin{aligned}
 &  \mathbf{V}_{\notin i}^* \left( \mathbf{A} - s_i \mathbf{B} \right) \mathbf{U}_{\notin i} \boldsymbol\alpha = \mathbf{V}_{\notin i}^* \mathbf{b}_i \\
 & \mathbf{V}_i^* \mathbf{B} \mathbf{U}_i \boldsymbol{\beta} = \mathbf{0} \ ,
\end{aligned}\right.$$

as $\left( \mathbf{A} - s_i \mathbf{B} \right) \mathbf{U}_i = \mathbf{0}$ and $\mathbf{V}_{i}^* \mathbf{B} \mathbf{U}_{\notin i} = \mathbf{0}$. Exploiting diagonalization properties, the system can be written as two uncoupled diagonal systems

$$\left\{ \begin{aligned}
 &  \text{diag} \left\{ a^{(j) \notin i} - s_i b^{(j) \notin i} \right\} \boldsymbol\alpha = \mathbf{V}_{\notin i}^* \mathbf{b}_i \\
 &  \text{diag} \left\{ b^{(i)} \right\} \boldsymbol{\beta} = \mathbf{0} \ ,
\end{aligned}\right.$$

or, exploiting normalization condition $\mathbf{v}_i^* \mathbf{B} \mathbf{u}_i = 1$, and thus $b^{(j)} = 1$ and $a^{(j)} = s_j$,

$$\left\{ \begin{aligned}
 &  \text{diag} \left\{ s_{j \notin i} - s_i \right\} \boldsymbol\alpha = \mathbf{V}_{\notin i}^* \mathbf{b}_i \\
 &  \mathbf{I} \, \boldsymbol{\beta} = \mathbf{0} \ ,
\end{aligned}\right.$$

The solution reads

$$\left\{ \begin{aligned}
 & \boldsymbol\alpha = \text{diag} \left\{ \dfrac{1}{ s_{j \notin i} - s_i } \right\} \mathbf{V}_{\notin i}^* \mathbf{b}_i \\
 & \boldsymbol{\beta} = \mathbf{0} \ ,
\end{aligned}\right.$$

and thus

$$\begin{aligned}
  \widetilde{\mathbf{u}}_{i/p}
  & = \mathbf{U}_{\notin i} \text{diag} \left\{ \dfrac{1}{ s_{j \notin i} - s_i } \right\} \mathbf{V}_{\notin i}^* \mathbf{b}_i  = \\
  & = \mathbf{U}_{\notin i} \text{diag} \left\{ \dfrac{1}{ s_{j \notin i} - s_i } \right\} \mathbf{V}_{\notin i}^* (- ( \mathbf{A}_{/p} - s_{i/p} \mathbf{B} - s_i \mathbf{B}_{/p}) \mathbf{u}_i)  = \\
  & = \mathbf{U}_{\notin i} \text{diag} \left\{ \dfrac{1}{ s_{j \notin i} - s_i } \right\} \mathbf{V}_{\notin i}^* (- ( \mathbf{A}_{/p} - s_i \mathbf{B}_{/p}) \mathbf{u}_i)  = \\
  & = \sum_{j \notin i} \dfrac{ \mathbf{v}_{j}^* ( - \mathbf{A}_{/p} + s_i \mathbf{B}_{/p}) \mathbf{u}_i }{ s_{j} - s_i } \mathbf{u}_{j} \ .
\end{aligned}$$

```

```{dropdown} Some algebra with components
:open:

$$\begin{aligned}
  u^{i}_{a/p}
  & = \sum_{b \ne i} u_{a}^{(b)} \delta_{bc} D^{(c)} v^{(c) \ *}_d b^{(i)}_d = \\
  & = \sum_{b \ne i} u_{a}^{(b)} \delta_{bc} D^{(c)} v^{(c) \ *}_d M_{de} u^{(i)}_e = \\
  & = \sum_{b \ne i} u_{a}^{(b)} D^{(b)} v^{(b) \ *}_d M_{de} u^{(i)}_e = \\
  & = \sum_{b \ne i} C^{b,i} u_{a}^{(b)} \ ,
\end{aligned}$$

with $C^{b,i} = D^{(b)} v^{(b) \ *}_d M_{de/p} u^{(i)}_e = \frac{\mathbf{v}^*_b \mathbf{M} \mathbf{u}_i}{s_b - s_i}$, and $\mathbf{M} = - \mathbf{A}_{/p} + s_i \mathbf{B}_{/p}$.

```


(math:spectral:sensitivity:second-order)=
## Generalized eigenvalue problem (second order)

### Right and left eigenvalue problem

