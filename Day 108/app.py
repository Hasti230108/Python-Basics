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
st.markdown(
    "### Intelligent SMS Spam Detection"
)
st.caption(
    "A Machine Learning application powered by "
    "TF-IDF and Multinomial Naive Bayes."
)
st.divider()
st.subheader("SMS Spam Detection")

samples = {
    "Choose a sample message": "",
    "Promotional message": (
        "Congratulations! You have won a free prize. "
        "Claim your reward now!"
    ),
    "Normal conversation": (
        "Hey, are we meeting tomorrow?"
    ),
    "Bank notification": (
        "Your account has been credited successfully."
    )
}

st.write(
    "Check whether a SMS message is legitimate "
    "or potentially spam using Machine Learning."
)
    
selected_sample = st.selectbox(
    "Try an example:",
    list(samples.keys())
)
sample_text = samples[selected_sample]

if not MODEL_PATH.exists():
    st.error(
        "Model file not found! "
        "Run train_model.py first to create it."
    )
    st.stop()

model, vectorizer = load_spamshield()

# Message input
message = st.text_area(
    "Enter your SMS message",
    value=sample_text,
    placeholder="Paste your SMS message here...",
    height=160,
    key=f"message_{selected_sample}"
)

# Submit button
submitted = st.button(
    "🔍 Analyse Message",
    type="primary",
    use_container_width=True
)

# Prediction
if submitted:

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
            st.error(
                "🚨 SPAM DETECTED\n\n"
                "The model classified this message as spam."
            )
        else:
            st.success(
                "✅ HAM DETECTED\n\n"
                "The model classified this message as legitimate."
            )

        st.markdown("#### Spam Probability")

        st.progress(float(spam_probability))

        st.metric(
            "Probability",
            f"{spam_probability * 100:.2f}%"
        )

        st.caption(
            "This probability is the model's estimated "
            "spam score, not a guarantee of message safety."
        )

st.divider()

with st.expander("ℹ️ About SpamShield"):

    st.write(
        "SpamShield is a beginner-friendly Machine Learning "
        "project that classifies SMS messages as ham or spam."
    )

    st.write("**Model:** Multinomial Naive Bayes")
    st.write("**Feature Extraction:** TF-IDF")
    st.write("**Dataset:** SMS Spam Collection")
    st.write("**Interface:** Streamlit")

    st.caption(
        "Predictions depend on patterns learned from the "
        "training dataset. Always use your judgement."
    )

st.caption("Built with Python & Machine Learning | Day 108")
