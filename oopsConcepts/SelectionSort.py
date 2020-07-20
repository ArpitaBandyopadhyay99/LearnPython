def sort_num(nums):
    for j in range(len(nums)):
        prevele = nums[j]
        counter = j
        ele = nums[j]
        for i in range(j+1, len(nums)):
            if ele > nums[i]:
                ele = nums[i]
                counter = i
            else:
                continue
        nums[counter] = prevele
        nums[j] = ele
    print("sorted: ", nums)


nums = [2, 1, 5, 10, 3]
print("before: ", nums)
sort_num(nums)
