(ode:integration-schemes)=
# Integration schemes for Cauchy problems

```{dropdown} OLD-Contents

**Schemes.**

* Euler methods, CN
* RK
* Multi-step: AB, AM, BDF,...
* Other methods:
  * Newmark-beta, Verlet (Leapfrog),...

**Concepts.**

* Convergence:
* Consistence:
* Stability:
  * zero-stability
  * A-stability
  * L-stability
* Stiffness

**Theoretical results**

* Dahlquist barriers
* Lax-Richtmyer

**References**

* [Advantage of L-stability compared to A-stability](https://math.stackexchange.com/questions/1466978/advantage-of-l-stability-compared-to-a-stability), Mathematics Stack Exchange.

```

Many models of real-life systems are governed by Ordinary Differential Equations (ODEs). While simple linear equations yield elegant analytical solutions, as shown in sections about [Linear ODEs with constant coefficients](ode:linear-equations) and [Linear ODEs in state-space representation](ode:linear:miscellanea), real-world engineering problems demand numerical approximations, as no practical closed-form solution exists.

The choice of a time-integration scheme is far more than a software implementation detail; it represents a fundamental trade-off between **accuracy**, **computational cost**, and **fidelity**: a naive choice of solver can damp out physically vital high-frequency oscillations, generate artificial energy out of nothing, or completely explode due to numerical instability.

This chapter tries to provide some rigorous mathematical foundation needed to analyze, select, (and build? Do we need any new algorithm? Do not re-invent the wheel!) robust time-integration schemes. 

**Contents.**

```{dropdown} [Foundations of numerical integration of initial value problems](ode:integration-schemes:foundations)
:open:

First, the canonical problem[^second-order-canonical-problem]

[^second-order-canonical-problem]: A second-order canonical problem $ \mathbf{M} \ddot{\mathbf{y}} + \mathbf{C} \dot{\mathbf{y}} + \mathbf{K} \mathbf{y} = \mathbf{f}(t, \mathbf{y}(t))$, with proper initial conditions, is also discussed. This problem often arises with some interesting properties - symmetry of matrices - usually arises from a [Lagrangian approach]() to classical mechanics systems. Some numerical methods targeting this form of equations exist, like [Leapfrog], [Verlet], or [Newmark] methods.

$$
\left\{\begin{aligned}
  & \dot{\mathbf{y}} = \mathbf{f}(t, \mathbf{y}(t)) \\
  & \mathbf{y}(0) = \mathbf{y}_0
\end{aligned}\right.
$$

is discussed, along with the definition of
* **local truncation error** and **consistency**
* **global truncation error** and **convergence**

<!--
We begin with core properties like consistency, order, and convergence before diving into stability analysis in the complex plane. We will explore how geometric integrators preserve underlying physical structures, such as phase-space volume and energy. Finally, we will bring these abstract mathematical tools down to earth by building a complete, high-fidelity simulation of the continuous torsional dynamics of an elastic homogeneous beam.
-->

```

```{dropdown} [Common integration schemes](ode:integration-schemes:common)
:open:

**For first-order equation.**
* One-step methods(I):
  * Explicit: Explicit Euler, Heun (special case of RK)
  * Implicit: Implicit Euler, Crank-Nicolson

* One-step methods(II): Runge-Kutta (RK) methods

* Linear multi-step methods:
  * Adams-Bashforth (AB)
  * Adams-Moulton   (AM)
  * Backward Differentiation Formulas (BDF)

```

```{dropdown} [Stability analysis](ode:integration-schemes:stability)
:open:

Linear stability on test equations, $\dot{y} = \lambda y$ for the first-order system, $\ddot{y} = \dots$ for the second-order system.
Through one-step transfer function $G(z)$, $z = \lambda \, dt$, $y_{n+1} = G(z) y_{n}$,

* Stability region of numerical methods
* 0-ztability
* A-stability
* L-stability


**Theorems and limits**
* Dahlquist barriers
* Lax theorem: consistency + stability = convergence

```

```{dropdown} [Integration and conservation laws](ode:integration-schemes:energy-conservation)
:open:

Some physical systems satisfy some conservation laws. As an example, **Hamiltonian systems** satisfy **energy conservation** or - equivalently - volume conservation in phase space.

Simplectic integrators are numerical methods that preserves these conservation laws of the original system.
...

```

```{dropdown} Examples
:open:

* [Example: torsional dynamics of an elastic beam](ode:integration-schemes:mechanical-system): finite element method of the continuous model is built; spectral decomposition of the discrete problem is discussed and compared with the eigenvalues of the continuous system; diagonal structural damping is introduced; previous results are used for an aware numerical integration in time of the dynamics of the beam subject to a harmonic torsional moment, using fast mode truncation and their static recovery.

```
