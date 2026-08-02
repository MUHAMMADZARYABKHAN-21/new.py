# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
#
# plt.figure(figsize=(10, 6))  # dpi=100 for clearer resolution
#
# # LargeGraph with x-axis limited between 2 and 3
# plt.xlim(2, 3)
# plt.ylim(4, 6)
# plt.plot(x, y)
#
# plt.show()
# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5,6]
# y = [5,7,9,10,12,15]
#
# plt.plot(x, y)
#
# plt.xlim(2,5)
# plt.ylim(5,12)
# plt.xticks([1,2,3,4,5],["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
# plt.yticks([0,5,10,15,20],["One","Two","Three","Four","Five"])
#
# plt.show()
import matplotlib.pyplot as plt

months = ["January","February","March","April","May"]

sales = [100,150,120,180,210]

plt.figure(figsize=(9,5), dpi=120)

plt.plot(
    months,
    sales,
    marker="o",
    linewidth=3
)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.xticks(rotation=30)

plt.ylim(50,250)

plt.grid(True)

plt.show()