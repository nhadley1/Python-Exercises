def sort (nums):
    temp = 0
    num2s = []
    for num in nums:
        for nums[num] in num2s:
            if nums[num] > nums[num + 1]:
                temp = nums[num]
                nums[num] = nums[num + 1]
                nums[num + 1] = temp
            else:
                continue

nums = [7, 3, 6, 9]

print(sort(nums))