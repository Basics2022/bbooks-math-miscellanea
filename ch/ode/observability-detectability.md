(observability-detectability)=
# Observability and Detectability

(observability-detectability:time-continuous)=
## Time-continuous linear systems

The solution of the linear system

$$\begin{aligned}
  \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
       \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} \\
\end{aligned}$$

with initial conditions $\mathbf{x}(0) = \mathbf{x}_0$ reads

$$\mathbf{x}(t) = \boldsymbol\Phi(t,t_0) \mathbf{x}_0 + \int_{\tau=0}^{t} \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau \ ,$$

and the output of the system reads

$$\begin{aligned}
  \mathbf{y}(t)
  & = \mathbf{C}(t) \mathbf{x}(t) + \mathbf{D}(t) \mathbf{u}(t) = \\
  & = \mathbf{C}(t) \boldsymbol\Phi(t,t_0) \mathbf{x}_0 + \mathbf{C}(t) \int_{\tau=0}^{t} \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau  + \mathbf{D}(t) \mathbf{u}(t)  \ .
\end{aligned}$$ (eq:linear:output)

### Observability

A system is observable if the initial state $\mathbf{x}_0$ can be uniquely determined, knowing the output $\mathbf{y}(t)$ and the input $\mathbf{u}(t)$ over a finite time interval.

A relation between initial conditions as a function of the output and the input of the system can be retrieved from the expression {eq}`eq:linear:output`,

$$\mathbf{C}(t) \boldsymbol\Phi(t,t_0) \mathbf{x}_0 = \mathbf{y}(t) - \left[ \mathbf{C}(t) \int_{\tau=0}^{t} \boldsymbol\Phi(t,\tau) \mathbf{B}(\tau) \mathbf{u}(\tau) d \tau + \mathbf{D}(t) \mathbf{u}(t) \right] =: \widetilde{\mathbf{y}}(t) \ ,$$

with the definition of the known combination of input and output on the RHS as $\widetilde{\mathbf{y}}(t)$.
This system of equations is usually not square, and only involves two time instants $t_0$, $t$. If the latter equation is multiplied by $\boldsymbol\Phi^T(\tau,t_0) \mathbf{C}^T(\tau)$ (least square solution; $L_2$ norm;...) and integrated from $t_0$ to $t$ in order to use all the information from $t_0$ to $t$ 

$$\int_{\tau=t_0}^{t} \boldsymbol\Phi^T(\tau,t_0) \mathbf{C}^T(\tau) \mathbf{C}(\tau) \boldsymbol\Phi(\tau,t_0) d \tau \, \mathbf{x}_0 = \int_{\tau=t_0}^{t} \boldsymbol\Phi^T(\tau,t_0) \mathbf{C}^T(\tau) \widetilde{\mathbf{y}}(\tau) d \tau \ .$$

$$\mathbf{W}_o(t) \, \mathbf{x}_0 = \int_{\tau=t_0}^{t} \boldsymbol\Phi^T(\tau,t_0) \mathbf{C}^T(\tau) \widetilde{\mathbf{y}}(\tau) d \tau \ .$$

**todo**

* Discuss the **pullback** of the output to the state space (before $\sim$ least-square inversion )


### Detectability

A system is observable if all the unobservable modes are naturally stable, i.e. they decay to zero.

**todo** *Check definition, and requirement for finite or infinite time range* 

