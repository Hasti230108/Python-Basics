import math
import random
from datetime import datetime
import statistics

numbers = []

for i in range(5):
    numbers.append(random.randint(1,100))

print("Numbers:", numbers)

mean = statistics.mean(numbers)

print("Mean:", mean)

print("Square Root of Mean:", math.sqrt(mean))

print("Current Time:", datetime.now().strftime("%H:%M:%S"))