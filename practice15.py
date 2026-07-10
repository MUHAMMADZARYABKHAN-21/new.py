import numpy as np

# Initial array with proper commas between rows
z = np.array((
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
))

# Sum across columns (axis=0) and rows (axis=1)
print(np.sum(z, axis=0))
print(np.sum(z, axis=1))


"""
===========================================================
NumPy Lesson 5 - Complete (Parts 1, 2 and 3)
Author: Muhammad Zaryab Khan
Topics:
1. Arithmetic Operations
2. Aggregation Functions
3. axis=0 and axis=1
===========================================================
"""

print("="*60)
print("PART 1 - ARITHMETIC OPERATIONS")
print("="*60)

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print("arr1 =", arr1)
print("arr2 =", arr2)

# Addition
print("\nAddition")
print(arr1 + arr2)

# Subtraction
print("\nSubtraction")
print(arr1 - arr2)

# Multiplication (element-wise)
print("\nMultiplication")
print(arr1 * arr2)

# Division
print("\nDivision")
print(arr1 / arr2)

# Floor Division
print("\nFloor Division")
print(arr1 // 3)

# Modulus
print("\nModulus")
print(arr1 % 3)

# Power
print("\nSquare")
print(arr1 ** 2)

print("\nCube")
print(arr1 ** 3)

# Square Root
print("\nSquare Root")
print(np.sqrt(arr1))

# Absolute Value
negative = np.array([-5, -2, 3, -10])
print("\nAbsolute Value")
print(np.abs(negative))

print("\nPython list vs NumPy array")
a = [1, 2, 3]
b = [4, 5, 6]
print("Python list:", a + b)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("NumPy array:", a + b)

print("\n" + "="*60)
print("PART 2 - AGGREGATION FUNCTIONS")
print("="*60)

marks = np.array([80, 90, 70, 85, 95])

print("Marks:", marks)
print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))

nums = np.array([2, 3, 4])
print("Product:", np.prod(nums))
print("Cumulative Sum:", np.cumsum(nums))
print("Cumulative Product:", np.cumprod(nums))

print("\n" + "="*60)
print("PART 3 - AXIS")
print("="*60)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matrix:")
print(matrix)

print("\nNo axis -> Sum of all elements")
print(np.sum(matrix))

print("\naxis=0 (operate down rows, result per column)")
print(np.sum(matrix, axis=0))

print("\naxis=1 (operate across columns, result per row)")
print(np.sum(matrix, axis=1))

print("\nColumn Means")
print(np.mean(matrix, axis=0))

print("\nRow Means")
print(np.mean(matrix, axis=1))

print("\nColumn Maximum")
print(np.max(matrix, axis=0))

print("\nRow Maximum")
print(np.max(matrix, axis=1))

print("\nColumn Minimum")
print(np.min(matrix, axis=0))

print("\nRow Minimum")
print(np.min(matrix, axis=1))

print("""
Memory Trick
------------
axis=0 -> Move DOWN rows -> Gives one result per COLUMN.
axis=1 -> Move ACROSS columns -> Gives one result per ROW.
""")

print("Practice:")
print("1. Predict np.sum(matrix, axis=0)")
print("2. Predict np.mean(matrix, axis=1)")
print("3. Predict np.max(matrix, axis=0)")
