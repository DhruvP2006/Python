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
username = input("Enter the Username")
password = input("Enter the Password")
def login(x, y):
  if(x.isalphanum() and y.isalphanum()):
