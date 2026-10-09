import pandas as pd



data = {
    "Name": ["Ali", "Sara", "John", None, "Ahmed", "Sara"],
    "Department": ["CS", "AI", "CS", "SE", None, "AI"],
    "Marks": [90, 85, None, 70, 95, 85],
    "Age": [20, 21, 22, None, 20, 21]
}

df = pd.DataFrame(data)

print(df)
print(df.describe())
print(df.info())
print(df.isnull())
print(df.isnull().sum())
print(df.duplicated().sum)


df=df.drop_duplicates()
print(df)
df["Name"]=df["Name"].fillna("xxx")
print(df)
df["Department"]=df["Department"].fillna("xx")

print(df)
df["Marks"]=df["Marks"].fillna(0)
print(df)
df["Age"]=df["Age"].fillna("xxx")
print(df)
print(df.isnull())
#
# df["Age"]=df["Age"].astype(float)
print(df)
df["Pass"] = df["Marks"] >= 50
print(df)
df["Grade"]=df["Marks"].apply(lambda x:"A"if x >=90
                              else "B" if x >=85
                              else "C" if x >=70
                              else "D"
                              )
print(df)
df=df.sort_values("Marks")
print(df)
df = df.reset_index(drop=True)
print(df)

