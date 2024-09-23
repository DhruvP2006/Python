#Write a program that takes a string as input from the user and computes the frequency of each letter. Use a variable of dictionary type to maintain the count.
a = str(input("Enter a String: ")).upper()
b = list(a)
c = list(set(a))
d = {}
i = 0
while(i < len(c)):
  d.update({c[i]:b.count(c[i])})
  i += 1
# d.pop(" ")sdc
print(d)