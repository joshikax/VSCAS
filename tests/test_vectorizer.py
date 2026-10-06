import numpy as np

from vscas.vectorizer import (
    build_vocabulary,
    feature_dict_to_vector,
    feature_dicts_to_matrix
)


def test_build_vocabulary():
    features = [
        {"loops": 2, "functions": 3},
        {"loops": 1, "classes": 2}
    ]

    vocabulary = build_vocabulary(features)

    assert vocabulary == ["classes", "functions", "loops"]


def test_feature_dict_to_vector():
    features = {
        "loops": 2,
        "functions": 3
    }

    vocabulary = ["functions", "loops"]

    vector = feature_dict_to_vector(features, vocabulary)

    expected = np.array([3.0, 2.0])

    assert np.array_equal(vector, expected)


def test_missing_feature_becomes_zero():
    features = {
        "loops": 2
    }

    vocabulary = ["functions", "loops"]

    vector = feature_dict_to_vector(features, vocabulary)

    expected = np.array([0.0, 2.0])

    assert np.array_equal(vector, expected)


def test_feature_dicts_to_matrix():
    features = [
        {
            "loops": 2,
            "functions": 3
        },
        {
            "loops": 1,
            "functions": 2
        }
    ]

    matrix, vocabulary = feature_dicts_to_matrix(features)

    assert vocabulary == ["functions", "loops"]

    expected = np.array([
        [3.0, 2.0],
        [2.0, 1.0]
    ])

    assert np.array_equal(matrix, expected)