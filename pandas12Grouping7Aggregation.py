import pandas as pd

employees = {
    "Employee": [
        "Ali", "Sara", "Ahmed", "Fatima",
        "Hassan", "Ayesha", "Usman", "Hamza"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "City": [
        "Islamabad", "Lahore", "Islamabad", "Karachi",
        "Lahore", "Karachi", "Islamabad", "Lahore"
    ],
    "Salary": [
        90000, 65000, 100000, 120000,
        70000, 110000, 95000, 72000
    ],
    "Experience": [
        2, 4, 5, 7,
        3, 6, 4, 2
    ]
}

df = pd.DataFrame(employees)

print(df)

print(df.groupby(["Employee", "City"]))
print(df.groupby("Department")["Salary"].mean())


print(df.groupby("City")["Salary"].mean())


print(df.groupby("Department")["Salary"].sum())



print(df.groupby("City")["Salary"].max())



print(df.groupby("Department")["Salary"].min())
















