# From quantum counting to spectral-shift counting

Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, 10th Anniversary Edition, Cambridge University Press (2010), hardback ISBN 978-1-107-00217-3. The links give the publisher's book record and edition front matter with section numbers. [Book record](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE) · [Front matter and contents](https://assets.cambridge.org/97811070/02173/frontmatter/9781107002173_frontmatter.pdf)

Start with §6.3 if you are comfortable with controlled circuits and eigenvalue decompositions. Use the earlier sections when their concepts enter the algorithm.

| Read | Use in the project |
| --- | --- |
| §§2.1.5–2.1.8, 2.1.10 | Pass between an eigenvalue and a function of a Hermitian operator. Interpret how a rectangular factor encodes a positive perturbation. |
| §§2.2.3, 2.2.5, 2.5 | Read a signal subspace as a projective outcome. Use two correlated label registers to average over perturbation directions. |
| §§4.3–4.4 | Control oracle calls on a path register. Copy the signal outcome into a coherent flag. |
| §§5.2–5.2.1, 6.1.1–6.1.4, 6.3 | Connect the phase of a product of reflections to its success probability and to the number of marked inputs. |
| §§6.6–6.7 | Track the information gained through repeated oracle queries. |

## Translate the search problem

In textbook quantum counting, the probability of a marked outcome comes from an oracle that evaluates a predicate on candidate labels. The project creates a success flag by filtering coherent inputs along an interpolating matrix path. Success depends both on an energy near the threshold and on the perturbation's overlap with its eigenspace. Spectral averaging converts this weighted probability into a smoothed change in the endpoint counts. [Model](../science/model.md) · [Spectral averaging](../science/spectral-averaging.md)

Covering the path requires controlled calls to normalized block encodings. A block encoding gives a specified matrix as the compression of a unitary between known signal subspaces. In the algorithm, the signal block of a Gaussian filter acts on the continuing branch, while the orthogonal subspace records failure. The label state gives a normalized trace over the columns of the perturbation factor. [Algorithm](../science/algorithm.md)

## Add early stopping and signed cancellation

The textbook's fixed-cost counting circuit motivates estimating a success amplitude. Here broad Gaussian stages reject most inputs cheaply. Narrow stages consume more queries and are reached with decreasing probability. The proof of this decrease uses the rank bound on the path's spectral density. Variable-time amplitude estimation then uses the root-mean-square branch cost together with the longest branch cost. The derivation and attribution for the polynomial filters and variable-time estimation are in the scientific account. [Algorithm](../science/algorithm.md) · [Resource accounting](../science/resources.md)

A signed update can move eigenvalues both ways. Two positive matrix paths reach the same reference, whose smoothed trace cancels. The smaller sign rank bounds one of the leg counts and distinguishes the regime in which resolving their difference needs the most precision. The lower bound embeds a Hamming-weight test into the same spectral question, with nearby oracle variants controlled by the endpoint gap. [Spectral averaging](../science/spectral-averaging.md) · [Lower bounds](../science/lower-bounds.md)

Work through the [two examples](WORKED_EXAMPLE.md), then follow the [milestone map](MILESTONES.md) for the complete argument.
