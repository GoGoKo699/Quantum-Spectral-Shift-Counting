# Model and results

## Input and output

The threshold is centered at zero. Counting below another known threshold reduces to this convention by shifting and rescaling the input and the gap. Let $`A`$ be an $`N\times N`$ Hermitian contraction. The perturbed endpoint is

~~~math
B=A+V_+-V_-,
\qquad V_\pm=W_\pm W_\pm^\dagger,
\qquad W_\pm:\mathbb C^{r_\pm}\longrightarrow\mathbb C^N,
\qquad \|W_\pm\|\le 1.
~~~

For spectral positive and negative parts, choose full-column-rank factors so that $`r_\pm`$ are the sign ranks. The upper bounds also apply to a supplied decomposition with overlapping ranges, in terms of its supplied factor widths. Set $`r=r_++r_-\ge1`$ and $`s=\min(r_+,r_-)`$. A zero-width factor is omitted.

Both endpoint spectra avoid $`(-\gamma,\gamma)`$ for a known $`0<\gamma\le1/4`$. Let $`n_<(H;x)=\mathrm{rank}{\bf1}_{(-\infty,x)}(H)`$. The output of the estimation task is a classical number $`\widehat k`$ satisfying

~~~math
k=n_<(A;0)-n_<(B;0),\qquad
\Pr[|\widehat k-k|\le\eta]\ge2/3.
~~~

For detection the required output is the bit $`{\bf1}_{k\ne0}`$ with success probability at least $`2/3`$. The convention gives positive $`k`$ for net upward crossings. Each continuous eigenvalue branch of a positive update is nondecreasing. In that case the net count is the number of levels that pass through zero.

## Oracle access

A normalized block encoding of $`M`$ is a unitary $`U_M`$ with known input and output signal embeddings $`P_{\mathrm{in}}`$ and $`P_{\mathrm{out}}`$ such that the compressed block $`P_{\mathrm{out}}^\dagger U_M P_{\mathrm{in}}`$ equals $`M`$. The algorithm is supplied controlled block encodings of $`A`$ and the two factors, their inverses, and their signal register conventions. It can prepare and reflect about the corresponding computational registers, implement known arithmetic and use clean ancillas. One invocation of a supplied unitary, its controlled form or its inverse is one query. A controlled invocation can carry a reversibly computed condition. The block encoding of the other endpoint and of either interpolating matrix is constructed from these calls.

There is no state-overlap promise. The procedure can begin in a known product state. Finite-dimensional Hilbert spaces may be embedded in qubit registers using zero padding, with the stipulated signal spaces restricting the counted inputs. In the algorithm, an implementation may pad the factor labels only. A padding convention used for the matrix space may add constant spectral zeros, which cancel between the endpoints and carry zero spectral weight; the gap applies to the physical block.

## Main results

**Theorem 1 (net-change detection).** In the given model there is an algorithm using

~~~math
\widetilde O\!\left(\frac{\sqrt{r(s+1)}}{\gamma}\right)
~~~

queries. For each sign-rank balance with $`r\ge1`$, there are diagonal instances and normalized oracle completions that require $`\Omega(\sqrt{r(s+1)}/\gamma)`$ queries. Arbitrarily many fixed bulk coordinates may be added to those instances.

**Theorem 2 (additive and exact counting).** For $`\eta>0`$, an estimator uses $`\widetilde O(r/[\gamma\max(1,\eta)])`$ queries in the nontrivial accuracy range. If $`\eta<1`$, the algorithm can instead output the exact integer with the same worst-case order. If $`r`$ is large enough and $`1\le \max(1,\eta)\le c r`$ for an absolute constant $`c>0`$, the corresponding lower bound is $`\Omega(r/[\gamma\max(1,\eta)])`$. The lower bound holds already for positive updates and also on suitable instances for a prescribed sign-rank split. A known range for the count makes the sufficiently coarse cases trivial.

The notation $`\widetilde O`$ suppresses logarithmic factors in the relevant rank, inverse gap and inverse failure probability. There are no precision logs in a demand smaller than the fixed error used before exact rounding. Input implementation resources enter separately in the [resource account](resources.md). The upper proofs use [spectral averaging](spectral-averaging.md) and [variable-time estimation](algorithm.md). See [lower bounds](lower-bounds.md) for the adversary model.
