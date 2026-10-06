import numpy as np


STRUCTURAL_FEATURES = [
    "functions",
    "loops",
    "conditions",
    "returns",
    "classes",
    "imports",
    "operators",
]


def structural_dict_to_vector(features):
    """
    Convert structural feature counts into a fixed-order vector.

    The feature order is defined by STRUCTURAL_FEATURES.
    Missing features are represented as zero.
    """

    return np.array(
        [
            features.get(feature, 0)
            for feature in STRUCTURAL_FEATURES
        ],
        dtype=float,
    )


def structural_feature_names():
    """
    Return the fixed structural feature order.
    """

    return STRUCTURAL_FEATURES.copy()