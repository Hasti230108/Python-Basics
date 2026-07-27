file = open("college.txt", "w")

name = input("Enter you name: ")
college = input("Enter college: ")
course = input("Enter course: ")

file.write(f"Name: {name} \n")
file.write(f"College: {college} \n")
file.write(f"Course: {course} \n")

file.close()

print("Data saved successfully!")