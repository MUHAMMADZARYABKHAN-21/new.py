# import pandas as pd
#
#
#
# import pandas as pd
#
# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hassan", "Fatima"],
#     "Age": [20, 21, 19, 22, 20, 23],
#     "Math": [85, 92, 76, 95, 88, 70],
#     "Physics": [78, 89, 81, 91, 86, 75],
#     "Department": ["CS", "AI", "CS", "AI", "CS", "SE"]
# }
#
# df = pd.DataFrame(data)
#
# print(df)
#
#
# print(df[df["Math"]>90])
# print(df[df["Physics"]>90])



import pandas as pd

data=pd.read_csv("Data.csv")
print(data)          # Just print the DataFrame directly


print(data[["Math"]]>85)


print(data[["Chemistry"]]<85)


print(data["Age"]!=20)

print(data[(data["Age"] > 21) & (data["Physics"] < 30)])












