import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
students = [40, 25, 20, 15]

plt.pie(students,labels=labels,
        autopct="%1.1f%%")
plt.show()

plt.pie(
    students,
    labels=labels,
    colors=["gold", "skyblue", "lightgreen", "tomato"]
)


plt.show()
explode = [1, 1, 1, 1]
plt.pie(
    students,
    labels=labels,
    explode=explode
)
plt.show()
plt.pie(


    students,labels=labels,
    shadow= True

)

plt.show()
plt.pie()
import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]

students = [40, 25, 20, 15]

explode = [0.1, 0, 0, 0]

colors = ["gold", "skyblue", "lightgreen", "tomato"]

plt.figure(figsize=(7,7))

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%",
    explode=explode,
    colors=colors,
    shadow=True,
    startangle=90
)

plt.title("Students' Favorite Programming Languages")

plt.show()