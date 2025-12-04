(tensor:algebra:unitary-tensors)=
# Unitary and rotation tensors

Some notes in the introduction to classical mechanics: [Rotations: Tensor formalism for rotations](https://basics2022.github.io/bbooks-physics-mechanics/ch/kinematics-rotations-tensors.html).

**todo** Move the mathematical treatment here?

**todo** Discuss vector operations that are invariant under 3-dimensional rotation and other unitary tensor applications (i.e. reflections). These properties are useful to prove the general expression of [isotropic tensors](tensor:algebra:isotropic-tensors).

## Invariant operations under rotations and unitary transformations

Proof that/if:

* the only independent invariant operations producing a scalar with **two** vectors $\mathbf{u}$, $\mathbf{v}$ are

   $$\begin{aligned}
     & \mathbf{u} \cdot \mathbf{u} = |\mathbf{u}|^2 \\
     & \mathbf{v} \cdot \mathbf{v} = |\mathbf{v}|^2 \\
     & \mathbf{u} \cdot \mathbf{v}
   \end{aligned}$$

* the only independent invariant operations producing a scalar with **three** vectors $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ are

   $$\begin{aligned}
     & \mathbf{u} \times \mathbf{v} \cdot \mathbf{w}
   \end{aligned}$$

* the only independent invariant operations producing a scalar with **four** vectors $\{ \mathbf{u}^{(i)} \}_{i=1:4}$ are

   $$\begin{aligned}
     \mathbf{u}^{(k_1)} \cdot \mathbf{u}^{(k_2)} \ \mathbf{u}^{(k_3)} \cdot \mathbf{u}^{(k_4)} \ ,
   \end{aligned}$$

   with every index $k_j$ independently ranging from $1$ to $4$.
