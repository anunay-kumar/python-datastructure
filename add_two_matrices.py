X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[10,11,12],[13,14,15],[16,17,18]]
R = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range(len(X[i])):
        R[i][j] = X[i][j] + Y[i][j]

for i in range(len(X)):
    print(X[i]);

print('+')

for i in range(len(Y)):
    print(Y[i]);
print('-' * 10)
    
print('=')

for i in range(len(R)):
    print(R[i]);
