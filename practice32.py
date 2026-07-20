import numpy as np
arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr)
y=np.random.permutation(arr)

print("\nAfter Shuffle:")
print(arr)

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

new_matrix = np.random.permutation(matrix)

print("Original:")
print(matrix)

print("\nPermutation:")
print(new_matrix)

