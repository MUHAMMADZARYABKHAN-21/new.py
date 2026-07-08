# 🔹 Challenge: Matrix Transformation
# You’re given this NumPy array:
#
# python
# import numpy as np
#
# x = np.array([
#     [1,  2,  3,  4],
#     [5,  6,  7,  8],
#     [9, 10, 11, 12]
# ])
# Tasks:
# Extract the last row ([9, 10, 11, 12]) and store it in a variable.
#
# Reverse that row so it becomes [12, 11, 10, 9].
#
# Replace the first row of x with this reversed row.
#
# Print the final array.

import numpy as np

x = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
 ])

print(x[2:])
y=print(x[2:])
Z=print(x[2,::-1])



z=print(x[2,::-1])

