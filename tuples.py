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

print(r)

#iterate through dictionary
print('-'*10)
for i in range(len(r)):
    t1 = tuple(r[i].items())
    #print(t1)
    for t in t1:
        #print(t)
        print(':'.join([str(ele) for ele in t]))
    print('-'*10)

t1 = 2,3,5
t1 = 4,5,6
print(t1)
