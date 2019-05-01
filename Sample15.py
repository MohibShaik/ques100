

# Write a program that accepts a sentence and calculate the number of letters and digits.

s=input("Enter the strings :")
d={"DIGITS":0,"LETTERS":0}

for i in s:
    if i.isdigit():
        d["DIGITS"]+=1
    elif i.isalpha():
        d["LETTERS"]+=1

    else :
        pass

print("letters : ", d["LETTERS"])
print("Digits : ", d["DIGITS"])