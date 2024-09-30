def generate(numRows):
    out = [[1]]
    for i in range(numRows):
        temp = [0] + out[-1] + [0]
        row = []
        for j in range(i + 1):
            row.append(temp[j] + temp[j + 1])
        out.append(row)
    return out


numRows = 3
print(generate(numRows))
