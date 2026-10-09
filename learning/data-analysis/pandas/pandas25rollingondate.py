# # import pandas as pd
# #
# #
# # dates = pd.date_range("2026-01-01", periods=5)
# #
# # df = pd.DataFrame({
# #     "Sales": [100,120,130,140,150]
# # }, index=dates)
# #
# # df["Rolling"] = df["Sales"].rolling("2D").mean()
# #
# # print(df)
# # df["sum"]=df["Sales"].rolling(2).sum()
# # print(df)
# #
#
#
# import pandas as pd
#
#
# data=pd.date_range(start="2019-01-01", periods=6)
# df=pd.DataFrame({
#     "SALES":[1000,3442,5432,2200,222,2231],
#
#
# },
#     index=pd.date_range(start="2019-01-01", periods=6)
# )
# print(df)
#
# df["max"]=df["SALES"].rolling(3).max()
# print(df)
# df["min"]=df["SALES"].rolling(3).min()
# print(df)
# df["difference"] = df["SALES"].rolling(3).apply(
#     lambda x: x.max() - x.min()
# )
#
# print(df)
#
#

