import pandas as pd

# First DataFrame
df = pd.DataFrame({
    "Marks": [60, 70, 80, 90]
})

df["Bonus"] = df["Marks"] + 5
df["Percentage"] = df["Marks"] / 100
print(df)

print(df.query("Marks > 70"))

# Second DataFrame
df = pd.DataFrame({
    "Math": [80, 90, 70],
    "Physics": [85, 95, 75]
})
print(df)

# Add TOTAL column
df = df.eval("TOTAL = Math + Physics")
print(df)

# Use assign correctly (commas + correct column name)
df = df.assign(
    Bonus=df["TOTAL"] + 5,
    Pass=df["TOTAL"] >= 170
)

print(df)

print(df.info(memory_usage="deep"))


df=pd.DataFrame({
    "Name":["KEN","AWGUN","FEDRAEL","LORAR"],
    "Marks": [60, 70, 80, 90],
    "Bonus": [623, 730, 830, 930]
})
print(df)

df["Total"]=df["Marks"]+df["Bonus"]
print(df)
df.assign(Total=df["Total"]+df["Bonus"])
df["average"]=df["Marks"]/df["Total"]
print(df)





print(df.query("Marks>70"))


print(df.eval("Difference=Bonus-Marks"))
print(df)

