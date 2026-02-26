(pde:hyperbolic)=
# Hyperbolic equations

- Integral equations
- Jump conditions
- Differential equations
- Method of characteristics: domains of influence
- "Inviscid" limit, multiple solutions, entropy condition and unique physical solution

Some useful script on GDrive $\texttt{basics-books/colabs/math/pde/fvm}$. So far 1-dimensional problem only: linear equation, linear system (linearized p-sys), non linear system (p-sys).

<!--
Different characteristics of hyperbolic problems:
- space domain dimension: 1-dimensional vs. multi-dimensional space domain
- linear vs. non-linear
- scalar (1 equation) vs. vector (system of equations)
-->

```{dropdown} Problems
:open:

**1-dimensional domain**
* [Scalar linear](pde:hyperbolic:problems:1d-scalar-linear)
* [Vector linear](pde:hyperbolic:problems:1d-vector-linear)
* [Scalar non-linear](pde:hyperbolic:problems:1d-scalar-nonlinear)
* [Vector non-linear](pde:hyperbolic:problems:1d-vector-nonlinear)

**n-dimensional domain**
* [Scalar linear](pde:hyperbolic:problems:nd-scalar-linear)
* [Vector linear](pde:hyperbolic:problems:nd-vector-linear)
* [Scalar non-linear](pde:hyperbolic:problems:nd-scalar-nonlinear)
* [Vector non-linear](pde:hyperbolic:problems:nd-vector-nonlinear)

```

**todo**
- hyperbolic problems as the **ideal limit of dissipative** (parabolic?) problems. In non-linear problems, multiple (infinite?) solutions of the hyperbolic problem exist, but there's only one (? Prove it! Or just provide the idea) solution that is the limit of the solution of the dissipative problem, in the *ideal* limit: when do jumps occur? When do rerefaction fans occur?
  - show multiple solutions
  - show limit of the dissipative solution

  on some simple problems, maybe starting from a scalar problem in 1-dimesnional domain, and then generalize to "more difficult" problems

- domains of **dependence** and **influence**. Show them in both unsteady and steady problems?
  - Example with compressible flows (or the p-sys) comparing unsteady and steady problems, and discussing the nature of the equations in the subsonic and supersonic regimes

