def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start

def nextGreatestLetter(letters, target):
    index = binary_search(letters, target)
    if index == len(letters):
        return letters[0]
    return letters[index]


letters = ['c', 'f', 'j']
target = 'k'
print(nextGreatestLetter(letters, target))