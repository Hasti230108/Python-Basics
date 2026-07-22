file = open("student.txt", "r")
count = 0
for line in file:
    count += 1

file.close()

print("Total lines: ", count)