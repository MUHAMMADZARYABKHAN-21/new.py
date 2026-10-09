import pandas as pd
from openai.types.beta.threads.run_create_params import AdditionalMessageAttachment

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

pivot_count = df.pivot_table(
    values="Student",
    index="Department",
    aggfunc="count"
)
print("\nCount of Students per Department:")
print(pivot_count)

pivot_avg = df.pivot_table(
    values="CGPA",
    index="Department",
    aggfunc="mean"
)
print("\nAverage CGPA per Department:")
print(pivot_avg)

pivot_multi = df.pivot_table(
    values="Student",
    index=["Department", "Semester"],
    aggfunc="count"
)
print("\nCount of Students per Department & Semester:")
print(pivot_multi)






data = {
    "Department": ["CS", "CS", "AI", "AI", "SE", "SE"],
    "Semester": [1, 2, 1, 2, 1, 2],
    "Students": [60, 55, 50, 48, 40, 38]
}

df = pd.DataFrame(data)


pivot=df.pivot_table(

    index="Department",
    values="Students",
    aggfunc="sum",
    margins=True,
    fill_value=0


)
print("\nSum of Students per Department:")
print(pivot)
