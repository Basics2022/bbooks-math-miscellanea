(rl:mdp:sol:rl)=
# Methods of solution of MPD: RL

```{dropdown} Introduction

- model-free / model-based
- on-policy / off-policy
- online / offline
- tabular / function approximation
- value-based / policy-based / actor-critic

```

Two main goals of methods in RL:
- [prediction or evaluation](rl:mdp:sol:rl:eval): estimate the performance of a given policy
- [control](rl:mdp:sol:rl:control): find the best (or a good policy) to get the best performance

These two tasks usually rely on two processes: [evaluation](rl:mdp:sol:rl:eval) and [improvement](rl:mdp:sol:rl:control:improv). Evaluation stage provides the perfomance of a given policy usually in terms of value functions. Improvement aims at finding a new policy with better performance.

Prediction involves only the evaluation step, while control usually involves an iteration over alternate evaluation and improvement processes.

(rl:mdp:sol:rl:eval)=
## Evaluation

(rl:mdp:sol:rl:eval:mc)=
###  Monte-Carlo RL

- model-free, learn from experience of complete episodes ((-) no bootstrapping)
- uses empirical mean return, instead of expected value
- first-visit MC (unbiased estimator) / every-visit MC (biased estimator)


**First-visit MC**

Initialize: $\pi$ policy to be evaluated; $V$ arbitrary state-value function, $R(s)$ empty list of returns

Loop until convergence or stopping criterion
- generate an episode using $\pi$
  - for each state $s$ in the episode:
    - evalaute and append the return $r(s)$ following the first occurrence of $s$ to the list of $R(s)$
    - update $V(s) = \text{average}(R(s))$ 

**Every-visit MC**

Initialize: $\pi$ policy to be evaluated; $V$ arbitrary state-value function, $R(s)$ empty list of returns

Loop until convergence or stopping criterion
- generate an episode using $\pi$
  - for each state $s$ in the episode:
    - for each occurrence of state $s$ in the episode:
      - evaluate and append the return $r(s)$ following the occurrence of $s$ to the list of $R(s)$
      - update $V(s) = \text{average}(R(s))$ 

**Using incremental mean update**

$$\begin{aligned}
  \mu_{N+1} 
  & = \frac{x_1 + \dots + x_N + x_{N+1}}{N+1} = \\
  & = \frac{x_1 + \dots + x_N}{N} \frac{N}{N+1} + \frac{x_{N+1}}{N+1} = \\
  & = \frac{N}{N+1} \mu_{N} + \frac{1}{N+1} x_{N+1} = \\
  & = \mu_{N} + \frac{1}{N+1} \left( x_{N+1} - \mu_{N} \right)
\end{aligned}$$

Incremental update of the average of the value function reads

$$V_{k}(s) \leftarrow V_{k-1}(s) + \frac{1}{k} \left( v_k - V_{k-1}(s) \right) \ ,$$

with $v_k$ the return of state $s_k$.

A generalized update may follow, to introduce a free hyperparameter as a weight of older estimation,

$$\begin{aligned}
  V_{k}(s) 
  \leftarrow & \ V_{k-1}(s) + \alpha_k \left( v_k - V_{k-1}(s) \right) \\
           = & \ ( 1 - \alpha_k ) V_{k-1}(s) + \alpha_k v_k
\end{aligned}$$

(rl:mdp:sol:rl:eval:td)=
### Temporal Difference (TD) Learning

- model-free, learn from experience of incomplete episodes (bootstrapping)
- ...

### TD prediction

- Starting from every visit MC

  $$V(s_t) \leftarrow V(s_t) + \alpha (v_t - V(s_t))$$

- Update towards an **estimation of the return**
  - the simplest TD algorithm is $TD(0)$.
    - estimated return (called **TD target**) reads

       $$v_t \sim r_{t+1} + \gamma V(s_{t+1}) $$

    - **TD error** error $\delta_t$ is defined as

       $$\delta_t := r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

    - update step

       $$\begin{aligned}
         V(s)
         \leftarrow & \ V(s) + \alpha_k \left( r_{t+1} + \gamma V(s_{t+1}) - V(s_{t+1}) \right) = \\
                  = & \ V(s) + \alpha_k \, \delta_t
       \end{aligned}$$

  - $TD(n)$ algorithm uses $n$-step prediction

     $$v_t^{(n)} = r_{t+1} + \gamma r_{t+2} + \dots \gamma r_{t+n} + \gamma^{n+1} V(s_{t+n})$$

  - $\lambda$-return $v_t^\lambda$ combines all $n$-step returns $v^{(n)}_t$ as

     $$v_t^{\lambda} := (1-\lambda) \sum_{n=1}^{+\infty} \lambda^{n-1} v_t^{(n)}$$

     weights s.t. sum of weights $=1$ and decay as $\lambda ( < 1)$

  - ...eligibility traces, forward and backward TD,...


(rl:mdp:sol:rl:control)=
## Model control

