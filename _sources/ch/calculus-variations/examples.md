(calculus-variations:examples)=
# Examples

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


