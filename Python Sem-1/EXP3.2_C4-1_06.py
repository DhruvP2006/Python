#Write a program to check whether a number is Armstrong or not. (An Armstrong number is a number that is equal to the sum of cubes of its digits; for example, 153 = 1^3 + 5^3 + 3^3.)

i = str(input("Enter a Number: "))
j = 0
for k in i:
  k = int(k)
  j = j + k ** 3
if(int(i) == int(j)):
  print("The given Number is an Armstrong Number")
else:
  print("The given Number is not an Armstrong Number")