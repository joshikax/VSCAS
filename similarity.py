import numpy as np


def dot_product(vector_a, vector_b):
    """
    Calculate the dot product of two vectors.
    """

    a = np.asarray(vector_a, dtype=float)
    b = np.asarray(vector_b, dtype=float)

    if a.shape != b.shape:
        raise ValueError("Vectors must have the same dimensions.")

    return float(np.dot(a, b))


def euclidean_norm(vector):
    """
    Calculate the Euclidean norm of a vector.
    """

    vector = np.asarray(vector, dtype=float)

    return float(np.linalg.norm(vector))


def cosine_similarity(vector_a, vector_b):
    """
    Calculate cosine similarity between two vectors.

    Formula:
        cos(theta) = (A . B) / (||A|| * ||B||)
    """

    a = np.asarray(vector_a, dtype=float)
    b = np.asarray(vector_b, dtype=float)

    if a.shape != b.shape:
        raise ValueError("Vectors must have the same dimensions.")

    norm_a = euclidean_norm(a)
    norm_b = euclidean_norm(b)

    if norm_a == 0 or norm_b == 0:
        return 0.0

    similarity = dot_product(a, b) / (norm_a * norm_b)

    return float(similarity)