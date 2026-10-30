# Day 102 — Iris AI Classifier: Model Comparison

Today, I upgraded my Iris Flower AI Classifier by adding a second machine learning model, **K-Nearest Neighbors (KNN)**, and comparing its accuracy with the existing Random Forest model.

Both models use the same training and testing datasets for an initial comparison.

## Objectives

- Add the KNN classification algorithm.
- Train two machine learning models on the Iris dataset.
- Evaluate both models using test accuracy.
- Display their accuracy side by side in Streamlit.
- Practice comparing machine learning models.

## Technologies Used

- Python
- Pandas
- scikit-learn
- Streamlit

## Models Used

### 1. Random Forest Classifier

Random Forest combines predictions from multiple decision trees to classify a flower.

### 2. K-Nearest Neighbors (KNN)

KNN predicts a flower's species by considering the labels of its nearest training samples.

In this project, KNN uses `n_neighbors=5`, meaning it considers five neighboring samples when making a prediction.

## Workflow

1. Load the Iris dataset using `load_iris()`.
2. Separate the flower measurements (`X`) from the species labels (`y`).
3. Split the dataset into training and testing sets.
4. Train the Random Forest model.
5. Train the KNN model.
6. Calculate test accuracy for both models.
7. Display the results in the Streamlit application.

## Model Comparison

| Model | Evaluation Metric |
|---|---|
| Random Forest | Test accuracy |
| K-Nearest Neighbors (KNN) | Test accuracy |

The application displays both accuracy values side by side, making it easy to compare their performance on the selected test dataset.

**Actual results:** Record the Random Forest and KNN accuracy values after running the application.

## Project Files

- `iris_classifier.py` — Loads the dataset, trains both models, calculates evaluation metrics, and predicts Iris species.
- `app.py` — Provides an interactive interface for flower prediction, model evaluation, and accuracy comparison.
- `README.md` — Documents the project and daily progress.
- `.gitignore` — Excludes Python cache files and other configured files from Git tracking.

## Key Takeaways

- Different machine learning algorithms can solve the same classification problem.
- Both models can be evaluated using the same test dataset.
- Accuracy measures the proportion of correct predictions.
- Model performance can vary depending on the algorithm and its settings.
- Streamlit can present model comparison results interactively.