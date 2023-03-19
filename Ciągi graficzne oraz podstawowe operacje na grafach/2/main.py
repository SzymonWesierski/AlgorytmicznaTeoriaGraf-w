import sys

matrix = []

while 1:
    try:
        a = input().split()
        if a == []:
            break
        matrix.append(a)
    except:
        break

for i in range(len(matrix) - 1):
    for j in range(len(matrix) - 1):
        matrix[i][j] = int(matrix[i][j])

vertex = int(matrix[len(matrix) - 1][0])

if(vertex > 0 and vertex <= len(matrix)):
    for i in range(0, len(matrix) - 1):
        if(matrix[vertex - 1][i] == 1):
            sys.stdout.write(str(i + 1) + " ")
else:
    print("BŁĄD")
