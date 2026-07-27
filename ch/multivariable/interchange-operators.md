(multivariable:interchanging-operators)=
# Interchanging operators

* $I \subseteq \mathbb{R}$ interval
* $Y$ set with accumulation point $y_0$
* $f: \ I \times Y \rightarrow \mathbb{R}$

Let the pointwise limit

$$g(x) := \lim_{y \rightarrow y_0} f(x,y) \ $$

exists for $\forall x \in I$, i.e. analogously $\forall \varepsilon > 0$, $\forall x \in I$, $\exists \delta > 0$ so that $|f(x,y) - g(x)| < \delta$ for $\forall y \in U_{y_0, \delta}$.

(multivariable:interchanging-operators:limit-limit)=
## Interchange limits - Moore-Osgood theorem

Let $x_0$ a limit point of $I$. Suppose

1. for $\forall y \in V_{y_0}$ (punctured neighborhood of $y_0$), $\varphi(y) := \lim_{x \rightarrow x_0} f(x,y)$ exists. (*Here $y$ is taken as fixed. If $y$ is taken as a parameter, these are common limits of function of one variable, for all the possible parameters $y$; can it be interpreted as pointwise convergence as $x \rightarrow x_0$ for all the points $y \in V_{y_0}$?*)
2. $f(x,y) \rightarrow g(x)$ as $y \rightarrow y_0$ uniformly for $x \in U_{x_0}$ (punctured)

Then

* $\lim_{y \rightarrow y_0} \varphi(y)$ exists and

  $$\lim_{y \rightarrow y_0} \varphi(y) = \lim_{x \rightarrow x_0} g(x) = \lim_{(x,y) \rightarrow (x_0, y_0)} f(x,y) \ .$$

```{dropdown} Proof
:open:

**Step 1.** By 2. (see definition of uniform convergence), for $\forall \varepsilon > 0$, $\exists \delta_1 > 0$ s.t. $| f(x,y) - g(x) | < \frac{\varepsilon}{3}$ for $\forall y \in V_{y_0, \delta_1}$, $\forall x \in U_{x_0}$. Take $y_1, y_2 \in V_{y_0, \delta_1}$, then

$$|f(x,y_1) - f(x,y_2)| \le |f(x,y_1) - g(x)| + |g(x) - f(x,y_2)| < \frac{2}{3} \varepsilon \ .$$

As $x \rightarrow x_0$, from 1.,

$$\lim_{x \rightarrow x_0} |f(x,y_1) - f(x,y_2)| = | \varphi(y_1) - \varphi(y_2) | \le \frac{2}{3} \varepsilon \ .$$

Thus, as $\varphi(y)$ satisfies the Cauchy condition, the limit $\lim_{y \rightarrow y_0} \varphi(y) =: L$ exists.

**Step 2.** Shrinking $V_{y_0, \delta_1}$ to $V_{y_0, \delta_2}$ so that $| \varphi(y) - L | < \frac{\varepsilon}{3}$ for $\forall y \in V_{y_0, \delta_2}$. From the definition of $\varphi(y)$, then $\exists \delta_x > 0$ s.t.

$$|f(x,y) - \varphi(y)| < \frac{\varepsilon}{3} \quad , \quad \forall 0 < | x - x_0 | < \delta_x \ .$$

Thus

$$| g(x) - L | \le | g(x) - f(x,y) | + | f(x,y) - \varphi(y) | + | \varphi(y) - L | < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon \ , $$

i.e. $g(x) \rightarrow L$ as $x \rightarrow x_0$.

```

**Counter-example.** $f(x,y) = \frac{x^2}{x^2 + y^2}$ on $(x,y) \ne (0,0)$ for $x_0 = y_0 = 0$. This function is not uniformly convergent as $y \rightarrow y_0$.

...


