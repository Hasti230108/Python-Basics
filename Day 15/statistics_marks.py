import statistics

marks = []

for i in range(5):
    marks.append(int(input("Enter Marks: ")))

print("Mean: ", statistics.mean(marks))
print("Median: ", statistics.median(marks))
print("Highest: ", max(marks))
print("Lowest: ", min(marks))