def test_range(n):
    if(n in range(3, 9)):
        print("The given number is in between 3 and 8: ")
    else:
        print("The given number is out of range")

a = input("Enter a number:")
a = int(a)
print(test_range(a))