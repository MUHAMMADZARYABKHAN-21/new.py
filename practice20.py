"""
===========================================================
NumPy Lesson 6.3 - reshape() vs resize()
Author: Muhammad Zaryab Khan

Topics Covered
--------------
1. reshape()
2. resize()
3. Differences
4. Common Errors
5. Real World Examples
6. Practice

===========================================================
"""

import numpy as np

# ==========================================================
# Creating Original Array
# ==========================================================

print("=" * 60)
print("Creating Original Array")
print("=" * 60)

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(arr)

print("\nShape:", arr.shape)

# Output
#
# [1 2 3 4 5 6]
# Shape: (6,)

# ==========================================================
# RESHAPE
# ==========================================================

print("\n" + "=" * 60)
print("1. RESHAPE")
print("=" * 60)

# reshape() only changes the arrangement.
# It NEVER changes the total number of elements.

reshape1 = arr.reshape(2, 3)

print("reshape(2,3)")
print(reshape1)

# Output
#
# [[1 2 3]
#  [4 5 6]]

print("\nShape:", reshape1.shape)

# ----------------------------------------------------------

reshape2 = arr.reshape(3, 2)

print("\nreshape(3,2)")
print(reshape2)

# Output
#
# [[1 2]
#  [3 4]
#  [5 6]]

# ----------------------------------------------------------

reshape3 = arr.reshape(1, 6)

print("\nreshape(1,6)")
print(reshape3)

# Output
#
# [[1 2 3 4 5 6]]

# ----------------------------------------------------------

reshape4 = arr.reshape(6, 1)

print("\nreshape(6,1)")
print(reshape4)

# Output
#
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

# ==========================================================
# Using -1
# ==========================================================

print("\n" + "=" * 60)
print("Using -1")
print("=" * 60)

# NumPy automatically calculates one dimension.

print("reshape(2,-1)")
print(arr.reshape(2, -1))

print("\nreshape(-1,2)")
print(arr.reshape(-1, 2))

# ==========================================================
# Invalid reshape()
# ==========================================================

print("\n" + "=" * 60)
print("Invalid reshape()")
print("=" * 60)

try:

    print(arr.reshape(3, 3))

except ValueError as e:

    print("Error:", e)

# Why?
#
# Array has 6 elements.
#
# 3 x 3 = 9 elements are required.
#
# reshape() cannot create new values.

# ==========================================================
# resize()
# ==========================================================

print("\n" + "=" * 60)
print("2. resize()")
print("=" * 60)

# resize() CAN change the total number of elements.
# If more elements are needed,
# NumPy repeats the original values.

resize1 = np.resize(arr, (2, 3))

print("resize(2,3)")
print(resize1)

# Same as reshape because size matches.

# ----------------------------------------------------------

resize2 = np.resize(arr, (3, 3))

print("\nresize(3,3)")
print(resize2)

# Output
#
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]]
#
# Notice:
#
# NumPy repeated the array because
# 3 x 3 = 9 elements are needed.

# ----------------------------------------------------------

resize3 = np.resize(arr, (4, 4))

print("\nresize(4,4)")
print(resize3)

# NumPy keeps repeating values until
# the requested shape is completely filled.

# ==========================================================
# Making Array Smaller
# ==========================================================

print("\n" + "=" * 60)
print("Reducing Size")
print("=" * 60)

resize4 = np.resize(arr, (2, 2))

print(resize4)

# Output
#
# [[1 2]
#  [3 4]]
#
# Values 5 and 6 are discarded.

# ==========================================================
# Another Example
# ==========================================================

print("\n" + "=" * 60)
print("Example with Different Numbers")
print("=" * 60)

numbers = np.array([10, 20, 30])

print("Original")
print(numbers)

print("\nreshape(3,1)")
print(numbers.reshape(3, 1))

print("\nresize(3,3)")
print(np.resize(numbers, (3, 3)))

# Output
#
# [[10 20 30]
#  [10 20 30]
#  [10 20 30]]

# ==========================================================
# Real World Example
# ==========================================================

print("\n" + "=" * 60)
print("Real World Example")
print("=" * 60)

# Suppose we have image pixels.

pixels = np.array([
    10, 20, 30,
    40, 50, 60
])

print("Original Pixels")
print(pixels)

# Convert into image.

image = pixels.reshape(2, 3)

print("\nImage")
print(image)

# Suppose software needs
# a 4x3 image.

bigger = np.resize(pixels, (4, 3))

print("\nBigger Image")
print(bigger)

# ==========================================================
# Difference Table
# ==========================================================

print("\n" + "=" * 60)
print("Difference")
print("=" * 60)

print("""
----------------------------------------------------------
reshape()

✔ Rearranges data
✔ Number of elements stays SAME
✔ Gives Error if size doesn't match

resize()

✔ Can increase size
✔ Can decrease size
✔ Repeats values if needed
✔ Never gives reshape size error
----------------------------------------------------------
""")

# ==========================================================
# Practice
# ==========================================================

print("\n" + "=" * 60)
print("Practice Questions")
print("=" * 60)



print("\nLesson Completed Successfully!")