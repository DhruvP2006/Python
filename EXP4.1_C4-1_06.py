#Write a Python program using a recursive function that takes a string as input from the user and displays whether the string is Palindrome.
string = input("Enter a String:");
def check_palindrome(a):
  if(len(a)<=1):
    return True
  if(a[0]==a[-1]):
    return True
  else:
    return False
  check_palindrome(a[1:-1])
if(check_palindrome(string)):
  print("The given string is a Palindrome")
else:
  print("The given string is not a Palindrome")