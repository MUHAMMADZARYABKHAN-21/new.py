import pandas as pd



data = {
    "ID": [101,102,103,104],
    "Name": ["Ali","Sara","Ahmed","Ayesha"],
    "Age": [20,21,19,22],
    "Math": [85,90,76,95]
}

df = pd.DataFrame(data)
print(df)
df["Physics"]=[45,46,78,99]

print(df)
df["Calculus"]=[88,91,78,95]
print(df)


df["Total"]=df["Physics"]+df["Calculus"]
print(df)
print(df["Physics"].sum())
print(df["Calculus"].sum())
df["Average"]=(df["Math"]+df["Physics"])/2




#    ID    Name  Age  Math  Physics  Calculus  Total
# 0  101     Ali   20    85       45        88    133
# 1  102    Sara   21    90       46        91    137
# 2  103   Ahmed   19    76       78        78    156
# 3  104  Ayesha   22    95       99        95    194
#
#





