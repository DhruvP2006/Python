# Question 1: Given a Python list you should be able to display Python list in the following order
aList = [100, 200, 300, 400, 500]
aList.reverse()
print(aList)

#Question 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
i=0
list3 = []
while(i< len(list1)):
  list3.append(list1[i] + list2[i])
  i+= 1
print(list3)

# Question 3: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
i=0
j=0
list3 = []
while(j< len(list1)):
  while(i< len(list2)):
    list3.append(list1[j] + list2[i])
    i+= 1
  j += 1
  i=0
print(list3)

#Question 4: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
i=list1.count("")
while i>=1:
  list1.remove("")
  i -= 1
print(list1)

# Question 5: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
list1.insert(list1.index(20), 200)
list1.pop(list1.index(20))
print(list1)

# Question 6: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
i=list1.count(20)
while i>=1:
  list1.remove(20)
  i -= 1
print(list1)

#Question 7: Given a Python list, remove 1st occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
list1.remove(20)
print(list1)