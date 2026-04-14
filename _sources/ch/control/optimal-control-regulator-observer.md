(control:controller-observer)=
# Combination of controller and observer

Full-state feed-back or the observed state builds the controller on the observed state. As an example, an [optimal full-state controller](contol:optimal:full-state-fb) is designed as the state was available, to find matrix $\mathbf{G}$; a state observer is designed to get the observed state $\mathbf{o}(t)$, through the design of a matrix $\mathbf{L}$ as in [Kalman filter](control:kalman); the feed-back on the observed state produces the control $\mathbf{u}(t) = - \mathbf{G} \mathbf{o}(t)$.

Two different cases are discussed here: 
1. the whole state is used to design the control law, as it's the case of small-systems with few states/degrees of freedom. In this situation, a **separation principle** holds, i.e. the state estimator design and the control design can be performed independently, as the eigenvalues of the closed-loop system are the eigenvalues of the closed-loop matrix $\mathbf{A} - \mathbf{B} \mathbf{G}$ and the observer $\mathbf{A} - \mathbf{L} \mathbf{C}$
2. a reduced state is used to design the control law, as it's the case of large-dimensional systems or continuous systems (as deformable bodies, whose nomber of degrees of freedom is infinite). For these systems, a subset of states is used for control design, in order to reduce the computational burden. In this situation, separation principle doesn't hold and **spill-over** may occur between states.

(control:controller-observer:separation-principle)=
## Separation principle

System

$$\begin{cases}
  \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B}_u \mathbf{u} + \mathbf{B}_d \mathbf{d} \\
       \mathbf{y}  = \mathbf{C} \mathbf{x} + \mathbf{D}_u \mathbf{u} + \mathbf{D}_d \mathbf{d} + \mathbf{D}_r \mathbf{r} \\
\end{cases}$$

Observer

$$\begin{cases}
  \dot{\mathbf{o}} = \mathbf{A} \mathbf{o} + \mathbf{B}_u \mathbf{u} + \mathbf{L} ( \mathbf{y} - \mathbf{y}_o ) \\
       \mathbf{y}_o= \mathbf{C} \mathbf{o} + \mathbf{D}_u \mathbf{u} \ .
\end{cases}$$

with the error dynamics, $\mathbf{e} := \mathbf{x} - \mathbf{o}$

$$
  \dot{\mathbf{e}} = \left( \mathbf{A} - \mathbf{L} \mathbf{C} \right) \mathbf{e} + \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right) \mathbf{d} - \mathbf{L} \mathbf{D}_r \mathbf{r} 
$$

and with the control law $\mathbf{u} = - \mathbf{G} \mathbf{o} = - \mathbf{G} \left( \mathbf{x} - \mathbf{e} \right)$. The augmented system with state $\{ \mathbf{x}, \mathbf{e} \}$ reads

$$
\frac{d}{dt} \begin{bmatrix} \mathbf{x} \\ \mathbf{e} \end{bmatrix} = 
\begin{bmatrix} \mathbf{A} - \mathbf{B}_u \mathbf{G} & \mathbf{B}_u \mathbf{G} \\ \mathbf{0} & \mathbf{A} - \mathbf{L} \mathbf{C} \end{bmatrix} 
\begin{bmatrix} \mathbf{x} \\ \mathbf{e} \end{bmatrix} + 
\begin{bmatrix} \mathbf{B}_d & \mathbf{0} \\ \mathbf{B}_d - \mathbf{L} \mathbf{D}_d & - \mathbf{L} \mathbf{D}_r \end{bmatrix} 
\begin{bmatrix} \mathbf{d} \\ \mathbf{r} \end{bmatrix} \ .
$$

The matrix of the system is a block triangular matrix, and thus its eigenvalues are the union of the eigenvalues of the diagonal blocks, i.e. the eigenvalues of the closed-loop matrix $\mathbf{A} - \mathbf{B}_u \mathbf{G}$, and the matrix of the observer $\mathbf{A} - \mathbf{L} \mathbf{C}$. Thus, for the modal stability of the system, the observer and the ccontroller can be designed independently. 

(control:controller-observer:spillover)=
## Spillover

(control:controller-observer:spillover:reduced-sys)=
### Design reduced system and full system

Let $\mathbf{x}_1$ the state of the reduced system used for the design, and $\mathbf{x}_2$ the "residual" state of the large-dimensional system used for verification, or as a detailed mathematical model of the system of interest. Let the dynamical system be

$$\begin{cases}
  \dot{\mathbf{x}}_1 = \mathbf{A}_1 \mathbf{x}_1 + \mathbf{B}_{1u} \mathbf{u} \\
  \dot{\mathbf{x}}_2 = \mathbf{A}_2 \mathbf{x}_2 + \mathbf{B}_{2u} \mathbf{u} \\
  \mathbf{y}         = \mathbf{C}_1 \mathbf{x}_1 + \mathbf{C}_2 \mathbf{x}_2 + \mathbf{D}_{u} \mathbf{u}  \\
