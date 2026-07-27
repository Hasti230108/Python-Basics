read_file = open("student.txt", "r")

content = read_file.read()

write_file = open("backup.txt", "w")
write_file.write(content)
write_file.close()
print("Data copied succesfully.")

read_file.close()