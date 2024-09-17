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
while(j<len(list2)):
  while(i< len(list1)):
    list3.append(list1[i] + list2[j])
    i+= 1
print(list3)

#Question 4: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list1)
list1.remove("")