# # import numpy as np
# # from pandas.core.indexing import IndexingMixin
# #
# # arr=np.array([[1,2,3,4],
# #              [5,6,7,8],
# #              [9,10,11,12]])
# # print(arr)
# # print(arr[0])
# # print(arr[1])
# # print(arr[2])
# # print(arr[:,0])
# # print(arr[:,1])
# # print(arr[:,2])
# #
# #
# # arr=np.array([[1,2,3,4],
# #              [5,6,7,8],
# #              [9,10,11,12]])
# # print(arr[0:1])
# # print(arr[0:2])
# # print(arr[0:3])
# #
# #
# #
# #
# # print(arr[:,0:2])
# # print(arr[:,0:3])
# # print(arr[:,3:5])
# #
# # print(arr[0:1,3:4])
# #
# # print("helo")
# #
# #
# # arr=np.array([[1,2,3,4],
# #              [5,6,7,8],
# #              [9,10,11,12]])
# # print(arr[0:1,3:4])
# #
# # print(arr[0:2,1:3])
# #
# # print(arr[1:,2:])
# #
#
#
#
# import numpy as np
#
# x = np.array([[12,12,13,14],
#               [15,16,17,18],
#               [19,20,21,22],
#               [23,24,25,26]])
#
# print(x[[0,2], [0,2]])
#
#
#
# print(x[[1,1,3],[0,1,0]])
#
#
# arr = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ])
#
# print(arr[:, [0,2]])
#
#
#
#
#
# print(arr[:,[2,3]])
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import numpy as np







x=np.array([33,55,44,32,55,66,12,33,44])
print(np.sort(x))
print(np.argsort(x))
print(np.argmax(x))
print(np.argmin(x))
print(np.mean(x)
      )

arr = np.array([10,20,30,40,50])

part = arr[1:4]
print(part)
part[0]=999
print(part)
print(arr)

arr=np.array([10,20,30,40,50])
x=arr.copy()

print(x)
x[0]=11
print(x)
print(arr)

















