def matrixFromList(array, vertexNumber):
    matrix = []

    for i in range(vertexNumber):
        matrix.append([0] * vertexNumber)

    i = 0
    for v in array:
        for n in v[1:]:
            matrix[i][n - 1] += 1
        i += 1

    return matrix


def matrixSquared(matrix, vertexNumber):
    squared_matrix = []

    for c in range(vertexNumber):
        for i in range(vertexNumber):
            squared_matrix.append([])
            number = 0
            for j in range(vertexNumber):
                number += matrix[i][j] * matrix[j][c]
            squared_matrix[i].append(number)
    return squared_matrix


def diagonal(matrix, vertexNumber):
    diagonalMatrix = []

    for i in range(vertexNumber):
        diagonalMatrix.append([0] * vertexNumber)

    for i in range(vertexNumber):
        diagonalMatrix[i][i] = matrix[i][i]

    return diagonalMatrix


def formula(squared_matrix, diagonal_matrix, matrix):
    formula_list = []
    for i in range(vertexNumber):
        numbers = ""
        numbers = str(i + 1) + " "
        for j in range(vertexNumber):
            number = matrix[i][j] + squared_matrix[i][j] - diagonal_matrix[i][j]
            if number != 0 and i != j:
                numbers += str(j + 1) + " "
        formula_list.append(numbers[:-1])
    return formula_list


array = []
while True:
    try:
        a = list(map(int, input().split()))
        if a == []:
            break
        array.append(a)
    except:
        break

vertexNumber = len(array)
matrix = matrixFromList(array, vertexNumber)
squared_matrix = matrixSquared(matrix, vertexNumber)
diagonal_matrix = diagonal(matrix, vertexNumber)
formula_list = formula(squared_matrix, diagonal_matrix, matrix)

for row in formula_list:
    print(row)
