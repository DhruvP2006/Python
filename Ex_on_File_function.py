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

# file_name = "abc.txt"
# try:
#     with open(file_name, "r") as file:
#         text = file.read()
#         words = text.split()
#         word_count = len(words)
#         print(f"Number words in {file_name} is: {word_count}")
# except FileNotFoundError:
#     print(f"Error: The file '{file_name}' was not found.")

# Copy content from one file to another
# source_file = "abc.txt"
# destination_file = "output.txt"
# try:
#   with open(source_file, "r") as source, open(destination_file, "w") as destination:
#     destination.write(source.read())
#   print(f"Content copied from{source_file} to {destination_file}")
# except FileNotFoundError:
#   print(f"Error: The file '{source_file}' was not found.")

# Find and replace a text in a file
# file_name = "abc.txt"
# old_word = "Dhruv"
# new_word = "Krish"
# try:
#   with open(file_name, 'r') as file:
#     text = file.read()
#     update_text = text.replace(old_word, new_word)
#   with  open(file_name, 'w') as file:
#     file.write(update_text)
#   print(f"{old_word} replaced with {new_word} in {file_name}")
# except FileNotFoundError:
#   print(f"Error: The file '{file_name}' was not found.")

# print Size of png file
