import matplotlib.pyplot as plt

students = ["riya", "disha", "garvita", "jay", "neha", "ayush", "jerome"]

marks = [90, 80, 61, 60, 88, 55, 76]

# Bar Chart
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Visualization")
plt.show()

# Line Chart
plt.plot(students, marks, marker='o')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Visualization")
plt.show()

# Pie Chart
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Student Marks Distribution")
plt.show()

# Scatter Plot
plt.scatter(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Visualization")
plt.show()
