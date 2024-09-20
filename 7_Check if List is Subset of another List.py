def is_subset(lst1, lst2):
    if len(lst1) == 0:
        return True
    if len(lst1) > len(lst2):
        return False
    length = len(lst1)
    for i in range(len(lst2) - length + 1):
        sub_li = lst2[i:length + i]
        if sub_li == lst1:
            return True
    return False


lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]
print(is_subset(lst1, lst2))