import pandas as pd

students = {
    "StudentID": [101, 102, 103, 102, 104, 105, 103],
    "Name": [
        "Ali",
        "Sara",
        "Ahmed",
        "Sara",
        "Fatima",
        "Hassan",
        "Ahmed"
    ],
    "Department": [
        "CS",
        "AI",
        "SE",
        "AI",
        "CS",
        "IT",
        "SE"
    ],
    "CGPA": [
        3.45,
        3.82,
        3.20,
        3.82,
        3.91,
        3.55,
        3.20
    ]
}

df = pd.DataFrame(students)

print(df)

print(df.duplicated())


print(df[df.duplicated()])


new_df=df.drop_duplicates()
print(new_df)

df=df.drop_duplicates()
print(df)