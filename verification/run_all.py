"""Finite checks for spectral-shift counting. Run with Python 3 and NumPy."""

from itertools import combinations
from math import comb, erf, erfc, exp, pi, sqrt

import numpy as np


def norm(matrix):
    return np.linalg.norm(matrix, ord=2)


def close(actual, expected, context, atol=2e-11):
    np.testing.assert_allclose(actual, expected, atol=atol, rtol=0, err_msg=context)


def smoothed_count(start, end, width):
    """Independent endpoint calculation, with zero energy receiving half weight."""
    start_values = np.linalg.eigvalsh(start)
    end_values = np.linalg.eigvalsh(end)
    return 0.5 * (
        sum(erf(width * x) for x in end_values)
        - sum(erf(width * x) for x in start_values)
    )


def negative_count(matrix):
    return int(np.count_nonzero(np.linalg.eigvalsh(matrix) < 0))


def path_probabilities(start, factor, widths, samples):
    """Integrate each weighted spectral measure on the same midpoint grid."""
    times = (np.arange(samples) + 0.5) / samples
    update = factor @ factor.conj().T
    values, vectors = np.linalg.eigh(start + times[:, None, None] * update)
    factor_weights = (abs(vectors.conj().transpose(0, 2, 1) @ factor) ** 2).sum(-1)
    return [
        float(np.mean(np.sum(factor_weights * np.exp(-(width * values) ** 2), axis=1))
              / factor.shape[1])
        for width in widths
    ]


def check_leg(start, factor, stages, samples):
    """Check the Gaussian identity, midpoint bound and every survival prefix."""
    end = start + factor @ factor.conj().T
    rank_width = factor.shape[1]
    filter_widths = np.sqrt(np.cumsum(np.square(stages)))
    previous_probability = 1.0
    max_quadrature_error = 0.0
    endpoint_counts = []
    probabilities = path_probabilities(start, factor, filter_widths, samples)
    for width, probability in zip(filter_widths, probabilities):
        smooth = smoothed_count(start, end, width)
        grid_count = width * rank_width * probability / sqrt(pi)
        grid_error = abs(grid_count - smooth)
        # Integral average distance to a midpoint is 1/(4*samples).
        lipschitz = 2 * width * norm(factor) ** 2 / sqrt(pi)
        bound = width * rank_width * lipschitz / (4 * sqrt(pi) * samples)
        assert grid_error <= bound + 2e-12, (grid_error, bound)
        assert -2e-12 <= smooth <= rank_width + 2e-12, smooth
        assert probability <= sqrt(pi) / width + bound * sqrt(pi) / (width * rank_width)
        assert 0 <= probability <= previous_probability + 2e-12
        previous_probability = probability
        endpoint_counts.append(smooth)
        max_quadrature_error = max(max_quadrature_error, grid_error)
    return endpoint_counts[-1], previous_probability, max_quadrature_error


def check_positive_paths():
    toy_start = np.diag([-0.5, 0.5])
    toy_factor = np.sqrt(np.array([[7 / 8], [1 / 8]]))
    rng = np.random.default_rng(27112026)
    cases = [(toy_start, toy_factor)]
    for index in range(28):
        dimension = 14
        rank_width = 1 + index % 5
        raw = rng.normal(size=(dimension, dimension))
        raw = raw + 1j * rng.normal(size=raw.shape)
        start = raw + raw.conj().T
        start /= norm(start)
        factor = rng.normal(size=(dimension, rank_width))
        factor = factor + 1j * rng.normal(size=factor.shape)
        factor /= norm(factor)
        cases.append((start, factor))
    stages = [1, 2, 4, 8, 16]
    width = sqrt(sum(x**2 for x in stages))
    histogram = {}
    max_grid_error = 0.0
    for start, factor in cases:
        end = start + factor @ factor.conj().T
        count = negative_count(start) - negative_count(end)
        histogram[count] = histogram.get(count, 0) + 1
        gap = min(min(abs(np.linalg.eigvalsh(start))), min(abs(np.linalg.eigvalsh(end))))
        smooth, _, grid_error = check_leg(start, factor, stages, samples=4096)
        assert abs(smooth - count) <= factor.shape[1] * erfc(width * gap) + 2e-12
        max_grid_error = max(max_grid_error, grid_error)
    toy_end = toy_start + toy_factor @ toy_factor.T
    assert negative_count(toy_start) - negative_count(toy_end) == 1
    noncommuting = norm(toy_start @ toy_end - toy_end @ toy_start)
    assert noncommuting > 0.3
    return (f"{len(cases)} positive paths, counts {dict(sorted(histogram.items()))}, "
            f"max midpoint error {max_grid_error:.3g}, toy commutator {noncommuting:.6f}")


