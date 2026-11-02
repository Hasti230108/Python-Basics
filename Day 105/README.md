# Day 105 — SpamShield: First Machine Learning Model

Today I trained my first machine-learning model for **SpamShield — SMS Spam Detection** using Python and Scikit-learn.

I used TF-IDF for text feature extraction and the Multinomial Naive Bayes algorithm to classify SMS messages as **spam** or **ham**.

## Topics Covered

- Train-test splitting
- `train_test_split()`
- Stratified sampling
- TF-IDF feature extraction
- Multinomial Naive Bayes
- Model training using `fit()`
- Predictions using `predict()`
- Model accuracy
- Precision, Recall and F1-score
- Classification report

## 1. Dataset Preparation

**Dataset:** SMS Spam Collection

- Total messages: 5,572
- Training messages: 4,457
- Testing messages: 1,115
- Test size: 20%
- Random state: 42
- Stratification: Enabled

I divided the dataset into training and testing sets so the model could be evaluated on messages it had not seen during training.

## 2. TF-IDF Feature Extraction

I used `TfidfVectorizer()` to convert SMS messages into numerical features.

- Vocabulary size: 7,668 features
- Training messages were used to learn the vocabulary.
- Testing messages were transformed using the same fitted vectorizer.

## 3. Model Training

**Algorithm:** Multinomial Naive Bayes

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
```

The `fit()` method trained the classifier using the TF-IDF features and their corresponding labels.

I then used `predict()` to classify the test messages.

## 4. Model Performance

<escape>**Accuracy: 96.05%**</escape>

### Classification Report

| Metric | Ham | Spam |
|---|---:|---:|
| Precision | 0.96 | 1.00 |
| Recall | 1.00 | 0.70 |
| F1-score | 0.98 | 0.83 |
| Support | 966 | 149 |

### Understanding the Results

- **Precision:** Measures how many predicted messages of a class were actually from that class.
- **Recall:** Measures how many actual messages of a class were correctly identified.
- **F1-score:** Combines precision and recall into one metric.

### Important Observation

Although the model achieved 96.05% accuracy, its spam recall was only 0.70.

This means the model missed some actual spam messages, even though its spam precision was 1.00 (rounded).

This gives us an area to investigate and improve in the next session.

## Key Takeaways

> TF-IDF converts text messages into numerical features.

> `train_test_split()` separates data for training and testing.

> `MultinomialNB` can be used for text classification.

> `fit()` trains the model, while `predict()` generates predictions.

> Accuracy alone is not enough to understand model performance.

> Precision, recall and F1-score provide additional insights.