# Program to find factorial of number using Recursion

def factorial(num):
    if num==1:
        return 1
    else:
        return(num*factorial(num-1))


res=factorial(4)
print(res)