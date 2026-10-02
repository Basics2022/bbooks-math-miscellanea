(calculus-variations:examples)=
# Examples

```{dropdown} Contents
:open:

**Geometry.** [Shortest path](calculus-variations:examples:line-length)

**Physics.** [Fermat principle](calculus-variations:examples:fermat) in optics; [Lagrange equations in classical mechanics](calculus-variations:examples:lagrange-equations:classical-mechanics); [Lagrange equations in special relativity](calculus-variations:examples:lagrange-equations:special-relativity); [Lagrange equations in quantum mechanics](calculus-variations:examples:lagrange-equations:quantum-mechanics)


```


(calculus-variations:examples:line-length)=
## Shortest path

Shortest path between two given points $A$, $B$. The length of a curve $\gamma_{AB}$ connecting the two points reads

$$L_{\gamma_{AB}} = \int_{\gamma_{AB}} ds \ ,$$

with $s$ the arc-length parameter. The value of $s$ at the extremes of integration **is not independent** on the curve $\gamma_{AB}$, and thus on the result. In order to write the integrals w.r.t. a parameter with given values at the extreme points, a change of parameter is required. Let's define a parameter $\ell$, so that the curve in space can be represented as $\gamma: \, \mathbf{r}(t)$, $t \in [t_A, t_B]$, with $t_A$, $t_B$ given, and $\mathbf{r}(t_A) = \mathbf{r}_A$, $\mathbf{r}(t_B) = \mathbf{r}_B$ given. The elementary length $ds$ becomes

