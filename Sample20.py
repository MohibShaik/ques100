#Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n

def my_gen(n):
    for i in range(n):
        if i%7==0:
            yield i

        i+=1


val=my_gen(50)
for x in val:
    print(x)
