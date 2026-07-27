import pandas as pd
from pandas import DataFrame

data = {
    "ID": [101,102,103,104,105],
    "Name": ["Ali","Sara","Ahmed","Ayesha","Hassan"],
    "Age": [20,21,19,22,20],
    "Math": [85,90,76,95,88],
    "Physics": [78,88,81,91,86],
    "Chemistry": [92,84,79,93,90]
}
df: DataFrame=pd.DataFrame(data)
print(df)



print(df([df["Math"]>80])&(df["Physics"]<85)])











