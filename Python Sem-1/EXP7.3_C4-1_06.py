# Create two NumPy arrays representing monthly high and low temperatures for a year.  Calculate the monthly average temperatures, and the overall average high and low  temperatures, and identify the months with the highest and lowest average temperatures. 
import numpy as np
monthly_high = np.array([29, 32, 35, 40, 38, 34, 33 ,33, 34, 31, 29])
montly_low = np.array([15, 17, 21, 25, 28, 27, 26, 25, 24, 22, 18, 15])
monthly_avg = np.zeros(11)
for i in range(11):
  monthly_avg[i] = (monthly_high[i] + montly_low[i])/2
print(monthly_avg)