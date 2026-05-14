(ode:linear-equations)=
# Linear equations

(ode:linear-equations:const-coeff)=
## Linear equations with constant coefficients

(ode:linear-equations:const-coeff:def)=
### Definition

(ode:linear-equations:const-coeff:general-sol)=
### General solution

$$y(x) = y_o(x) + y_p(x)$$

(ode:linear-equations:const-coeff:general-sol:homogeneous)=
#### Solution of the homogeneous equation


```{dropdown} Independent solutions for non-multiple root

$$\begin{aligned}
  0 & = a_n y^{(n)}(x) + \dots a_1 y'(x) + a_0 y(x) = \\
    & = a_n \left( - s_1 + \frac{d}{dx} \right) \dots \left( - s_n + \frac{d}{dx} \right) y(x) \ ,
\end{aligned}$$

If all the roots are non-multiple, then $n$ independent solutions are found setting the result of every individual operator $\left( - s_k + \frac{d}{dx} \right)$ on $y(x)$ equal to zero,

$$0 = \left( - s_k + \frac{d}{dx} \right) y(x) = - s_k y(x) + y'(x) \ ,$$

whose solution is $y_k(x) = A_k e^{s_k x}$.

```

(ode:linear-equations:const-coeff:general-sol:homogeneous:multiple-roots)=
##### Independent solutions for roots with miltiplicity $\ p > 1$

```{dropdown} Independent solutions for root with multiplicity $\ p=2$

$$0 = \left( - s_k + \frac{d}{dx} \right)^2 y(x) = \left( - s_k + \frac{d}{dx} \right) \left( - s_k + \frac{d}{dx} \right) y(x) \ .$$

In order to satisfy this equation, one of the the following two conditions must hold

$$\begin{aligned}
  - s y(x) + y'(x) & = 0 \\
  - s y(x) + y'(x) & = A \, e^{s x} \\
\end{aligned}$$

The solution of the first condition is

$$- s y(x) + y'(x) = 0 \qquad \rightarrow \qquad y(t) = C e^{s x}$$

The solution of the second condition is

$$\begin{aligned}
  - s y(x) + y'(x) & = A \, e^{sx}  \\
  e^{-sx} \left( - s y(x) + y'(x) \right) & = A  \\
  \dfrac{d}{dx} \left( e^{-sx} \, y(x) \right) & = A  \\
  \int \frac{d}{dx} \left( e^{-sx} y(x) \right) & = A \, x + B \\
   e^{-sx} y(x) & = A \, x + B \qquad \rightarrow \qquad  y(x) = A \, x \, e^{sx} + B \, e^{sx}  \ ,
\end{aligned}$$

```

```{dropdown} Independent solutions for root with multiplicity $\ p=3$

$$0 = \left( - s_k + \frac{d}{dx} \right)^3 y(x) = \left( - s_k + \frac{d}{dx} \right) \left( - s_k + \frac{d}{dx} \right) \left( - s_k + \frac{d}{dx} \right) y(x) \ .$$

In order to satisfy this equation, one of the the following two conditions must hold

$$\begin{aligned}
  - s y(x) + y'(x) & = 0 \\
  - s y(x) + y'(x) & = A \, e^{s x} \\
  - s y(x) + y'(x) & = A \, e^{s x} + B \, x \, e^{s x} \\
\end{aligned}$$

The solution of the first condition is...

The solution of the second condition is...

The solution of the third condition is (and contains the solution of the first and the second condition)

$$\begin{aligned}
  - s y(x) + y'(x) & = A \, e^{sx} + B \, x \, e^{sx} \\
  e^{-sx} \left( - s y(x) + y'(x) \right) & = A + B x \\
  \dfrac{d}{dx} \left( e^{-sx} \, y(x) \right) & = A + B x \\
  \int \frac{d}{dx} \left( e^{-sx} y(x) \right) & = A x + \widetilde{B} x^2 + C \\
   e^{-sx} y(x) & = A \, x + B \qquad \rightarrow \qquad  y(x) = C_0 e^{sx} + C_1 \, x \, e^{sx} + C_2 \, x^2 \, e^{sx}  \ .
\end{aligned}$$


```

```{dropdown} Independent solutions for root with multiplicity $\ p$
:open:

$$y(x) = C_0 e^{sx} + C_1 \, x \, e^{sx} + \dots C_{p-1} \, x^{p-1} \, e^{sx}$$

```

(ode:linear-equations:const-coeff:general-sol:homogeneous:as-stability)=
##### Asymptotic stability of the homogeneous equation

The asymptotic stability of the homogeneous equation with non-zero initial conditions is equivalent to the asymptotic stability of the equation to an impulsive force, see [LTI: impulsive force](ode:lti:impulsive-force).

**todo** *how many equilibrium points? If only one equilibrium exists, it's possible to talk about the stability of the whole system, instead of the stability of the individual equilibrium point (without the need of the representation of the phase space*)

**todo** *General definition of asymptotic stability of an equilibrium.*
* stable equilibrium: $y(x) \rightarrow \overline{y}$, as $x \rightarrow + \infty$
* unstable equilibrium: $|y(x) - \overline{y}| \rightarrow +\infty$, as $x \rightarrow + \infty$
* marginally stable equilibrium: if not stable or unstable, i.e. $|y(x) - \overline{y}| < M$, without being asymptotically stable

The conditions for asymptotic stability immediately follows from the general solution of the homogeneous equation:
* asymptotically stable: all the eigenvalues have negative real part, so that 

  $$|e^{s_k x}| = | e^{\text{re}\{ s \} x} e^{j \text{im} \{ s \}} | = e^{\text{re}\{ s \} x} \rightarrow 0 \quad , \quad \text{ as } x \rightarrow + \infty \text{ if } \text{re}\{ s \} < 0 $$

* unstable: there is either 
   * an eigenvalue with positive real part

        $$|e^{s_k x}| = | e^{\text{re}\{ s \} x} e^{j \text{im} \{ s \}} | = e^{\text{re}\{ s \} x} \rightarrow +\infty \quad , \quad \text{ as } x \rightarrow + \infty \text{ if } \text{re}\{ s \} < 0 $$

   * or a multiple eigenvalue with zero real part. As an example a root $s = j \omega$ with multiplicity $p = 2$
        
        $$\left|e^{j \omega x}( C_0 + C_1 x )\right| = \left| C_1 x \right| \rightarrow +\infty \quad , \quad \text{ as } x \rightarrow + \infty $$

       if $C_1 \ne 0$ (but this condition is purely ideal in practical applications, as a perfect zero hardly exists in nature). The same relation holds, when evaluating the pair oc conjugate complex elementary solution, $e^{j \omega} (C_0 + C_1 x) + e^{-j \omega} (C^*_0 + C^*_1 x )$

* marginally-stable, if all the eigenvalues have negative real part, except for a set of imaginary eigenvalues with multiplicity $p = 1$. The asymptotic solution becomes

    $$y(x) \rightarrow \sum_{k \in \text{marginal}} C_k e^{j \omega_k x} $$


(ode:linear-equations:const-coeff:general-sol:particular)=
#### Particular solution


