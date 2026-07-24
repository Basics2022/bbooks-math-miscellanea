(complex:series)=
# Sequences and Series in the Complex Field

The extension of sequences and series from the real line $\mathbb{R}$ to the complex plane $\mathbb{C} \cong \mathbb{R}^2$ preserves many fundamental operational properties while introducing deeper geometric and analytic structures. Most notably, the equivalence between complex differentiability (**holomorphy**) and power series convergence (**analyticity**) forms the cornerstone of complex analysis.


(complex:series:numerical)=
## Complex Numerical Sequences and Series

(complex:series:numerical:sequence)=
### Complex Numerical Sequences

A complex sequence $\{z_n\}_{n \in \mathbb{N}} \subset \mathbb{C}$ can be decomposed into its real and imaginary components:

$$z_n = x_n + i y_n, \quad \text{where } x_n, y_n \in \mathbb{R}$$

(complex:series:numerical:sequence:convergence)=
#### Convergence
```{admonition} Definition: Convergence in $\mathbb{C}$

A sequence $\{z_n\}$ **converges** to $L = u + i v \in \mathbb{C}$ (written $\lim_{n \to \infty} z_n = L$) if:

$$\lim_{n \to \infty} |z_n - L| = 0 \ .$$

Or, with the $\espilon$-definition: given $\varepsilon > 0$, $\exists N$ s.t. $| z_n - L | < \varepsilon$ for $\forall n > N$.


```

Equivalently, convergence in $\mathbb{C}$ under the standard Euclidean metric can be written component-wise, with $z_n = x_n + i y_n$,

$$\lim_{n \to \infty} z_n = L \iff \left( \lim_{n \to \infty} x_n = u \quad \text{and} \quad \lim_{n \to \infty} y_n = v \right)$$

<!--
#### Cauchy Criterion
Since $\mathbb{C}$ equipped with the modulus metric $|z| = \sqrt{\text{Re}(z)^2 + \text{Im}(z)^2}$ is a **complete metric space** (a Cauchy space/ anach space over $\mathbb{C}$), a sequence $\{z_n\}$ converges if and only if it satisfies the Cauchy criterion:

$$\forall \varepsilon > 0, \, \exists N \in \mathbb{N} \quad \text{such that} \quad \forall n, m > N \implies |z_n - z_m| < \varepsilon$$

-->

(complex:series:numerical:series)=
### Complex Numerical Series

A complex infinite series is defined as the formal sum:

$$\sum_{n=0}^{+\infty} z_n, \quad z_n \in \mathbb{C}$$

It converges to $S \in \mathbb{C}$ if the sequence of partial sums $S_N = \sum_{n=0}^{N} z_n$ converges to $S$.

(complex:series:numerical:series:convergence)=
#### Convergence

**Convergence.** Using the [convergence of a sequence](complex:series:numerical:sequence:convergence), a series is convergent if the sequence of the partial sums $S_N = \sum_{n=0}^{N} z_n$ converges.

**Absolute Convergence:** The series $\sum z_n$ converges absolutely if the real-valued series of moduli converges:

$$\sum_{n=0}^{+\infty} |z_n| < +\infty$$

*Property:* Absolute convergence in $\mathbb{C}$ implies standard convergence.

**Conditional Convergence:** The series converges, but $\sum |z_n| = +\infty$. As an example:

$$1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + ...$$

```{admonition} Tests for absolute convergence
| Test | Statement |
| :--- | :--- |
| **Ratio Test** | If $\lim_{n \to \infty} \left\|\frac{z_{n+1}}{z_n}\right\| = L$, then: <br> • $L < 1 \implies$ Absolutely Convergent <br> • $L > 1 \implies$ Divergent |
| **Root Test** | If $\limsup_{n \to \infty} \sqrt[n]{\|z_n\|} = L$, then: <br> • $L < 1 \implies$ Absolutely Convergent <br> • $L > 1 \implies$ Divergent |
```

---

## Complex Sequences and Series of Functions

Let $\Omega \subseteq \mathbb{C}$ be an open set and let $\{f_n\}_{n \in \mathbb{N}}$ be a sequence of complex-valued functions $f_n: \Omega \to \mathbb{C}$.

### Convergence types of Sequences

1. **Pointwise Convergence:** $f_n \to f$ pointwise on $\Omega$ if for every $z \in \Omega$:

   $$\lim_{n \to \infty} |f_n(z) - f(z)| = 0$$

   (or for $\forall z \in \Omega$, $\forall \varepsilon > 0$, $\exists N$ so that $| f_n(z) - f(z) | < \varepsilon$ for $\forall n > N$.)

2. **Uniform Convergence:** $f_n \rightrightarrows f$ uniformly on $E \subseteq \Omega$ if:

   $$\lim_{n \to \infty} \sup_{z \in E} |f_n(z) - f(z)| = 0$$
   
   (or for $\forall \varepsilon > 0$, $\exists N$ so that $| f_n(z) - f(z) | < \varepsilon$ for $\forall n > N$, $\forall z \in \Omega$.)

3. **Locally Uniform (Compact) Convergence:** $f_n \to f$ uniformly on every compact subset $K \subset \Omega$.

---

### Weierstrass theorem

**todo** *Uncomment?*

---

**todo**

