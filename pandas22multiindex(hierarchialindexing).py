import pandas as pd

data = {
    "Department": ["CS", "CS", "AI", "AI", "SE", "SE"],
    "Semester": [1, 2, 1, 2, 1, 2],
    "Students": [60, 55, 50, 48, 40, 38]
}

df = pd.DataFrame(data)

print(df)

df=df.set_index(["Department", "Semester"])
print(df)

print(df.loc["CS",1])
print(df.loc["CS"])




print(df.loc["SE",2])
print(df)

df=df.reset_index()
print(df)


arrays = [
    ["Math", "Math", "Science", "Science"],
    ["Midterm", "Final", "Midterm", "Final"]
]
columns = pd.MultiIndex.from_arrays(arrays, names=["Subject", "Exam"])

scores = pd.DataFrame(
    [[80, 90, 85, 88],
     [70, 75, 78, 82]],
    columns=columns,
    index=["Ali", "Sara"]
)

print(scores)


