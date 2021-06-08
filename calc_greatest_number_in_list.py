#!/usr/bin/python

"""
Calculate the greatest of the list of numbers provided
Usage: ./calc_greatest_number_in_list.py [9,3,4,5,6]
"""
import sys

mylist = eval(sys.argv[1])

a = mylist[0]
for i in range(1, len(mylist)):
    b = mylist[i]
    #print('a',a,'b',b)
    if not a>b:
        a = b
print("Greatest number is {}".format(a))
