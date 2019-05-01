
rowNum=int(input("enter the no.of rows:")) # prompt to take input from userS
colNum=int(input("enter the no.of columns:"))
multilist = [[0 for col in range(colNum)] for row in range(rowNum)] # list comprehension

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)
