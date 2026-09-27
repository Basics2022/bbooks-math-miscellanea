(calculus-variations:extra)=
# Extra

<!--
(calculus-variations:extra:non-prescribed-extreme-s)=
## Prescribed ends but non-prescribed extreme values of the parameter $s$
-->

(calculus-variations:extra:s-parametrization)=
## Parametrization of the integral with the arc-length

Parametrization of the curve $\gamma_{AB}: \, \mathbf{r}(s)$, with a physical parameter $s \in [s_A, s_B]$ whose values at extreme points may depend on the solution itself: i.e. even though $\mathbf{r}_A$, $\mathbf{r}_B$ are prescribed, the values $s_A$, $s_B$, s.t. $\mathbf{r}_A = \mathbf{r}(s_A)$, $\mathbf{r}_B = \mathbf{r}(s_B)$, are not. The functional reads

$$S_{\gamma_{AB}} = S[\mathbf{r}(s)] = \int_{\mathbf{r} \in \gamma_{AB}} \mathcal{L}(\mathbf{r}, s) \, ds = \int_{s_A}^{s_B} \mathcal{L}(\mathbf{r}(s), s) \, ds $$

````{dropdown} Method 1.
:open:

$$\begin{aligned}
  \Delta S_{\gamma_{AB}} 
  & = S[\mathbf{r}(s_\delta)+\varepsilon \delta\mathbf{r}(s_\delta)] - S[\mathbf{r}(s)+\varepsilon \delta\mathbf{r}(s)] = \\
  & = \int_{\mathbf{r} \in \mathbf{r}(s_\delta)+\varepsilon \delta \mathbf{r}(s_\delta)} \mathcal{L}(\mathbf{r}, s_{\delta}) \, ds_{\delta} - \dots = \\
\end{aligned}$$

Here $d s_{\delta}$ is the arc-length of the elementary vector of the curve $\gamma_\delta$, $d \mathbf{r}_{\delta} = d \mathbf{r} + \varepsilon d \delta \mathbf{r}$, i.e.

$$\begin{aligned}
  d s_{\delta}^2
  & = \left( d \mathbf{r} + \varepsilon d \delta \mathbf{r} \right) \cdot \left( d \mathbf{r} + \varepsilon d \delta \mathbf{r} \right) = \\
  & = | d \mathbf{r} |^2 + 2 \varepsilon d \mathbf{r} \cdot d \delta \mathbf{r} + o(\varepsilon) = \\
  & \simeq | d \mathbf{r} |^2 \left( 1 + 2 \varepsilon \dfrac{d \delta \mathbf{r} \cdot d \mathbf{r}}{|d \mathbf{r}|^2} \right) + o(\varepsilon)  \ ,
\end{aligned}$$

so that first-order approximation reads 

$$\begin{aligned}
  d s_{\delta} 
  & = | d \mathbf{r} | \left( 1 + \varepsilon \dfrac{d \delta \mathbf{r} \cdot d \mathbf{r}}{|d \mathbf{r}|^2}  \right) = \\
  & = ds + \varepsilon \hat{\mathbf{t}} \cdot d \delta \mathbf{r} \ .
\end{aligned}$$

The first integral in the difference thus becomes

