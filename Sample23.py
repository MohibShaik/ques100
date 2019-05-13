# Password Validation


# Password validation Using Regular Expressions.
import re

values=[]
items=[x for x in input("Enter your password : ").split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if re.search("[a-z]", p) is None:
        continue
    elif re.search("[0-9]", p) is None:
        continue
    elif re.search("[A-Z]", p) is None:
        continue
    elif re.search("[$#@]", p) is None:
        continue
    elif re.search("\s", p):
        continue
    else:
        pass
    values.append(p)
print(','.join(values))



