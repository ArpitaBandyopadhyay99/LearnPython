from numpy import *


def greet(val):
    return "Hello " + val


result = greet('Arpita')
print(result)


# function can return multiple values, position type arguments
def add_sub(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d


result1, result2, result3, result4 = add_sub(10, 5)
print(result1, result2, result3, result4)


# variable type arguments
def add_var(*b):
    sum = 0
    for i in b:
        sum = sum + i
    return sum


summ = add_var(2, 3, 4)
print(summ)


# default argument, if you dont pass that arg value it will assign the default value
def display(name='Yooohooo'):
    print("name: ", name)


display()  # not passed any argument
display("Chal Hatt")  # passed argument


# pass list as argument
def even_odd(ins):
    even_count = 0
    odd_count = 0
    for val in ins:
        if val % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


ins = array([1, 2, 3, 4, 5])
ec, oc = even_odd(ins)
print("List: ", ins, " Count >>> even: ", ec, " odd: ", oc)
