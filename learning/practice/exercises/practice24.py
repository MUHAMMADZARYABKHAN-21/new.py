import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.stack((a, b))

print(result)



a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.stack((a, b), axis=1)

print(result)






result = np.stack((a, b), axis=0)

print(result)




a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

print(np.stack((a, b), axis=-1))














city1 = np.array([30, 32, 31])
city2 = np.array([28, 29, 30])

data = np.stack((city1, city2))

print(data)











a = np.array([[67, 88, 90, 12],
              [12, 44, 78, 0]])   # padded

b = np.array([[66, 99, 111, 0],
              [112.312, 654, 0, 0]])  # padded

result = np.stack((a, b))


print(result)



a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

result = np.hstack((a, b))

print(result)





a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([[7,8,9],
            [10,11,12]])
result=np.hstack((a,b))
print(result)





print("REAL WORLD EXAMPLE")


names = np.array([
    ["Ali"],
    ["Sara"],
    ["Ahmed"]
])

marks = np.array([
    [90],
    [85],
    [78]
])

student_data = np.hstack((names, marks))

print(student_data)











A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])


print(np.hstack((A,B)))

print(np.concatenate((A,B), axis=1))



# //////////////////////////////vstack expalnations////////////




import numpy as np

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

result = np.vstack((a, b))

print(result)


a=np.array(["Zarak","Zaryab","Madiha"])
b=np.array([21,23,44])
result=np.vstack((a,b))
print(result)





a = np.array([["Zarak"], ["Zaryab"], ["Madiha"]])
b = np.array([21, 23, 44]).reshape(-1, 1)  # reshape into column vector
result = np.hstack((a, b))
print(result)




































