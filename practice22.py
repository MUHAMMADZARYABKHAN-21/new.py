import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([1,2,3,4,5,6,7,8,9,10])
z=np.concatenate((x,y))
print(z)


a=np.array([11,12,123])
b=np.concatenate((a,a,a))
c=b.astype(float)
print(c)
print(b)


