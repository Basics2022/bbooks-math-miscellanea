(multivariable-calculus)=
# Introduction to multi-variable calculus

(multivariable-calculus:fun)=
## Function

(multivariable-calculus:lim)=
## Limit

(multivariable-calculus:der)=
## Derivatives

(multivariable-calculus:int)=
## Integrals

## Theorems

(multivariable-calculus:green-lemma)=
### Green's lemma

$$\begin{aligned}
  \int_{S} \frac{\partial F}{\partial y} dx dy & =     - \oint_{\partial S} F dx \\
  \int_{S} \frac{\partial G}{\partial x} dx dy & = \quad \oint_{\partial S} G dy   
\end{aligned}$$

```{dropdown} Proof for simple domains.
In a simple domain in  $x$, so that the closed contour $\partial S$ is delimited by the curves $y=Y_1(x)$, $y=Y_2(x) > Y_1(x)$, for $x \in [x_1, x_2]$,

$$\begin{aligned}
  \int_{S} \frac{\partial F}{\partial y} dx dy 
  & =   \int_{x=x_1}^{x_2} \int_{y = Y_1(x)}^{Y_2(x)} \frac{\partial F}{\partial y} dy \, dx = \\
  & =   \int_{x=x_1}^{x_2} \left[ F(x,Y_2(x)) - F(x,Y_1(x)) \right] dx = \\
  & = - \int_{x=x_1}^{x_2} F(x,Y_1(x)) - \int_{x=x_2}^{x_1} F(x, Y_2(x)) dx = \\
  & = - \oint_{\partial S} F(x,y) dx 
\end{aligned}$$

In a simple domain in  $y$, so that the closed contour $\partial S$ is delimited by the curves $x=X_1(y)$, $x=X_2(y) > X_1(y)$ for $y \in [y_1, y_2]$,

$$\begin{aligned}
  \int_{S} \frac{\partial G}{\partial x} dx dy 
  & = \int_{y=y_1}^{y_2} \int_{x = X_1(y)}^{X_2(y)} \frac{\partial G}{\partial x} dx \, dy = \\
  & = \int_{y=y_1}^{y_2} \left[ G(X_2(y),y) - G(X_1(y),y) \right] dy = \\
  & = \int_{y=y_1}^{y_2} G(X_1(y),y) dy + \int_{y=y_2}^{y_1} G(X_2(y),y) dy = \\
  & = \oint_{\partial S} G(x,y) dy 
\end{aligned}$$

```

