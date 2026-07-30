import pandas as pd

# Create the DataFrame
data = {
    "Department": ["CS", "CS", "AI", "AI", "SE", "SE"],
    "Year": [2024, 2025, 2024, 2025, 2024, 2025],
    "Student": ["Ali", "Ahmed", "Sara", "Ayesha", "John", "Mike"],
    "Marks": [90, 85, 95, 88, 70, 75]
}

df = pd.DataFrame(data)

# Set MultiIndex
df = df.set_index(["Department", "Year"])

print("Original DataFrame")
print(df)

# 1. Print all rows for AI
print("\n1. All AI rows")
print(df.loc["AI"])

# 2. Print the row for SE, 2025
print("\n2. SE, 2025")
print(df.loc[("SE", 2025)])

# 3. Print all departments for the year 2024
print("\n3. All Departments in 2024")
print(df.loc[(slice(None), 2024), :])

# 4. Print all years for the CS department
print("\n4. All Years for CS")
print(df.loc[("CS", slice(None)), :])

# 5. Use xs() to get all rows for 2025
print("\n5. Cross Section (Year = 2025)")
print(df.xs(2025, level="Year"))

# 6. Print students with marks greater than 80
print("\n6. Students with Marks > 80")
print(df[df["Marks"] > 80])

# 7. Reset the index
print("\n7. Reset Index")
print(df.loc[("CS", slice(None)), :])
df = df.reset_index()
print(df)


