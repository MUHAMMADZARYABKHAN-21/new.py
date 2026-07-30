import pandas as pd

data = {
    "Department": ["CS", "CS", "AI", "AI", "SE", "SE"],
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "John", "Mike"],
    "Marks": [90, 80, 85, 95, 70, 75]
}

df = pd.DataFrame(data)

print(df)
print(df.groupby("Department")["Marks"].mean())
print(df.groupby("Department")["Marks"].sum())


data = {
    "Student": ["Ali", "Sara", "Ahmed", "Fatima", "Hassan", "Ayesha", "Bilal", "Zain"],
    "Department": ["CS", "AI", "CS", "SE", "AI", "SE", "CS", "AI"],
    "CGPA": [3.6, 3.9, 3.2, 3.8, 3.1, 3.5, 3.7, 3.4]
}

df = pd.DataFrame(data)

# Mean CGPA per department, broadcast back to every row
df["Dept_Avg"] = df.groupby("Department")["CGPA"].transform("mean")

print(df)

# Compare each student's CGPA to their department's average
df["Above_Average"] = df["CGPA"] > df["Dept_Avg"]

print(df)
result=df.groupby("Department").filter(lambda  x:x["CGPA"]>3.0)
print(result)