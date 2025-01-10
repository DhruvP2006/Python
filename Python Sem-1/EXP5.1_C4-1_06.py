# Write a Python program that uses lambda with filter() to select even numbers and map() to square them, displaying the original, filtered, and squared lists.
num_list = [5, 12, 17, 18, 24, 32]

def evenfunc(x):
  if(x%2==0):
    return True
  else:
    return False
even_num = filter(evenfunc, num_list)

for x in even_num:
  print(x)