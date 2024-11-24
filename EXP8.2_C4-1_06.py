# 1.	Write a Python program to draw a line using given axis values with suitable labels in the x-axis, y-axis, and title.
import matplotlib.pyplot as plt
import numpy as np

Month = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
Performance = np.array([23, 45, 38, 50, 42, 60, 55, 70, 65, 58, 75, 68])

plt.xlabel("Months")
plt.ylabel("Performance")
plt.title("Monthly Performance Trends")

plt.grid(True)
plt.plot(Month, Performance, marker="o", linestyle="-", color="r", label="Performance")
plt.show()