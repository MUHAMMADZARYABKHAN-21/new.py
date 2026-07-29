
import pandas as pd

students = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Hassan"],
    "Department": ["CS", "AI", "SE", "CS", "IT"],
    "CGPA": [3.6, 3.9, 2.8, 3.4, 3.1]
}

df = pd.DataFrame(students)

print(df)

department_map={
    "CS":"COMPUTER SCIENCE",
    "AI":"ARTIFICIAL INTELLIGENCE",
    "SE":"SOFTWARE ENGINEERING",
   " CS":"COMPUTER SCIENCE",
    "IT":"INFORMATION TECHNOLOGY"
}
df["Department"]=df["Department"].map(department_map)
print(df)

df["Name"]=df["Name"].replace({"Ali":"NOMAN",
                                 "Sara":"ZARYAB",
                               "Ahmed":"AHMED",
                               "Hassan":"JOHN_F-KENNEDY"

                                 })
print(df)


df["Name"]=df["Name"].apply(str.lower)
print(df)
df["Name"]=df["Name"].apply(str.upper)
print(df)
df["Results"]=df["CGPA"].apply(lambda x:"PASS" if x>=3.00 else "FAIL")
print(df)


students = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Hassan"],
    "Department": ["CS", "AI", "SE", "CS", "IT"],
    "CGPA": [3.6, 3.9, 2.8, 3.4, 3.1]
}

df = pd.DataFrame(students)

print("========== ORIGINAL DATAFRAME ==========")
print(df)

# ==========================================================
# 1. Convert Department names using map()
# map() replaces EVERY value using a dictionary.
# If a value is not found in the dictionary, it becomes NaN.
# ==========================================================

department_map = {
    "CS": "Computer Science",
    "AI": "Artificial Intelligence",
    "SE": "Software Engineering",
    "IT": "Information Technology"
}

df["Department"] = df["Department"].map(department_map)

print("\n========== AFTER map() ==========")
print(df)

# ==========================================================
# 2. Replace only one value using replace()
# Only "Computer Science" will be replaced by "CS".
# Everything else remains unchanged.
# ==========================================================

df["Department"] = df["Department"].replace(
    {"Computer Science": "CS"}
)

print("\n========== AFTER replace() ==========")
print(df)

# ==========================================================
# 3. Convert all names to lowercase using apply()
# apply() runs the given function on every value.
# ==========================================================

df["Name"] = df["Name"].apply(str.lower)

print("\n========== LOWERCASE NAMES ==========")
print(df)

# ==========================================================
# 4. Increase every CGPA by 0.2 using apply()
# lambda x: x + 0.2 means:
# Take each CGPA and add 0.2
# ==========================================================

df["CGPA"] = df["CGPA"].apply(lambda x: x + 0.2)

print("\n========== UPDATED CGPA ==========")
print(df)

# ==========================================================
# 5. Create Status column
# ==========================================================

df["Status"] = df["CGPA"].apply(
    lambda x:
        "Excellent" if x >= 3.5
        else "Good" if x >= 3.0
        else "Needs Improvement"
)

print("\n========== STATUS COLUMN ==========")
print(df)

# ==========================================================
# 6. Find the length of every student's name
# ==========================================================

df["Name_Length"] = df["Name"].apply(len)

print("\n========== NAME LENGTH ==========")
print(df)

# ==========================================================
# 7. Demonstrate an incomplete map()
# Values not found in the dictionary become NaN.
# ==========================================================

print("\n========== INCOMPLETE map() EXAMPLE ==========")

small_map = {
    "CS": "Computer Science",
    "AI": "Artificial Intelligence"
}

print(df["Department"].map(small_map))

# ==========================================================
# Final DataFrame
# ==========================================================

print("\n========== FINAL DATAFRAME ==========")
print(df)