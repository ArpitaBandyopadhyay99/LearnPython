import math
import sys

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print(x + y)

# y = sys.argv[1]  # taking from command line
# x = int(y)
x = int(input("enter num for cube: "))  # taking from console
# result = math.pow(x, 3)
# print(int(result))

if x > 0:
    print("Positive Number", end="")  # end="" is used to print in same line
    print("....bye....")
elif x == 0:
    print("Zero")
else:
    print("Negative Number")

while x > 0:
    print("val of x: ", x)
    x -= 1

# list = [20, 'str', 1.5]  # for loop increment sequentially, here you can not assign increment value by yourself
list = "ARPITA"
for i in list:
    print(i)

for i in range(2, 8, 2):   # range(startIndex, endIndexExclusive, incrementBy)
    print(i)
