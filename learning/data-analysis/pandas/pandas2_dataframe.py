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


print("adding columns")
c["GRADE"]=['C','A','B','C','B-']

print(pd.DataFrame(data=c))
c["hobbies"]=["CRICKET","FOOTBALL","SCROLLING","NETFLIX","VOLLEYBALL"]
print(c)





# Create dictionary with student data
data = {
    "ID": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["Ali", "Ayesha", "Noman", "Sara", "John",
             "Mansoor", "Fatima", "Usman", "Morgan", "Sophia"],
    "Age": [18, 19, 20, 21, 22, 19, 20, 21, 22, 23],
    "Math": [85, 78, 92, 88, 76, 90, 84, 79, 95, 87],
    "Physics": [80, 82, 91, 85, 77, 89, 83, 81, 94, 86],
    "Chemistry": [79, 85, 88, 90, 75, 92, 80, 84, 93, 89]
}

# Convert dictionary into DataFrame
students_df = pd.DataFrame(data)

# Print the DataFrame
print(students_df)
students_df = pd.DataFrame(data)

# Calculate averages
avg_math = students_df["Math"].mean()
avg_physics = students_df["Physics"].mean()
avg_chemistry = students_df["Chemistry"].mean()

print("Average Math Score:", avg_math)
print("Average Physics Score:", avg_physics)
print("Average Chemistry Score:", avg_chemistry)










Data={"NAME":["BAKHTZADA","ABUBAKAR","NOMAN"],
      "ID":[24562,56321,6786],
      "CGPA":[3.01,3.45,3.23]

      }
print(pd.DataFrame(Data))




















