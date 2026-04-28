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
Let

* $\mathbf{U}_1$ spanning the **reachable** and **non-observable sub-psace**, $R \cap \overline{O}$
* $\mathbf{U}_2$ complementing $\mathbf{U}_1$ to get the reachable sub-sspace $R$
* $\mathbf{U}_3$ complementing $\mathbf{U}_3$ to get the non-observable sub-space $O$
* $\mathbf{U}_4$ complementing $\mathbf{U}_1$, $\mathbf{U}_2$, $\mathbf{U}_3$ to get $\mathbb{R}^n$

The columns of $\mathbf{U}_1$ and $\mathbf{U}_3$ form a vector basis of the non-observable sub-space. The columns of $\mathbf{U}_1$ and $\mathbf{U}_2$ form a vector basis of the reachable subspace.  

A coordinate transfromation of the form

$$\mathbf{x} = \mathbf{T} \mathbf{x} = \begin{bmatrix} \ \mathbf{U}_1 & \mathbf{U}_2 & \mathbf{U}_3 & \mathbf{U}_4 \ \end{bmatrix} \mathbf{z} = \begin{bmatrix} \ \mathbf{U}_1 & \mathbf{U}_2 & \mathbf{U}_3 & \mathbf{U}_4 \ \end{bmatrix} \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \\ \mathbf{z}_3 \\ \mathbf{z}_4 \end{bmatrix} \ ,$$

produce a transformed system with the following structure