\end{cases}$$

and the optimal control designed on the reduced system, so that the input is $\mathbf{u} = - \mathbf{G} \mathbf{x}_1$. The equations governing the closed-loop dynamics of the detailed system reads

$$\begin{aligned}
\frac{d}{dt} \begin{bmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{bmatrix} & =
\begin{bmatrix}
\mathbf{A}_1 - \mathbf{B}_{1u} \mathbf{G} & \cdot \\
 - \mathbf{B}_{2u} \mathbf{G}  & \mathbf{A}_2  \\
\end{bmatrix}
\begin{bmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{bmatrix} \\
\mathbf{y} & = \begin{bmatrix} \mathbf{C}_1 - \mathbf{D}_u \mathbf{G} & \mathbf{C}_2 \end{bmatrix} \begin{bmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{bmatrix}
\end{aligned}$$

The matrix of the system is block triangular, so that the eigenvalues of the system are the union of the eigenvalues of the closed loop matrix designed on the reduced system $\mathbf{A}_1 - \mathbf{B}_{1u} \mathbf{G}$, and the matrix of the residual detailed system $\mathbf{A}_2$. In order to get a stable system, the reduced system must contain all the open-loop unstable dynamics, as the matrix $\mathbf{A}_2$ must be stable.

(control:controller-observer:spillover:reduced-sys-observer)=
### Design reduced system, observer and full system

Let $\mathbf{x}_1$ the state of the reduced system used for the design, and $\mathbf{x}_2$ the "residual" state of the large-dimensional system used for verification, or as a detailed mathematical model of the system of interest. Let the dynamical system be

$$\begin{cases}
  \dot{\mathbf{x}}_1 = \mathbf{A}_1 \mathbf{x}_1 + \mathbf{B}_{1u} \mathbf{u} \\
  \dot{\mathbf{x}}_2 = \mathbf{A}_2 \mathbf{x}_2 + \mathbf{B}_{2u} \mathbf{u} \\
  \mathbf{y}         = \mathbf{C}_1 \mathbf{x}_1 + \mathbf{C}_2 \mathbf{x}_2 + \mathbf{D}_{u} \mathbf{u}  \\
\end{cases}$$

and the observer designed on the low-dimensional system

$$\begin{cases}
  \dot{\mathbf{o}} = \mathbf{A}_1 \mathbf{o} + \mathbf{B}_{1u} \mathbf{u} + \mathbf{L} \left( \mathbf{y} - \mathbf{y}_o \right) \\
  \mathbf{y}_o     = \mathbf{C}_1 \mathbf{o} + \mathbf{D}_{1u} \mathbf{u}
\end{cases}$$

so that

$$\dot{\mathbf{o}} = \left( \mathbf{A}_1 - \mathbf{L} \mathbf{C}_1 \right) \mathbf{o} + \mathbf{L} \mathbf{C}_1 \mathbf{x}_1 + \mathbf{L} \mathbf{C}_2 \mathbf{x}_2 + \left( \mathbf{B}_{1u} - \mathbf{L} \mathbf{D}_{u} \right) \mathbf{u} \ ,$$

and the dynamical equation of the error $\mathbf{e} := \mathbf{x}_1 - \mathbf{o}$ is

$$\dot{\mathbf{e}} = \left( \mathbf{A}_1 - \mathbf{L} \mathbf{C}_1 \right) \mathbf{e} - \mathbf{L} \mathbf{C}_2 \mathbf{x}_2  \ .$$

The input is proportional to the observed state, $\mathbf{u} = - \mathbf{G} \mathbf{o}$. Thus, the augmented system reads

$$
\frac{d}{dt} \begin{bmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \\ \mathbf{e} \end{bmatrix} =
\begin{bmatrix}
\mathbf{A}_1 - \mathbf{B}_{1u} \mathbf{G} & \cdot & \mathbf{B}_{1u} \mathbf{G} \\
 - \mathbf{B}_{2u} \mathbf{G}  & \mathbf{A}_2 & \mathbf{B}_{2u} \mathbf{G} \\
 \cdot & - \mathbf{L} \mathbf{C}_2 & \mathbf{A}_1 - \mathbf{L} \mathbf{C}_1
\end{bmatrix}
\begin{bmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \\ \mathbf{e} \end{bmatrix} \ .
$$

The matrix of the system is not block triangular, as the dynamics of the "residual" state of the large-dimensional system and the reconstruction error are coupled. The eigenvalue of the systems are non-trivial as they're not anymore the eigenvalue of the diagonal blocks.

