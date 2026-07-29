import pandas as pd

data=pd.read_csv("../rawdata.csv")
print(data)

df=pd.DataFrame(data)
print(df)


df["JoiningDate"]=pd.to_datetime(df["JoiningDate"])
print(df)


print(df["JoiningDate"].dt.year)
print(df["JoiningDate"].dt.month_name())
print(df["JoiningDate"].dt.day)

print(df["JoiningDate"].dt.day_name())

