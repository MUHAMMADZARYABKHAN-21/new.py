import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Ahmed", "Sara", "John"],
    "Department": ["CS", "CS", "AI", "SE"]
})

print(df.dtypes)
df["Department"]=df["Department"].astype("category")
print(df.dtypes)

print(df)
print(df["Department"].cat.categories)
print(df["Department"].cat.codes)
df["Department"] = df["Department"].cat.rename_categories({
    "CS": "Computer Science",
    "AI": "Artificial Intelligence",
    "SE": "Software Engineering"
})
#
# print(df)
# df["Department"] = df["Department"].cat.add_categories(["Computer Science"])
#
# print(df)



