(pde:hyperbolic:entropy)=
# Convexity in hyperbolic problems

Convexity of the entropy function and the flux are assumption used discussing [physical solutions in hyperbolic problems](pde:hyperbolic:entropy).

Convexity of the entropy flux $\eta''(u) \ge 0$ is a requirement for the entropy inequality

## Examples

```{dropdown} Burgers' equation
:open:

* Flux: $F(u) = \frac{u^2}{2}$
* Entropy: $\eta(u) = \frac{u^2}{2}$
* Entropy flux: $q(u) = \frac{u^3}{3}$

so that the compatibility condition $q'(u) = F'(u) \eta'(u)$ is satisfied.

The flux is convex, $F''(u) = 1 > 0$; the entropy function is convex as well, $\eta''(u) = 1 > 0$.



```
