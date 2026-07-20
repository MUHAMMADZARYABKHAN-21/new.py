import numpy as np


arr = np.array([1,2,3,4,5])

print("Before Shuffle:")
print(arr)

np.random.shuffle(arr)

print("\nAfter Shuffle:")
print(arr)



arr=np.array(["ALI","NOMAN","JAMEBOND","EMMAWATSON","SIDNEYSWEENIE"])
print("Before Shuffle:")
print(arr)
np.random.shuffle(arr)
print("\nAfter Shuffle:")
print(arr)




print("2d array:")
x=np.array([[1,2,3,8],
           [12,45,6,7],
           [1,6,7,0]])
print("Before Shuffle:")
print(x)
np.random.shuffle(x)
print("\nAfter Shuffle:")
print(x)




# Example 1
arr = np.array([1,2,3,4,5])

print("Original Array:")
print(arr)

np.random.shuffle(arr)

print("\nShuffled Array:")
print(arr)

# Example 2
names = np.array(["Ali","Sara","Ahmed","Fatima"])

print("\nOriginal Names:")
print(names)

np.random.shuffle(names)

print("\nShuffled Names:")
print(names)

# Example 3
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("\nOriginal Matrix:")
print(matrix)

np.random.shuffle(matrix)

print("\nShuffled Matrix:")
print(matrix)










