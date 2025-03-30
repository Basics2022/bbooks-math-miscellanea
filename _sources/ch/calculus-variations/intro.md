(calculus-variations:intro)=
# Introduction to Calculus of Variations

Calculus of variation deals with variations - i.e. "small changes" - of functions and functionals. 

The meaning of the term functional may vary on the subfield of interest. In the field of calculus of variation, a **functional** can be defined as a function of function, i.e. a function whose argument is another function.

```{dropdown} Fields and applications
Fields and applications related to calculus of variations (give some examples below):
- gradient-based techniques like some methods in:
  - optimization, either free or constrained (via Lagrange multiplier methods)
  - sensitivity
- classical mechanics and physics in general: 
  - analytical mechanics: [Lagrangian formulation](https://basics2022.github.io/bbooks-physics-mechanics/ch/lagrange.html) and [Hamiltonian formulation](https://basics2022.github.io/bbooks-physics-mechanics/ch/hamilton.html) of classical mechanics
- ...
```

```{dropdown} Examples
- Lagrange equations for general problem
- examples:
  - brachistochrone for minimum time,...
  - catenary, i.e. static solution of wire and cables with neglibile bending stiffness
  - isoperimetric inequality, i.e. circle is the plane closed curve with given perimeter enclosing the largest area
- sensitivity of results to parameters. Some interesting sensitivity, both in time and trasnformed domains
  - characteristics of a system:
    - equilibria
    - eigenvalues
    - ...
- optimal control methods
```

(calculus-variations:lagrange)=
## Lagrange equations

Given the functional $S$, with arguments a function $q(t)$ and the independent variable $t$,

$$S[q(t),t] = \int_{t=t_0}^{t_1} L(\dot{q}(t), \, q(t), \, t) \, dt$$

its variation w.r.t. the function $q(t)$ reads

$$\delta S[q(t), t] = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \left( S[q(t)+\varepsilon w(t), \, t] - S[q(t),\, t]\right)$$

where the function $w(t)$ is arbitrary, among those satisfying the constraint of the problems: as an example here, if the function $q(t)$ has prescribed values $q^*$ for some values of the independent variable, $t^*$, the variation $w(t)$ of the function $q(t)$ is zero there, $w(t^*)$ so that the variated function $q(t) + \varepsilon w(t)$ satisfies the constraint as well, i.e. $q(t^*) + \varepsilon w(t^*) = q^*$.

**Variation involves only small changes of function arguments**, since these ones are the elements that can be effectively changed, while the independent variable is not.

Direct computation of the variation gives

$$\begin{aligned}
\delta S[q(t), t]
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \left( S[q(t)+\varepsilon w(t), \, t] - S[q(t),\, t]\right) = \\
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \left( \int_{t = t_0}^{t_1}  L(\dot{q}(t)+\varepsilon w(t), \, q(t)+\varepsilon w(t), \, t) - \int_{t=t_0}^{t_1}  L(\dot{q}(t), \, q(t), \, t) \, dt \right) = \\
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \int_{t = t_0}^{t_1} \left( L(\dot{q}(t)+\varepsilon w(t), \, q(t)+\varepsilon w(t), \, t) - L(\dot{q}(t), \, q(t), \, t) \right) \, dt = \\
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \int_{t = t_0}^{t_1} \left\{ L(\dot{q}(t), \, q(t), \, t) + \varepsilon \left[ \frac{\partial L}{\partial \dot{q}} \dot{w}(t) + \frac{\partial L}{\partial q} w(t) \right] + o(\varepsilon) - L(\dot{q}(t), \, q(t), \, t) \right\} \, dt = \\
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \int_{t = t_0}^{t_1} \left\{ \varepsilon \left[ \frac{\partial L}{\partial \dot{q}} \dot{w}(t) + \frac{\partial L}{\partial q} w(t) \right] + o(\varepsilon) \right\} \, dt = \\
  & = \int_{t = t_0}^{t_1} \left\{ \frac{\partial L}{\partial \dot{q}} \dot{w}(t) + \frac{\partial L}{\partial q} w(t) \right\} \, dt = \\
  & = \left.\left[ w(t) \frac{\partial L}{\partial \dot{q}} \right]\right|_{t=t_0}^{t_1} + \int_{t = t_0}^{t_1} \left\{ - \dfrac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) + \frac{\partial L}{\partial q} \right\} w(t) \, dt \ .
\end{aligned}$$

