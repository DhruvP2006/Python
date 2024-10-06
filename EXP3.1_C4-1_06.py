#Write a program to read the numbers until -1 is encountered. Also, count the number of prime and composite numbers entered by the user.	
i = int(input("Enter the Number of Elements you want to Enter: "))
j = []
for k in range(i):
  j.append(int(input()))
for k in range(len(j)):
  if(j[k]!= -1):
    print(j[k])
  else:
    break
com_num = 0
prime_num = 0
for k in range(len(j)):
  for x in range(2, int(j[k]+1)):
    if(j[k]%x != 0 or j[k] == 2):
      prime_num += 1
      break
    else:
      com_num += 1
      break
print("Count of Prime Numbers is:", prime_num)
print("Count of Composite Numbers is: ", com_num)