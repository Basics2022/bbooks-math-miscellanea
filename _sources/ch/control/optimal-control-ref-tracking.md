(control:optimal:ref-tracking)=
# Optimal control for reference tracking

<!--
See [this Colab](https://colab.research.google.com/drive/1G5nu_jUEZgmja0SmA0I1rcPOVZKKu4oZ?authuser=1#scrollTo=nJXJBxc1LWic) on my personal GDrive, until this is not included in this Jupyter book.
-->

In order to get perfect asymptotic tracking of polynomial reference signals with degree $m$ with optimal control, the original system must be augmented with the dynamical equations of $m+1$ integral errors. This process is shown for [tracking step reference](control:optimal:ref-tracking:step) with the augmentation of the original system with a single integrator and for [tracking ramp reference](control:optimal:ref-tracking:ramp) with the augmentation with a double integrator.

This procedure is somehow equivalent to the addition of integrators in open-loop transfer function, as discussed in the section about [reference tracking as a performance of a closed-loop system](control:closed-loop:requirements-performance:siso:ref-tracking).

An example about optimal control for reference tracking in a mass-damper-spring system is shown in the [next section](control:optimal:ref-tracking:example), as a **Jupyter notebook** that can be opened, run, and modified in **Colab**.

(control:optimal:ref-tracking:step)=
## Augmented system for tracking step reference signal - integrator

Let $\mathbf{y}_{\text{ref}}$ a reference signal. An augmented system can be defined in order to use optimal control for tracking the desired reference signal.

$$\begin{aligned}
 \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
      \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u}
\end{aligned}$$

the state-space representation of the plant. Let $\mathbf{y}_{ref}$ a desired output and the integral error

$$\mathbf{e}(t) := \int_{\tau=0}^{t} \left\{ \mathbf{y}(\tau) - \mathbf{y}_{ref}(\tau) \right\} d \tau \ ,$$

as a new state with dynamical equation

$$\dot{\mathbf{e}} = \mathbf{y}(t) - \mathbf{y}_{ref}(t) = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} - \mathbf{y}_{ref} \ .$$

The optimal control is applied to the augmented system

$$\underbrace{\begin{bmatrix} \dot{\mathbf{x}} \\ \dot{\mathbf{e}} \end{bmatrix}}_{\dot{\mathbf{z}}} = \underbrace{\begin{bmatrix} \mathbf{A} & \cdot \\ \mathbf{C} & \cdot \end{bmatrix}}_{\hat{\mathbf{A}}} \underbrace{\begin{bmatrix} \mathbf{x} \\ \mathbf{e} \end{bmatrix}}_{\mathbf{z}} + \underbrace{\begin{bmatrix} \mathbf{B} \\ \mathbf{D} \end{bmatrix}}_{\hat{\mathbf{B}}_u} \mathbf{u} + \underbrace{\begin{bmatrix} \cdot \\ -\mathbf{I} \end{bmatrix}}_{\hat{\mathbf{B}}_{ref}} \mathbf{y}_{ref}$$

Optimal control framework provides the opitmal gain matrix $\hat{\mathbf{K}}$, so that $\mathbf{u} = - \hat{\mathbf{K}} \mathbf{z}$ and the closed loop system becomes

$$\dot{\mathbf{z}} = \left( \hat{\mathbf{A}} - \hat{\mathbf{B}}_u \hat{\mathbf{K}} \right) \mathbf{z} + \hat{\mathbf{B}}_{ref} \mathbf{y}_{ref} \ .$$

