# Quantum Spectral-Shift Counting

How many energy levels move across a threshold when a Hamiltonian is changed by a low-rank perturbation? A quantum algorithm can answer using a number of oracle calls set by the update rank and the endpoint gap. The size of the ambient spectrum does not enter the query bound.

For Hermitian endpoints $`A`$ and $`B`$, write the update as a positive part minus a negative part. Let $`r`$ be their total rank, $`s`$ the smaller of their ranks, and $`\gamma`$ the common gap about the threshold. With controlled, normalized block encodings of the initial matrix and the two update factors, the main bounds are:

| Task | Worst-case query complexity up to logarithms |
| --- | --- |
| Detect a nonzero net change in the number of levels below the threshold | $`\widetilde{\Theta}(\sqrt{r(s+1)}/\gamma)`$ |
| Detect a crossing under a positive update | $`\widetilde{\Theta}(\sqrt r/\gamma)`$ |
| Estimate the net count to absolute error $`\eta`$ | $`\widetilde{\Theta}(r/[\gamma\max(1,\eta)])`$ in the nontrivial accuracy range |

The count includes multiplicities. For signed updates, upward and downward crossings contribute opposite signs. When the two sign ranks are comparable, deciding whether those contributions cancel can take order $`r/\gamma`$ queries up to logarithms. Exact integer counting follows from an estimate with error below half a level.

The algorithm uses the update factors to sample the spectral flow along two monotone paths. Coherent Gaussian filtering rejects off-threshold amplitude at progressively finer resolutions. Spectral averaging bounds the probability of reaching each finer stage. The two paths meet at an auxiliary matrix whose contribution cancels, so the gap assumption concerns the endpoints alone.

## Run the spectral-shift estimator

1. **Prepare one path and its input label.** Use the supplied normalized controlled block encodings and adjoints for the centered initial matrix and rectangular update factors. Prepare a uniform dyadic midpoint register and one half of a maximally entangled factor label, keeping the other half as a reference. Use [reversible selector comparisons](science/algorithm.md#path-oracle) to select the plus path from the initial endpoint to the common auxiliary matrix, or the minus path from the final endpoint to that same matrix.
2. **Flag the filter stages coherently.** Apply the chosen factor and record its signal test. At each successive Gaussian width, prepare the [dyadic filter weights](science/algorithm.md#a-finite-gaussian-circuit), apply the signed controlled walk powers, and undo the selector preparation. Store the first failed test and apply subsequent stages only to continuing branches. Keep the tests and midpoint label coherent until estimation.
3. **Estimate success and combine the counts.** Apply [variable-time amplitude estimation](science/algorithm.md#estimating-one-leg), undo the known dummy-branch mixture, and rescale each success probability using its Gaussian width and padded factor dimension. Subtract the minus-path count from the plus-path count. For [detection](science/algorithm.md#detecting-cancellation), first use the larger-leg lower-bound test. If it is inconclusive, refine both leg estimates, subtract, round and test for zero. For exact counting, round only once the total error is below half a level.

Set the resolution and error budgets from the endpoint gap. The [resource account](science/resources.md) charges the supplied circuits, their adjoints, known gates, arithmetic and workspace.

## Read the science

- [Task, access model and theorems](science/model.md) states the promises and costs.
- [Spectral averaging](science/spectral-averaging.md) turns the count into a Gaussian acceptance probability and explains signed cancellation.
- [Algorithm and query bounds](science/algorithm.md) gives the coherent circuit and the detection rule.
- [Query lower bounds](science/lower-bounds.md) explains the dependence on the minority sign rank.
- [Resources and accuracy](science/resources.md) accounts for control, arithmetic and approximate input encodings.
- [Related work](references/related-work.md) credits the classical spectral shift identity, finite-rank inertia methods and quantum estimation primitives.

## Learn and verify

Start with the [learning route](learning/README.md), the [30 milestones](learning/MILESTONES.md), or the [science guide](science/README.md). See [verification](verification/README.md) for the executable checks and their expected results. These checks exercise finite matrices and filter circuits. The asymptotic bounds follow from the proofs.

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
