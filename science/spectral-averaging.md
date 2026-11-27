# Spectral averaging

## One monotone path

Write $`H_t=A_0+tWW^\dagger`$ for $`0\le t\le1`$, and $`A_1=H_1`$. Define $`\xi(x)=n_<(A_0;x)-n_<(A_1;x)`$ and let $`m`$ be the width of $`W`$. By rank interlacing,

~~~math
0\le\xi(x)\le m.
~~~

Monotonicity follows from the min–max principle. For the upper bound, intersect the spectral subspace of $`A_0`$ below $`x`$ with the kernel of $`W^\dagger`$. The dimension decreases by at most $`m`$, and the quadratic form of the update vanishes on the intersection. The min–max principle gives at least that many levels of $`A_1`$ below $`x`$.

For a continuous $`f`$ on a neighborhood of the spectra and an antiderivative $`F`$, the trace derivative and eigenvalue counting give

~~~math
\begin{aligned}
\int_0^1\operatorname{Tr}(W^\dagger f(H_t)W)\,dt
 &=\operatorname{Tr}F(A_1)-\operatorname{Tr}F(A_0)\\
 &=\int_{\mathbb R}f(x)\xi(x)\,dx .
\end{aligned}
~~~

For polynomials the derivative follows from the product rule and cyclicity of trace. Uniformly approximate $`f`$ by polynomials on the spectral interval and integrate to approximate $`F`$. For the second equality, order both spectra with multiplicity. Each paired eigenvalue interval contributes the integral of $`f`$ from its initial to final value. The formula is the finite-matrix Birman–Solomyak identity. It remains valid at degeneracies.

## Gaussian window

For $`f(x)=e^{-\kappa^2 x^2}`$, define the probability and the smoothed count by

~~~math
p_\kappa=\frac1m\int_0^1\operatorname{Tr}(W^\dagger e^{-\kappa^2H_t^2}W)\,dt,
\qquad z_\kappa=\frac{\kappa m}{\sqrt\pi}p_\kappa.
~~~

Rank interlacing gives $`p_\kappa\le\sqrt\pi/\kappa`$ and $`0\le z_\kappa\le m`$. If the endpoints share a gap of radius $`\gamma`$, their shift equals the integer $`k`$ throughout that gap. Outside it, $`|\xi(x)-k|\le m`$. Thus

~~~math
|z_\kappa-k|\le m\,\mathrm{erfc}(\kappa\gamma).
~~~

Taking $`\kappa`$ of order $`\gamma^{-1}\sqrt{\log(2r/\varepsilon)}`$ makes the tail contribution below an absolute count error $`\varepsilon`$ in the regimes of interest. No gap enters the upper bound on the survival probability.

## Signed update

Set $`C=A+V_+=B+V_-`$. Use monotone paths from $`A`$ to $`C`$ and from $`B`$ to $`C`$, and write their densities $`\xi_\pm`$ and smoothed counts $`z_\pm`$. At every energy,

~~~math
\xi_+(x)-\xi_-(x)=n_<(A;x)-n_<(B;x),
\qquad
0\le z_\pm\le r_\pm .
~~~

The same Gaussian on the two paths cancels the trace term at $`C`$ identically. The difference equals a smoothing of the signed endpoint shift even if $`C`$ has a zero eigenvalue. The signed density and $`k`$ lie in $`[-r_-,r_+]`$, so

~~~math
|z_+-z_--k|\le r\,\mathrm{erfc}(\kappa\gamma).
~~~

A single indefinite path need not give the same survival estimate when weighted by the absolute velocity. For example, take $`H_t=\begin{pmatrix}a&b(t-\tfrac12)\\b(t-\tfrac12)&0\end{pmatrix}`$ with fixed $`a,b>0`$. The lower eigenvalue is quadratic near the turning point at zero. The absolute velocity is $`bI`$, and its mass in a window of width $`w`$ about zero is proportional to $`\sqrt w`$ for small $`w`$. The two monotone paths give the linear-in-width bound that the filtering cost uses.
