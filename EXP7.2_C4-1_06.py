# Write a Python program to calculate the sum of all columns in a 2D NumPy array. 
import numpy as np
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
b = np.zeros(a.shape[1], dtype="int32")
for i in range(a.shape[1]):
  b[i] = a[0, i] + a[1, i]
print(b)