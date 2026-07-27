


import pandas as pd

data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hassan"],
    "Age": [20, 21, 19, 22, 20],
    "Math": [85, 90, 76, 95, 88],
    "Physics": [78, 88, 81, 91, 86],
    "Chemistry": [92, 84, 79, 93, 90]
}

df = pd.DataFrame(data)
print(df)





print(df.sort_values(by="Math"))




print(df.sort_values(by="Physics"))




print(df.sort_values(by="Name"))


print(df.sort_values(by="Age"))
















print(df.sort_values(
    by=["Age", "Math"],
    ascending=[True, False]
))
print(df.sort_values(by=["Age","Math"]))

print(df.sort_index())