$$| d \mathbf{r} | = \underbrace{| \mathbf{r}'(s)|}_{=1, \, \text{by def of $s$}} ds = | \mathbf{r}'(\ell) | \, d \ell \ .$$

The integral thus becomes

$$L_{\gamma_{AB}} = L[\mathbf{r}(\ell)] = \int_{\ell_A}^{\ell_B} |\mathbf{r}'(\ell)| \, d \ell \ ,$$

where the dependence on the curve $\mathbf{r}(\ell)$ is made explicit, and the values of the parameter $\ell$ at the extreme is given.
Variation of the functional reads

$$\begin{aligned}
  \delta L
  & = \delta \int_{\ell_A}^{\ell_B} |\mathbf{r}'(\ell)| \, d \ell = \\
  & = \int_{\ell_A}^{\ell_B} \delta |\mathbf{r}'(\ell)| \, d \ell = \\
  & = \int_{\ell_A}^{\ell_B} \delta \mathbf{r}' \cdot \dfrac{\mathbf{r}'}{|\mathbf{r}'|} d \ell = \\
  & = \underbrace{ \left.\delta \mathbf{r} \cdot \hat{\mathbf{t}} \right|_{\ell_A}^{\ell_B}}_{= 0} - \int_{\ell_A}^{\ell_B} \delta \mathbf{r} \cdot \dfrac{d \hat{\mathbf{t}}}{d \ell} d \ell \ ,
\end{aligned}$$

being $\hat{\mathbf{t}}(\ell) = \frac{\mathbf{r}'(\ell)}{|\mathbf{r}'(\ell)|}$, the unit-length tangent vector to the curve. Stationariety of $L$, for any possible variation $\delta \mathbf{r}(\ell)$ implies

$$\dfrac{d \hat{\mathbf{t}}}{d \ell} = \mathbf{0} \ ,$$

Thus, the solution reads $\mathbf{r}(\ell) = \alpha \hat{\mathbf{t}} \, \ell + \mathbf{r}_0$, and prescribing the boundary conditions 

$$\mathbf{r}(\ell) = \mathbf{r}_A + \frac{\ell-\ell_A}{\ell_B-\ell_A} \left( \mathbf{r}_B-\mathbf{r}_A \right) \ .$$

```{dropdown} Details about the integration
:open:


```


(calculus-variations:examples:fermat)=
## Fermat principle

In geometrical optics, Fermat principles asserts that a light ray between two points represent the path with the shortest travelling time connecting them. Let $\gamma$ a curve in space. The travelling time of a light ray with speed $c$ reads

$$T = \int_{\gamma_{AB}} dt = \int_{\gamma_{AB}} \dfrac{1}{c} d s \ ,$$

begin $ds = c dt$. Let $\ell$ be a parameter, so that $\gamma: \, \mathbf{r}(\ell)$ is a parametrization of the curve, with the extreme points independent from the result. The speed of light may depend on the position in space, $c(\mathbf{r})$, and it can be written as a function of the speed of light in vacuum and the refractive index $n(\mathbf{r})$ as $c(\mathbf{r}) = \frac{c_0}{n(\mathbf{r})}$. Making the dependence on $\mathbf{r}(\ell)$, $\mathbf{r}'(\ell)$ explicit in the functional,

$$T[\mathbf{r}(\ell)] = \int_{\ell_A}^{\ell_B} n(\mathbf{r}(\ell)) \, |\mathbf{r}'(\ell)| \, d \ell \ .$$

Fermat principle reads

$$\begin{aligned}
  0
  & = \delta T = \\
  & = \delta  \int_{\ell_A}^{\ell_B} n(\mathbf{r}(\ell)) \, |\mathbf{r}'(\ell)| \, d \ell = \\
  & = \int_{\ell_A}^{\ell_B} \left\{ \delta \mathbf{r} \cdot \nabla_{\mathbf{r}} n |\mathbf{r}|' + \delta \mathbf{r}' \cdot \frac{\mathbf{r}'}{|\mathbf{r}'|} n(\mathbf{r}) \right\} \, d \ell = \\ 
  & = \int_{\ell_A}^{\ell_B} \delta \mathbf{r} \cdot \left\{ \nabla_{\mathbf{r}} n \, |\mathbf{r}|' - \dfrac{d}{d \ell} \left( \frac{\mathbf{r}'}{|\mathbf{r}'|} n(\mathbf{r}) \right) \right\} \, d \ell + \underbrace{ \left. \delta \mathbf{r} \cdot \frac{\mathbf{r}'}{|\mathbf{r}'|} n(\mathbf{r}) \right|_{\ell_A}^{\ell_B}}_{=0} \ , 
\end{aligned}$$

From the arbitrarieness of $\delta \mathbf{r}$,

$$\begin{aligned}
  0 
  & = \dfrac{d}{d \ell} \left( n(\mathbf{r}(\ell)) \dfrac{\mathbf{r}'(\ell)}{|\mathbf{r}'(\ell)|} \right) - |\mathbf{r}'(\ell)| \, \nabla n(\mathbf{r}(\ell)) = \\
  & = \dfrac{\mathbf{r}'}{|\mathbf{r}|} \mathbf{r}' \cdot \nabla n - n \dfrac{d}{d \ell} \left( \dfrac{\mathbf{r}'}{|\mathbf{r}'|} \right) - |\mathbf{r}'| \nabla n = \\
  & = | \mathbf{r}' | \left[ \mathbb{I} - \dfrac{\mathbf{r}' \cdot \mathbf{r}'}{|\mathbf{r}'|^2} \right] \cdot \nabla n - n \dfrac{d}{d\ell} \left( \dfrac{\mathbf{r}'}{|\mathbf{r}'|} \right) \ . 
\end{aligned}$$

and thus

$$\mathbb{P}_{\perp \hat{\mathbf{t}}} \cdot \nabla n = \dfrac{n}{|\mathbf{r}'|} \dfrac{d \hat{\mathbf{t}}}{d \ell} \ ,$$

or, re-introducting the "physical" variable $s$ (the arc-length is the parameter with physical, geometrical, non arbitrary meaning; the equations should be invariant from the parametrization, so we should be happy of the following result, written in invariant form),

$$\mathbb{P}_{\perp \hat{\mathbf{t}}} \cdot \nabla n = n \dfrac{d \hat{\mathbf{t}}}{ds} \ .$$ (eq:variations:fermat:invariant)

being $\mathbb{P}_{\perp \hat{\mathbf{t}}}$ the orthogonal projector in the direction perpendicular to the unit tangent vector $\hat{\mathbf{t}}$.
Using the results of [geometry of curves](differential-geometry:intro), the derivative $\hat{\mathbf{t}}'(s) = \kappa(s) \hat{\mathbf{n}}(s)$, being $\hat{\mathbf{n}}$ the unit normal vector pointing towards the local center of curvature (center of the osculator circle, tangent with the same second order derivative), and $\kappa(s) = \frac{1}{R(s)}$ is the local curvature, and $R(s)$ the radius of curvature (the radius of the osculator circle). Thus

$$\kappa \hat{\mathbf{n}} = \left[ \mathbb{I} - \hat{\mathbf{t}} \otimes \hat{\mathbf{t}} \right] \cdot \frac{\nabla n}{n}$$

Projecting this equation on the local Frenet basis $\{ \hat{\mathbf{t}}, \hat{\mathbf{n}}, \hat{\mathbf{b}} \}$,

$$\left\{ \begin{aligned}
  t: & \, 0 = \frac{1}{n} \hat{\mathbf{t}} \cdot \nabla n \\
  n: & \, \kappa = \frac{1}{n} \hat{\mathbf{n}} \cdot \nabla n \\
  b: & \, 0 = \frac{1}{n} \hat{\mathbf{b}} \cdot \nabla n \\
\end{aligned} \right.$$

(calculus-variations:examples:lagrange-equations:classical-mechanics)=
## Lagrange equations in classical mechanics


(calculus-variations:examples:lagrange-equations:special-relativity)=
## Lagrange equations in special relativity

(calculus-variations:examples:lagrange-equations:special-relativity:tensor)=
### Using tensor formalism

Equations of motion and physical principles **must** be written using physical properties, and thus be independent from an arbitrary parametrization.

**Strong formulation.** Let the equation of motion of a particle be

$$m \dfrac{d \mathbf{U}}{d \tau} = \mathbf{K} \ ,$$

with $m$ the rest mass, $\tau$ the proper time, $\mathbf{U} = \frac{d \mathbf{X}}{d \tau}$ the 4-velocity, and $\mathbf{K}$ the 4-force. 

**Weak formulation.** Multiplying by an arbitrary test 4-vector $\mathbf{W}(\tau)$ and integrating over an arbitrary interval $\tau \in [ \tau_0, \tau_1]$,

$$\begin{aligned}
  0 
  & = \int_{\tau_0}^{\tau_1} \mathbf{W} \cdot \left\{ m \dfrac{d \mathbf{U}}{d \tau} - \mathbf{K} \right\} d \tau \ .
\end{aligned}$$

The parametrization of the trajectory is changed from $\tau$ to an arbitrary parameter $\lambda$, so that $\mathbf{X}_{0,1} = \mathbf{X}(\tau_{0,1}) = \mathbf{X}(\tau(\lambda_{0,1}))$ are prescribed for given values $\lambda_{0,1}$. As the invariant $d \tau$ is defined through

$$c^2 d \tau^2 = d s^2 = d \mathbf{X} \cdot d \mathbf{X} = \mathbf{X}'(\lambda) \cdot \mathbf{X}'(\lambda) \, d \lambda^2 \ ,$$

the relation between the differentials and the rule of derivation of composite functions read

$$d \tau = \dfrac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c} \, d \lambda \qquad , \qquad \dfrac{d}{d \tau} = \dfrac{d \lambda}{d \tau} \dfrac{d}{d \lambda} = \dfrac{c}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \dfrac{d}{d \lambda} \ .$$

The velocity vector becomes 

$$\mathbf{U} = \dfrac{d \mathbf{X}}{d \tau} = \dfrac{d \lambda}{d \tau} \dfrac{d \mathbf{X}}{d \lambda} = \dfrac{c}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \mathbf{X}' \ . $$

The integral thus becomes

$$\begin{aligned}
  0
  & = \int_{\tau_0}^{\tau_1} \mathbf{W} \cdot \left\{ m \dfrac{d \mathbf{U}}{d \tau} - \mathbf{K} \right\} d \tau = \\
  & = \int_{\lambda_0}^{\lambda_1} \mathbf{W} \cdot \left\{ m \dfrac{c}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \left( \dfrac{c}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \mathbf{X}' \right)' - \mathbf{K} \right\} \dfrac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c} d \lambda = \\
  & = \int_{\lambda_0}^{\lambda_1} \mathbf{W} \cdot \left( \dfrac{mc}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \mathbf{X}' \right)' \, d \lambda - \int_{\lambda_0}^{\lambda_1} \mathbf{W} \cdot \mathbf{K} \dfrac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c} d \lambda = \\
\end{aligned}$$

**Lagrange mechanics** immediately follows choosing the test function $\mathbf{W} = \delta \mathbf{X}$.

* Free particle. For a free particle, $\mathbf{K} = \mathbf{0}$.

   $$\begin{aligned}
     0 
     & = \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \left( \dfrac{mc}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \mathbf{X}' \right)' \, d \lambda = \\
     & = \underbrace{\left. \left[ \delta \mathbf{X} \cdot \dfrac{mc}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \mathbf{X}'  \right)  \right|_{\lambda_0}^{\lambda_1}}_{= 0} - \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X}' \cdot \dfrac{mc}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \mathbf{X}' \, d \lambda = \\
     & = - \delta \int_{\lambda_0}^{\lambda_1} mc \, \sqrt{\mathbf{X}' \cdot \mathbf{X}'} \, d \lambda = \\
     & = - \delta \int_{\tau_0}^{\tau_1} mc^2 \, d \tau = \\
     & = - \delta \int_{s_0}^{s_1} mc \, d s = \\
     & = \delta S \ ,
   \end{aligned}$$

   where the change of the independent parameters is made after the variation is put outside the integral $\int_{\lambda_0}^{\lambda_1}$, with given extreme values.

* Particle subjecd to Lorentz force, 

   $$\mathbf{K} = q \mathbf{F}(\mathbf{X}) \cdot \mathbf{U} = q \mathbf{F}(\mathbf{X}) \frac{c}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \mathbf{X}' \ .$$

   The second integral becomes

   $$\begin{aligned}
     - \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \mathbf{K} \dfrac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c} d \lambda 
     & = - q \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \mathbf{F} \cdot \mathbf{U} \dfrac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c} d \lambda = \\ 
     & = - q \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \mathbf{F} \cdot \mathbf{X}' \, d \lambda = \\
     & = - q \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \left[ \nabla \mathbf{A} - \nabla^T \mathbf{A} \right] \cdot \mathbf{X}' \, d \lambda = && \text{(see details, below)} \\
     & = - \delta \int_{\lambda_0}^{\lambda_1} q \mathbf{A}(\mathbf{X}) \cdot \mathbf{X}' \, d \lambda = \\
     & = - \delta \int_{\tau_0}^{\tau_1} q \mathbf{A}(\mathbf{X}) \cdot \mathbf{U} \, d \tau
   \end{aligned}$$

   The variational principle thus reads

   $$\begin{aligned}
     0 & = \delta S = \\
       & = \delta \int_{\tau_0}^{\tau_1} \left\{ - m c^2 - q \mathbf{A}(\mathbf{X}(\tau)) \cdot \mathbf{U}(\tau) \right\} \, d \tau = \\
       & = \delta \int_{\lambda_0}^{\lambda_1} \left\{ - m c \sqrt{\mathbf{X}'(\lambda) \cdot \mathbf{X}'(\lambda)} - q \mathbf{A}\left(\mathbf{X}(\lambda)\right) \cdot \mathbf{X}'(\lambda) \right\} \, d \lambda \ .
   \end{aligned}$$

   ```{dropdown} EM field force - details
   :open:

   $$\begin{aligned}
     \delta \int_{\lambda_0}^{\lambda_1} \mathbf{A}(\mathbf{X}) \cdot \mathbf{X}' \, d \lambda
     & =
       \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \nabla \mathbf{A}(\mathbf{X}) \cdot \mathbf{X}' \, d \lambda
     + \int_{\lambda_0}^{\lambda_1} \mathbf{A}(\mathbf{X}) \cdot \delta \mathbf{X}' \, d \lambda \\
     & =
       \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \nabla \mathbf{A}(\mathbf{X}) \cdot \mathbf{X}' \, d \lambda
     + \left[ \mathbf{A}(\mathbf{X}) \cdot \delta \mathbf{X} \right]_{\lambda_0}^{\lambda_1} - \int_{\lambda_0}^{\lambda_1} \dfrac{d}{d \lambda} \mathbf{A}(\mathbf{X}(\lambda)) \cdot \delta \mathbf{X} = \\
     & = 
       \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \nabla \mathbf{A}(\mathbf{X}) \cdot \mathbf{X}' \, d \lambda
     - \int_{\lambda_0}^{\lambda_1} \mathbf{X}' \cdot \mathbf{A}(\mathbf{X}(\lambda)) \cdot \delta \mathbf{X} = \\
     & = 
       \int_{\lambda_0}^{\lambda_1} \delta \mathbf{X} \cdot \left[ \nabla \mathbf{A}(\mathbf{X}) - \nabla^T \mathbf{A}(\mathbf{X}) \right] \cdot \mathbf{X}' \, d \lambda
   \end{aligned}$$

   ```
   
   ```{dropdown} From the variational principle to the equations of motion
   :open:

   $$\begin{aligned}
     0 
       & = \delta \int_{\lambda_0}^{\lambda_1} \mathcal{L}\left( \mathbf{X}(\lambda), \mathbf{X}'(\lambda), \lambda \right) \, d \lambda = \\
       & = \int_{\lambda_0}^{\lambda_1} \left\{ \delta \mathbf{X}'(\lambda) \cdot \nabla_{\mathbf{X}'} \mathcal{L} + \delta \mathbf{X}(\lambda) \cdot \nabla_{\mathbf{X}} \mathcal{L}  \right\} \, d \lambda = \\
       & = \underbrace{\left.\left[ \delta \mathbf{X} \cdot \nabla_{\mathbf{X}'} \mathcal{L} \right]\right|_{\lambda_0}^{\lambda_1}}_{=0} - \int_{\lambda_0}^{\lambda_1}  \delta \mathbf{X} \cdot \left\{ \dfrac{d}{d\lambda} \left( \nabla_{\mathbf{X}'} \mathcal{L} \right) - \nabla_{\mathbf{X}} \mathcal{L}  \right\} \, d \lambda \ ,
   \end{aligned}$$

   and, since $\delta \mathbf{X}$ must be arbitary, Lagrange equations follow

   $$\dfrac{d}{d\lambda} \left( \nabla_{\mathbf{X}'} \mathcal{L} \right) - \nabla_{\mathbf{X}} \mathcal{L} = \mathbf{0} \ .$$

   If the Lagrangian funcion is

   $$\mathcal{L}(\mathbf{X}, \mathbf{X}', \lambda) = - m c \sqrt{\mathbf{X}'(\lambda) \cdot \mathbf{X}'(\lambda)} - q \mathbf{A}\left(\mathbf{X}(\lambda)\right) \cdot \mathbf{X}'(\lambda) \ ,$$

   its derivatives are

   $$\begin{aligned}
    \nabla_{\mathbf{X}'} \mathcal{L} & = - \dfrac{m c}{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}} \mathbf{X}' - q \mathbf{A}(\mathbf{X}) = - m \mathbf{U} - q \mathbf{A} \\
    \nabla_{\mathbf{X} } \mathcal{L} & = - q \nabla \mathbf{A} \cdot \mathbf{X}' = - q \nabla \mathbf{A} \cdot \mathbf{U} \dfrac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c} \\
   \end{aligned}$$

   and 

   $$\begin{aligned}
   \dfrac{d}{d\lambda} \nabla_{\mathbf{X}'} \mathcal{L}
   & = \dfrac{d \tau}{d\lambda} \dfrac{d}{d \tau} \left( - m \mathbf{U} - q \mathbf{A} \right) = \\
   & = \dfrac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c} \dfrac{d }{d \tau} \left(- m \mathbf{U} - q \mathbf{A}(\mathbf{X}) \right) = \\
   & = \dfrac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c} \left(- m  \dfrac{d }{d \tau}\mathbf{U} - q \mathbf{U} \cdot \nabla \mathbf{A}(\mathbf{X}) \right) \ .
   \end{aligned}$$

   Putting together all the pieces of the Lagrange equations, and dividing by $\frac{\sqrt{\mathbf{X}' \cdot \mathbf{X}'}}{c}$ - different from zero, if the 3-velocity of the particle is $|\mathbf{v}| < c$ -,

   $$0 = - m \dfrac{d \mathbf{U}}{d \tau} - q \mathbf{U} \cdot \nabla \mathbf{A} + q \nabla \mathbf{A} \cdot \mathbf{U} \ ,$$

   and thus

   $$m \dfrac{d \mathbf{U}}{d \tau} = q \left[ \nabla \mathbf{A} - \nabla^T \mathbf{A} \right] \cdot \mathbf{U} \ .$$



   ```

 

(calculus-variations:examples:lagrange-equations:special-relativity:coordinates)=
### Using coordinates

With $\mathbf{X}\left( q^{\mu}(\lambda) \right)$,...


(calculus-variations:examples:lagrange-equations:quantum-mechanics)=
## Quantum Mechanics

(calculus-variations:examples:lagrange-equations:quantum-mechanics:schrodinger-eq)=
### Schrodinger equation

$$i \hbar \dfrac{d}{dt} | \Psi(t) \rangle = \hat{H} | \Psi \rangle \ , $$

Schrodinger equation for a particle with mass $m$ in a conservative force field with potential energy $V(\mathbf{r})$,in position representation, becomes

$$i \hbar \partial_t \Psi = - \dfrac{\hbar^2}{2 m} \nabla^2 \Psi + V(\mathbf{r}) \Psi \ ,$$

with $\Psi(\mathbf{r},t): \Omega \times T \rightarrow \mathbb{C}$.

```{dropdown} Derivative w.r.t. a complex number and its complex conjugate
:open:

Let a complex variable be $z = x + i y$. Any complex function can be written as a linear combination of its real and imaginary part, $f(z) = u(z) + i v(z)$, $u(z): \mathbb{C} \rightarrow \mathbb{R}$, $u(z): \mathbb{C} \rightarrow \mathbb{R}$, and reacast as a 2-dimensional function of the real and imaginary part of the independent variable, i.e. $F(x,y) = U(x,y) + i V(x,y)$.

**Holomorphic functions.** ...

$$f'(z_0) = \lim_{z \rightarrow z_0} \frac{f(z) - f(z_0)}{z-z_0}$$

[Cauchy-Riemann conditions](complex:analysis:holo-fun:cauchy-riemann) for holomorphic functions immediately follow from the way $z$ approaches $z_0$ in the complex plane.

$$\begin{aligned}
  \frac{d f}{d z} 
  & = \frac{\partial F}{\partial x} = \frac{\partial U}{\partial x} + i \frac{\partial V}{\partial x} \\
  & = \frac{\partial F}{i \, \partial y} = \frac{1}{i} \frac{\partial U}{\partial y} + \frac{\partial V}{\partial y} \\
\end{aligned}$$

```

```{dropdown} Derivative w.r.t. the conjugate conjugate variable
:open:

Let a function $f(z) = u(z) + i v(z) = U(x,y) + i V(x,y)$, with $x$, $y$ indepdendent variables. With a change of coordinates,

$$
\left\{
\begin{aligned}
 z   & = x + i y \\ 
 z^* & = z - i y
\end{aligned}\right.
\qquad , \qquad
\left\{
\begin{aligned}
 x & = \frac{1}{2} \left( z + z^* \right) \\
 y & = \frac{1}{2i} \left( z - z^* \right)
\end{aligned}\right.
$$

and thus, with the definition

$$\begin{aligned}
  \mathscr{u}(z, z^*) & = U(x(z,z^*), y(z,z^*))  \\
  \mathscr{v}(z, z^*) & = V(x(z,z^*), y(z,z^*))
\end{aligned}$$

...

```



```{dropdown} Free-style approach
:open:

Multiplying Schrodinger equation by the c.c. of a test function $f(z)$, and integrating in both time and space domain,

$$\begin{aligned}
  0 
  & = \int_{T} \int_{\Omega} f^* \left\{ - i \hbar \partial_t \Psi - \frac{\hbar^2}{2m} \partial_{kk} \Psi + V \Psi \right\} d \mathbf{r} \, dt = \\
  & = \int_{T} \int_{\Omega} \left\{ - i \hbar \, f^* \partial_t \Psi + \frac{\hbar^2}{2m} \partial_k f^* \, \partial_{k} \Psi + f^* V \Psi \right\} d \mathbf{r} \, dt - \int_{T} \oint_{\partial \Omega} \dfrac{\hbar^2}{2m} f^* n_k \partial_k \Psi \, d \mathbf{r} \, dt \ .
\end{aligned}$$

Now, let's

* add the complex conjugate
* define $f = \partial \Psi$
* set the test function equal to zero on $\partial \Omega$

$$\begin{aligned}
  0 
  & = \int_{T} \int_{\Omega} \left\{ - i \hbar \, \delta \Psi^* \partial_t \Psi + \frac{\hbar^2}{2m} \partial_k \delta \Psi^* \, \partial_{k} \Psi + \delta \Psi^* V \Psi \right\} d \mathbf{r} \, dt + \\
  & + \int_{T} \int_{\Omega} \left\{ i \hbar \, \delta \Psi \partial_t \Psi^* + \frac{\hbar^2}{2m} \partial_k \delta \Psi \, \partial_{k} \Psi^* + \delta \Psi V \Psi^* \right\} d \mathbf{r} \, dt = \\
\end{aligned}$$

Last two pairs of terms can be written as... while the first pair

$$\begin{aligned}
  \delta \left( \Psi^* \partial_t \Psi - \Psi \partial_t \Psi^* \right)
  & = \delta \Psi^* \partial_t \Psi + \Psi^* \delta \partial_t \Psi - \delta \Psi \partial_t \Psi^* - \Psi \partial_t \delta \Psi^* = \\
  & = \delta \Psi^* \partial_t \Psi + \partial_t \left( \Psi^* \delta \Psi \right) - \delta \Psi^* \partial_t \Psi - \delta \Psi \partial_t \Psi^* - \partial_t \left( \Psi \delta \Psi^* \right) + \partial_t \Psi \delta \Psi^* = \\
  & = 2 \left( \delta \Psi^* \partial_t \Psi - \delta \Psi \partial_t \Psi^* \right) + \partial_t \left( \dots \right) \ .
\end{aligned}$$

having used integration by parts and switched the variation and the partial derivative w.r.t. time (**but**, is that legal? See below {eq}`eq:calculus-variation:switch-d-delta`). Thus the variational principle - with prescribed $\delta \Psi$ at boundary of space and time domain - reads

$$0 = - \delta \int_{T} \int_{\Omega} \left\{ i \frac{\hbar}{2} \left( \Psi^* \partial_t \Psi - \Psi \partial_t \Psi^* \right) - \dfrac{\hbar^2}{2 m } \nabla \Psi^* \cdot \nabla \Psi - \Psi^* V(\mathbf{r}) \Psi \right\} d \mathbf{r} \, d t \ .$$

The function inside the integral is defined as the Lagrangian function

$$\mathcal{L}\left( \Psi, \partial_t \Psi, \partial_k \Psi \right) = i \frac{\hbar}{2} \left( \Psi^* \partial_t \Psi - \Psi \partial_t \Psi^* \right) - \dfrac{\hbar^2}{2 m } \nabla \Psi^* \cdot \nabla \Psi - \Psi^* V(\mathbf{r}) \Psi \ .$$ (eq:calculus-variation:lagrangian:schrodinger)

```

````{dropdown} Lagrange equations
:open:

Schrodinger equation can be retrieved from Lagrange equation

$$0 = \partial_t \left( \dfrac{\partial \mathcal{L}}{\partial \left( \partial_t \Psi \right)} \right) + \partial_k \left( \dfrac{\partial \mathcal{L}}{\partial \left( \partial_k \Psi \right)} \right) - \dfrac{\partial \mathcal{L}}{\partial \Psi} \ ,$$

taking the derivatives of the Lagrangian function $\mathcal{L}\left( \Psi, \partial_t \Psi, \partial_k \Psi \right)$ in formula {eq}`eq:calculus-variation:lagrangian:schrodinger`.


```{dropdown} Proof.
:open:

**todo**

```

````

```{dropdown} A more rigorous approach
:open:

Let $\Psi(q^j(\mathbf{r},t), \mathbf{r},t)$ be a function of generalized coordinates $q^j(\mathbf{r},t)$, function of the independent variables $\mathbf{r}$, t. Its partial time and space derivatives read

$$\begin{aligned}
  \partial_{t} \Psi & = \partial_t q^j \, \partial_{q^j} \Psi + \partial_t q^j \\
  \partial_{k} \Psi & = \partial_k q^j \, \partial_{q^j} \Psi + \partial_k q^j \\
\end{aligned}$$

and thus, the variation reads

$$\delta \Psi = \delta q^j \partial_{q^j} \Psi \ .$$

...

```

```{dropdown} Exchanging derivatives and variation
:open:

Let $f(q^i(x,t), x,t)$, and 

$$\begin{aligned}
  \partial_x f & = \partial_x q^i \partial_{q^i} f + \partial_x f \\
  \delta f     & = \delta q^i \partial_{q^i} f
\end{aligned}$$

Thus

<!--

$$
\delta \partial_x f = \delta q^i \partial_{q^i} \partial_x f = \delta q^i \partial_{q^i} \left( \partial_x q^k \partial_{q^k} f + \partial_x f \right)
$$

$$\begin{aligned}
\partial_x \delta f =
\partial_x \left( \delta q^i \partial_{q^i} f \right) =
\partial_x \delta q^i \partial_{q^i} f + \delta q^i \partial_{q^k} \partial_{q^i} f \partial_x q^k 
\end{aligned}$$(eq:calculus-variation:switch-d-delta)

-->

```
