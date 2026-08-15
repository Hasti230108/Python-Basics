import numpy as np

rng = np.random.default_rng()

print(f"Random integer: {rng.integers(1, 101)}")
print(f"Random integers: {rng.integers(1, 101, size=5)}")
print(f"\nRandom floats: {rng.random(5)}")
print(f"\nRandom mattrix:\n{rng.integers(1, 101,  size=(3, 3))}")

marks = np.array([45, 78, 92, 47, 96, 87, 83, 79])

print(f"\nMarks: {marks}")
print(f"Random choice: {rng.choice(marks)}")
print(f"Three random marks: {rng.choice(marks, size=3)}")

print(f"\nReproducible random numbers:")
rng1 = np.random.default_rng(42)
print(rng1.integers(1, 101, size=5))

rng2 = np.random.default_rng(42)
print(rng2.integers(1, 101, size=5))