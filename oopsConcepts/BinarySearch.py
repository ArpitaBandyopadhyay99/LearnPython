nums = [1, 3, 5, 10, 4, 12]
nums.sort()

print(nums)
ele = int(input("Enter: "))


def binary_search(ele, nums, start, end):
    mid = int((start + end)/2)
    if ele > nums[end] or ele < nums[start]:
        return -1
    elif ele == nums[mid]:
        return mid
    elif ele < nums[mid]:
        end = mid-1
        return binary_search(ele, nums, start, end)
    else:
        start = mid+1
        return binary_search(ele, nums, start, end)


index = binary_search(ele, nums, 0, len(nums)-1)
if index != -1:
    print(ele, " found at index ", index)
else:
    print(ele, " not found")