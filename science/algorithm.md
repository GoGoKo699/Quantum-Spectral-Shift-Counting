# Coherent filtering and counting

## Path oracle

Let $`V_\pm=W_\pm W_\pm^\dagger`$ and $`C=A+V_+`$. On the two monotone paths use

~~~math
H_{+,t}=A+tV_+,\qquad
H_{-,t}=A+V_+-(1-t)V_-.
~~~

The second path runs from $`B`$ to $`C`$ and uses the same supplied oracles as the first. Products of the rectangular encodings, using separate signal workspaces, give normalized encodings of $`V_\pm`$. Prepare a dyadic grid of $`M`$ midpoints $`t=(j+1/2)/M`$ in uniform superposition, storing the time label throughout the test.

For either path one can fix a normalization $`\alpha=4`$. Take four equally weighted selector values and an independent uniform dyadic label. On the plus path use one selector for $`A`$, use a fraction $`t`$ of another selector for $`V_+`$, and select a zero block in all other cases. On the minus path dedicate selectors to $`A`$, $`V_+`$ and a fraction $`1-t`$ of $`-V_-`$. Reversible comparison with the dyadic time numerator controls the two fractions. Unpreparing the selector gives the block $`H_t/\alpha`$ with a constant number of input oracle calls. A spare signal qubit and a Pauli X implement the zero block.

## A finite Gaussian circuit

For $`x=H_t/\alpha`$ and $`a=\kappa_j^2\alpha^2/2`$, the amplitude filter is $`e^{-a x^2}`$. It has the even Chebyshev expansion

~~~math
e^{-a x^2}=\sum_{\ell\ge0}(-1)^\ell w_\ell T_{2\ell}(x),
\quad
w_0=e^{-a/2}I_0(a/2),\quad
w_\ell=2e^{-a/2}I_\ell(a/2)\;\;(\ell\ge1).
~~~

Here $`I_\ell`$ is the modified Bessel function. Substitute $`x=\cos\theta`$ and expand $`e^{-(a/2)\cos 2\theta}`$ in Fourier coefficients to obtain the identity. Equivalently, the $`w_\ell`$ are the law of the absolute difference of two independent Poisson variables of mean $`a/4`$. This follows by expanding the characteristic function of their difference, and shows that their sum is one. The moment-generating function of the difference is $`e^{(a/2)(\cosh v-1)}`$. Using $`v=\min(1,D/a)`$ and $`\cosh v-1\le v^2`$ on $`[0,1]`$ bounds the discarded tail by $`2e^{-c\min(D^2/a,D)}`$ for an absolute $`c>0`$. Truncation at

~~~math
D=O\!\left(\kappa_j\sqrt{\log(1/\epsilon)}
                  +\log(1/\epsilon)\right)
~~~

suffices for uniform error $`\epsilon`$ up to a constant allocation of the error budget.

Let $`U`$ encode $`x`$ in a common input/output signal space. The Hermitian unitary $`S=|0\rangle\langle1|\otimes U+|1\rangle\langle0|\otimes U^\dagger`$ has the same compressed block when the new signal qubit is $`|+\rangle`$. If $`\Pi`$ is the augmented signal projection then the walk $`(2\Pi-I)S`$ has powers whose projected blocks are $`T_d(x)`$. On each signal eigenvector this follows by reducing to the two-dimensional span of that vector and its reflection image. The eigenvalues $`\pm1`$ give the endpoint cases by continuity.

Prepare a selector for the truncated weights, apply the signed walk power for each index, then unprepare the selector. Assign the remaining mass to a zero block. For an entirely dyadic selector, round certified lower approximations to the nonnegative weights down to dyadic values whose total shortfall is at most $`\epsilon`$. A uniform bit register and reversible comparison against the resulting cumulative intervals realize those weights exactly. Controlled binary walk powers use $`O(D+1)`$ walk steps in total. The compressed result is a contraction that differs from the ideal Gaussian by $`O(\epsilon)`$ in operator norm. Even real QSVT gives an alternative using bounded polynomial approximation of the same filter.

## Stopping and survival

On a leg of width $`m`$ prepare one half of a maximally entangled factor label and retain the other half. Padding the label dimension to the next power of two $`m_0`$ is convenient. Labels outside the factor width can fail immediately, and the final count conversion uses $`m_0`$ instead of $`m`$. Apply the factor encoding $`W`$ and test its signal coherently. Then apply Gaussian stages with widths $`\kappa_j=2^j`$, flagging the first failed signal test. A fresh clock qubit records each stage boundary. Later stages act only on continuing branches, where the signal registers occupy their known states. The retained factor label and time register make probabilities average over both choices.

