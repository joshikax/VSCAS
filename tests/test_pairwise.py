import numpy as np
import pytest

from vscas.pairwise import pairwise_cosine_similarity


def test_pairwise_matrix_shape():
    matrix = np.array([
        [1, 2, 3],
        [1, 2, 3],
        [3, 0, 0],
    ])

    result = pairwise_cosine_similarity(matrix)

    assert result.shape == (3, 3)


def test_diagonal_is_one():
    matrix = np.array([
        [1, 2, 3],
        [3, 4, 5],
    ])

    result = pairwise_cosine_similarity(matrix)

    assert result[0, 0] == pytest.approx(1.0)
    assert result[1, 1] == pytest.approx(1.0)


def test_matrix_is_symmetric():
    matrix = np.array([
        [1, 2, 3],
        [3, 4, 5],
        [5, 6, 7],
    ])

    result = pairwise_cosine_similarity(matrix)

    assert np.allclose(result, result.T)


def test_identical_vectors_have_similarity_one():
    matrix = np.array([
        [1, 2, 3],
        [1, 2, 3],
    ])

    result = pairwise_cosine_similarity(matrix)

    assert result[0, 1] == pytest.approx(1.0)
    assert result[1, 0] == pytest.approx(1.0)


def test_orthogonal_vectors_have_similarity_zero():
    matrix = np.array([
        [1, 0],
        [0, 1],
    ])

    result = pairwise_cosine_similarity(matrix)

    assert result[0, 1] == pytest.approx(0.0)
    assert result[1, 0] == pytest.approx(0.0)


def test_invalid_input():
    matrix = np.array([1, 2, 3])

    with pytest.raises(ValueError):
        pairwise_cosine_similarity(matrix)