(tensor:calculus:time-derivative-of-integrals)=
# Time derivative of integrals over moving domains

Some results about time derivatives over moving domains are collected here. 


Link to [hand-written notes](https://basics.altervista.org/test/Math/time_derivatives_of_integrals/time_derivatives_of_integrals.html).

(tensor:calculus:time-derivative-of-integrals:volume-density)=
## Volume density

**Reynolds transport theorem.**
Given a volume $V(t)$ with boundary $\partial V(t)$, whose points $\vec{r} \in \partial V(t)$ have velocity $\vec{v}_b$,

$$\dfrac{d}{dt} \int_{V(t)} f = \int_{V(t)} \dfrac{\partial f}{\partial t} + \oint_{\partial V(t)} f \vec{v}_b \cdot \hat{n} \ .$$

```{dropdown} "Proof"
:open:

$$\begin{aligned}
  \dfrac{d}{dt} \int_{v(t)} f(\vec{r}, t) \, dt 
  & = \lim_{\Delta t \rightarrow 0 } \frac{1}{\Delta t} \left[ \int_{v(t+\Delta t)} f(\vec{r}, t+\Delta t) - \int_{v(t)} f(\vec{r}, t)  \right] = \\
  & = \lim_{\Delta t \rightarrow 0 } \frac{1}{\Delta t} \left[ \int_{v(t)} \big\{ f(\vec{r}, t+\Delta t) - f(\vec{r}, t) \big\} + \int_{\Delta v(t;\Delta t)} f(\vec{r}, t) \right] = \\
  & = \lim_{\Delta t \rightarrow 0 } \frac{1}{\Delta t} \left[ \int_{v(t)} \left\{ \Delta t \,  \dfrac{ \partial f}{\partial t}( \vec{r}, t) + o(\Delta t) \right\} + \oint_{\partial v(t)} \left\{ \Delta t \, \vec{v}_b \cdot \hat{n} \, f(\vec{r}, t) + o(\Delta t) \right\} \right] = \\
  & = \int_{v(t)} \dfrac{\partial f}{\partial t} + \oint_{\partial v(t)} f \vec{v}_b \cdot \hat{n} \ .
\end{aligned}$$


```

(tensor:calculus:time-derivative-of-integrals:flux)=
## Flux across a surface

$$\frac{d}{dt} \int_{S(t)} \vec{f} \cdot \hat{n} = \int_{S(t)} \frac{\partial \vec{f}}{\partial t} \cdot \hat{n} + \int_{S(t)} \nabla \cdot \vec{f} \,\, \vec{v}_b \cdot \hat{n} - \int_{\partial S(t)} \vec{v}_b \times \vec{f} \cdot \hat{t} $$

```{dropdown} "Proof"
:open:

$$\begin{aligned}
  \dfrac{d}{dt} \int_{s(t)} \vec{f}(\vec{r}, t) \cdot \hat{n} \, dt 
  & = \lim_{\Delta t \rightarrow 0 } \frac{1}{\Delta t} \left[ \int_{s(t+\Delta t)} \vec{f}(\vec{r}, t+\Delta t) \cdot \hat{n}(\vec{r}, t+\Delta t) - \int_{s(t)} f(\vec{r}, t) \cdot \hat{n}(\vec{r}, t) \right] = \\
  & = \lim_{\Delta t \rightarrow 0 } \frac{1}{\Delta t} \left[ \int_{s(t+\Delta t)} \vec{f}(\vec{r}, t+\Delta t) \cdot \hat{n}(\vec{r}, t+\Delta t) - \int_{s(t)} f(\vec{r}, t) \cdot \hat{n}(\vec{r}, t) \right. + \\
  & \left. \qquad \qquad - \int_{s(t)} \vec{f}(\vec{r}, t + \Delta t) \cdot \hat{n}(\vec{r}, t) + \int_{s(t)} \vec{f}(\vec{r}, t + \Delta t) \cdot \hat{n}(\vec{r}, t) \right] = \\
  & = \lim_{\Delta t \rightarrow 0} \dfrac{1}{\Delta t} \left[ \int_{s(t)} \Delta t \dfrac{\partial \vec{f}}{\partial t} \cdot \hat{n} + o(\Delta t)  + \oint_{\partial \Delta v(t;\Delta t)} \vec{f} \cdot \hat{n} - \oint_{\partial s(t)} \Delta t \vec{f} \cdot \hat{t} \times \vec{v}_b \right]= \\
  & = \int_{s(t)} \dfrac{\partial \vec{f}}{\partial t} \cdot \hat{n} + \int_{s} \nabla \cdot \vec{f} \, \vec{v}_b \cdot \hat{n} - \oint_{\partial s(t)} \vec{v}_b \times \vec{f} \cdot \hat{t} \ .
\end{aligned}$$


having used

$$\oint_{\partial \Delta v(t;\Delta t)} \vec{f} \cdot \hat{n} = \int_{\Delta v} \nabla \cdot \vec{f} = \Delta t \int_{s} \nabla \cdot \vec{f} \, \hat{n} \cdot \vec{v}_b + o(\Delta t)$$

```

(tensor:calculus:time-derivative-of-integrals:work)=
## Work line integral along a line

$$\frac{d}{dt} \int_{\ell(t)} \vec{f} \cdot \hat{t} =  \int_{\ell(t)} \frac{\partial \vec{f}}{\partial t} \cdot \hat{t} + \int_{\ell(t)} \nabla \times \vec{f} \cdot \vec{v}_b \times \hat{t} + \vec{f}_B \cdot \vec{v}_B - \vec{f}_A \cdot \vec{v}_A $$

```{dropdown} "Proof"
:open:

$$\begin{aligned}
  \dfrac{d}{dt} \int_{\ell(t)} \vec{f}(\vec{r}, t) \cdot \hat{t}(\vec{r},t) \, dt 
  & = \lim_{\Delta t \rightarrow 0 } \frac{1}{\Delta t} \left[ \int_{\ell(t+\Delta t)} \vec{f}(\vec{r}, t+\Delta t) \cdot \hat{t}(\vec{r}, t+\Delta t) - \int_{\ell(t)} \vec{f}(\vec{r}, t) \cdot \hat{t}(\vec{r}, t) \right] = \\
  & = \lim_{\Delta t \rightarrow 0 } \frac{1}{\Delta t} \left[ \int_{\ell(t+\Delta t)} \vec{f}(\vec{r}, t+\Delta t) \cdot \hat{t}(\vec{r}, t+\Delta t) - \int_{\ell(t)} f(\vec{r}, t) \cdot \hat{t}(\vec{r}, t) \right. + \\
  & \left. \qquad \qquad - \int_{\ell(t)} \vec{f}(\vec{r}, t + \Delta t) \cdot \hat{t}(\vec{r}, t) + \int_{\ell(t)} \vec{f}(\vec{r}, t + \Delta t) \cdot \hat{t}(\vec{r}, t) \right] = \\
  & = \lim_{\Delta t \rightarrow 0 } \frac{1}{\Delta t} \left[ \int_{\ell(t+\Delta t)} \Delta t \, \dfrac{\partial \vec{f}}{\partial t}(\vec{r}, t+\Delta t) \cdot \hat{t}(\vec{r}, t+\Delta t) + \right. \\
  & \left. \qquad \qquad + \oint_{\partial \Delta s(t)} f(\vec{r}, t) \cdot \hat{t}(\vec{r}, t) - \Delta t \vec{f}_A \cdot \vec{v}_A + \Delta t \vec{f}_B \cdot \vec{v}_B + o(\Delta t) \right] =  \\
  & = \int_{\ell(t)} \frac{\partial \vec{f}}{\partial t} \cdot \hat{t} + \int_{\ell(t)} \nabla \times \vec{f} \cdot \vec{v}_b \times \hat{t} + \vec{f}_B \cdot \vec{v}_B - \vec{f}_A \cdot \vec{v}_A  \ .
\end{aligned}$$


having used

$$\oint_{\partial \Delta s(t;\Delta t)} \vec{f} \cdot \hat{t} = \int_{\Delta s} \hat{n} \cdot \nabla \times \vec{f} = \Delta t \int_{\ell} \nabla \times \vec{f} \cdot \hat{v}_b \times \vec{t} + o(\Delta t)$$


```
