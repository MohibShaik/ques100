
string=input(" Enter the String: ")
length=len(string)
for row in range(length):
    for col in range(length):
        print(string[col],end=" ")
    print("")