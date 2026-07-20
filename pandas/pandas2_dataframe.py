import pandas as pd


data={
    "Name":["MANSOOR","ALI AHMAD","JOHN","MORGAN","KHURSHEED"],
    "Department":["COMPUTERSCIENCE","AI","DATASCIENCE","ELECTRICALENGINEERING","CYBERSECURITY"],
    "Marks":[67,66,87,90,87]






}
c=pd.DataFrame(data)
print(c)


print(c["Name"])
print(c["Department"])
print(c["Marks"])




print("/////////////////////////////////////"
      "/////////////////////////////////")

print(c[["Name","Department"]])