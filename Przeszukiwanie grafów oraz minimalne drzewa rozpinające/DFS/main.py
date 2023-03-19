def checkingForErrors(array, array_len, start):
    if start not in range(1, array_len):
        return False

    for i in range(array_len - 1) :
        if array[i][0] != i + 1:
            return False
        for j in range(2, len(array[i])):
            if array[i][j - 1] > array[i][j]:
                return False
    return True

def dfs(array,start):
    stos = [start]
    visited = []

    while stos != []:
        vertex = stos[len(stos) - 1]
        if vertex not in visited:
            visited.append(vertex)
        neighbours = array[vertex - 1][1:]
        min_neighbour = next_vertex(neighbours,visited)
        if min_neighbour:
            stos.append(min_neighbour)
        else:
            stos.pop(len(stos) - 1)
    return visited

def next_vertex(neighbors,visited):
    try:
        min_neighbour = min(neighbors)
        if min_neighbour not in visited:
            return min_neighbour
        else:
            neighbors.remove(min_neighbour)
            return next_vertex(neighbors, visited)
    except:
        return None


array = []
while 1:
    try:
        a = input().split()
        if a == []:
            break
        for i in range(len(a)) :
            a[i] = int(a[i])
        array.append(a)
    except EOFError:
        break
    except :
        print("BŁĄD")
        exit()


array_len = len(array)
start = array[array_len - 1][0]
array.pop(array_len - 1)

if checkingForErrors(array, array_len, start):
    visited = dfs(array,start)
    result = ""
    for i in range(1, array_len):
        if i not in visited:
            print("Graf jest niespójny")
            exit()
    for c in visited:
        result += str(c) + " "
    print("Porządek DFS:", result[:-1])
    print("Graf jest spójny")
else:
    print("BŁĄD")


