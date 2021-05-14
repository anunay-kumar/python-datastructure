import numpy

X = [[1,2,7],[4,5,6],[7,8,9]]
Y = [[10,11,7,1],[13,14,8,2],[16,17,9,3]]
R = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print("Calculating matrix multiplication using logic:")

for i in range(len(X)):
    print(X[i])
    
print('*')

for j in range(len(Y)):
    print(Y[j])
    
print('-' * 10)
print('=')

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            R[i][j] = R[i][j] + X[i][k] * Y[k][j]
            #print(X[i][k],'*',Y[k][j],'=',R[i][j])
    #print('---')

for r in range(len(R)):
    print(R[r])
    
print("\nVerify matrix multiplication using numpy:")
print(numpy.dot(X,Y))
