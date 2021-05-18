import json

dict = {}
mylist = ['a','b','c','d','e','f','g']
mylistval = [0,1,2,3,4,5,6]
mylistnewval = [12,13,14,15,16,17,18]

#Create dictionary from lists
for i in range(len(mylist)):
    dict[mylist[i]] = mylistval[i]
    #print(dict[mylist[i]])
print(dict)

#Reassign key
for i in range(len(mylist)):
    dict[mylist[i]] = mylistnewval[i]
    #print(dict[mylist[i]])
print(dict)

#Append Manipulated key
for i in range(len(mylist)):
    dict[mylist[i] + '0'] = mylistval[i]
    #print(dict[mylist[i]])
print(dict)

#Manipulate key
dict = {}
for i in range(len(mylist)):
    dict[mylist[i] + '0'] = mylistval[i]
    #print(dict[mylist[i]])
print(dict)

print("JSON:\n" + json.dumps(dict))
print("JSON:\n" + json.dumps(dict, indent=4))
