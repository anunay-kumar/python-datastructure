#!/usr/bin/python3


import sys,time

mydict = {}

def fibonacci(n):
    start = time.perf_counter()
    
    a=0
    b=1
    c=a+b
    print("-fib-index", c)
    if n == 1:
        return c
    
    for i in range(2,n):
        #Check if results exist
        if n-1 in mydict:
            print("Using previous stored calc...")
            c = mydict[n-2] + mydict[n-1]
            print("Completed operation in seconds:", time.perf_counter() - start)
            return c
        a=b
        b=c
        c=a+b 
        print("-fib-index", c)
    
    #Store results
    mydict[n-1]=b
    mydict[n]=c

    print("Saved fib calc for future use", mydict)
    print("Completed operation in seconds:", time.perf_counter() - start)
    return c

print("Fibonacci(",sys.argv[1],"):", fibonacci(int(sys.argv[1])))
print("Fibonacci(",sys.argv[2],"):", fibonacci(int(sys.argv[2])))

      