```{dropdown} Pointwise and uniform convergence
:open:

$$\lim_{y \rightarrow y_0} f(x,y) = g(x) \ .$$

**Pointwise.** For $\forall \varepsilon > 0$, $\forall x \in X$, $\exists \delta > 0$ s.t. $| f(x,y) - g(x) | < \varepsilon$ for $\forall y \in Y_{y_0, \delta}$. Here $\delta( \varepsilon, x)$.


**Uniform.** For $\forall \varepsilon > 0$, $\exists \delta > 0$ s.t. $| f(x,y) - g(x) | < \varepsilon$ for $\forall y \in Y_{y_0, \delta}$, $\forall x \in X$, . Here $\delta( \varepsilon)$.
This can be written in terms of $\sup | f(x,y) - g(x) |$ as well, as it must hold for $\forall x \in X$.


```

```{dropdown} Cauchy criterion
:open:

Let $I \subseteq \mathbb{R}$ be an interval containing a limit point $x_0$, and let $f: I \setminus \{x_0\} \to \mathbb{R}$.

The limit $\lim_{x\to x_0} f(x)$ exists in $\mathbb{R}$ if and only if for every $\varepsilon > 0$, there exists a deleted neighborhood $U = (x_0 - \delta, x_0 + \delta) \setminus \{x_0\}$ such that for all $x_1, x_2 \in U$,

$$\vert{}f(x_1) - f(x_2)\vert{} < \varepsilon \ .$$

**Proof.**

**Direction $(\Rightarrow)$: if the limit exists, the Cauchy condition holds.** Assume $\lim_{x \to x_0} f(x) = L$ exists. Fix $\varepsilon > 0$. By definition of a functional limit, there exists $\delta > 0$ such that for all $x \in I$ with $0 < \vert{}x - x_0\vert{} < \delta$:

$$\vert{}f(x) - L\vert{} < \frac{\varepsilon}{2}$$

Take any $x_1, x_2 \in I$ such that $0 < \vert{}x_1 - x_0\vert{} < \delta$ and $0 < \vert{}x_2 - x_0\vert{} < \delta$. By the triangle inequality:

$$\vert{}f(x_1) - f(x_2)\vert{} = \vert{}(f(x_1) - L) - (f(x_2) - L)\vert{} \le \vert{}f(x_1) - L\vert{} + \vert{}f(x_2) - L\vert{}$$

Substitution gives $\vert{}f(x_1) - f(x_2)\vert{} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$. Thus, the condition holds. $\square$

**Direction $(\Leftarrow)$: if the Cauchy condition holds, then the limit exists.**

...**todo**...

```

```{dropdown} Bolzano-Weierstrass theorem
:open:

Every bounded sequence of real numbers has a convergence subsequence, i.e. let $( x_n )_{x=1}^{+\infty}$ be a sequence in $\mathbb{R}$. If $\exists a, b \in \mathbb{R}$ s.t. $a \le x_n \le b$, then $( x_n )_{n=1}^{+\infty}$ contains a convergent subsequence $(x_{n_k})_{k=1}^{+\infty}$

**Proof.** Take the original interval $I_0 = [a,b]$, and split it with its midpoint $c_0 = \frac{a+b}{2}$. (At least) one of the two sub-intervals contains infinitey many terms of the original sequence. Choose this sub-interval $I_1$, and repeat the process. Select the sub-sequence with these rules: pick $x_{n_1} \in I_1$; pick $x_{n_2} \in I_2$ s.t. $n_2 > n_1$ (always possible, as there's a infinite number of terms); pick $x_{n_3} \in I_3$ s.t. $n_3 > n_2$;... The sequence of the left endpoints $( a_k )$ is non-decreasing and bounded above by $b$, so by [monotone convergence theorem](https://en.wikipedia.org/wiki/Monotone_convergence_theorem), then $\lim_{k \rightarrow +\infty} a_k = L$, for some $L \in \mathbb{R}$. The series of right endpoints satisfies $b_k = a_k + \frac{b-a}{2^k}$ and thus $\lim_{k \rightarrow +\infty} b_k = L$ as well. Thus, as $a_k \le x_{n_k} \le b_k$, it follows (squeeze theorem) that $\lim_{k \rightarrow +\infty} x_{n_k} = L$. $\blacksquare$


```


