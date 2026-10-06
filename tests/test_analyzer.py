import pytest

from vscas.analyzer import (
    hybrid_similarity,
    compare_vectors,
)


def test_hybrid_similarity():
    result = hybrid_similarity(
        lexical_similarity=0.90,
        structural_similarity=0.80,
    )

    assert result == pytest.approx(0.87)


def test_custom_weight():
    result = hybrid_similarity(
        lexical_similarity=0.90,
        structural_similarity=0.80,
        lexical_weight=0.5,
    )

    assert result == pytest.approx(0.85)


def test_invalid_weight():
    with pytest.raises(ValueError):
        hybrid_similarity(0.9, 0.8, lexical_weight=1.5)


def test_compare_vectors():
    result = compare_vectors(
        lexical_vector_a=[1, 2, 3],
        lexical_vector_b=[1, 2, 3],
        structural_vector_a=[2, 3, 4],
        structural_vector_b=[2, 3, 4],
    )

    assert result["lexical_similarity"] == pytest.approx(1.0)
    assert result["structural_similarity"] == pytest.approx(1.0)
    assert result["hybrid_similarity"] == pytest.approx(1.0)