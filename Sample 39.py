n=int(input("Enter the no.of Rows : "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print("")