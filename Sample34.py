# pattern to print String Pattern

string=input("enter the string : ")
length=len(string)      # finds the length of given string
for row in range(length): # here no.of rows= length of given string 
    for col in range(row+1):
        print(string[col],end=" ")

    print(" ")