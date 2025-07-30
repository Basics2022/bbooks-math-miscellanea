(optimization)=
# Optimization

- **Gradient-based methods**, and Hessian based, for continuos functions
- Free and constrained optimization
- ...

(optimization:constrained)=
## Unconstrained optimization

Given $f(\mathbf{x})$, with $\mathbf{x} \in \mathbb{R}^n$, a **candidate local** extreme $\mathbf{x}^*$ is a point where the *gradient* $\partial_\mathbf{x} f$ of function $f$ is zero

$$\partial_{\mathbf{x}} f(\mathbf{x}^*) = \mathbf{0} \ .$$

Among these candidates, local extreme may be:
- maximum: if the Hessian evalauted in $\mathbf{x}^*$ is definite negative,

  $$\begin{cases}
    \partial_{\mathbf{x}} f(\mathbf{x}^*) = \mathbf{0} \\
    \partial_{\mathbf{x} \mathbf{x}} f(\mathbf{x}^*) > 0 \\
  \end{cases}$$

- minimum: if the Hessian evalauted in $\mathbf{x}^*$ is definite positive,

  $$\begin{cases}
    \partial_{\mathbf{x}} f(\mathbf{x}^*) = \mathbf{0} \\
    \partial_{\mathbf{x} \mathbf{x}} f(\mathbf{x}^*) < 0 \\
  \end{cases}$$

Here the formalism $\partial_{\mathbf{x} \mathbf{x}} f(\mathbf{x}^*) < 0$ indicates that the Hessian matrix is negative definite, see {prf:ref}`optimization:hessian:extreme`. 

```{prf:example} Positive/negative definite Hessian
:label: optimization:hessian:extreme

Local polynomial expansion of a differentiable function $\mathbf{x}$ around $\mathbf{x}^*$ reads

$$f(\mathbf{x}) = f(\mathbf{x}^*) + \Delta \mathbf{x}^T \partial_{\mathbf{x}} f(\mathbf{x}^*) + \dfrac{1}{2} \Delta \mathbf{x}^T \, \partial_{\mathbf{x} \mathbf{x}} f(\mathbf{x}^*) \, \Delta \mathbf{x} + o(|\Delta\mathbf{x}|^2) \ ,$$

with $\Delta \mathbf{x} = \mathbf{x} - \mathbf{x}^*$.

Candidate extreme points are thos points $\mathbf{x}^*$ where the gradient vanishes $\partial_{\mathbf{x}} f\mathbf{x}^*) = 0$. If the Hessian $H(\mathbf{x}^*) := \partial_{\mathbf{x} \mathbf{x}} f(\mathbf{x}^*)$ is positive definite, by definition,

$$\mathbf{v}^T \, H(\mathbf{x}^*) \mathbf{v} > 0 \ , \qquad \forall \mathbf{v} \ne \mathbf{0} \ ,$$

then

$$f(\mathbf{x}) =  f(\mathbf{x}^*) + \dfrac{1}{2} \Delta \mathbf{x}^T  H(\mathbf{x}^*) \, \Delta \mathbf{x} + o(|\Delta\mathbf{x}|^2) > f(\mathbf{x}^*) \ ,$$

as $|\Delta \mathbf{x}| \rightarrow 0$, and thus $\mathbf{x}^*$ is a point of minimum, as $f(\mathbf{x}) > f(\mathbf{x}^*)$ for all the neighoring points $\mathbf{x}$.

```

(optimization:constrained)=
## Constrained optimization

$$f(\mathbf{x}) \ , \qquad \mathbf{x} \in D \subseteq \mathbb{R}^n $$

with constraints, such as

$$\begin{aligned}
  \mathbf{g}(\mathbf{x}) & = \mathbf{0} \\
  \mathbf{h}(\mathbf{x}) & \ge \mathbf{0} \\
\end{aligned}$$

(optimization:constrained:lagrange-multipliers)=
### Method of Lagrange multipliers for equality constraints

$$\widetilde{f}(\mathbf{x}; \boldsymbol{\lambda}) = f(\mathbf{x}) - \boldsymbol{\lambda}^T \, \mathbf{g}(\mathbf{x}) \ .$$


