#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j?

# using List comprehension to take multiple input values.

rowNum,colNum=[int(x) for x in input("enter the number:").split(',')]
multilist=[[0 for col in range(colNum)] for row in range(rowNum)] # list comprehension

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]=row*col #i*j

print(multilist)