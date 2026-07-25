try:
    marks = int(input("Enter marks: "))

    if marks > 100 or marks < 0:
        raise Exception("Enter valid marks between 0 to 100.")
    elif marks >= 90:
        print("Pass. Grade A")
    elif marks >= 70:
        print("Pass. Grade B")
    elif marks >= 50:
        print("Pass. Grade C") 
    elif marks >= 40:
        print("Pass. Grade D")
    else:
        print("FAIL")

except ValueError:
    print("Enter valid marks.")

except Exception as e:
    print(e)