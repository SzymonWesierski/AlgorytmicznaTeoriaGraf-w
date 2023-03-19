import sys

list = matrix =[]

while True:
    try:
        a = input()
        list = a.split()
        for i in range(0, len(list)):
            list[i] = int(list[i])
        matrix.append(list)
    except EOFError:
        break

for i in range(0, len(matrix) - 1) :
    matrix[i].append(matrix[len(matrix) - 1][i])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        sys.stdout.write(str(matrix[i][j]))
        if(j<len(matrix)-1):
            sys.stdout.write(" ")
    print("")

