t = int(input())
while(t>0):
  string = input()
  string2 = ""
  for i in string:
    if(i == "p"):
      string2 += "q"
    elif(i == "q"):
      string2 += "p"
    elif(i=="w"):
      string2 += "w"
  print(string2[::-1]) 
  t-= 1