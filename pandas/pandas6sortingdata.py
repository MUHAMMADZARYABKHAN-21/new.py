import pandas as pd
import pandas as pd
from pandas.conftest import ascending

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hassan", "Fatima"],
    "Age": [20, 21, 19, 22, 20, 23],
    "Math": [85, 92, 76, 95, 88, 70],
    "Physics": [78, 89, 81, 91, 86, 75],
    "Department": ["CS", "AI", "CS", "AI", "CS", "SE"]
}

df = pd.DataFrame(data)

print(df)
#
# print(df.sort_values("Math"))
#
# print(df.sort_values("Physics", ascending=False))
#
#
#
#
# print(df.sort_values(["Physics","Age"]))
#
# print(df.sort_values(
#     ["Age", "Math"],
#     ascending=[True, False]
# ))
#
#



print(df.sort_index())
# print(df.sort_index())
# print(df.sort_index(ascending=False))







# sorted_df = df.sort_values("Math")
#
# print(sorted_df)




# Using the same DataFrame:
#
# Sort by Age.
# Sort by Math in descending order.
# Sort by Physics.
# Sort by Department alphabetically.
# Sort by Age and then Math.
# Sort by Department (ascending) and Math (descending).
# Sort by Name.
# Sort by the row index in descending order.
# Reset the index after sorting by Math.
# Print the final sorted DataFrame.
print(df.sort_values( ["Age"]))

print(df.sort_values(["Math",ascending=False]))
print(df.sort_values(["Department"]))

