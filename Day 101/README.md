# 🌸 Day 101 — Iris Flower AI Classifier: Model Evaluation

Today, I continued my **Iris Flower AI Classifier** project by adding model evaluation features using Python and scikit-learn.

The application now predicts Iris flower species and displays the model's test accuracy, confusion matrix, and classification report through Streamlit.

## Project Objectives

- Evaluate a machine learning classification model.
- Calculate test accuracy.
- Generate a confusion matrix.
- Display a classification report.
- Understand how well the model predicts different Iris species.
- Present evaluation results in a Streamlit web application.

## Technologies Used

- Python
- Pandas
- scikit-learn
- Streamlit

## Project Structure

```text
Day 101/
├── __pycache__/
├── iris_classifier.py
├── app.py
├── README.md
└── .gitignore
```

`__pycache__/` is a Python-generated cache folder and should be excluded from Git using `.gitignore`.

## Concepts Practiced

### 1. Model Accuracy

Used `accuracy_score()` to calculate the proportion of correct predictions on the test dataset.

**Test accuracy: 90%**

The model correctly classified 27 out of 30 test samples.

### 2. Confusion Matrix

Used `confusion_matrix()` to compare actual species with predicted species.

The matrix helps identify correct predictions and cases where the model confuses one species with another.

### 3. Classification Report

Used `classification_report()` to display:

- **Precision:** How often predictions for a class are correct.
- **Recall:** How many actual samples of a class are identified.
- **F1-score:** A combined measure of precision and recall.
- **Support:** Number of actual test samples in each class.

### 4. Streamlit Integration

Displayed the confusion matrix and classification report directly in the web application using `st.dataframe()` and `st.code()`.

## Model Evaluation Results

| Metric | Result |
|---|---:|
| Total dataset samples | 150 |
| Training samples | 120 |
| Testing samples | 30 |
| Test accuracy | 90% |
| Correct predictions | 27 |
| Incorrect predictions | 3 |

The model classified all 10 Setosa test samples correctly. It made some mistakes distinguishing Versicolor and Virginica.

*Note: Results are based on the current train-test split and model configuration.*

## Files Explained

- `iris_classifier.py` — Loads the Iris dataset, trains the Random Forest model, generates evaluation metrics, and predicts flower species.
- `app.py` — Provides an interactive Streamlit interface with measurement sliders, species predictions, probability estimates, a confusion matrix, and a classification report.
- `.gitignore` — Excludes Python cache files and other specified files from Git tracking.

## Key Takeaways

- A trained model should be evaluated on test data.
- Accuracy provides an overall measure of correct predictions.
- A confusion matrix reveals which classes are being confused.
- A classification report provides class-specific evaluation metrics.
- Streamlit can display machine learning results interactively.