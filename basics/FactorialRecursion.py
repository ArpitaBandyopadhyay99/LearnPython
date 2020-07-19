from numpy import *


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


inp = int(input("Enter: "))
print(fact(inp))
