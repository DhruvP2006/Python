#Write a Python program using a recursive function that takes a string as input from the user and displays whether the string is Palindrome.
a = input("Do you want to Check Palindrome(Y/N): ")
def Palindrome(j):
  while(a == "Y"):
      i = input("Enter a String to check if it`s a Plaindrome or not:")
      if(j == reversed(j)):
        print("The given string is a Palindrome")
      else:
        print("The given string is Not a Palindrome")
      a = input("Do you want to Check Palindrome(Y/N): ")  

if(a == "Y"):
  