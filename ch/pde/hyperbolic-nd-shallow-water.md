(pde:hyperbolic:nd:shallow-water)=
# Shallow water

(pde:hyperbolic:nd:shallow-water:integral)=
## Integral equations

* Intgral equation for a control volume at rest $V$
* Intgral equation for an arbitrary domain $v_t$, with Reynolds' transport theorem

(pde:hyperbolic:nd:shallow-water:integral:jump)=
### Jump conditions

* From the integral equation for an arbitrary domain $v_t$, collapsed on a surface

(pde:hyperbolic:nd:shallow-water:differential)=
## Differential equations

* In regions where the fields are smooth, from integral to differential equations with "divergence theorem"

(pde:hyperbolic:nd:shallow-water:differential:spectrum)=
### Spectral decomposition

* Eigenvalues, right and left eigenvectors
* Characteristic lines/surfaces, and compatibility conditions

(pde:hyperbolic:nd:shallow-water:riemann)=
## Riemann problem

* Useful in numerical schemes in finite volume methods, using Godunov flux

(pde:hyperbolic:nd:shallow-water:riemann:roe)=
### Linearization - Roe intermediate state

* Local linearization of the problem, to reduce the computational cost of solving non-linear Riemann problems at all the interfaces in a grid in FVM

(pde:hyperbolic:nd:shallow-water:bc)=
## Boundary conditions

* characteristic-based
* wall
* ...

