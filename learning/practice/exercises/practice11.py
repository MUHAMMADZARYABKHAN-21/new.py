import numpy as np

# -------------------------------
# Example 1: Boolean indexing
# -------------------------------
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Select elements greater than 2 OR greater than 1 (redundant, but shows OR usage)
print(x[(x > 2) | (x > 1)])


# -------------------------------
# Example 2: Random integers
# -------------------------------
# Generate 1000 random integers between 1 and 1000
x = np.random.randint(1, 1000, size=1000)
print(x)

print("result:")

# Select elements greater than 2 OR greater than 90
print(x[(x > 2) | (x > 90)])


# -------------------------------
# Example 3: NOT operator (~)
# -------------------------------
z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
              21, 22, 24, 24, 25, 26, 27, 28, 29, 30, 31])

# Keep only elements NOT greater than 31
print(z[~(z > 31)])


# -------------------------------
# Example 4: Combining conditions
# -------------------------------
arr = np.array([10, 20, 30, 40, 50])

# Select elements greater than 10 AND less than 50 AND not equal to 30
print(arr[(arr > 10) & (arr < 50) & (arr != 30)])


# -------------------------------
# Example 5: Conditional assignment
# -------------------------------
arr = np.array([10, 20, 30, 40, 50])

# Replace all elements greater than 30 with 0
arr[arr > 30] = 0
print(arr)
