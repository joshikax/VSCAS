import numpy as np
import pytest

from vscas.tfidf import (
    calculate_tf,
    calculate_idf,
    build_vocabulary,
    build_tfidf_matrix
)


def test_calculate_tf():
    tokens = ["for", "for", "if", "return"]

    tf = calculate_tf(tokens)

    assert tf["for"] == pytest.approx(0.5)
    assert tf["if"] == pytest.approx(0.25)
    assert tf["return"] == pytest.approx(0.25)


def test_empty_tf():
    tf = calculate_tf([])

    assert tf == {}


def test_calculate_idf():
    documents = [
        ["for", "if"],
        ["for", "return"],
        ["while", "return"]
    ]

    idf = calculate_idf(documents)

    assert "for" in idf
    assert "if" in idf
    assert "while" in idf
    assert "return" in idf

    # "for" appears in 2 of 3 documents,
    # while "if" appears in only 1.
    assert idf["if"] > idf["for"]


def test_build_vocabulary():
    documents = [
        ["for", "if"],
        ["while", "return"]
    ]

    vocabulary = build_vocabulary(documents)

    assert vocabulary == ["for", "if", "return", "while"]


def test_tfidf_matrix():
    documents = [
        ["for", "if"],
        ["for", "return"]
    ]

    matrix, vocabulary = build_tfidf_matrix(documents)

    assert vocabulary == ["for", "if", "return"]

    assert matrix.shape == (2, 3)

    assert isinstance(matrix, np.ndarray)

    # "if" only occurs in document 1,
    # so its TF-IDF value should be positive there.
    if_index = vocabulary.index("if")

    assert matrix[0, if_index] > 0
    assert matrix[1, if_index] == 0