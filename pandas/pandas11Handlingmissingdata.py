import pandas as pd
import numpy as np

students = {
    "Student": ["Ali", "Sara", "Ahmed", "Fatima", "Hassan"],
    "Age": [20, 21, np.nan, 22, 20],
    "CGPA": [3.6, np.nan, 3.2, 3.9, 3.4],
    "City": ["Islamabad", "Lahore", "Karachi", np.nan, "Islamabad"]
}

df = pd.DataFrame(students)

# Check missing values
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().any(axis='rows'))

# Drop rows with missing values
print(df.dropna())


mean_age = df["Age"].mean()

print(mean_age)
df["Age"]=df["Age"].fillna(mean_age)

print(df)
df["Age"] = df["Age"].fillna(df["Age"].median())
print(df)






