import pandas as pd

data = {
    "Student": ["Ali", "Sara", "Ahmed", "John", "Ayesha", "Ali"],
    "Department": ["CS", "AI", "CS", "SE", None, "CS"],
    "Marks": [90, 85, None, 70, 95, 90],
    "Age": [20, 21, 22, None, 20, 20],
    "Gender": ["M", "F", "M", "M", "F", "M"]
}

df = pd.DataFrame(data)

print(df)

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.duplicated().sum())

df = df.drop_duplicates()

df["Department"] = df["Department"].fillna("Unknown")

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Pass"] = df["Marks"] >= 50

df["Grade"] = df["Marks"].apply(
    lambda x:
    "A" if x >= 90 else
    "B" if x >= 80 else
    "C"
)

print(df["Marks"].max())
print(df["Marks"].min())
print(df["Grade"].value_counts())
print(df.groupby("Department")["Marks"].mean())
df = df.sort_values("Marks", ascending=False)
df = df.reset_index(drop=True)

df = df.reset_index(drop=True)
df.to_pickle("clean_students.pkl")