# Scientific account

A local update can change the occupied part of a spectrum by only a few levels. The computational question is whether that small integer change can be read without first finding the occupation of either endpoint. This project counts the change by weighting each energy along the interpolation with the operator that generates the update.

| Start here | What it establishes |
| --- | --- |
| [Model and results](model.md) | Oracle access, endpoint gap and the full rank-dependent statements |
| [Spectral averaging](spectral-averaging.md) | Rank-bounded density, Gaussian smoothing and cancellation at a gapless reference |
| [Algorithm](algorithm.md) | Explicit Gaussian circuits, coherent stopping, additive count and signed detection |
| [Lower bounds](lower-bounds.md) | Weak marked-item oracle and the sign-rank dependence |
| [Resources](resources.md) | Known operations, workspace, normalization and error budgets |
| [Related work](../references/related-work.md) | Prior spectral shift, inertia, spectral estimation and quantum primitives |

The key distinction in the proofs is between the magnitude of a single monotone spectral shift and the difference of two such shifts. Each monotone path has nonnegative weight with density bounded by its factor width. Their difference can vanish even when both weights are substantial. The algorithm estimates each weight to the precision the comparison requires. The lower bound shows that resolving cancellation near a balanced count can require more queries.

The [worked examples](../learning/WORKED_EXAMPLE.md) connect the scalar count, a noncommuting update and the two-path construction. The [verification guide](../verification/README.md) documents numerical and circuit checks.
