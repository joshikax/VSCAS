import os
import re


def read_source_code(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def detect_language(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    language_map = {
        ".py": "Python",
        ".c": "C",
        ".cpp": "C++",
        ".cc": "C++",
        ".java": "Java"
    }

    return language_map.get(extension, "Unknown")


def remove_comments(code, language):
    if language == "Python":
        code = re.sub(r"#.*", "", code)

    elif language in ["C", "C++", "Java"]:
        code = re.sub(r"//.*", "", code)
        code = re.sub(r"/\*[\s\S]*?\*/", "", code)

    return code


def remove_strings(code):
    code = re.sub(
        r'"(?:\\.|[^"\\])*"',
        "STRING",
        code
    )

    code = re.sub(
        r"'(?:\\.|[^'\\])*'",
        "STRING",
        code
    )

    return code


def normalize_whitespace(code):
    return re.sub(r"\s+", " ", code).strip()


def preprocess_code(code, language):
    code = remove_comments(code, language)
    code = remove_strings(code)
    code = normalize_whitespace(code)

    return code


TOKEN_PATTERN = r"""
    [A-Za-z_][A-Za-z0-9_]*
    |\d+(?:\.\d+)?
    |==|!=|<=|>=|//|\+=|-=|\*=|/=|&&|\|\|
    |[+\-*/%=<>!]
    |[(){}\[\],;:.]
"""


def tokenize(code):
    return re.findall(
        TOKEN_PATTERN,
        code,
        re.VERBOSE
    )


KEYWORDS = {
    "Python": {
        "def", "return", "if", "elif", "else",
        "for", "while", "in", "import", "from",
        "class", "try", "except", "finally",
        "with", "as", "pass", "break", "continue"
    },

    "C": {
        "int", "float", "double", "char", "void",
        "if", "else", "for", "while", "return",
        "struct", "include"
    },

    "C++": {
        "int", "float", "double", "char", "void",
        "if", "else", "for", "while", "return",
        "class", "struct", "include"
    },

    "Java": {
        "public", "private", "protected",
        "class", "static", "void", "int",
        "float", "double", "char",
        "if", "else", "for", "while",
        "return", "import", "new"
    }
}


def normalize_identifiers(tokens, language):
    keywords = KEYWORDS.get(language, set())

    normalized = []

    for token in tokens:

        if token in keywords:
            normalized.append(token)

        elif re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*",
            token
        ):

            if token == "STRING":
                normalized.append(token)
            else:
                normalized.append("IDENT")

        else:
            normalized.append(token)

    return normalized