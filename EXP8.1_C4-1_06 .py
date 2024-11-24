import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8]) 
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints) 
plt.show()

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints) 
plt.show()

ypoints = np.array([3, 8, 1, 10]) 
plt.plot(ypoints, linestyle = 'dotted') 
plt.show()

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y	= np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data") 
plt.xlabel("Average Pulse") 
plt.ylabel("Calorie Burnage")
plt.show()

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y) 
plt.show()

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y	= np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid()
plt.show()

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) 
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2) 
plt.plot(x,y)

plt.show()


# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1) 
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2) 
plt.plot(x,y)

plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y) 
plt.show()


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()


y = np.array([35, 25, 25, 15])
mylabels	= ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels) 
plt.show()
