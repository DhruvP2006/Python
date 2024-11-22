import matplotlib.pyplot as plt
import numpy as np
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8 ,1, 10])
# plt.plot(ypoints, color="r", marker="o", mfc="b", mec="#010101", lw="20")
# plt.show()


# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(x1, y1)
# plt.plot(x2, y2)
# plt.show()

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'sans-serif', 'color':'blue', 'size':'20'}
font2 = {'family':'sans-serif', 'color':'red', 'size':'20'}

plt.xlabel("Average Pulse", fontdict=font1)
plt.ylabel("Calorie Burnage")
plt.title("Average Pulse v/s Calorie Burnage Graph")
plt.plot(x, y)
plt.show()

