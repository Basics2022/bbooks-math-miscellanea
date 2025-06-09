(rl:mdp:sol:rl)=
# Large or Continuous MDPs

For small-dimensional problems, value functions can be efficiently represented by arrays or look-up tables,

$$\begin{aligned}
  V(s)   \quad & \rightarrow \quad \mathbf{V} \in \mathbb{R}^{|S|} \\
  Q(s,a) \quad & \rightarrow \quad \mathbf{Q} \in \mathbb{R}^{|S| \times |A|} \\
\end{aligned}$$

For large problems with large number of discrete states $\sim 10^{N}$ ($N = 20$ for backgammon, $= 10^{170}$ for Go), or continuous state space, RL usually relies on **function approximation** of the value function,

$$\begin{aligned}
  V^{\pi}(s)   & \sim V(s  ; \boldsymbol{\theta}) \\
  Q^{\pi}(s,a) & \sim Q(s,a; \boldsymbol{\theta}) \\
\end{aligned}$$

Parameters $\boldsymbol{\theta}$ are updated during learning. Examples of function approximators, the most suitable depend on the problem itself (ANN, Fourier/wavelets basis, polynomial, piecewise-polynomial, coarse coding,...)

**Optimizing/minimizing mean-squared error between $V(s,\theta)$ and $V^{\pi}(s)$**

$$L(\boldsymbol{\theta}) := \mathbb{E}_{\pi} \left[ \left( V^{\pi}(s) - V(s; \boldsymbol{\theta}) \right)^2 | s_t = s  \right]$$

Gradient descent,

$$\begin{aligned}
  \Delta \boldsymbol{\theta} 
  & = - \frac{1}{2} \alpha \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}) = \\
  & = - \frac{1}{2} \alpha \nabla_{\boldsymbol{\theta}} \, \mathbb{E}_{\pi} \left[ \left( V^{\pi}(s) - V(s, \boldsymbol{\theta}) \right)^2 | s_t = s \right] = \\
  & = \alpha \, \mathbb{E}_{\pi} \big[ \left( V^{\pi}(s) - V(s, \boldsymbol{\theta}) \right) \nabla_{\boldsymbol{\theta}} V(s, \boldsymbol{\theta}) \ | \ s_t = s \big]  \ ,
\end{aligned}$$

and the stochastic gradient decent update reads

$$
  \Delta \boldsymbol{\theta}
  = \alpha \ \left( V^{\pi}(s) - V(s, \boldsymbol{\theta}) \right) \, \nabla_{\boldsymbol{\theta}} V(s, \boldsymbol{\theta})  \ .
$$

State representation with **features** $\boldsymbol{\phi}(s)$,

$$\boldsymbol{\phi}(s) = \begin{bmatrix}  \phi_1(s) \\ \dots \\ \phi_n(s) \end{bmatrix}$$

**State-value function as a linear combination of features**

$$V(s; \boldsymbol{\theta}) = \boldsymbol{\phi}^T(s) \, \boldsymbol{\theta} \ ,$$

and the gradient of the objective function directly follows from

$$\nabla_{\boldsymbol{\theta}} V(s; \boldsymbol{\theta}) = \boldsymbol{\phi}(s) \ .$$

...

**Action-value function as a linear combination of features**

$$Q(s, a; \boldsymbol{\theta}) = \boldsymbol{\phi}^T(s,a) \, \boldsymbol{\theta} \ ,$$

...

## Value and Policy-Based RL
- value based
- policy based
- actor-critic

...


