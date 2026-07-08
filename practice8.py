import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

# Example 1: Filter values less than 35
print(numbers[numbers < 35])   # Output: [10 20 30]

# Example 2: Filter values that are multiples of 20
print(numbers[numbers % 20 == 0])   # Output: [20 40]

# Example 3: Filter values between 15 and 45
print(numbers[(numbers >= 15) & (numbers <= 45)])   # Output: [20 30 40]

print(numbers[(numbers>=0)])


print(numbers[(numbers==10)])
print(numbers[numbers != 30])