The solution depends on the boundary conditions at the extreme points $t_0$, $t_1$. **If** the value of the function $q(t)$ is prescribed in $t_0$ and $t_1$, $q(t_0) = q_0$, $q(t_1) = q_1$, then its variation is zero, $w(t_0) = w(t_1) = 0$, for the reason that has been discussed above. The variation of the functional with prescribed boundary values of the argument function thus reads

$$\delta S[q(t), t] = \int_{t = t_0}^{t_1} \left\{ - \dfrac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) + \frac{\partial L}{\partial q} \right\} \delta q(t) \, dt \ ,$$

having called $w(t) =: \delta q(t)$ to stress that is the variation of function $q(t)$. This notation - it's just notation, it has no special properties - could be useful if the functional depends on several arguments.

**Stationary conditions, $\delta S = 0$.** Stationary condition of the functional $S$ implies that $\delta S = 0$ for all the possible variations of the argument function, $\forall \delta q(t)$. This condition implies that the integrand is identically zero, i.e. **Lagrange equations**,

$$\frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}} \right) - \frac{\partial L}{\partial q} = 0 \ ,$$


<!-- (calculus-variations:lagrange:high-order-der)=  -->
```{dropdown} Higher-order derivatives

**Method 1.** If the Lagrangian function $L$ depends on higher order derivatives,

$$L \left(q^{(n)}(t), \, q^{(n-1)}(t), \, \dots, \, q'(t), \, q(t), \, t \right)$$

it's possible to recast the problem defining the $n$-dimensional function, $\mathbf{q}(t)$,

$$\mathbf{q}(t) = \left( q^0(t), q^1(t), \dots, q^{n-1}(t) \right) := \left(q(t), q'(t), \dots, q^{(n-1)}(t) \right) \ .$$

With some abuse of notation in $L$, the functional $S$ can be recasted as

$$\begin{aligned}
  S[q(t),t] 
  & = \int_{t=t_0}^{t_1} L(q^{(n)}(t), \, \dots, \, q(t), \, t) \, dt = \\
  & = \int_{t=t_0}^{t_1} L(\dot{\mathbf{q}}(t), \, \mathbf{q}(t), \, t) \, dt \ .
\end{aligned}$$

**todo** *Add constraints on components of $\mathbf{q}(t)$?*

Repeating the computation, the variation of the functional reads

$$\delta S[\mathbf{q}(t), t] = \left.\left[ \delta \mathbf{q}^T(t) \frac{\partial L}{\partial \dot{\mathbf{q}}} \right]\right|_{t=t_0}^{t_1} + \int_{t = t_0}^{t_1} \delta \mathbf{q}^T(t) \, \left\{ - \dfrac{d}{dt} \left( \frac{\partial L}{\partial \dot{\mathbf{q}}} \right) + \frac{\partial L}{\partial \mathbf{q}} \right\} \, dt \ .$$

**Method 2.** ...

<!--

(not exponents but indices of components!), so that

$$\dfrac{d}{dt} \mathbf{q}(t) = \frac{d}{dt} \left(q(t), q'(t), \dots, q^{(n-1)}(t) \right) =  \left(q'(t), q''(t), \dots, q^{(n)}(t) \right) $$
-->
```

(calculus-variations:euler-beltrami)=
### Euler-Beltrami equation

If the Lagrangian function $L$ is not an explicit function of the independent variable, $L(q'(x),q(x))$, Euler-Berltrami equation follows from the derivative of the Lagrangian,

$$\begin{aligned}
  \frac{d L}{dx} 
  & = \frac{\partial L}{\partial q'} q''(x) + \frac{\partial L}{\partial q} q' = \\
  & = \frac{\partial L}{\partial q'} q'' + \dfrac{d}{dx} \left( \frac{\partial L}{\partial q'} \right) q' = \\
  & = \dfrac{d}{dx} \left( \frac{\partial L}{\partial q'} q' \right) \ ,
\end{aligned}$$

and thus

$$
\dfrac{d}{dx} \left[ L - q' \dfrac{\partial L}{\partial q'} \right] = 0
\qquad \rightarrow \qquad
L - q' \dfrac{\partial L}{\partial q'} = C \quad \text{const.}
$$

**Note 1.** While Lagrange equations are a set of $N$ equations if the functional depends on $N$ argument functions $q_k(t)$, $k=1:N$, Euler-Beltrami equation is an equation only. Indeed for multiple argument functions

