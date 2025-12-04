(tensor:algebra:invariants)=
# Tensor Invariants

## Rank-$2$ tensors

* Characteristic polynomial (*this definition needs that determinant exists*)

   $$0 = \text{det}\left( \mathbf{A} - s \mathbf{I} \right) \ .$$

   *Using a unit normal basis* (**todo** generalization required?)

   $$\begin{aligned}
   0 
   & = \left|\begin{matrix}
     A_{11} - s & A_{12}     & A_{13}     \\
     A_{21}     & A_{22} - s & A_{23}     \\
     A_{31}     & A_{32}     & A_{33} - s
   \end{matrix}\right|
   = - s^3 + s^2 I_1 - s I_2 + I_3 \ ,
   \end{aligned}$$

   with

   $$\begin{aligned}
     I_1 & = \text{tr}(\mathbf{A}) = A_{11} + A_{22} + A_{33} \\
     I_2 & = \dfrac{1}{2} \left( \text{tr}(\mathbf{A})^2 - \text{tr}(\mathbf{A}^2) \right) = \dots = A_{11} A_{22} + A_{11} A_{33} + A_{22} A_{33} - A_{31} A_{13} - A_{12} A_{21} - A_{32} A_{23} \\
     I_3 & = \text{det}(\mathbf{A}) = \dots \\
   \end{aligned}$$

   The coefficients of the characteristic polynomial are invariant under transformation of coordinates (**todo** here only referring to Cartesian basis, and thus orthogonal transformations?)

* **Trace**...


* Determinant...

