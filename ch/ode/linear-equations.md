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

(ode:linear-equations:const-coeff:general-sol:homogeneous:mulitple-roots)=
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

(ode:linear-equations:const-coeff:general-sol:particular)=
#### Particular solution


