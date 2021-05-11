mylist = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # Input Matrix


#Initialize transpose list - calculate the transpose's rows/cols based on input matrix
transposelist = []
iCols = len(mylist)
iRows = len(mylist[0])
for row in range(iRows):
    temp = []
    for col in range(iCols):
        temp.append(0)
    transposelist.append(temp)
#print(transposelist)

#Calculate Transpose
for i in range(len(mylist)):
    #print(mylist[i])
    for j in range(len(mylist[i])):
        #print(j,i)
        transposelist[j][i] = mylist[i][j]
        #print(transposelist)
        
print('-- Matrix --')
for i in range(len(mylist)):
    print(mylist[i])
    
print('-- Transpose --')
for i in range(len(transposelist)):
    print(transposelist[i])    
