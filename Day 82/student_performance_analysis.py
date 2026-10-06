import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    "Students": ["Hasti", "Mahek", "Siddh", "Nehal", "Kriish", "Risha", "Aayushi", "Pratik"],
    "Math": [93, 85, 78, 82, 88, 95, 80, 85],
    "Python": [88, 92, 80, 85, 90, 87, 71, 78],
    "DBMS": [89, 90, 85, 88, 92, 91, 84, 86],
    "Study Hours": [5, 6, 4, 5, 7, 6, 3, 4]
}

df = pd.DataFrame(data)

print(df)

math_average = np.mean(df["Math"])
python_average = np.mean(df["Python"])
dbms_average = np.mean(df["DBMS"])

print("\nSubject Averages:")
print("Math:", math_average)
print("Python:", python_average)
print("DBMS:", dbms_average)

subjects = ["Math", "Python", "DBMS"]
averages = [math_average, python_average, dbms_average]

plt.bar(subjects, averages)
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject Average Performance")
plt.show()

