def binary_search(lst, target):
    start = 0
    end = len(lst)

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
    return -1


lst = [11, 12, 22, 25, 34, 64, 90]
target = 11
print(binary_search(lst, target))
