def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    # TODO: Implement this function
    nums = tuple(set(nums))
    if len(nums) == 1 and nums[0] != 0 or 0 not in nums:
        return 0
    small = min(nums)
    large = max(nums)
    for i in range(small, large):
        if i not in nums:
            return i
    return large+1