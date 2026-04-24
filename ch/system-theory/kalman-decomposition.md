(system-theory:kalman-decomposition)=
# Kalman decomposition

In this section, [singular value decomposition](math:svd) of the Gramians of [observability](observability-detectability) and [controllability](controllability-reachability) helps in the decomposition of a LTI system in its non-observable/observable and controllable/non-controllable parts.

$A$**-invariance** of $\text{Ran}(\mathbf{W}_c)$ and $\text{Ker}(\mathbf{W}_o)$ is exploited.

**todo** *Infinite-horizon time, or steady-state conditions, are discussed here?*

(system-theory:kalman-decomposition:controllability)=
## Controllability

```{dropdown} Controllability
:open:

Let $\mathbf{W}_c$ the controllability Gramian of a LTI system. Controllable states belong to the range of $W_c$. Controllable states define a sub-space of $\mathbb{R}^n$, being $\mathbf{x} \in \mathbb{R}^n$. Singular value decomposition (or spectral decomposition) of the semi-poisitive definite symmetric Gramian matrix,

$$\mathbf{W}_C = \mathbf{U}_C \boldsymbol\Sigma_C \mathbf{U}_C^* \ ,$$

provides a decomposition of $\mathbb{R}^n$ into the controllable sub-space and its orthogonal complement, with

$$\mathbf{W}_C = [ \, \mathbf{U}_c \, | \, \mathbf{U}_{\overline{c}} \, ] \begin{bmatrix} \boldsymbol\Sigma_c & \cdot \\ \cdot & \cdot \end{bmatrix} \begin{bmatrix} \mathbf{U}_c^* \\ \mathbf{U}_{\overline{c}} \end{bmatrix} \ ,$$

with the columns of $\mathbf{U}_c$ as a base of the controllable sub-space. Introducing a change of variable of the state

$$\mathbf{x} = \mathbf{U}_C \mathbf{x}_1 \ ,$$

the LTI system becomes

$$\begin{aligned}
  \dot{\mathbf{x}}_1 & = \mathbf{U}_C^* \mathbf{A} \mathbf{U}_C \mathbf{x}_1 + \mathbf{U}_C^* \mathbf{B} \mathbf{u} \\
       \mathbf{y}    & = \mathbf{C} \mathbf{U}_C \mathbf{x}_1 + \mathbf{D} \mathbf{u} \ .
\end{aligned}$$

and thus

$$\begin{aligned}
 \frac{d}{dt} \begin{bmatrix} \mathbf{x}_{1,c} \\ \mathbf{x}_{1,\overline{c}} \end{bmatrix} & = \begin{bmatrix} \mathbf{U}_c^* \mathbf{A} \mathbf{U}_c & \mathbf{U}_c^* \mathbf{A} \mathbf{U}_{\overline{c}} \\ \mathbf{0} & \mathbf{U}_{\overline{c}}^* \mathbf{A} \mathbf{U}_{\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{1,c} \\ \mathbf{x}_{1,\overline{c}} \end{bmatrix} + \begin{bmatrix} \mathbf{U}_c^* \mathbf{B} \\ \mathbf{0} \end{bmatrix} \mathbf{u} \\ 
  \mathbf{y} & = \begin{bmatrix} \mathbf{C} \mathbf{U}_c & \mathbf{C} \mathbf{U}_{\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{1,c} \\ \mathbf{x}_{1, \overline{c}} \end{bmatrix} + \mathbf{D} \mathbf{u} \ .
\end{aligned}$$


```

```{dropdown} Properties
:open:

The columns of the matrix $\mathscr{C} = [ \, \mathbf{B} \, | \, \mathbf{A} \mathbf{B} \, | \, \dots \, | \, \mathbf{A}^{n-1} \mathbf{B} \, ]$ are linear combinations of the range of $\mathbf{W}_C$, i.e. of the columns of $\mathbf{U}_c$, and thus they're orthogonal w.r.t. the columns of $\mathbf{U}_{\overline{c}}$. It follows that

$$\begin{aligned}
  \mathbf{U}_{\overline{c}}^* \mathbf{B} & = \mathbf{0} \\
  \mathbf{U}_{\overline{c}}^* \mathbf{A}^k \mathbf{B} & = \mathbf{0} \quad , \quad \forall k \in \mathbb{N} \\
\end{aligned}$$

as $\mathbf{U}^*_{\overline{c}} \mathbf{A}^k \mathbf{B} = \mathbf{U}_{\overline{c}}^* \mathbf{U}_c \boldsymbol\alpha$ and $\mathbf{U}_{\overline{c}}^* \mathbf{U}_c = \mathbf{0}$

```


