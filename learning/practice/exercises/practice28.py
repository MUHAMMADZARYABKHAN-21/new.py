import numpy as np

# Sorted array
arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

# Search for a single value
print("\nInsert 35 at index:")
print(np.searchsorted(arr, 35))

# Search for multiple values
values = [15, 25, 45]

print("\nInsert positions:")
print(np.searchsorted(arr, values))

# Duplicate values
duplicates = np.array([10, 20, 30, 30, 30, 40])

print("\nLeft insertion:")
print(np.searchsorted(duplicates, 30, side="left"))

print("Right insertion:")
print(np.searchsorted(duplicates, 30, side="right"))

# Actually insert a value
new_array = np.insert(arr, np.searchsorted(arr, 35), 35)

print("\nArray after insertion:")
print(new_array)

