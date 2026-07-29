import pandas as pd


Data=pd.read_csv("Employee.csv")
print(Data.head())
print(Data.describe())
print(Data.info())
print(Data.groupby(["Education","City"])["Age"].max())
print(Data.groupby("Education")["Age"].mean())




