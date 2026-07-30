import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Marks": [90, 45, 80, 60]
}

df = pd.DataFrame(data)

result = (
    df
    .query("Marks >= 60")
    .sort_values("Marks", ascending=False)
    .reset_index(drop=True)
)

print(result)
