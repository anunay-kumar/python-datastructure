import json

r = []

mylist = []
mylist.append(['anunay', '35', 'male'])
mylist.append(['Jason', '32', 'male'])
mylist.append(['Susan', '36', 'female'])

#Combine into a dictionary
mylabels = (['name', 'age', 'gender'])
for item in mylist:
    combined = zip(mylabels,item)
    #print(dict(combined))
    r.append(dict(combined))

#Convert from List -> Json -> Validated Json List
jsonO = json.loads((json.dumps(r)))
print(jsonO)
print(type(jsonO))

print(','.join([str(ele) for ele in jsonO]))
