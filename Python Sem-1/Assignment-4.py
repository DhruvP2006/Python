# Q1 Write a Python program that takes a text file as input and prints a dictionary where the keys are the words in the file and the values are the number of times each word appears in the file.
# with open("abc.txt") as f:
#   line = f.read
#   words = line.split()
#   word_dict = {}
#   for i in words:
#     word

# Q2
# try:
#     a = int(input("Enter the number of integers you want to enter: "))
#     b = []
#     while a > 0:
#         num = int(input("Enter a Number from 1-100: "))
#         if (num<0 or num>100):
#           raise AssertionError("Value should be between 1 - 100")
#         b.append(num)
#         a -= 1
# except ValueError:
#   print("Please Enter an integer")
# except AssertionError as e:
#   print(e)

# Q3
# class NegativeValueError(Exception):
#   pass
# try:
#   a = int(input("Enter a non-negative Integer"))
#   if(a<0):
#     raise NegativeValueError("Value should be Positive")
#   else:
#     print(a**0.5)
# except NegativeValueError as e:
#   print(e)

# Q4
# try:
#   index = [1, 2, 3, 4,5,6,7]
#   a = int(input("Enter an index between 0-6"))
#   print(index[a])
# except IndexError:
#   print("Please enter a number between 0-6")

# Q5
# with open('abc.txt', 'w') as f:
#   for i in range(1, 11):
#     f.write(f"{str(i)} \n")

# with open("abc.txt", 'a') as f:
#   for i in range(11, 21):
#     f.write(f"{str(i)}\n")
# with open("abc.txt", "r") as f:
#   line = f.read()
#   print(line)

# Q6
# with open("output.txt", 'w') as f:
#     input_string = input("Enter a String: ")
#     capitalize_next = False  # Flag to determine when to capitalize a character

#     for char in input_string:
#         if char == '.':
#             f.write(char)  # Write the full stop
#             capitalize_next = True  # Capitalize the next character
#         elif char.isdigit():
#             f.write(f"[{char}]")  # Write the number in brackets
#         elif capitalize_next and char.isalpha():
#             f.write(char.upper())  # Capitalize the character after a full stop
#             capitalize_next = False  # Reset the flag
#         else:
#             f.write(char)  # Write the character as is

# print("Data has been written to 'output.txt'.")

# Q7
# with open('abc.txt', 'w') as f:
#   a = input("Enter a String: ")
#   f.write(a)
# with open('abc.txt', 'a') as f:
#   b = input("Enter a String: ")
#   f.write(b)

# Q10
# class EvenNumError(Exception):
#   pass
# try:
#   line = ''
#   flag = False
#   with open("source.txt", 'r') as f:
#     line = f.readlines()
#     for i in line:
#       if(i.strip().isdigit() and i%2==0):
#         raise EvenNumError("")
#         Flag = True

#   with open("destination.txt", "w") as f:
#     f.writelines(line)
# except FileNotFoundError:
#   print("The said file is not found")
# except EvenNumError as e:
#   print("The entered Number is an Even Number")
