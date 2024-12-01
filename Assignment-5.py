# Q1
import matplotlib.pyplot as plt
import numpy as np 
# x = np.array(np.random.randint(0,100 ,size=50))
# y = np.array(np.random.randint(0, 100, size=50))
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True)
# plt.plot(x, y, marker='o', linestyle= '-', mfc='#fff', color="r")
# plt.show()

# Q2
# j = 7
# week_avg_temp = []  

# while j > 0:
#     temp = np.random.randint(15, 35, size=24) 
#     avg_temp = sum(temp) / 24  
#     week_avg_temp.append(avg_temp)  
#     j -= 1

# week_avg_temp = np.array(week_avg_temp)
# x = np.array([1,2,3,4,5,6,7])
# plt.hist( week_avg_temp)
# plt.show()

# Q3
# x = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
# y = np.array([40, 48, 45, 38, 43, 38, 43, 28, 44, 39, 46, 37])
# colors = np.array(['blue', 'red','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue'])
# print(y)
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Sales Chart")
# plt.grid(True)
# plt.bar(x, y, color = colors)
# plt.show()

# Q4
# months = np.array(['Jan', 'Feb', 'Mar','Apr', 'May','Jun','Jul','Aug','Sep', 'Oct','Nov','Dec'])
# sales = np.array([12000, 15000, 13000, 17000, 14000, 17000, 18000, 17000, 17700, 18900, 20000, 21000])
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Sales Trends")
# plt.grid(True)
# plt.plot(months, sales)
# plt.show()

# Q5
# a = np.arange(1, 20, 1.25)
# b = []
# for i in a:
#   b.append(np.log(i))
# b = np.array(b)
# print(b)

# Q7
# from mypackage.math_operations import add
# print(add(4, 5))

# Q8
# plt.subplot(1, 2, 1)
# Products = np.array(["A", "B", "C", "D", "E"])
# Sales = np.array([15, 30, 25, 10, 20])
# plt.bar(Products, Sales)


# plt.subplot(1, 2, 2)
# Market_Share = np.array([10, 20, 30, 20, 20])
# labels = np.array(["A", "B", "C", "D", "E"])
# my_explode = np.array([0.2, 0, 0, 0, 0])
# plt.pie(Market_Share, labels = labels, explode = my_explode)
# plt.legend(title = "My Pie Chart")
# plt.show()

# Q9
# plt.subplot(2, 2, 1)
# x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11])
# y = np.array([99, 86, 87, 88, 100, 86, 103, 87, 94, 78])
# plt.title("Line Chart")
# plt.plot(x, y)

# plt.subplot(2,2,2)
# plt.title("Scatter Plot")
# plt.scatter(x, y)

# plt.subplot(2,2,3)
# plt.title("Histogram")
# data = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
# plt.hist(data, bins=5)

# plt.subplot(2,2,4)
# catagories = np.array(['A', 'B', 'C', 'D'])
# values = np.array([5, 7, 3, 8])
# plt.bar(catagories, values)
# plt.show()

# Q10
# values = np.array(np.arange(0, 6.283, 0.1))
# sine_values = []
# cosine_values = []
# for i in values:
#   sine_values.append(np.sin(i))
#   cosine_values.append(np.cos(i))
# sine_values = np.array(sine_values)
# cosine_values= np.array(cosine_values)
# print(sine_values, cosine_values)

# Q12 a
# a = np.array(np.random.randint(1, 20, size=(4,5)))
# print(a)
# a = a.reshape(5,4)
# print(a)

# Q12 b
# a = np.array(np.random.randint(1, 100, size=50))
# a = np.sort(a)
# print(a)
# print(a[-5:-1])

