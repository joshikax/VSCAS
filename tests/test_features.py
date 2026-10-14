
from vscas.features import (
    count_tokens,
    extract_features,
    extract_lexical_features,
    extract_structural_features,
)


def test_count_tokens():
    assert count_tokens(["IDENT", "+", "IDENT"]) == {
        "IDENT": 2,
        "+": 1,
    }


def test_lexical_features():
    tokens = ["IDENT", "=", "10", "+", "IDENT", "2"]
    features = extract_lexical_features(tokens)

    assert features == {
        "identifier_count": 2,
        "number_count": 2,
        "operator_count": 2,
        "keyword_count": 0,
    }


def test_structural_features():
    tokens = [
        "def", "if", "for", "while",
        "return", "return", "class", "import",
    ]
    features = extract_structural_features(tokens)

    assert features == {
        "function_count": 1,
        "loop_count": 2,
        "condition_count": 1,
        "return_count": 2,
        "class_count": 1,
        "import_count": 1,
    }


def test_extract_features():
    features = extract_features(["IDENT", "=", "1", "return"])

    assert features["lexical"]["identifier_count"] == 1
    assert features["lexical"]["number_count"] == 1
    assert features["structural"]["return_count"] == 1
