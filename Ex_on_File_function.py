# try:
#   f= open('abc.txt', 'rt')
#   print("The contents of the file are: ")
#   print(f.read())
# finally:
#   f.close()

# try:
#   f=open("abc.txt", "rt")
#   data = f.readlines()
#   for line in data:
#     word = line.split()
#     print(word)
# finally:
#   f.close()

# try:
#   f= open("abc.txt", "w")
#   f.write("My Name is Dhruv")
# finally:
#   f.close()

# try: 
#   f= open("abc.txt", "a")
#   f.write("Dhruv")
# finally:
#   f.close()

# try:
#   f = open("abc.txt", "r")
#   line = f.readline()
#   print(line)
# finally:
#   f.close()

# try:
#   f = open("abc.txt", "r")
#   line = f.readlines()
#   print(line)
# finally:
#   f.close()

# with open("file.txt", "x") as f:
#   f.write("Hello Aayush")

# import os 
# if os.path.exists("file.txt"):
#   print("True")
# os.remove("file.txt")

with open("abc.txt", "a+") as f:
  f.write("Dhruv")
  line=f.readline()


