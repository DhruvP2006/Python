#1) Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
samplelist = list(sampleDict.values())
i = len(samplelist)-1
while(i>=0):
  if(samplelist[i] == 200):
    print(samplelist[i] == 200)
  i -= 1

#2) Convert the two lists given below into one dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
i = 0
newdict = {}
while(i<len(keys)):
  newdict[keys[i]] = values[i] 
  i += 1
print(newdict)

#3) Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

#4) Create a new dictionary by extracting the following keys from a given dictionary Given dictionary:
sampleDict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}
print("name:", sampleDict['name'], "salary:", sampleDict['salary'])

#5) Delete set of keys from Python Dictionary
sampleDict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}
print("city:", sampleDict['city'], "age:", sampleDict['age'])

#6) Rename key city to location in the following dictionary
sampleDict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}
sampleDict["location"] = sampleDict.pop("city")

print(sampleDict)