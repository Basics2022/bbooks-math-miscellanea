(tensor:calculus:time-derivative-of-integrals)=
# Time derivative of integrals over moving domains

Some results about time derivatives over moving domains are collected here. 

(tensor:calculus:time-derivative-of-integrals:volume-density)=
## Volume density

**Reynolds transport theorem.**
Given a volume $V(t)$ with boundary $\partial V(t)$, whose points $\vec{r} \in \partial V(t)$ have velocity $\vec{v}_b$,

$$\dfrac{d}{dt} \int_{V(t)} f = \int_{V(t)} \dfrac{\partial f}{\partial t} + \oint_{\partial V(t)} f \vec{v}_b \cdot \hat{n} \ .$$

```{dropdown} "Proof"
```

(tensor:calculus:time-derivative-of-integrals:flux)=
## Flux across a surface

$$\frac{d}{dt} \int_{S(t)} \vec{f} \cdot \hat{n} = \int_{S(t)} \frac{\partial \vec{f}}{\partial t} \cdot \hat{n} + \int_{S(t)} \nabla \cdot \vec{f} \,\, \vec{v}_b \cdot \hat{n} - \int_{\partial S(t)} \vec{v}_b \times \vec{f} \cdot \hat{t} $$

```{dropdown} "Proof"
```

(tensor:calculus:time-derivative-of-integrals:work)=
## Work line integral along a line

$$\frac{d}{dt} \int_{\ell(t)} \vec{f} \cdot \hat{t} =  \int_{\ell(t)} \frac{\partial \vec{f}}{\partial t} \cdot \hat{t} + \int_{\ell(t)} \nabla \times \vec{f} \cdot \vec{v}_b \times \hat{t} + \vec{f}_B \cdot \vec{v}_B - \vec{f}_A \cdot \vec{v}_A $$

```{dropdown} "Proof"
```
