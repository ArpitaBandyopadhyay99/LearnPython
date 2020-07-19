from array import *

# If replaced by "I" then it will not store negative values as it represents unsigned integer
# i -> signed integer, I -> unsigned integer
# l -> signed Long, L-> unsigned Long
# f -> signed float
# d -> signed double
# u -> char
sampleArr = array("i", [10, -20, 30])
sampleArr.reverse()
tupleTemp = sampleArr.buffer_info()  # current memory address and array size
print(sampleArr, " size: ", tupleTemp[1], " buffer:  ", tupleTemp)

for i in sampleArr:
    print("Iterate using array itself: ", i)

for i in range(len(sampleArr)):
    print("Another way of printing using range: ", i)

# this type of array copy has issue - original will also change
newArr = sampleArr
print(newArr)
newArr[2] = 100
print("Incorrect way of copy array -> new: ", newArr, " original: ", sampleArr)


# this array copy is perfect - original will not change
newCopyArr = array(sampleArr.typecode, (a*2 for a in sampleArr))
print(newCopyArr)
newCopyArr[1] = 999
print("Correct way of copy array new: ", newCopyArr, " original: ", sampleArr)
