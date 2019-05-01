
# Program to print fibonacci series of n terms using Recursion
# Here i have imported lru(Least Recently Used cache) to speed up the computing

from functools import lru_cache

@lru_cache(maxsize=1000)
#function to print Fibonacci series using recursion
def fib(n):
    if n<=1:
        return n

    else:
        return fib(n-1)+fib(n-2)


for n in range(0,10):
    print(fib(n))