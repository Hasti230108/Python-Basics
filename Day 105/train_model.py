from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
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