def factorial(no):
    if no == 0:
        return 1
    else:
        return no*factorial(no-1)

print("factorial of a given a number is:", factorial(8))

# l = [-10, 5, 12, -78, 6, -1, -7, 9]
# positive_nos = list(filter(lambda x: x > 0, l))
# print("Positive numbers are: ", positive_nos)

list1 = [2, 3, 4, 8, 9]
list2 = list(map(lambda x: x*x*x, list1))
print("Cube values are: ", list2)