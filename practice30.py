from os import replace

import numpy as np

array=np.array([12,45,6,7,99,88,33,22,111,222,33,65,70,123,633453,34534,5656,54,32,87])


print(np.random.choice(array, size=5))
print(np.random.choice(array,size=12))

print(np.random.choice(array, size=10, replace=False))




images = np.array([
    "cat1.jpg",
    "cat2.jpg",
    "cat3.jpg",
    "cat4.jpg"
])
print(np.random.choice(images,size=2))



# Original array
arr = np.array([10,20,30,40,50])

print("Original Array:")
print(arr)

# One random value
print("\nOne Random Value:")
print(np.random.choice(arr))

# Three random values
print("\nThree Random Values:")
print(np.random.choice(arr, size=3))

# Without replacement
print("\nWithout Replacement:")
print(np.random.choice(arr,
                       size=3,
                       replace=False))

# Student names
students = np.array([
    "Ali",
    "Sara",
    "Ahmed",
    "Fatima"
])

print("\nRandom Student:")
print(np.random.choice(students))

# Weighted probabilities
grades = ["A","B","C"]

print("\nWeighted Choice:")
print(np.random.choice(
    grades,
    p=[0.7,0.2,0.1]
))

arr = np.array([1,2,3,4,5])

print("Before Shuffle:")
print(arr)

np.random.shuffle(arr)

print("\nAfter Shuffle:")
print(arr)