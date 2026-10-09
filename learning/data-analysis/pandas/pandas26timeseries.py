# import pandas as pd
# import numpy as np
#
# # Show every row/column, no truncation with "..."
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", None)
#
# np.random.seed(1)
#
# data = pd.date_range(start='2019-01-01', periods=120, freq='D')
#
# df = pd.DataFrame({
#     "Sales": np.random.randint(100, 500, size=120)
# }, index=data)
#
# print(df)
#
# df["Yesterday"] = df["Sales"].shift(1)
# print(df)
#
# df["Tomorrow"] = df["Sales"].shift(-1)
# print(df)
#
# df["Difference"] = df["Sales"].diff()
# print(df)
#
# df["Percentage"] = df["Sales"].pct_change()
# print(df)
#
# monthly_sales = df["Sales"].resample("ME").sum()
# print(monthly_sales)
# yearly_sales = df["Sales"].resample("YE").sum()
# print(yearly_sales)
import pandas as pd
import numpy as np

dates = pd.date_range("2026-05-01", periods=10)

df = pd.DataFrame({
    "Sales": np.random.randint(100, 450, 10),
}, index=dates)

print("Original DataFrame")
print(df)

# 1. Yesterday's Sales
df["Yesterday"] = df["Sales"].shift(1)

# 2. Tomorrow's Sales
df["Tomorrow"] = df["Sales"].shift(-1)

# 3. Day-to-day Difference
df["Difference"] = df["Sales"].diff()

# 4. Percentage Growth
df["Growth (%)"] = df["Sales"].pct_change() * 100

# 5. 3-Day Rolling Average (time-based)
df["Rolling Avg"] = df["Sales"].rolling("3D").mean()

print("\nUpdated DataFrame")
print(df)

# 6. Weekly Sum
print("\nWeekly Sum")
print(df[["Sales"]].resample("W").sum())



