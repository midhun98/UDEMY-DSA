def rotate(matrix):
    """
    Function to rotate the matrix 90 degrees clockwise.
    :param matrix: List[List[int]] -> 2D list representing the matrix
    :return: None -> Modifies the matrix in-place
    """
    # TODO: Implement this function
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))