```{dropdown} $\lim_{t \rightarrow +\infty} e(t)$
:open:

**Transfer function.** From the reference signal to the tracking error,

$$\mathbf{e}(s) = \mathbf{y}_{\text{ref}} - \mathbf{G}_k(s) \frac{\mathbf{e}}{s}$$

$$\mathbf{e}(s) = \left[ \mathbf{I} + \frac{1}{s} \mathbf{G}_k(s) \right]^{-1} \mathbf{y}_{\text{ref}}(s)$$

**Final value theorem.**

$$\lim_{t \rightarrow +\infty} \mathbf{e}(t) = \lim_{s \rightarrow 0} s \mathbf{e}(s)$$

Let $\mathbf{y}_{\text{ref}}$ a polynomial reference input, $\mathbf{y}_{\text{ref}} = \mathbf{C}_{-1} \delta(t) + \sum_{k=0}^{m} \mathbf{C}_k t^k$ then its Laplace transform reads $\mathbf{y}_{\text{ref}}(s) = \sum_{k=-1}^{m} \frac{\mathbf{C}_k}{s^{k+1}}$

$$\begin{aligned}
  \lim_{t \rightarrow +\infty} \mathbf{e}(t) 
  & = \lim_{s \rightarrow 0} s \mathbf{e}(s) = \\
  & = \lim_{s \rightarrow 0} s \left[ \mathbf{I} + \frac{1}{s} \mathbf{G}_k(s) \right]^{-1} \left( \sum_{k=-1}^{m} \frac{\mathbf{C}_k}{s^{k+1}} \right) = \\
  & = \lim_{s \rightarrow 0} s \cdot s \, \mathbf{G}_k^{-1}(s) \left( \sum_{k=-1}^{m} \frac{\mathbf{C}_k}{s^{k+1}} \right) \ ,
\end{aligned}$$

and thus, if
* $m = 0$ (i.e. linear combination of Dirac's delta and a step) the asymptotic value of the tracking error is zero; 
* $m = 1$ (i.e. up to a ramp) the asymptotic value of the tracking error is constant, $\mathbf{G}_k^{-1}(0) \mathbf{C}_1$; 
* $m > 1$ the tracking error goes to infinity.

```


:::{figure} ./../../media/control/optimal-control-tracking-step.png
:alt: Optimal control. Reference tracking for step
:align: center
:name: fig-optimal-tracking-step

Caption

:::

(control:optimal:ref-tracking:ramp)=
## Augmented system for tracking ramp reference signal - double integrator

Let $\mathbf{y}_{\text{ref}}$ a reference signal. An augmented system can be defined in order to used optimal control. Let

$$\begin{aligned}
 \dot{\mathbf{x}} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} \\
      \mathbf{y}  & = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u}
\end{aligned}$$

the state-space representation of the plant. Let $\mathbf{y}_{ref}$ a desired output and the integral error

$$\mathbf{e}_1(t) := \int_{\tau=0}^{t} \left\{ \mathbf{y}(\tau) - \mathbf{y}_{ref}(\tau) \right\} d \tau \ ,$$

as a new state with dynamical equation

$$\dot{\mathbf{e}}_1 = \mathbf{y}(t) - \mathbf{y}_{ref}(t) = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} - \mathbf{y}_{ref} \ .$$

The second augmenting state is defined as

$$\mathbf{e}_2(t) := \int_{\tau=0}^{t} \mathbf{e}_1(\tau) \, d\tau \ ,$$

so that the dynamical equation is

$$\dot{\mathbf{e}}_2 = \mathbf{e}_1 \ .$$

The optimal control is applied to the augmented system

$$\underbrace{\begin{bmatrix} \dot{\mathbf{x}} \\ \dot{\mathbf{e}}_1 \\ \dot{\mathbf{e}}_2 \end{bmatrix}}_{\dot{\mathbf{z}}} = \underbrace{\begin{bmatrix} \mathbf{A} & \cdot & \cdot \\ \mathbf{C} & \cdot & \cdot \\ \cdot & \mathbf{I} & \cdot \end{bmatrix}}_{\hat{\mathbf{A}}} \underbrace{\begin{bmatrix} \mathbf{x} \\ \mathbf{e}_1 \\ \mathbf{e}_2 \end{bmatrix}}_{\mathbf{z}} + \underbrace{\begin{bmatrix} \mathbf{B} \\ \mathbf{D} \\ \cdot \end{bmatrix}}_{\hat{\mathbf{B}}_u} \mathbf{u} + \underbrace{\begin{bmatrix} \cdot \\ -\mathbf{I} \\ \cdot \end{bmatrix}}_{\hat{\mathbf{B}}_{ref}} \mathbf{y}_{ref}$$

Optimal control framework provides the opitmal gain matrix $\hat{\mathbf{K}}$, so that $\mathbf{u} = - \hat{\mathbf{K}} \mathbf{z}$ and the closed loop system becomes

...

