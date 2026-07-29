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

df = pd.DataFrame(employees)

print(df["Name"].str.upper())

print(df["Email"].str.lower())
print(df["Name"].str.title())

print(df["Name"].str.strip())
print(df["Department"].str.upper())
print(df["Department"].str.title())







print(df)
print(df["Email"].str.replace("gmail","xcom"))


print(df[df["Email"].str.contains("gmail", case=False)])
print(df[df["Name"].str.strip().str.startswith("a")])

print(df[df["Email"].str.lower().str.endswith("gmail.com")])


df["Name"] = df["Name"].str.strip().str.title()

df["Email"] = df["Email"].str.strip().str.lower()

df["Department"] = df["Department"].str.title()




