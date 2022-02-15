def scale(matrix, row, scale):
    for i in range(len(matrix[row])):
        matrix[row][i] *= scale


def add(matrix, row, source, scale):
    for i in range(len(matrix[row])):
        matrix[row][i] += matrix[source][i] * scale


def swap(matrix, first, second):
    temp = matrix[first]
    matrix[first] = matrix[second]
    matrix[second] = temp


def firstTerm(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i


def rowOfColumn(matrix, column):
    rows = []
    for i in range(len(matrix)):
        if firstTerm(matrix[i]) == column:
            rows.append(i)
    if len(rows) == 1:
        return rows[0]


def gauss_jordan(matrix, augment=1):
    for column in range(len(matrix[0]) - augment):
        firstTermIndex = firstTerm(matrix[column])
        if firstTermIndex is None:
            continue
        scale(matrix, column, 1 / matrix[column][firstTermIndex])
        for row in range(len(matrix)):
            if row == column:
                continue
            add(matrix, row, column, -matrix[row][firstTermIndex])

    rowPlacement = 0
    for column in range(len(matrix[0]) - 1):
        row = rowOfColumn(matrix, column)
        if row is not None:
            swap(matrix, row, rowPlacement)
            rowPlacement += 1

    return matrix


def solve(mat, augment=1):
    print(
        "\n".join(
            "["
            + ", ".join(str(item) if item < 0 else " " + str(abs(item)) for item in a)
            + "]"
            for a in gauss_jordan(mat, augment)
        )
    )


# Examples below

# 3x3 has 1 solution
(
    [
        [1, 1, 0, 0],
        [2, -1, 1, 3],
        [1, -2, 2, 3],
    ]
)

# 3x3 has no solutions
(
    [
        [1, 1, 1, 10],
        [1, 1, 1, 12],
        [3, 4, -5, 8],
    ]
)

# 2x2 has 1 solution
(
    [
        [2, 1, 1],
        [-1, 1, 0],
    ]
)

# 2x2 has 1 solution
(
    [
        [4, -1, 6],
        [2, 1, 0],
    ]
)

# 4x4 has 1 solution (messy results)
(
    [
        [1, 2, 3, 4, 5],
        [3, 2, 6, -3, 2],
        [2, -4, -2, -1, 3],
        [3, 5, 7, -1, 3],
    ]
)

# 3x3 has 1 solution
(
    [
        [1, 1, 1, 9],
        [0, 1, -1, 2],
        [1, 1, 3, 0],
    ]
)

# 2x2 parallel lines, no solutions
(
    [
        [2, -1, 3],
        [2, -1, 0],
    ]
)

# 2x2 same line, many solutions
(
    [
        [4, 1, 3],
        [8, 2, 6],
    ]
)

# 2x3 not solvable with info, many solutions
(
    [
        [2, 3, 4, 5],
        [1, 2, 4, 4],
    ]
)

# 5x2 no solutions
(
    [
        [1, 4, 3],
        [2, 6, 3],
        [7, 3, 1],
        [3, 4, 5],
        [3, 4, 2],
    ]
)

# 3x3 many solution
(
    [
        [1, 4, 3],
        [-2, 0, -1],
        [0, 8, 5],
    ],
    0,
)
