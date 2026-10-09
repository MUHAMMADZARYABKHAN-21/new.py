import pandas as pd
df=pd.read_csv("Readfile.csv")
print(df)

print(df.head())
print(df.tail())


df.to_csv("new_students.csv", index=False)
# df.to_excel("students.xlsx", index=False)
print(df.shape)   # No parentheses


x=pd.DataFrame(df)
print(x)













