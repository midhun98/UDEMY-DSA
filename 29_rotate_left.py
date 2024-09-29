def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    for _ in range(D):
        num = ARR.pop(0)
        ARR.append(num)
    return ARR


ARR = [10, 20, 30, 40, 50]
D = 3
print(rotate_left(ARR, D))
