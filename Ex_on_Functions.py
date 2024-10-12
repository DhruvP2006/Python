# Write a function power(a,b) to calculate value of ’ a’ raised to’ b’ . The function receives a and b from user, finds the result and returns the result
# def power(a, b):
#   while(b>1):
#     a = a*a
#     b -= 1
#   print(a)

# power(int(input("Enter the Number: ")), int(input("Enter the power to be raised to: ")))

# W.A.P to find power of a number using recursion
# def power(base, exp):
#     if exp == 0:
#         return 1
#     else:
#         return base * power(base, exp - 1)
# print(power(int(input("Enter the Number: ")), int(input("Enter the power to be raised to: "))))

# Write a function to convert a decimal number to Binary number . The function receives the decimal number from main( ) and returns the binary number which is printed through main( ).
# def main(dec_num):
#   if(dec_num>=1):
#       main(dec_num//2)
#       print(dec_num%2, end='')
# main(int(input("Enter a Number:")))

# W.A.P to print all prime numbers between two numbers (entered by the user) by making a user-defined function.

# def prime_nums(start, end):
#     prime_list = []
#     for x in range(start, end + 1): 
#         if x < 2:  
#             continue
#         is_prime = True
#         for j in range(2, int(x**0.5) + 1):  
#             if x % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_list.append(x)  
#     return prime_list

# start = int(input("Enter the starting Number: "))
# end = int(input("Enter the ending number: "))

# prime_lst = prime_nums(start, end)
# print("Prime numbers:", prime_lst)


# Write a program to find sum of first n natural numbers using recursion. 
# def sum_n(n):
#   if n==0:
#     return 0
#   else:
#     return n + sum_n(n-1)
# print(sum_n(int(input("Enter a Number: "))))

# W.A.P to find Sum of Digits of a Number Both with and without using Recursion
a = int(input("Enter a Number: "))
a = list(a)