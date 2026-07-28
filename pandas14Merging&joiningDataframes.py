import pandas as pd

students = {
    "StudentID": [101, 102, 103, 104],
    "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
    "Department": ["CS", "AI", "SE", "CS"]
}

df_students = pd.DataFrame(students)

print(df_students)



marks = {
    "StudentID": [101,102,103,104],
    "Math": [90,85,78,95],
    "Physics": [88,91,80,93]
}

df_marks = pd.DataFrame(marks)

print(df_marks)




result=pd.merge(df_students, df_marks,on="StudentID")
print(result)






# inermerge

students = {
    "StudentID": [101, 102, 103, 104],
    "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
    "Department": ["CS", "AI", "SE", "CS"]
}

df_students = pd.DataFrame(students)

print(df_students)



marks = {
    "StudentID": [1101,102,103,104],
    "Math": [90,85,78,95],
    "Physics": [88,91,80,93]
}

df_marks = pd.DataFrame(marks)

print(df_marks)

result=pd.merge(df_students,df_marks,on="StudentID",how="inner")



print(result)
# Left merge


result=pd.merge(df_students,df_marks,on="StudentID",how="left")

print(result)





# Right merge
result=pd.merge(df_students,df_marks,on="StudentID",how="right")
# Outer merge
print(result)
result=pd.merge(df_students,df_marks,on="StudentID",how="outer")
















