student = {"name": "Tinker", "age": 19, "course": "AI & ML" }

student["age"] = 18

student.update({"city": "Mumbai"})

del student["course"]

print("---Student Details---")
print("Name :", student["name"])
print("Age :", student["age"])
