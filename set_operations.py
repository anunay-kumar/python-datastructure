a = set([1,2,3,4,5,6,7,8])
b = set([2,3,4,5,6,7,8,9])
c = set([1,2,3,4])
d = set([5,6,7,8,9])
e = set([5,6,7,8,9])

print('Union Set a|b: ',a|b) #union
print('Intesection Set a/b: ',a.intersection(b)) #intersection
print('Subset: d<=b',d<=b) # d is subset of b
print('Proper Subset d/b: ',d<b) # d is proper subset of b
print('Subset: e<=d',e<=d) # e is subset of b
print('Proper Subset: d<b ',e<d) # e is proper subset of b
print('Superset: e>=d',e>=d) # e is superset of b
print('Proper Superset: e>d',e>d) # e is proper superset of b
