import pandas as pd

data = {
    "Student": [
        "Ali", "Sara", "Ahmed",
        "Fatima", "Hassan",
        "Ayesha", "Bilal", "Zain"
    ],

    "Department": [
        "CS", "AI", "CS",
        "SE", "AI",
        "SE", "CS", "AI"
    ],

    "Semester": [
        1, 1, 2,
        2, 1,
        2, 1, 2
    ],

    "CGPA": [
        3.6, 3.9, 3.2,
        3.8, 3.1,
        3.5, 3.7, 3.4
    ]
}

df = pd.DataFrame(data)

print(df)

