import numpy as np


x= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x[(x>2)|(x>1)])



 # using rand operation on array




# Generate one random integer between 1 and 1000
x = np.random.randint(1, 1000 ,size =1000)
print(x)


print("result ")

print(x[(x>2)|(x>90)])





# not operator


z=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,24,25,26,27,28,29,30,31])


print(z[~(z>31)])








