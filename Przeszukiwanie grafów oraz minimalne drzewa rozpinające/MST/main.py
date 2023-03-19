def PrimsAlgorithm(matrix, numberofvertex):
    INF = 9999999
    v = numberofvertex
    selected = [0] * v
    no_edge = 0
    selected[0] = True
    sum = 0
    while no_edge < numberofvertex - 1:
        minimum = INF
        x = 0
        y = 0
        for i in range(numberofvertex):
            if selected[i]:
                for j in range(numberofvertex):
                    if (not selected[j]) and matrix[i][j]:
                        if minimum > matrix[i][j]:
                            minimum = matrix[i][j]
                            x = i
                            y = j
        sum += matrix[x][y]
        selected[y] = True
        no_edge += 1
    if selected.count(1) == numberofvertex:
        return str(sum)
    else:
        return "Graf nie jest spójny"


matrix = [input().split()]
numberofvertex = len(matrix[0])

for i in range(numberofvertex - 1):
    matrix.append(input().split())

for i in range(numberofvertex):
    for j in range(numberofvertex):
        matrix[i][j] = int(matrix[i][j])

result = PrimsAlgorithm(matrix, numberofvertex)
print(result)
