import pandas as pd

# =====================================
# Create the DataFrame
# =====================================

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Hassan"],
    "Joining_Date": [
        "2024-01-15",
        "2023-11-20",
        "2022-06-05",
        "2024-03-10",
        "2021-12-01"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# =====================================
# Convert Joining_Date to datetime
# =====================================

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print("\nDataFrame After Converting to Datetime:")
print(df)

# =====================================
# Check Data Types
# =====================================

print("\nData Types:")
print(df.dtypes)

# =====================================
# Extract Date Components
# =====================================

print("\nDay:")
print(df["Joining_Date"].dt.day)

print("\nMonth:")
print(df["Joining_Date"].dt.month)

print("\nYear:")
print(df["Joining_Date"].dt.year)

print("\nWeekday Number:")
print(df["Joining_Date"].dt.weekday)

print("\nMonth Name:")
print(df["Joining_Date"].dt.month_name())

print("\nDay Name:")
print(df["Joining_Date"].dt.day_name())

# =====================================
# Current Date & Time
# =====================================

today = pd.Timestamp.today()

print("\nCurrent Timestamp:")
print(today)

# =====================================
# Employees Who Joined in March
# =====================================

print("\nEmployees Who Joined in March:")
print(df[df["Joining_Date"].dt.month == 3])

# =====================================
# Employees Who Joined After 2023-01-01
# =====================================

print("\nEmployees Who Joined After 2023-01-01:")
print(
    df[
        df["Joining_Date"] > "2023-01-01"
    ]
)

# =====================================
# Employees Who Joined in 2024
# =====================================

print("\nEmployees Who Joined in 2024:")
print(
    df[
        df["Joining_Date"].dt.year == 2024
    ]
)



