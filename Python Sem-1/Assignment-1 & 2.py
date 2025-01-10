# Q1 Write a Python program that takes a string from the user, removes all vowels from the string, extracts the remaining letters, and sorts them in alphabetical order. The program should then print the sorted letters as a list.
# a = input()
# a = a.strip("aeiou").lower()
# a = ''.join(sorted(a))
# print(a)

# Q2 Write a Python program that takes a list of words from the user, identifies and removes any words that are palindromes (words that read the same backward as forward), and then sorts the remaining words in reverse alphabetical order. The program should finally print the updated list as a tuple.
# words = input("Enter words separated by spaces: ").split()
# for i in words:
#   if(i == i[::-1]):
#     words.remove(i)
# print(words)

# Q3
# str1 = input("Enter the first String: ")
# str2 = input("Enter the Second String: ")
# str3 = str1 + str2
# str4 = ''
# for i in str3:
#   if(i.isdigit()):
#     continue
#   else:
#     str4 += i
# str4= str4.upper()

# print(str4)

# Q4
# str1 = input("Enter a String")
# str2 = ''
# for i in range(len(str1)-1, -1, -1):
#   str2 += str1[i]
# print(str2)

# Q5
# dict1 = {'a': 3, 'b': 4, 'c': 10, 'd': 5, 'e': 12}
# dict2 = {}
# for i in dict1:
#   if(dict1[i]%2==0):
#     dict2.update({i:dict1[i]})
# print(dict2)

# Q6
# list1 = ['abc', 'xyz', 'aba', '1221']
# counter = 0
# for i in list1:
#   if(len(i)>=2 and i[0]==i[-1]):
#     counter += 1
# print(counter)

# Q7
# sample_list = [12, 7, 15, 22, 10, 6]
# counter = 0
# for i in sample_list:
#   if(i>10 and i%2==0):
#     counter += 1
# print(counter)

# Q8
# Item_Name = input("Enter the Item Names (comma-separated): ").split(',')
# Item_qnty = list(map(int, input("Enter the Item Quantities (comma-separated): ").split(',')))
# Item_price = list(map(float, input("Enter the Item Prices (comma-separated): ").split(',')))

# total = []  
# print("\n********************BILL********************")
# print(f"{'Item Name':<15}{'Quantity':<10}{'Price':<10}{'Total':<10}")

# for i in range(len(Item_Name)):
#     item_total = Item_price[i] * Item_qnty[i]
#     total.append(item_total)
#     print(f"{Item_Name[i]:<15}{Item_qnty[i]:<10}{Item_price[i]:<10.2f}{item_total:<10.2f}")

# print("********************************************")
# print("Total Amount to be Paid: ", sum(total))
# print("********************************************")

# Q9
# a = list(map(int, input("Enter a list of Integers").split(" ")))
# a = sorted(set(a))
# print(a)

# Q10