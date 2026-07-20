import numpy as np
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])


for x in np.nditer(matrix):
    print(x)






arr = np.array([
    [10,20],
    [30,40]
])

for index, value in np.ndenumerate(arr):
    print(index, value)



m= np.array([
    [1,2,54,67,12,12]
    ,[34,12,44,55,33,11]
    ,[55,33,22,11,55,44]

])
print(m.shape)


for i in np.nditer(m):
    print(i)

for index,value in np.ndenumerate(m):
    print(index, value)




#
# print(m)
#
#
# print(np.transpose(m))











