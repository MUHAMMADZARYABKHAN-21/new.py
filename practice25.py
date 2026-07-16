import numpy as np

# Create a 1D array of integers
arr = np.array([78, 92, 65, 88, 71])

# Sort the array (returns a new sorted copy)
sorted_arr = np.sort(arr)

print("Original:", arr)       # Original unsorted array
print("Sorted:", sorted_arr) # Sorted array (ascending order)

# Generate 100 random integers between 10 and 399
arr = np.random.randint(10, 400, 100)

# Sort the random array
print(np.sort(arr))

# Calculate mean (average value)
print(np.mean(arr))

# Calculate standard deviation (spread of values)
print(np.std(arr))


# In-place sorting (modifies the array directly)
arr = np.array([5, 1, 8, 2])
arr.sort()
print(arr)  # Output: [1 2 5 8]


# Create a 2D matrix
matrix = np.array([
    [9, 2, 7],
    [6, 1, 4]
])

# Default sort (row-wise)
print(np.sort(matrix))

# Sort column-wise (axis=0)
sorted_matrix = np.sort(matrix, axis=0)
print(sorted_matrix)

# Sort row-wise (axis=1)
sorted_matrix = np.sort(matrix, axis=1)
print(sorted_matrix)


# Descending order sort
arr = np.array([5, 1, 8, 2])
descending = np.sort(arr)[::-1]  # Reverse after sorting
print(descending)  # Output: [8 5 2 1]


# Get indices that would sort the array
arr = np.array([90, 70, 85, 60])
print(np.argsort(arr))  # Output: [3 1 2 0]


# Another argsort example
arr = np.array([90, 91, 1000, 54, 78])
print(np.argsort(arr))  # Indices of sorted order

# Generate 50 random integers between 1 and 1099
x = np.random.randint(1, 1100, 50)
print(x)                # Print the random array
print(np.argsort(x))    # Indices that would sort the array



v=np.array([[1,2,3,4,5],

           [12,13,45,67,12]])
print(np.where(v==12))
print(np.where(v==45))













