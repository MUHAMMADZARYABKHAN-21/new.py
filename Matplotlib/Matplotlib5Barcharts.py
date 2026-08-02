# # # import matplotlib.pyplot as plt
# # #
# # # subjects = ["Math", "Physics", "CS", "English"]
# # # marks = [90, 85, 95, 80]
# # #
# # # # plt.barh(subjects, marks),color = ["pink",
# # # # #          "red",
# # # # #          "purple",
# # # # #          "orange"],
# # # # #         width = 0.8,
# # # # #         edgecolor = "blue"
# # # #
# # # #
# # # # #
# # # plt.barh(subjects, marks)
# # #
# # #
# # #
# # # plt.title("Student Marks")
# # # plt.xlabel("Subjects")
# # # plt.ylabel("Marks")
# # #
# # # plt.show()
# #
# #
# #
# #
# # import matplotlib.pyplot as plt
# #
# #
# # products=["Laptop","PHONE","Tablet","Watch"]
# # sales=[456,777,55,444]
# # plt.bar(products,sales,
# #         color="blue",
# #         align="center",
# #             edgecolor="black",)
# #
# # plt.title("Sales by Product")
# # plt.xlabel("Product")
# # plt.ylabel("Sales")
# #
# #
# #
# # for bar in bars:
# #     height = bar.get_height()
# #     plt.text(
# #         bar.get_x() + bar.get_width()/2,
# #         height,
# #         str(height),
# #         ha="center",
# #         va="bottom"
# #     )
# #
# # plt.show()
#
# import matplotlib.pyplot as plt
#
# products = ["Laptop", "Phone", "Tablet", "Watch"]
# sales = [456, 777, 55, 444]
#
# # Save the bar objects in a variable
# bars = plt.bar(products, sales,
#                color="blue",
#                align="center",
#                edgecolor="black")
#
# plt.title("Sales by Product")
# plt.xlabel("Product")
# plt.ylabel("Sales")
#
# # Add labels on top of each bar
# for bar in bars:
#     height = bar.get_height()
#     plt.text(
#         bar.get_x() + bar.get_width()/2,  # center of the bar
#         height,                           # height position
#         str(height),                      # text = sales value
#         ha="center",                      # horizontal alignment
#         va="bottom"                       # vertical alignment
#     )
#
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Subjects
subjects = ["Math", "Physics", "CS", "English"]

# Marks of two students
marks_student1 = [90, 85, 95, 80]
marks_student2 = [70, 88, 92, 75]

# Positions for bars
x = np.arange(len(subjects))   # [0,1,2,3]
width = 0.35                   # width of each bar

# Plot bars side by side
plt.bar(x - width/2, marks_student1, width, label="Student 1", color="blue", edgecolor="black")
plt.bar(x + width/2, marks_student2, width, label="Student 2", color="red", edgecolor="black")

# Labels and title
plt.xticks(x, subjects)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Comparison of Marks: Student 1 vs Student 2")
plt.legend()

# Show chart
plt.show()

