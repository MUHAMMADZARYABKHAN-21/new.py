import numpy as np


x= np.array([1,2,3,4,5,6,7,8,9,10])
print(x[:1])
print(x[:2])
print(x[:3])
print(x[:4])
print(x[:5])

print(x[-1])
print(x[-2])
print(x[-3])
print(x[-4])
print(x[-5])

#slicing with steps

x= np.array([1,2,3,4,5,6,7,8,9,10])
print(x[1:9:3])


y=x
print(y)

x=np.array([1,2,3,4,5,6,7,8,9,12])
print(x[1:9])











