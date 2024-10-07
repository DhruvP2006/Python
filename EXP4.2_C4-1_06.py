#Write a Python program for a character frequency counter function that takes a list of strings from the user as input and displays the frequency of each character in the list.
def letter_frequency(a):
  a = str(a).upper()
  b = list(a)
  c = list(set(a))
  d = {}
  i = 0
  while(i < len(c)):
    d.update({c[i]:b.count(c[i])})
    i += 1
  return d
print(letter_frequency(input("Enter a String:")))