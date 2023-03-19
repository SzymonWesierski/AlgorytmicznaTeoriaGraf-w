import sys

def dijkstra(n, array, start_vertex):
    vertices = []
    costs = []
    previous = []
    s = []

    # Inicjalizacja danych
    for i in range(n):
        vertices.append(i)
        costs.append(sys.maxsize)
        previous.append(-1)

    costs[start_vertex] = 0
    #print(costs)

    # Główna pętla algorytmu
    while vertices:
        # Szukanie wierzchołka o najniższym koszcie
        u = min(vertices, key=lambda vertex: costs[vertex])

        # Przenoszenie wierzchołka do zbioru S
        s.append(u)
        vertices.remove(u)

        # Aktualizacja kosztów dojścia do sąsiednich wierzchołków
        for v, cost in enumerate(array[u]):
            if cost > 0 and v in vertices and costs[v] > costs[u] + cost:
                costs[v] = costs[u] + cost
                previous[v] = u

    # Zwracanie wyniku
    return costs, previous

# Wczytywanie danych
array = []
n = 0
while True:
    try:
        a = list(map(int, input().split()))
        if a == []:
            break
        array.append(a)
        n += 1
    except EOFError:
        break
    except:
        print("BŁĄD")
        exit()

# Przetwarzanie
array_len = len(array)
max_distance = 0
periphery = []
max_distance_list = []

for i in range(array_len):
    result = dijkstra(n, array, i)
    m = max(result[0])
    if max_distance <= m:
        max_distance = m
        max_distance_list.append(result[0])

#print(max_distance_list)

for el in max_distance_list:
    while max_distance in el:
        max_distance_result = el.index(max_distance) + 1
        el[max_distance_result - 1] = -1
        if max_distance_result not in periphery:
            periphery.append(max_distance_result)

end = ""

for el in sorted(periphery):
    end += str(el) + " "

print(end[:-1])
