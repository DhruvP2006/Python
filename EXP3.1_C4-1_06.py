#Write a program to read the numbers until -1 is encountered. Also, count the number of prime and composite numbers entered by the user.	
i = [input("Enter Numbers: ")]
j = 0
flag = False
prime_num = 0
composite_num = 0

for n in i:
  print(n)
  if(n == -1):
    break

# for m in i:
#   if(m == -1):
#     break
#   for k in range(2, i):
#     if(i%k == 0):
#       flag = True
#       break
#   if(flag==True):
#     prime_num += 1
#   else:
#     composite_num += 1