def isPrime(n):
    if n==2 or n==3 :
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,n,2):
        if n%i==0:
            return False
    else:
         return True
res=isPrime(5)
print(res)