# Resources and finite accuracy

## Resolution and digital arithmetic

Choose a dyadic sequence $`\kappa_j=2^j`$ with final effective width $`\kappa=(\sum_j\kappa_j^2)^{1/2}`$. An explicit tail bound $`\mathrm{erfc}(x)\le e^{-x^2}`$ for $`x\ge0`$ makes it sufficient to choose

~~~math
\kappa\ \ge\ \frac1\gamma\sqrt{\log(20r/\varepsilon)}
~~~

for a working count error $`\varepsilon`$ with $`0<\varepsilon\le r`$. Doubling the width until the inequality holds costs only a constant factor in the terminal width. For detection and exact rounding take a fixed small $`\varepsilon`$. For coarser counting it is a small fraction of the requested error.

For a leg with velocity bounded by one, Fourier inversion of the Gaussian gives an operator Lipschitz bound. Indeed the Gaussian multiplier is a normalized weighted average of $`e^{ivH_t}`$, with mean absolute $`|v|`$ equal to $`2\kappa'/\sqrt\pi`$ for a prefix of width $`\kappa'`$. Duhamel's formula then yields

~~~math
\left\|e^{-\kappa'^2H_t^2}-e^{-\kappa'^2H_{t'}^2}\right\|
\le \frac{2\kappa'}{\sqrt\pi}|t-t'|.
~~~

Since $`\mathrm{Tr}WW^\dagger/m_0\le1`$, the midpoint quadrature error in the average path probability is $`O(\kappa/M)`$ uniformly across prefixes. A power-of-two grid with $`M\ge C\kappa^2r/\varepsilon`$ for a suitable constant $`C`$ controls this error on the target count scale. The time-label length is only $`O(\log M)`$, and the circuit evaluates the path coherently. For each of $`L`$ Gaussian stages, choose operator error at most $`c\varepsilon/(L\kappa r)`$ with a small absolute $`c`$. Telescoping the contraction products shows that the total error of every prefix amplitude is at most $`c\varepsilon/(\kappa r)`$. The corresponding probability error is at most twice this. The same bounds accommodate dyadic coefficient rounding. Together these errors have a small allocated contribution to the count and retain the survival estimates.

## Gates and workspace

Each path-oracle invocation uses a constant number of controlled primitive encodings and their inverses. Uniform selector registers and reversible comparisons implement its path weights. For a stage of cutoff $`D`$, controlled walk powers use $`O(D+1)`$ oracle calls. The dyadic LCU selector uses $`O(\log(D/\epsilon_{\rm stage}))`$ uniform bits. A consecutive list of $`D+2`$ intervals selects the walk exponent, its parity sign and the zero-block case using $`O((D+1)\mathrm{polylog}((D+1)/\epsilon_{\rm stage}))`$ known gates, with comparable cleanup cost. Its lookup bits can be reused at each stage after the selector is uncomputed on the continuing branch. The classical tables can be precomputed with certified precision, for example by summing two truncated Poisson distributions with tail bounds and then rounding down. This is polynomial in the cutoff, inverse gap and precision bit length, with no need to materialize an $`N`$-dimensional matrix.

The circuit uses the matrix and factor-label registers, the coherent time register, oracle and selector workspaces, and a clock of $`O(L)`$ bits. The variable-time estimator uses controlled calls to these prefixes and their adjoints, known reflections and the associated amplitude-estimation registers. The gate cost from the described construction is bounded by the query count times a polynomial in the register lengths, input-oracle gate costs and logarithms of inverse gap and precision. The estimate of oracle calls applies whether or not the supplied encodings admit efficient elementary-gate realizations. The known arithmetic and control therefore belong in any application comparison, along with the cost of preparing and implementing the oracle itself.

## Approximate input blocks

Suppose the supplied normalized unitaries have fixed compressed blocks $`\widetilde A,\widetilde W_\pm`$ within operator error $`\delta_A,\delta_\pm`$ of the specified inputs. Use the Hermitian part $`A'=(\widetilde A+\widetilde A^\dagger)/2`$, obtained by the reflected path encoding. The two effective paths have common reference $`C'=A'+\widetilde W_+\widetilde W_+^\dagger`$ and second endpoint

~~~math
B'=A'+\widetilde W_+\widetilde W_+^\dagger-
        \widetilde W_-\widetilde W_-^\dagger.
~~~

Each effective factor is contractive, being a block of a unitary. Hence $`\|B'-B\|\le\delta_A+2\delta_++2\delta_-`$. If this sum is at most $`\gamma/2`$, Weyl's inequality gives both effective endpoints a gap of radius at least $`\gamma/2`$ and preserves both endpoint inertias. Running the algorithm with the smaller gap yields the original count. Cancellations at the common reference remain exact and all width bounds apply. This fixed-input accuracy condition depends on the gap alone.

An implementation may separately introduce error during execution. Under a hard cap of $`G`$ elementary operations, per-operation channel error $`O(1/G)`$ with a small constant gives a constant final distribution error by telescoping. The same applies to adaptive choices on stored classical transcripts. Allocate it separately from the algorithm's sampling failure and round only after all deterministic and statistical count errors fit within the specified tolerance. The executable tests check finite circuit blocks and approximate inputs. The variable-time estimation guarantee is used analytically.
