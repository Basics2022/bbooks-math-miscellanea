(math:matrix-factorization)=
# Matrix factorizations

- **Singular Value Decomposition (SVD)**
- **Spectral decomposition** Eigenvalues, eigenvectors; Jordan canonical formula...

(math:matrix-factorization:ev:gershgorin)=
## Gershgorin circle theorem

Let $\mathbf{A}$ a complex $n,n$ matrix. Let $R_i = \sum_{j \ne i} |a_{ij}|$, and $D(a_{ii}, R) \subseteq \mathbb{C}$ the closed disc centered at $a_{ii}$ with radius $R_i$ in the complex plane.

Every eigenvalue of $\mathbf{A}$ lies within at least one of the Gershgorin discs $D(a_{ii}, R_i)$.

```{dropdown} Proof
:open:

Let $\lambda$ an eigenvalue of $\mathbf{A}$. Thus, it exsits a vector $\mathbf{v}$ s.t. $\mathbf{A} \mathbf{v} = \lambda \mathbf{v}$, or

$$\sum_{j} a_{ij} v_j = \lambda v_i \ .$$

Moving $a_{ii}$ from the LHS to the RHS, it follows

$$\sum_{j \ne i} a_{ij} v_j = \left( \lambda - a_{ii} \right) v_i \ .$$

Selecting $i$ s.t. $|v_i| \ge |v_j|$, $\forall j$ it follows that

$$|\lambda - a_{ii}| = \left| \sum_{j \ne i} a_{ij} \frac{v_j}{v_i} \right| \le  \sum_{j \ne i} \left| a_{ij} \frac{v_j}{v_i} \right| \le \sum_{j \ne i} | a_{ij} | \le R_{i} \ .$$

```

(math:matrix-factorization:ev:spectral-radius)=
## Spectral radius

Spectral radius of a matrix $\mathbf{A}$ is defined as the maximum of the absolute value of its eigenvalues

$$\rho(\mathbf{A}) = \max |\lambda(\mathbf{A})| \ .$$



- **QR**
- **LU**
- **Schur**
- **Cholesky** Symmetric positive definite matrices have Choleski decomposition,

   $$\mathbf{M} = \mathbf{L} \mathbf{L}^* \ ,$$

   with $\mathbf{L}$ lower triangular matrix. And thus quite easy to "invert", for solving linear systems.