$$\begin{aligned}
  \frac{d L}{dx} 
  & = \frac{\partial L}{\partial q'_k} q''_k(x) + \frac{\partial L}{\partial q_k} q'_k = \\
  & = \frac{\partial L}{\partial q'_k} q''_k + \dfrac{d}{dx} \left( \frac{\partial L}{\partial q'_k} \right) q'_k 
    = \dfrac{d}{dx} \left( \frac{\partial L}{\partial q'_k} q'_k \right) \ ,
\end{aligned}$$

where Einstein's summation notation of repeated index is used. Euler-Beltrami thus reads

$$L(q_l'(x),q_l(x)) - q'_k(x) \frac{\partial L}{\partial q'_k}(q'_l(x), q_l(x)) = C \  .$$

**Note 2.** If the Lagrangian function is an explicit function of the independent variable $x$, $L(q'(x), q(x), x)$, it's not hard to realize that  the derivative of the Lagrangian function, along with the use of the Lagrange equation, gives

$$\dfrac{d}{dx} \left[ L - q' \dfrac{\partial L}{\partial q'} \right] = \dfrac{\partial L}{\partial x} \ .$$

```{prf:example} Euler-Beltrami with $L(q'(x),q(x),x)$, Hamiltonian, energy and E.Noether

Euler-Beltrami equation shows that if $L(q'(x), q(x))$, thus $L - q' \partial_{q'} L$ is constant, (or an integral of motion in dynamics). In analytical mechanics ([Lagrange mechanics](https://basics2022.github.io/bbooks-physics-mechanics/ch/lagrange.html), [Hamiltonian mechanics](https://basics2022.github.io/bbooks-physics-mechanics/ch/hamilton.html)), Lagrangian and Hamiltonian functions of a system read

$$\begin{aligned}
  L(\dot{q}_k(t), q_k(t), t) & = T(\dot{q},q,t) + U(q,t) \\
  H(p,q,t) & := p_k \dot{q}_k - L = \dot{q}_k \frac{\partial L}{\partial \dot{q}^k} - L \ ,
\end{aligned}$$

having used the common definition of the generalized momenta $p_k := \frac{\partial L}{\partial \dot{q}^k}$. It should be immediate to realize that the Hamiltonian is just the quantity appearing in Euler-Beltrami equation (or in its "modified version" if $\partial_t L \ne 0$), and thus

$$\dfrac{d H}{d t} = \dfrac{\partial L}{\partial t} \ .$$

In mechanics, if $\partial_t L = 0$, the Hamiltonian is a constant of motion. In this case, it can be prove that the Hamiltonian is equal to the eneergy of the system. 

```


**Classical examples.**
```{prf:example} Brachistochrone

Find the trajectory...

- Elementary length: $ds = v \, dt$
- Energy: $E(y) = \frac{1}{2} m v^2 - m g y + C$. Setting $E = 0$ at starting point, from rest, at $y_0 = 0$, it implies $C=0$; thus $v = \sqrt{2gy}$
- $x(s), \, y(s)$,
- $ds = \sqrt{dx^2 + dy^2} = \sqrt{1+y'^2(x)} \, dx$

$$T = \int_{t_0}^{t_1} \, dt = \int_{s_0}^{s_1} \frac{ds}{v} = \int_{x_0}^{x_1} \frac{\sqrt{1+y'^2(x)}}{\sqrt{2gy(x)}} \, dx$$

The Lagrangian doesn't explicitly depend on $x$, thus Euler-Beltrami equation can be used. Partial derivative of the Lagrangian function w.r.t. $q'$ reads

$$\frac{\partial L}{\partial y'} = ... = \frac{1}{\sqrt{2 g y} \sqrt{1+y'^2}} y' \ ,$$

and thus Euler-Beltrami equation reads

$$C = L - q' \frac{\partial L}{\partial y'} = \frac{ 1 + y'^2 - y'^2}{\sqrt{2 g y} \sqrt{1+y'^2}} = \frac{1}{\sqrt{2 g y} \sqrt{1+y'^2}}$$

Squaring $2 g C^2 = \frac{1}{y(1+y'^2)}$, it's possible to write

$$y(x) = \frac{1}{2gC^2(1+y'^2(x))} \ ,$$

Making the substitution $y(x)' = \dots$

```

```{prf:example} Catenary




```

```{prf:example} Isoperimetric problem




```


