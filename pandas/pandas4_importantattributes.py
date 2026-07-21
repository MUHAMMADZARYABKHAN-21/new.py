# import pandas as pd
#
# # Example DataFrame (replace with your own CSV load)
# df = pd.read_csv("new_students.csv")
#
# #  Commands for DataFrame inspection
#
# # print(df.shape)        # Rows and columns (tuple)
# # print(df.columns)      # Column names
# # print(df.index)        # Row indexes
# # print(df.dtypes)       # Data type of each column
# # print(df.info())       # Dataset overview
# # print(df.describe())   # Statistics for numeric columns
# # print(df.values)       # Convert to NumPy array
# # print(df.size)         # Total number of values (rows × columns)
# # print(df.ndim)         # Number of dimensions (2 for DataFrame)
# # print(df.empty)        # Check if DataFrame is empty (True/False)
# #
# #
# #
# #
# #
# #
# #
# #
#
#
# data = {
#     "Name":["Ali","Sara","Ahmed","Ayesha"],
#     "Age":[20,21,19,22],
#     "CGPA":[3.2,3.8,3.1,3.9],
#     "City":["Lahore","Islamabad","Karachi","Peshawar"]
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# #
# # print(df.head())
# # print(df.tail())
# # print(df.describe())
# # print(df.shape)
# # print(df.columns)
# # print(df.dtypes)
# # print(df.size)
# #
# # print(df.index)
# print(df.info())