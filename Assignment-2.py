# Q1 Write a Python program that takes a string from the user, removes all vowels from the string, extracts the remaining letters, and sorts them in alphabetical order. The program should then print the sorted letters as a list.
# a = input()
# a = a.strip("aeiou").lower()
# a = ''.join(sorted(a))
# print(a)

# Q2 Write a Python program that takes a list of words from the user, identifies and removes any words that are palindromes (words that read the same backward as forward), and then sorts the remaining words in reverse alphabetical order. The program should finally print the updated list as a tuple.
words = list(input())
for i in words:
  if(i = i.reverse()):
    words.