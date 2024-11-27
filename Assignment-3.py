# Q1
# num = input()
# num = sorted(map(int, num.split()))
# for i in num:
#   if(i%2 == 0):
#     print(i)
# for i in num:
#   if(i%2 != 0):
#     print(i)

# Q2
# score = input()
# score = list(map(int, score.split(',')))
# avg_score = sum(score)/5
# if(avg_score>=85):
#   print("Average: ", avg_score)
#   print("Eligible for Scholarship")
# elif(avg_score>=75 and avg_score<85):
#   print("Average: ", avg_score)
#   print("Waiting List")
# elif(avg_score>0 and avg_score<75):
#   print("Average: ", avg_score)
#   print("Not Eligible")

# Q3
# username = input()
# password = input()
# if(len(password)<8):
#   print("Password must be at least 8 characters long")
# elif(len(username)<8):
#   print("Username must be at least 8 characters long")
# elif(username.isalnum()):
#   print("Username must be alphanumeric")
# elif(password.isalnum()):
#   print("Password must be alphanumeric")

# Q4
# start = int(input("Enter the First Number"))
# end = int(input("Enter the Second Number"))
# numbers = end - start
# even_num = numbers/2
# odd_num = numbers - even_num
# print(even_num)
# print(odd_num)

# Q5
# students = [ {'name': 'Arjun', 'math': 85, 'science': 90, 'english': 78}, {'name': 'Balram',
# 'math': 92, 'science': 88, 'english': 84}, {'name': 'Damodar', 'math': 72, 'science': 75,
# 'english': 80} ]
# results = {}
# for i in students:
#   results.update({i['name']:(i['math']+i['science']+i['english'])/3})
# print(results)

# Q6
# start_day = input("Enter the Starting Day of the Month")
# num_of_days = int(input("Enter the Number of Days"))
# print("S M T W T F S")
#   for i in range(1, num_of_days+1):
#     print(i)

# Q7
# a = int(input("Enter a Number"))
# result = 1
# for i in range(1, a+1):
#   result *= i
# print(result)

# Q8
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for a in range(5, 0, -1):
#     for b in range(1, a):
#         print("*", end=" ")
#     print()

# Q9
# x,y  = map(int, input("Enter the x and y coordinates").split(","))
# if(x==0 and y==0):
#   print("Origin")
# elif(x==0 and y!=0):
#   print("X-axis")
# elif(x!=0 and y==0):
#   print("Y-axis")
# elif(x>0 and y>0):
#   print("First Quadrant")
# elif(x<0 and y>0):
#   print("Second Quadrant")
# elif(x<0 and y<0):
#   print("Third Quadrant")
# elif(x>0 and y<0):
#   print("Fourth Quadrant")

# Q10
# while(True):
#   a = int(input("Enter a number"))
#   if(((1+(2**a))%(1+(2*a)))==0):
#     print("True")
#   else:
#     print("False")

# Q11
# count_upper = 0
# count_lower = 0
# a = input("Enter a String:" )
# for i in a:
#   if(i.isupper()):
#     count_upper += 1
#   else:
#     count_lower += 1
# print(count_upper, count_lower)

# Q12
# a = input("Enter a String")
# for i in a:
#   if(i.isdigit()):
#     print(f"{i} is a digit")
#   elif(i.islower()):
#     print(f"{i} is lowercase")
#   elif(i.isupper()):
#     print(f"{i} is uppercase")
#   else:
#     print(f"{i} Something Else")
#   match i:
#     case _ if i.isdigit():
#       print(f"{i} is a digit")
#     case _ if i.islower():
#        print(f"{i} is lowercase")
#     case _ if i.isupper():
#       print(f"{i} is uppercase")
#     case _:
#       print(f"{i} Something Else")


# Q17
# a = (input("Enter 5 integers: "))
# i = 5
# j = 1
# while(i>0 and j<=5):
#   print(f"{a[:i]}       {a[:j]}")
#   i -= 1
#   j += 1

# Q20
# population = 500000
# for i in range(0, 10):
#   population += 0.12*population
# print(population)