```{dropdown} $\lim_{t \rightarrow +\infty} e(t)$
:open:

**Transfer function.** The closed-loop system reads

$$\begin{aligned}
  s \mathbf{x} & = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u} = \\
               & = \left( \mathbf{A} - \mathbf{B} \mathbf{K} \right) \mathbf{x} - \mathbf{B} \mathbf{K}_1 \mathbf{z}_1 - \mathbf{B} \mathbf{K}_2 \mathbf{z}_2 \\
  \mathbf{y} & = \left( \mathbf{C} - \mathbf{D} \mathbf{K}_u \right) \mathbf{x} - \mathbf{D} \mathbf{K}_1 \mathbf{z}_1 - \mathbf{D} \mathbf{K}_2 \mathbf{z}_2 \ .
\end{aligned}$$

so that

$$\begin{aligned}
  \mathbf{x} 
  & = \left( s \mathbf{I} - \mathbf{A} + \mathbf{B} \mathbf{K} \right)^{-1} \left[ - \mathbf{B} \mathbf{K}_1 \mathbf{z}_1 - \mathbf{B} \mathbf{K}_2 \mathbf{z}_2 \right] = \\ 
  & = \dots 
\end{aligned}$$

and $\mathbf{y} = \mathbf{G}_1(s) \mathbf{K}_1 \mathbf{z}_1 + \mathbf{G}_2(s) \mathbf{K}_2 \mathbf{z}_2$.

From the reference signal to the tracking error,

$$\begin{aligned}
  \mathbf{e}(s)
  & = \mathbf{y}_{\text{ref}} - \mathbf{y} = \\
  & = \mathbf{y}_{\text{ref}} - \mathbf{G}(s) \mathbf{K}_1 \mathbf{z}_1 - \mathbf{G}(s) \mathbf{K}_2 \mathbf{z}_2 = \\
  & = \mathbf{y}_{\text{ref}} - \mathbf{G}_1(s) \frac{\mathbf{e}}{s} - \mathbf{G}_2(s) \frac{\mathbf{e}}{s^2} \ ,
\end{aligned}$$

$$\mathbf{e}(s) = \left[ \mathbf{I} + \frac{1}{s} \mathbf{G}_1(s) + \frac{1}{s^2} \mathbf{G}_2(s) \right]^{-1} \mathbf{y}_{\text{ref}}(s)$$

**Final value theorem.**

$$\lim_{t \rightarrow +\infty} \mathbf{e}(t) = \lim_{s \rightarrow 0} s \mathbf{e}(s)$$

Let $\mathbf{y}_{\text{ref}}$ a polynomial reference input, $\mathbf{y}_{\text{ref}} = \mathbf{C}_{-1} \delta(t) + \sum_{k=0}^{m} \mathbf{C}_k t^k$ then its Laplace transform reads $\mathbf{y}_{\text{ref}}(s) = \sum_{k=-1}^{m} \frac{\mathbf{C}_k}{s^{k+1}}$

$$\begin{aligned}
  \lim_{t \rightarrow +\infty} \mathbf{e}(t) 
  & = \lim_{s \rightarrow 0} s \mathbf{e}(s) = \\
  & = \lim_{s \rightarrow 0} s \left[ \mathbf{I} + \frac{1}{s} \mathbf{G}_1(s) + \frac{1}{s^2} \mathbf{G}_2(s) \right]^{-1} \left( \sum_{k=-1}^{m} \frac{\mathbf{C}_k}{s^{k+1}} \right) = \\
  & = \lim_{s \rightarrow 0} s \cdot s^2 \, \mathbf{G}_2^{-1}(s) \left( \sum_{k=-1}^{m} \frac{\mathbf{C}_k}{s^{k+1}} \right) \ ,
\end{aligned}$$

and thus, if
* $m = 1$ (i.e. linear combination of Dirac's delta, step, and ramp) the asymptotic value of the tracking error is zero; 
* $m = 2$ (i.e. up to a parabolic input, $\dots + \mathbf{C}_2 t^2$) the asymptotic value of the tracking error is constant, $\mathbf{G}_2^{-1}(0) \mathbf{C}_2$;
* $m > 2$ the tracking error goes to infinity.


```

:::{figure} ./../../media/control/optimal-control-tracking-ramp.png
:alt: Optimal control. Reference tracking for ramp
:align: center
:name: fig-optimal-tracking-ramp

Caption

:::
