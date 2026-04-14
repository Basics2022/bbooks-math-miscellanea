(hamilton-bellman-jacobi)=
# Hamilton Bellman Jacobi equation

Let a dynamical system

$$\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u}) \ ,$$

with initial conditions $\mathbf{x}(0) = \mathbf{x}_0$. Let a **value function** $V(\mathbf{x}_t, t)$ defined as 

$$V(\mathbf{x}_t, t) = \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}(\tau)) d \tau +  D(\mathbf{x}(T)) \ ,$$

quantifying a cost for $\tau \in [t, T]$, subject to the dynamical equations. Value function has two arguments, the "initial time" $t$ and the state of the system at that time $\mathbf{x}_t$. The dynamical equations are a constraint that can be introduced into the value function with the method of Lagrange multipliers

$$\widetilde{V}(\mathbf{x}_t, t, \boldsymbol{\lambda}) = \int_{\tau=t}^{T} C(\mathbf{x}(\tau), \mathbf{u}(\tau)) d \tau +  D(\mathbf{x}(T)) - \int_{\tau=t}^T \boldsymbol\lambda^T(\tau) \left( \dot{\mathbf{x}}(\tau) - \mathbf{f}(\mathbf{x}(\tau), \mathbf{u}(\tau)) \right) d \tau \ .$$

```{dropdown} Method 1. Non-augmented value function
:open:


```


```{dropdown} Method 2. Augmented value function
:open:




```
