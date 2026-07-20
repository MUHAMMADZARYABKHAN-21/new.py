import pandas as pd

# Example 1: Series from a list
x = pd.Series([1, 2, 3, 4, 5, 6])
print(x)
# Output: index (0–5) on the left, values (1–6) on the right

# Example 2: Series with custom index labels
x = pd.Series([23, 55, 66, 77], index=["ali", "AYESHA", "NOMAN", "MUSHTAQ"])
print(x)

# Accessing values by index label
print(x["AYESHA"])   # 55
print(x["NOMAN"])    # 66
print(x["MUSHTAQ"])  # 77
print(x["ali"])      # 23


# Example 3: Series from a dictionary
x = {
    "STUDENTS": 5,
    "AYESHA": 6,
    "NOMAN": 7,
    "MUSHTAQ": 8
}
print(x)             # Normal dictionary
y = pd.Series(x)     # Convert dictionary to Series
print(y)             # Keys become index, values become data


# Example 4: Another dictionary with company info
c = {
    "phone": "iPhone",
    "companyname": "AppleVersion"
}
z = pd.Series(c)
print(z)
