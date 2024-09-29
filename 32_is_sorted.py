def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise
    """
    # TODO: Implement this function
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

arr = [1, 2, 8, 4, 5]
print(is_sorted(arr))