```{dropdown} Optimal input and controllability Gramian 
:open:

Let's solve the optimal output defined as the one with the maximum objective function $\frac{1}{2}\int_{\tau=0}^{t} \left| \mathbf{y}(\tau) \right|^2$, subject to the equations of motion as constraints. **todo** Here the final time $t$ is assumed to be known, but in general it's not: include $t$ in the optimization, or run several optimizations to find optimal $t^*$. The solution of the free system - or the forced system, with the $\widetilde{\mathbf{y}}(t)$ defined as the combination of output and input above - reads 

$$\mathbf{x}(t) = \boldsymbol\Phi(t,t_0) \mathbf{x}_0 \ ,$$

so that the output is $\mathbf{y}(t) = \mathbf{C} \boldsymbol\Phi(t,t_0) \mathbf{x}_0$. The objective function read

$$\begin{aligned}
 J(\mathbf{x}_0)
 & = \frac{1}{2} \int_{\tau=0}^{t} \mathbf{y}^T(\tau) \mathbf{y}(\tau) d \tau = \\
 & = \frac{1}{2} \mathbf{x}_0^T \int_{\tau=0}^{t} \boldsymbol\Phi^T(t,t_0) \mathbf{C}^T \mathbf{C} \boldsymbol\Phi(t,t_0) \mathbf{x}_0 = \\
 & = \frac{1}{2} \mathbf{x}_0^T \mathbf{W}_o(t) \mathbf{x}_0 \ .
\end{aligned}$$

* If $\mathbf{x}_0 \in K(\mathbf{W}_o(t))$, i.e. belongs to the kernel of the **observatility Gramian**, thus $J(\mathbf{x}_0) = 0$, i.e. the initial conditions has no influence on the output.
* If $\mathbf{x}_0 \notin K(\mathbf{W}_o(t))$, i.e. does not belong to the kernel of the observatility Gramian, thus $J(\mathbf{x}_0) > 0$.
* using singular value decomposition, it's possible to find the initial condition producing the largest output. Let $\mathbf{W}_o = \mathbf{U} \boldsymbol\Sigma \mathbf{U}^*$, the optimal initial condition with given $L_2$ norm, e.g. $\|\mathbf{x}_0\|_2 = 1$, is the singular vector $\mathbf{u}_1$ associated with the largest singular value $\sigma_1$, $\mathbf{x}_0 = \mathbf{u}_1$, and the optimal output is

   $$\max_{\|\mathbf{x}_0\|_2 = 1} J(\mathbf{x}_0) = J(\mathbf{x}_0 = \mathbf{u}_1) = \frac{1}{2} \sigma_1 \ .$$

```

Observability Gramian satisfies the [Lyapunov equation](lyapunov-eq)

$$
 \dot{\mathbf{W}}_o(t) = \mathbf{C}^T(t) \mathbf{C}(t) + \mathbf{A}^T(t) \mathbf{W}_o(t) + \mathbf{W}_o(t) \mathbf{A}(t) \ ,
$$

with initial conditions $\mathbf{W}_o(0) = \mathbf{0}$, as the integral vanishes with the same values of the lower and upper extremes of integration.

```{dropdown} Lyapunov equation for the controllability Graminan
:open:

$$\begin{aligned}
 \frac{d}{dt} \mathbf{W}_o(t)
 & = \frac{d}{dt} \int_{\tau=0}^{t} \boldsymbol\Phi^T(t,\tau) \mathbf{C}^T(\tau) \mathbf{C}(\tau)\boldsymbol\Phi(t,\tau) d \tau = \\
 & = \mathbf{C}(t) \mathbf{C}^T(t) + \int_{\tau=0}^{t} \partial_t \boldsymbol\Phi^T(t,\tau) \mathbf{C}^T(\tau) \mathbf{C}(\tau)\boldsymbol\Phi(t,\tau) d \tau + \int_{\tau=0}^{t} \boldsymbol\Phi^T(t,\tau) \mathbf{C}^T(\tau) \mathbf{C}(\tau) \partial_t \boldsymbol\Phi(t,\tau) d \tau = \\
 & = \mathbf{C}(t) \mathbf{C}^T(t) + \mathbf{A}(t) \mathbf{W}_c(t) + \mathbf{W}_c(t) \mathbf{A}^T(t) \ ,
\end{aligned}$$

as $\boldsymbol\Phi(t,t) = \mathbf{I}$, and $\partial_t \boldsymbol\Phi(t,\tau) = \mathbf{A}(t) \boldsymbol\Phi(t,\tau)$.


```



(observability-detectability:time-discrete)=
## Time-discrete linear systems


