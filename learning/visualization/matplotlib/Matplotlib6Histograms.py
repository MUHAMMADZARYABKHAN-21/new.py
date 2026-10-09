# # import matplotlib.pyplot as plt
# #
# # # Student marks
# # marks = [45, 50, 55, 60, 62, 65, 70, 72, 75, 80, 82, 85, 90, 92, 95]
# #
# # # Create figure
# # plt.figure(figsize=(8, 5))
# #
# # # Histogram
# # plt.hist(
# #     marks,
# #     bins=5,
# #     color="green",
# #     edgecolor="black"
# # )
# #
# # # Title and labels
# # plt.title("Distribution of Student Marks")
# # plt.xlabel("Marks")
# # plt.ylabel("Number of Students")
# #
# # # Grid
# # plt.grid(axis="y", linestyle="--", alpha=0.7)
# #
# # plt.show()
# import matplotlib.pyplot as plt
#
# # Data
# class_A = [60, 65, 70, 75, 80, 85, 90]
# class_B = [50, 55, 60, 65, 70, 75, 80]
#
# plt.figure(figsize=(8, 5))
#
# # Class A
# plt.hist(
#     class_A,
#     bins=5,
#     alpha=0.6,
#     color="blue",
#     edgecolor="black",
#     label="Class A"
# )
#
# # Class B
# plt.hist(
#     class_B,
#     bins=5,
#     alpha=0.6,
#     color="red",
#     edgecolor="black",
#     label="Class B"
# )
#
# plt.title("Comparison of Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
#
# plt.legend()
# plt.grid(axis="y", linestyle="--", alpha=0.7)
#
# plt.show()
import matplotlib.pyplot as plt

heights = [150,152,155,158,160,162,165,167,168,170,172,175,178,180]

plt.figure(figsize=(8,5))

plt.hist(
    heights,
    bins=7,
    color="purple",
    edgecolor="black"
)

plt.title("Student Height Distribution")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()