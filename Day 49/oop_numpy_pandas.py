import numpy as np
import pandas as pd

class StudentAnalyzer:
    def __init__(self, names, marks):
        self.names = names
        self.marks = np.array(marks)

    def show_data(self):
        df = pd.DataFrame({"Names": self.names, "Marks": self.marks})
        print(df)

    def average_mark(self):
        return np.mean(self.marks)

    def highest_marks(self):
        return np.max(self.marks)

    def lowest_marks(self):
        return np.min(self.marks)

    def above_average(self):
        avg = self.average_mark()
        df = pd.DataFrame({
            "Names": self.names,
            "Marks": self.marks
        })
        print(df[df["Marks"] > avg])

    def add_result(self):
        df = pd.DataFrame({
            "Names": self.names, "Marks": self.marks
        })
        df["Result"] = np.where(df["Marks"] >= 80, "Pass", "Fail")
        print(df)

names = ["Hasti", "Elia", "Tahseen", "Twinkle", "Rahul"]
marks = [86, 92, 75, 88, 90]

analyzer = StudentAnalyzer(names, marks)
analyzer.show_data()
print("Average Mark:", analyzer.average_mark())
print("Highest Mark:", analyzer.highest_marks())
print("Lowest Mark:", analyzer.lowest_marks())
print("\nStudents Above Average:")
analyzer.above_average()
print("\nStudents with Result:")
analyzer.add_result()