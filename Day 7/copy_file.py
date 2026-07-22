source = open("student.txt", "r")
content = source.read()
source.close()

destination = open("student_copy.txt", "w")
destination.write(content)
destination.close()

print("File copied successfully.")