(tensor:calculus:identities)=
# Calculus identities

Here some calculus identities are listed and proved, often using Cartesian coordinates and index notation. While these identities are independent on the choice of the coordinates - as calculus is - a generic set of coordinates can be used to prove them, and Cartesian coordinates are the most convenint choice.


$$\Delta \vec{v} = \nabla (\nabla \cdot \vec{v}) - \nabla \times \nabla \times \vec{v} \ .$$ (eq:identity:laplacian)

```{dropdown} Proof.

Uusing the identity

$$\varepsilon_{ijk} \varepsilon_{ilm} = \delta_{jl} \delta_{km} - \delta_{jm} \delta_{kl}$$

and index notation for Cartesian coordinates,

$$\begin{aligned}
 \big( \nabla \times \nabla \times \vec{v} \big)_i 
 & = \hat{e}_i \cdot \big( \nabla \times \nabla \times \vec{v} \big) = \\
 & = \varepsilon_{ijk} \, \partial_j ( \varepsilon_{klm} \, \partial_l v_m ) = \\
 & = \varepsilon_{kij} \, \varepsilon_{klm} \partial_{jl} v_m = \\
 & = ( \delta_{il} \, \delta_{jm} - \delta_{im} \, \delta_{jl} ) \, \partial_{jl} v_m = \\
 & = \partial_{ij} \, v_j - \partial_{jj} \, v_i = \\
 & = \hat{e}_i \cdot \big( \nabla (\nabla \cdot \vec{v}) - \Delta \vec{v} \big) = 
 & = \big( \nabla (\nabla \cdot \vec{v}) - \Delta \vec{v} \big)_i \ .
\end{aligned}$$


```


