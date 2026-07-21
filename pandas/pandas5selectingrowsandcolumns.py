import pandas as pd

#
#
# import pandas as pd
#
# data = {
#     "ID": [101,102,103,104,105],
#     "Name": ["Ali","Sara","Ahmed","Ayesha","Hassan"],
#     "Age": [20,21,19,22,20],
#     "Math": [85,90,76,95,88],
#     "Physics": [78,88,81,91,86],
#     "Chemistry": [92,84,79,93,90]
# }
#
# df = pd.DataFrame(data)
#
# print(df)
#
#
# print(df[["Name","Math"]])
#
#
# print(df[["ID","Age"]])








data = {
    "ID": [101,102,103,104,105],
    "Name": ["Ali","Sara","Ahmed","Ayesha","Hassan"],
    "Age": [20,21,19,22,20],
    "Math": [85,90,76,95,88],
    "Physics": [78,88,81,91,86],
    "Chemistry": [92,84,79,93,90]
}

x=pd.DataFrame(data)
print(x)
# print(x.iloc[1])

# print(x.iloc[0,4])
# print(x.iloc[4,1])
#
# print(x.iloc[3])


print(x.iloc[:,0:4])

print(x.iloc[0])


print(x.iloc[1])

print(x.iloc[2])


print(x.iloc[3])




print(x.iloc[1:4,0:3])