Let $`\kappa^2=\sum_j\kappa_j^2`$. For each fixed $`t`$ the ideal filters commute. The probability of success through any Gaussian prefix is consequently the expectation of $`e^{-\kappa_{\rm prefix}^2H_t^2}`$ weighted by $`WW^\dagger/m_0`$. The [rank-density inequality](spectral-averaging.md#one-monotone-path) gives probability at most $`\sqrt\pi/\kappa_{\rm prefix}`$. Finite-grid and finite-filter errors can be bounded uniformly across all prefixes. Choose them to change each probability by at most $`O(\varepsilon/(\kappa m_0))`$ for the working count error $`\varepsilon`$. The [resource proof](resources.md) shows this directly. This preserves the survival bound in order of magnitude.

The cumulative query count through a stage is $`\widetilde O(\kappa_j)`$. Stage $`j>0`$ is entered with probability $`O(1/\kappa_{j-1})`$. The largest and root-mean-square query clocks are therefore

~~~math
T_{\max}=\widetilde O(\kappa),\qquad
T_2^2\le \sum_j \Pr[\text{reach }j]\,
                    \widetilde O(\kappa_j^2)
       =\widetilde O(\kappa).
~~~

The factor-signal and padding tests take constant query cost and belong to the first stopping stages. The success probability of the full circuit before optional padding is $`\sqrt\pi z/(\kappa m_0)`$ up to the allocated probability error.

## Estimating one leg

For an absolute count error of order $`E`$ with $`1\le E\le m`$, add a known early success branch. Use a fair coin between the original experiment and a dummy experiment with success probability of order $`E/(\kappa m_0)`$. The dummy probability can be a nearby known dyadic number. For unit-scale error the constants in the target and dummy probability can be chosen independently. After the coin, success has known positive lower bound and is of order $`(z+E)/(\kappa m_0)`$. Subtract the known dummy contribution after estimation. The stopping clocks retain their orders.

Variable-time amplitude estimation of Chakraborty, Gilyén and Jeffery (Theorem 23) estimates success probability to relative error $`\rho`$ using $`\widetilde O((T_{\max}+T_2/\sqrt{p})/\rho)`$ oracle calls. It applies with deterministic known initial state preparation, since the factor projection is a part of the stopped circuit. A constant-relative preliminary estimate localizes $`z+E`$ up to a constant factor. A second estimate uses relative error of order $`E/(z+E)`$, with a small enough constant for the desired absolute precision. The resulting per-leg cost is

~~~math
\widetilde O\!\left(
\kappa\left[1+\sqrt{\frac{m}{z+E}}\right]
\left[1+\frac{z+E}{E}\right]\right)
=\widetilde O\!\left(\frac{\kappa\sqrt{m(z+E)}}{E}\right).
~~~

The equality uses $`E\le m`$ and $`z\le m`$, with $`m_0\le2m`$. Probability guarantees can be amplified to fixed small failure per pass and combined by a union bound. Fixed worst-case query caps follow from the displayed estimates on the successful preliminary events. Capped runs return a default value and are counted in the allowed failure probability.

Taking $`\kappa=\widetilde O(1/\gamma)`$ gives worst-case additive counting cost $`\widetilde O(r/[\gamma\max(1,\eta)])`$. Allocate a small constant fraction of the total count tolerance to each leg, smooth and subtract. A leg whose known width is below its error allocation can be replaced by the midpoint of its possible range. When the target is below one level, use fixed sub-half total error and round once after subtracting. If the total tolerance reaches the midpoint radius of the known net range, its midpoint already gives a valid output.

## Detecting cancellation

Choose one common $`\kappa`$ with signed smoothing error at most $`1/10`$. Set the dummy count scale to one. Estimate the larger-width leg at constant relative precision for its padded value. This takes $`\widetilde O(\kappa\sqrt r)`$ queries, and gives a conservative lower estimate for its smoothed count. If that lower estimate exceeds $`s+1`$, report a nonzero net change. The other leg is at most $`s`$, so the signed smoothed count has absolute value greater than one.

Otherwise, on the successful preliminary event the larger-width smoothed count is $`O(s+1)`$. The smaller one is at most $`s`$. Estimate each to absolute error at most $`1/10`$ using the per-leg cost with unit dummy scale. Their difference, together with smoothing, is within $`3/10`$ of the exact integer; round and test for zero. The cost is

~~~math
\widetilde O\!\left(\kappa\sqrt{r(s+1)}\right)
=\widetilde O\!\left(\frac{\sqrt{r(s+1)}}{\gamma}\right).
~~~

A hard cap at this order covers both decisions and all successful preliminary estimates. A single positive update gives $`s=0`$, and the same rule distinguishes zero from a positive crossing count. See [the adversary proof](lower-bounds.md) for the matching dependence.
