import numpy as np


# 1. Array Creation
arr1 = np.array([1, 2, 3])              # Basic array
arr2 = np.zeros((2, 3))                 # 2x3 array of zeros
arr3 = np.ones((2, 3))                  # 2x3 array of ones
arr4 = np.arange(0, 10, 2)              # Even numbers from 0 to 8
arr5 = np.linspace(0, 1, 5)             # 5 equally spaced numbers between 0 and 1
arr6 = np.eye(3)                        # Identity matrix

print("Array Creation Examples:\n", arr1, arr2, arr3, arr4, arr5, arr6, "\n")

# 2. Array Attributes
print("Shape:", arr3.shape)
print("Size:", arr3.size)
print("Data Type:", arr3.dtype, "\n")

# 3. Indexing & Slicing
print("First element:", arr1[0])
print("Slice:", arr4[1:4], "\n")

# 4. Mathematical Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Dot Product:", np.dot(a, b))
print("Element-wise Square:", np.square(a), "\n")

# 5. Broadcasting
matrix = np.ones((3, 3))
vector = np.array([1, 2, 3])
print("Broadcasting Example:\n", matrix + vector, "\n")

# 6. Universal Functions (ufuncs)
print("Sine:", np.sin(a))
print("Exponential:", np.exp(a))
print("Logarithm:", np.log(a), "\n")

# 7. Statistical Functions
data = np.array([1, 2, 3, 4, 5])
print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))
print("Max:", np.max(data))
print("Min:", np.min(data), "\n")

# 8. Linear Algebra
mat = np.array([[1, 2], [3, 4]])
print("Matrix Determinant:", np.linalg.det(mat))
print("Matrix Inverse:\n", np.linalg.inv(mat))
print("Eigenvalues:", np.linalg.eig(mat)[0], "\n")

# 9. Reshaping & Flattening
reshaped = np.arange(12).reshape(3, 4)
print("Reshaped Array:\n", reshaped)
print("Flattened:", reshaped.flatten(), "\n")

# 10. Random Numbers
rand_arr = np.random.rand(2, 2)         # Uniform [0,1)
randn_arr = np.random.randn(2, 2)       # Normal distribution
randint_arr = np.random.randint(1, 10, (2, 2))  # Random integers
print("Random Arrays:\n", rand_arr, randn_arr, randint_arr, "\n")

# 11. Boolean Indexing & Masking
mask = data > 2
print("Mask:", mask)
print("Filtered Data:", data[mask], "\n")

# 12. Saving & Loading
np.save("my_array.npy", data)           # Save to file
loaded = np.load("my_array.npy")        # Load from file
print("Loaded Array:", loaded)


# Practice Questions
#
# Try these on your own:
#
# Create an array of 10 zeros.
# Create a 3 × 3 array of ones.
# Create numbers from 5 to 25 using arange().
# Create 6 equally spaced numbers between 0 and 30 using linspace().
# Generate 8 random integers between 1 and 50.
# Print the shape, size, ndim, and dtype of a 2 × 4 array.
# Homework

a=np.zeros(10)
print(a)
b=np.ones((3,3))
c=np.arange(5,25)
print(c)
d=np.linspace(0,30,5)
print(d)
d=np.random.randint(1,50)
e=np.array(([1,2,3,4],
           [5,6,7,8]))
print(e.shape)
print(e.dtype)
print(e.ndim)
print(e.size)



