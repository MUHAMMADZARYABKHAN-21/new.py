import pandas as pd

data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Sales": [100, 120, 130, 90, 150, 170, 160]
}

df = pd.DataFrame(data)

print(df)
df["Median"]=df["Sales"].rolling(3).median()
print(df)
df["Rolling_Var"] = df["Sales"].rolling(3).var()

df["Rolling_Q25"] = df["Sales"].rolling(3).quantile(0.25)
df["Custom"] = df["Sales"].rolling(3).apply(lambda x: x.max() - x.min())

print(df)