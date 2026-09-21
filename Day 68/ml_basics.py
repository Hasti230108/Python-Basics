import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "age": [62, 24, 35, 19, 51, 70, 28, 45],
    "heart_rate": [118, 78, 105, 82, 110, 125, 85, 102],
    "injury": [1, 0, 1, 0, 1, 1, 0, 1],
    "priority": ["Critical", "Low", "High", "Low", "High", "Critical", "Low", "High"]
}

df = pd.DataFrame(data)

encoder= LabelEncoder()

y_encoded = encoder.fit_transform(df["priority"])

print("\nEncoded Target:")
print(y_encoded)

print("\nClasses:")
print(encoder.classes_)

print("\nOriginal Target:")
print(df["priority"].values)

print("\nEncoded Target:")
print(y_encoded)

x = df[["age", "heart_rate", "injury"]]
y = y_encoded

print("\nFinal Features:")
print(x)

print("\nFinal Target:")
print(y)