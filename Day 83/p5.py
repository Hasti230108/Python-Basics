a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a >= b:
    if a >= c:
        print(a, "is the largest number")
    else:
        print(c, "is the largest number")
else:
    if b >= c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")

marks = int(input("\nEnter marks:"))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade O")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("FAIL")
