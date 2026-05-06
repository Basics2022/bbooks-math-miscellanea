(system-theory:state-space-realizations)=
# State-space realizations

State-Space RealizationsIn system theory, a realization is a state-space triplet $\{A, B, C, D\}$ that represents a given transfer function $H(s)$. For a strictly proper system, the relationship is defined by:

$$H(s) = C(sI - A)^{-1}B$$

Given a general $n$-th order transfer function:

$$H(s) = \frac{b_{n-1}s^{n-1} + \dots + b_1s + b_0}{s^n + a_{n-1}s^{n-1} + \dots + a_1s + a_0}$$

There are two primary canonical forms used for implementation and analysis.

(system-theory:state-space-realizations:ccf)=
## Controller Canonical Form (CCF)

The Controller Canonical Form is structured to make the system's controllability obvious. It is often used in control design (e.g., pole placement) because the input $u(t)$ enters the "chain" of integrators at the final stage.

**State-Space Representation.** The matrices for an $n$-th order system in CCF are:

$$A = \begin{bmatrix} 
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & 1 \\
-a_0 & -a_1 & -a_2 & \dots & -a_{n-1}
\end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}$$

$$C = \begin{bmatrix} b_0 & b_1 & \dots & b_{n-1} \end{bmatrix}$$

Characteristics
* Structure: The states are typically chosen as the output and its derivatives ($x_1 = y, x_2 = \dot{y}, \dots$) in the absence of zeros.
* Controllability: A system in this form is always controllable, provided there are no pole-zero cancellations.

(system-theory:state-space-realizations:ocf)=
## Observer Canonical Form (OCF)

The Observer Canonical Form is the dual of the CCF. It is structured such that the output $y(t)$ is directly influenced by all state variables, making the system's observability easily verifiable.

**State-Space Representation.**

The matrices for an $n$-th order system in OCF are:

$$A = \begin{bmatrix} 
0 & 0 & \dots & 0 & -a_0 \\
1 & 0 & \dots & 0 & -a_1 \\
0 & 1 & \dots & 0 & -a_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 1 & -a_{n-1}
\end{bmatrix}, \quad
B = \begin{bmatrix} b_0 \\ b_1 \\ b_2 \\ \vdots \\ b_{n-1} \end{bmatrix}$$

$$C = \begin{bmatrix} 0 & 0 & \dots & 0 & 1 \end{bmatrix}$$

Characteristics:
* Duality: The $A$ matrix of the OCF is the transpose of the $A$ matrix of the CCF ($A_{OCF} = A_{CCF}^T$), and the $B$ and $C$ matrices are swapped and transposed ($B_{OCF} = C_{CCF}^T$ and $C_{OCF} = B_{CCF}^T$).
* Observability: A system in this form is always observable.

## Example: realization of a second-order system

From the specific case $H(s) = \frac{s}{s^2 + a_1s + a_0}$:

Controller Realization

$$\dot{x} = \begin{bmatrix} 0 & 1 \\ -a_0 & -a_1 \end{bmatrix} x + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u, \quad y = \begin{bmatrix} 0 & 1 \end{bmatrix} x$$

Observer Realization

$$\dot{x} = \begin{bmatrix} 0 & -a_0 \\ 1 & -a_1 \end{bmatrix} x + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u, \quad y = \begin{bmatrix} 0 & 1 \end{bmatrix} x$$

## Minimality and Similarity Transformations

A realization is minimal if and only if it is both controllable and observable. The dimension of a minimal realization equals the degree of the denominator of the transfer function (the McMillan degree).Any two realizations $\{A, B, C\}$ and $\{\tilde{A}, \tilde{B}, \tilde{C}\}$ of the same transfer function are related by a similarity transformation $T$ such that:

$$\tilde{A} = T A T^{-1}, \quad \tilde{B} = T B, \quad \tilde{C} = C T^{-1}$$

