(rl:mdp:sol:dp-lp)=
# Methods of solution of MPD: DP and LP

## Brute force: policy search

(rl:mdp:sol:dp)=
## Dynamic programming

```{dropdown} Introduction to DP
:open:

- sequential or temporal approach to optimization
- solving complex problems breaking them down into sub-problems:
  - solve sub-problems
  - combine solutions of sub-problems
- for problems with 2 properties:
  - optimal substructure: optimal sol can be decomposed in sub-pbs
  - overlapping sub-problems: sub-pbs recur, sols can be cached and reused
- DP assumes full knowledge of the MDP
- used for planning (???)
- prediction: given MDP and policy, evaluate value function
- control: given MDP, evaluate optimal value function and policy
```

(rl:mdp:sol:dp:pi)=
### Policy iteration

Policy iteration alternates [policy evaluation](rl:mdp:sol:dp:pi:eval) and [policy improvement](rl:mdp:sol:dp:pi:impr) steps. When value function converges, iteration stops at **Bellman optimality condition**, as shown in the [algorithm](rl:mdp:sol:dp:pi:algorithm) below.

(rl:mdp:sol:dp:pi:eval)=
#### Policy Evaluation

**Bellman equation for a given policy $\pi$.** Solution of Bellman equation {eq}`eq:bellman:v:exp`,

$$V^{\pi}(s) = \sum_{a \in A} R(s,a) \left\{  \pi(a|s) + \gamma \sum_{s' \in S} P(s'|s,a) V^{pi}(s') \right\}$$

-  direct solution. Complexity: ...

- full policy-evaluation back-up

  $$V_{k+1}(s) \leftarrow \sum_{a \in A} R(s,a) \left\{  \pi(a|s) + \gamma \sum_{s' \in S} P(s'|s,a) V^{\pi}_k(s') \right\}$$

  synchronous, asynchronous update; **todo** *convergence?*

(rl:mdp:sol:dp:pi:impr)=
#### Policy Improvement 

**Greedy update.** Let $\pi$ be a deterministic policy. Greedy update acts maximizing the action-value function for all state over all the actions,

$$\pi'(s) := \text{argmax}_{a \in A} Q^{\pi}(s,a) \ ,$$

and it "improves the value function" (which value function?) of any state,

$$Q^{\pi}(s,\pi'(s)) := \max_{a \in A} Q^{\pi}(s,a) \ge Q^{\pi}(s,\pi(s)) = V^{\pi}(s) \ .$$ (eq:greedy)

In stochastic optimization, usually [$\varepsilon$-greedy improvement](rl:mdp:sol:rl:control:improv:eps-greedy) is introduced to improve **exploration** and try to avoid converging to local optimum.

```{prf:theorem} Policy improvement theorem
:label: thm:pi

Let $\pi$ and $\pi'$ a pair of deterministic policites s.t.

$$Q^{\pi}(s, \pi'(s)) \ge V^{\pi}(s) \ , \quad \forall s \in S$$

Then $\pi' \ge \pi$, i.e. $V^{\pi'}(s) \ge V^{\pi}(s)$, $\forall s \in S$.

```

```{dropdown} Proof.

$$\begin{aligned}
  V^{\pi}(s)
  & \le Q^{\pi}(s,\pi'(s)) = \\
  & =: \mathbb{E}_{\pi} \left[ \left. v_t  \right| s_t = s, a_t = \pi'(s) \right] = \\
  & =  \mathbb{E}_{\pi} \left[ \left. r_{t+1} + \gamma v_{t+1}  \right| s_t = s, a_t = \pi'(s) \right] = \\
 (1) & =  \mathbb{E}_{\pi'} \left[ r_{t+1} | s_t = s \right] + \gamma \mathbb{E}_{\pi} \left[ \left. v_{t+1}  \right| s_{t+1} = s', a_{t+1} = \pi(s) \right] = \\
  & =   \mathbb{E}_{\pi'} \left[ r_{t+1} | s_t = s \right] + \gamma V^{\pi}(s) = \\
  & \le \mathbb{E}_{\pi'} \left[ r_{t+1} | s_t = s \right] + \gamma Q^{\pi}(s,\pi'(s)) = \\
  & =   \mathbb{E}_{\pi'} \left[ r_{t+1} | s_t = s \right] + \gamma \mathbb{E}_{\pi} \left[ \left. r_{t+2} + \gamma v_{t+2}  \right| s_{t+1} = s, a_{t+1} = \pi'(s) \right] = \\
 (2) & =   \mathbb{E}_{\pi'} \left[ r_{t+1} | s_t = s \right] + \gamma \mathbb{E}_{\pi'} \left[ r_{t+2} | s_{t+1} = s \right] + \gamma^2 \mathbb{E}_{\pi} \left[ \left. v_{t+2}  \right| s_{t+2} = s'', a_{t+2} = \pi(s) \right] = \\
  & =   \mathbb{E}_{\pi'} \left[ r_{t+1} + \gamma r_{t+2}  | s_t = s \right] + \gamma^2 V^{\pi}(s) = \\
  & \le \mathbb{E}_{\pi'} \left[ r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \dots | s_t = s \right] = \\
  & \le V^{\pi'}(s) \ .
\end{aligned}$$

with in $(1)$ the first action $a_t$ is drawn from $\pi'(s)$, $s'$ results from the transition 

$$P^{\pi}(s'|s) = P(s'|s,a)\pi(a|s) \ ,$$

and the following are drawn from $\pi$. The same notation is used in $(2)$, and in all the following manipulations.

```

(rl:mdp:sol:dp:pi:algorithm)=
#### Policy Iteration algorithm

Policy iteration algorithm

$$\pi_0 \rightarrow V^{\pi_0} \rightarrow \pi_1 \rightarrow V^{\pi_1} \rightarrow \dots \pi^* \rightarrow V^* \rightarrow \pi^*$$

Convergence is reached when $\pi_{n+1}(s) = \pi_{n}(s)$. Greedy update {eq}`eq:greedy` gives

$$Q^{\pi_{n}}(s, \pi_{n+1}(s)) = Q^{\pi_n}(s, \pi_n(s)) = V^{\pi_n}(s) \ ,$$

namely, when the optimality condition {eq}`eq:optimality-condition` is reached.


(rl:mdp:sol:dp:vi)=
### Value Iteration

Unlike policy iteration, value iteration algorithm doesn't provide any explicit policy, but only optimal value of the value-functions.

An optimal policy for a MDP is built with an optimal action $a^*$ first, followed by actions drawn from the optimal policy. Thus, it must satisfy

$$V^*(s) = \max_{a \in A} R(s,a) + V^*(s') \ ,$$

with $s_{n} = s$ and $s_{n+1} = s'$, resulting from transition $s'|s,a$. Subdividing the problem in sub-problems, **deterministic value iteration** proceeds from $s'$ backwards to $s$,

$$V^*(s) \leftarrow \max_{a \in A} R(s,a) + V^*(s') \ .$$

or

$$V^*(s) \leftarrow \max_{a \in A} \left\{ R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) V(s') \right\} .$$

(rl:mdp:sol:dp:extensions)=
### Dynamic programming: extensions

- synchronous, or in-place
- prioritized sweeping/update
- ...

(rl:mdp:sol:lp)=
## Linear programming

...
