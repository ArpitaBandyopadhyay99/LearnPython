from array import *

vals = array('i', [])

n = int(input("Enter size of array: "))

for i in range(n):
    a = int(input("Enter value: "))
    vals.append(a)

print(vals)

# index = int(input("Enter index of element: "))
# print(vals[index])

val = int(input("Enter search element: "))
for i in range(len(vals)):
    if vals[i] == val:
        print("index of", val, " : ", i)
        break
else:
    print(val, " not found in array")

# inbuilt function to find index
print(vals.index(val))
