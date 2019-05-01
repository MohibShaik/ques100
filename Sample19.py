# bank
netAmount=0
while True:

    # take user input
    str=input("enter the transction")
    
    # get the value of transaction type and amount
    # in the separated variables

    Transction=str.split()
    type=Transction[0]
    amount= int(Transction[1])

    if (type=='D'or type=='d'):
        netAmount+=amount

    elif (type=='W' or type=='w'):
        netAmount-=amount

    else:
        pass

    str=input("Want to continue (Y for yes) ? :")
    if not(str[0]=="Y" or str[0]=="y"):
        break


print("Net Amount Available :",netAmount)