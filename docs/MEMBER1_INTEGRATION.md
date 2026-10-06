# VSCAS — Member 1 Integration Guide

## Member 1 Role

Member 1 is responsible for the mathematical and similarity engine of VSCAS.

The engine converts source-code features into numerical vectors and calculates similarity using Linear Algebra.

---

## 1. Cosine Similarity

File:

`vscas/similarity.py`

Function:

```python
cosine_similarity(vector_a, vector_b)
```

This calculates the similarity between two vectors using:

\[
Cosine(A,B)=\frac{A\cdot B}{||A||||B||}
\]

Example:

```python
from vscas.similarity import cosine_similarity

score = cosine_similarity([1, 2, 3], [1, 2, 3])

print(score)
```

Output:

```text
1.0
```

---

## 2. Vectorization

File:

`vscas/vectorizer.py`

Functions:

```python
build_vocabulary(feature_dictionaries)

feature_dict_to_vector(features, vocabulary)

feature_dicts_to_matrix(feature_dictionaries)
```

Example feature dictionary:

```python
{
    "functions": 3,
    "loops": 2,
    "conditions": 4
}
```

The dictionary is converted into a numerical vector using a common feature vocabulary.

---

## 3. TF-IDF

File:

`vscas/tfidf.py`

Functions:

```python
calculate_tf(tokens)

calculate_idf(documents)

build_vocabulary(documents)

build_tfidf_matrix(documents)
```

Input:

```python
documents = [
    ["for", "if", "return"],
    ["for", "while", "return"]
]
```

Output:

A TF-IDF numerical matrix and vocabulary.

---

## 4. Structural Features

File:

`vscas/structural.py`

The current structural feature basis is:

```text
functions
loops
conditions
returns
classes
imports
operators
```

Function:

```python
structural_dict_to_vector(features)
```

Example:

```python
{
    "functions": 3,
    "loops": 2,
    "conditions": 4
}
```

becomes:

```text
[3, 2, 4, 0, 0, 0, 0]
```

---

## 5. Hybrid Similarity

File:

`vscas/analyzer.py`

Function:

```python
hybrid_similarity(
    lexical_similarity,
    structural_similarity,
    lexical_weight=0.7
)
```

Current weighting:

```text
Lexical similarity    = 70%
Structural similarity = 30%
```

Formula:

```text
Final Score =
0.7 × Lexical Similarity
+
0.3 × Structural Similarity
```

Example:

```text
Lexical similarity    = 0.90
Structural similarity = 0.80

Final similarity = 0.87
```

---

## 6. Complete Vector Comparison

Function:

```python
compare_vectors(
    lexical_vector_a,
    lexical_vector_b,
    structural_vector_a,
    structural_vector_b
)
```

Returns:

```python
{
    "lexical_similarity": ...,
    "structural_similarity": ...,
    "hybrid_similarity": ...
}
```

---

## 7. Pairwise Similarity Matrix

File:

`vscas/pairwise.py`

Function:

```python
pairwise_cosine_similarity(matrix)
```

Each row of the input matrix represents one source-code vector.

The output is a square similarity matrix.

Example:

```text
       A     B     C

A    1.00  0.82  0.31
B    0.82  1.00  0.28
C    0.31  0.28  1.00
```

The matrix is symmetric.

---

## Integration With Member 2

Member 2 should provide:

1. Tokenized source-code documents.
2. Lexical feature dictionaries.
3. Structural feature dictionaries.

The structural feature names should match:

```text
functions
loops
conditions
returns
classes
imports
operators
```

---

## Integration With Member 3

Member 3 can use:

- lexical similarity
- structural similarity
- hybrid similarity
- pairwise similarity matrix

for the dashboard, similarity results and heatmap.

---

## Testing

The Member 1 mathematical engine currently has:

```text
29 automated tests
```

Expected result:

```text
29 passed
```

The tests cover:

- dot product
- Euclidean norm
- cosine similarity
- vectorization
- TF-IDF
- structural vectors
- hybrid similarity
- pairwise similarity