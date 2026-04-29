(order-reduction:intro)=
# Order reduction of dynamical systems

Classes of order reduction methods:

* **Modal methods.** Modal methods are often useful for mechanical systems, whose governing equations are second order differential equations with symmetric mass and stiffness matrices.[^modal-adjoint]

   [^modal-adjoint]: Modal methods can be used for non-symmetric systems as well, relying on spectral decomposition of the adjoint problem (or, equivalently, to left eigenvectors).

   The behavior of a mechanical system can be often represented as a superposition of independent mass-damper-spring systems, with their individual proper eigenvalue (for under-damped systems, frequency and damping, $s_k = \sigma_k + j \omega_k$), and their shape determined by the eigenvector $\mathbf{u}_k$ (or better, usually a pair of complex conjugate eigenvalues and eigenvectors).

   If the spectrum of the forcing is known, with $\omega_{f,max}$ as the maximum frequency of the forcing, it's possible to split the modes of the system in slow (or dynamical) modes - showing dynamical response to forcing, and whose natural frequency is $\omega < \omega_{f,max}$ -, and fast modes (or static) - showing static response to forcing, and thus whose natural frequency is $\omega \gg \omega_{f,max}$.

   Two methods of modal order reduction follows: 1) [truncation of fast modes](https://basics2022.github.io/bbooks-physics-continuum-mechanics/ch/solids/small-displacements-numerics.html#truncation-and-direct-recovery-of-loads); 2) [static recovery of fast modes](https://basics2022.github.io/bbooks-physics-continuum-mechanics/ch/solids/small-displacements-numerics.html#mode-acceleration-and-static-recovery-of-fast-modes). These methods are discussed in the notes about [modal methods in structural mechanics](https://basics2022.github.io/bbooks-physics-continuum-mechanics/ch/solids/small-displacements-numerics.html).

* **[Balanced truncation](order-reduction:balanced-truncation).** Balanced truncation relies on coordinate transformation that scales the problem to equally weight reachability and observability properties. Once the coordinates have been transformed, the reduced order model is obtained truncating every modes whose reachability/controllability is below a desired threshold.

* **Energy-based.** POD...

* ...*Koopman,...*

These methods can be combined in sequences of order reductions.

