import random
import statistics
import math
from datetime import datetime

name = input("Enter your name: ")
rollNo = int(input("Enter your roll no.: "))

marks = []

for i in range(5):
    marks.append(random.randint(0,100))

average = statistics.mean(marks)
median = statistics.median(marks)
squareRoot = math.sqrt(average)

print("\n---Report Card---")
print(f"\nStudent Name : {name}")
print(f"\nRoll No. : {rollNo}")
print(f"\nMarks : {marks}")
print(f"\nAverage : {average}")
print(f"\nMedian : {median}")
print(f"\nSquare root average : {squareRoot}")
print("\nGenerated on :")
print("\n",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))