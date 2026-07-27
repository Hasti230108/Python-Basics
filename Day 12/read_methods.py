file = open("student.txt", "r")

print("\n---Using read()---")
file.seek(0)
content1 = file.read()
print(content1)

print("\n---Using readline()---")
file.seek(0)
content2a = file.readline()
print(content2a)
content2b = file.readline()
print(content2b)

print("\n---Using readlines()---")
file.seek(0)
content3 = file.readlines()
print(content3)

file.close()