```{dropdown} From $\ < \ $ to $\ \le \ $ in limits
:open:

Let $f(x) < C$ for $x \in U_{x_0}$. Then $L := \lim_{x \rightarrow x_0} f(x) \le C$.

**Proof.** By contradiction, let's assume $L > C$. 1) Define $\varepsilon := L - C > 0$; 2) apply the definition of limit. For $\forall \varepsilon > 0$, $\exists \delta > 0$ s.t. $| f(x) - L | < \varepsilon$ for $\forall y \in U_{x_0, \delta}$; 3) this implies $L - \varepsilon < f(x) < L + \varepsilon$; 4) replacing $\varepsilon = L - C$, it follows $C < f(x) < - C$, and this contains a contradiction with the assumption of the theorem $f(x) < C$. It follows that the premise $L > C$ is false, and thus $L \le C$. $\blacksquare$

```

(multivariable:interchanging-operators:limit-integral)=
## Interchange limit and integral

If

* $[a,b]$ compact
* $f(\cdot, y)$ Riemann integrable on $[a,b]$ for each $y$
* $f(x,y) \rightarrow g(x)$ uniformly as $y \rightarrow y_0$ uniformly for $x \in [a,b]$

Then

* $g$ is Riemann integrable and

  $$\lim_{y \rightarrow y_0} \int_{x=a}^{b} f(x,y) \, dx = \int_{x=a}^{b} g(x) \, dx \ .$$

```{dropdown} Proof
:open:

**Integrability of $g(x)$.** Given $\varepsilon > 0$, there exists a neighborhood of $y_0$ so that 

$$\sup_{x \in [a,b]} |f(x,y) - g(x)| < \frac{\varepsilon}{4(b-a)} \ .$$

Since $f(\cdot, y)$ is Riemann integrable, it's possible to choose a partition $P$ so that $U(f(\cdot,y),P) - L(f(\cdot,y),P) < \frac{\varepsilon}{2}$, with 

$$\begin{aligned}
  L(f(x),P) & = \sum_{n} \inf_{x\in I_n} f(x) ( x_{n} - x_{n-1} ) \\
  U(f(x),P) & = \sum_{n} \sup_{x\in I_n} f(x) ( x_{n} - x_{n-1} ) \\
\end{aligned}$$

As $\sup g = \sup ( f + g - f ) \le \sup f + \sup |f-g|$, $\inf g = \inf ( f + g - f ) \le \inf f - \sup | f-g |$,

$$U(g,P) - L(g,P) \le U(f,P) - U(f,P) + 2 \sup|f-g| (b-a) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon \ .$$

For Riemann crieterion, $g$ is Riemann integrable. Then

$$\left| \int_{a}^{b} f(x,y) \, dx - \int_{a}^{b} g(x) \, dx \right| \le \int_{a}^{b} \left| f(x,y) - g(x) \right| \, dx \le (b-a) \sup_{x \in [a,b]} | f(x,y) - g(x) | < \frac{varepsilon}{4} \ ,$$

and thus

$$\lim_{y \rightarrow y_0} \int_{a}^{b} f(x,y) \, dx = \int_{a}^{b} \lim_{y \rightarrow y_0} f(x,y) \, dx \ .$$


```

```{dropdown} Riemann integrable function
:open:

$$\int_{x=a}^{b} f(x) \,\ dx = \lim_{\Delta x \rightarrow +\infty} \sum_{n=1}^{N} f(\xi_n) ( x_{n} - x_{n-1} ) \ ,$$

with $\xi_n \in [x_n, x_{n+1}]$ with $x_0 = a$, $x_N = b$.

```

```{dropdown} Riemann criterion for integrability
:open:


```


(multivariable:interchanging-operators:limit-integral:riemann)=
### Riemann integral

(multivariable:interchanging-operators:limit-integral:lebesgue)=
### Lebesgue integral


(multivariable:interchanging-operators:limit-derivative)=
## Interchange limit and derivative