(system-theory:kalman-decomposition:observability)=
## Observability

```{dropdown} Observability
:open:

Let $\mathbf{W}_o$ the observability Gramian of a LTI system. Non-observable states belong to the kernel of $W_o$. Non-observable states define a sub-space of $\mathbb{R}^n$, being $\mathbf{x} \in \mathbb{R}^n$. Singular value decomposition (or spectral decomposition) of the semi-poisitive definite symmetric Gramian matrix,

$$\mathbf{W}_O = \mathbf{U}_O \boldsymbol\Sigma_O \mathbf{U}_O^* \ ,$$

provides a decomposition of $\mathbb{R}^n$ into the non-observable sub-space and its orthogonal complement, with

$$\mathbf{W}_O = [ \, \mathbf{U}_o \, | \, \mathbf{U}_{\overline{o}} \, ] \begin{bmatrix} \boldsymbol\Sigma_o & \cdot \\ \cdot & \cdot \end{bmatrix} \begin{bmatrix} \mathbf{U}_o^* \\ \mathbf{U}_{\overline{o}} \end{bmatrix} \ ,$$

with the columns of $\mathbf{U}_{\overline{o}}$ as a base of the non-observable sub-space. Introducing a change of variable of the state

$$\mathbf{x} = \mathbf{U}_o \mathbf{x}_1 \ ,$$

the LTI system becomes

$$\begin{aligned}
  \dot{\mathbf{x}}_1 & = \mathbf{U}_O^* \mathbf{A} \mathbf{U}_O \mathbf{x}_1 + \mathbf{U}_O^* \mathbf{B} \mathbf{u} \\
       \mathbf{y}    & = \mathbf{C} \mathbf{U}_O \mathbf{x}_1 + \mathbf{D} \mathbf{u} \ .
\end{aligned}$$

and thus

$$\begin{aligned}
 \frac{d}{dt} \begin{bmatrix} \mathbf{x}_{1,o} \\ \mathbf{x}_{1,\overline{o}} \end{bmatrix} & = \begin{bmatrix} \mathbf{U}_o^* \mathbf{A} \mathbf{U}_o & \mathbf{0} \\ \mathbf{U}_{\overline{o}}^* \mathbf{A} \mathbf{U}_{o} & \mathbf{U}_{\overline{o}}^* \mathbf{A} \mathbf{U}_{\overline{o}} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{1,o} \\ \mathbf{x}_{1,\overline{o}} \end{bmatrix} + \begin{bmatrix} \mathbf{U}_o^* \mathbf{B} \\ \mathbf{U}_{\overline{o}}^* \mathbf{B} \end{bmatrix} \mathbf{u} \\ 
  \mathbf{y} & = \begin{bmatrix} \mathbf{C} \mathbf{U}_o & \mathbf{0} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{1,o} \\ \mathbf{x}_{1, \overline{o}} \end{bmatrix} + \mathbf{D} \mathbf{u} \ ,
\end{aligned}$$

as $\mathbf{U}_o^* \mathbf{A} \mathbf{U}_{\overline{o}} = \mathbf{0}$ (see below).


```

```{dropdown} Properties
:open:

The kernel of the observability Gramian is the sub-space of vectors $\mathbf{v}$ so that $\mathscr{O} \mathbf{v} = \mathbf{0}$, with

$$\mathscr{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C} \mathbf{A} \\ \dots \\ \mathbf{C} \mathbf{A}^{n-1} \end{bmatrix} \ .$$

It follows that

$$\begin{aligned}
   \mathbf{C} \mathbf{U}_{\overline{o}} & = \mathbf{0} \\
   \mathbf{C} \mathbf{A}^k \mathbf{U}_{\overline{o}}  & = \mathbf{0} \quad , \quad \forall k \in \mathbb{N} \\
\end{aligned}$$

so that the rows of $\mathbf{C}$ and the rows of $\mathbf{C} \mathbf{A}^k$ are linear combinations of the columns of $\mathbf{U}_o$, i.e. the columns of $\left( \mathbf{C} \mathbf{A}^k \right)^*$ are linear combinations of the columns of $\mathbf{U}_o$,

$$\left( \mathbf{C} \mathbf{A}^k \right)^* = \mathbf{U}_o \boldsymbol\alpha \ , $$

or

$$\mathbf{C} \mathbf{A}^k = \boldsymbol\alpha^* \mathbf{U}_o^* \ .$$

As the property holds for every $k \in \mathbb{N}$, the following holds as well

$$\mathbf{U}_o^* \mathbf{A} \mathbf{U}_{\overline{o}} \ .$$


```

