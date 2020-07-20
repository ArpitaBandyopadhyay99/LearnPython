def sort_num(nums):
    for j in range(len(nums)):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                continue
    print("sorted: ", nums)


nums = [2, 1, 5, 4, 3]
print("before: ", nums)
sort_num(nums)
