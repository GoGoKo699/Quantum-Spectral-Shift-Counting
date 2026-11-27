# Counting one crossing and resolving cancellation

## One upward crossing

Set the threshold to zero. Take a two-dimensional Hermitian matrix $A$ and a one-column factor $w$.

```math
A=\begin{pmatrix}-1/2&0\\0&1/2\end{pmatrix},\qquad
w=\frac{1}{\sqrt 8}\begin{pmatrix}\sqrt 7\\1\end{pmatrix},\qquad
H_t=A+tww^\dagger .
```

The count of strictly negative eigenvalues of $A$ is one. The trace of $H_t$ is $t$, and its determinant is $-1/4+3t/8$. For $0\le t<2/3$, the negative determinant gives one negative and one positive eigenvalue. The determinant vanishes at $t=2/3$, where the second eigenvalue is $2/3$. For $2/3<t\le 1$, positive trace and determinant put both eigenvalues above zero.

At the final matrix $B=H_1$, the eigenvalues are $(1-1/\sqrt 2)/2$ and $(1+1/\sqrt 2)/2$. The common endpoint gap is $\gamma=(1-1/\sqrt 2)/2$, and the net shift $k=n_-(A)-n_-(B)$ equals one. The matrices along the path vary in eigenvectors as well as eigenvalues since $A$ and $ww^\dagger$ have a nonzero commutator.

| Matrix point | Count below zero |
| --- | --- |
| Initial $A$ | 1 |
| Crossing at $t=2/3$ | 0 |
| Final $B$ | 0 |

## Turn the crossing into a probability

Prepare the path parameter uniformly and apply $e^{-\kappa^2 H_t^2/2}$ as the success block of a quantum operation. In this rank-one example the success probability, averaged on ideal continuous $t$, is

```math
p=\int_0^1 w^\dagger e^{-\kappa^2 H_t^2}w\,dt.
```

The square in the success probability explains the factor of two between the exponents of the operator and the probability. Spectral averaging gives $\kappa p/\sqrt{\pi}$ as the normalized Gaussian average of the two endpoint count difference. On $(-\gamma,\gamma)$ the difference is one, so only the Gaussian tail can change the average.

For stages with inverse widths $1,2,4,8,16$, the combined inverse width is $\kappa=\sqrt{341}$. Midpoint integration with 8,192 intervals gives the ideal-filter probabilities of passing all stages through the indicated inverse width.

| Last inverse width | Prefix survival probability |
| --- | --- |
| 1 | 0.83011326 |
| 2 | 0.53495390 |
| 4 | 0.32052965 |
| 8 | 0.18684676 |
| 16 | 0.09597747 |

Rescaling the last probability gives $0.99993447$. The smoothing error bound is $\mathrm{erfc}(\kappa\gamma)\approx 0.00013105$, and estimation of this probability to sufficient additional accuracy recovers the integer one by rounding. The table checks the ideal filter and integration. The algorithm implements a finite grid, polynomial approximations, and a coherent estimator. [Spectral averaging](../science/spectral-averaging.md) · [Algorithm](../science/algorithm.md)

## A signed update with a gapless reference

Take two orthonormal basis states and their projectors $P_0=\lvert 0\rangle\langle 0\rvert$ and $P_1=\lvert 1\rangle\langle 1\rvert$. Define

```math
C=\tfrac14\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
A=C-\tfrac12 P_0,\qquad B=C-\tfrac12 P_1 .
```

The signed update is $B-A=(P_0-P_1)/2$. Both endpoints have eigenvalues $\pm\sqrt{2}/4$, so the net count at zero is unchanged. The reference $C$ has eigenvalues 0 and $1/2$. The two positive legs are $A\to C$ and $B\to C$. Swapping the two basis states carries one leg to the other, so they have identical Gaussian-weighted counts. Their difference vanishes even though the reference has an eigenvalue at the threshold.

The two-leg identity in the general signed proof gives the same cancellation of the reference trace for paths with different spectra, and it uses the common gap at $A$ and $B$. [Spectral averaging](../science/spectral-averaging.md) · [Algorithm](../science/algorithm.md)
