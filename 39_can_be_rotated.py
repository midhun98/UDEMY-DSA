def can_be_rotated(mat, target):
    length = len(mat)
    for _ in range(4):
        out = []
        for i in range(length):
            row = []
            for j in range(length - 1, -1, -1):
                row.append(mat[j][i])
            out.append(row)
        mat = out
        if target == mat:
            return True
    return False


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
print(can_be_rotated(mat, target))
