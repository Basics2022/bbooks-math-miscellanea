(rl:mdp)=
# Markov Processes

```{prf:definition} Stochastic process
:label: def:stoch-process

A stochastic process is as collection of random variables $X(t)$ defined on a common probability space $(\Omega, \mathcal{F}, P)$, indexed by some set $T$, with outcomes in a measurable space $(S, \Sigma)$,

$$\left\{ X(t): t \in T \right\} \ .$$

```

Markov process is a memomry-less stochastic process (see def {prf:ref}`def:stoch-process`). For discrete-time Markov processes, state at time $n$ only depends on state at time $n-1$

$$\langle S, P, \mu \rangle$$

with 
- $S$ (finite) set of states
- $\mathbf{P}$ state transition probability matrix, $P_{ss'} = P(s'|s)$
- $\mu$ a set of initial probability, $\mu_i = P(X_0 = i), \forall i$ 

**Properties of probability matrix.**




A **stationary MP** is a process described by a constant state transition probability.

**1-step transition.**

```{admonition} Notation: probability vectors as row vectors
:class: tip

In treating stochastic processes, probability vectors are usually treated as row vectors. Probability distribution over states $s'$ at time $n$ is the sum of probabilities or reaching $s'$ starting from $s$ at time $n-1$

$$p_n(s') = \sum_s P(s'|s) p_{n-1}(s) = \sum_s p_{n-1}(s) P_{s s'} \ ,$$

or using matrix formalism

$$\mathbf{p}_n = \mathbf{p}_{n-1} \mathbf{P} \ .$$

```

**Properties of probability matrix.** 

Since $P_{s s'} = P(s'|s)$ represents the probability of arriving in $s'$ starting from $s$ (i.e. the *conditional probability* of arriving in $s'$, starting from $s$), the entries of a matrix representing a time-discrete process are

