file = open("student.txt", "a")

hobby = input("Enter your hobby: ")
mobile = input("Enter your mobile number: ")

file.write(f"Hobby: {hobby} \n")
file.write(f"Mobile: {mobile} \n")

file.close()

print("Data updated successfully!")