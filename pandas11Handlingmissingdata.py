

# Create a dictionary containing student information.
# np.nan represents missing values in the dataset.
students = {
    "Student": ["Ali", "Sara", "Ahmed", "Fatima", "Hassan"],
    "Age": [20, 21, np.nan, 22, 20],
    "CGPA": [3.6, np.nan, 3.2, 3.9, 3.4],
    "City": ["Islamabad", "Lahore", "Karachi", np.nan, "Islamabad"]
}

# Convert the dictionary into a pandas DataFrame.
df = pd.DataFrame(students)

# Check each value in the DataFrame.
# True means the value is missing, False means it is present.
print(df.isnull())

# Count the number of missing values in each column.
print(df.isnull().sum())

# Check if each column contains at least one missing value.
# axis='rows' means the check is done down the rows for each column.
print(df.isnull().any(axis='rows'))