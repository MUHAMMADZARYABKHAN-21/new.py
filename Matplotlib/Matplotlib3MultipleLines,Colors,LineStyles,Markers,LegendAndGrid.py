# # import matplotlib.pyplot as plt
# # from sympy.printing.pretty.pretty_symbology import line_width
# #
# # # x=[1,2,3,4,5]
# # # Math=[67,89,45,67,22]
# # # Physics=[55,77,88,34,22]
# # #
# # # plt.plot(x,Math,label="Math",color='pink')
# # #
# # # plt.plot(x,Physics,label="Physics",linewidth=3,linestyle="-."
# # #          )
# # # plt.legend()
# # #
# # # plt.show()
# #
# # x=[1,2,3,4,5]
# # Math=[67,89,45,67,22]
# # Physics=[55,77,88,34,22]
# #
# # plt.plot(x,Math,label="Math",color='pink',marker="o")
# #
# # plt.plot(x,Physics,label="Physics",linewidth=3,linestyle="-"
# #          ,marker="*")
# # plt.legend()
# #
# # plt.show()
# #
# # import matplotlib.pyplot as plt
# #
# # x = [1,2,3,4,5]
# #
# # math = [80,82,85,90,95]
# # physics = [75,78,80,84,88]
# #
# # plt.plot(
# #     x,
# #     math,
# #     label="Math",
# #     color="blue",
# #     linewidth=3,
# #     linestyle="-",
# #     marker="o"
# # )
# #
# # plt.plot(
# #     x,
# #     physics,
# #     label="Physics",
# #     color="red",
# #     linewidth=2,
# #     linestyle="--",
# #     marker="s"
# # )
# #
# # plt.legend()
# # plt.grid(
# #     color="gray",
# #     linestyle="--",
# #     linewidth=0.5
# # )
# #
# # plt.show()
# #
# #
# #
# #
#
# import matplotlib.pyplot as plt
#
# Month = ["JAN","FEB","MARCH","APRIL","MAY","JUNE","JULY"]
# Sales_2025 = [4500,3456,6783,3456,6543,2367,7000]
# Sales_2026 = [5643,2223,7895,5678,9009,7865,7865]
#
# plt.plot(Month, Sales_2025,
#          label="Sales2025",
#          marker="o",
#          color="blue")
#
# plt.plot(Month, Sales_2026,
#          label="Sales2026",
#          marker="o",
#          color="red")
#
# plt.title("Sales2025 vs Sales2026")
# plt.xlabel("Month")
# plt.ylabel("Sales")
#
# plt.legend(loc="upper left")
#
# # Make grid lines clearer
# plt.grid(True, which="both", axis="both", linestyle="--", linewidth=0.7, alpha=0.7)
#
# plt.show()
#

import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

Ali=[45,76,89,56,77,88]
Noman=[67,89,77,88,99,87]
Subjects=["Physics","Chemistry","Islamiat","Biology","Calculus","Pakistanstudies"


          ]
plt.plot(Subjects,Ali,
         color="red",
         linestyle="solid",
         marker="o",label="Ali"
)
plt.plot(Subjects,Noman,
         color="blue",
         linestyle="solid",
         marker="o",
         label="Noman")

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.legend()

plt.title("Subjects marks comparison")

plt.grid()
plt.show()





