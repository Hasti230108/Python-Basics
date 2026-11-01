# Day 104 — SpamShield: TF-IDF Text Feature Extraction

Today I explored **TF-IDF (Term Frequency–Inverse Document Frequency)** using Python and Scikit-learn as part of my SpamShield SMS Spam Detection project.

TF-IDF converts text messages into numerical features so machine-learning models can process and learn from text.

## Topics Covered

- Introduction to Natural Language Processing (NLP)
- What is TF-IDF?
- Term Frequency (TF)
- Inverse Document Frequency (IDF)
- Using `TfidfVectorizer`
- Converting text into numerical features
- Understanding vocabulary and feature matrices
- Loading a real SMS dataset
- Understanding matrix shape and vocabulary size

## 1. What Is TF-IDF?

TF-IDF stands for **Term Frequency–Inverse Document Frequency**.

It assigns weights to words based on their occurrence in a message and how common those words are across a collection of messages.

This helps represent text numerically for machine-learning tasks.

## 2. Sample Text Experiment

I first tested TF-IDF using three sample messages:

```python
messages = [
    "win free prize",
    "meeting tomorrow",
    "win a free ticket"
]
```

Using `TfidfVectorizer()`, I converted these messages into a numerical matrix.

### Output

- Messages: `3`
- Vocabulary features: `6`
- Matrix shape: `(3, 6)`

Each row represents a message, and each column represents a word feature.

## 3. TF-IDF on the Real SMS Dataset

I then applied TF-IDF to the SMS Spam Collection dataset.

### Dataset Details

| Metric | Result |
|---|---:|
| Total messages | 5,572 |
| Vocabulary features | 8,713 |
| TF-IDF matrix shape | `(5572, 8713)` |

The vectorizer learned a vocabulary of 8,713 features from the messages.

Each SMS is represented by a numerical feature vector that can later be used to train a spam classification model.

## 4. Important Functions Used

- `TfidfVectorizer()` — creates a TF-IDF text vectorizer.
- `fit_transform()` — learns the vocabulary and converts text into numerical features.
- `transform()` — converts new text using an already-fitted vectorizer.
- `get_feature_names_out()` — retrieves the learned vocabulary.
- `X_tfidf.shape` — displays the number of messages and features.

## Files Created

```text
Day 104/
├── data/
│   └── SMSSpamCollection
├── explore_dataset.py
├── tfidf_experiment.py
└── README.md
```

### File Descriptions

- `explore_dataset.py` — explores the SMS dataset, labels, missing values, and duplicates.
- `tfidf_experiment.py` — experiments with TF-IDF using sample messages and the real dataset.
- `data/SMSSpamCollection` — contains the SMS Spam Collection dataset.

## Key Takeaways

> TF-IDF converts text into numerical features.

> Each row in the feature matrix represents one message.

> Each column represents a vocabulary feature.

> The matrix shape `(5572, 8713)` means 5,572 messages and 8,713 features.

> The resulting features can be used to train machine-learning models for spam detection.