from collections import Counter, defaultdict, deque, namedtuple

# counter
text = "Happy People loves Python"
count = Counter(text)
print(count)
most_letter, frequency = count.most_common(1)[0]
print(f"Most repeated letter: {most_letter}")
print(f"Frequency: {frequency}")


# deafult dictionary
d = defaultdict(list)
d["Developer"].append(99)
print(d)

students = defaultdict(int)
students["Tinker"] += 1
print(students)


# deque
a = deque([10, 20, 30, 40, 50])
print(a)
a.append(55)
a.appendleft(5)
print(a)
a.pop()
print(a)
a.popleft()
print(a)


# named tuple
Person = namedtuple("Person",["name", "age"])
p1 = Person("Tinker", 19)
p2 = Person("Elia", 18)
print(f"Person 1: Name:{p1.name}, Age:{p1.age}")
print(f"Person 2: Name:{p2.name}, Age:{p2.age}")
