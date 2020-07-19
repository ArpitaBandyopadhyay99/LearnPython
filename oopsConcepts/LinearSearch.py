nums = [2, 9, 50, 5, 10]


def linear_search(ele, nums):
    n = len(nums)
    for i in range(n):
        if ele == nums[i]:
            return i

    return -1


element = int(input("Enter: "))
pos = linear_search(element, nums)
if pos != -1:
    print(element, " found at ", pos)
else:
    print(element, " not found")


