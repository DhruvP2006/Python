# Write a program to find out whether a number is even or odd.
num = int(input("Enter a Number: "))
if(num%2==0):
  print("The entered number is an even number") 
else:
  print("The entered number is an odd number")

# Write a program to find out whether input alphabet is a vowel or not.
alpha = (input("Enter a character: "))
if(alpha =='a' or alpha== 'e' or alpha == 'i' or alpha == 'o' or alpha=='u'):
  print("The entered character is a vowel")
else:
  print("The entered character is not a vowel")

# In a company, an employee is paid as per the following rules-
# I. If his Basic salary is less than Rs 15000 then HRA=10% and DA=90% of
# Basic Salary respectively.
# II. If his Basic salary is equal to or above Rs 15000 then HRA=Rs1700 and DA=98% of Basic Salary respectively.
# If the employee’s salary is read through the keyboard. Write a program to find his gross salary
salary = int(input("Enter your Basic Salary: "))
if (salary<15000):
  gross_salary = 0.1*salary+0.9*salary
else:
    gross_salary = 1700+0.98*salary
print("Your gross Salary is", gross_salary)

#While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. If Quantity and price per item are read from the user. Write a program to calculate the total expense
qnt = int(input("Enter the quantity of item: "))
price = int(input("Enter price of per item: "))
if(qnt>1000):
  total = qnt*price - 0.1*qnt*price
else:
  total = qnt*price
print("The total expense is ", total)

# Given a point (x,y). WAP to find out if the point lies on the X axis or Y axis or on the origin.
x = int(input("Enter the x-cordinate: "))
y = int(input("Enter the y-cordinate: "))
if(x == 0 and y==0):
  print("The point lies on the origin")
elif(y == 0 or x ==0):
  if(y==0):
    print("The point lies on the x-axis")
  else: 
   print("The point lies on the y-axis")
else:
  print("The point lies at an arbitary point")

# Given three points (x1,y1),(x2,y2) and (x3,y3). WAP to check if all the 3 points fall on one straight line or not.
print("Enther the Following co-ordinates:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))
m1 = (x2-x1)/(y2-y1)
m2 = (x3-x2)/(y3-y2)
if(m1 == m2):
  print("All the 3 points fall on one straight line")
else:
  print("All the 3 points don`t fall on one straight line")

# WAP to check whether the triangle is isosceles, equilateral or scalene.
print("Enter the length of the three sides of a Triangle: ")
s1 = int(input("Side 1: "))
s2 = int(input("Side 2: "))
s3 = int(input("Side 3: "))
if( s1 != s2 and s1!= s3 and s2!=s3 ):
  print("The given sides are for an Scalene Triangle")
elif(s1==s2 and s1==s3 and s2==s3):
  print("The given sides are for an Equilateral Triangle")
else:
  print("The given sides are for an Isosceles Triangle")