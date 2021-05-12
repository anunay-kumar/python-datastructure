X = [[1,2,7],[4,5,6],[7,8,9]]
Y = [[10,11,7,1],[13,14,8,2],[16,17,9,3]]
R = [[0,0],[0,0],[0,0]]

for i in range(len(X)):
    print(X[i])
    
print('*')

for j in range(len(Y)):
    print(Y[j])
    
print('-' * 10)
print('=')

for i in range(len(X)):
    for j in range(len(X[i])):
        for k in range(len(Y)):
            temp = []
            print('-----')
            for m in range(len(Y[k])):
                temp.append(Y[k][m])
            print(temp)
                
                                
        
    '''
        for k in range(len(Y)):
            print(X[i][k],'*',Y[k][j])
            sum = X[i][k] * Y[k][j] + sum
        print(sum)
        sum = 0
            
     '''
