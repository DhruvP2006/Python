#Write a Python program that takes a string from the user, removes all vowels from the string, extracts the remaining letters, and sorts them in alphabetical order. The program should then print the sorted letters as a list.
# raw_string = list(input("Enter a string"))
# raw_string.sort()
# def vowel_eliminator(x):
#   if x.lower() in 'aeiou':
#     return False
#   else:
#     return True
# filtered_string = filter(vowel_eliminator, raw_string)
# for i in filtered_string:
#   print(i, end="")


# Write a Python program that takes a list of words from the user, identifies and removes any words that are palindromes (words that read the same backward as forward), and then sorts the remaining words in reverse alphabetical order. The program should finally print the updated list as a tuple.
# raw_list = input("Enter a List of Words: ").split()
# raw_list.sort()
# raw_list.reverse()
# def palindrome_filter(x):
#   x = x.lower()
#   if x == x[::-1]:
#     return False
#   else:
#     return True
# filtered_list = filter(palindrome_filter, raw_list)
# filtered_list = tuple(filtered_list)
# for x in filtered_list:
#   print(x, end=" ")

# Write a Python program that takes two strings as input from the user. The program should perform thefollowing operations:
# ● Concatenate the two strings.
# ● Remove all digits from the concatenated string.
# ● Convert the string to uppercase.
# ● Print the final result.
string_1 = input("Enter the First String")
string_2 = input("Enter the Second String")
