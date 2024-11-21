# Q1 Write a Python program that takes a text file as input and prints a dictionary where the keys are the words in the file and the values are the number of times each word appears in the file.
with open("abc.txt") as f:
  line = f.read
  words = line.split()
  word_dict = {}
  for i in words:
    word

