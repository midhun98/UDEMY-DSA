def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        current_sum = max(current_sum, 0)
    return max_sum

arr = [5, 1, -1]
print(max_subarray_sum(arr))
