def moveZeroes(nums):
    nonZeroIndex = 0  

    for i in range(len(nums)):
        if nums[i] != 0:
            print(nums)
            nums[nonZeroIndex], nums[i] = nums[i], nums[nonZeroIndex]
            nonZeroIndex += 1

nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)
