a = input()
b = input()
if(a == b):
 print(a, " is equal to ", b)
elif  (a<b):
  print(a, " is less than ", b)
elif(a>b):
  print(a, " is greater than ", b)
j = 0
for i in range(2, 20, 2):
  j = j + i
print(j)
j = 0
for i in range(1, 11):
  j = i*i
  print(j)
j = 0
l1 = [ 24, 20, 18, 23, 21, 16]
for i in l1:
  j = j + i
j = j/len(l1)
print(j)

for i in range(1, 21):
  if(i%2==0):
    print(i)
for i in range(1, 21):
  if(i%2!=0):
    print(i)

for i in range(9, 51):
  if(i%2 == 0):
    print(i)

for i in range(1, 5):
  for j in range(1, 5):
    print(i*j)
    if(j>4):
      break

for i in 'Dhruv Pankhania':
  if i == 'a':
    continue
  print(i)