$$\left\{\begin{aligned}
  \frac{d}{dt} \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \\ \mathbf{z}_3 \\ \mathbf{z}_4 \end{bmatrix} & =
  \begin{bmatrix} 
     \mathbf{A}_{11} & \mathbf{A}_{12} & \mathbf{A}_{13} & \mathbf{A}_{14} \\ 
     \mathbf{0}      & \mathbf{A}_{22} & \mathbf{0}      & \mathbf{A}_{24} \\ 
     \mathbf{0}      & \mathbf{0}      & \mathbf{A}_{33} & \mathbf{A}_{34} \\ 
     \mathbf{0}      & \mathbf{0}      & \mathbf{0}      & \mathbf{A}_{44} \\ 
  \end{bmatrix}
  \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \\ \mathbf{z}_3 \\ \mathbf{z}_4 \end{bmatrix} +
  \begin{bmatrix} \mathbf{B}_1 \\ \mathbf{B}_2 \\ \mathbf{0} \\ \mathbf{0} \end{bmatrix} \mathbf{u} \\
  \mathbf{y} & = \begin{bmatrix} \ \mathbf{0} & \mathbf{C}_2 & \mathbf{0} & \mathbf{C}_4 \end{bmatrix}
  \begin{bmatrix} \mathbf{z}_1 \\ \mathbf{z}_2 \\ \mathbf{z}_3 \\ \mathbf{z}_4 \end{bmatrix} +
  \mathbf{D} \mathbf{u} 
\end{aligned}\right.$$


````{dropdown} Details
:open:

**Columns of $\ \mathbf{T}$.** Here the columns of $\mathbf{U}_1$ are assumed to be a set of unit normal vectors, $\mathbf{U}_1^* \mathbf{U}_1 = \mathbf{I}$. Without this assumption, Gram-Schmidt orthogonalization process ensure a orthogonal basis $\boldsymbol\Phi_1$ exists and the basis in $\mathbf{U}_1$ can be written as a linear combination of the columns of $\boldsymbol\Phi_1$, i.e. $\mathbf{U}_1 = \boldsymbol\Phi_1 \boldsymbol\alpha_1$, with non-singular $\boldsymbol\alpha_1$. Columns of $\mathbf{U}_2$ are linearly independent from the columns of $\mathbf{U}_1$ to form a basis of the reachable sub-space. Columns $\mathbf{U}_3$ are linearly independent from the columns of $\mathbf{U}_1$ to form a basis of the non-observable sub-space. In general, they're not unit orthogonal but a unit orthogonal basis can be found, to get

$$\begin{aligned}
  \mathbf{U}_2 & = \boldsymbol\Phi_2 \boldsymbol\alpha_2 + \mathbf{U}_1 \boldsymbol\alpha_{12} \\
  \mathbf{U}_3 & = \boldsymbol\Phi_3 \boldsymbol\alpha_3 + \mathbf{U}_1 \boldsymbol\alpha_{13} \ .
\end{aligned}$$

In general, the columns of $\boldsymbol\Phi_2$ and $\boldsymbol\Phi_3$ are not mutually orthogonal, as the reachable sub-space and the non-observable sub-space are not orthogonal, $\boldsymbol\Phi_2^* \boldsymbol\Phi_3 \ne \mathbf{0}$. The columns of the complement $\mathbf{U}_4$ are assumed to be unit normal vectors, orthogonal w.r.t. the columns of $\mathbf{U}_1$, $\mathbf{U}_2$, $\mathbf{U}_3$ (and of $\boldsymbol\Phi_2$, $\boldsymbol\Phi_3$).

**Recast $\ \mathbf{T}$.**

$$
\mathbf{T} = \begin{bmatrix} \ \mathbf{U}_1 & \boldsymbol\Phi_2 & \boldsymbol\Phi_3 & \mathbf{U}_4 \ \end{bmatrix}
\begin{bmatrix}
  \mathbf{I} & \boldsymbol\alpha_{12} & \boldsymbol\alpha_{13} & \cdot \\
  \cdot      & \boldsymbol\alpha_{2 } & \cdot                  & \cdot \\
  \cdot      & \cdot                  & \boldsymbol\alpha_{3 } & \cdot \\
  \cdot      & \cdot                  & \cdot                  & \mathbf{I}
\end{bmatrix} =
\boldsymbol\Phi \boldsymbol\alpha
$$

**Inverse $\ \mathbf{T}^{-1}$.**

$$\mathbf{T}^{-1} = \boldsymbol\alpha^{-1} \boldsymbol\Phi^{-1} \ ,$$

with

$$\boldsymbol\alpha^{-1} & = 
\begin{bmatrix}
  \mathbf{I} &-\boldsymbol\alpha_{12}\boldsymbol\alpha_{2 }^{-1}      &-\boldsymbol\alpha_{13}\boldsymbol\alpha_{3 }^{-1}      & \cdot \\
  \cdot      & \boldsymbol\alpha_{2 }^{-1} & \cdot                       & \cdot \\
  \cdot      & \cdot                       & \boldsymbol\alpha_{3 }^{-1} & \cdot \\
  \cdot      & \cdot                       & \cdot                       & \mathbf{I}
\end{bmatrix}$$

$$\boldsymbol\Phi^{-1} & =
\begin{bmatrix}
  \mathbf{U}_1^* \\
  \left[ \left( \mathbf{I} - \boldsymbol\Phi_3 \boldsymbol\Phi_3^* \right) \boldsymbol\Phi_2 \left( \mathbf{I} - \boldsymbol\Phi_2^* \boldsymbol\Phi_3 \boldsymbol\Phi_3^* \boldsymbol\Phi_2 \right)^{-1} \right]^* \\
  \left[ \left( \mathbf{I} - \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \right) \boldsymbol\Phi_3 \left( \mathbf{I} - \boldsymbol\Phi_3^* \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \boldsymbol\Phi_3 \right)^{-1} \right]^* \\
  \mathbf{U}_4^* 
\end{bmatrix}
$$

```{dropdown} Details
:open:



```

**Transformed matrices: matrix $\hat{\mathbf{C}}$.**


$$\hat{\mathbf{C}} = \mathbf{C} \mathbf{T} = \mathbf{C} \boldsymbol\Phi \boldsymbol\alpha$$

$$\mathbf{C} \boldsymbol\Phi = \mathbf{C} \begin{bmatrix} \ \mathbf{U}_1 & \boldsymbol\Phi_2 & \boldsymbol\Phi_3 & \mathbf{U}_4 \ \end{bmatrix} = \begin{bmatrix} \ \mathbf{0}   & \mathbf{C} \boldsymbol\Phi_2 & \mathbf{0} & \mathbf{C} \mathbf{U}_4 \ \end{bmatrix} \ ,$$

as $\mathbf{C} \mathbf{U}_1 = \mathbf{0}$, $\mathbf{C} \boldsymbol\Phi_3 = \mathbf{0}$. Looking at the structures of the matrices $\mathbf{C} \boldsymbol\Phi$ and $\boldsymbol\alpha$, 

$$
\begin{bmatrix} \cdot & \ast & \cdot & \ast \end{bmatrix}
\begin{bmatrix} 
  \ast  & \ast  & \ast  & \cdot \\
  \cdot & \ast  & \cdot & \cdot \\
  \cdot & \cdot & \ast  & \cdot \\
  \cdot & \cdot & \cdot & \ast  \\
\end{bmatrix} = 
\begin{bmatrix} \cdot & \ast & \cdot & \ast \end{bmatrix} \ ,
$$

it's easy to show that this multiplication preserves the structure of the matrix $\mathbf{C}\boldsymbol\Phi$. Explicitly evaluating the non-zero blocks, the transformed matrix reads

$$\hat{\mathbf{C}} = \begin{bmatrix} \ \mathbf{0} & \mathbf{C} \boldsymbol\Phi_2 \boldsymbol\alpha_2 & \mathbf{0} & \mathbf{C}\mathbf{U}_4 \ \end{bmatrix}$$

**Transformed matrices: matrix $\hat{\mathbf{B}}$.**

$$\hat{\mathbf{B}} =  \mathbf{T}^{-1} \mathbf{B} = \boldsymbol\alpha^{-1} \boldsymbol\Phi^{-1} \mathbf{B}$$

$$
\boldsymbol\Phi^{-1} \mathbf{B} = 
\begin{bmatrix}
  \mathbf{U}_1^* \\
  \left[ \left( \mathbf{I} - \boldsymbol\Phi_3 \boldsymbol\Phi_3^* \right) \boldsymbol\Phi_2 \left( \mathbf{I} - \boldsymbol\Phi_2^* \boldsymbol\Phi_3 \boldsymbol\Phi_3^* \boldsymbol\Phi_2 \right)^{-1} \right]^* \\
  \left[ \left( \mathbf{I} - \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \right) \boldsymbol\Phi_3 \left( \mathbf{I} - \boldsymbol\Phi_3^* \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \boldsymbol\Phi_3 \right)^{-1} \right]^* \\
  \mathbf{U}_4^* 
\end{bmatrix} \mathbf{B}
$$

as $\mathbf{U}_1^* \mathbf{B} = \mathbf{0}$, $\left[ \left( \mathbf{I} - \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \right) \boldsymbol\Phi_3 \right]^* \mathbf{B}  = \mathbf{0}$. The last relation holds, as $\left( \mathbf{I} - \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \right) \boldsymbol\Phi_3$ is the orthogonal projection of $\boldsymbol\Phi_3$ perpendicular to the vectors $\boldsymbol\Phi_2$. Since this projection is perpendicular both to $\mathbf{U}_1$ and to $\boldsymbol\Phi_2$ (that generates the reachable sub-space), it follows that $\left[ \left( \mathbf{I} - \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \right) \boldsymbol\Phi_3 \right]^* \mathbf{B} = \mathbf{0}$. The same argument gives $\mathbf{U}_4^* \mathbf{B} = \mathbf{0}$, and thus

$$\boldsymbol\Phi^{-1} \mathbf{B} = \begin{bmatrix} \ \ast \ \\ \ \ast \ \\ \ \cdot \ \\ \ \cdot \ \end{bmatrix} \ .$$ 

Looking at the structure of the matrices $\boldsymbol\alpha^{-1}$ and $\boldsymbol\Phi^{-1} \mathbf{B}$, it's easy to show that their matrix multiplication preserves the structure

$$
\begin{bmatrix} 
  \ast  & \ast  & \ast  & \cdot \\
  \cdot & \ast  & \cdot & \cdot \\
  \cdot & \cdot & \ast  & \cdot \\
  \cdot & \cdot & \cdot & \ast  \\
\end{bmatrix} 
\begin{bmatrix} \ \ast \ \\ \ \ast \ \\ \ \cdot \ \\ \ \cdot \ \end{bmatrix} = 
\begin{bmatrix} \ \ast \ \\ \ \ast \ \\ \ \cdot \ \\ \ \cdot \ \end{bmatrix} \ .
$$

**Transformed matrices: matrix $\hat{\mathbf{A}}$.**

The structure of the matrix arises from $\mathbf{A}$-invariance of reachability and controllability sub-spaces and from the properties

$$\begin{aligned}
  \overline{\mathbf{r}}^* \mathbf{A} \mathbf{r} & = 0 \\
            \mathbf{o}^*  \mathbf{A} \overline{\mathbf{o}} & = 0 \ ,
\end{aligned}$$

and recalling that $\mathbf{U}_1: \, r \overline{o}$, $(\mathbf{I}-\boldsymbol\Phi_3 \boldsymbol\Phi_3)^* \boldsymbol\Phi_2: r o \, $, $(\mathbf{I}-\boldsymbol\Phi_2 \boldsymbol\Phi_2)^* \boldsymbol\Phi_3: \, \overline{r} \overline{o}$, $\mathbf{U}_4: \, \overline{r} o$.
Focusing on $\boldsymbol\Phi^{-1} \mathbf{A} \boldsymbol\Phi$ first

$$\begin{aligned}
  \boldsymbol\Phi^{-1} \mathbf{A} \boldsymbol\Phi 
  & = 
\begin{bmatrix}
  \mathbf{U}_1^* \\
  \left[ \left( \mathbf{I} - \boldsymbol\Phi_3 \boldsymbol\Phi_3^* \right) \boldsymbol\Phi_2 \left( \mathbf{I} - \boldsymbol\Phi_2^* \boldsymbol\Phi_3 \boldsymbol\Phi_3^* \boldsymbol\Phi_2 \right)^{-1} \right]^* \\
  \left[ \left( \mathbf{I} - \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \right) \boldsymbol\Phi_3 \left( \mathbf{I} - \boldsymbol\Phi_3^* \boldsymbol\Phi_2 \boldsymbol\Phi_2^* \boldsymbol\Phi_3 \right)^{-1} \right]^* \\
  \mathbf{U}_4^* 
\end{bmatrix} 
\mathbf{A}
\begin{bmatrix} \ \mathbf{U}_1 & \boldsymbol\Phi_2 & \boldsymbol\Phi_3 & \mathbf{U}_4 \ \end{bmatrix} = \\
  & = 
  \begin{bmatrix}
    \ast  & \ast  & \ast  & \ast  \\
    \cdot & \ast  & \cdot & \ast  \\
    \cdot & \cdot & \ast  & \ast  \\
    \cdot & \cdot & \cdot & \ast 
  \end{bmatrix}
\end{aligned}$$

Pre- and post-multiplication by $\boldsymbol\alpha^{-1}$ and $\boldsymbol\alpha$ preserves the structure of $\boldsymbol\Phi^{-1} \mathbf{A} \boldsymbol\Phi$ to have

$$
\hat{\mathbf{A}} = 
\begin{bmatrix} 
   \mathbf{A}_{11} & \mathbf{A}_{12} & \mathbf{A}_{13} & \mathbf{A}_{14} \\ 
   \mathbf{0}      & \mathbf{A}_{22} & \mathbf{0}      & \mathbf{A}_{24} \\ 
   \mathbf{0}      & \mathbf{0}      & \mathbf{A}_{33} & \mathbf{A}_{34} \\ 
   \mathbf{0}      & \mathbf{0}      & \mathbf{0}      & \mathbf{A}_{44} \\ 
\end{bmatrix} \ .
$$

````


<!--
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

```{dropdown}
:open:



```


```{dropdown} Transformation and properties of Gramian matrices
:open:

$$\begin{aligned}
  \mathbf{W}_{C,1} & = \mathbf{U}_C \mathbf{W}_C \mathbf{U}_C^* \\
  \mathbf{W}_{O,1} & = \mathbf{U}^*_C \mathbf{W}_O \mathbf{U}_C
\end{aligned}$$

$$\mathbf{A}_1 = \mathbf{U}_C \mathbf{A} \mathbf{U}_C^*$$



```

-->
