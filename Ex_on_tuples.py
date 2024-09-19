#Exercise Question 1: Reverse the following tuple
aTuple = (10, 20, 30, 40, 50)
btuple = aTuple[::-1]
print(btuple)

#Exercise Question 2: Access value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

#Exercise Question 3: Create a tuple with single item 50
aTuple = (50)
print (aTuple)

#Exercise Question 4: Unpack the following tuple into 4 variables

aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple
print(a, b, c, d)

#Exercise Question 5: Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print("tuple1 = ", tuple1)
print("tuple2 = ", tuple2)

#Exercise Question 6: Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = (tuple1[3], tuple1[4])
print(tuple2)

#Exercise Question 7: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

#Exercise Question 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
list1 = list(tuple1)
k=0
while(k<=len(list1)):
  i = 0
  j = 1
  while(i<(len(list1)-1)):
    if(list1[i][1]>list1[j][1]):
      list1[i], list1[j] = list1[j], list1[i]
    i += 1
    j += 1
  k += 1
tuple1 = tuple(list1)
print(tuple1)

#Exercise Question 9: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#Exercise Question 10: Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)
print(tuple1[0] == tuple1[1] == tuple1[2] == tuple1[3])
  