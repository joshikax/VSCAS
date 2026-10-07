from vscas.preprocessing import (
    preprocess_code,
    tokenize,
    normalize_identifiers
)

from vscas.features import extract_features


code = """
def calculate(a, b):
    total = a + b

    if total > 10:
        return total

    return 0
"""


language = "Python"


# Step 1: Preprocess
processed = preprocess_code(code, language)

# Step 2: Tokenize
tokens = tokenize(processed)

# Step 3: Normalize identifiers
normalized_tokens = normalize_identifiers(tokens, language)

# Step 4: Extract features
features = extract_features(normalized_tokens)


print("========== PROCESSED CODE ==========")
print(processed)

print("\n========== TOKENS ==========")
print(tokens)

print("\n========== NORMALIZED TOKENS ==========")
print(normalized_tokens)

print("\n========== FEATURES ==========")
print(features)