$$\begin{aligned}
  & \int_{s_{\delta} = s_{\delta,A}}^{s_{\delta,B}}  \mathcal{L}(\mathbf{r}_\delta(s_\delta), s_\delta ) \left( ds + \varepsilon \hat{\mathbf{t}} \cdot d \delta \mathbf{r} \right) \\ 
  & \qquad = \int_{s_{\delta} = s_{\delta,A}}^{s_{\delta,B}}  \left[ \mathcal{L}(\mathbf{r}(s_\delta), s_\delta ) + \varepsilon \delta \mathbf{r} \cdot \nabla \mathcal{L}(\mathbf{r}(s_\delta), s_\delta) + o(\varepsilon) \right] \left( \dfrac{ds}{d s_\delta} + \varepsilon \hat{\mathbf{t}} \cdot \frac{d \delta \mathbf{r}}{d s_\delta} \right) d s_{\delta} = \\
  & \qquad = \int_{s = s_{A}}^{s_{B}} \mathcal{L}(\mathbf{r}(s), s) \, ds + 
  \varepsilon \int_{s = s_{A}}^{s_{B}} \delta \mathbf{r} \cdot \nabla \mathcal{L}(\mathbf{r}(s), s) \, ds + \\ 
  & \qquad + \varepsilon \left.\left[ \delta \mathbf{r} \cdot \hat{\mathbf{t}} \mathcal{L} \right]\right|_{A}^{B}
  - \varepsilon \int_{s_\delta = s_{\delta,A}}^{s_{\delta,B}} \delta \mathbf{r} \cdot \dfrac{d}{ds}\left( \hat{\mathbf{t}} \mathcal{L} \right) d s_\delta
  + o(\varepsilon) = \\
  & \qquad = \int_{s = s_{A}}^{s_{B}} \mathcal{L}(\mathbf{r}(s), s) \, ds + 
  \varepsilon \int_{s = s_{A}}^{s_{B}} \delta \mathbf{r} \cdot \left\{ \nabla \mathcal{L}(\mathbf{r}(s), s) - \dfrac{d}{ds_\delta}\left( \hat{\mathbf{t}} \mathcal{L} \right) \right\} \, ds + \\ 
  & \qquad + \varepsilon \left.\left[ \delta \mathbf{r} \cdot \hat{\mathbf{t}} \mathcal{L} \right]\right|_{A}^{B}
  + o(\varepsilon) \ .
\end{aligned}$$

Thus, the variation becomes 

$$\begin{aligned}
  \delta_{\mathbf{r}} S
  & = \lim_{\varepsilon \rightarrow 0} \dfrac{1}{\varepsilon} \Delta_{\mathbf{r}} S = \\
  & = 
  \int_{s = s_{A}}^{s_{B}} \delta \mathbf{r} \cdot \left\{ \nabla \mathcal{L}(\mathbf{r}(s), s) - \dfrac{d}{ds}\left( \hat{\mathbf{t}} \mathcal{L} \right) \right\} \, ds + 
  \left.\left[ \delta \mathbf{r} \cdot \hat{\mathbf{t}} \mathcal{L} \right]\right|_{A}^{B}
\end{aligned}$$

having assumed a function $s(s_\delta)$ associating every point on curve $\gamma_{AB}$ to a value of the parameter $s_{\delta}$, and having used the rules for changing independent variables in the integrals, $\frac{ds}{ds_{\delta}} ds_{\delta} = d_s$, and for the derivative of compsite functions $\frac{d}{ds_\delta} = \frac{d s}{d s_\delta} \frac{d}{d s}$.

```{dropdown} Fermat principle
:open:

Following [Fermat principle](calculus-variations:examples:fermat), the differential equations of the trajectory of a light ray come from the condition

$$\delta \int_{\gamma} \frac{1}{c} \, ds = \frac{1}{c_0} \delta \int_{\gamma} n \, ds\ .$$

Here the integrand is $\mathcal{L}(\mathbf{r}(s),s) = n(\mathbf{r}(s),s)$, and following the general formulation of the variational problem with prescribed ends $\delta \mathbf{r}|_{A,B} = \mathbf{0}$ gives

$$\begin{aligned}
  \mathbf{0}
  & = \nabla \mathcal{L} - \dfrac{d}{ds} \left( \hat{\mathbf{t}} \mathcal{L} \right) = \\
  & = \nabla \mathcal{L} - \kappa \hat{\mathbf{n}} \mathcal{L} - \hat{\mathbf{t}} \hat{\mathbf{t}} \cdot \mathcal{L} = \\
  & = \mathbb{P}_{\perp \hat{\mathbf{t}}} \cdot \nabla \mathcal{L} - \kappa \hat{\mathbf{n}} \mathcal{L} \ ,
\end{aligned}$$

i.e. the very same equations as {eq}`eq:variations:fermat:invariant`, having recalled that the derivative of the tangent unit vector to a line w.r.t. the arc-length is proportional to the unit normal vector, through the curvature, $\frac{d \hat{\mathbf{t}}}{d s}= \kappa \hat{\mathbf{n}}$.


```



````

```{dropdown} Method 2.
:open:





```



(calculus-variations:extra:non-prescribed-ends)=
## Integral with non prescirbed ends


