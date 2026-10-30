(differential-geometry:surfaces)=
# Surfaces

$$\vec{r}(q^1, q^2)$$

$$d \vec{r} =
  \frac{\partial \vec{r}}{\partial q^1} \, d q^1 + \frac{\partial \vec{r}}{\partial q^2} \, d q^2 =
  \vec{b}_1 \, d q^1 + \vec{b}_2 \, d q^2
$$

A third vector $\vec{b}_3 := \hat{n}$ can be defined so that $|\hat{n}| = 1$ and $\hat{n} \cdot \vec{b}_{i} = 0$, $i=1:2$. For $i=1:2$, $k=1:2$

$$\frac{\partial \vec{b}_i}{\partial q^j} = \Gamma_{ij}^k \vec{b}_k = \Gamma_{ij}^1 \vec{b}_1 + \Gamma_{ij}^2 \vec{b}_2 + \Gamma_{ij}^3 \vec{b}_3$$

so that

$$\Gamma_{ij}^{k} = \vec{b}^k \cdot \frac{\partial \vec{b}_i}{\partial q^j}$$

**Normal vector.** 

$$\vec{n}(q^1, q^2) = \frac{\partial \vec{r}}{\partial q^1}(q^1, q^2) \times \frac{\partial \vec{r}}{\partial q^2}(q^1, q^2) = \vec{b}_1(q^1, q^2) \times \vec{b}_2(q^1, q^2)$$

**Tangent plane.** 

$$(\vec{r} - \vec{r}(q^1, q^2)) \cdot \vec{n}(q^1, q^2) = 0$$

**Length of elementary segment.**

$$\begin{aligned}
|d \vec{r}|^2 
  & = d \vec{r} \cdot d \vec{r} = \\
  & = \left( \vec{b}_1 \, d q^1 + \vec{b}_2 \, d q^2 \right) \cdot \left( \vec{b}_1 \, d q^1 + \vec{b}_2 \, d q^2 \right) = \\
  & = g_{11} \, dq^1 \, dq^1 + g_{12} \, dq^1 \, dq^2 + g_{21} \, dq^2 \, dq^1 + g_{22} \, dq^2 \, d q^2 = g_{ij} \, dq^i \, dq^j 
\end{aligned}$$

**Second order approximation.**

$$\begin{aligned}
  \vec{r}(q^1 + d q^1, q^2 + d q^2) 
  & = \vec{r}(q_1, q_2) + \frac{\partial \vec{r}}{\partial q^i} \, dq^i + \frac{\partial^2 \vec{r}}{\partial q^i \partial q^j} \, dq^i \, dq^j = \\
  & = \vec{r}(q_1, q_2) + \vec{b}_{i} \, dq^i + \vec{b}_k \Gamma^{k}_{ij} \, dq^i \, dq^j +  \hat{n} \, \Gamma^{3}_{ij} \, dq^i \, dq^j 
\end{aligned}$$

so that

$$\begin{aligned}
\left[ \vec{r}(q^1 + d q^1, q^2 + d q^2) - \vec{r}(q^1, q^2) \right] \cdot \hat{n} 
 & = \Gamma^3_{ij} \, d q^i \, dq^j = \\
 & = \hat{n} \cdot \frac{\partial^2 \vec{r}}{\partial q^i \partial q^j} \, d q^i \, dq^j = \\
 & = \hat{n} \cdot \frac{\partial^2 \vec{r}}{\partial q^i \partial q^j} \, \vec{b}^i \cdot \vec{b}_k d q^k \, \vec{b}^j \cdot \vec{b}_l dq^l = \\
 & = \underbrace{d q^k \vec{b}_k}_{d \vec{r}} \cdot \left[ \hat{n} \cdot \frac{\partial^2 \vec{r}}{\partial q^i \partial q^j}  \vec{b}^i \otimes \vec{b}^j \right] \cdot \underbrace{d q^l \vec{b}_l}_{d\vec{r}}
\end{aligned}$$

**Curvature tensor.**

...
