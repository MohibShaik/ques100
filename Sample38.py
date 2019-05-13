num=int(input("Enter the no.of rows : "))
for i in range(num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(i+1):
        print('* ',end="")
    print()