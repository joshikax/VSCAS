from collections import Counter


# Keywords used to identify program structure
CONTROL_FLOW = {
    "if", "elif", "else",
    "for", "while",
    "switch", "case"
}

FUNCTION_KEYWORDS = {
    "def"
}

RETURN_KEYWORDS = {
    "return"
}

IMPORT_KEYWORDS = {
    "import", "from", "include"
}

CLASS_KEYWORDS = {
    "class", "struct"
}


def count_tokens(tokens):
    """
    Count how many times each token appears.
    """
    return Counter(tokens)


def extract_lexical_features(tokens):
    """
    Extract features based on the lexical content of the program.
    """

    counts = Counter(tokens)

    operators = {
        "+", "-", "*", "/", "%",
        "=", "==", "!=", "<", ">",
        "<=", ">=", "+=", "-=", "*=", "/="
    }

    numbers = sum(
        1 for token in tokens
        if token.replace(".", "", 1).isdigit()
    )

    operator_count = sum(
        1 for token in tokens
        if token in operators
    )

    identifier_count = counts["IDENT"]

    keyword_count = sum(
        1 for token in tokens
        if token not in {"IDENT", "STRING"}
        and not token.replace(".", "", 1).isdigit()
        and token not in operators
    )

    return {
        "identifier_count": identifier_count,
        "number_count": numbers,
        "operator_count": operator_count,
        "keyword_count": keyword_count
    }


def extract_structural_features(tokens):
    """
    Extract features describing the structure of the program.
    """

    counts = Counter(tokens)

    return {
        "function_count": counts["def"],

        "loop_count": (
            counts["for"] +
            counts["while"]
        ),

        "condition_count": (
            counts["if"] +
            counts["elif"] +
            counts["else"] +
            counts["switch"] +
            counts["case"]
        ),

        "return_count": counts["return"],

        "class_count": (
            counts["class"] +
            counts["struct"]
        ),

        "import_count": (
            counts["import"] +
            counts["from"] +
            counts["include"]
        )
    }


def extract_features(tokens):
    """
    Extract both lexical and structural features.
    """

    lexical = extract_lexical_features(tokens)

    structural = extract_structural_features(tokens)

    return {
        "lexical": lexical,
        "structural": structural
    }