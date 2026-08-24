try:
    while True:
        row, column = map(int, input().split())

        matrix = []

        for _ in range(row):
            line = list(map(int, input().split()))
            matrix.append(line)

        for j in range(column):
            result = []

            for i in range(row):
                result.append(str(matrix[i][j]))

            print(' '.join(result))

except EOFError:
    pass