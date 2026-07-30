import pandas as pd

df = pd.DataFrame({
    "Marks": [60, 70, 80, 90]
})

bonus = []

for mark in df["Marks"]:
    bonus.append(mark + 5)

df["Bonus"] = bonus

print(df)