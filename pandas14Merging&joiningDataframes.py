import pandas as pd
#
# students = {
#     "StudentID": [101, 102, 103, 104],
#     "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
#     "Department": ["CS", "AI", "SE", "CS"]
# }
#
# df_students = pd.DataFrame(students)
#
# print(df_students)
#
#
#
# marks = {
#     "StudentID": [101,102,103,104],
#     "Math": [90,85,78,95],
#     "Physics": [88,91,80,93]
# }
#
# df_marks = pd.DataFrame(marks)
#
# print(df_marks)
#
#
#
#
# result=pd.merge(df_students, df_marks,on="StudentID")
# print(result)
#
#
#
#
#
#
#
#
#
#
#
#
#
# # inermerge
#
# students = {
#     "StudentID": [101, 102, 103, 104],
#     "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
#     "Department": ["CS", "AI", "SE", "CS"]
# }
#
# df_students = pd.DataFrame(students)
#
# print(df_students)
#
#
#
# marks = {
#     "StudentID": [1101,102,103,104],
#     "Math": [90,85,78,95],
#     "Physics": [88,91,80,93]
# }
#
# df_marks = pd.DataFrame(marks)
#
# print(df_marks)
#
# result=pd.merge(df_students,df_marks,on="StudentID",how="inner")
#
#
#
# print(result)
# # Left merge
#
#
# result=pd.merge(df_students,df_marks,on="StudentID",how="left")
#
# print(result)
#
#
#
#
#
# # Right merge
# result=pd.merge(df_students,df_marks,on="StudentID",how="right")
# # Outer merge
# print(result)
# result=pd.merge(df_students,df_marks,on="StudentID",how="outer")
#
#
#
#
# #
# #
# # merge()  → Match data using a common key (like StudentID)
# #
# # concat() → Simply stick DataFrames together
# #
# # join()   → Join DataFrames using the index
#
# result=pd.concat([df_students,df_marks,df_students],ignore_index=True)
# print(result)
#
#
#
#
#



df1 = pd.DataFrame({
    "StudentID": [101, 102, 103],
    "Name": ["Ali", "Sara", "Ahmed"],
    "Department": ["CS", "AI", "SE"]
})

print(df1)



df2 = pd.DataFrame({
    "StudentID": [104, 105, 106],
    "Name": ["Fatima", "Usman", "Hamza"],
    "Department": ["CS", "AI", "IT"]
})

print(df2)
students=pd.concat([df1,df2])
print(students)



students = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(students)



d1=pd.DataFrame(
    {

        "Students":["Ali","Sara","Noman","Romaisa"]

    })

d2=pd.DataFrame({
    "Subjects":["CS","AI","CYS","SE"]

})
print(d1)
print(d2)
D3=pd.concat([d1,d2],axis=1)

print(D3)








students = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "Department": ["CS", "AI", "SE"]
},index=[101,102,103])

print(students)





