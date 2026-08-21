import numpy as np

rng = np.random.default_rng(42)

uniform_data = rng.uniform(0, 1, size=10)

print(f"Uniform data: {uniform_data}")

uniform_marks = rng.uniform(50, 100, size=10)

print(f"\nRandom marks: {uniform_marks}")

print(f"Mean: {np.mean(uniform_marks)}")
print(f"Standard deviation: {np.std(uniform_marks)}") 

normal_data = rng.normal(70, 10, size=10)

print(f"\nNormal data: {normal_data}")
print(f"Mean: {np.mean(normal_data)}")
print(f"Standard deviation: {np.std(normal_data)}")

student_marks = rng.normal(70, 10, size=1000)
print(f"Mean: {np.mean(student_marks)}")
print(f"Median:{np.mean(student_marks)}")
print(f"Minimum:{np.min(student_marks)}")
print(f"Maximum:{np.max(student_marks)}")
print(f"Standard deviation: {np.std(student_marks)}")

students_between_60_80 = student_marks[
    (student_marks >= 60) & (student_marks <= 80)
]

print(f"\nStudents between 60 and 80: {students_between_60_80}")
print(f"Count between 60 and 80: {np.count_nonzero(students_between_60_80)}")

standard_data = rng.standard_normal(10)

print(f"\nStandard normal data: {standard_data}")
print(f"Mean: {np.mean(standard_data)}")
print(f"Standard deviation: {np.std(standard_data)}")