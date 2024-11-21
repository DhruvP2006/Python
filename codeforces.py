testcase = int(input())
while(testcase>0):
  n, m = map(int, input().split())
  s = input().strip()
  t = input().strip()
  possible = True
  new_s = " "
  new_t = " "
  for i in range(n-1):
    if(s[i]=="a"):
      new_s +="ab"
    else:
      new_s +="b"
      if(s==t):
        possible = True
        break
      else:
        possible = False
        s = ogs
  for j in range(m-1):
    if(t[j]=="a"):
      new_t +="ab"
    else: 
      new_t +="b"
      if(t==s):
        possible = True
        break
      else:
        possible = False
        t= ogt

  if(possible):
    print("Yes")
  else:
    print("No")
  testcase -= 1