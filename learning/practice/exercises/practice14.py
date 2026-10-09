import numpy as np
# 📘 NumPy Lesson 5.2 – Aggregation Functions
# 🎯 What are Aggregation Functions?
#
# Aggregation means:
#
# Taking many values and summarizing them into one value.

x=np.array([4,45,89,91,92])
print(x)

print(np.sum(x))
print(np.mean(x))
print(np.max(x))
print(np.min(x))
print(np.median(x))
y=np.array([4,45,89,91,92,93])

print(np.median(y))




#Standard deviation


x=np.array([4,45,89,91,92,93])
print(np.std(x))
print(np.var(x))
print(np.prod(x))
print(np.cumsum(x))
print(np.cumprod(x))




























