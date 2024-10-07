#Write a Python program using a recursive function that takes a string as input from the user and displays whether the string is Palindrome.
def Palindrome(j):
      if(j == j[::-1]):
        print("The given string is a Palindrome")
      else:
        print("The given string is Not a Palindrome")
a = input("Do you want to Check Palindrome? (Y/N): ")
while(a == "Y"):
  Palindrome(input("Enter a String to check if it`s a Plaindrome or not:"))
  a = input("Do you want to Check Palindrome again? (Y/N): ")