
from sklearn.tree import DecisionTreeClassifier

# Examples: [hours studied]
X = [[1], [2], [3], [4], [5], [6]]

# Labels: 0 = Needs practice, 1 = Ready
y = [0, 0, 0, 1, 1, 1]

# Create the model
model = DecisionTreeClassifier(random_state=42)

# Let the model learn from examples
model.fit(X, y)

# Ask it to predict for a new example
result = model.predict([[5]])

print("Prediction:", result[0])
