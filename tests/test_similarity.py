import pytest

from vscas.similarity import (
    dot_product,
    euclidean_norm,
    cosine_similarity
)


def test_dot_product():
    result = dot_product([1, 2, 3], [4, 5, 6])
    assert result == 32.0


def test_euclidean_norm():
    result = euclidean_norm([3, 4])
    assert result == 5.0


def test_identical_vectors():
    result = cosine_similarity([1, 2, 3], [1, 2, 3])
    assert result == pytest.approx(1.0)


def test_orthogonal_vectors():
    result = cosine_similarity([1, 0], [0, 1])
    assert result == pytest.approx(0.0)


def test_zero_vector():
    result = cosine_similarity([0, 0], [1, 2])
    assert result == 0.0


def test_dimension_mismatch():
    with pytest.raises(ValueError):
        cosine_similarity([1, 2], [1, 2, 3])