$$0 \le P_{s s'} \le 1 \ .$$

The sum over $s'$ is $1$ (sum over all the possibilities),

$$\sum_{s'} P(s' | s) = \sum_{s'} P_{s s'} = 1 \ , \quad \forall s \qquad \text{or} \qquad \mathbf{P} \mathbf{1} = \mathbf{1} \ .$$

Thus, a probability matrix $\mathbf{P}$ has a eigenvalue $\lambda = 1$ with the uniform vector $\mathbf{1}$ as eigenvector.

**Is this unique?** *No, in general.*

**Existence of a stationary distribution**

[**Spectral radius**](math:matrix-factorization:ev:spectral-radius) of a probability matrix is $\rho(\mathbf{P}) = 1$.

```{dropdown} Proof
:open:

By [Gershgorin circle theorem](math:matrix-factorization:ev:gershgorin),

$$| \lambda - P_{ii} | \le \sum_{j \ne i} |P_{ij}| \ ,$$

for $i$ s.t. the components of the (right) eigenvalue $\mathbf{v}$ satisfy $|x_i| \ge |x_j|$, $\forall j$. As $P_{ij} \ge 0$ and $\sum_j P_{ij} = P_{ii} + \sum_{j \ne i} P_{ij} = 1$, it follows

$$|\lambda - P_{ii}| \le \sum_{j \ne i} P_{ij} = \sum_{j} P_{ij} - P_{ii} = 1 - P_{ii} \ ,$$

meaning that any eigenvalue $\lambda$ is contained in a circle centered in $P_{ii}$ with radius $1 - P_{ii}$. It's not hard to prove that such a circle is contained in a circle centered in $0$ with radius $1$[^spectral-radius-triangle]. Thus, for all the eigenvalues $|\lambda| \le 1$ holds, and at least one eigenvalue with $|\lambda| = 1$, namely the $\lambda = 1$ eigenvalue shown above, exists. Thus, the spetral radius of a probability matrix is $\rho(\mathbf{P}) = 1$.

[^spectral-radius-triangle]: $1 - P_{ii} \ge |\lambda - P_{ii}| = |\lambda - 0 + 0 - P_ii| \ge | |\lambda| - P_ii |$; if $|\lambda| \ge P_{ii}$ it follows $1 \ge |\lambda|$; if $|\lambda| \le P_{ii}$...**todo**

```

**n-step transition.** $n$-step transition in a stationary MP reads

$$\mathbf{p}_{m+n} = \mathbf{p}_{m+n-1} \mathbf{P} = \mathbf{p}_{m+n-2} \mathbf{P} \mathbf{P} = \dots =  \mathbf{p}_m \mathbf{P}^n \ .$$

**First passage.** ...; recurrent states

**Classification of states**: accessible, communicating (and dividing states into partitions, disjoint classes); positive recurrent, periodic, ergodic; absorbing or transient

**Classification of MP**: absorbing, ergodic, regular

**Stationary distribution,** a probability vector $\mathbf{p}$ so that probability doesn't change in the next timestep,

$$\mathbf{p} = \mathbf{p} \mathbf{P} \ .$$

**Fundamental matrix**

**Other definitions**: mixing rate, spectral gap

## Markov Reward Processes

$$\langle S, P, R, \gamma, \mu \rangle$$

with 
- $R$ **reward function**; it could be a stochastic variable, depending on a state with probability $p(r|s)$ *(or on the transition $p(r|s,s')$?)*
- $\gamma$ **discount factor**, $\gamma \in [0,1]$; it's used to represent the present value of future rewards ($\gamma \sim 0$ short-sighted, $\gamma \sim 1$ far-sighted)

**Return**
- Time horizion: finite, indefinite (until stopping criteria, or absorbing state), infinite
- Possible choices of cumulative reward:
  - total reward, $V = \sum_i r_i$
  - average reward, $V = \frac{1}{n} \sum_{i=1}^{n} r_i$
  - discounted reward $V = \sum_{i} \gamma^{i-1} r_i$

Return $v_t$ is defined as the total discount reward from timestep $t$

$$v_t = \sum_{k=0}^{+\infty} \gamma^k r_{t+k+1} = r_{t+1} + \gamma r_{t+2} + \dots$$

**Value function** Expected value of the return $v_t$ from state $s_t = s$

$$V(s) := \mathbb{E}\left[ v_t | s_t = s  \right]$$

### Bellman Equation for $V(s)$

$$\begin{aligned}
  V(s) 
  & = \mathbb{E} \left[ v_t | s_t = s \right] = \\
  & = \mathbb{E} \left[ \left. r_{t+1} + \gamma \sum_{k=0}^{+\infty} \gamma^{k} r_{t+2+k} \right| s_t = s \right] = \\
  & = \mathbb{E} \left[ \left. r_{t+1} + \gamma v_{t+1} \right| s_t = s \right] = \\
  & = \mathbb{E} \left[  r_{t+1} | s_t = s \right] + \gamma \mathbb{E} \left[ v_{t+1} | s_t = s \right] = \\
  & = R(s) + \gamma \sum_{s'} P(s'|s) \mathbb{E} \left[ v_{t+1} | s_{t+1} = s' \right] = \\
  & = R(s) + \gamma \sum_{s'} P(s'|s) \, V(s') \ .
\end{aligned}$$

or in matrix form

$$\mathbf{V} = \mathbf{R} + \gamma \mathbf{P} \mathbf{V} \ .$$

**Solution of Bellman equation.** Bellman equation for value function is linear. It can be solved directly, solving the linear problem

$$\left( \mathbf{I} - \gamma \mathbf{P} \right) \mathbf{V} = \mathbf{R} \ .$$

Solutions:
- direct solution of the linear system (feasible for small-dimensional MRP only?)
- iterative methods for large MRPs: DP (dynamic programming), MC (Monte-Carlo evaluation), TD (Temporal-Difference learning)


## Markov Decision Processes

$$\langle S, A, P, R, \gamma, \mu \rangle$$

with
- A (finite) set of actions
- $\mathbf{P}$ state transition probability matrix, $P(s'|s,a)$
- $R$ reward function, $R(s,a) = \mathbb{E}\left[ r | s, a \right]$

### Policies

A policy is a distribution over actions, given the initial state

$$\pi(a|s) = P(a|s)$$

Given a policy $\pi(a|s)$, a MDP becomes the MRP with

- transition probability

   $$P^{\pi}(s'|s) = \sum_{a \in A} \pi(a|s) P(s'|s,a)$$

- reward (**todo** *Prove it!*)

   $$R^{\pi}(s) = \sum_{a \in A} \pi(a|s) R(s,a)$$

**Value functions.**
- State value function, $V^{\pi}(s)$, expected return starting from $s$ and following policy $\pi$

   $$V^{\pi}(s) := \mathbb{E}_{\pi} \left[ v_t | s_t = s \right]$$

- Action-value functon $Q^{\pi}(s,a)$, expected return starting from $s$, taking action $a$ first and then following policy $\pi$
   
   $$Q^{\pi}(s,a) := \mathbb{E}_{\pi} \left[ v_t | s_t = s, a_t = a \right]$$

### Bellman Equations

**Bellman expectation equations.** Bellman expectation equation for the state-value function $V^{\pi}(s)$ reads

$$\begin{aligned}
  V^{\pi}(s) 
  &:= \mathbb{E}_{\pi} \left[ v_t | s_t = s \right] = \\
  & = \mathbb{E}_{\pi} \left[ \left. r_{t+1} + \gamma \sum_{k=0}^{+\infty} \gamma^{k} r_{t+2+k} \right| s_t = s \right] = \\
  & = \sum_{a \in A} \pi(a|s) \mathbb{E}_{\pi} \left[ \left. r_{t+1} + \gamma \sum_{k=0}^{+\infty} \gamma^{k} r_{t+2+k} \right| s_t = s, a_t = a \right] = \\
  & = \sum_{a \in A} \pi(a|s) \mathbb{E} \left[ r_{t+1} | s_t = s, a_t = a \right] + \gamma \sum_{a \in A} \sum_{s' \in S} \pi(a|s) P(s'|s,a) \mathbb{E}_{\pi} \left[ \left. v_{t+1} \right| s_{t+1} = s' \right] = \\
  & = \sum_{a \in A} \pi(a|s) R(s,a) + \gamma \sum_{s' \in S} P^{\pi}(s'|s) \mathbb{E}_{\pi} \left[ \left. v_{t+1} \right| s_{t+1} = s' \right] = \\
  & = \sum_{a \in A} R(s,a) \left\{  \pi(a|s) + \gamma \sum_{s' \in S} P(s'|s,a) V^{\pi}(s') \right\} = \\
  & = R^{\pi}(s) + \gamma \sum_{s' \in S} P^{\pi}(s'|s) V^{\pi}(s') = \\
\end{aligned}$$ (eq:bellman:v:exp)

Bellman expectation equation for the action-value function $Q^{\pi}(s)$ reads

$$\begin{aligned}
  Q^{\pi}(s,a)
  &:= \mathbb{E}_{\pi} \left[ v_t | s_t = s, a_t = a \right] = \\
  & = \mathbb{E} \left[ r_{t+1} | s_t = s, a_t = a \right] + \gamma \mathbb{E}_{\pi} \left[ \left. v_{t+1} \right| s_t = s, a_t = a \right] = \\
  & = R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) \mathbb{E}_{\pi} \left[ \left. v_{t+1} \right| s_{t+1} = s' \right] = \\
  & = R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) V^{\pi}(s') = \\
  & = R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) \sum_{a' \in A} \pi(a'|s') \mathbb{E}_{\pi}[ v_{t+1} | s_{t+1} = s', a_{t+1} = a' ] = \\
  & = R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) \sum_{a' \in A} \pi(a'|s') Q^{\pi}(s', a')
\end{aligned}$$ (eq:bellman:q:exp)

**Bellman expectation operators** **todo**

**Optimal value functions, and optimal policies**

```{prf:definition} Optimal value functions
:label: def:optimal-value-fcns

Optimal state-value function $V^*(s)$ is defined as 

$$V^*(s) = \max_{\pi} V^{\pi}(s) \ .$$

Optimal action-value function $Q^*(s,a)$ is defined as

$$Q^*(s,a) = \max_{\pi} Q^{\pi}(s,a) \ .$$

```
Usually, the goal of a problem involving MDP is the maximization of value functions, as the performance of the MDP.

Valus functions define a partial ordering of policies,

$$\pi \ge \pi' \ \text{if} \ V^{\pi}(s) \ge V^{\pi'} \, \forall s \in S \ .$$

```{prf:theorem} Optimal policies

For a MDP,
- an optimal policy $\pi^*$ exists, s.t. $\pi^* \ge \pi$, $\forall \pi$
- all optimal policies achieve the same value of optimal functions, namely

   $$V^{\pi^*}(s) = V^*(s) \quad , \quad Q^{\pi^*}(s,a) = Q^*(s,a) \ . $$

- a deterministic optimal policy exists, and it's found optimizing action-value function over actions $a$,

  $$\pi^*(a|s) = \left\{ 
  \begin{aligned}
     & 1  && , \quad  \text{if } a = \text{argmax}_{a \in A} Q^*(s,a) \\
     & 0  && , \quad  \text{otherwise}
  \end{aligned}
  \right.
  $$

```

```{dropdown} Proof
:open:

**todo**

```

```{admonition} Property: optimal state-value and action-value functions
:name: prop:optimal-v-q

$$V^*(s) = \max_a Q^{*}(s,a)$$ (eq:optimality-condition)

**todo** *Prove it!*

```

**Bellman optimality equations.**
Using the property {ref}`prop:optimal-v-q` and the expression of action-value function in {eq}`eq:bellman:q:exp`

$$\begin{aligned}
  V^{*}(s) 
  & = \max_a Q^*(s,a) = \\
  & = \max_a \max_{\pi} Q^{\pi}(s,a) = \\
  & = \max_a \max_{\pi} \left\{ R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) V^{\pi}(s') \right\} = \\
  & = \max_a \left\{ R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) V^{*}(s') \right\} 
\end{aligned}$$

$$\begin{aligned}
  Q^{*}(s,a) 
  & = \max_\pi Q^{\pi}(s,a) = \\
  & = \max_\pi \left\{ R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) V^{\pi}(s') \right\} = \\
  & = R(s,a) + \max_\pi \left\{ \gamma \sum_{s' \in S} P(s'|s,a) V^{\pi}(s') \right\} = \\
  & = R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) V^{*}(s') = \\ 
  & = R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) \max_{a'} Q^*(s', a') 
\end{aligned}$$

**Bellman optimality operators**

**Properties of Bellman operators**

**Solving Bellman optimality equations**
- non-linear
- no closed form solution
- iterative solutions:
  - Dynamic Programming (DP): Value Iteration (VI), Policy Iteration (PI)
  - Linear Programming (LP)
  - Reinforcement Learning (RL): Q-learning (off-policy), SARSA (on-policy),...

