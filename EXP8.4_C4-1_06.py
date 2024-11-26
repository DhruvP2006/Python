# Prepare a dataset using list as Weight and height parameters for your batch students and draw a scatter plot with appropriate label and title.
import matplotlib.pyplot as plt
import numpy as np

height = np.array([170, 160, 175, 180, 165, 155, 185, 172, 168, 177, 162, 174, 158, 169, 173, 178, 160,176])
weight = np.array([60, 55, 68, 75, 58, 50, 80, 65, 62, 70, 54, 72, 52, 63, 67, 74, 56, 69])

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Weight v/s Height")
plt.scatter(height, weight)
plt.show()