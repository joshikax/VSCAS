import streamlit as st
import pandas as pd
import numpy as np

from vscas.preprocessing import (
    detect_language,
    preprocess_code,
    tokenize,
    normalize_identifiers,
)
from vscas.features import extract_features
from vscas.structural import structural_dict_to_vector
from vscas.vectorizer import feature_dicts_to_matrix
from vscas.analyzer import compare_vectors


st.set_page_config(
    page_title="VSCAS | Code Similarity Analyzer",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 VSCAS")
st.subheader("Vector Space Based Source Code Similarity Analysis")

st.write(
    "Analyze source-code similarity using preprocessing, "
    "feature extraction, vectorization, cosine similarity, "
    "and hybrid similarity analysis."
)

st.sidebar.title("VSCAS")
st.sidebar.write("Source Code Similarity Analyzer")

st.sidebar.divider()

st.sidebar.subheader("Analysis Pipeline")

st.sidebar.write("1. Source Code Upload")
st.sidebar.write("2. Preprocessing")
st.sidebar.write("3. Tokenization")
st.sidebar.write("4. Feature Extraction")
st.sidebar.write("5. Vectorization")
st.sidebar.write("6. Similarity Analysis")
st.sidebar.write("7. Visualization")

st.sidebar.divider()

st.sidebar.subheader("Similarity Methods")

st.sidebar.write("Lexical Similarity")
st.sidebar.write("Structural Similarity")
st.sidebar.write("Hybrid Similarity")

st.sidebar.divider()

st.sidebar.caption(
    "VSCAS uses linear algebra and vector-space methods "
    "to analyze source-code similarity."
)

st.divider()

st.header("📂 Upload Source Code")

st.write(
    "Upload two or more source-code files to compare their similarity."
)

uploaded_files = st.file_uploader(
    "Choose source-code files",
    type=["py", "c", "cpp", "cc", "java"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.subheader("Selected Files")

    file_table = []

    for file in uploaded_files:
        language = detect_language(file.name)

        file_table.append(
            {
                "File": file.name,
                "Language": language,
                "Size": f"{file.size / 1024:.2f} KB",
            }
        )

    st.dataframe(
        pd.DataFrame(file_table),
        use_container_width=True,
        hide_index=True,
    )

if uploaded_files and len(uploaded_files) < 2:
    st.warning(
        "Please upload at least two source-code files to perform similarity analysis."
    )

if uploaded_files and len(uploaded_files) >= 2:
    st.success(
        f"{len(uploaded_files)} source-code files are ready for analysis."
    )

    st.divider()

    analyze_button = st.button(
        "🔍 Analyze Similarity",
        use_container_width=True,
        type="primary",
    )

    if analyze_button:
        file_data = []

        for file in uploaded_files:
            code = file.getvalue().decode("utf-8")
            language = detect_language(file.name)

            processed_code = preprocess_code(
                code,
                language,
            )

            tokens = tokenize(processed_code)

            normalized_tokens = normalize_identifiers(
                tokens,
                language,
            )

            features = extract_features(
                normalized_tokens
            )

            file_data.append(
                {
                    "name": file.name,
                    "language": language,
                    "features": features,
                }
            )

        lexical_features = [
            item["features"]["lexical"]
            for item in file_data
        ]

        lexical_matrix, lexical_vocabulary = (
            feature_dicts_to_matrix(
                lexical_features
            )
        )

        structural_vectors = [
            structural_dict_to_vector(
                {
                    "functions": item["features"]["structural"]["function_count"],
                    "loops": item["features"]["structural"]["loop_count"],
                    "conditions": item["features"]["structural"]["condition_count"],
                    "returns": item["features"]["structural"]["return_count"],
                    "classes": item["features"]["structural"]["class_count"],
                    "imports": item["features"]["structural"]["import_count"],
                    "operators": item["features"]["lexical"]["operator_count"],
                }
            )
            for item in file_data
        ]

        results = []

        for i in range(len(file_data)):
            for j in range(i + 1, len(file_data)):
                comparison = compare_vectors(
                    lexical_matrix[i],
                    lexical_matrix[j],
                    structural_vectors[i],
                    structural_vectors[j],
                )

                results.append(
                    {
                        "File 1": file_data[i]["name"],
                        "File 2": file_data[j]["name"],
                        "Lexical Similarity": comparison["lexical_similarity"],
                        "Structural Similarity": comparison["structural_similarity"],
                        "Hybrid Similarity": comparison["hybrid_similarity"],
                    }
                )

        results_df = pd.DataFrame(results)

        highest = results_df.loc[
            results_df["Hybrid Similarity"].idxmax()
        ]

        lowest = results_df.loc[
            results_df["Hybrid Similarity"].idxmin()
        ]

        st.divider()

        st.header("📊 Analysis Summary")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Files Analyzed",
                len(file_data),
            )

        with col2:
            st.metric(
                "Comparisons",
                len(results_df),
            )

        with col3:
            st.metric(
                "Highest Similarity",
                f"{highest['Hybrid Similarity'] * 100:.2f}%",
            )

        with col4:
            st.metric(
                "Lowest Similarity",
                f"{lowest['Hybrid Similarity'] * 100:.2f}%",
            )

        st.divider()

        st.header("📋 Similarity Results")

        display_df = results_df.copy()

        display_df[
            "Lexical Similarity"
        ] = display_df[
            "Lexical Similarity"
        ].map(
            lambda value: f"{value * 100:.2f}%"
        )

        display_df[
            "Structural Similarity"
        ] = display_df[
            "Structural Similarity"
        ].map(
            lambda value: f"{value * 100:.2f}%"
        )

        display_df[
            "Hybrid Similarity"
        ] = display_df[
            "Hybrid Similarity"
        ].map(
            lambda value: f"{value * 100:.2f}%"
        )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
        )

        st.divider()

        st.header("🧮 Similarity Matrix")

        file_names = [
            item["name"]
            for item in file_data
        ]

        similarity_matrix = np.eye(
            len(file_data)
        )

        for result in results:
            i = file_names.index(result["File 1"])
            j = file_names.index(result["File 2"])

            similarity_matrix[i][j] = result[
                "Hybrid Similarity"
            ]

            similarity_matrix[j][i] = result[
                "Hybrid Similarity"
            ]

        matrix_df = pd.DataFrame(
            similarity_matrix,
            index=file_names,
            columns=file_names,
        )

        st.dataframe(
            matrix_df.style.format(
                lambda value: f"{value * 100:.2f}%"
            ).background_gradient(
                cmap="Blues"
            ),
            use_container_width=True,
        )

        st.divider()

        st.header("🔥 Similarity Heatmap")

        st.write(
            "Higher similarity values are represented by darker cells."
        )

        heatmap_df = matrix_df.copy()

        heatmap_df = heatmap_df.style.background_gradient(
            cmap="Blues"
        ).format(
            lambda value: f"{value * 100:.2f}%"
        )

        st.dataframe(
            heatmap_df,
            use_container_width=True,
        )

        st.divider()

        st.header("🏆 Similarity Insights")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Most Similar Pair")

            st.write(
                f"**{highest['File 1']} ↔ {highest['File 2']}**"
            )

            st.metric(
                "Hybrid Similarity",
                f"{highest['Hybrid Similarity'] * 100:.2f}%",
            )

        with col2:
            st.subheader("Least Similar Pair")

            st.write(
                f"**{lowest['File 1']} ↔ {lowest['File 2']}**"
            )

            st.metric(
                "Hybrid Similarity",
                f"{lowest['Hybrid Similarity'] * 100:.2f}%",
            )

        st.divider()

        st.header("ℹ️ Understanding the Scores")

        explanation_col1, explanation_col2, explanation_col3 = st.columns(
            3
        )

        with explanation_col1:
            st.subheader("Lexical Similarity")
            st.write(
                "Measures similarity between the extracted lexical features "
                "of the source-code files."
            )

        with explanation_col2:
            st.subheader("Structural Similarity")
            st.write(
                "Measures similarity between structural characteristics "
                "such as functions, loops, conditions, and returns."
            )

        with explanation_col3:
            st.subheader("Hybrid Similarity")
            st.write(
                "Combines lexical and structural similarity into a final "
                "similarity score."
            )