(system-theory:kalman-decomposition:kalman)=
## Kalman decomposition

```{dropdown} Kalman decomposition
:open:

A first decomposition is applied for controllability. Two further decompositions for observability follows on the controllable and non-controllable parts of the system.

The first change of coordinates with the singular value decomposition of the controllability Gramian 

$$\mathbf{x} = \begin{bmatrix} \mathbf{U}_c & \mathbf{U}_{\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{1,c} \\ \mathbf{x}_{1,\overline{c}} \end{bmatrix}$$

gives

$$\begin{aligned}
 \frac{d}{dt} \begin{bmatrix} \mathbf{x}_{1,c} \\ \mathbf{x}_{1,\overline{c}} \end{bmatrix} & = \begin{bmatrix} \mathbf{U}_c^* \mathbf{A} \mathbf{U}_c & \mathbf{U}_c^* \mathbf{A} \mathbf{U}_{\overline{c}} \\ \mathbf{0} & \mathbf{U}_{\overline{c}}^* \mathbf{A} \mathbf{U}_{\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{1,c} \\ \mathbf{x}_{1,\overline{c}} \end{bmatrix} + \begin{bmatrix} \mathbf{U}_c^* \mathbf{B} \\ \mathbf{0} \end{bmatrix} \mathbf{u} \\ 
  \mathbf{y} & = \begin{bmatrix} \mathbf{C} \mathbf{U}_c & \mathbf{C} \mathbf{U}_{\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{1,c} \\ \mathbf{x}_{1, \overline{c}} \end{bmatrix} + \mathbf{D} \mathbf{u} \ .
\end{aligned}$$

Then the controllable variables and the non-controllable variables are further transformed as

$$\begin{aligned}
  \mathbf{x}_{1,c} & = \mathbf{U}_O^c \mathbf{x}_{2,c} = \begin{bmatrix} \mathbf{U}_o^c & \mathbf{U}_{\overline{o}}^c \end{bmatrix} \begin{bmatrix} \mathbf{x}_{c,o} \\ \mathbf{x}_{c,\overline{o}} \end{bmatrix} \\
  \mathbf{x}_{1,\overline{c}} & = \mathbf{U}_O^{\overline{c}} \mathbf{x}_{2,\overline{c}} = \begin{bmatrix} \mathbf{U}_o^{\overline{c}} & \mathbf{U}_{\overline{o}}^{\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{\overline{c},o} \\ \mathbf{x}_{\overline{c},\overline{o}} \end{bmatrix} \ ,
\end{aligned}$$

or

$$\begin{bmatrix} \mathbf{x}_{1,c} \\ \mathbf{x}_{1,\overline{c}} \end{bmatrix} = \begin{bmatrix} \mathbf{U}_o^c & \mathbf{U}_{\overline{o}}^{c} & \cdot & \cdot \\ \cdot & \cdot & \mathbf{U}_o^{\overline{c}} & \mathbf{U}_{\overline{o}}^{\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{x}_{co} \\ \mathbf{x}_{c\overline{o}} \\ \mathbf{x}_{\overline{c}o} \\ \mathbf{x}_{\overline{c}\overline{o}} \end{bmatrix} \ .$$

with $\mathbf{W}_{c,1}(\mathbf{A}_{cc}, \mathbf{C}_c) = \mathbf{U}_O^{c} \boldsymbol\Sigma_{c,1} \mathbf{U}_O^{c *}$, and $\mathbf{W}_{\overline{c},1}(\mathbf{A}_{\overline{c}\overline{c}}, \mathbf{C}_{\overline{c}}) = \mathbf{U}_O^{\overline{c}} \boldsymbol\Sigma_{\overline{c},1} \mathbf{U}_O^{\overline{c} *}$.


```

