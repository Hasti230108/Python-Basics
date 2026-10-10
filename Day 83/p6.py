with open("students.txt", "w") as f:
    f.write("Riya, 88\n")
    f.write("Aarav, 92\n")
    f.write("Kabir, 76\n")

with open("students.txt", "r") as f:
    content = f.read()
    print("Full content")
    print(content)

with open("students.txt", "a") as f:
    f.write("Meera, 95\n")

with open("students.txt", "r") as f:
    print(f.read())
