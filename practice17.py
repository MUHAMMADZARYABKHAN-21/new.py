"""
===========================================================
NumPy Lesson 6.2 - flatten() vs ravel()
Author: Muhammad Zaryab Khan
===========================================================

Topics Covered
--------------
1. What is flatten()?
2. What is ravel()?
3. Copy vs View
4. Memory Sharing
5. Real-World Example
6. Summary

===========================================================
"""

import numpy as np

# =========================================================
# Creating a 2D NumPy Array
# =========================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("=" * 60)
print("Original Matrix")
print("=" * 60)
print(matrix)

# Output:
#
# [[1 2 3]
#  [4 5 6]]

# =========================================================
# flatten()
# =========================================================

print("\n" + "=" * 60)
print("flatten()")
print("=" * 60)

# flatten() converts a multidimensional array
# into a 1D array.
#
# IMPORTANT:
# flatten() creates a COPY of the original array.

flat = matrix.flatten()

print("Flattened Array:")
print(flat)

# Output:
#
# [1 2 3 4 5 6]

# =========================================================
# Checking Whether flatten() Changes Original Array
# =========================================================

print("\nChanging flat[0] = 100")

flat[0] = 100

print("Flattened Array:")
print(flat)

print("\nOriginal Matrix:")
print(matrix)

# Output:
#
# Flattened Array:
# [100   2   3   4   5   6]
#
# Original Matrix:
#
# [[1 2 3]
#  [4 5 6]]

# Notice:
# The original matrix DID NOT change.
#
# Why?
#
# Because flatten() created a completely new array
# stored in different memory.

# =========================================================
# ravel()
# =========================================================

print("\n" + "=" * 60)
print("ravel()")
print("=" * 60)

matrix2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

ravel_array = matrix2.ravel()

print("Ravel Array:")
print(ravel_array)

# Output:
#
# [1 2 3 4 5 6]

# =========================================================
# Checking Whether ravel() Changes Original Array
# =========================================================

print("\nChanging ravel_array[0] = 100")

ravel_array[0] = 100

print("Ravel Array:")
print(ravel_array)

print("\nOriginal Matrix:")
print(matrix2)

# Output:
#
# Ravel Array:
# [100   2   3   4   5   6]
#
# Original Matrix:
#
# [[100   2   3]
#  [  4   5   6]]

# Notice:
#
# The original matrix ALSO changed.
#
# Why?
#
# Because ravel() usually returns a VIEW
# of the original array.
#
# Both variables share the same memory.

# =========================================================
# Memory Demonstration
# =========================================================

print("\n" + "=" * 60)
print("Memory Demonstration")
print("=" * 60)

arr = np.array([
    [10, 20],
    [30, 40]
])

copy_array = arr.flatten()
view_array = arr.ravel()

print("Original:")
print(arr)

copy_array[1] = 999

print("\nAfter changing flatten() copy:")

print("Copy:")
print(copy_array)

print("Original:")
print(arr)

# Original remains unchanged.

view_array[2] = 777

print("\nAfter changing ravel() view:")

print("View:")
print(view_array)

print("Original:")
print(arr)

# Original changes because ravel()
# shares memory.

# =========================================================
# Real-World Example
# =========================================================

print("\n" + "=" * 60)
print("Real-World Example")
print("=" * 60)

# Suppose this is a grayscale image.

image = np.array([
    [255, 100, 80],
    [60, 30, 10]
])

print("Image:")
print(image)

# Many Machine Learning models
# require image pixels in a single row.

pixels1 = image.flatten()
pixels2 = image.ravel()

print("\nUsing flatten():")
print(pixels1)

print("\nUsing ravel():")
print(pixels2)

# Both produce:
#
# [255 100 80 60 30 10]

# =========================================================
# Shape Comparison
# =========================================================

print("\n" + "=" * 60)
print("Shape Comparison")
print("=" * 60)

print("Original Shape :", image.shape)

print("Flatten Shape :", pixels1.shape)

print("Ravel Shape :", pixels2.shape)

# Output:
#
# Original Shape : (2,3)
#
# Flatten Shape : (6,)
#
# Ravel Shape : (6,)

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("Summary")
print("=" * 60)

print("flatten()")
print("✔ Creates a NEW array (Copy)")
print("✔ Original array is NOT affected")
print("✔ Uses more memory")
print("✔ Slightly slower")

print()

print("ravel()")
print("✔ Returns a View whenever possible")
print("✔ Shares memory with original")
print("✔ Faster")
print("✔ Uses less memory")

# =========================================================
# Comparison Table
# =========================================================

print("\nComparison Table")

print("""
---------------------------------------------------------
Feature              flatten()          ravel()
---------------------------------------------------------
Returns 1D Array         Yes              Yes
Creates Copy             Yes               No*
Shares Memory             No              Yes*
Changes Original          No              Yes*
Speed                  Slower           Faster
Memory                 More             Less
---------------------------------------------------------

* ravel() returns a view whenever possible.
In some special cases, NumPy may create a copy.
""")

# =========================================================
# Practice
# =========================================================

print("\n" + "=" * 60)
print("Practice Questions")
print("=" * 60)

print("""
1. What is the difference between flatten() and ravel()?

2. Which one creates a copy?

3. Which one shares memory?

4. Which one is faster?

5. Which one should you use if you don't want to modify
   the original array accidentally?

Try answering these before checking your notes.
""")