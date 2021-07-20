#!/usr/bin/python3

'''
Calculate sum of N integers using dynamic programming and calculate time performance
'''

import sys,time

start_time = time.perf_counter()

mydict = {}

def sum_to_n(n):
    start_time = time.perf_counter()
    rc = 0
    for i in reversed(range(n)):
        if i+1 in mydict:
            print("Previous sum exists, not recalculating...",mydict[i+1])
            rc = mydict[i+1] + n
            print("Time taken in seconds:",time.perf_counter() - start_time)
            return rc
        else:    
            #print(i + 1)
            rc += i + 1
            mydict[n]=rc
    print(mydict)
    print("Time taken in seconds:",time.perf_counter() - start_time)
    return rc

print(sum_to_n(n = int(sys.argv[1])))
print(sum_to_n(n = int(sys.argv[2])))
