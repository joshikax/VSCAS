# VSCAS — Visual Source Code Analysis System

VSCAS (Visual Source Code Analysis System) is a Python-based tool for analyzing source code using preprocessing, tokenization, feature extraction, vectorization, and similarity analysis.

The system is designed to analyze source-code files and extract meaningful lexical and structural information that can be used to compare programs and identify similarities.

## 👥 Team Members

| Member       | Name                         | USN            |
| ------------ | ---------------------------- | -------------- |
| **Member 1** | **Joshika Kuntimaddi**       | PES2UG25CS267  |
| **Member 2** | **Namita Maruti Sherakhane** | PES2UG252CS323 |
| **Member 3** | **M Navya**                  | PES2UG25CS281  |
| **Member 4** | **Manya Agarwal**            | PES2UG25CS298  |

## 🎯 Project Objectives

* Read and analyze source-code files.
* Detect the programming language from file extensions.
* Remove comments and string literals from source code.
* Normalize whitespace and source-code formatting.
* Tokenize source code into meaningful tokens.
* Normalize identifiers to reduce the effect of variable and function names.
* Extract lexical and structural features.
* Convert extracted features into numerical vectors.
* Calculate similarity between source-code representations.
* Provide a foundation for detecting similar or potentially copied source code.

## 🏗️ Project Structure

```text
VSCAS/
│
├── vscas/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── features.py
│   ├── pairwise.py
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── structural.py
│   ├── tfidf.py
│   └── vectorizer.py
│
├── tests/
│   ├── test_analyzer.py
│   ├── test_features.py
│   ├── test_pairwise.py
│   ├── test_similarity.py
│   ├── test_structural.py
│   ├── test_tfidf.py
│   └── test_vectorizer.py
│
├── samples/
│   ├── sample1.py
│   └── sample2.py
│
├── docs/
├── requirements.txt
├── test_math.py
└── README.md
```

## 🔍 Main Features

### 1. Source Code Preprocessing

The preprocessing module prepares source code for analysis by:

* Reading source-code files.
* Detecting the programming language.
* Removing comments.
* Replacing string literals.
* Normalizing whitespace.

Supported languages include:

* Python
* C
* C++
* Java

### 2. Tokenization

Source code is converted into a sequence of meaningful tokens.

For example:

```text
def IDENT ( IDENT , IDENT ) : return IDENT + IDENT
```

### 3. Identifier Normalization

Variable names, function names, and other identifiers are converted into a common representation.

For example:

```text
calculate
total
result
```

can become:

```text
IDENT
IDENT
IDENT
```

This allows structurally similar programs to be compared even when different variable names are used.

### 4. Feature Extraction

VSCAS extracts both lexical and structural features.

#### Lexical Features

* Identifier count
* Number count
* Operator count
* Keyword count

#### Structural Features

* Function count
* Loop count
* Condition count
* Return count
* Class/struct count
* Import count

### 5. TF-IDF Representation

The project includes TF-IDF processing for representing tokenized source-code documents numerically.

### 6. Vectorization

Feature dictionaries can be converted into numerical vectors using a common vocabulary, making them suitable for mathematical similarity calculations.

### 7. Similarity Analysis

VSCAS supports cosine similarity between numerical representations of source code.

Cosine similarity ranges from:

```text
1.0 → Highly similar
0.0 → No similarity
```

Pairwise similarity can also be calculated for multiple source-code files.

## ⚙️ Installation

### Prerequisites

Make sure Python 3.x is installed on your system.

### Clone the Repository

```bash
git clone https://github.com/joshikax/VSCAS.git
cd VSCAS
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Current dependencies include:

```text
numpy
streamlit
```

## 🧪 Running Tests

Run the complete test suite using:

```bash
python -m pytest -q
```

The current test suite passes:

```text
29 passed
```

## 📊 Example

Given two programs:

### Program 1

```python
def add(a, b):
    return a + b
```

### Program 2

```python
def add(x, y):
    result = x + y
    return result
```

The programs can be preprocessed, tokenized, normalized, and converted into feature representations. Their lexical and structural features can then be compared using vector-based similarity measures.

## 🔄 Processing Pipeline

```text
Source Code
     │
     ▼
Language Detection
     │
     ▼
Comment Removal
     │
     ▼
String Normalization
     │
     ▼
Whitespace Normalization
     │
     ▼
Tokenization
     │
     ▼
Identifier Normalization
     │
     ▼
Feature Extraction
     │
     ├───────────────┐
     ▼               ▼
Lexical Features   Structural Features
     │               │
     └───────┬───────┘
             ▼
       Vectorization
             │
             ▼
      Similarity Analysis
             │
             ▼
       Comparison Result
```

## 🛠️ Technologies Used

* **Python** — Core programming language
* **NumPy** — Numerical computations and vector operations
* **Pytest** — Automated testing
* **Streamlit** — User interface/dashboard
* **Regular Expressions** — Source-code preprocessing and tokenization
* **Git & GitHub** — Version control and collaboration

## 🚀 Future Enhancements

* Support for additional programming languages.
* Abstract Syntax Tree (AST) based analysis.
* Advanced code similarity algorithms.
* Code plagiarism detection.
* Interactive similarity reports.
* Upload-based source-code analysis.
* Improved visualization through Streamlit.
* More robust analysis of complex programming constructs.

## 👩‍💻 Team Contributions

### Member 1 — Joshika Kuntimaddi

Project development, integration, and assigned project modules.

### Member 2 — Namita Maruti Sherakhane

Code preprocessing and feature extraction.

### Member 3 — M Navya

Testing, analysis, and assigned project modules.

### Member 4 — Manya Agarwal

Code analysis, testing, and assigned project modules.

## 📄 License

This project is developed for academic purposes.

---

### VSCAS

**Visual Source Code Analysis System**

*Analyzing code. Extracting structure. Measuring similarity.*
