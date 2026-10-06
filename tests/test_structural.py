import numpy as np

from vscas.structural import (
    STRUCTURAL_FEATURES,
    structural_dict_to_vector,
    structural_feature_names,
)


def test_structural_vector():
    features = {
        "functions": 3,
        "loops": 2,
        "conditions": 4,
        "returns": 2,
        "classes": 1,
        "imports": 3,
        "operators": 8,
    }

    vector = structural_dict_to_vector(features)

    expected = np.array(
        [3, 2, 4, 2, 1, 3, 8],
        dtype=float,
    )

    assert np.array_equal(vector, expected)


def test_missing_features_become_zero():
    features = {
        "functions": 2,
        "loops": 3,
    }

    vector = structural_dict_to_vector(features)

    expected = np.array(
        [2, 3, 0, 0, 0, 0, 0],
        dtype=float,
    )

    assert np.array_equal(vector, expected)


def test_feature_order():
    names = structural_feature_names()

    assert names == [
        "functions",
        "loops",
        "conditions",
        "returns",
        "classes",
        "imports",
        "operators",
    ]


def test_structural_vector_dimension():
    features = {}

    vector = structural_dict_to_vector(features)

    assert len(vector) == len(STRUCTURAL_FEATURES)
    assert len(vector) == 7