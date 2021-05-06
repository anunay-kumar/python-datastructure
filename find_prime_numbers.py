"""
Find all the prime number between two numbers
"""
i=1
j=int(float(input('Finding prime number between 1 and <limit> provided by you, enter limit: ')))
for num in range(i,j):
    prime=True
    #print('num is',num)
    for divisor in range(2,num):
        #print('divisor is',divisor)
        if num%divisor == 0:
            prime=False
            break
    if prime and num !=1:
        print(num, 'is prime')
    '''
    else:
        print(num, 'is not prime')
    print("--")
    '''
