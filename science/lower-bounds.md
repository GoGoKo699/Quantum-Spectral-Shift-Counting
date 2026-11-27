# Query lower bounds

The lower bound uses diagonal matrices for which each oracle call gives only a weak indication of one input bit. The algorithm may query in superposition and use the adjoint and controlled forms of all supplied encodings.

## An instance with prescribed sign ranks

First make the larger sign rank positive, of size $`m=\max(r_+,r_-)`$. For a hidden bit string $`x\in\{0,1\}^m`$, use

~~~math
A_i=-\frac12+(2x_i-1)\gamma,\qquad (V_+)_i=\frac12,\qquad
B_i=(2x_i-1)\gamma
~~~

on its $`m`$ coordinates. Each marked coordinate contributes one upward crossing. Supply fixed encodings of the update factors. On $`s`$ separate minority coordinates let $`u`$ coordinates have $`A_i=1/4`$ and $`(V_-)_i=1/2`$, making $`u`$ downward crossings. The other $`s-u`$ minority coordinates can have $`A_i=3/4`$ and $`(V_-)_i=1/4`$. Their updates are nonzero, keeping the prescribed sign rank, and they stay above zero. For a larger negative rank, reflect the construction through zero and swap the factors. The net count is therefore $`|x|-u`$ up to overall sign.

The endpoints satisfy the stated gap for $`\gamma\le1/4`$. Extra coordinates with fixed nonzero energy and no update leave the count unchanged. The spectral factors have orthogonal ranges on this family and the oracle completions of the fixed factors carry no information about $`x`$.

## A weak normalized oracle

For a diagonal entry $`a`$, choose the real reflection

~~~math
U(a)=
\begin{pmatrix}
a & \sqrt{1-a^2}\\
\sqrt{1-a^2} & -a
\end{pmatrix}.
~~~

The data register selects the reflection for its coordinate and the first signal block is the input diagonal matrix. On the bit-dependent entries $`|a|\le3/4`$, the derivative of $`U(a)`$ is bounded in norm by an absolute constant. Hence the two oracle actions at one coordinate differ by $`O(\gamma)`$ in operator norm. This bound also holds for controlled operations and inverses. A lower bound for these valid completions applies to any algorithm required to handle all encodings in the access model.

## Neighboring Hamming layers

Connect every string of weight $`u`$ to its supersets of weight $`u+d`$. The rectangular incidence matrix $`\Gamma`$ has row and column degrees $`\binom{m-u}{d}`$ and $`\binom{u+d}{d}`$. Its spectral norm is the square root of their product, attained by uniform singular vectors. Restrict to pairs that differ at coordinate $`i`$ to obtain $`\Gamma_i`$. Its nonzero rows and columns again have constant degrees, with the first degree multiplied by $`d/(m-u)`$ and the second by $`d/(u+d)`$. Thus

~~~math
\frac{\|\Gamma_i\|}{\|\Gamma\|}
=\frac{d}{\sqrt{(m-u)(u+d)}}.
~~~

For completeness, the positive adversary progress is the $`\Gamma`$-weighted sum of cross-input state overlaps, with weights given by its top left and right singular vectors. It begins at $`\|\Gamma\|`$ for a common initial state. Amplification to, for example, error $`1/16`$ uses a constant number of repetitions. A final classical decision with that error gives cross-input overlaps bounded in magnitude by a constant less than one, by Cauchy–Schwarz on the two outcome subspaces. The progress consequently changes by $`\Omega(\|\Gamma\|)`$.

Known gates preserve every overlap. For an oracle call decompose the query register by coordinate. Only entries of $`\Gamma_i`$ contribute on differing inputs in that block. They all have orientation $`x_i=0,y_i=1`$, so the matrix of changes is the tensor product of $`\Gamma_i`$ and $`I-U(a_0)^\dagger U(a_1)`$, or its controlled variant. Its norm is at most $`O(\gamma)\|\Gamma_i\|`$. Applying Cauchy–Schwarz across the orthogonal query blocks bounds progress change per call by $`O(\gamma)\max_i\|\Gamma_i\|`$. Deferred measurements give the same argument for adaptive algorithms with a worst-case query cap. The resulting bound is

~~~math
\Omega\!\left(\frac{\sqrt{(m-u)(u+d)}}{\gamma d}\right).
~~~

## From the adversary to the two tasks

For detection choose $`u=\lfloor s/2\rfloor`$ and $`d=1`$. The two endpoint shifts are zero and one up to overall sign. Since $`m\ge r/2`$ and $`u\le m/2`$, this gives $`\Omega(\sqrt{r(s+1)}/\gamma)`$, including $`s=0`$.

For additive estimation compare weights near $`m/2`$ separated by the smallest integer $`d>2\eta`$. An estimate correct on either instance distinguishes the layers because their permitted output intervals are disjoint. A fixed minority update merely adds a common shift and can have zero crossings. In the nontrivial range where $`d`$ is at most a small constant fraction of $`m`$, the bound becomes $`\Omega(r/[\gamma\max(1,\eta)])`$. This covers fixed subunit estimation and exact counting via the neighboring layers.
