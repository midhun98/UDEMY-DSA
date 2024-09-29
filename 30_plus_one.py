def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    # TODO: Implement this function
    num = ''
    for i in digits:
        num+=str(i)
    num = str(int(num)+1)
    out = []
    for i in num:
        out.append(int(i))
    return out