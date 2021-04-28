import math,sys

print("Find the perfect squareroot of a number")
a = abs(int(float(input('Enter the number for which want to find the perfect square root: '))))
i=1
square = False
while i <= math.sqrt(a):
    if i*i == a:
        print('Found perfect square root of {} which is {}'.format(a,i))
        square = True
        break
    i += 1
if not square:
    print('Warning: Found IMperfect square root of {} which is {}'.format(a,math.sqrt(a)))