def check_signed_paths():
    # Both legs end at a singular matrix, with noncommuting 2x2 restrictions.
    endpoint = np.diag([0.0, 0.6, 0.32])
    positive = np.array([[0.55, 0.0], [0.24, 0.0], [0.0, 0.78]])
    negative = np.array([[0.45], [-0.30], [0.0]])
    start = endpoint - positive @ positive.T
    end = endpoint - negative @ negative.T
    assert np.linalg.eigvalsh(endpoint)[0] == 0
    assert norm(start @ endpoint - endpoint @ start) > 0
    assert norm(end @ endpoint - endpoint @ end) > 0
    checks = [(start, end, positive, negative, 1),
              (end, start, negative, positive, -1),
              (start[:2, :2], end[:2, :2], positive[:2, :1], negative[:2], 0)]
    stages = [1, 2, 4, 8, 16]
    width = sqrt(sum(x**2 for x in stages))
    differences = []
    for initial, final, w_plus, w_minus, expected in checks:
        gamma = min(min(abs(np.linalg.eigvalsh(initial))), min(abs(np.linalg.eigvalsh(final))))
        assert gamma > 0.18
        assert negative_count(initial) - negative_count(final) == expected
        positive_count, plus_p, _ = check_leg(initial, w_plus, stages, samples=4096)
        negative_count_smooth, minus_p, _ = check_leg(final, w_minus, stages, samples=4096)
        difference = positive_count - negative_count_smooth
        close(difference, smoothed_count(initial, final, width), "common endpoint cancellation")
        rank_width = w_plus.shape[1] + w_minus.shape[1]
        assert abs(difference - expected) <= 2 * rank_width * erfc(width * gamma) + 2e-12
        grid_difference = width / sqrt(pi) * (w_plus.shape[1] * plus_p - w_minus.shape[1] * minus_p)
        assert round(grid_difference) == expected
        differences.append(grid_difference)
    return f"singular common endpoint, recovered net counts {[round(x) for x in differences]}"


def psd_square_root(matrix):
    values, vectors = np.linalg.eigh(matrix)
    assert min(values) >= -2e-12
    return (vectors * np.sqrt(np.maximum(values, 0))) @ vectors.conj().T


def unitary_completion(block):
    identity = np.eye(len(block))
    return np.block([[block, psd_square_root(identity - block @ block.conj().T)],
                     [psd_square_root(identity - block.conj().T @ block), -block.conj().T]])


def selector_prepare(weights):
    """A known unitary with first column sqrt(weights)."""
    target = np.sqrt(weights)
    basis = np.eye(len(weights))[:, 0]
    difference = basis - target
    length = float(difference @ difference)
    if length < 1e-28:
        return np.eye(len(weights))
    return np.eye(len(weights)) - 2 * np.outer(difference, difference) / length


def gaussian_coefficients(width, alpha, order):
    """Chebyshev Gaussian coefficients from the difference of two Poisson variables."""
    mean = (width * alpha) ** 2 / 8
    cutoff = int(mean + 14 * sqrt(mean + 1) + 24)
    poisson = np.empty(cutoff + 1)
    poisson[0] = exp(-mean)
    for index in range(1, len(poisson)):
        poisson[index] = poisson[index - 1] * mean / index
    correlation = np.correlate(poisson, poisson, mode="full")[cutoff:cutoff + order + 1]
    correlation[1::2] *= -2
    correlation[2::2] *= 2
    return correlation


def choose_and_unprepare(preparation, operations, state):
    selected = np.array([preparation[index, 0] * (matrix @ state)
                         for index, matrix in enumerate(operations)])
    return preparation.conj().T @ selected


def normalized_path_encoding(start, factor_encoding, time):
    """Compose an exact normalized Hermitian oracle for the positive leg."""
    dimension = len(start)
    identity = np.eye(2 * dimension)
    signal_reflection = np.diag(np.r_[np.ones(dimension), -np.ones(dimension)])
    factor_reflection = factor_encoding @ signal_reflection @ factor_encoding.conj().T
    signal_flip = np.kron(np.array([[0, 1], [1, 0]]), np.eye(dimension))
    operations = [unitary_completion(start), factor_reflection, identity, signal_flip]
    preparation = selector_prepare([0.5, time / 4, time / 4, (1 - time) / 2])
    full_preparation = np.kron(preparation, identity)
    select = np.zeros((8 * dimension, 8 * dimension), dtype=complex)
    for index, operation in enumerate(operations):
        slot = slice(index * 2 * dimension, (index + 1) * 2 * dimension)
        select[slot, slot] = operation
    return full_preparation.conj().T @ select @ full_preparation


