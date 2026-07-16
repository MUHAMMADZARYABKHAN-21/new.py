import numpy as np



x= np.array([[67,89,123,45,67,78],[22,33,44,55,66,88]])

print(np.argmax(x))


print(np.argmin(x))




arr = np.array([10, 20, 10, 30, 20, 40])

print(np.unique(arr))


arr=np.array(["ali","usman","noman","noman","ali"])
print(np.unique(arr))


names = np.array([
    "Ali",
    "Sara",
    "Ali",
    "Ahmed",
    "Sara"
])

print(np.unique(names))




grades = np.array([
    "A",
    "B",
    "A",
    "C",
    "B",
    "A"
])

print(np.unique(grades))




grades = np.array([
    "A",
    "B",
    "A",
    "C",
    "B",
    "A"
])

values, counts = np.unique(grades, return_counts=True)

print(values)
print(counts)



























l=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])



values,counts = np.unique(l,return_counts=True)
print(values)
print(counts)

arr = np.array([0, 5, 0, 8, 10, 0])

indices = np.nonzero(arr)

print(indices)

















