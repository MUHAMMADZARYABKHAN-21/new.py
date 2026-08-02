import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [40, 50, 65, 80, 90]
plt.scatter(
    hours,
    marks,
    marker="^"
)
plt.scatter(
    hours,
    marks,
    alpha=0.5
)

plt.show()



hours = [1,2,3,4,5,6,7]
marks = [40,50,60,72,80,88,95]

plt.figure(figsize=(7,5))

plt.scatter(
    hours,
    marks,
    color="blue",
    s=120,
    marker="o",
    alpha=0.8
)

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.grid(True)

plt.show()




x = [1,2,3,4,5]
y = [10,20,30,40,50]

colors = ["red","blue","green","orange","purple"]

plt.scatter(
    x,
    y,
    c=colors,
    s=150
)

plt.show()

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]
values = [5,10,15,20,25]

plt.scatter(
    x,
    y,
    c=values,
    cmap="viridis",
    s=120
)

plt.colorbar()

plt.show()