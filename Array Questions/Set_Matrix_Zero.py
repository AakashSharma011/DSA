def set_zeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])

    col0 = 1

    # Step 1: Mark rows and columns
    for i in range(m):

        if matrix[i][0] == 0:
            col0 = 0

        for j in range(1, n):

            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 2: Fill zeros using markers
    for i in range(m - 1, -1, -1):

        for j in range(n - 1, 0, -1):

            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

        if col0 == 0:
            matrix[i][0] = 0

matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

set_zeroes(matrix)
print(matrix)
