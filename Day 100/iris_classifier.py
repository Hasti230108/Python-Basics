from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model():
    iris = load_iris(as_frame=True)

    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return model, iris, accuracy


def predict_species(model, iris, measurements):
    prediction = model.predict(measurements)[0]
    probabilities = model.predict_proba(measurements)[0]

    species = iris.target_names[prediction]
    confidence = probabilities[prediction]

    return species, confidence, probabilities


if __name__ == "__main__":
    model, iris, accuracy = train_model()

    print("Iris dataset shape:", iris.data.shape)
    print("Training samples:", 120)
    print("Testing samples:", 30)
    print("Model accuracy:", round(accuracy * 100, 2), "%")

    sample = iris.data.iloc[[0]]
    species, confidence, _ = predict_species(
        model, iris, sample
    )

    print("Sample prediction:", species)
