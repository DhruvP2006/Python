# Write a Python function count_vowels(text) that takes a string as input and returns the count of vowels (a, e, i, o, u) in the input string, ignoring case.
a = input("Enter a string")
a = a.upper()
b = list(a)
c = list(set(b))
def remove_consonants(char):
  vowels = {'A', 'E', 'I', 'O', 'U'}
  if char in vowels:
    return True
  return False

vowels_list = list(filter(remove_consonants, b))

d = {}
for char in c:
    d[char] = vowels_list.count(char)
print(d)
