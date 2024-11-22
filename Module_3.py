# You are given a list of integers. Write a Python program that rearranges the list based on a specific pattern. The pattern is as follows: All even elements should come before all odd elements, and within even and odd elements, they should be sorted in ascending order.
# main_list =input("Enter a List of Numbers: ")
# main_list = main_list.split()
# even_list = []
# odd_list = []
# for x in main_list:
#   if(int(x)%2==0):
#     even_list.append(int(x))
#   else:
#     odd_list.append(int(x))
# even_list.sort()
# odd_list.sort()
# new_list = even_list+odd_list
# print(new_list)

# marks_list =input("Enter a List of Marks: ")
# marks_list = marks_list.split()
# total = 0
# for x in marks_list:
#   total += int(x) 
# avg = total/5

# if(avg>=85):
#   print("Eligible for Scholarship")
# elif(avg>=75 and avg<85):
#   print("Waiting List")
# elif(avg>=75 and avg<85):
#   print("Not Eligible")


# Write a function login(username, password) that checks if both the username and password meet certain conditions (e.g., username must be alphanumeric, password must be at least 8 characters). Display appropriate error messages if the inputs don't meet the
# username = input("Enter the Username: ")
# password = input("Enter the Password: ")
# def login(x, y):
#   if(x.isalnum()):
#     print("username must be alphanumeric")
#   if(y.isalnum()):
#     print("Password must be alphanumeric")
#   if(len(y)<8):
#     print("Password must be at least 8 characters")
# login(username, password)

# Write a program that asks the user for a range of numbers and then counts how many of those numbers are even and how many are odd.
# a = int(input("Enter a range of Number: "))
# odd_count = 0
# even_count = 0
# for i in range(a):
#   if(i%2 == 0):
#     even_count += 1
#   else:
#     odd_count += 1

# print(f"Number of even numes is {even_count}")    
# print(f"Number of odd numes is {odd_count}")

# Write a Python program that takes a list of dictionaries, where each dictionary represents a student with their name and scores in various subjects. The program should return a new dictionary where each key is a student's name, and the value is their average score across all subjects. (Using Function)

students = [ {'name': 'Arjun', 'math': 85, 'science': 90, 'english': 78}, {'name': 'Balram',
'math': 92, 'science': 88, 'english': 84}, {'name': 'Damodar', 'math': 72, 'science': 75,
'english': 80} ]

# Write a program to generate calender of a month given the start_day and the number of days in that month.

start_day = (input("Enter the Start Day: "))
Number_of_Days = int(input("Enter the Number of days"))
print("S M T W T F S")
