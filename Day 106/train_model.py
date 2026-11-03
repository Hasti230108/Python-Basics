from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "SMSSpamCollection"

df = pd.read_csv(
    DATA_PATH,
    sep="\t",
    header=None,
    names=["label", "message"]
)

X = df["message"]
y = df["label"]

X_train_full, X_test, y_train_full, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_full,
    y_train_full,
    test_size=0.25,
    random_state=42,
    stratify=y_train_full
)

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_val_tfidf = vectorizer.transform(X_val)
X_test_tfidf = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

predictions = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, predictions)

print("===== SPAMSHIELD MODEL RESULTS =====")
print("Training messages:", len(X_train))
print("Testing messages:", len(X_test))
print("Vocabulary size:", len(vectorizer.get_feature_names_out()))
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\n===== CLASSIFICATION REPORT =====")
print(classification_report(y_test, predictions))

predictions = model.predict(X_test_tfidf)
cm = confusion_matrix(
    y_test,
    predictions,
    labels=["ham", "spam"]
)

print("\n===== CONFUSION MATRIX =====")
print(cm)

results = pd.DataFrame({
    "Message": X_test.values,
    "Actual": y_test.values,
    "Predicted": predictions
})

mistakes = results[
    results["Actual"] != results["Predicted"]
]

print("\n===== TOTAL MISCLASSIFICATIONS =====")
print(len(mistakes))

print("\n===== MISSED SPAM MESSAGES =====")
print(
    mistakes[mistakes["Actual"] == "spam"].head(10)
)

print("\n===== LEGITIMATE MESSAGES FLAGGED AS SPAM =====")
print(
    mistakes[mistakes["Actual"] == "ham"].head(10)
)


spam_index = list(model.classes_).index("spam")

spam_probabilities = model.predict_proba(
    X_test_tfidf
)[:, spam_index]

results["Spam Probability"] = spam_probabilities

false_negatives = results[
    (results["Actual"] == "spam") &
    (results["Predicted"] == "ham")
]

print("\n===== MISSED SPAM CONFIDENCE =====")
print(
    false_negatives[
        ["Spam Probability"]
    ].describe()
)

print("\n===== MISSED SPAM: HIGHEST SPAM PROBABILITY =====")

print(
    false_negatives
    .sort_values(
        by="Spam Probability",
        ascending=False
    )
    [["Message", "Spam Probability"]]
    .head(10)
    .to_string(index=False)
)