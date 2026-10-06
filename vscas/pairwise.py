import numpy as np

from .similarity import cosine_similarity


def pairwise_cosine_similarity(matrix):
    """
    Calculate cosine similarity between every pair of vectors.

    Parameters
    ----------
    matrix : array-like
        A matrix where each row represents one source-code vector.

    Returns
    -------
    numpy.ndarray
        Symmetric pairwise similarity matrix.
    """

    matrix = np.asarray(matrix, dtype=float)

    if matrix.ndim != 2:
        raise ValueError("Input must be a 2D matrix.")

    number_of_documents = matrix.shape[0]

    similarity_matrix = np.zeros(
        (number_of_documents, number_of_documents),
        dtype=float,
    )

    for i in range(number_of_documents):
        for j in range(number_of_documents):
            similarity_matrix[i, j] = cosine_similarity(
                matrix[i],
                matrix[j],
            )

    return similarity_matrix