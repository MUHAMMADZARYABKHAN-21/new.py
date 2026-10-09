import numpy as np

# 1D Array
arr = np.array([0, 5, 0, 8, 10, 0])

print("Original Array:")
print(arr)

# Find indices of non-zero values
indices = np.nonzero(arr)

print("\nIndices of non-zero values:")
print(indices)

# Extract non-zero values
print("\nNon-zero values:")
print(arr[indices])

# 2D Array
matrix = np.array([
    [1, 0, 3],
    [0, 5, 0]
])

print("\nMatrix:")
print(matrix)

rows, cols = np.nonzero(matrix)

print("\nRow indices:", rows)
print("Column indices:", cols)

print("\nNon-zero values:")
print(matrix[rows, cols])