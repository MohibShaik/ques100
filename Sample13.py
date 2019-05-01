#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#empty list
list=[]
# taking the multiple binary values from the user
Bdigits=[x for x in input("Enter the binary digits").split(',')]

for i in Bdigits:
    a=int(i,2)
    if not a%5:
        list.append(i)
print(','.join(list))
