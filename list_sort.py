# take second element for sort
def takeSecond(elem):
    return elem[0]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
r=[4,3,5,7,8]

# sort list with key
print(r.sort(reverse=True))
print(r)

# sort list with key
random.sort(reverse=False, key=takeSecond)
print(random)
