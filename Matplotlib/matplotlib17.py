# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# fig, ax = plt.subplots()
#
# x = []
# y = []
#
# def update(frame):
#
#     x.append(frame)
#     y.append(frame**2)
#
#     ax.clear()
#
#     ax.plot(
#         x,
#         y,
#         marker="o"
#     )
#
#     ax.set_title("Animated Line Plot")
#
# ani = FuncAnimation(
#     fig,
#     update,
#     frames=20,
#     interval=300
# )
#
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x = np.linspace(0,10,200)

def update(frame):

    ax.clear()

    y = np.sin(x + frame/10)

    ax.plot(x, y)

ani = FuncAnimation(
    fig,
    update,
    frames=100,
    interval=50
)

plt.show()