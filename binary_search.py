#!/usr/bin/python

"""
Doing binary search. Input data must be sorted.
usage: bubble_sort.py [2,7,8,11,13,15,19,24]
"""

import sys,argparse,time

parser = argparse.ArgumentParser(description='Doing binary search')
parser.add_argument("list_of_numbers",help="provide a list of numbers sorted in format [10,12,23,44,45]")
parser.add_argument("search_for",help="provide the number to search for")
parser.add_argument("-v", "--v", help="Verbose", action="store_true")
args = parser.parse_args()

# Print if verbose
def vprint(val):
    if args.v:
        print(val)


#vprint(type(args.list_of_numbers))
vprint("searching for: " + args.search_for)
vprint("provided list: " + args.list_of_numbers)
vprint("---")
#Convert to list
try:
    mylist = eval(args.list_of_numbers)
except:
    print("Provided list is incorrect")
    sys.exit(1)

#Convert to int
try:
    search_for = int(args.search_for)
except:
    print("Provided search is incorrectly formatted, provide an integer only")
    sys.exit(1)

#initialize start and end point of the binary seach slice
start = 0
end = len(mylist) - 1
found = False

while not found and start <= end:
    midpoint = (start + end) // 2
    if search_for == mylist[midpoint]:
        found = True
    elif search_for < mylist[midpoint]:
        end = midpoint - 1
    elif search_for > mylist[midpoint]:
        start = midpoint + 1
    vprint("start slice: " + str(start))
    vprint("midpoint slice: " + str(midpoint))
    vprint("end slice: " + str(end))
    vprint("----")
    #time.sleep(5)

if found:
    print("Found the search number {} at index {}".format(search_for, midpoint))
else:
    print("Failed to find search number {}".format(search_for))