def lcu_gaussian(matrix, encoding, data, width, alpha, order):
    """Simulate PREP–SELECT–PREP† and retain all signal and failure amplitudes."""
    dimension = len(matrix)
    encoding_dimension = len(encoding)
    signal = np.r_[np.ones(dimension), -np.ones(encoding_dimension - dimension)]
    reflection = np.diag(signal)
    walk = reflection @ encoding
    even_walk = walk @ walk
    coefficients = gaussian_coefficients(width, alpha, order)
    weights = np.r_[abs(coefficients), 1 - np.sum(abs(coefficients))]
    assert min(weights) >= 0
    prepare = selector_prepare(weights)
    close(prepare[:, 0], np.sqrt(weights), "LCU selector weights")
    powers = [np.eye(encoding_dimension)]
    for _ in range(order):
        powers.append(even_walk @ powers[-1])
    operations = [np.sign(coefficient) * power for coefficient, power in zip(coefficients, powers)]
    # A signal flip pads the truncated tail with a zero top block.
    signal_flip = np.kron(np.array([[0, 1], [1, 0]]), np.eye(encoding_dimension // 2))
    operations.append(signal_flip)
    state = np.r_[data, np.zeros(encoding_dimension - dimension)]
    output = choose_and_unprepare(prepare, operations, state)
    alive = output[0, :dimension]
    failures = np.r_[output[0, dimension:], output[1:].flatten()]

    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    chebyshev = np.zeros(2 * order + 1)
    chebyshev[::2] = coefficients
    response = np.polynomial.chebyshev.chebval(eigenvalues / alpha, chebyshev)
    direct = eigenvectors @ (response * (eigenvectors.conj().T @ data))
    close(alive, direct, "LCU live amplitudes versus direct Chebyshev polynomial")
    close(np.vdot(alive, alive) + np.vdot(failures, failures), np.vdot(data, data),
          "LCU branch normalization")
    return alive, failures, float(weights[-1])


def check_coherent_stopping():
    start = np.diag([-0.5, 0.5])
    factor = np.array([[0.82, 0.16], [0.29, 0.43]])
    update = factor @ factor.T
    times = (np.arange(8) + 0.5) / 8
    stages = [1, 2, 4]
    order = 20
    dimension = len(start)
    preparation = unitary_completion(factor)
    close(preparation.conj().T @ preparation, np.eye(2 * dimension), "factor block unitary")
    path_matrices = [start + time * update for time in times]
    path_encodings = [normalized_path_encoding(start, preparation, time) for time in times]
    for matrix, encoding in zip(path_matrices, path_encodings):
        close(encoding, encoding.conj().T, "composed path oracle adjoint")
        close(encoding @ encoding, np.eye(len(encoding)), "composed path oracle unitary")
        close(encoding[:dimension, :dimension], matrix / 2, "composed path signal block")
    label_weight = 1 / sqrt(len(times) * factor.shape[1])
    first_failures = []
    alive = {}
    for time_index in range(len(times)):
        for label in range(factor.shape[1]):
            basis = np.eye(2 * dimension)[:, label]
            output = label_weight * (preparation @ basis)
            alive[time_index, label] = output[:dimension]
            first_failures.append(output[dimension:])

    failure_by_stage = [float(np.linalg.norm(first_failures) ** 2)]
    probabilities = []
    accumulated_tail = 0.0
    max_probability_error = 0.0
    for stage_index, width in enumerate(stages):
        halted = []
        stage_tail = 0.0
        for (time_index, label), data in alive.items():
            continuing, stopped, stage_tail = lcu_gaussian(
                path_matrices[time_index], path_encodings[time_index], data, width, 2, order
            )
            alive[time_index, label] = continuing
            halted.append(stopped)
        failure_by_stage.append(float(np.linalg.norm(halted) ** 2))
        continuing_array = np.array(list(alive.values()))
        probability = float(np.linalg.norm(continuing_array) ** 2)
        probabilities.append(probability)
        # Time, reference and stopping labels are orthogonal. Sum their squared
        # amplitudes and compare with the ideal Gaussian probability on the same grid.
        close(sum(failure_by_stage) + probability, 1, "coherent stopping mass")
        combined_width = sqrt(sum(x**2 for x in stages[:stage_index + 1]))
        ideal_probability, = path_probabilities(start, factor, [combined_width], len(times))
        accumulated_tail += stage_tail
        error = abs(ideal_probability - probability)
        assert error <= 2 * accumulated_tail + 2e-12
        max_probability_error = max(max_probability_error, error)
    assert all(p > 1e-3 for p in failure_by_stage), failure_by_stage
    # Equal-weight dummy history uses its own clock label and can halt immediately.
    dummy_probability = 0.025
    dummy_accept = np.array([sqrt(dummy_probability / 2), sqrt(probabilities[-1] / 2)])
    close(np.vdot(dummy_accept, dummy_accept), (dummy_probability + probabilities[-1]) / 2,
          "early-success padding")
    return (f"eight coherent time labels, three degree-{2 * order} LCU filters, "
            f"final success {probabilities[-1]:.8f}, max ideal-probability error "
            f"{max_probability_error:.3g}")


def check_fixed_block_precision():
    gamma = 0.15
    delta = gamma / 10
    start = np.diag([-0.48, 0.35])
    positive = np.array([[0.86], [0.13]])
    negative = np.array([[0.12], [0.76]])
    nominal_end = start + positive @ positive.T - negative @ negative.T
    assert min(abs(np.linalg.eigvalsh(nominal_end))) > gamma
    rng = np.random.default_rng(1937)
    for _ in range(32):
        perturbations = []
        for matrix in [start, positive, negative]:
            change = rng.normal(size=matrix.shape) + 1j * rng.normal(size=matrix.shape)
            perturbations.append(delta * change / norm(change))
        first, second, third = perturbations
        effective_start = start + (first + first.conj().T) / 2
        effective_positive = positive + second
        effective_negative = negative + third
        assert max(norm(effective_positive), norm(effective_negative)) < 1
        common = effective_start + effective_positive @ effective_positive.conj().T
        effective_end = common - effective_negative @ effective_negative.conj().T
        assert norm(effective_end - nominal_end) <= 5 * delta
        assert min(abs(np.linalg.eigvalsh(effective_end))) >= gamma / 2
        assert negative_count(effective_start) - negative_count(effective_end) == (
            negative_count(start) - negative_count(nominal_end)
        )
    return "32 fixed complex block perturbations, stable endpoint inertia"


def check_inclusion_adversary():
    cases = 0
    max_error = 0.0
    for width in range(1, 9):
        indices = range(width)
        for weight in range(width):
            for delta in range(1, width - weight + 1):
                rows = [frozenset(subset) for subset in combinations(indices, weight)]
                columns = [frozenset(subset) for subset in combinations(indices, weight + delta)]
                adjacency = np.array([[x <= y for y in columns] for x in rows], dtype=float)
                expectation = sqrt(comb(width - weight, delta) * comb(weight + delta, delta))
                close(norm(adjacency), expectation, "full inclusion norm")
                for index in indices:
                    mask = np.array([[index in y - x for y in columns] for x in rows])
                    ratio = norm(adjacency * mask) / expectation
                    expected_ratio = delta / sqrt((width - weight) * (weight + delta))
                    close(ratio, expected_ratio, "per-coordinate adversary ratio")
                    max_error = max(max_error, abs(ratio - expected_ratio))
                cases += 1
    ratios = []
    for gap in [1 / 128, 1 / 32, 1 / 8, 1 / 4]:
        first = unitary_completion(np.array([[-0.5 - gap]]))
        second = unitary_completion(np.array([[-0.5 + gap]]))
        close(first @ first.T, np.eye(2), "weak oracle completion")
        close(second @ second.T, np.eye(2), "weak oracle completion")
        ratios.append(norm(first - second) / gap)
    assert max(ratios) < 3
    return (f"{cases} inclusion matrices, max ratio error {max_error:.3g}, "
            f"max weak-oracle norm difference divided by gap {max(ratios):.6f}")


def main():
    checks = [
        ("Gaussian averaging", check_positive_paths),
        ("Signed cancellation", check_signed_paths),
        ("Coherent stopping", check_coherent_stopping),
        ("Fixed block precision", check_fixed_block_precision),
        ("Adversary", check_inclusion_adversary),
    ]
    for label, check in checks:
        print(f"{label} — {check()}")
    print("All finite checks passed.")


if __name__ == "__main__":
    main()
