#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Input from the user
str=input("Enter the sentence : ")

#Initialising a dictionary
d={"UPPER":0,"LOWER":0}

# Looping through the given string
for i in str:
    if i.isupper():
        d["UPPER"]+=1

    elif i.islower():
        d["LOWER"]+=1

    else:
        pass

print("Uppers : ",d["UPPER"])
print("Lowers : ",d["LOWER"])