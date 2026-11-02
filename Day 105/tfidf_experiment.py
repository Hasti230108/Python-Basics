from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

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

vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

print("Dataset messages:", len(X))
print("Vocabulary size:", len(vectorizer.get_feature_names_out()))
print("TF-IDF matrix shape:", X_tfidf.shape)
print("First 10 words:", vectorizer.get_feature_names_out()[:10])