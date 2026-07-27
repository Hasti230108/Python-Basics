file = open("student.txt", "w")

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

file.write(f"Name: {name} \n")
file.write(f"Age: {age} \n")
file.write(f"City: {city} \n")

file.close()

print("Data saved successfully!")