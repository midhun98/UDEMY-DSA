"""
Description:
Given a binary array nums, return the maximum number of consecutive 1s in the array.

Input Parameters:
    nums (List[int]): A binary array where each element is either 0 or 1.

Output:
    int: The maximum number of consecutive 1s in the array.

Example:

    Input: nums = [0, 0, 0, 0]
    Output: 0
     
    Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
    Output: 4
     
    Input: nums = [1, 1, 0, 1, 1, 1]
    Output: 3
"""

def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    # TODO: Implement this function
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        if num == 0:
            current_count = 0
    return max_count