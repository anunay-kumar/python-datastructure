#!/usr/bin/python

'''
This module calculates factorial for a list of numbers and can be executed via cmdline
Ex: ~$ list_as_commandline_param_module.py [2,3,4]
'''

import math
import sys

def compute(numbers):
    #[print(num) for num in numbers]
    return([math.factorial(int(float(num))) for num in numbers])


if __name__ == "__main__":
    numbers = eval(sys.argv[1])
    print(numbers)
    print(type(numbers))
    print(compute(numbers))
else:
    print("You are executing the function after importing: {}" .format(__name__))
