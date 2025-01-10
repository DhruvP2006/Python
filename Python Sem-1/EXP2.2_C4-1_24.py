#Write a Python program to take list values as input parameters and return another list without any duplicates.
list1 = []

i = int(input("Enter the Number of Elements you want to Type: "))-1
while(i>=0):
  list1.append(input("Input parameters: "))
  i -= 1
set1 = set(list1)
list1 = list(set1)
print(list1)

