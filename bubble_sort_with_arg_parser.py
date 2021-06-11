#!/usr/bin/python

"""
Doing bubble sort
usage: bubble_sort.py [5,2,78,1,3,5,90,0]
"""

import sys,argparse

parser = argparse.ArgumentParser(description='Doing bubble sort.')
parser.add_argument("list_of_numbers",help="provide a list of numbers in format [1,2,3,4,5]")
parser.add_argument("-v", "--v", help="Verbose", action="store_true")
args = parser.parse_args()

# Print if verbose
def vprint(val):
    if args.v:
        print(val)


vprint(type(args.list_of_numbers))
vprint(args.list_of_numbers)

#Convert to list
try:
    mylist = eval(args.list_of_numbers)
except:
    print("Provided list is incorrect")
    sys.exit(1)

while True:
    swap = False
    for i in range(len(mylist)-1):
        vprint(mylist[i])
        if mylist[i]>mylist[i+1]:
            #tmp = mylist[i]
            mylist[i],mylist[i+1] = mylist[i+1], mylist[i]
            #mylist[i+1] = tmp
            swap = True
    if not swap:
        break

print(mylist)
