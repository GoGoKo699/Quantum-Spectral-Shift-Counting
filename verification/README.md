# Verification

From the repository root, install NumPy and run the checks.

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

| Check | What is compared |
| --- | --- |
| Gaussian averaging | Weighted spectral quadrature along 29 monotone paths versus an independent endpoint trace of the error function. The code checks smoothing bias, midpoint discretization and every survival prefix. |
| Signed cancellation | Two Gaussian path integrals through a singular common matrix for each of three endpoint pairs. The signed difference recovers counts $+1,-1,0$. |
| Coherent stopping | Small unitary matrices for the factor and path block encodings. A finite Chebyshev linear combination of walk powers acts at each of three stages. Time, reference and stopping labels stay orthogonal throughout. The surviving amplitudes agree with direct polynomial evaluation and every failure branch contributes to normalization. |
| Fixed block precision | Endpoint inertia under 32 fixed complex perturbations of the supplied signal blocks, at precision one tenth of the certified gap. |
| Adversary | Direct singular values of 120 inclusion matrices and their coordinate restrictions versus the closed-form norm ratios. The small weak-oracle completions have norm differences proportional to the gap. |

The circuit check uses a two-dimensional data space, two factor columns, eight uniformly weighted path midpoints and a degree-40 polynomial at each stage. The finite unitary simulation checks the filters and branch bookkeeping through the input to variable-time amplitude estimation. The asymptotic query bounds follow from the proofs.
