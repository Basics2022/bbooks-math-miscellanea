(control:kalman)=
# Kalman filter

Kalman filter is an optimal state estimator, in terms of minimum-variance error reconstruction. It has the structure of a state observer. Let the linear system

$$\begin{cases}
  \dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} + \mathbf{B}_d \mathbf{d} \\
  \mathbf{y} = \mathbf{C} \mathbf{x} + \mathbf{D}_u \mathbf{u} + \mathbf{D}_d \mathbf{d} + \mathbf{D}_r \mathbf{r} \  ,
\end{cases}$$

Kalman filter for time-continuous systems has the structure

$$\begin{cases}
  \dot{\mathbf{o}} = \mathbf{A} \mathbf{o} + \mathbf{B} \mathbf{u} + \mathbf{L} ( \mathbf{y} - \mathbf{y}_o ) \\
  \mathbf{y}_o = \mathbf{C} \mathbf{o} + \mathbf{D}_u \mathbf{u}
\end{cases}$$

## Error dynamics

Let the error be defined as $\mathbf{e} := \mathbf{x} - \mathbf{o}$, its dynamical equation reads

$$\begin{aligned}
  \dot{\mathbf{e}} & = \left( \mathbf{A} - \mathbf{L} \mathbf{C} \right)  \mathbf{e} + \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right) \mathbf{d} - \mathbf{L} \mathbf{D}_r \mathbf{r} \\
  \dot{\mathbf{e}} & = \mathbf{A}_e \mathbf{e} + \mathbf{B}_{ed} \mathbf{d} + \mathbf{B}_{er} \mathbf{r} \\
  \dot{\mathbf{e}} & = \mathbf{A}_e \mathbf{e} + \boldsymbol\xi \ ,
\end{aligned}$$ (eq:kalman:error:eq)

with the definition of the noise input in the dynamical equation of the error, $\boldsymbol\xi = \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right) \mathbf{d} - \mathbf{L} \mathbf{D}_r \mathbf{r}$. 

```{dropdown} Details

$$\begin{aligned}
  \dot{\mathbf{e}}
  & = \dot{\mathbf{x}} - \dot{\mathbf{o}} = \\
  & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} + \mathbf{B}_d \mathbf{d} - \left( \mathbf{A} \mathbf{o} + \mathbf{B} \mathbf{u} + \mathbf{L} ( \mathbf{y} - \mathbf{y}_o )\right) = \\
  & = \left( \mathbf{A} - \mathbf{L} \mathbf{C} \right)  \mathbf{e} + \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right) \mathbf{d} - \mathbf{L} \mathbf{D}_r \mathbf{r}
\end{aligned}$$

```

Let the exogenous input $\mathbf{d}$ and the measurement input $\mathbf{r}$ be random signals, thus the input $\boldsymbol\xi$ of the error dynamical equation {eq}`eq:kalman:error:eq` is a random signal with correlation

<!--
$$\mathbb{E}\left[ \boldsymbol\xi(t) \boldsymbol\xi^*(\tau) \right] =
   \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right)   \mathbb{E}\left[ \mathbf{d} \mathbf{d}^*  \right] \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right)^*
 - \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right)   \mathbb{E}\left[ \mathbf{d} \mathbf{r}^*  \right] \left(                \mathbf{L} \mathbf{D}_r \right)^*
 - \left(                \mathbf{L} \mathbf{D}_r \right)   \mathbb{E}\left[ \mathbf{r} \mathbf{d}^*  \right] \left( \mathbf{B}_d - \mathbf{L} \mathbf{D}_d \right)^*
 + \left(                \mathbf{L} \mathbf{D}_r \right)   \mathbb{E}\left[ \mathbf{r} \mathbf{r}^*  \right] \left(                \mathbf{L} \mathbf{D}_r \right)^*
$$
-->

$$\begin{aligned}
\mathbf{R}_{\boldsymbol\xi \boldsymbol\xi}(t,\tau) := \mathbb{E}\left[ \boldsymbol\xi(t) \boldsymbol\xi^*(\tau) \right]
 & = \mathbf{B}_{ed} \mathbf{R}_{\mathbf{d}\mathbf{d}}(t,\tau) \mathbf{B}_{ed}^*
   + \mathbf{B}_{ed} \mathbf{R}_{\mathbf{d}\mathbf{r}}(t,\tau) \mathbf{B}_{er}^* + \\
 & + \mathbf{B}_{er} \mathbf{R}_{\mathbf{r}\mathbf{d}}(t,\tau) \mathbf{B}_{ed}^*
   + \mathbf{B}_{er} \mathbf{R}_{\mathbf{r}\mathbf{r}}(t,\tau) \mathbf{B}_{er}^*
\end{aligned}$$

Using the general results for linear systems for **white noise** as an input $\boldsymbol\xi$, the covariance matrix $\mathbf{P}_{\mathbf{e}}(t) := \mathbf{R}_{\mathbf{e}\mathbf{e}}(t,t)$ of the error - governed by eqaution {eq}`eq:kalman:error:eq` - satisfies the Lyapunov equation {eq}`eq:lyapunov:correlation`

$$\dot{\mathbf{P}}_{\mathbf{e}} = \mathbf{A}_e \mathbf{P}_{\mathbf{e}} + \mathbf{P}_{\mathbf{e}} \mathbf{A}_e^* + \boldsymbol\sigma_{\xi}^2 \ ,$$

being 

$$\boldsymbol\sigma_{xi}^2 = \dots $$

## Optimality conditions

...

$$\mathbf{L} = $$

* duality with the optimal control...
* ...

