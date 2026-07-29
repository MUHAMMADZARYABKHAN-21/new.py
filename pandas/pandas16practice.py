import pandas as pd

employees = {
    "Name": [
        " ali ",
        "SARA",
        "ahMed",
        " Fatima ",
        "Hassan"
    ],

    "Email": [
        "ALI@GMAIL.COM",
        "Sara@yahoo.com",
        "ahmed@Outlook.Com",
        "fatima@gmail.com",
        " Hassan@hotmail.com "
    ],

    "Department": [
        "computer science",
        "ARTIFICIAL INTELLIGENCE",
        "Software Engineering",
        "Computer Science",
        "artificial intelligence"
    ]
}

# Create DataFrame
df = pd.DataFrame(employees)

# =====================================================
# Original Data
# =====================================================

print("========== ORIGINAL DATA ==========")
print(df)

# =====================================================
# 1. Convert Name to UPPERCASE
# =====================================================

print("\n========== NAME IN UPPERCASE ==========")
print(df["Name"].str.upper())

# =====================================================
# 2. Convert Email to lowercase
# =====================================================

print("\n========== EMAIL IN LOWERCASE ==========")
print(df["Email"].str.lower())

# =====================================================
# 3. Remove extra spaces from Name
# =====================================================

print("\n========== REMOVE SPACES ==========")
print(df["Name"].str.strip())

# =====================================================
# 4. Employees having Gmail accounts
# case=False ignores uppercase/lowercase differences
# =====================================================

print("\n========== GMAIL USERS ==========")
print(df[df["Email"].str.contains("gmail", case=False)])

# =====================================================
# 5. Employees whose names start with A
# strip() removes spaces
# upper() converts everything to uppercase
# startswith() checks the first letter
# =====================================================

print("\n========== NAMES STARTING WITH A ==========")
print(df[df["Name"].str.strip().str.upper().str.startswith("A")])

# =====================================================
# 6. Employees using Hotmail
# =====================================================

print("\n========== HOTMAIL USERS ==========")
print(
    df[
        df["Email"]
        .str.strip()
        .str.lower()
        .str.endswith("hotmail.com")
    ]
)

# =====================================================
# 7. Extract only usernames
# split('@') creates two parts:
# ['ali', 'gmail.com']
# str[0] takes the first part
# =====================================================

print("\n========== EMAIL USERNAME ==========")
print(
    df["Email"]
    .str.strip()
    .str.lower()
    .str.split("@")
    .str[0]
)

# =====================================================
# 8. Extract only domains
# str[1] takes the second part
# =====================================================

print("\n========== EMAIL DOMAIN ==========")
print(
    df["Email"]
    .str.strip()
    .str.lower()
    .str.split("@")
    .str[1]
)

# =====================================================
# 9. Replace Computer Science with CS
# title() first standardizes capitalization
# =====================================================

df["Department"] = (
    df["Department"]
    .str.title()
    .str.replace("Computer Science", "CS")
)

print("\n========== UPDATED DEPARTMENT ==========")
print(df["Department"])

# =====================================================
# 10. Clean the complete DataFrame
# =====================================================

df["Name"] = (
    df["Name"]
    .str.strip()
    .str.title()
)

df["Email"] = (
    df["Email"]
    .str.strip()
    .str.lower()
)

print("\n========== CLEAN DATAFRAME ==========")
print(df)



