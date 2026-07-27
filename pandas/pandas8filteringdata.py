import pandas as pd

#
#
# #
# # data = {
# #     "ID": [101, 102, 103, 104, 105],
# #     "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hassan"],
# #     "Age": [20, 21, 19, 22, 20],
# #     "Math": [85, 90, 76, 95, 88],
# #     "Physics": [78, 88, 81, 91, 86],
# #     "Chemistry": [92, 84, 79, 93, 90]
# # }
# #
# # df = pd.DataFrame(data)
# #
# # print(df[df["Age"]>20])
# # print(df[df["Age"] == 20])
# #
# # print(df[df["Physics"] < 85])
# #
# # print(df[(df["Age"] > 20) & (df["Math"] > 90)])
# #
# # # Filter rows where Physics < 85 AND Math > 90
# # print(df[(df["Physics"] < 85) & (df["Math"] > 90)])
# #
# # # Same filter again (you can remove if duplicate)
# # print(df[(df["Physics"] < 85) & (df["Math"] > 90)])
# #
# # # Show only Name and Math columns for students with Math > 85
# # print(df.loc[df["Math"] > 85, ["Name", "Math"]])
# #
# # # Filter rows where Math > 90 OR Physics > 90
# # print(df[(df["Math"] > 90) | (df["Physics"] > 90)])
# #
# #
# #
# #
# #
# #
# #
# # print(pd.DataFrame(df))
# #
# # print(df[(df["Physics"] > 95) & (df["Chemistry"] < 70)])
# #
# #
# # print(df[(df["Chemistry"]==93)&(df["Physics"]==91)])
# #
# #
# #
#
#
#
#
#
#
# import pandas as pd
#
# # Sample data
# data = {
#     "ID": [1, 2, 3],
#     "Name": ["Ali", "Sara", "Ahmed"],
#     "Math": [85, 92, 78],
#     "Physics": [88, 76, 95],
#     "Chemistry": [90, 84, 80]
# }
# #
# # # Create DataFrame
# # df = pd.DataFrame(data)
# #
# # # Calculate total marks (sum of subjects)
# # df["Total Marks"] = df["Math"] + df["Physics"] + df["Chemistry"]
# #
# # # Assume each subject is out of 100 → total = 300
# # df["Percentage"] = (df["Total Marks"] / 300) * 100
# #
# # df["Chemistry+Phusics"]=df["Chemistry"]+df["Physics"]
# #
# # print(df)
# #
# # print(df[(df["Math"]>50)&(df["Physics"]>50)])
#
# print(df[(df["Chemistry"]==93)&(df["Physics"]==91)])
#
#
#





data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hassan"],
    "Age": [20, 21, 19, 22, 20],
    "Math": [85, 90, 76, 95, 88],
    "Physics": [78, 88, 81, 91, 86],
    "Chemistry": [92, 84, 79, 93, 90]
}


df=pd.DataFrame(data)
print(df.loc[df["Math"]>85,["Name","Age"]])



print(df[df["Name"].isin(["Ali","Hassan"])])


print([df[df["Age"].between(20,25)]])
print(df[df["Name"].str.contains("med")])





