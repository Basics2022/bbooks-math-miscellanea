```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```

(classical-electromagnetism:numerics)=
# Metodi numerici

## Elettrostatica
I problemi dell'elettrostatica sono governate dalle due equazioni di Maxwell per i campi $\mathbf{e}$, $\mathbf{d}$,

$$\begin{cases}
  \nabla \cdot \mathbf{d} = \rho \\ \\
  \nabla \times \mathbf{e} = \mathbf{0 \ ,}
\end{cases}$$

dotate delle opportune condizioni al contorno ed equazioni costitutive. Per un materiale lineare isotropo, ad esempio, $\mathbf{d} = \varepsilon \mathbf{e}$. La condizione di irrotazionalità del campo elettrico, permette di scriverlo come gradiente di un potenziale scalare, $\mathbf{e} = - \nabla v$, e di ottenere l'equazione di Poisson,

$$-\nabla \cdot (\varepsilon \nabla v ) = \rho \ .$$

### Sorgente

$$\mathbf{e}(r) = \frac{q_i}{4 \pi \varepsilon}\frac{\mathbf{r} - \mathbf{r}_i}{|\mathbf{r} - \mathbf{r}_i|^3}$$

$$\mathbf{e}(\mathbf{r}) = - \nabla_{\mathbf{r}} v(\mathbf{r})$$

$$\varepsilon \, v(\mathbf{r}) = \frac{q_i}{4 \pi}\frac{1}{|\mathbf{r} - \mathbf{r}_i|}$$

### Dipolo
Un dipolo è definito come due cariche di intensità uguale e contraria $-q_2 = q_1 = q > 0$, nei punti dello spazio $P_1$, $P_2 = P_1 + \mathbf{l}$, nelle condizioni limite $|\mathbf{l}| \rightarrow 0$, $q \rightarrow \infty$, in modo tale da avere $q |\mathbf{l}|$ finito, $\mathbf{p} = q \mathbf{l}$.

Il potenziale del dipolo è dato dal principio di sovrapposizione delle cause e degli effetti,

$$\begin{aligned}
  \varepsilon \, v(\mathbf{r})
  & = - \frac{q}{4 \pi }\frac{1}{\left|\mathbf{r} - \mathbf{r}_0 + \frac{\mathbf{l}}{2} \right|} 
      + \frac{q}{4 \pi }\frac{1}{\left|\mathbf{r} - \mathbf{r}_0 - \frac{\mathbf{l}}{2} \right|} = \\
  & = \ ... \\
  & = \frac{q}{4 \pi} \left( 
  - \frac{1}{\left|\mathbf{r} - \mathbf{r}_0 \right|} + \frac{\mathbf{r} - \mathbf{r}_0}{\left|\mathbf{r} - \mathbf{r}_0 \right|^3} \cdot \frac{\mathbf{l}}{2}
  + \frac{1}{\left|\mathbf{r} - \mathbf{r}_0 \right|} + \frac{\mathbf{r} - \mathbf{r}_0}{\left|\mathbf{r} - \mathbf{r}_0 \right|^3} \cdot \frac{\mathbf{l}}{2} + o(|\mathbf{l}|) \right) = \\
  & = \ ... \\
  & = \frac{1}{4 \pi}
 \frac{\mathbf{r} - \mathbf{r}_0}{\left|\mathbf{r} - \mathbf{r}_0 \right|^3} \cdot \mathbf{P} \ ,
\end{aligned}$$
avendo definito il vettore momento dipolo $\mathbf{P} = q \mathbf{l}$.

**Polariazazione - Potenziale generato da una distribuzione di dipoli.**

$$d \mathbf{P} = \mathbf{p} \, \Delta V$$

$$\varepsilon v_P(\mathbf{r}) = \int_{\mathbf{r}_0 \in V_0} \frac{1}{4 \pi}
 \frac{\mathbf{r} - \mathbf{r}_0}{\left|\mathbf{r} - \mathbf{r}_0 \right|^3} \cdot \mathbf{p}(\mathbf{r}_0) \, dV_0 $$

$$\begin{aligned}
\partial_i |\mathbf{r}|^2 & = 2 x_i \\
                          & = 2 |\mathbf{r}| \partial_i |\mathbf{r}|
\end{aligned}
\qquad \rightarrow \qquad \partial_i |\mathbf{r}| = \frac{x_i}{|\mathbf{r}|}$$

$$\partial_i |\mathbf{r}|^n = n |\mathbf{r}|^{n-1} \, \partial_i |\mathbf{r}| = n x_i |\mathbf{r}|^{n-2}$$

$$\frac{\mathbf{r}-\mathbf{r}_0}{|\mathbf{r}-\mathbf{r}_0|^3} = \nabla_{\mathbf{r}_0} \frac{1}{|\mathbf{r}-\mathbf{r}_0|}$$

$$\begin{aligned}
\frac{\mathbf{r}- \mathbf{r}_0}{|\mathbf{r}- \mathbf{r}_0|^3} \cdot \mathbf{p}(\mathbf{r}_0) 
 & = \nabla_{\mathbf{r}_0} \frac{1}{|\mathbf{r}-\mathbf{r}_0|} \cdot \mathbf{p}(\mathbf{r}_0) = \\
 & = \nabla_{\mathbf{r}_0} \cdot \left( \frac{1}{|\mathbf{r}-\mathbf{r}_0|} \mathbf{p}(\mathbf{r}_0) \right) - \frac{1}{|\mathbf{r}- \mathbf{r}_0|} \nabla_{\mathbf{r}_0} \cdot \mathbf{p}(\mathbf{r}_0) = \\
\end{aligned}$$

e quindi

$$4 \, \pi \, \varepsilon v_P(\mathbf{r}) = \oint_{\mathbf{r}_0 \in \partial V_0} \frac{\hat{\mathbf{n}}(\mathbf{r}_0) \cdot \mathbf{p}(\mathbf{r}_0)}{|\mathbf{r}-\mathbf{r}_0|} - \oint_{\mathbf{r}_0 \in V_0} \frac{\nabla_{\mathbf{r}_0} \cdot \mathbf{p}(\mathbf{r}_0)}{|\mathbf{r} - \mathbf{r}_0|}$$

I due contributi hanno la forma di sorgenti, essendo termini proporzionali a $\frac{1}{|\mathbf{r}-\mathbf{r}_0|}$.
Il potenziale dovuto alla densità di volume di dipoli equivale alla somma dei due contributi delle cariche di:
- polarizzazione di superficie $\sigma_p =   \hat{\mathbf{n}} \cdot \mathbf{p}$
- polarizzazione di volume     $\rho_p   = - \nabla \cdot \mathbf{p}$

**Oss.** Se la polarizzazione è uniforme nel volume, il contributo della polarizzazione nel volume si annulla e rimane solo il contributo della polarizzazione sul contorno del volume.

**Oss.** Legge di Gauss per il campo elettrico,

$$\begin{aligned}
  \nabla \cdot \mathbf{e} & = \frac{1}{\varepsilon_0} \rho = \\
                          & = \frac{1}{\varepsilon_0} \left( \rho_l + \rho_p \right) = \\
                          & = \frac{1}{\varepsilon_0} \left( \rho_l - \nabla \cdot \mathbf{p} \right) \\
  \nabla \cdot \left( \varepsilon_0 \mathbf{e} + \mathbf{p} \right) & = \rho_l \\
  \nabla \cdot  \mathbf{d} & = \rho_l
\end{aligned}$$



