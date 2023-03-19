def degrees(array):
    list = []
    for el in array:
        list.append(len(el) - 1)
    return list

def largestFirst(array, vertex_degrees):
    array_len = len(array)
    uncolored = []
    colored = [0] * array_len

    [uncolored.append(i) for i in range(array_len - 1,-1,-1)]

    while uncolored:
        neighbourColorList = []
        v = max(uncolored, key=lambda vertex: vertex_degrees[vertex])

        for neighbour in array[v][1:]:
            neighbourColorList.append(colored[neighbour - 1])
        color = 1

        while colored[v] == 0:
            if color not in neighbourColorList:
                colored[v] = color
                break
            else:
                color += 1

        uncolored.remove(v)

    return colored

array = []
while True:
    try:
        a = list(map(int, input().split()))
        if a == []:
            break
        array.append(a)
    except :
        break

vertex_degrees = degrees(array)
colored = largestFirst(array, vertex_degrees)

print_colored = ""

for color in colored:
    print_colored += str(color) + " "

print("Pokolorowanie wierzchołków:", print_colored[:-1])
print("Liczba chromatyczna ==",max(colored))
