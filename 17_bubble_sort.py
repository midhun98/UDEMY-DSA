"""
Code Bubble Sort

Bubble Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Bubble Sort algorithm. Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

Parameters:

    lst (List of integers): The list to be sorted.

Returns:

    A list of integers sorted in ascending order.

Example:

    Input: lst = [64, 34, 25, 12, 22, 11, 90]
    Output: [11, 12, 22, 25, 34, 64, 90]

    Input: lst = [5, 1, 4, 2, 8]
    Output: [1, 2, 4, 5, 8]
"""

def bubble_sort(lst):
    for i in range(len(lst)-1, 0 , -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


lst = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lst))
