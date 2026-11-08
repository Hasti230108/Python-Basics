from pathlib import Path
import pandas as pd

# Find the folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "SMSSpamCollection"

print("Looking for dataset at:", DATA_PATH)
print("Dataset exists:", DATA_PATH.exists())

df = pd.read_csv(
    DATA_PATH,
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8"
)

print("===== SPAMSHIELD DATASET =====")
print("Dataset shape:", df.shape)

print("\n===== FIRST 5 MESSAGES =====")
print(df.head())

print("\n===== LABEL COUNTS =====")
print(df["label"].value_counts())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== EXAMPLE SPAM MESSAGES =====")
print(df[df["label"] == "spam"]["message"].head(3))

print("\n===== LABEL PERCENTAGES =====")
print((df["label"].value_counts(normalize=True) * 100).round(2))

print("\n===== DUPLICATE MESSAGES =====")
print("Duplicate rows:", df.duplicated().sum())

print("\n===== DUPLICATE LABEL CHECK =====")

label_counts = df.groupby("message")["label"].nunique()
conflicting_messages = label_counts[label_counts > 1]

print("Messages with conflicting labels:", len(conflicting_messages))