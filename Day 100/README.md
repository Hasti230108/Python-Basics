# Day 100 — Iris Flower AI Classifier

A beginner-friendly Machine Learning mini-project built using Python, scikit-learn, Pandas, and Streamlit.

The application predicts the species of an Iris flower using four measurements: sepal length, sepal width, petal length, and petal width.

## Project Objective

The goal of this project is to understand the basic Machine Learning workflow and build an interactive application that uses a trained model to make predictions.

## Technologies Used

- **Python** — Main programming language
- **scikit-learn** — Dataset loading, model training, prediction, and evaluation
- **Pandas** — Handling flower measurements in DataFrames
- **Streamlit** — Building the interactive web application

## Dataset

This project uses the built-in Iris dataset provided by scikit-learn.

- **Total samples:** 150
- **Input features:** 4
- **Species classes:** 3

The three species are:
- Iris setosa
- Iris versicolor
- Iris virginica

### Input Features

1. Sepal length (cm)
2. Sepal width (cm)
3. Petal length (cm)
4. Petal width (cm)

## Project Structure

```text
Day 100/
├── __pycache__/              # Generated Python cache files
├── ml_first_experiment.py    # First scikit-learn experiment
├── iris_classifier.py       # Model training and prediction functions
├── app.py                   # Streamlit user interface
├── README.md                # Project documentation
└── .gitignore               # Files Git should ignore
```

## How It Works

1. Load the Iris dataset using `load_iris()`.
2. Separate the measurements (`X`) from the species labels (`y`).
3. Split the dataset into training and testing sets.
4. Train a `RandomForestClassifier`.
5. Evaluate the model using accuracy.
6. Accept flower measurements through Streamlit sliders.
7. Predict the flower species and display the model's estimated probabilities.

## Main Files

### `ml_first_experiment.py`

A small experiment created to understand the basic scikit-learn methods `fit()` and `predict()`.

### `iris_classifier.py`

Contains reusable functions:
- `train_model()` — Loads the data, trains the model, and evaluates its accuracy.
- `predict_species()` — Predicts the species and returns the model's estimated probabilities.

The testing code runs when this file is executed directly. Importing it into another file does not automatically run the testing section.

### `app.py`

Creates the interactive Streamlit application with:
- Four measurement sliders
- Dataset sample count
- Model test accuracy
- Species prediction
- Probability bar chart

The trained model is cached with `st.cache_resource` to avoid retraining it on every interaction.

## Model Evaluation

The model is evaluated on a held-out test set containing 30 samples, while 120 samples are used for training.

The test accuracy is calculated using `accuracy_score()`. The actual result can vary if the model or dataset split changes.

The model's estimated probabilities are not guarantees that a prediction is correct.

## Concepts Learned

- Built-in datasets in scikit-learn
- Features and target labels
- Training and testing data
- `train_test_split()`
- `RandomForestClassifier`
- `fit()` and `predict()`
- Model accuracy
- Reusable Python modules and imports
- Streamlit widgets and charts
- Caching a trained model with `st.cache_resource`

## Limitations

This is an educational project using a small, well-known dataset. Its results should not be treated as a guarantee of accuracy on every real-world flower.