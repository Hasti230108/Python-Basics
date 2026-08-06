import numpy as np

numbers = [10, 20, 30, 40, 50]
array = np.array(numbers)

print(numbers)
print(type(numbers))

print(array)
print(type(array))

print(f"\nDimensions: {array.ndim}")
print(f"Shape : {array.shape}")
print(f"Size: {array.size}")
print(f"Datatype: {array.dtype}")


print("\nIndexing:")
print(f"First Element: {array[0]}")
print(f"Last Element: {array[-1]}")

print("\nSlicing:")
print(f"All elements: {array[0:5]}")
print(f"First 3 elements: {array[0:3]}")

print("\nArithmetic Operations:")
print(array + 10)
print(array - 5)
print(array * 2)
print(array / 2)

array2 = np.array([1, 2, 3, 4, 5])
print("\nArray Operations:")
print(array + array2)
print(array - array2)
print(array * array2)
print(array / array2)
