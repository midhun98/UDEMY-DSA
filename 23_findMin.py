def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[mid]

nums = [14, 15, 16, 17, 10, 11, 12] 
print(findMin(nums))