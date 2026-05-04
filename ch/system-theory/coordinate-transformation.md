(system-theory:coordinate-transformation)=
# Coordinate transformation

(system-theory:coordinate-transformation:general)=
## General transformation

In this section, a coordinate transformation of the state of a linear system

$$\left\{\begin{aligned}
  \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
       \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} \
\end{aligned}\right.$$

is discussed.
Let the coordinate transformation be $\mathbf{x} = \mathbf{T} \hat{\mathbf{x}}$ be invertible, then the linear system using the new set of coordinates becomes

$$\left\{\begin{aligned}
  \dot{\hat{\mathbf{x}}} & = \hat{\mathbf{A}} \hat{\mathbf{x}} + \hat{\mathbf{B}} \mathbf{u} \\
            \mathbf{y}   & = \hat{\mathbf{C}} \hat{\mathbf{x}} + \hat{\mathbf{D}} \mathbf{u} \
\end{aligned}\right.$$

with

$$\begin{aligned}
  \hat{\mathbf{A}} & = \mathbf{T}^{-1} \mathbf{A} \mathbf{T} & \hat{\mathbf{B}} & = \mathbf{T}^{-1} \mathbf{B} \\
  \hat{\mathbf{C}} & =                 \mathbf{C} \mathbf{T} & \hat{\mathbf{D}} & =                 \mathbf{D} \ .
\end{aligned}$$

### Characteristic polynomial

The characteristic polynomial of the system doesn't change, as

$$\left| s \mathbf{I} - \hat{\mathbf{A}} \right| = \left| s \mathbf{I} - \mathbf{T}^{-1} \mathbf{A} \mathbf{T} \right| = \left| \mathbf{T}^{-1} \left( s \mathbf{I} - \mathbf{A} \right) \mathbf{T} \right| = \underbrace{\left| \mathbf{T}^{-1} \right|}_{= \left| \mathbf{T} \right|^{-1}} \left| s \mathbf{I} - \mathbf{A} \right| \left| \mathbf{T} \right| = \left| s \mathbf{I} - \mathbf{A} \right| \ .$$

### Gramians

The observability Gramian ({prf:ref}`def:observability-gramian`) and controllability Gramian ({prf:ref}`def:controllability-gramian`) of the transformed system read

$$\begin{aligned}
\hat{\mathbf{W}}_o & = \mathbf{T}^{ T} \mathbf{W}_c \mathbf{T}      \\
\hat{\mathbf{W}}_c & = \mathbf{T}^{-1} \mathbf{W}_c \mathbf{T}^{-T} \\
\end{aligned}$$

```{dropdown} Proof
:open:

$$\begin{aligned}
  \hat{\mathbf{W}}_o := \int_{\tau = 0}^{t} e^{\hat{\mathbf{A}}^T (t-\tau)} \hat{\mathbf{C}}^T(\tau) \hat{\mathbf{C}}(\tau) e^{\hat{\mathbf{A}}(t-\tau)} d \tau \\
  \hat{\mathbf{W}}_c := \int_{\tau = 0}^{t} e^{\hat{\mathbf{A}} (t-\tau)} \hat{\mathbf{B}}(\tau) \hat{\mathbf{B}}^T(\tau) e^{\hat{\mathbf{A}}^T(t-\tau)} d \tau \\
\end{aligned}$$

```


(system-theory:coordinate-transformation:examples)=
## Example of transformations

(system-theory:coordinate-transformation:examples:diagonalization)=
### Diagonalization

**Spectral decomposition.** If the [spectral decomposition]() of matrix $\mathbf{A} \in \mathbb{C}^{n,n}$ exists, there are vector basis $\{ \mathbf{v}_i \}_{i=1:n}$, $\{ \mathbf{w}_i \}_{i=1:n}$ of $\mathbb{C}^n$ so that

$$\begin{aligned}
  \mathbf{A} \mathbf{v}_i & = s_i \mathbf{v}_i  \\
  \mathbf{w}^*_i \mathbf{A} & = s_i \mathbf{w}^*_i  \ ,
\end{aligned}$$

being $s_i$ the eigenvalues of the matrix, $\mathbf{v}_i$ the right-eigenvectors and $\mathbf{w}_i$ the left eigenvectors. Using matrix formalism

$$\begin{aligned}
  \mathbf{A} \mathbf{V} & = \mathbf{V} \boldsymbol{\Lambda}  \\
  \mathbf{W} \mathbf{A} & = \boldsymbol{\Lambda} \mathbf{W}  \ .
\end{aligned}$$

Left- and right-eigenvectors associated with different eigenvalues are orthogonal.

```{dropdown} Left- and right-eigenvectors orthogonality.
:open:

$$\begin{aligned}
  \mathbf{w}^*_k \mathbf{A} \mathbf{v}_i & = s_i \mathbf{w}^*_k \mathbf{v}_i \\
  \mathbf{w}^*_k \mathbf{A} \mathbf{v}_i & = s_k \mathbf{w}^*_k \mathbf{v}_i \\
\end{aligned}$$

implies (subtraction) $(s_i - s_k) \mathbf{w}^*_k \mathbf{v}_i = 0$. If $s_i \ne s_k$, then $\mathbf{w}^*_k \mathbf{v}_i = 0$.

* If $s_i, s_k \ne 0$, this also implies $\mathbf{w}_k^* \mathbf{A} \mathbf{v}_i = 0$. 
* This relation when the indices are equal can be used for normalization condition
* A unit orthogonal basis can be computed for eigenvalues with algebraic multiplicity $> 1$ 

If normalization condition reads $\mathbf{w}_i^* \mathbf{v}_i = 1$ (no sum), $\mathbf{W}^* \mathbf{V} = \mathbf{I}$, then

$$\mathbf{W}^* \mathbf{A} \mathbf{V} = \boldsymbol{\Lambda} \ .$$

```

**Diagonalization.** Let $\mathbf{x} = \mathbf{V} \hat{\mathbf{x}}$ the representation of the state with the vector basis $\mathbf{V}$, and the projection of the state dynamical equation onto $\mathbf{W}$. The state-space representation of the system reads

$$\left\{\begin{aligned}
  \dot{\hat{\mathbf{x}}} = \boldsymbol{\Lambda} \hat{\mathbf{x}} + \mathbf{W}^* \mathbf{B} \mathbf{u} \\
            \mathbf{y}   = \mathbf{C} \mathbf{V} \hat{\mathbf{x}} + \mathbf{D} \mathbf{u}  \ ,
\end{aligned}\right. $$

with $\boldsymbol{\Lambda}$ diagonal. I.e. in components, with $\hat{\mathbf{B}} := \mathbf{W}^* \mathbf{B}$,

$$\dot{\hat{x}}_i = \lambda_i \hat{x}_i + \sum_{j=1}^{m} \hat{B}_{ij} u_j = \lambda_i \hat{x}_i + \hat{\mathbf{b}}_i^* \mathbf{u} \ ,$$

or in Laplace domain, the $i^{th}$ component in the diagonal representation reads

$$\hat{x}_i = \frac{1}{s - \lambda_i} \hat{\mathbf{b}}_i^* \mathbf{u} \ .$$

the state in the original coordinates reads

$$\mathbf{x} = \mathbf{V} \hat{\mathbf{x}} = \sum_{i=1}^{n} \mathbf{v}_i \hat{x}_i = \sum_{i=1}^{n} \mathbf{v}_i  \frac{1}{s - \lambda_i} \hat{\mathbf{b}}_i^* \mathbf{u} \ .$$

and the output reads

$$\begin{aligned}
 \mathbf{y}
 & = \mathbf{C} \mathbf{V} \hat{\mathbf{x}} + \mathbf{D} \mathbf{u} = \\
 & = \hat{\mathbf{C}} \hat{\mathbf{x}} + \mathbf{D} \mathbf{u} = \\
 & = \sum_{i=1}^{n} \hat{\mathbf{c}}_i \hat{x}_i + \mathbf{D} \mathbf{u} = \\
 & = \left[ \sum_{i=1}^{n} \frac{1}{s-\lambda_i} \hat{\mathbf{c}}_i \hat{\mathbf{b}}^*_i + \mathbf{D} \right] \mathbf{u} = \\
 & = \mathbf{H}(s) \mathbf{u} \ .
\end{aligned}$$

```{dropdown} Proof
...

```

**Transfer function.** Thus, the transfer function between the input and the output can be written as

$$\begin{aligned}
  \hat{\mathbf{H}}(s) = \sum_{i=1}^{n} \frac{1}{s-\lambda_i} \hat{\mathbf{c}}_i \hat{\mathbf{b}}^*_i + \mathbf{D} \ . 
\end{aligned}$$

This is a linear combination of factors $\frac{1}{s - \lambda_i}$. Thus, the denominators of these fractions appear in the denominatore of the transfer function if both $\mathbf{b}_i \ne \mathbf{0}$ and $\mathbf{c}_i \ne \mathbf{0}$. **todo** *Further cancellations may occur. It's better to use [observability](system-theory:kalman-decomposition:observability) or [controllability](system-theory:kalman-decomposition:controllability) vector basis or [Kalman decomposition](system-theory:kalman-decomposition:kalman) to link cancellations and observability/controllability*


(system-theory:coordinate-transformation:examples:kalman)=
### Kalman decomposition

$$\mathbf{x} = \mathbf{T} \mathbf{x} = \begin{bmatrix} \ \mathbf{U}_1 & \mathbf{U}_2 & \mathbf{U}_3 & \mathbf{U}_4 \ \end{bmatrix} \mathbf{z} = \begin{bmatrix} \ \mathbf{U}_1 & \mathbf{U}_2 & \mathbf{U}_3 & \mathbf{U}_4 \ \end{bmatrix} \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \\ \mathbf{z}_3 \\ \mathbf{z}_4 \end{bmatrix} \ ,$$

[Kalman decomposition](system-theory:kalman-decomposition:kalman) of a linear system reads

$$\left\{\begin{aligned}
  \frac{d}{dt} \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \\ \mathbf{z}_3 \\ \mathbf{z}_4 \end{bmatrix} & =
  \begin{bmatrix} 
     \mathbf{A}_{11} & \mathbf{A}_{12} & \mathbf{A}_{13} & \mathbf{A}_{14} \\ 
     \mathbf{0}      & \mathbf{A}_{22} & \mathbf{0}      & \mathbf{A}_{24} \\ 
     \mathbf{0}      & \mathbf{0}      & \mathbf{A}_{33} & \mathbf{A}_{34} \\ 
     \mathbf{0}      & \mathbf{0}      & \mathbf{0}      & \mathbf{A}_{44} \\ 
  \end{bmatrix}
  \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \\ \mathbf{z}_3 \\ \mathbf{z}_4 \end{bmatrix} +
  \begin{bmatrix} \mathbf{B}_1 \\ \mathbf{B}_2 \\ \mathbf{0} \\ \mathbf{0} \end{bmatrix} \mathbf{u} \\
  \mathbf{y} & = \begin{bmatrix} \ \mathbf{0} & \mathbf{C}_2 & \mathbf{0} & \mathbf{C}_4 \end{bmatrix}
  \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \\ \mathbf{z}_3 \\ \mathbf{z}_4 \end{bmatrix} +
  \mathbf{D} \mathbf{u} 
\end{aligned}\right.$$


(system-theory:coordinate-transformation:examples:kalman:tf)=
#### Transfer function

Asymptotical stable systems have the free response decaying to zero after a certain time range, so that only the forced response survives. Forced response in Laplace domain reads

$$\begin{aligned}
  ( s \mathbf{I} - \mathbf{A}_{44}) \mathbf{z}_4 & = \mathbf{0} \\
   \mathbf{z}_3 & = ( s \mathbf{I} - \mathbf{A}_{33})^{-1} \mathbf{A}_{34} \mathbf{z}_4 \\
   \mathbf{z}_2 & = ( s \mathbf{I} - \mathbf{A}_{22})^{-1} \left( \mathbf{A}_{24} \mathbf{z}_4 + \mathbf{B}_2 \mathbf{u} \right) \\
   \mathbf{z}_1 & = ( s \mathbf{I} - \mathbf{A}_{11})^{-1} \left( \mathbf{A}_{12} \mathbf{z}_2 + \mathbf{A}_{13} \mathbf{z}_3 + \mathbf{A}_{14} \mathbf{z}_4 + \mathbf{B}_1 \mathbf{u} \right) \\
\end{aligned}$$

and thus

$$\begin{aligned}
  \mathbf{z}_4 & = \mathbf{0} \\
  \mathbf{z}_3 & = \mathbf{0} \\
  \mathbf{z}_2 & = ( s \mathbf{I} - \mathbf{A}_{22})^{-1} \mathbf{B}_2 \mathbf{u} \\
  \mathbf{z}_1 & = ( s \mathbf{I} - \mathbf{A}_{11})^{-1} \left[ \mathbf{A}_{12} ( s \mathbf{I} - \mathbf{A}_{22})^{-1} \mathbf{B}_2 + \mathbf{B}_1 \right] \mathbf{u}
\end{aligned}$$

and the output reads

$$\mathbf{y} = \mathbf{C}_2 ( s \mathbf{I} - \mathbf{A}_{22})^{-1} \mathbf{B}_2 \mathbf{u} \ .$$

From the input-output relation, it's clear that only the reachable and observable part of the system contributes to the transfer function, i.e. to the input-output relation for asymptotically stable systems after the free response due to non-zero initial conditions has decayed.


