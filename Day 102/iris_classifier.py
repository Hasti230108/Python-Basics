from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier

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
    
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions, labels=[0, 1, 2])
    report = classification_report(
        y_test, predictions, target_names=iris.target_names
    )    

    knn_predictions = knn_model.predict(X_test)
    knn_accuracy = accuracy_score(y_test, knn_predictions)
    
    return model, iris, accuracy, cm, report, knn_model, knn_accuracy


def predict_species(model, iris, measurements):
    prediction = model.predict(measurements)[0]
    probabilities = model.predict_proba(measurements)[0]

    species = iris.target_names[prediction]
    confidence = probabilities[prediction]

    return species, confidence, probabilities


if __name__ == "__main__":
    model, iris, accuracy, cm, report, knn_model, knn_accuracy = train_model()

    print("Iris dataset shape:", iris.data.shape)
    print("Training samples:", 120)
    print("Testing samples:", 30)
    print("Model accuracy:", round(accuracy * 100, 2), "%")
    print("Confusion Matrix:")
    print(cm)
    print("Classification Report:")
    print(report)
    print("Random Forest accuracy:", f"{accuracy:.1%}")
    print("KNN accuracy:", f"{knn_accuracy:.1%}")

    sample = iris.data.iloc[[0]]
    species, confidence, _ = predict_species(
        model, iris, sample
    )

    print("Sample prediction:", species)
