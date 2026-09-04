import numpy as np
import pandas as pd

class StudentPerformanceAnalyzer:
    def __init__(self, names, marks):
        self.names = names
        self.marks = np.array(marks)

    def show_students(self):
        df = pd.DataFrame({
            "Name": self.names,
            "Marks": self.marks
        })
        print(df)

    def average_marks(self):
        print(f"Average Marks: {np.mean(self.marks)}")

    def highest_marks(self):
        print(f"Highest Marks: {np.max(self.marks)}")

    def lowest_marks(self):
        print(f"Lowest Marks: {np.min(self.marks)}")

    def performance_level(self):
        df = pd.DataFrame({
            "Name": self.names,
            "Marks": self.marks,
            "Performance Level": np.where(
                self.marks >= 90, "Excellent",
                np.where(self.marks >= 75, "Good", "Needs Improvement")
            )
        })
        print(df)

    def above_average_students(self):
        avg = np.mean(self.marks)
        above_avg = np.array(self.names)[self.marks > avg]
        print("\nStudents with above-average marks:")
        for name in above_avg:
            print(name)

names = [
    "Hasti",
    "Tinker",
    "Amisha",
    "Sahima",
    "Tanisha",
    "Mridula"
]

marks = [
    86,
    92,
    68,
    88,
    74,
    96
]

analyze = StudentPerformanceAnalyzer(names, marks)
analyze.show_students()
analyze.average_marks()
analyze.highest_marks()
analyze.lowest_marks()
analyze.performance_level()
analyze.above_average_students()