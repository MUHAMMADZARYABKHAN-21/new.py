import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
#
# plt.plot(x, y)
#
# plt.title("Student Marks"
#           , fontsize= 8
#           , color= 'red',
#           fontweight= 'bold',
#           loc="left")
#
#
#
# plt.xlabel("Subjects", fontsize=8, color='red', fontweight='bold', fontstyle='normal')
# plt.ylabel("Marks", fontsize=8)

# plt.show()

#
# subjects = ["Math", "Physics", "Chemistry", "English", "CS"]
# marks = [85, 78, 92, 80, 95]
#
# plt.plot(subjects, marks)
#
# plt.title(
#     "Student Marks",
#     fontsize=18,
#     color="blue",
#     fontweight="bold"
# )
#
# plt.xlabel(
#     "Subjects",
#     fontsize=14,
#     color="green"
# )
#
# plt.ylabel(
#     "Marks",
#     fontsize=14,
#     color="red"
# )
#
# plt.show()



month=['jan','Feb','March','April']
sales=[450,550,678,800]

plt.title(
    "Sales of market",
    fontsize=18,
    color="blue",
    fontweight="bold",
    fontstyle="italic"
)
plt.xlabel(
    "Month",
    fontsize=14,
    color="green",
    

)
plt.ylabel(
    "Sales",
    fontsize=14,
    color="red"
)

plt.plot(month, sales)

plt.show()

