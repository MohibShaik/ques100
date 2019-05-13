#Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

def squares(n):
    items={x: x*x for x in range(1,n)}
    print(items)

squares(4)