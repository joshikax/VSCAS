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
    page_title="VSCAS",
    page_icon="📊",
    layout="wide",
)

st.title("VSCAS")
st.subheader("Vector Space Based Source Code Similarity Analysis")

st.write(
    "Analyze source-code similarity using preprocessing, "
    "feature extraction, vectorization, cosine similarity, "
    "and hybrid similarity."
)

st.divider()

st.header("Upload Source Code")

uploaded_files = st.file_uploader(
    "Choose source-code files",
    type=["py", "c", "cpp", "cc", "java"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.subheader("Selected Files")

    for file in uploaded_files:
        language = detect_language(file.name)
        st.write(f"📄 **{file.name}** — {language}")

if uploaded_files and len(uploaded_files) < 2:
    st.warning("Please upload at least two source-code files.")

if uploaded_files and len(uploaded_files) >= 2:
    st.divider()

    if st.button("🔍 Analyze Similarity", use_container_width=True):
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

        st.divider()

        st.header("Analysis Summary")

        highest = results_df.loc[
            results_df["Hybrid Similarity"].idxmax()
        ]

        lowest = results_df.loc[
            results_df["Hybrid Similarity"].idxmin()
        ]

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
                f"{highest['Hybrid Similarity']:.4f}",
            )

        with col4:
            st.metric(
                "Lowest Similarity",
                f"{lowest['Hybrid Similarity']:.4f}",
            )

        st.divider()

        st.header("Similarity Results")

        display_df = results_df.copy()

        for column in [
            "Lexical Similarity",
            "Structural Similarity",
            "Hybrid Similarity",
        ]:
            display_df[column] = display_df[column].map(
                lambda value: f"{value:.4f}"
            )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
        )

        st.divider()

        st.header("Similarity Matrix")

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
            matrix_df.style.format("{:.4f}"),
            use_container_width=True,
        )

        st.divider()

        st.header("Similarity Heatmap")

        st.write(
            "Darker cells indicate higher similarity."
        )

        st.dataframe(
            matrix_df.style.background_gradient(
                cmap="Blues"
            ).format("{:.4f}"),
            use_container_width=True,
        )

        st.divider()

        st.header("Similarity Insights")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🏆 Highest Similarity")
            st.write(
                f"**{highest['File 1']} ↔ {highest['File 2']}**"
            )
            st.metric(
                "Hybrid Similarity",
                f"{highest['Hybrid Similarity']:.4f}",
            )

        with col2:
            st.subheader("Lowest Similarity")
            st.write(
                f"**{lowest['File 1']} ↔ {lowest['File 2']}**"
            )
            st.metric(
                "Hybrid Similarity",
                f"{lowest['Hybrid Similarity']:.4f}",
            )