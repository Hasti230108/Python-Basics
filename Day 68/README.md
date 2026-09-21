# Day 68 — Machine Learning Basics 

Today I started learning **Machine Learning** and prepared a dataset for model training.

The main focus was understanding **features, targets, and label encoding**.

## Topics Covered

* Introduction to Machine Learning
* Features (`X`)
* Target (`y`)
* Dataset creation using Pandas
* `LabelEncoder`
* Categorical to numerical conversion
* Basic ML data preparation

## Dataset

The dataset contains emergency-related information:

* `age`
* `heart_rate`
* `injury`
* `priority`

Here, `age`, `heart_rate`, and `injury` are the **features**, while `priority` is the **target**.

## Features and Target

```python
x = df[["age", "heart_rate", "injury"]]
y = df["priority"]
```

The features are the information given to the ML model, while the target is what the model will eventually learn to predict.

## Label Encoding

Since the priority values are text:

```text
Critical
High
Low
```

I used `LabelEncoder` to convert them into numerical values:

```text
Critical → 0
High     → 1
Low      → 2
```

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(df["priority"])
```

## ML Preparation Flow

```text
Dataset
   ↓
Features + Target
   ↓
Label Encoding
   ↓
Numerical Target
   ↓
Ready for ML Model
```

## Key Takeaway

I learned that **features are the input information given to a model, while the target is the value the model tries to predict.**

I also learned why categorical target values may need to be converted into numerical values before using them with ML algorithms.

## Technologies Used

* Python
* Pandas
* Scikit-learn