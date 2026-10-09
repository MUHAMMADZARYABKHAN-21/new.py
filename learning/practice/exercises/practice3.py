import numpy as np

# Example array
arr2 = np.array([10, 20, 30, 40, 50, 60, 70])

# Print slice from index 2 to 6 (exclusive of 6)
print(arr2[2:6])   # → [30 40 50 60]

# Another array
arr3 = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

# Reverse with step -3 and multiply by 3
print(arr3[::-3] * 3)   # → [3000 2100 1200 300]

# Corrected array creation (typo fixed: np.aray → np.array)
arr3 = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr3)        # Full array
print(arr3[1:5])   # Slice from index 1 to 4 → [2 3 4 5]


