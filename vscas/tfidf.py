import math
from collections import Counter

import numpy as np


def calculate_tf(tokens):
    """
    Calculate Term Frequency (TF).

    TF(term) = frequency of term / total number of terms
    """

    if not tokens:
        return {}

    counts = Counter(tokens)
    total_terms = len(tokens)

    return {
        term: count / total_terms
        for term, count in counts.items()
    }


def calculate_idf(documents):
    """
    Calculate Inverse Document Frequency (IDF).

    IDF(term) = log((1 + N) / (1 + DF)) + 1

    N  = number of documents
    DF = number of documents containing the term
    """

    number_of_documents = len(documents)

    if number_of_documents == 0:
        return {}

    document_frequency = Counter()

    for document in documents:
        unique_terms = set(document)

        for term in unique_terms:
            document_frequency[term] += 1

    return {
        term: math.log(
            (1 + number_of_documents) / (1 + frequency)
        ) + 1
        for term, frequency in document_frequency.items()
    }


def build_vocabulary(documents):
    """
    Build a sorted vocabulary from all documents.
    """

    vocabulary = set()

    for document in documents:
        vocabulary.update(document)

    return sorted(vocabulary)


def build_tfidf_matrix(documents):
    """
    Convert tokenized documents into a TF-IDF matrix.

    Each row represents one source-code document.
    Each column represents one token.
    """

    if not documents:
        return np.empty((0, 0), dtype=float), []

    vocabulary = build_vocabulary(documents)

    idf = calculate_idf(documents)

    matrix = []

    for document in documents:
        tf = calculate_tf(document)

        vector = [
            tf.get(term, 0.0) * idf.get(term, 0.0)
            for term in vocabulary
        ]

        matrix.append(vector)

    return np.array(matrix, dtype=float), vocabulary