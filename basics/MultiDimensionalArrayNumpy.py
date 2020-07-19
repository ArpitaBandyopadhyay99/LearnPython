from numpy import *

arr = array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
print("dimensional array: ", arr.ndim, ", size: ", arr.size, ", shape: ", arr.shape)

reshapeArr = arr.reshape(3, 2)
print("reshaped arr: ", reshapeArr)

convertToSingle = arr.flatten()
print("flatten: ", convertToSingle)


