(math:linear-algebra:linear-sys)=
# Linear Systems

The linear system

$$\mathbf{A} \mathbf{x} = \mathbf{b}$$

with $\mathbf{A} \in \mathbb{R}^{m,n}$, $\mathbf{x} \in \mathbb{R}^n$, $\mathbf{b} \in \mathbb{R}^m$ has solution if there exists (at least) a vector $\widetilde{\mathbf{x}}$ whose product with $\mathbf{A}$ gives $\mathbf{b}$.

**Condition for the existence of a solution.**
A solution exists if $\mathbf{b}$ belongs to the [range of $\mathbf{A}$](math:linear-algebra:matrix:subspaces:range).

**Uniqueness of a solution.** If a solution $\widetilde{\mathbf{x}}$ exists, it's unique if the [kernel of $\mathbf{A}$](math:linear-algebra:matrix:subspaces:null) is empty, $K(\mathbf{A}) = \emptyset$. If the kernel is not empty,

$$\mathbf{b} = \mathbf{A}(\widetilde{\mathbf{x}} + \mathbf{u}) =  \mathbf{A}\widetilde{\mathbf{x}} + \underbrace{\mathbf{A} \mathbf{u}}_{=\mathbf{0}} \ ,$$

for $\forall \mathbf{u} \in K(\mathbf{A})$, and thus an infinite number of solutions exists. Given a vector basis of the kernel $\mathbf{K}(\mathbf{A})$, where $\text{dim}\left( K(\mathbf{A}) \right) = n_K$, $\{ \mathbf{u}_1, \dots, \mathbf{u}_{n_K} \}$, the general solution has $n_K$ "degrees of arbitrarieness", since the general solution of the problem is

$$\widetilde{\mathbf{x}} + \sum_{i = 1}^{n_K} a_i \mathbf{u}_i = \widetilde{\mathbf{x}} + \mathbf{U} \mathbf{a} \ .$$



**todo** treat under-, det-, over-determined lin sys


