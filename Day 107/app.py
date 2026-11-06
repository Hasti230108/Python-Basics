
from pathlib import Path

import joblib
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "spamshield_model.pkl"

@st.cache_resource
def load_spamshield():
    saved_objects = joblib.load(MODEL_PATH)

    model = saved_objects["model"]
    vectorizer = saved_objects["vectorizer"]

    return model, vectorizer

st.set_page_config(
    page_title="SpamShield",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ SpamShield")
st.subheader("SMS Spam Detection")
st.write(
    "Check whether a SMS message is legitimate "
    "or potentially spam using Machine Learning."
)

if not MODEL_PATH.exists():
    st.error(
        "Model file not found! "
        "Run train_model.py first to create it."
    )
    st.stop()

model, vectorizer = load_spamshield()

# Message input
with st.form("spam_detection_form"):

    message = st.text_area(
        "Enter your SMS message:",
        placeholder="Type or paste your message here...",
        height=150
    )

    check_message = st.form_submit_button(
        "🔍 Check Message",
        width="stretch"
    )

# Prediction
if check_message:

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        # Convert message into TF-IDF features
        message_tfidf = vectorizer.transform([message])

        # Predict message category
        prediction = model.predict(message_tfidf)[0]

        # Get spam probability
        spam_index = list(model.classes_).index("spam")

        spam_probability = model.predict_proba(
            message_tfidf
        )[0][spam_index]

        st.divider()

        st.subheader("Prediction Result")

        if prediction == "spam":
            st.error("🚨 This message is classified as SPAM.")
        else:
            st.success("✅ This message is classified as HAM.")

        st.metric(
            "Spam Probability",
            f"{spam_probability * 100:.2f}%"
        )
