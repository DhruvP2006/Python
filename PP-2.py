# 1.	Write a program that takes a list of numbers as input from the user and calculates their average. If the list is empty, raise a custom exception EmptyListError with an appropriate error message.
# class EmptyListError(Exception):
#     def __init__(self, message="No numbers entered. The list is empty."):
#         self.message = message
#         super().__init__(self.message)

# try:
#     a = str(input("Enter a List a Number(Space Separated): "))
#     if not a:
#         raise EmptyListError()
#     a = list(map(float, a.split()))
#     avg = 0
#     for i in a:
#         avg = sum(a)/len(a)
#     print(f"The average of the given numbers is {avg}")
# except EmptyListError as e:
#     print(e)


# Write a program that prompts the user for a file name and then reads and prints the contents of the requested file in the upper case.
file_name = input("Enter a File Name: ")
with open(f"{file_name}.txt", "r") as f:
    print(f.read().upper())