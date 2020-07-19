# input number will print results less than or equal to the given input
# e.g input = 9, result = 0 1 1 2 3 5 8

from numpy import *


def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Invalid element")
    elif n == 0:
        print(a)
    elif n == 1:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            if c > n:
                print(c, ":", n)
                break
            else:
                print(c)


val = int(input("Enter element: "))
fib(val)