<!--
###The Rigidity of Complex Holomorphic Limits: Weierstrass's Theorem

In real analysis, a uniform limit of continuously differentiable ($C^1$) functions is continuous, but not necessarily differentiable. In complex analysis, the Cauchy Integral Formula enforces a much stronger rigidity.

```{admonition} Weierstrass's Theorem on Holomorphic Limits
:class: note
Let $\{f_n\}$ be a sequence of **holomorphic** functions on an open domain $\Omega \subset \mathbb{C}$.
If $f_n \to f$ **uniformly on every compact subset** $K \subset \Omega$, then:

1. The limit function $f(z)$ is **holomorphic** in $\Omega$.
2. The sequence of derivatives $\{f_n'\}$ converges compact-uniformly in $\Omega$ to $f'(z)$:
   $$f_n' \rightrightarrows f' \quad \text{on compacts } K \subset \Omega$$
```

*Proof Sketch:* By Morera's Theorem, if $\oint_\gamma f_n(z) \, dz = 0$ for every closed triangular contour $\gamma \subset \Omega$, uniform convergence allows interchanging the limit and the integral:
$$\oint_\gamma f(z) \, dz = \oint_\gamma \left(\lim_{n \to \infty} f_n(z)\right) dz = \lim_{n \to \infty} \oint_\gamma f_n(z) \, dz = 0$$
Hence, $f$ is holomorphic. Derivatives follow via Cauchy's Integral Formula for derivatives.

-->

<!--
## Complex Power Series

A complex power series centered at $z_0 \in \mathbb{C}$ is a function series of the form:

$$P(z) = \sum_{n=0}^{+\infty} a_n (z - z_0)^n, \quad a_n, z_0 \in \mathbb{C}$$

### Cauchy-Hadamard Theorem and the Radius of Convergence

The geometry of convergence for power series in $\mathbb{C}$ is defined by a disk centered at $z_0$.

```{admonition} Cauchy-Hadamard Theorem
Given the power series $\sum_{n=0}^{+\infty} a_n (z - z_0)^n$, define the **radius of convergence** $R \in [0, +\infty]$ by:

$$\frac{1}{R} = \limsup_{n \to \infty} \sqrt[n]{|a_n|}$$

Then:
1. **Inside the Disk ($|z - z_0| < R$):** The series converges **absolutely**, and converges **uniformly** on any closed disk $\{z : |z - z_0| \le r < R\}$.
2. **Outside the Disk ($|z - z_0| > R$):** The series **diverges** for all $z$.
3. **On the Boundary ($|z - z_0| = R$):** The behavior is subtle and varies point by point.
```

---

### Holomorphy and Distance to Singularities

Every complex power series represents a holomorphic function inside its open disk of convergence $D_R(z_0) = \{z \in \mathbb{C} : |z - z_0| < R\}$.

Conversely, any function $f(z)$ holomorphic in a domain $\Omega$ can be expanded in a unique Taylor series centered at any $z_0 \in \Omega$:

$$f(z) = \sum_{n=0}^{+\infty} \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n$$

```{admonition} The Singularity Distance Principle
:class: tip
The radius of convergence $R$ of the Taylor series of $f(z)$ centered at $z_0$ is precisely the **distance from $z_0$ to the nearest singularity** of $f(z)$ in the complex plane:

$$R = \text{dist}(z_0, \partial \Omega) = \min \{ |z_0 - z_{\text{sing}}| : f \text{ fails to be holomorphic at } z_{\text{sing}} \}$$
```

---

## Generalization: Laurent Series

When studying a function $f(z)$ near an isolated singularity $z_0$ (where $f$ is not holomorphic at $z_0$ itself), Taylor series cannot be applied. Instead, we use a **Laurent series**, which includes negative powers of $(z - z_0)$:

$$f(z) = \sum_{n=-\infty}^{+\infty} a_n (z - z_0)^n = \underbrace{\sum_{n=1}^{+\infty} \frac{a_{-n}}{(z - z_0)^n}}_{\text{Principal Part}} + \underbrace{\sum_{n=0}^{+\infty} a_n (z - z_0)^n}_{\text{Analytic / Regular Part}}$$

### Domain of Convergence
A Laurent series converges in an **annular domain** (ring) $A(z_0, r, R)$:

$$A(z_0, r, R) = \{ z \in \mathbb{C} : r < |z - z_0| < R \}$$

where:
* $R = \left(\limsup_{n \to \infty} \sqrt[n]{|a_n|}\right)^{-1}$ (governs convergence of positive powers).
* $r = \limsup_{n \to \infty} \sqrt[n]{|a_{-n}|}$ (governs convergence of negative powers).


### Classification of Singularities via Laurent Series

The structure of the Principal Part $\sum_{n=1}^{\infty} a_{-n} (z - z_0)^{-n}$ classifies the singularity at $z_0$:

1. **Removable Singularity:** All $a_{-n} = 0$ for $n \ge 1$ (Principal part is identically zero).
2. **Pole of Order $m$ ($m \ge 1$):** $a_{-m} \neq 0$, but $a_{-n} = 0$ for all $n > m$.
3. **Essential Singularity:** Infinitely many negative coefficients $a_{-n} \neq 0$ are non-zero (e.g., $e^{1/z}$ at $z_0 = 0$).

-->
