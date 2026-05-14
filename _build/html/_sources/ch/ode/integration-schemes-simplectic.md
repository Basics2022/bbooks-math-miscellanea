(ode:integration-schemes:simplectic)=
# Simplectic integrators

For Hamiltonian systems (see [Classical Mechanics: Hamiltonian Mechanics](https://basics2022.github.io/bbooks-physics-mechanics/ch/hamilton.html)), simplectic integrators preserve the volume in phase space.

$$\begin{aligned}
  \dot{\mathbf{p}} & =-\partial_{\mathbf{q}} H \\
  \dot{\mathbf{q}} & = \partial_{\mathbf{p}} H \\
\end{aligned}$$

```{dropdown} Preservation of volume in phase space for Hamiltonian systems
:open:

Let $V_t$ a material domain in phase space. The derivative of its volume reads

$$\begin{aligned}
  \frac{d}{dt} \int_{V_t} 1
  & = \int_{V_t} \int_{V_t} \partial_t 1 + \oint_{\partial V_t} \mathbf{u} \cdot \hat{\mathbf{n}} = \\
  & = \oint_{\partial V_t} \left( \partial_{\mathbf{p}} H, - \partial_{\mathbf{q}} H \right) \cdot \hat{\mathbf{n}} = \\
  & = \int_{V_t} \nabla_{\mathbf{q}} \cdot \nabla_{\mathbf{p}} H - \nabla_{\mathbf{p}} \cdot \nabla_{\mathbf{q}} H = \\
  & = 0 \ .
\end{aligned}$$

having applied Reynolds' transport theroem in the phase space, with $\mathbf{u} = \frac{d \mathbf{r}}{dt} = \left( \partial_{\mathbf{p}} H, -\partial_{\mathbf{q}} H \right)$ the "velocity" in the phase space, with the state $\mathbf{r} = ( \mathbf{q}, \mathbf{p} )$, and $\hat{\mathbf{n}}$ the  unit normal vector pointing outwards. In the last steps, Hamilton equations are used to write velocity components as a function of partial derivatives of the Hamiltonian function, and divergence theorem is used in the phase space to transform the surface integral to a volume integral. The last step reads in components reads

$$\nabla_{\mathbf{q}} \cdot \nabla_{\mathbf{p}} H - \nabla_{\mathbf{p}} \cdot \nabla_{\mathbf{q}} H = \frac{\partial^2 H}{\partial q^i \partial p_i} - \frac{\partial^2 H}{\partial p^i \partial q_i} = 0 \ ,$$

under the assumption of sufficient regularity required by the Schwartz theorem about mixed partial derivatives.


```

**Algorithms - examples:**
* Verlet: simplectic, time reversible
* ...

**Applications - examples:**
* Integration of spatial dynamics: motion of planets,...
* ...


