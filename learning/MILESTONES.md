# Learning milestones

The first twelve milestones develop the spectral and query models. The remaining eighteen follow the constructive proof, the sign-balance lower bound, and the resources needed to implement the method. The [textbook bridge](NIELSEN_CHUANG_BRIDGE.md) maps the selected edition to the project, and the [worked example](WORKED_EXAMPLE.md) checks the signs and the Gaussian normalization.

| Phase | Milestones | Connection established |
| --- | --- | --- |
| Background and preliminaries | [M01](#m01-count-eigenvalues-below-a-threshold)–[M06](#m06-interpret-the-endpoint-gap) | Energy counts, sign structure, and endpoint promises |
| Background and preliminaries | [M07](#m07-read-a-normalized-block-encoding)–[M12](#m12-assemble-the-operational-task) | Coherent access, success estimation, and the query model |
| Narrative and innovation | [M13](#m13-differentiate-a-spectral-trace)–[M16](#m16-construct-a-coherent-sampled-path) | Spectral averaging turns the count into a probability |
| Narrative and innovation | [M17](#m17-stack-gaussian-contractions)–[M21](#m21-detect-a-positive-shift) | Early stopping yields a positive-shift detector |
| Narrative and innovation | [M22](#m22-form-two-monotone-legs)–[M27](#m27-match-the-sign-balance-law) | Signed cancellation and a matching lower bound |
| Narrative and innovation | [M28](#m28-allocate-implementation-error)–[M30](#m30-connect-the-complete-result) | Implementation scope and the complete argument |

## Phase I · Background and preliminaries

### M01 Count eigenvalues below a threshold

**Central question.** What quantity changes when a Hermitian matrix is perturbed?

**Understanding target.** Define the strict endpoint count and include each eigenvalue with its multiplicity. Evaluate the count when an eigenvalue equals the threshold.

**Prerequisites.** Start here.

**Conceptual connection.** Use a count difference to describe how many units of occupation move across an energy boundary.

**Sources.** [Model](../science/model.md) · [Worked example](WORKED_EXAMPLE.md) · [Nielsen–Chuang §§2.1.5–2.1.6](NIELSEN_CHUANG_BRIDGE.md)

### M02 Read functions of Hermitian matrices

**Central question.** How does a scalar function act on a matrix?

**Understanding target.** Use spectral decomposition to replace each eigenvalue by its function value while retaining its spectral projector. Interpret the trace as a sum over those function values.

**Prerequisites.** [M01](#m01-count-eigenvalues-below-a-threshold).

**Conceptual connection.** A step function represents the exact count and a smooth function approximates it near a gapped endpoint.

**Sources.** [Spectral averaging](../science/spectral-averaging.md) · [Nielsen–Chuang §2.1.8](NIELSEN_CHUANG_BRIDGE.md)

### M03 Decompose a signed update

**Central question.** How can one perturbation move levels in both directions?

**Understanding target.** Express a Hermitian update as a positive factor product minus a second positive factor product. Identify the two sign ranks and their sum.

**Prerequisites.** [M01](#m01-count-eigenvalues-below-a-threshold), [M02](#m02-read-functions-of-hermitian-matrices).

**Conceptual connection.** The sign decomposition supplies the two matrix paths and the rank parameter in their resource law.

**Sources.** [Model](../science/model.md) · [Nielsen–Chuang §§2.1.6, 2.1.10](NIELSEN_CHUANG_BRIDGE.md)

### M04 Follow a positive path

**Central question.** What does adding a positive matrix do to ordered energy levels?

**Understanding target.** Apply the minimum–maximum principle to see that a positive perturbation moves each ordered eigenvalue upward or leaves it fixed.

**Prerequisites.** [M02](#m02-read-functions-of-hermitian-matrices), [M03](#m03-decompose-a-signed-update).

**Conceptual connection.** Monotonicity gives a nonnegative count difference at every energy on a positive leg.

**Sources.** [Spectral averaging](../science/spectral-averaging.md) · [Worked example](WORKED_EXAMPLE.md)

### M05 Use finite-rank interlacing

**Central question.** How many levels can one positive update move across a single threshold?

**Understanding target.** Use rank interlacing to bound the difference of threshold counts by the update rank, including arbitrary finite multiplicities.

**Prerequisites.** [M03](#m03-decompose-a-signed-update), [M04](#m04-follow-a-positive-path).

**Conceptual connection.** The same bound will constrain how much narrowly filtered spectral weight the path can contain.

**Sources.** [Spectral averaging](../science/spectral-averaging.md)

### M06 Interpret the endpoint gap

**Central question.** Where does a common spectral gap affect the count?

**Understanding target.** Recognize that the two endpoint counting functions and their difference are constant throughout the common gap, even when a path eigenvalue crosses inside it.

**Prerequisites.** [M01](#m01-count-eigenvalues-below-a-threshold), [M04](#m04-follow-a-positive-path), [M05](#m05-use-finite-rank-interlacing).

**Conceptual connection.** The algorithm recovers the threshold count from the full interval on which the difference is constant.

**Sources.** [Model](../science/model.md) · [Worked example](WORKED_EXAMPLE.md)

### M07 Read a normalized block encoding

**Central question.** What does one coherent matrix query supply?

**Understanding target.** Identify a matrix as a compression of a unitary between known signal subspaces. Track the normalization of a product, including the product of a rectangular factor with its adjoint.

**Prerequisites.** [M02](#m02-read-functions-of-hermitian-matrices), [M03](#m03-decompose-a-signed-update).

**Conceptual connection.** The oracle interface fixes both the matrix accessible in each branch and the unit of query cost.

**Sources.** [Model](../science/model.md) · [Algorithm](../science/algorithm.md) · [Nielsen–Chuang §§2.1.6, 4.3](NIELSEN_CHUANG_BRIDGE.md)

### M08 Track success by squared norm

**Central question.** What probability does a signal projection produce?

**Understanding target.** Apply the projective measurement rule to the successful signal block. Follow an unnormalized continuing vector through several applications.

**Prerequisites.** [M02](#m02-read-functions-of-hermitian-matrices), [M07](#m07-read-a-normalized-block-encoding).

**Conceptual connection.** A sequence of filters multiplies their amplitudes, then the final squared norm gives the accumulated survival probability.

**Sources.** [Algorithm](../science/algorithm.md) · [Nielsen–Chuang §§2.2.3, 2.2.5, 4.4](NIELSEN_CHUANG_BRIDGE.md)

### M09 Average over factor labels

**Central question.** How can a quantum state represent an average over all update directions?

**Understanding target.** Use two correlated uniform label registers and apply the factor to one register. Show how orthogonality of the untouched labels yields a normalized trace over the factor columns.

**Prerequisites.** [M03](#m03-decompose-a-signed-update), [M07](#m07-read-a-normalized-block-encoding), [M08](#m08-track-success-by-squared-norm).

**Conceptual connection.** The resulting state samples perturbation-weighted energy through its success flags.

**Sources.** [Algorithm](../science/algorithm.md) · [Nielsen–Chuang §§2.1.7, 2.5](NIELSEN_CHUANG_BRIDGE.md)

### M10 Count from a coherent success flag

**Central question.** How does amplitude estimation read a probability?

**Understanding target.** Connect the rotation in the success–failure plane to a success probability and use phase estimation to recover it. Relate uncertainty in the probability to uncertainty in a rescaled count.

**Prerequisites.** [M08](#m08-track-success-by-squared-norm), [M09](#m09-average-over-factor-labels).

**Conceptual connection.** The same amplitude-estimation idea works when the labels index a matrix path and survival defines success.

**Sources.** [Textbook bridge](NIELSEN_CHUANG_BRIDGE.md) · [Algorithm](../science/algorithm.md) · [Nielsen–Chuang §§5.2–5.2.1, 6.1.3–6.1.4, 6.3](NIELSEN_CHUANG_BRIDGE.md)

### M11 Recognize a query lower bound

**Central question.** What limits the information from related black-box inputs?

**Understanding target.** Track how small changes in neighboring input oracles restrict progress per query. Relate distinguishing promises on Hamming weights to approximate counting.

**Prerequisites.** [M07](#m07-read-a-normalized-block-encoding), [M10](#m10-count-from-a-coherent-success-flag).

**Conceptual connection.** Weak encodings can hide whether each update coordinate crosses the threshold.

**Sources.** [Lower bounds](../science/lower-bounds.md) · [Nielsen–Chuang §§6.6–6.7](NIELSEN_CHUANG_BRIDGE.md)

### M12 Assemble the operational task

**Central question.** What input, promise, output, and cost define the spectral-shift problem?

**Understanding target.** State the given block encodings and common endpoint gap. Distinguish detection of a change, additive estimation of the signed count, and exact recovery by rounding.

**Prerequisites.** [M01](#m01-count-eigenvalues-below-a-threshold), [M03](#m03-decompose-a-signed-update), [M06](#m06-interpret-the-endpoint-gap), [M07](#m07-read-a-normalized-block-encoding), [M10](#m10-count-from-a-coherent-success-flag), [M11](#m11-recognize-a-query-lower-bound).

**Conceptual connection.** Fix the model in which one algorithm and one lower bound can be compared.

**Sources.** [Model](../science/model.md) · [Resource accounting](../science/resources.md)

## Phase II · Narrative and innovation

### M13 Differentiate a spectral trace

**Central question.** How does a positive matrix direction enter the derivative of a spectral sum?

**Understanding target.** Apply the trace derivative identity along a straight path and keep the perturbation factor inside the trace. Recognize why changing eigenvectors along the path preserves the identity.

**Prerequisites.** [M02](#m02-read-functions-of-hermitian-matrices), [M04](#m04-follow-a-positive-path), [M12](#m12-assemble-the-operational-task).

**Conceptual connection.** Integrating the derivative moves between endpoint traces and a positive weighted energy measure.

**Sources.** [Spectral averaging](../science/spectral-averaging.md) · [Worked example](WORKED_EXAMPLE.md)

### M14 Identify the bounded spectral density

**Central question.** What density does the positive path sample after integrating the derivative?

**Understanding target.** Identify the spectral-shift density as the endpoint count difference and use finite-rank interlacing to bound its value at any energy.

**Prerequisites.** [M05](#m05-use-finite-rank-interlacing), [M09](#m09-average-over-factor-labels), [M13](#m13-differentiate-a-spectral-trace).

**Conceptual connection.** This is the shared bound for the smoothed count and all earlier filter stages.

**Sources.** [Spectral averaging](../science/spectral-averaging.md)

### M15 Recover a plateau through smoothing

**Central question.** How does a Gaussian average recover the integer shift?

**Understanding target.** Integrate the density against a normalized centered Gaussian. Bound the bias using its mass outside the interval where the endpoint count difference is constant.

**Prerequisites.** [M06](#m06-interpret-the-endpoint-gap), [M13](#m13-differentiate-a-spectral-trace), [M14](#m14-identify-the-bounded-spectral-density).

**Conceptual connection.** The tail estimate sets the final filter scale from the endpoint gap and the requested count accuracy.

**Sources.** [Spectral averaging](../science/spectral-averaging.md) · [Worked example](WORKED_EXAMPLE.md)

### M16 Construct a coherent sampled path

**Central question.** How can one query act on the whole interpolation grid?

**Understanding target.** Use a uniform time register and controlled coefficients to encode the matrix at each grid point. Follow its contribution to the averaged success probability.

**Prerequisites.** [M07](#m07-read-a-normalized-block-encoding), [M09](#m09-average-over-factor-labels), [M13](#m13-differentiate-a-spectral-trace).

**Conceptual connection.** Path discretization keeps the oracle calls coherent while approximating the integral to the required count accuracy.

**Sources.** [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md) · [Nielsen–Chuang §4.3](NIELSEN_CHUANG_BRIDGE.md)

### M17 Stack Gaussian contractions

**Central question.** Why split a narrow filter into several stages?

**Understanding target.** Use dyadically growing inverse widths. Combine the continuing amplitudes and compute the net inverse width from the sum of squared stage widths.

**Prerequisites.** [M08](#m08-track-success-by-squared-norm), [M15](#m15-recover-a-plateau-through-smoothing), [M16](#m16-construct-a-coherent-sampled-path).

**Conceptual connection.** Earlier broad stages can reject inputs while preserving the final Gaussian response on the continuing branch.

**Sources.** [Algorithm](../science/algorithm.md) · [Worked example](WORKED_EXAMPLE.md)

### M18 Make each stopping branch reversible

**Central question.** How can a quantum estimator reuse a circuit with different stopping times?

**Understanding target.** Store the first failure stage in a coherent flag and condition subsequent stages on continued success. Interpret the factor call as an initial possible failure.

**Prerequisites.** [M07](#m07-read-a-normalized-block-encoding), [M08](#m08-track-success-by-squared-norm), [M16](#m16-construct-a-coherent-sampled-path), [M17](#m17-stack-gaussian-contractions).

**Conceptual connection.** A reversible branch record enables reflections and inverse operations on the same multi-stage computation.

**Sources.** [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md) · [Nielsen–Chuang §§4.3–4.4](NIELSEN_CHUANG_BRIDGE.md)

### M19 Bound maximum and RMS cost

**Central question.** Why are the longest branch and the root-mean-square branch cheaper in different ways?

**Understanding target.** Use the rank-density bound at each prefix and the growing per-stage query cost. Obtain inverse-width scaling for the longest branch and its square root, up to logarithms, for the RMS cost.

**Prerequisites.** [M14](#m14-identify-the-bounded-spectral-density), [M17](#m17-stack-gaussian-contractions), [M18](#m18-make-each-stopping-branch-reversible).

**Conceptual connection.** The decreasing survival probability offsets the rising cost of narrow filters.

**Sources.** [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md)

### M20 Estimate a rare survival probability

**Central question.** How can relative estimation work even when the true signal is zero?

**Understanding target.** Add a calibrated early success contribution, obtain a coarse probability scale, and refine the relative estimate to the required absolute error of the count.

**Prerequisites.** [M10](#m10-count-from-a-coherent-success-flag), [M15](#m15-recover-a-plateau-through-smoothing), [M18](#m18-make-each-stopping-branch-reversible), [M19](#m19-bound-maximum-and-rms-cost).

**Conceptual connection.** The scale-dependent query cost makes a coarse decision inexpensive when the final count is already large enough.

**Sources.** [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md) · [Nielsen–Chuang §6.3](NIELSEN_CHUANG_BRIDGE.md)

### M21 Detect a positive shift

**Central question.** How can one test for at least one upward crossing?

**Understanding target.** Use the tail bound and a constant-accuracy count test near zero. Derive the square-root rank query dependence and identify the additional inverse-gap factor.

**Prerequisites.** [M15](#m15-recover-a-plateau-through-smoothing), [M19](#m19-bound-maximum-and-rms-cost), [M20](#m20-estimate-a-rare-survival-probability).

**Conceptual connection.** The positive case sets the endpoint of the signed detection law when the smaller sign rank is zero.

**Sources.** [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md)

### M22 Form two monotone legs

**Central question.** How does one apply positive spectral averaging to a signed perturbation?

**Understanding target.** Reach one common reference from both endpoints by adding the corresponding positive factors. Subtract the two smoothed leg counts at the same inverse width.

**Prerequisites.** [M03](#m03-decompose-a-signed-update), [M13](#m13-differentiate-a-spectral-trace), [M15](#m15-recover-a-plateau-through-smoothing), [M20](#m20-estimate-a-rare-survival-probability).

**Conceptual connection.** The common trace cancels exactly and the remaining smoothing bias is controlled by the original endpoints.

**Sources.** [Spectral averaging](../science/spectral-averaging.md) · [Algorithm](../science/algorithm.md) · [Worked example](WORKED_EXAMPLE.md)

### M23 Use the smaller sign rank

**Central question.** When does a coarse estimate settle the signed test?

**Understanding target.** Bound the smaller leg by its rank. If the bigger leg's certified count is already above that range, declare nonzero. Otherwise estimate both legs finely in the resulting small-count regime.

**Prerequisites.** [M05](#m05-use-finite-rank-interlacing), [M20](#m20-estimate-a-rare-survival-probability), [M22](#m22-form-two-monotone-legs).

**Conceptual connection.** This gives the dependence on sign balance by restricting costly refinement to cases where cancellation is possible.

**Sources.** [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md)

### M24 Estimate and round a signed count

**Central question.** How does the algorithm report the size of the shift?

**Understanding target.** Allocate the count error across both leg estimates and the smoothing bias. Use a subunit error budget for exact integer recovery and a larger one for coarse additive estimation.

**Prerequisites.** [M12](#m12-assemble-the-operational-task), [M15](#m15-recover-a-plateau-through-smoothing), [M20](#m20-estimate-a-rare-survival-probability), [M22](#m22-form-two-monotone-legs).

**Conceptual connection.** Error allocation yields the additive-count result on the same oracle interface as detection.

**Sources.** [Model](../science/model.md) · [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md)

### M25 Encode a weak-oracle crossing

**Central question.** How can a bit change whether an energy level crosses zero?

**Understanding target.** Place an endpoint eigenvalue just below or above zero according to a hidden bit. Complete the scalar matrix entry to a unitary and bound the marked–unmarked difference by the gap scale.

**Prerequisites.** [M06](#m06-interpret-the-endpoint-gap), [M07](#m07-read-a-normalized-block-encoding), [M11](#m11-recognize-a-query-lower-bound).

**Conceptual connection.** The hard instances capture the inverse-gap cost inside the normalized block-encoding model.

**Sources.** [Lower bounds](../science/lower-bounds.md) · [Nielsen–Chuang §6.7](NIELSEN_CHUANG_BRIDGE.md)

### M26 Compare nearby Hamming weights

**Central question.** Why can changing the count by one be hard at high Hamming weight?

**Understanding target.** Use the inclusion relation between strings on neighboring weight layers. Compare the full adversary norm with the norm restricted to pairs differing in a given coordinate.

**Prerequisites.** [M11](#m11-recognize-a-query-lower-bound), [M25](#m25-encode-a-weak-oracle-crossing).

**Conceptual connection.** The weight-layer geometry sets the rank dependence and the factor-rank imbalance can choose which layer matters.

**Sources.** [Lower bounds](../science/lower-bounds.md) · [Nielsen–Chuang §§6.6–6.7](NIELSEN_CHUANG_BRIDGE.md)

### M27 Match the sign-balance law

**Central question.** How does the minority rank place the hard instances in weight space?

**Understanding target.** Use fixed opposing crossings to set the zero-net case near a chosen Hamming weight. Combine the weak oracle and the layer bound to match the upper detection cost.

**Prerequisites.** [M22](#m22-form-two-monotone-legs), [M23](#m23-use-the-smaller-sign-rank), [M25](#m25-encode-a-weak-oracle-crossing), [M26](#m26-compare-nearby-hamming-weights).

**Conceptual connection.** The construction unifies the positive search regime and the balanced cancellation regime in one lower bound.

**Sources.** [Lower bounds](../science/lower-bounds.md) · [Resource accounting](../science/resources.md)

### M28 Allocate implementation error

**Central question.** Which errors are multiplied when an acceptance probability becomes a count?

**Understanding target.** Track smoothing, grid, polynomial, oracle, and statistical contributions through the count rescaling. Separate oracle calls from elementary gates and workspace.

**Prerequisites.** [M12](#m12-assemble-the-operational-task), [M15](#m15-recover-a-plateau-through-smoothing), [M16](#m16-construct-a-coherent-sampled-path), [M17](#m17-stack-gaussian-contractions), [M19](#m19-bound-maximum-and-rms-cost), [M24](#m24-estimate-and-round-a-signed-count).

**Conceptual connection.** The calculation connects the ideal filters to the finite-precision implementation and states which resources depend on oracle realization.

**Sources.** [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md)

### M29 Interpret the finite checks

**Central question.** What does a small exact or numerical example establish?

**Understanding target.** Reproduce the noncommuting two-level crossing and the common-reference cancellation. Match endpoint counts to filter probabilities and connect the observed errors to the analytic bounds.

**Prerequisites.** [M15](#m15-recover-a-plateau-through-smoothing), [M17](#m17-stack-gaussian-contractions), [M22](#m22-form-two-monotone-legs), [M28](#m28-allocate-implementation-error).

**Conceptual connection.** Use finite examples to check the mechanism and use the proofs to justify the asymptotic claim.

**Sources.** [Worked example](WORKED_EXAMPLE.md) · [Spectral averaging](../science/spectral-averaging.md) · [Algorithm](../science/algorithm.md)

### M30 Connect the complete result

**Central question.** Why can one threshold problem interpolate between search and approximate counting?

**Understanding target.** Explain the count-to-probability identity, the reduction in branch cost, the two-leg cancellation and the hard weight layers as one chain. State the endpoint gap, access model and rank parameters that give the result its scope.

**Prerequisites.** [M12](#m12-assemble-the-operational-task), [M21](#m21-detect-a-positive-shift), [M23](#m23-use-the-smaller-sign-rank), [M24](#m24-estimate-and-round-a-signed-count), [M27](#m27-match-the-sign-balance-law), [M28](#m28-allocate-implementation-error), [M29](#m29-interpret-the-finite-checks).

**Conceptual connection.** Connect the source of the speedup with the precise case in which signed cancellation makes detection harder.

**Sources.** [Scientific account](../science/README.md) · [Model](../science/model.md) · [Resource accounting](../science/resources.md) · [Lower bounds](../science/lower-bounds.md)
