from numpy import *

# numpy is use to create multidimensional array

mixArr = array([1, 2, 3, 4, 'str'])
# print(mixArr)

arr = array([10, 20, 30], int)  # integer type array
# print(arr)

# linspace(startIndex,endIndex,partition) divide array in given partition
lin = linspace(1, 10, 10)
print(lin, ' data type: ', lin.dtype)

# logspace - similar to linspace only difference is it represents log values
logg = logspace(1, 5, 2)
print(logg)

# arange(startIndex,endExclusiveIndex,incrementBy) - similar to range but for array
arng = arange(1, 10, 2)
print(arng)

# zeros(numberOfElement)  - fills with zero , by default type is float
zer = zeros(5)
print(zer)

# ones(numberOfElements) - same as zero
one = ones(5, int)
print(one)
