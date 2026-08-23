import numpy as np

marks = np.array([72, 91, 65, 88, 54, 79, 96, 43, 81, 69])

print(f"Original marks: {marks}")

print(f"Sorted marks: {np.sort(marks)}")

print(f"Highest Marks: {np.max(marks)}")

print(f"Lowest Marks: {np.min(marks)}")

print(f"Average Marks: {np.mean(marks)}")

print(f"Standard deviation: {np.std(marks)}")

print(f"Position of highest marks: {np.argmax(marks)}")

print(f"Position of lowest marks: {np.argmin(marks)}")

print(f"Students above 80: {marks[marks > 80]}")

print(f"Number of students who scored above 80: {np.sum(marks > 80)}")

print(f"Students who passed passed >= 50: {marks[marks >= 50]}")

print(f"Number of stuents who passed: {np.sum(marks >= 50)}")

print(f"Students who failed: {marks[marks < 50]}")

print(f"Number of student who failed: {np.sum(marks < 50)}")

print(f"Marks betweem 40 and 90: {marks[(marks >= 40) & (marks <= 90)]}")

bonus = np.array([5, 0, 10, 5, 8, 0, 12, 3, 4, 6])
final_marks = marks + bonus
print(f"Bonus marks added: {np.minimum(final_marks, 100)}")

passed = np.sum(marks >= 50)
total_students = len(marks)
percentage = (passed / total_students) * 100
print(f"Percentage of students passed: {percentage}%")