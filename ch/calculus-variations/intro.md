(calculus-variations:intro)=
# Introduction to Calculus of Variations

Given the functional $S$,

$$S[q(t),t] = \int_{t=t_0}^{t_1} L(\dot{q}(t), \, q(t), \, t) \, dt$$

its variation reads

$$\delta S[q(t), t] = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \left( S[q(t)+\varepsilon w(t), \, t] - S[q(t),\, t]\right)$$

$$\begin{aligned}
\delta S[q(t), t]
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \left( S[q(t)+\varepsilon w(t), \, t] - S[q(t),\, t]\right) = \\
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \int_{t = t_0}^{t_1} \left( L(\dot{q}(t)+\varepsilon w(t), \, q(t)+\varepsilon w(t), \, t) - L(\dot{q}(t), \, q(t), \, t) \right) \, dt = \\
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \int_{t = t_0}^{t_1} \left\{ L(\dot{q}(t), \, q(t), \, t) + \varepsilon \left[ \frac{\partial L}{\partial \dot{q}} \dot{w}(t) + \frac{\partial L}{\partial q} w(t) \right] + o(\varepsilon) - L(\dot{q}(t), \, q(t), \, t) \right\} \, dt = \\
  & = \lim_{\varepsilon \rightarrow 0} \frac{1}{\varepsilon} \int_{t = t_0}^{t_1} \left\{ \varepsilon \left[ \frac{\partial L}{\partial \dot{q}} \dot{w}(t) + \frac{\partial L}{\partial q} w(t) \right] + o(\varepsilon) \right\} \, dt = \\
  & = \int_{t = t_0}^{t_1} \left\{ \frac{\partial L}{\partial \dot{q}} \dot{w}(t) + \frac{\partial L}{\partial q} w(t) \right\} \, dt = \\
  & = \left.\left[ w(t) \frac{\partial L}{\partial \dot{q}} \right]\right|_{t=t_0}^{t_1} + \int_{t = t_0}^{t_1} \left\{ - \dfrac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) + \frac{\partial L}{\partial q} \right\} w(t) \, dt \ .
\end{aligned}$$

If $q(t_0)$, $q(t_1)$ are prescribed, then $w(t_0) = w(t_1) = 0$ and thus

$$\delta S[q(t), t] = \int_{t = t_0}^{t_1} \left\{ - \dfrac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) + \frac{\partial L}{\partial q} \right\} \delta q(t) \, dt \ ,$$

having called $w(t) = \delta q(t)$ to stress that is the variation of function $q(t)$.

**Stationary conditions, $\delta S = 0$.** Stationary condition for $\forall \delta q(t)$ implies Lagrange equation,

$$\frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}} \right) - \frac{\partial L}{\partial q} = 0 \ .$$


## Higher-order derivatives

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

**todo** *Add constraints on components of $\mathbf{q}(t)$*

Repeating the computation, the variation of the functional reads

$$\delta S[\mathbf{q}(t), t] = \left.\left[ \delta \mathbf{q}^T(t) \frac{\partial L}{\partial \dot{\mathbf{q}}} \right]\right|_{t=t_0}^{t_1} + \int_{t = t_0}^{t_1} \delta \mathbf{q}^T(t) \, \left\{ - \dfrac{d}{dt} \left( \frac{\partial L}{\partial \dot{\mathbf{q}}} \right) + \frac{\partial L}{\partial \mathbf{q}} \right\} \, dt \ .$$

**Method 2.**

<!--

(not exponents but indices of components!), so that

$$\dfrac{d}{dt} \mathbf{q}(t) = \frac{d}{dt} \left(q(t), q'(t), \dots, q^{(n-1)}(t) \right) =  \left(q'(t), q''(t), \dots, q^{(n)}(t) \right) $$
-->