(rl:mdp:sol:rl:control:improv)=
### On- and Off-Policy Learning
- On-policy: learn policy $\pi$ from experience sampled from $\pi$
- Off-policy: learn policy $\pi$ from experience sampled from $\widetilde{\pi}$

**Greedy policy improvement** 
- over $V(s)$ requires model of MDP,

   $$\pi'(s) = \text{argmax}_{a \in A} \left\{ R(s,a) + P(s'|s,a) V(s') \right\} $$

- **over $Q(s,a)$ is model-free**
 
   $$\pi'(s) = \text{argmax}_{a \in A} Q(s,a) \ .$$

(rl:mdp:sol:rl:control:mc)=
### MC control

```{note} Generalized policy iteration with MC evaluation

MC evaluation is model-free. To keep a model-free control task, a model-free policy improvement is required, like greedy policy improvement over $Q(s,a)$.

```

(rl:mdp:sol:rl:control:improv:eps-greedy)=
### $\varepsilon$-greedy policy improvement

$$
\pi(a|s) = \left\{
\begin{aligned}
  & 1 - \varepsilon \left( 1 - \frac{1}{N} \right) && , \qquad  \text{if } a = \text{argmax}_{a \in A} Q^{\pi}(s,a) \\
  & \frac{\varepsilon}{N} && , \qquad \text{otherwise}
\end{aligned}
\right.
$$

```{prf:theorem} $\varepsilon$-greedy Policy Improvement

For ..., the $\varepsilon$-greedy policy $\pi'$ w.r.t. $Q^{\pi}$ is an improvement, $V^{\pi'}(s) \ge V^{\pi}(s)$.


```

```{dropdown} Proof

$$\begin{aligned}
  Q^{\pi}(s, \pi'(s))
  & = \sum_{a \in A} \pi'(a|s) Q^{\pi}(s,a) = \\
  & = \sum_{a \in A, a \ne a^*} \frac{\varepsilon}{m} Q^{\pi}(s,a) + \left( 1 - \varepsilon + \frac{\varepsilon}{m} \right) Q^{\pi}(s,a^*) = \\
  & = \sum_{a \in A} \frac{\varepsilon}{m} Q^{\pi}(s,a) + \left( 1 - \varepsilon \right) Q^{\pi}(s,a^*) = \\
  (1) & \ge \sum_{a \in A} \frac{\varepsilon}{m} Q^{\pi}(s,a) + \left( 1 - \varepsilon \right) \sum_{a \in A} \dfrac{\pi(a|s) - \frac{\varepsilon}{m}}{1 - \varepsilon} Q^{\pi}(s,a) = \\
  & = \sum_{a \in A} \pi(a|s) Q^{\pi}(s,a) = V^{\pi}(s) \\
\end{aligned}$$

having used in $(1)$ ...
And for the policy improvement theorem {prf:ref}`thm:pi`, $V^{\pi'}(s) \ge V(s)$. **todo** *Check it!*

```

**GLIE (Greedy in the Limit of Infinite Exploration)** ...

**GLIE MC Control**
- $k^{th}$ episode using \pi$$
- for each state $s_t$,  and action $a_t$ in the episode, update number of $(s,a)$ pair occurence and action-value function

   $$\begin{aligned}
     N(s_t, a_t) & \ \leftarrow \ N(s_t, a_t) + 1 \\
     Q(s_t, a_t) & \ \leftarrow \ Q(s_t, a_t) + \frac{1}{N(s_t, a_t) (v_t - Q(s_t, a_t))}
   \end{aligned}$$

- improve policy with $\varepsilon$-greedy method over action-value function $Q$,

  $$\begin{aligned}
    \varepsilon & \ \leftarrow \ \frac{1}{k} \\
    \pi & \ \leftarrow \ \varepsilon-\text{greedy}(Q) \\
  \end{aligned}$$

(rl:mdp:sol:rl:control:td)=
### TD control

- (+): online, from incomplete episodes, lower variance
- use TD instead of MC for policy evaluation, **SARSA**:

  $$Q(s,a) \ \leftarrow \ Q(s,a) + \alpha \left( r + \gamma Q(s',a') - Q(s,a) \right)$$

...

**Variations.** SARSA$(\lambda)$,...

```{note} SARSA is on-policy
```

### Off-policy learning

**Q-learning**, is off-policy as $a'$ is not taken from $\pi$

  $$Q(s,a) \ \leftarrow \ Q(s,a) + \alpha \left( r + \gamma \max_{a'} Q(s',a') - Q(s,a) \right)$$

(rl:mdp:sol:rl:ac)
## Actor-Critic

**todo**

## Learning and planning
- Model-free RL: no model; **learn** policy and/or value function from real experience
- Model-based RL: learn a model from real experience; **plan** policy and/or value function from simulated experience
- Dyna: leanr a model from real experience; **learn and plan** a policy and/or value function from real and simulated experience

