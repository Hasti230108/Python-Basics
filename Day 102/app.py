import streamlit as st
import pandas as pd

from iris_classifier import train_model, predict_species

st.set_page_config(
    page_title="Iris AI Classifier",
    page_icon="🌸",
    layout="wide"
)

@st.cache_resource
def get_model():
    return train_model()

model, iris, accuracy, cm, report, knn_model, knn_accuracy = get_model()

st.title("🌸 Iris Flower AI Classifier")
st.write("Explore flower measurements and predict an Iris species.")

st.info("Adjust the four measurements, then predict the flower species.")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.1)
    sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.5)

with col2:
    petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.4)
    petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 0.2)

col1, col2 = st.columns(2)
col1.metric("Dataset Samples", len(iris.data))
col2.metric("Test Accuracy", f"{accuracy:.1%}")

if st.button("🌼 Predict Species", type="primary"):
    measurements = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=iris.feature_names
    )

    species, confidence, probabilities = predict_species(
        model, iris, measurements
    )

    st.success(f"Predicted species: Iris {species.title()}")
    st.write(f"Model probability for this prediction: {confidence:.1%}")

    chart = pd.DataFrame({
        "Species": iris.target_names,
        "Probability": probabilities
    }).set_index("Species")

    st.bar_chart(chart)

st.subheader("📊 Confusion Matrix")

st.write(
    "Rows = actual species; columns = predicted species."
)

st.dataframe(
    pd.DataFrame(
        cm,
        index=iris.target_names,
        columns=iris.target_names
    )
)

st.subheader("📋 Classification Report")
st.code(report)

st.subheader("🤖 Model Comparison")

col1, col2 = st.columns(2)

col1.metric("Random Forest Accuracy", f"{accuracy:.1%}")
col2.metric("KNN Accuracy", f"{knn_accuracy:.1%}")

st.caption("Day 102 | Python • Pandas • scikit-learn • Streamlit")
