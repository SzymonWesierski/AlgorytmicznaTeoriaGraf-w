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
del matrix[len(matrix) - 1]

if(vertex > 0 and vertex <= len(matrix)):
    for i in range (0, len(matrix)):
        for j in range (0, len(matrix)):
            if(j == vertex - 1):
                del matrix[i][j]
                break;
    del matrix[vertex - 1]

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            sys.stdout.write(str(matrix[i][j]))
            if(j<len(matrix)-1):
                sys.stdout.write(" ")
        print("")
else:
    print("BŁĄD")
