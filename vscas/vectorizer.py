import numpy as np


def build_vocabulary(feature_dictionaries):
    """
    Build a common vocabulary from multiple feature dictionaries.

    Example:
        {"loops": 2, "functions": 3}
        {"loops": 1, "classes": 2}

    Vocabulary:
        ["classes", "functions", "loops"]
    """

    vocabulary = set()

    for features in feature_dictionaries:
        vocabulary.update(features.keys())

    return sorted(vocabulary)


def feature_dict_to_vector(features, vocabulary):
    """
    Convert a feature dictionary into a numerical vector
    using a common vocabulary.
    """

    return np.array(
        [features.get(feature, 0) for feature in vocabulary],
        dtype=float
    )


def feature_dicts_to_matrix(feature_dictionaries):
    """
    Convert multiple feature dictionaries into a matrix.

    Each row represents one source-code file.
    Each column represents one feature.
    """

    vocabulary = build_vocabulary(feature_dictionaries)

    matrix = np.array(
        [
            feature_dict_to_vector(features, vocabulary)
            for features in feature_dictionaries
        ],
        dtype=float
    )

    return matrix, vocabulary