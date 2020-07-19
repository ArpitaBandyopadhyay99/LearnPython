from numpy import *

# adding two array using numpy
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([30, 20, 20, 10, 50])
arr3 = arr1 + arr2
print("addition: ", arr3)

# add 5 to each element of array
arr4 = arr2 + 5
print("added 5: ", arr4)

# concatenate two array
conArr = concatenate([arr1, arr2])
print("two arrays: ", arr1, " ::: ", arr2, "concatenated: ", conArr)

# copy to new array, will have diff memory address
old = array([1, 2, 3, 4, 5])

# deep copy, change on new will not impact old
newDeep = old.copy()
newDeep[2] = 99
print(">>>> ", old, " new deep array: ", newDeep, "old addr: ", id(old), " new addr: ", id(newDeep))

# shallow copy, change on new will change old although they have different address
newShallow = old.view()
newShallow[2] = 100
print(">>>> ", old, " new shallow array: ", newShallow, "old addr: ", id(old), " new addr: ", id(newShallow))


# numpy means numeric operations like sqrt, log, sin, cos
arr5 = sqrt(arr2)
arr6 = log(arr2)
total = sum(arr2)
maxVal = max(arr2)
arr7 = sort(arr2)
arr8 = unique(arr2)
print("sqrt: ", arr5)
print("log: ", arr6, " sum: ", total, " max: ", maxVal)
print("sorted: ", arr7)
print("unique element: ", arr8)