```{dropdown}
:open:

For the non-controllable space, the non-observable part $\mathbf{U}_{\overline{o}}^{\overline{c}}$ satisfies

$$\mathbf{C}_{\overline{c}} \mathbf{A}_{\overline{c}\overline{c}}^k \mathbf{U}_{\overline{o}}^{\overline{c}} = \mathbf{0} \ .$$

Thus, the matrix

$$\begin{bmatrix} \mathbf{0} \\ \mathbf{U}_{\overline{o}}^{\overline{c}} \end{bmatrix} \ ,$$

satisfies

$$\mathbf{C}_1 \mathbf{A}_1 \begin{bmatrix} \mathbf{0} \\ \mathbf{U}_{\overline{o}}^{\overline{c}}  \end{bmatrix} = \mathbf{0} \ ,$$

and thus the columns of this matrix belongs to the non-observable subspace of $\mathbf{A}_1$. Recalling the first transformation, $\mathbf{A}_1 = \mathbf{U}_C^* \mathbf{A} \mathbf{U}_C$, $\mathbf{C}_1 = \mathbf{C} \mathbf{U}_C$, it follows that 

$$\mathbf{C} \mathbf{A} \mathbf{U}_C \begin{bmatrix} \mathbf{0} \\ \mathbf{U}_{\overline{o}}^{\overline{c}}  \end{bmatrix} = \mathbf{0} \ ,$$

and the expression of the non-controllable, non-observable subspace. If the vector $\begin{bmatrix} \mathbf{0} \\ \mathbf{U}_{\overline{o}}^{\overline{c}} \end{bmatrix}$ belongs to the kernel $\mathbf{W}_{o,1}$, thus also the vector $\mathbf{A}_1 \begin{bmatrix} \mathbf{0} \\ \mathbf{U}_{\overline{o}}^{\overline{c}} \end{bmatrix}$ belongs to the kernel of $\mathbf{W}_{o,1}$ for the $\mathbf{A}_1$-invariance of the kernel of $\mathbf{W}_{o,1}$. Thus, this vector is orthogonal to the vectors of the observability complement, **todo** *Prove that the columns of the following matrices are a basis of the observability complement*

$$\begin{bmatrix} \mathbf{U}_{o}^{c} \\ \mathbf{0} \end{bmatrix} \quad , \quad \begin{bmatrix} \mathbf{0} \\ \mathbf{U}_o^{\overline{c}} \end{bmatrix} \ .$$

Thus,

$$\mathbf{0} = \begin{bmatrix} \mathbf{U}_o^{c *} & \mathbf{0} \end{bmatrix} \begin{bmatrix} \mathbf{A}_{cc} & \mathbf{A}_{c\overline{c}} \\ \mathbf{0} & \mathbf{A}_{\overline{c}\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{0} \\ \mathbf{U}_{\overline{o}}^{\overline{c}} \end{bmatrix} = \mathbf{U}_o^{c *} \mathbf{A}_{c \overline{c}} \mathbf{U}_{\overline{o}}^{\overline{c}} \ .$$

provides an orthogonality condition between the observable-controllable and non-observable and non-controllable part of the system, while

$$\mathbf{0} = \begin{bmatrix} \mathbf{0} & \mathbf{U}_o^{\overline{c} *} \end{bmatrix} \begin{bmatrix} \mathbf{A}_{cc} & \mathbf{A}_{c\overline{c}} \\ \mathbf{0} & \mathbf{A}_{\overline{c}\overline{c}} \end{bmatrix} \begin{bmatrix} \mathbf{0} \\ \mathbf{U}_{\overline{o}}^{\overline{c}} \end{bmatrix} = \mathbf{U}_o^{\overline{c} *} \mathbf{A}_{\overline{c} \overline{c}} \mathbf{U}_{\overline{o}}^{\overline{c}} \ .$$

was already known as a property of the observability partition.

```


```{dropdown} Transformation and properties of Gramian matrices
:open:

$$\begin{aligned}
  \mathbf{W}_{C,1} & = \mathbf{U}_C \mathbf{W}_C \mathbf{U}_C^* \\
  \mathbf{W}_{O,1} & = \mathbf{U}^*_C \mathbf{W}_O \mathbf{U}_C
\end{aligned}$$

$$\mathbf{A}_1 = \mathbf{U}_C \mathbf{A} \mathbf{U}_C^*$$


```


