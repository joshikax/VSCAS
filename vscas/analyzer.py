from .similarity import cosine_similarity


def hybrid_similarity(
    lexical_similarity,
    structural_similarity,
    lexical_weight=0.7,
):
    """
    Combine lexical and structural similarity.

    Final Score =
        lexical_weight * lexical_similarity
        +
        structural_weight * structural_similarity
    """

    if not 0.0 <= lexical_weight <= 1.0:
        raise ValueError("Lexical weight must be between 0 and 1.")

    structural_weight = 1.0 - lexical_weight

    return (
        lexical_weight * lexical_similarity
        + structural_weight * structural_similarity
    )


def compare_vectors(
    lexical_vector_a,
    lexical_vector_b,
    structural_vector_a,
    structural_vector_b,
    lexical_weight=0.7,
):
    """
    Compare two source-code representations.

    Returns:
        lexical similarity
        structural similarity
        final hybrid similarity
    """

    lexical_score = cosine_similarity(
        lexical_vector_a,
        lexical_vector_b,
    )

    structural_score = cosine_similarity(
        structural_vector_a,
        structural_vector_b,
    )

    final_score = hybrid_similarity(
        lexical_score,
        structural_score,
        lexical_weight,
    )

    return {
        "lexical_similarity": lexical_score,
        "structural_similarity": structural_score,
        "hybrid_similarity": final_score,
    }