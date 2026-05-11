(system-theory:time-delay:pade)=
# Padé approximation of time delay

(system-theory:time-delay:pade:time-delay)=
## Time delay

In time-domain

$$u_{\tau}(t) := u(t-\tau) \ , \quad \tau \ge 0 \ ,$$

with causal function $u(t) = 0$, for $t < 0$.

In Laplace domain,

$$\begin{aligned}
  \mathscr{L}\left\{ u(t-\tau) \right\} 
  & := \int_{t=0}^{+\infty} u(t-\tau) e^{-st} \, dt = \\
  & = \int_{t'=0}^{+\infty} u(t') e^{-s (t'+\tau)} \, dt' = \\
  & = e^{-s\tau} \int_{t'=0}^{+\infty} u(t') e^{-s t'} \, dt' = \\
  & = e^{-s \tau} U(s) \ .
\end{aligned}$$

(system-theory:time-delay:pade:pade)=
## Padé approximation

Padè approximation is a rational approximation of the exponential transfer function of the delay, $e^{-s \tau}$.

* Padé approximation is a (reasonable) **low-frequency approximation** of time delay. This immediately follows as Padé approximation exploits Taylor expansion of the time-delay transfer function $e^{-s \tau}$ for $s = 0$.

* Padé is usually **required in time-domain methods**, in order to avoid delay differential equations

**Examples.**
* [First-order system w/ time delay - referece tracking](control:examples:optimal-control:first-order-with-time-delay:ref-tracking)
* ...


(system-theory:time-delay:pade:pade:examples)=
### Examples

**$(1,1)$-Padé approximation.**

$$e^{-s \tau} \simeq P_{1,1}(s) = \frac{1 - \frac{\tau}{2}s}{1 + \frac{\tau}{2}s}$$

```{dropdown} $(1,1)$-Padé approximation - details

As an example, a rational approximation with both numerator and denominator of first order

$$e^{-s \tau} \simeq \frac{1 + a s}{1 + b s} \ .$$

Using Taylor approximation $e^{-s \tau}$

$$e^{-s \tau} \simeq 1 - \tau s + \frac{\tau^2 s^2}{2} + o (s^2) \ ,$$

and equating

$$\left( 1 - \tau s + \frac{\tau^2 s^2}{2} + o(s^2) \right) ( 1 + b s ) = 1 + a s \ ,$$

the first terms

$$\begin{aligned}
 1  : & \quad 1 = 1 \\
 s  : & \quad -\tau + b = a \\
 s^2: & \quad \frac{\tau^2}{2} - \tau b = 0 \ ,
\end{aligned}$$

it follows

$$\begin{aligned}
  b & =  \frac{\tau}{2} \\
  a & = -\frac{\tau}{2} \ ,
\end{aligned}$$


```

**$(2,2)$-Padé approximation.**

$$e^{-s \tau} \simeq P_{2,2}(s) = \frac{1 - \frac{\tau s}{2} + \frac{\tau^2 s^2}{12}}{1 + \frac{\tau s}{2} + \frac{\tau^2 s^2}{12}}$$

```{dropdown} $(2,2)$-Padé approximation - details

As an example, a rational approximation with both numerator and denominator of first order

$$e^{-s \tau} \simeq \frac{1 + a s + b s^2}{1 + c s + d s^2} \ .$$

Using Taylor approximation $e^{-s \tau}$

$$e^{-s \tau} \simeq 1 - \tau s + \frac{\tau^2 s^2}{2} - \frac{\tau^3 s^3}{3!} + \frac{\tau^4 s^4}{4!} + o (s^4) \ ,$$

and equating

$$\left( 1 - \tau s + \frac{\tau^2 s^2}{2} - \frac{\tau^3 s^3}{3!} + \frac{\tau^4 s^4}{4!}  + o(s^2) \right) ( 1 + c s + d s^2 ) = 1 + a s + b s^2 \ ,$$

the first terms

$$\begin{aligned}
 1  : & \quad 1 = 1 \\
 s  : & \quad -\tau + c = a \\
 s^2: & \quad  \frac{\tau^2}{2 } - \tau c + d = b \\
 s^3: & \quad -\frac{\tau^3}{3!} + \frac{\tau^2}{2 } c - \tau d = 0 \\
 s^4: & \quad  \frac{\tau^4}{4!} - \frac{\tau^3}{3!} c + \frac{\tau^2}{2} d = 0 \ ,
\end{aligned}$$

it follows

$$\begin{aligned}
  c & = \frac{1}{2}\tau \\ 
  d & = \frac{1}{12}\tau^2 \\ 
  a & = -\frac{1}{2}\tau \\ 
  b & = \frac{1}{12}\tau^2 \\ 
\end{aligned}$$

as

$$\begin{aligned}
\frac{1}{6} c - \frac{1}{2 \cdot 3!} \tau = 0 \quad & \rightarrow \quad c = \frac{1}{2}\tau \\ 
d = \tau \frac{c}{2} - \frac{1}{6} \tau^2     \quad & \rightarrow \quad d = \frac{1}{12}\tau^2 \\ 
                                                    & \rightarrow \quad a = -\frac{1}{2}\tau \\ 
                                                    & \rightarrow \quad b = \frac{1}{12}\tau^2 \\ 
\end{aligned}$$


```

(system-theory:time-delay:pade:pade:state-space)=
### Padé approximation in state-space representation

Let the LTI system

$$\begin{aligned}
  \dot{\mathbf{x}}(t) & = \mathbf{A} \mathbf{x}(t) + \mathbf{B} \mathbf{u}(t-\tau) \\
       \mathbf{y} (t) & = \mathbf{C} \mathbf{x}(t) + \mathbf{D} \mathbf{u}(t-\tau) \ ,
\end{aligned}$$

A Padé approximation results in a LTI whose output is the approximate delayed input, and whose input is the input itself. As an example, the $(1,1)$-Padé approximation in Laplace domain reads

$$U_\tau(s) = e^{-s \tau} U(s) \simeq \frac{1 - \frac{\tau s}{2}}{1 + \frac{\tau s}{2}} U(s) = \left[ \frac{-s + \frac{2}{\tau}}{s + \frac{2}{\tau} } \right] U(s) = \left[ - 1 + \frac{\frac{4}{\tau}}{s + \frac{2}{\tau}} \right] U(s) ,$$

and it has a state-space realization using [controllable canonical form](system-theory:state-space-realizations:ccf),[^pade-canonical-form]

$$\left\{\begin{aligned}
  \dot{\mathbf{x}}_\tau & = \begin{bmatrix} -\frac{2}{\tau} \end{bmatrix} \mathbf{x}_\tau + \begin{bmatrix} 1 \end{bmatrix} u \\
  u_\tau(t)          & = \begin{bmatrix} \frac{4}{\tau} \end{bmatrix} \mathbf{x}_\tau + \begin{bmatrix} -1 \end{bmatrix} u 
\end{aligned}\right. \ .$$

The **augmented system** reads

$$\left\{ \begin{aligned}
  \begin{bmatrix} \dot{\mathbf{x}} \\ \dot{\mathbf{x}}_{\tau} \end{bmatrix} & = \begin{bmatrix} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \mathbf{x}_{\tau} \end{bmatrix} + \begin{bmatrix} \end{bmatrix} \mathbf{u} \\
                       \mathbf{y}                                           & = \begin{bmatrix} \end{bmatrix} \begin{bmatrix} \mathbf{x} \\ \mathbf{x}_{\tau} \end{bmatrix} + \begin{bmatrix} \end{bmatrix} \mathbf{u} \\
\end{aligned} \right.$$

[^pade-canonical-form]: Usually, controllable canonical form for delay on input; observable canonical form for delay on output. Here, in this example with a $(1,1)$-Padé approximation, the state of the system is 1-dimensional, and the two canonical forms differ only by the "position" of the "$b_{n-1} = \frac{4}{\tau}$ element. The not-strictly proper TF is first written as a sum of a constant and a strictly proper TF, whose realization follows the rules of canonical realizations.

.




