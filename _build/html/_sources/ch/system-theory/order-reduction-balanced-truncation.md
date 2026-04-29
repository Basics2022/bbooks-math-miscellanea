(order-reduction:balanced-truncation)=
# Balanced truncation

While [Kalman decomposition](kalman-decomposition) provides the theoretical results for the existence of 4 subspaces of a linear dynamical system, and the transformation of coordinates that partition the dynamical systems using reachability and (non-)observatilibty as criteria, this decomposition is likely to be almost useless in many applications: it relies on a sharp distinction between zero and non-zero observability/controllability while these properties can be represented with non-binary numbers but real numbers, and suffers from the limits of finite algebra (the result of a numerical algorithm involving real numbers is unlikely to be $0$, and thus it's likely that we need to answer questions like "is $10^{-9}$ zero enough?" in some step of the algorithm). Moreover, the most interesting part of the system is likely to be the reachable and observable part[^unstable-non-observable-non-reachable]: balanced truncation doesn't suffer from the issues of a full Kalman decomposition while ranking dynamics of the system using controllability and reachability as a criterion.

[^unstable-non-observable-non-reachable]: The non-observable or non-controllable parts of a system should not contain any unstable dynamics, otherwise it can be measured by the sensors, and/or controlled by the actuators. Observability and controllability are strictly related to the choice of sensors and actuators. If any uncontrollable unstable dynamics exists, a different choice of actuators may solve this issue. If any unobservable unstable dynamics exists, a different choice of sensors may solve the issue.

For finite-time horizon problems, controllability Gramian $\mathbf{W}_c$ and observability Gramian $\mathbf{W}_o$ can be computed as the solution of the Lyapunov equation

$$\begin{aligned}
 \mathbf{0} & = \mathbf{A} \mathbf{W}_c + \mathbf{W}_c \mathbf{A}^T + \mathbf{B} \mathbf{B}^T \\
 \mathbf{0} & = \mathbf{A}^T \mathbf{W}_o + \mathbf{W}_o \mathbf{A} + \mathbf{C}^T \mathbf{C} \ .
\end{aligned}$$

Balanced truncation exploits two pairs of combined scaling+rotation transformations, obtained with [singular value decomposition](math:svd) of the Gramians of the system.

**Method 1.**
* Singular value decomposition of the controllability Gramian $\mathbf{W}_c = \mathbf{U}_c \boldsymbol\Sigma_c^2 \mathbf{U}_c^*$
* First coordinate transformation, $\mathbf{x} = \mathbf{T}_c \mathbf{x}_1$, with $\mathbf{T}_c = \mathbf{U}_c \boldsymbol\Sigma_c$, so that  $\mathbf{A}_1 = \mathbf{T}_c^{-1} \mathbf{A} \mathbf{T}_c$, and the observability Gramian of the transformed system can be expressed as $\mathbf{W}_{o,1} = \mathbf{T}_c^{T} \mathbf{W}_o \mathbf{T}_c$
* Singular value decomposition of $\mathbf{W}_{o,1} = \mathbf{U}_{o,1} \boldsymbol\Sigma_{o,1}^2 \mathbf{U}_{o,1}^*$
* Second transformation $\mathbf{x}_1 = \mathbf{T}_o \mathbf{x}_2$, with $\mathbf{T}_o = \mathbf{U}_{o,1} \boldsymbol\Sigma_{o,1}^{-1/2}$
* Thus, the Gramians in the twice transformed system, with $\mathbf{T} = \mathbf{T}_c \mathbf{T}_o$, read

  $$\begin{aligned}
    \mathbf{W}_{c,2} & = \mathbf{T}^{-1} \mathbf{W}_{c} \mathbf{T}^{-T} = \left( \boldsymbol\Sigma_{o,1}^{1/2} \mathbf{U}_{o,1}^* \boldsymbol\Sigma_c^{-1} \mathbf{U}_c^* \right) \left( \mathbf{U}_c \boldsymbol\Sigma_c^2 \mathbf{U}_c^* \right) \left( \mathbf{U}_c \boldsymbol\Sigma_c^{-1} \mathbf{U}_{o,1} \boldsymbol \Sigma_{o,1}^{1/2} \right) & = \boldsymbol\Sigma_{o,1}  \\
    \mathbf{W}_{o,2} & = \mathbf{T}_o^T \mathbf{W}_{o,1} \mathbf{T}_o = \left( \boldsymbol\Sigma_{o,1}^{-1/2} \mathbf{U}_{o,1}^* \right) \left( \mathbf{U}_{o,1} \boldsymbol\Sigma_{o,1}^2 \mathbf{U}_{o,1}^* \right) \left( \mathbf{U}_{o,1} \boldsymbol\Sigma_{o,1}^{-1/2} \right) & = \boldsymbol\Sigma_{o,1} \ ,
  \end{aligned}$$

  i.e. they're equal. The pair of transformations makes Gramians equal and diagonal, and the elements of the diagonal - called **Hankel values** of the system - simultaneously measure the controllability and the observability of the system.

**todo** *here inverse of the diagonal singular value matrices are assumed to exists, i.e. there's no non-observable or non-controllable state.*

The transformed system is then partitioned as

$$\left\{
\begin{aligned}
  \frac{d}{dt} \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \end{bmatrix} & = 
               \begin{bmatrix} \mathbf{A}_{11} & \mathbf{A}_{12} \\ \mathbf{A}_{21} & \mathbf{A}_{22} \end{bmatrix}
               \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \end{bmatrix} + 
               \begin{bmatrix} \mathbf{B}_{1} \\ \mathbf{B}_{2} \end{bmatrix} \mathbf{u} \\
\mathbf{y} & = \begin{bmatrix} \mathbf{C}_1 & \mathbf{C}_2 \end{bmatrix} 
               \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \end{bmatrix} + \mathbf{D} \mathbf{u}  
\end{aligned}
\right.$$

with $\mathbf{x} = \mathbf{T} \mathbf{z}$, and thus

$$\mathbf{z} = \mathbf{T}^{-1} \mathbf{x} = \boldsymbol\Sigma_{o,1}^{1/2} \mathbf{U}_{o,1}^* \boldsymbol\Sigma_c^{-1} \mathbf{U}_c^*$$

$$\begin{aligned}
\begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \end{bmatrix}
 & =
\begin{bmatrix} \boldsymbol\Sigma_{o,1;1}^{1/2} & \mathbf{0} \\ \mathbf{0} & \boldsymbol\Sigma_{o,1;2}^{1/2} \end{bmatrix}
\begin{bmatrix} \mathbf{U}_{o,1;11}^* & \mathbf{U}_{o,1;12}^* \\ \mathbf{U}_{o,1;21}^* & \mathbf{U}_{o,1;22}^* \end{bmatrix}
\begin{bmatrix} \boldsymbol\Sigma_{c  ;1}^{-1 } & \mathbf{0} \\ \mathbf{0} & \boldsymbol\Sigma_{c;2}^{-1} \end{bmatrix}
\begin{bmatrix} \mathbf{U}_{c;11}^* & \mathbf{U}_{c;12}^* \\ \mathbf{U}_{c;21}^* & \mathbf{U}_{c;22}^* \end{bmatrix}
 \mathbf{x} = \\
 & =
\begin{bmatrix} \boldsymbol\Sigma_{o,1;1}^{1/2}\mathbf{U}_{o,1;11}^* & \boldsymbol\Sigma_{o,1;1}^{1/2}\mathbf{U}_{o,1;12}^* \\ \boldsymbol\Sigma_{o,1;2}^{1/2} \mathbf{U}_{o,1;21}^* & \boldsymbol\Sigma_{o,1;2}^{1/2} \mathbf{U}_{o,1;22}^* \end{bmatrix}
\begin{bmatrix} \boldsymbol\Sigma_{c  ;1}^{-1 }\mathbf{U}_{c;11}^* & \boldsymbol\Sigma_{c  ;1}^{-1 }\mathbf{U}_{c;12}^* \\ \boldsymbol\Sigma_{c;2}^{-1}\mathbf{U}_{c;21}^* & \boldsymbol\Sigma_{c;2}^{-1}\mathbf{U}_{c;22}^* \end{bmatrix}
 \mathbf{x} = \\
\end{aligned}$$

**todo** *Show if this algorithm allows to compute only the desired part of the svd, allowing the incremental computation, and not requiring the full svd computation*



```{dropdown} Transformation of Gramians
:open:

$$\begin{aligned}
  \hat{\mathbf{W}}_c & = \int e^{\hat{\mathbf{A}}t} \hat{\mathbf{B}} \hat{\mathbf{B}}^T e^{\hat{\mathbf{A}}^T t} = \mathbf{T}^{-1} \mathbf{W}_c \mathbf{T}^{-T} \\
  \hat{\mathbf{W}}_o & = \int e^{\hat{\mathbf{A}}^T t} \hat{\mathbf{C}}^T \hat{\mathbf{C}} e^{\hat{\mathbf{A}} t} = \mathbf{T}^{T} \mathbf{W}_o \mathbf{T} \\
\end{aligned}$$


as for $\mathbf{x} = \mathbf{T} \hat{\mathbf{x}}$, $\hat{\mathbf{A}} = \mathbf{T}^{-1} \mathbf{A} \mathbf{T}$, $\hat{\mathbf{B}} = \mathbf{T}^{-1} \mathbf{B}$, $\hat{\mathbf{C}} = \mathbf{C} \mathbf{T}$, $\hat{\mathbf{D}} = \mathbf{D}$.


```


**Method 2.**
* Cholesky decomposition (for positive semi-definite matrices) of the controllability and observability Gramians $\mathbf{W}_c = \mathbf{L}_c \mathbf{L}_c^*$, $\mathbf{W}_o = \mathbf{L}_o \mathbf{L}_o^*$
* Compute the SVD of the product of the Cholesky factors, $\mathbf{L}_o^* \mathbf{L}_c = \mathbf{U} \boldsymbol\Sigma \mathbf{V}^*$
* Partition 
  
    $$
    \boldsymbol\Sigma = \begin{bmatrix} \boldsymbol\Sigma_1 & \mathbf{0} \\ \mathbf{0} & \boldsymbol\Sigma_2 \end{bmatrix}
    \quad , \quad \mathbf{U} = \begin{bmatrix} \ \mathbf{U}_1 & \mathbf{U}_2 \ \end{bmatrix}
    \quad , \quad \mathbf{V} = \begin{bmatrix} \ \mathbf{V}_1 & \mathbf{V}_2 \ \end{bmatrix}
    $$

* Projection matrices $\mathbf{T} = \mathbf{L}_c \mathbf{V}_1 \boldsymbol\Sigma_1^{-1/2}$, $\widetilde{\mathbf{T}} = \boldsymbol\Sigma_1^{-1/2} \mathbf{U}_1^* \mathbf{L}_o^*$[^balanced-truncation-petrov-galerkin],

    $$\begin{aligned}
      \mathbf{A}_r & = \widetilde{\mathbf{T}} \mathbf{A} \mathbf{T} \\
      \mathbf{B}_r & = \widetilde{\mathbf{T}} \mathbf{B}            \\
      \mathbf{C}_r & =                        \mathbf{C} \mathbf{T} \\
      \mathbf{D}_r & =                        \mathbf{D}            \\
    \end{aligned}$$

   [^balanced-truncation-petrov-galerkin]: This can be interpreted as a **Petrov-Galerkin** projection (**todo** *link to Finite Element Method?*), i.e. a model reduction with different base and test basis: here, base vectors are the columns of the matrix $\mathbf{T}$ while test vectors are the rows of the matrix $\widetilde{\mathbf{T}}$.
